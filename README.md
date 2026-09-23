<div align="center">

# Andrés Briñez

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&size=18&pause=1000&color=B5430F&center=true&vCenter=true&width=620&lines=AI+Enterprise+Architect;Enterprise+Architecture+%26+AI+Governance;ERP+that+runs+%7C+RAG+%7C+Agents;I+ship+what+I+design)](https://git.io/typing-svg)

<br>

<a href="https://andresbrinez.com"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/html5.svg" width="36" alt="Website"/></a>&nbsp;&nbsp;
<a href="https://www.linkedin.com/in/acbri/"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/linkedin.svg" width="36" alt="LinkedIn"/></a>&nbsp;&nbsp;
<a href="mailto:acbri.19@gmail.com"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/gmail.svg" width="36" alt="Email"/></a>&nbsp;&nbsp;
<a href="https://github.com/ACBRI"><img src="https://raw.githubusercontent.com/edent/SuperTinyIcons/master/images/svg/github.svg" width="36" alt="GitHub"/></a>

<br>

**English**  ·  [Español](README.es.md)

</div>

---

**AI Enterprise Architect · Enterprise Architecture and AI Governance · Quito, Ecuador**

I step into organizations that have outgrown their own systems, work out how they actually run, and design the architecture — and the AI governance — that lets them keep growing without breaking.

Two things separate what I do from a slide deck. The first is that I implement what I design: the ERP goes live, the pipeline runs on a schedule, the model answers with the company's own documents. The second is that I write the decisions down, in a form someone can audit a year later.

---

<br>

## What I am doing right now

**Enterprise AI capability for a consumer-goods multinational** (through PENTA Digital Lab). Solution architecture for an end-to-end commercial transformation: as-is survey, gap analysis, target model, systems integration, and GenAI and agents placed inside the business processes rather than beside them.

**A consultancy that runs on the systems it sells.** [andresbrinez.com](https://andresbrinez.com) is my own Odoo 19 Community instance, self-hosted, serving the public site, the client portal, the CRM, quotations and invoicing from a single system. Continuous integration on my own runners, deployment with one command, backups verified end to end. Every product I sell was first run against my own business.

---

<br>

## What I have built

**Enterprise architecture and ERP**

- Architecture of an end-to-end commercial transformation for a consumer-goods multinational: TO-BE model, gap analysis, systems integration
- Ecuadorian electronic invoicing for Odoo 19: eight modules ported from the OCA's 18.0 line — invoices, credit and debit notes, withholding, purchase settlements, waybills, the ATS return and inbound supplier documents — with 314 automated tests and CI
- Colombian withholding tax for Odoo 19: withholding at source, CIIU economic activities and the bridge to electronic invoicing, so each withholding declares its own tax in the XML
- Two-country accounting in production (Ecuador and Colombia), including an expense classifier that reads the supplier's registered activity before asking a model
- Odoo upgrade radar: walks a codebase and reports what breaks on the next version, file and line, in the order worth fixing

**AI in production**

- Retrieval over a company's own documents and ERP data, built the way the production literature says to build it: hybrid retrieval from day one, reranking, a measured faithfulness threshold, and an evaluation set of real questions with written answers
- A generative-AI pipeline for meeting transcription and minutes (Whisper with speaker diarization, then cleanup)
- Reunia — an AI-first meeting-intelligence platform, in progress
- LLM-agent workflows that turn a meeting transcript into user stories

**Modelling and documentation**

- C4 with Structurizr, BPMN 2.0, ArchiMate and architecture decision records, in organizations that had none
- Documentation as code: versioned, reviewable, and still true after the consultant leaves

These are not lab projects. They are systems someone uses today to make decisions that cost real money.

---

<br>

## In the open

Most of my work lives in private repositories, for the obvious reason. What can be checked from outside:

- **[andresbrinez.com](https://andresbrinez.com)** — the site is the artefact: it runs on the stack it describes, in two languages, with the prices published
- **[Odoo Community Association](https://github.com/OCA)** — contributor licence signed; code reviews on [purchase-workflow](https://github.com/OCA/purchase-workflow/pull/3097), and Spanish translator on the OCA's Weblate
- **[discovery-copilot](https://github.com/ACBRI/discovery-copilot)** — a meeting-to-user-stories agent, built on a fictional transcript so it can stay public

---

<br>

## How I work

The first thing is never code — it is understanding. I map processes by talking to the people who run them, model them formally, and record the decisions that matter, so nobody has to guess later why something was done that way.

I treat governance the same way: clear rules for how AI and data get used, not locks that slow the business down. And when a repetitive task can be automated, I automate it, so the time gets spent thinking instead of copying.

I decide by satisficing, in Herbert Simon's sense: set the level a solution has to reach, then take the first alternative that reaches it. The maximizing system arrives late, and sometimes never arrives at all.

---

<br>

## Stack

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
AI and GenAI            Anthropic (Claude) · OpenAI · Vertex AI / Gemini · RAG · Agents · Whisper
Governance and risk     NIST AI RMF · ISO/IEC 42001 (adopting) · DLP · AI usage policies
Enterprise architecture C4 / Structurizr · BPMN 2.0 · ArchiMate · ADRs · TOGAF (in progress)
ERP and data            Odoo 14-20 · OCA modules · PostgreSQL 17 · Python
Cloud and DevOps        GCP · AWS · Docker · Terraform · Cloudflare · GitHub Actions · CI/CD
Observability           Prometheus · Grafana · Loki · cAdvisor
Business intelligence   Apache Superset · Metabase · SQL views
Docs and automation     Obsidian · LaTeX · React / TypeScript
```

---

<br>

## Experience

**PENTA Digital Lab · AI and ERP Solutions Architect** — *May 2026 – present · Ecuador*
Enterprise architecture, GenAI and agent integration, and AI-first adoption for a consumer-goods multinational.

**Independent practice · Enterprise architecture, Odoo and applied AI** — *2020 – present · Ecuador and Colombia*
Process mapping, architecture maps, Odoo implementations with Ecuadorian and Colombian localisation, and AI inside real processes. Fixed scope and published prices.

**Oil and Gas Engineering · Solutions Architect and Process Analyst** — *2025 – 2026*
Enterprise architecture, ERP, BI and digital transformation for distributed engineering operations across Latin America.

**NUTRABIOTICS S.A.S · Full Stack Developer** — *2022 – 2023*
Odoo development, information security and AWS infrastructure.

**Earlier** — education, engineering, financial technology. Where I learned that if you cannot explain something clearly, you probably do not understand it well enough yet.

---

<br>

## Education

Systems Engineering — UNAD Colombia *(in progress)*
47+ certifications in cloud, security, data and architecture
Currently working through TOGAF and the AI-governance frameworks (NIST AI RMF, ISO/IEC 42001)

---

<br>

## Where I am heading

I want to lead AI architecture and governance in international organizations, remotely. Not for the title: for the chance to build AI capabilities that last and that someone actually uses.

---

<div align="center">

<br>

[![Contribution streak](https://streak-stats.demolab.com?user=ACBRI&hide_border=true&background=F3EFE2&ring=B5430F&fire=B5430F&currStreakLabel=27201B&sideLabels=6E6156&dates=6E6156&currStreakNum=27201B&sideNums=27201B&stroke=DED7C8)](https://github.com/ACBRI)

<br>

[![Contribution graph](https://ghchart.rshah.org/B5430F/ACBRI)](https://github.com/ACBRI)

<br>

Quito, Ecuador

<a href="https://andresbrinez.com">andresbrinez.com</a> · <a href="https://www.linkedin.com/in/acbri/">LinkedIn</a>

</div>
