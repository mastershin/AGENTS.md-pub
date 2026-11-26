# Enterprise Clinical Imaging & EHR AI Architecture: Operations vs. Analytics/Research
### Comprehensive Enterprise Landscape (Commercial Cloud, Clinical Platforms & Open Source)

This blueprint defines two enterprise architectures ingesting **EHR Clinical Notes (HL7/FHIR)** and **PACS Medical Imaging (DICOM)**—combining **enterprise clinical middleware, HIPAA-eligible cloud AI services, copyleft/open-source imaging tools, and modern agentic/graph frameworks**.

> **Clinical Scale Tier Legend:**
> * **Tier 1 (Departmental / Research Lab):** $< 50\text{K}$ studies/year / $< 5\text{ TB}$ DICOM + EHR text
> * **Tier 2 (Regional Hospital Network):** $50\text{K} - 1\text{M}$ studies/year / $5\text{ TB} - 250\text{ TB}$
> * **Tier 3 (Enterprise Health System / IDN):** $> 1\text{M}$ studies/year / $250\text{ TB} - 10\text{ PB}+$

---

## Path 1: Clinical Operations (Real-Time Triage, Summarization & Diagnostic Support)

**Objective:** Real-time clinical ingestion of incoming PACS exams + EHR patient context to prioritize acute cases, run FDA-cleared or locally validated imaging models, summarize patient/imaging timelines for clinician review, and write governed results back into PACS/EHR worklists.

### End-to-End Operational Pipeline & Enterprise Stack

| Pipeline Stage | Logo & Product | License / Model | Operational Function (EHR + PACS) | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| **1. Enterprise PACS & EHR Routing** | ![Laurel Bridge](https://img.shields.io/badge/Laurel%20Bridge-AI%20Workflow%20Suite-0F172A?style=flat-square) **Laurel Bridge AI Workflow Suite**<br>![dcm4chee](https://img.shields.io/badge/dcm4che-dcm4chee%205-0284C7?style=flat-square) **dcm4chee Archive 5** | Commercial Enterprise / MPL-GPL-LGPL | Multi-hospital DICOM routing, study filtering by modality/CPT code, HL7/FHIR EHR order/note synchronization, and failover queuing. | **Tier 2 – Tier 3** (Multi-site IDNs and enterprise VNA environments). |
| **2. Durable Study Orchestration** | ![Temporal](https://img.shields.io/badge/Temporal-Cloud%20%2F%20OSS-111827?style=flat-square) **Temporal** | MIT + Temporal Cloud | Guarantees end-to-end study execution across PACS fetch, FHIR lookup, GPU inference, and PACS write-back with strict SLA timeouts. | **Tier 2 – Tier 3** (Mission-critical acute triage workflows). |
| **3. Clinical Imaging Inference** | ![MONAI Deploy](https://img.shields.io/badge/MONAI-Deploy-008080?style=flat-square) **MONAI Deploy** + **FDA-Cleared Vendor AI** (Aidoc, Viz.ai, Rad AI) + **NVIDIA Triton** | Apache 2.0 + Commercial Clinical AI | Runs validated triage/quantification models (e.g., ICH, PE, LVO, lung nodules) and generates `DICOM SEG` overlays & `DICOM SR` structured measurements. | **Tier 2 – Tier 3** (Production clinical radiology & emergency workflows). |
| **4. Multimodal VLM & EHR Summarization** | ![Azure](https://img.shields.io/badge/Azure-AI%20Foundry%20(HIPAA)-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) **Azure AI Foundry / AWS Bedrock** + **MedGemma** + **LangGraph** | Commercial HIPAA BAA + Open Weights + MIT | Retrieves relevant longitudinal EHR notes, labs, and prior radiology reports; synthesizes concise clinical history and draft impressions for radiologist sign-off. | **Tier 2 – Tier 3** (Enterprise health systems operating under cloud HIPAA BAAs). |
| **5. Clinical Review & Worklist Delivery** | ![OHIF](https://img.shields.io/badge/OHIF-Viewer-0EA5E9?style=flat-square) **OHIF Viewer** / **Enterprise PACS Viewer** (Sectra, Visage, Nuance PowerScribe) | MIT / Commercial Clinical | Embeds AI overlays and draft structured findings directly into the radiologist's diagnostic reading cockpit for one-click accept/modify/reject. | **Tier 1 – Tier 3** (Zero-click clinical workflow integration). |
| **6. Clinical Guardrails & Telemetry** | ![Azure Content Safety](https://img.shields.io/badge/Azure-AI%20Content%20Safety-0078D4?style=flat-square) **Azure AI Content Safety / Bedrock Guardrails** + **LangSmith / Langfuse** | Commercial / MIT | Verifies groundedness of draft summaries against source EHR/imaging facts and tracks clinician acceptance/override rates and model drift. | **Tier 2 – Tier 3** (Enterprise clinical governance & safety committees). |

---

## Path 2: Clinical Analytics & Research (De-Identified Cohorts, Longitudinal Graphs & Model R&D)

**Objective:** High-scale retrospective and continuous ingestion of EHR notes + PACS studies, automated HIPAA de-identification, deduplication of scattered clinical records, **temporal knowledge graph construction** (tracking disease evolution and guideline/protocol shifts over time), and multi-modal foundation model R&D.

### End-to-End Analytics & Research Pipeline & Enterprise Stack

| Pipeline Stage | Logo & Product | License / Model | Research & Analytics Function (EHR + PACS) | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| **1. Research PACS & PHI De-Identification** | ![Orthanc](https://img.shields.io/badge/Orthanc-DICOM%20Server-10B981?style=flat-square) **Orthanc** + **RSNA CTP** + **Microsoft Presidio** + **Private AI** | GPLv3/AGPL / Apache 2.0 / MIT / Commercial | Extracts cohorts from enterprise VNA, strips DICOM tags, redacts burned-in pixel PHI, and de-identifies free-text EHR clinical notes with consistent patient tokens. | **Tier 1 – Tier 3** (IRB-governed clinical data warehouses & multi-site trials). |
| **2. Petabyte Cloud Storage & ETL** | ![AWS HealthImaging](https://img.shields.io/badge/AWS-HealthImaging-FF9900?style=flat-square&logo=amazonaws&logoColor=white) **AWS HealthImaging** / **GCP Medical Imaging Suite** + **Apache Airflow** | Commercial Cloud + Apache 2.0 | Stores petabytes of de-identified DICOM studies with sub-second frame streaming alongside scheduled ETL pipelines for EHR notes and pathology slides. | **Tier 3 ($1\text{ PB}+$)** (Multi-hospital research imaging lakes). |
| **3. Multimodal Embeddings & Vector Search** | ![Cohere](https://img.shields.io/badge/Cohere-Embed%20v4-39594D?style=flat-square) **Cohere Embed / Voyage AI** + **Milvus / Pinecone / Qdrant** | Commercial / Apache 2.0 | Indexes hundreds of millions of clinical note chunks, pathology reports, and radiology embeddings for fast cross-modal cohort search. | **Tier 2 – Tier 3** ($10\text{M} - 1\text{B}+$ clinical vectors). |
| **4. Evolving & Temporal Knowledge Graph** | ![Neo4j](https://img.shields.io/badge/Neo4j-Enterprise-008CC1?style=flat-square&logo=neo4j&logoColor=white) **Neo4j** + **Zep / Graphiti** + **Cognee** | GPLv3/Commercial + Apache 2.0 | Deduplicates scattered EHR/radiology entities, links serial imaging studies to treatments, and models **bi-temporal timelines** (disease progression & protocol changes over time). | **Tier 2 – Tier 3** (Longitudinal outcomes research & real-world evidence). |
| **5. Annotation, Pathology & Model R&D** | ![MONAI Label](https://img.shields.io/badge/MONAI-Label-008080?style=flat-square) **MONAI Label** + **3D Slicer** + **QuPath** + **BiomedParse / MedGemma** | Apache 2.0 / BSD / GPLv3 / Open Weights | Collaborative radiology & gigapixel digital pathology annotation, radiomics extraction, and fine-tuning multimodal foundation models. | **Tier 1 – Tier 3** (Academic medical centers & pharma/biotech R&D). |
| **6. Drift, Bias & Eval Observability** | ![Arize Phoenix](https://img.shields.io/badge/Arize-Phoenix%20%2F%20W%26B%20Weave-FF6B6B?style=flat-square) **Arize Phoenix / W&B Weave** + **Ragas** | ELv2/Commercial + Apache 2.0 | Tracks embedding/scanner drift across MRI/CT vendors, audits subgroup bias (age, sex, scanner), and evaluates longitudinal summarization quality. | **Tier 2 – Tier 3** (Enterprise MLOps & clinical validation governance). |

---

## Summary Decision Matrix: Path 1 vs. Path 2

| Architectural Dimension | Path 1: Clinical Operations | Path 2: Clinical Analytics & Research |
| :--- | :--- | :--- |
| **Trigger & Latency** | Event-driven (HL7/FHIR + DICOM `C-STORE`); seconds to minutes | Scheduled batch / streaming cohort ingestion; minutes to hours |
| **PHI Posture** | **Live PHI** inside strict HIPAA BAA / on-prem VPC boundary | **De-identified / Pseudonymized** via CTP + Presidio / Private AI |
| **Primary AI Output** | Triage alerts, `DICOM SEG/SR` overlays, concise draft impressions | Deduplicated longitudinal graphs, cohort insights, trained models |
| **Temporal Requirement** | Current encounter + recent relevant priors | Full multi-year patient trajectory + historical policy/protocol diffs |
| **Governance Gate** | Clinician-in-the-loop sign-off + FDA/regulatory validation | IRB/data-governance approval + offline benchmark validation |