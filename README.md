<a href="https://andresbrinez.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/cabecera-oscura-en.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/cabecera-clara-en.svg">
    <img src="assets/cabecera-clara-en.svg" width="100%" alt="Andrés Briñez. AI engineering, data and Odoo ERP. Quito, Ecuador.">
  </picture>
</a>

<p align="center">
  <a href="https://andresbrinez.com">andresbrinez.com</a> ·
  <a href="https://www.linkedin.com/in/acbri/">LinkedIn</a> ·
  <a href="mailto:contacto@andresbrinez.com">contacto@andresbrinez.com</a>
  <br>
  <b>English</b> · <a href="README.es.md">Español</a>
</p>

**AI engineering, data and Odoo ERP for companies · Quito, Ecuador (UTC-5)**

I build AI that takes over a real step of your work. It reads your
documents, listens to your meetings and calls, answers from your own data
and acts inside the systems you already use. Behind it, clean data and Odoo
ERP for finance: accounting, e-invoicing and tax.

The aim is a mid-sized company that runs the way large ones do. You get the
scope in writing before I start, and results you can check.

## What I do today

I work for myself. **Andrés Briñez** is my own practice, based in Quito
since September 2026. It operates on its own product:
[andresbrinez.com](https://andresbrinez.com) is a self-hosted Odoo 19
Community instance that serves the public site in two languages, the client
portal, the CRM, quotations and invoicing from a single system.

What you can hand me:

- **An AI agent for your process.** Claude with tools that read and write in
  your ERP, database or files, inside the limits you set.
- **Answers from your own documents (RAG).** Search with embeddings and
  pgvector, measured with test questions, so you know how often it is right.
- **Audio turned into work.** Transcription with Whisper, speaker
  recognition, and minutes or summaries written by an LLM.
- **Data that has to move or connect.** Python and PostgreSQL pipelines, API
  integrations and n8n workflows.
- **Odoo ERP for finance.** Accounting, e-invoicing and tax for Ecuador and
  Colombia.

## What I have built

- **Reunia, AI meeting minutes that know who spoke.** It transcribes the
  audio with Whisper, recognizes each speaker across meetings by voice
  embeddings in pgvector, and writes the minutes with an LLM. FastAPI on
  Cloud Run, Terraform. Built end to end and first deployed in July 2026.
- **A call copilot.** It transcribes the call on the device while people
  speak and answers with Claude in a little over a second.
- **A RAG system over more than 2,000 of my own files.** LlamaIndex and
  pgvector. It answers 24 of 26 test questions correctly, and the two it
  misses are documented. Sensitive files never leave the machine.
- **Ecuador's e-invoicing localization on Odoo 19 Community.** I brought it
  to Odoo 19: 11 modules and 580 automated tests. The tax authority (SRI)
  authorized the invoice, credit note, purchase settlement and withholding
  in its certification environment. My own company has invoiced with it
  since September 2026.
- **Two companies, two countries, one Odoo.** The accounting of a company in
  Ecuador and one in Colombia, in production on a single instance, with
  scripted deployment on my own continuous integration and tested backups.

These five live in private repositories. What anyone can open is below.

## In the open

- **[andresbrinez.com](https://andresbrinez.com)**: the site runs on the
  stack it describes, in two languages, with the prices published.
- **[Odoo Community Association](https://github.com/OCA)**: contributor
  agreement signed; two approving reviews on pull requests that were merged
  in purchase-workflow
  ([#3097](https://github.com/OCA/purchase-workflow/pull/3097),
  [#3129](https://github.com/OCA/purchase-workflow/pull/3129)); Spanish
  translator on the OCA's Weblate.
- **[discovery-copilot](https://github.com/ACBRI/discovery-copilot)**: an
  agent that reads the transcript of a requirements meeting and returns user
  stories with acceptance criteria. It runs on a fictional transcript, so
  the repository stays open.
- **[survey-19](https://github.com/ACBRI/survey-19)**: the OCA module
  `survey_question_type_binary`, a survey question answered with files,
  migrated to Odoo 19 on a fork of OCA/survey, with its checks and tests
  scripted in the repository.
- **[agrosmart-digital-twin](https://github.com/ACBRI/agrosmart-digital-twin)**:
  a university project. The runnable digital twin of a low-cost irrigation
  system: simulated field nodes over MQTT, TimescaleDB and Grafana, started
  with one `docker compose up`.

## Experience

**AI Engineer · Solutions Architect and Odoo Consultant (independent)**<br>
Andrés Briñez · andresbrinez.com · Quito, Ecuador · *Sep 2026 – present*<br>
AI products and business systems for companies, with the scope in writing
before work starts.

**Odoo Consultant · Enterprise Architecture**<br>
PENTA Digital Lab · Cuenca, Ecuador · *May 2026 – Aug 2026*<br>
Odoo 18-to-19 migration of custom modules with AI agents, each module
verified against a running instance. Discovery workshops, functional
specifications in versioned LaTeX, and processes modeled in C4, BPMN 2.0 and
ArchiMate.

**Lead Odoo and Cloud Architect**<br>
TECNACORP · Quito, Ecuador · *Sep 2025 – May 2026*<br>
Odoo 18 in operation on Google Cloud with Cloud Run, Cloud SQL and
Terraform. Continuous integration with GitHub Actions and Docker,
observability and automated backups. KoboCollect, the forms field crews fill
in without signal, connected to Odoo with n8n.

**ERP Solutions Architect (Odoo) · Presales**<br>
SOINTEM · Quito, Ecuador · *Apr 2025 – Sep 2025*<br>
Odoo designed and implemented end to end, through go-live, in
manufacturing, retail distribution, floriculture and e-commerce.

**Cloud Solutions Specialist**<br>
Universal Waterproofing · Adelaide, Australia · *Jan 2024 – Nov 2024*<br>
Handled the company's cloud side alongside on-site waterproofing work:
automations and custom modules in Odoo, and the platform migrated to AWS
with Docker and Terraform.

**Cybersecurity and Full Stack Development**<br>
Nutrabiotics · Bogotá, Colombia · *Jul 2022 – Dec 2023*<br>
Joined as Junior Full Stack Developer and moved to the cybersecurity role in
February 2023. Critical systems migrated to AWS, with role-based IAM
policies and monitoring.

**Founder · Full Stack Developer**<br>
Shield Cloud · Remote · *Dec 2020 – Jun 2022*<br>
My own company for web and cloud projects: web applications in React and
Node.js on AWS, with the infrastructure declared in Terraform.

## Stack

```
AI         Claude · AI agents · RAG · LlamaIndex · Whisper · pgvector
Data       Python · PostgreSQL · FastAPI · n8n · API integrations
Odoo ERP   Odoo 18 and 19 · OCA · accounting · e-invoicing · tax
Platform   Google Cloud · Terraform · Docker · GitHub Actions
```

## Education and recognition

- **Systems Engineering** (undergraduate degree, in progress), Universidad
  Nacional Abierta y a Distancia (UNAD), Colombia. Seventh semester as of
  October 2026.
- **MediaHack 2025, winning project.** Veritas AI, an AI news verifier for
  the 2025 elections, built with my team. UNESCO Ecuador and Fundación
  OpenLab, March 2025.
- **Course certificates.** Claude Code 101 and Claude 101, Anthropic, April
  2026.

## Working with me

Scope, price and delivery date in writing before anything starts. Small
deliveries you can test. If AI is not the right tool for your problem, I say
so.

If you are hiring: I am open to AI engineer, solutions architect and Odoo
consultant roles, in Ecuador or remote. Colombian, resident in Quito with an
Ecuadorian ID card. Native Spanish and intermediate English: I work best in
writing.

Write to [contacto@andresbrinez.com](mailto:contacto@andresbrinez.com).

<a href="https://andresbrinez.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/pie-oscuro.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/pie-claro.svg">
    <img src="assets/pie-claro.svg" width="100%" alt="andresbrinez.com">
  </picture>
</a>
