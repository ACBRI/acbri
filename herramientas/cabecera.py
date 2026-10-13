#!/usr/bin/env python3
"""Genera la cabecera animada y el pie del perfil, en claro y en oscuro.

Los SVG de `assets/` no se editan a mano: salen de este guion. El texto va
convertido a trazos porque GitHub sirve cada SVG como imagen, y un SVG usado
como imagen no puede cargar tipografías de fuera.

Uso:

    python3 herramientas/cabecera.py --fuentes RUTA/A/LAS/TTF

`--fuentes` es la carpeta con `archivo-600-normal-latin.ttf` y
`plex-mono-500-normal-latin.woff2` (Archivo e IBM Plex Mono, las dos con
licencia SIL OFL 1.1). Solo hace falta fontTools; para leer el .woff2,
también brotli.

Con `--cuadro S` escribe además, en `--salida`, la cabecera detenida en el
segundo S. Sirve para revisar la animación cuadro a cuadro; esos archivos no
van al repositorio.
"""

from __future__ import annotations

import argparse
import math
import random
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

RAIZ = Path(__file__).resolve().parent.parent

# Lienzo de la cabecera, en unidades del viewBox.
ANCHO, ALTO = 1200, 340
HORIZONTE = 244
# El monograma de marca/logo.svg vive en una retícula de 64. Aquí va a 3,4
# veces, con la barra de la A (y = 41) puesta sobre el horizonte.
ESCALA = 3.4
LOGO_X = 909
LOGO_Y = HORIZONTE - 41 * ESCALA
SOL_X = LOGO_X + 46 * ESCALA
SOL_Y = LOGO_Y + 19 * ESCALA
SOL_R = 5 * ESCALA
# La barra gruesa del monograma arranca aquí; a su izquierda sigue el llano.
BARRA_X = LOGO_X + 3 * ESCALA

# Tokens del manual de marca «Sabana y candela» (docs/01 del sitio).
TEMAS = {
    "oscura": {
        "cielo": ("#121120", "#1C1A2E", "#272039", "#161528"),
        "filete": "#2E2B45",
        "tierra": "#EFE9DC",
        "tierra_suave": "#B9AE9C",
        "candela": "#F07A3B",
        "sabana": "#D9B25A",
        "sabana_tinta": "#D9B25A",
        "morichal": "#6FA57C",
        "resplandor": (
            ("0", "#F07A3B", "0.62"),
            ("0.15", "#F07A3B", "0.34"),
            ("0.40", "#B4506E", "0.15"),
            ("1", "#1C1A2E", "0"),
        ),
        "franja": ("#F07A3B", "0.34"),
        "filo": "1",
        "halo": ("#F07A3B", "0.55"),
        "estrellas": True,
    },
    "clara": {
        "cielo": ("#FAF8F1", "#F6F2E8", "#F3EFE2", "#EEE7D5"),
        "filete": "#DED7C8",
        "tierra": "#27201B",
        "tierra_suave": "#6E6156",
        "candela": "#D4581B",
        "sabana": "#C39A3F",
        "sabana_tinta": "#7A5E1F",
        "morichal": "#2F5F3A",
        "resplandor": (
            ("0", "#D4581B", "0.24"),
            ("0.18", "#D4581B", "0.12"),
            ("0.45", "#C39A3F", "0.10"),
            ("1", "#F3EFE2", "0"),
        ),
        "franja": ("#C39A3F", "0.15"),
        "filo": "0",
        "halo": ("#D4581B", "0.30"),
        "estrellas": False,
    },
}

LEMAS = {
    "en": "AI ENGINEERING · DATA · ODOO ERP",
    "es": "INGENIERÍA DE IA · DATOS · ODOO ERP",
}
DESCRIPCIONES = {
    "en": (
        "Andrés Briñez. AI engineering, data and Odoo ERP.",
        "The AB monogram standing on the horizon of the Colombian plains, "
        "with the sun inside the upper bowl of the B.",
    ),
    "es": (
        "Andrés Briñez. Ingeniería de IA, datos y Odoo ERP.",
        "El monograma AB sobre el horizonte del llano, con el sol dentro "
        "de la panza alta de la B.",
    ),
}


# --------------------------------------------------------------------------
# Texto a trazos
# --------------------------------------------------------------------------


def _n(valor: float) -> str:
    """Número corto para el SVG: un decimal, sin ceros de sobra."""
    texto = f"{valor:.1f}".rstrip("0").rstrip(".")
    return "0" if texto in ("-0", "") else texto


def _interletraje(fuente: TTFont):
    """Devuelve k(izquierda, derecha): el ajuste de pares de la tabla GPOS."""
    if "GPOS" not in fuente:
        return lambda a, b: 0
    tabla = fuente["GPOS"].table
    indices = set()
    for registro in tabla.FeatureList.FeatureRecord:
        if registro.FeatureTag == "kern":
            indices.update(registro.Feature.LookupListIndex)
    consultas = []
    for i in sorted(indices):
        consulta = tabla.LookupList.Lookup[i]
        subtablas = []
        for sub in consulta.SubTable:
            if type(sub).__name__ == "ExtensionPos":
                sub = sub.ExtSubTable
            if type(sub).__name__ == "PairPos":
                subtablas.append(sub)
        consultas.append(subtablas)

    def k(a: str, b: str) -> int:
        total = 0
        for subtablas in consultas:
            for sub in subtablas:
                cubiertos = sub.Coverage.glyphs
                if a not in cubiertos:
                    continue
                if sub.Format == 1:
                    pares = sub.PairSet[cubiertos.index(a)].PairValueRecord
                    par = next((p for p in pares if p.SecondGlyph == b), None)
                    if par is None:
                        continue
                    valor = par.Value1
                else:
                    c1 = sub.ClassDef1.classDefs.get(a, 0)
                    c2 = sub.ClassDef2.classDefs.get(b, 0)
                    valor = sub.Class1Record[c1].Class2Record[c2].Value1
                total += getattr(valor, "XAdvance", 0) or 0
                break
        return total

    return k


def trazos(
    fuente: TTFont, texto: str, cuerpo: float, x: float, y: float, espaciado: float
) -> tuple[str, float]:
    """Convierte `texto` en el atributo `d` de un path.

    `x`, `y` es el arranque de la línea base; `espaciado` va en em. Devuelve
    también el ancho que ocupó la línea.
    """
    glifos = fuente.getGlyphSet()
    mapa = fuente.getBestCmap()
    avances = fuente["hmtx"]
    escala = cuerpo / fuente["head"].unitsPerEm
    ajuste = _interletraje(fuente)
    nombres = [mapa[ord(c)] for c in texto]
    cursor = x
    partes = []
    for i, nombre in enumerate(nombres):
        pluma = SVGPathPen(glifos, ntos=_n)
        glifos[nombre].draw(TransformPen(pluma, (escala, 0, 0, -escala, cursor, y)))
        orden = pluma.getCommands()
        if orden:
            partes.append(orden)
        cursor += avances[nombre][0] * escala + espaciado * cuerpo
        if i + 1 < len(nombres):
            cursor += ajuste(nombre, nombres[i + 1]) * escala
    return "".join(partes), cursor - espaciado * cuerpo - x


# --------------------------------------------------------------------------
# Piezas del dibujo
# --------------------------------------------------------------------------


def hierba(azar: random.Random, desde: float, hasta: float, y: float, tema: dict,
           alto_max: float = 21.0, franja: float = 113.0, claro: float = 1.0
           ) -> tuple[list[list[str]], list[tuple[int, int]]]:
    """Matas de hierba sobre el horizonte, con claros entre una y otra.

    Van repartidas en franjas para que el viento las cruce de izquierda a
    derecha. Cada franja lleva dos tandas, la de las briznas altas y la de
    las bajas, que se mecen con amplitud distinta. `claro` ensancha el
    espacio entre matas.
    """
    franjas: dict[tuple[int, int], list[str]] = {}

    def brizna(px: float, alto: float, cerca: bool) -> None:
        caida = alto * azar.uniform(0.06, 0.36)
        color = tema["morichal"] if cerca else tema["sabana"]
        d = (
            f"M{_n(px)} {_n(y)}"
            f"q{_n(caida * 0.15)} {_n(-alto * 0.62)} {_n(caida)} {_n(-alto)}"
        )
        pieza = (
            f'<path d="{d}" stroke="{color}" stroke-width="{_n(azar.uniform(1.0, 1.5))}" '
            f'opacity="{azar.uniform(0.55, 0.95):.2f}"/>'
        )
        clave = (int(px // franja), 1 if alto > alto_max * 0.55 else 0)
        franjas.setdefault(clave, []).append(pieza)

    centro = desde + azar.uniform(4, 18)
    while centro < hasta - 8:
        porte = azar.uniform(0.45, 1.0)
        for _ in range(azar.randint(4, 9)):
            px = centro + azar.gauss(0, 5.5)
            if not desde <= px <= hasta:
                continue
            lejos = min(1.0, abs(px - centro) / 11)
            alto = 4 + alto_max * porte * (1 - 0.6 * lejos) * azar.uniform(0.6, 1.0)
            brizna(px, alto, cerca=azar.random() < 0.12 + 0.45 * porte * (1 - lejos))
        salto = azar.uniform(20, 58) * claro
        # Entre mata y mata, alguna brizna suelta y corta.
        suelta = centro + azar.uniform(9, salto - 6)
        if azar.random() < 0.55 and suelta < hasta:
            brizna(suelta, azar.uniform(3, 7), cerca=False)
        centro += salto
    claves = sorted(franjas)
    return [franjas[c] for c in claves], claves


def monograma(tema: dict, x: float, y: float, escala: float, animado: bool) -> str:
    """El monograma AB de marca/logo.svg, trazo a trazo, y su sol."""
    largo = ' pathLength="1"' if animado else ""
    partes = [
        ("M3 41H36", "t1"),       # el horizonte: la barra de la A
        ("M9 58L36 8", "t2"),     # la A: una diagonal que sube desde el llano
        ("M36 8V58", "t3"),       # el tallo compartido: baja desde donde llega la A
        ("M36 8H45A11 11 0 0 1 45 30H36", "t4"),   # la panza alta de la B
        ("M36 30H47A14 14 0 0 1 47 58H36", "t5"),  # la panza baja
    ]
    lineas = [
        f'<g transform="translate({_n(x)} {_n(y)}) scale({escala})" fill="none" '
        f'stroke="{tema["tierra"]}" stroke-width="7" stroke-linecap="round" '
        f'stroke-linejoin="round">'
    ]
    for d, orden in partes:
        marca = f' class="t {orden}"' if animado else ""
        lineas.append(f'<path{marca}{largo} d="{d}"/>')
    lineas.append("</g>")
    return "\n".join(lineas)


CONSTELACION = {
    # Tallos que suben desde el llano y los tramos que los unen: estructura
    # donde antes había extensión.
    "tallos": [
        "M560 244V188",
        "M664 244V134",
        "M772 244V166",
        "M852 244V100",
    ],
    "tramos": [
        "M560 188L596 152H646L664 134",
        "M664 134L698 100H852",
        "M772 166L814 124H828L852 100",
    ],
    "nodos": [(560, 188, 3.2), (664, 134, 3.6), (772, 166, 3.2), (852, 100, 4.2)],
    "cruces": [(596, 152), (646, 152), (698, 100), (814, 124)],
    # Recorridos completos de los pulsos, del llano al nodo más alto.
    "rutas": [
        "M560 244V188L596 152H646L664 134L698 100H852",
        "M772 244V166L814 124H828L852 100",
        "M664 244V134L698 100H852",
    ],
}

ESTRELLAS = [
    (48, 38, 1.1, 0.55), (131, 71, 0.8, 0.45), (212, 30, 1.0, 0.6),
    (318, 58, 0.8, 0.4), (402, 24, 1.2, 0.7), (486, 78, 0.9, 0.5),
    (538, 36, 1.0, 0.6), (612, 62, 0.8, 0.45), (706, 28, 1.3, 0.75),
    (748, 74, 0.8, 0.4), (806, 44, 1.0, 0.55), (902, 30, 0.9, 0.5),
    (958, 66, 1.1, 0.6), (1034, 34, 0.8, 0.45), (1112, 58, 1.0, 0.5),
    (1166, 96, 0.8, 0.4), (286, 104, 0.8, 0.35), (1150, 26, 1.2, 0.65),
]
# Las que titilan, con su periodo en segundos.
TITILAN = {0: 5.2, 4: 6.4, 8: 4.6, 12: 7.0, 17: 5.8}


def estilos(tema: dict, t: float | None) -> str:
    """La hoja de estilos de la cabecera.

    El estado sin animación es el dibujo terminado: cada animación de
    apertura parte de un estado oculto y llega al que ya trae el elemento.
    Con `prefers-reduced-motion` no corre ninguna.

    `t` detiene todo en ese segundo (solo para revisar cuadros).
    """
    quieto = t is not None
    paso = t or 0.0

    def r(segundos: float) -> str:
        return f"{segundos - paso:.2f}s"

    css = f"""
.cielo{{animation:encender 2.4s ease-out {r(0)} backwards}}
.sol{{animation:salir 2.4s cubic-bezier(.2,.7,.2,1) {r(0)} backwards}}
.halo{{transform-origin:{_n(SOL_X)}px {_n(SOL_Y)}px;animation:aparecer 2.4s ease-out {r(0)} backwards,respirar 8s ease-in-out {r(2.4)} infinite}}
.t{{stroke-dasharray:1 1.2;animation:trazar .9s cubic-bezier(.5,0,.2,1) backwards}}
.t1{{animation-delay:{r(0.1)}}}
.t2{{animation-delay:{r(0.35)}}}
.t3{{animation-delay:{r(1.05)}}}
.t4{{animation-delay:{r(1.35)}}}
.t5{{animation-delay:{r(1.55)}}}
.llano{{stroke-dasharray:1 1.2;animation:trazar 1.9s cubic-bezier(.4,0,.2,1) {r(0.35)} backwards}}
.nombre{{animation:subir 1s ease-out {r(0.9)} backwards}}
.lema{{animation:subir 1s ease-out {r(1.25)} backwards}}
.red path{{stroke-dasharray:1 1.2;animation:trazar 1.2s ease-out backwards}}
.red circle{{animation:aparecer .6s ease-out backwards}}
.m{{transform-origin:0 {HORIZONTE}px;animation:aparecer 1.2s ease-out {r(0.7)} backwards,mecer 7.5s ease-in-out infinite}}
.m.b{{animation-name:aparecer,mecer-alto}}
.p{{stroke-dasharray:5 300;opacity:0;animation:viajar linear infinite}}
.e{{animation:titilar ease-in-out infinite}}
@keyframes encender{{from{{opacity:0}}}}
@keyframes aparecer{{from{{opacity:0}}}}
@keyframes salir{{from{{opacity:0;transform:translateY(26px)}}}}
@keyframes subir{{from{{opacity:0;transform:translateY(9px)}}}}
@keyframes trazar{{0%{{stroke-dashoffset:1;opacity:0}}6%{{opacity:1}}100%{{stroke-dashoffset:0}}}}
@keyframes respirar{{0%,100%{{opacity:1;transform:scale(1)}}50%{{opacity:.72;transform:scale(1.07)}}}}
@keyframes mecer{{0%,100%{{transform:skewX(0)}}38%{{transform:skewX(-7deg)}}62%{{transform:skewX(-3deg)}}80%{{transform:skewX(-5.5deg)}}}}
@keyframes mecer-alto{{0%,100%{{transform:skewX(0)}}38%{{transform:skewX(-11deg)}}62%{{transform:skewX(-5deg)}}80%{{transform:skewX(-8.5deg)}}}}
@keyframes viajar{{0%{{stroke-dashoffset:5;opacity:0}}4%{{opacity:.95}}30%{{opacity:.95}}34%,100%{{stroke-dashoffset:-100;opacity:0}}}}
@keyframes titilar{{0%,100%{{opacity:1}}50%{{opacity:.2}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""
    if quieto:
        css += "*{animation-play-state:paused!important}\n"
    return css.strip()


def cabecera(idioma: str, nombre_tema: str, fuentes: dict, t: float | None = None) -> str:
    tema = TEMAS[nombre_tema]
    paso = t or 0.0

    def r(segundos: float) -> str:
        return f"{segundos - paso:.2f}s"

    titulo, descripcion = DESCRIPCIONES[idioma]
    nombre_d, _ = trazos(fuentes["archivo"], "Andrés Briñez", 60, 72, 156, -0.02)
    lema_d, _ = trazos(fuentes["plex"], LEMAS[idioma], 19, 75, 194, 0.08)

    c0, c1, c2, c3 = tema["cielo"]
    fx, fo = tema["franja"]
    hx, ho = tema["halo"]
    paradas = "".join(
        f'<stop offset="{o}" stop-color="{c}" stop-opacity="{a}"/>'
        for o, c, a in tema["resplandor"]
    )

    azar = random.Random(19)
    tandas, claves = hierba(azar, 6, BARRA_X - 14, HORIZONTE, tema)
    grupos = []
    for briznas, (franja, alta) in zip(tandas, claves):
        retardo = 2.4 + franja * 0.42 + alta * 0.18
        clase = "m b" if alta else "m"
        grupos.append(
            f'<g class="{clase}" style="animation-delay:{r(0.7)},{r(retardo)}">'
            + "".join(briznas)
            + "</g>"
        )

    red = []
    for i, d in enumerate(CONSTELACION["tallos"]):
        red.append(f'<path pathLength="1" d="{d}" style="animation-delay:{r(1.3 + i * 0.14)}"/>')
    for i, d in enumerate(CONSTELACION["tramos"]):
        red.append(f'<path pathLength="1" d="{d}" style="animation-delay:{r(1.75 + i * 0.16)}"/>')
    puntos = []
    for i, (px, py, pr) in enumerate(CONSTELACION["nodos"]):
        retardo = r(2.0 + i * 0.14)
        puntos.append(
            f'<circle cx="{px}" cy="{py}" r="{_n(pr * 2.3)}" fill="none" '
            f'stroke-opacity=".45" style="animation-delay:{retardo}"/>'
            f'<circle cx="{px}" cy="{py}" r="{pr}" fill="{tema["sabana"]}" '
            f'stroke="none" style="animation-delay:{retardo}"/>'
        )
    for i, (px, py) in enumerate(CONSTELACION["cruces"]):
        puntos.append(
            f'<circle cx="{px}" cy="{py}" r="1.7" fill="{tema["sabana"]}" '
            f'stroke="none" opacity=".8" style="animation-delay:{r(1.9 + i * 0.1)}"/>'
        )
    pulsos = []
    for d, (periodo, retardo) in zip(CONSTELACION["rutas"], ((11, 3.4), (13, 6.2), (17, 9.6))):
        pulsos.append(
            f'<path class="p" pathLength="100" d="{d}" '
            f'style="animation-duration:{periodo}s;animation-delay:{r(retardo)}"/>'
        )

    estrellas = ""
    if tema["estrellas"]:
        piezas = []
        for i, (px, py, pr, po) in enumerate(ESTRELLAS):
            if i in TITILAN:
                piezas.append(
                    f'<g opacity="{po}"><circle class="e" cx="{px}" cy="{py}" r="{pr}" '
                    f'style="animation-duration:{TITILAN[i]}s;animation-delay:{r(2.4 + i * 0.37)}"/></g>'
                )
            else:
                piezas.append(f'<circle cx="{px}" cy="{py}" r="{pr}" opacity="{po}"/>')
        estrellas = f'<g class="cielo" fill="{tema["tierra"]}">' + "".join(piezas) + "</g>"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ANCHO} {ALTO}" width="{ANCHO}" height="{ALTO}" role="img" aria-labelledby="t d">
<title id="t">{titulo}</title>
<desc id="d">{descripcion}</desc>
<style>
{estilos(tema, t)}
</style>
<defs>
<linearGradient id="c" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="{c0}"/><stop offset=".52" stop-color="{c1}"/><stop offset=".72" stop-color="{c2}"/><stop offset="1" stop-color="{c3}"/>
</linearGradient>
<radialGradient id="r" cx="{_n(SOL_X)}" cy="{_n(SOL_Y + 34)}" r="470" gradientUnits="userSpaceOnUse">{paradas}</radialGradient>
<radialGradient id="f" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{fx}" stop-opacity="{fo}"/><stop offset="1" stop-color="{fx}" stop-opacity="0"/></radialGradient>
<radialGradient id="h" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="{hx}" stop-opacity="{ho}"/><stop offset=".45" stop-color="{hx}" stop-opacity="{float(ho) * 0.35:.2f}"/><stop offset="1" stop-color="{hx}" stop-opacity="0"/></radialGradient>
<linearGradient id="l" x1="0" y1="0" x2="{_n(BARRA_X)}" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{tema["tierra"]}" stop-opacity=".22"/><stop offset=".7" stop-color="{tema["tierra"]}" stop-opacity=".7"/><stop offset="1" stop-color="{tema["tierra"]}"/></linearGradient>
<clipPath id="m"><rect width="{ANCHO}" height="{ALTO}" rx="2"/></clipPath>
</defs>
<g clip-path="url(#m)">
<rect width="{ANCHO}" height="{ALTO}" fill="url(#c)"/>
<g class="cielo">
<rect width="{ANCHO}" height="{ALTO}" fill="url(#r)"/>
<ellipse cx="{_n(SOL_X - 120)}" cy="{HORIZONTE}" rx="660" ry="46" fill="url(#f)"/>
<ellipse cx="{_n(SOL_X - 60)}" cy="{HORIZONTE}" rx="420" ry="9" fill="url(#f)" opacity="{tema["filo"]}"/>
</g>
{estrellas}
<g class="red" fill="none" stroke="{tema["sabana_tinta"]}" stroke-width="1" stroke-opacity=".42" stroke-linecap="round" stroke-linejoin="round">
{"".join(red)}
{"".join(puntos)}
</g>
<g fill="none" stroke="{tema["tierra"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">
{"".join(pulsos)}
</g>
<path class="llano" pathLength="1" d="M{_n(BARRA_X)} {HORIZONTE}H0" fill="none" stroke="url(#l)" stroke-width="2"/>
<g fill="none" stroke-linecap="round">
{chr(10).join(grupos)}
</g>
<circle class="halo" cx="{_n(SOL_X)}" cy="{_n(SOL_Y)}" r="{_n(SOL_R * 4.6)}" fill="url(#h)"/>
{monograma(tema, LOGO_X, LOGO_Y, ESCALA, True)}
<circle class="sol" cx="{_n(SOL_X)}" cy="{_n(SOL_Y)}" r="{_n(SOL_R)}" fill="{tema["candela"]}"/>
<path class="nombre" fill="{tema["tierra"]}" d="{nombre_d}"/>
<path class="lema" fill="{tema["sabana_tinta"]}" d="{lema_d}"/>
</g>
<rect x=".5" y=".5" width="{ANCHO - 1}" height="{ALTO - 1}" rx="2" fill="none" stroke="{tema["filete"]}"/>
</svg>
"""


def pie(nombre_tema: str) -> str:
    """El cierre de la página: el mismo horizonte, quieto y sin fondo."""
    tema = TEMAS[nombre_tema]
    ancho, alto, y = 1200, 84, 58
    escala = 1.1
    x0 = ancho - 64 * escala - 6
    y0 = y - 41 * escala
    barra = x0 + 3 * escala
    azar = random.Random(7)
    tandas, _ = hierba(azar, 4, barra - 6, y, tema, alto_max=12.0, claro=1.9)
    briznas = "".join("".join(tanda) for tanda in tandas)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {ancho} {alto}" width="{ancho}" height="{alto}" role="img" aria-label="Andrés Briñez">
<defs>
<linearGradient id="l" x1="0" y1="0" x2="{_n(barra)}" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{tema["tierra"]}" stop-opacity=".12"/><stop offset=".75" stop-color="{tema["tierra"]}" stop-opacity=".6"/><stop offset="1" stop-color="{tema["tierra"]}"/></linearGradient>
</defs>
<path d="M{_n(barra)} {y}H0" fill="none" stroke="url(#l)" stroke-width="1.6"/>
<g fill="none" stroke-linecap="round">{briznas}</g>
{monograma(tema, x0, y0, escala, False)}
<circle cx="{_n(x0 + 46 * escala)}" cy="{_n(y0 + 19 * escala)}" r="{_n(5 * escala)}" fill="{tema["candela"]}"/>
</svg>
"""


def main() -> None:
    analizador = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    analizador.add_argument("--fuentes", required=True, type=Path,
                            help="carpeta con las tipografías de la marca")
    analizador.add_argument("--salida", type=Path, default=RAIZ / "assets",
                            help="carpeta de destino (por defecto, assets/)")
    analizador.add_argument("--cuadro", type=float, action="append", default=[],
                            help="escribe también la cabecera detenida en ese segundo")
    opciones = analizador.parse_args()

    fuentes = {
        "archivo": TTFont(opciones.fuentes / "archivo-600-normal-latin.ttf"),
        "plex": TTFont(opciones.fuentes / "plex-mono-500-normal-latin.woff2"),
    }
    opciones.salida.mkdir(parents=True, exist_ok=True)
    escritos = []
    for tema in TEMAS:
        for idioma in LEMAS:
            if not opciones.cuadro:
                destino = opciones.salida / f"cabecera-{tema}-{idioma}.svg"
                destino.write_text(cabecera(idioma, tema, fuentes), encoding="utf-8")
                escritos.append(destino)
            for t in opciones.cuadro:
                destino = opciones.salida / f"cuadro-{tema}-{idioma}-{t:06.2f}.svg"
                destino.write_text(cabecera(idioma, tema, fuentes, t), encoding="utf-8")
                escritos.append(destino)
        if not opciones.cuadro:
            sufijo = "oscuro" if tema == "oscura" else "claro"
            destino = opciones.salida / f"pie-{sufijo}.svg"
            destino.write_text(pie(tema), encoding="utf-8")
            escritos.append(destino)
    for destino in escritos:
        print(f"{destino.stat().st_size:>7} bytes  {destino}")


if __name__ == "__main__":
    main()
