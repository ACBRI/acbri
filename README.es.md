<div align="center">

# Andrés Briñez

![Arquitectura empresarial](https://img.shields.io/badge/Arquitectura_empresarial-27201B?style=flat-square)
![Gobernanza de IA](https://img.shields.io/badge/Gobernanza_de_IA-B5430F?style=flat-square)
![Odoo](https://img.shields.io/badge/Odoo_14--20-27201B?style=flat-square)
![RAG y agentes](https://img.shields.io/badge/RAG_y_agentes-B5430F?style=flat-square)
![Quito](https://img.shields.io/badge/Quito,_Ecuador-6E6156?style=flat-square)

<br>

<a href="https://andresbrinez.com"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/html5.svg" width="36" alt="Sitio"/></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/acbri/"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/linkedin.svg" width="36" alt="LinkedIn"/></a>&nbsp;&nbsp;
<a href="mailto:acbri.19@gmail.com"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/gmail.svg" width="36" alt="Correo"/></a>&nbsp;&nbsp;
<a href="https://github.com/ACBRI"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/github.svg" width="36" alt="GitHub"/></a>

<br>

[English](README.md)  ·  **Español**

</div>

---

**Arquitecto de IA empresarial · Arquitectura empresarial y gobernanza de IA · Quito, Ecuador**

Entro en organizaciones que se quedaron pequeñas dentro de sus propios sistemas, entiendo cómo operan de verdad y diseño la arquitectura —y la gobernanza de IA— que les permite seguir creciendo sin romperse.

Dos cosas separan lo que hago de una presentación. La primera es que implemento lo que diseño: el ERP sale a producción, el proceso corre solo todas las noches, el modelo responde con los documentos de la propia empresa. La segunda es que dejo las decisiones escritas, de una forma que alguien pueda auditar un año después.

---

<br>

## En qué estoy ahora

**Capacidad de IA empresarial para una multinacional de consumo masivo** (a través de PENTA Digital Lab). Arquitectura de solución para una transformación comercial de punta a punta: levantamiento del estado actual, análisis de brechas, modelo objetivo, integración de sistemas, y la IA generativa y los agentes dentro de los procesos del negocio, no al lado.

**Una consultoría que opera con los sistemas que vende.** [andresbrinez.com](https://andresbrinez.com) es mi propio Odoo 19 Community, autohospedado, sirviendo desde un solo sistema el sitio público, el portal de cliente, el CRM, las cotizaciones y la facturación. Integración continua en máquinas propias, despliegue con una orden, respaldos probados de extremo a extremo. Cada producto que vendo se probó primero contra mi propio negocio.

---

<br>

## Lo que he construido

**Arquitectura empresarial y ERP**

- Arquitectura de una transformación comercial de punta a punta para una multinacional de consumo masivo: modelo objetivo, análisis de brechas, integración de sistemas
- Facturación electrónica del SRI para Odoo 19: ocho módulos portados desde la línea 18.0 de la OCA —facturas, notas de crédito y débito, retenciones, liquidaciones de compra, guías de remisión, el ATS y la recepción de comprobantes de proveedor— con 314 pruebas automáticas e integración continua
- Retención en la fuente de Colombia para Odoo 19: retenciones, actividades económicas CIIU y el puente con la factura electrónica, para que cada retención declare su tributo en el XML
- Contabilidad de dos países en producción (Ecuador y Colombia), con un clasificador de gastos que consulta la actividad económica registrada del proveedor antes de preguntarle a un modelo
- Radar de actualización de Odoo: recorre un código propio y dice qué se rompe en la siguiente versión, con archivo y línea, en el orden que conviene arreglarlo

**IA en producción**

- Respuestas sobre los documentos y los datos del ERP de una empresa, construido como manda la literatura de producción: recuperación híbrida desde el primer día, reordenamiento de resultados, un umbral de fidelidad medido y un conjunto de preguntas reales con su respuesta escrita
- Un proceso de IA generativa para transcripción y minutas de reuniones (Whisper con separación de hablantes, y después limpieza)
- Reunia — plataforma de inteligencia de reuniones, en construcción
- Flujos con agentes que convierten la transcripción de una reunión en historias de usuario

**Modelado y documentación**

- C4 con Structurizr, BPMN 2.0, ArchiMate y registros de decisiones de arquitectura, en organizaciones que no tenían ninguno
- Documentación como código: versionada, revisable y todavía cierta cuando el consultor se va

No son proyectos de laboratorio. Son sistemas que alguien usa hoy para tomar decisiones que cuestan dinero.

---

<br>

## Lo que se puede comprobar desde fuera

La mayor parte de mi trabajo vive en repositorios privados, por la razón evidente. Lo que sí se puede verificar:

- **[andresbrinez.com](https://andresbrinez.com)** — el sitio es la prueba: corre sobre la pila que describe, en dos idiomas y con los precios publicados
- **[Odoo Community Association](https://github.com/OCA)** — acuerdo de contribución firmado; revisiones de código en [purchase-workflow](https://github.com/OCA/purchase-workflow/pull/3097) y traductor de español en el Weblate de la OCA
- **[discovery-copilot](https://github.com/ACBRI/discovery-copilot)** — un agente que convierte una reunión en historias de usuario, construido sobre una transcripción ficticia para poder quedarse público

---

<br>

## Cómo trabajo

Lo primero nunca es el código: es entender. Levanto los procesos hablando con quienes los ejecutan, los modelo formalmente y dejo registradas las decisiones que importan, para que nadie tenga que adivinar después por qué se hizo algo así.

La gobernanza la trato igual: reglas claras de cómo se usan la IA y los datos, no candados que frenen al negocio. Y cuando una tarea repetitiva se puede automatizar, la automatizo, para que el tiempo se gaste en pensar y no en copiar.

Decido por *satisficing*, en el sentido de Herbert Simon: fijar el nivel que una solución debe cumplir y tomar la primera alternativa que lo cumple. El sistema maximizador llega tarde y a veces no llega.

---

<br>

## Herramientas

<div align="center">

<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/python.svg" width="40" alt="Python"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/postgresql.svg" width="40" alt="PostgreSQL"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/docker.svg" width="40" alt="Docker"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/terraform.svg" width="40" alt="Terraform"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/google.svg" width="40" alt="GCP"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/amazon.svg" width="40" alt="AWS"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/grafana.svg" width="40" alt="Grafana"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/nginx.svg" width="40" alt="Nginx"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/cloudflare.svg" width="40" alt="Cloudflare"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/git.svg" width="40" alt="Git"/></a>&nbsp;
<a href="#"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/javascript.svg" width="40" alt="JavaScript"/></a>

</div>

<br>

```
IA y generativa       Claude · OpenAI · Gemini · RAG · Agentes · Whisper
Gobernanza y riesgo   NIST AI RMF · ISO/IEC 42001 · DLP · políticas de uso
Arquitectura          C4 / Structurizr · BPMN 2.0 · ArchiMate · ADR · TOGAF
ERP y datos           Odoo 14-20 · módulos OCA · PostgreSQL 17 · Python
Nube y DevOps         GCP · AWS · Docker · Terraform · GitHub Actions · CI/CD
Observabilidad        Prometheus · Grafana · Loki · cAdvisor
Inteligencia negocio  Apache Superset · Metabase · vistas SQL
Documentación         Obsidian · LaTeX · React / TypeScript
```

---

<br>

## Experiencia

**PENTA Digital Lab · Arquitecto de soluciones de IA y ERP** — *mayo 2026 – hoy · Ecuador*
Arquitectura empresarial, integración de IA generativa y agentes, y adopción de IA en una multinacional de consumo masivo.

**Práctica independiente · Arquitectura empresarial, Odoo e IA aplicada** — *2020 – hoy · Ecuador y Colombia*
Levantamiento de procesos, mapas de arquitectura, implementaciones de Odoo con la localización de Ecuador y Colombia, e IA dentro de procesos reales. Alcance escrito y precios publicados.

**Oil & Gas Engineering · Arquitecto de soluciones y analista de procesos** — *2025 – 2026*
Arquitectura empresarial, ERP, inteligencia de negocio y transformación digital para operaciones de ingeniería distribuidas en Latinoamérica.

**NUTRABIOTICS S.A.S · Desarrollador full stack** — *2022 – 2023*
Desarrollo en Odoo, seguridad de la información e infraestructura en AWS.

**Antes** — educación, ingeniería y tecnología financiera. Donde aprendí que si uno no puede explicar algo con claridad, probablemente todavía no lo entiende del todo.

---

<br>

## Formación

Ingeniería de Sistemas — UNAD Colombia *(en curso)*
Más de 47 certificaciones en nube, seguridad, datos y arquitectura
Trabajando en TOGAF y en los marcos de gobernanza de IA (NIST AI RMF, ISO/IEC 42001)

---

<br>

## Hacia dónde voy

Quiero dirigir arquitectura y gobernanza de IA en organizaciones internacionales, en remoto. No por el cargo: por construir capacidades de IA que duren y que alguien use de verdad.

---

<div align="center">

<br>

[![Gráfico de contribuciones](https://ghchart.rshah.org/B5430F/ACBRI)](https://github.com/ACBRI)

<br>

Quito, Ecuador

<a href="https://andresbrinez.com">andresbrinez.com</a> · <a href="https://www.linkedin.com/in/acbri/">LinkedIn</a>

</div>
