# Enterprise Clinical Imaging & EHR AI Architecture: Operations vs. Analytics/Research
### 100% Free & Permissive Open Source Stack (Apache 2.0 / MIT / BSD / MPL 1.1 Only)

This blueprint defines two distinct, air-gapped-ready enterprise data and AI architectures ingesting **EHR Clinical Notes (HL7/FHIR)** and **PACS Medical Imaging (DICOM)**—built **exclusively with 100% free, permissively licensed open-source tools** (zero GPL/AGPL, SSPL/RSAL, BSL, or proprietary cloud lock-in).

> **Clinical Scale Tier Legend:**
> * **Tier 1 (Departmental / Research Lab):** $< 50\text{K}$ studies/year / $< 5\text{ TB}$ DICOM + EHR text
> * **Tier 2 (Regional Hospital Network):** $50\text{K} - 1\text{M}$ studies/year / $5\text{ TB} - 250\text{ TB}$
> * **Tier 3 (Enterprise Health System / IDN):** $> 1\text{M}$ studies/year / $250\text{ TB} - 10\text{ PB}+$

---

## Architecture Overview: Two Separated Pipelines

```text
                        ┌──────────────────────────────────────────────┐
                        │   HOSPITAL SOURCE SYSTEMS (PHI BOUNDARY)     │
                        │  • PACS / VNA (DICOM DIMSE & DICOMweb)       │
                        │  • EHR / CDR (HL7 FHIR R4, Notes, Labs)      │
                        └───────────────┬──────────────┬───────────────┘
                                        │              │
                 ┌──────────────────────▼──┐        ┌──▼──────────────────────┐
                 │  PATH 1: CLINICAL OPS   │        │ PATH 2: RESEARCH & ANALYTICS
                 │  (Real-Time / Live PHI) │        │ (Batch / De-Identified) │
                 └──────────────────────┬──┘        └──┬──────────────────────┘
                                        │              │
  1. Ingest & Route:   MONAI Deploy Gateway + Temporal │ RSNA CTP + Apache Airflow + Presidio
  2. Analyze & Reason: MONAI + Triton + vLLM + LangGraph│ MONAI Label + Graphiti + BGE-M3 + Qdrant
  3. Output & Action:  OHIF Viewer + DICOM SR/SEG Draft│ Cohort Discovery, Longitudinal Graphs, R&D
  4. Governance:       NeMo Guardrails + Langfuse OSS  │ Promptfoo + Ragas + Model Registry
```

---

## Path 1: Clinical Operations (Real-Time Triage, Summarization & Diagnostic Support)

**Objective:** Sub-minute ingestion of incoming PACS imaging + recent EHR context to detect critical findings, summarize prior history, draft structured radiology/clinical impressions for **human-in-the-loop clinician sign-off**, and write results back to PACS/EHR.

### End-to-End Operational Pipeline & Recommended OSS Stack

| Pipeline Stage | Logo & Tool (License) | GitHub Repository | Operational Function (EHR + PACS) | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| **1. PACS & EHR Ingestion** | ![MONAI Deploy](https://img.shields.io/badge/MONAI-Informatics%20Gateway-008080?style=flat-square) **MONAI Deploy Gateway** *(Apache 2.0)*<br>![dcm4che](https://img.shields.io/badge/dcm4che-Toolkit-0284C7?style=flat-square) **dcm4che / pynetdicom** *(MPL 1.1 / MIT)* | [monai-deploy-informatics-gateway](https://github.com/Project-MONAI/monai-deploy-informatics-gateway)<br>[dcm4che/dcm4che](https://github.com/dcm4che/dcm4che) | Listens for incoming DICOM `C-STORE` / `STOW-RS` studies and pulls matching patient EHR notes, allergies, and lab orders via FHIR R4 APIs. | **Tier 1 – Tier 3** (Hospital Kubernetes ingress). |
| **2. Durable Workflow Orchestration** | ![Temporal](https://img.shields.io/badge/Temporal-Durable%20Execution-111827?style=flat-square) **Temporal** *(MIT)* | [temporalio/temporal](https://github.com/temporalio/temporal) | Guarantees zero silent study drops; manages strict SLAs, retries on GPU/FHIR timeouts, and routes urgent findings (e.g., stroke/PE) to priority queues. | **Tier 2 – Tier 3** (Mission-critical clinical reliability). |
| **3. Imaging AI Inference** | ![MONAI](https://img.shields.io/badge/MONAI-Core%20%2F%20Deploy-008080?style=flat-square) **MONAI Core & MAPs** *(Apache 2.0)*<br>![Triton](https://img.shields.io/badge/NVIDIA-Triton%20Server-76B900?style=flat-square) **NVIDIA Triton** *(BSD-3-Clause)* | [Project-MONAI/MONAI](https://github.com/Project-MONAI/MONAI)<br>[triton-inference-server/server](https://github.com/triton-inference-server/server) | Executes validated 2D/3D segmentation, nodule/hemorrhage detection, and volumetric measurements, packaging outputs into `DICOM SEG` & `DICOM SR`. | **Tier 2 – Tier 3** (Multi-GPU hospital inference clusters). |
| **4. Multimodal & EHR Reasoning Agent** | ![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Graph-1C3C3C?style=flat-square) **LangGraph** *(MIT)*<br>![PydanticAI](https://img.shields.io/badge/PydanticAI-Typed%20Agents-E92063?style=flat-square) **PydanticAI** *(MIT)*<br>![vLLM](https://img.shields.io/badge/vLLM-Local%20LLM%2FVLM-00ADD8?style=flat-square) **vLLM** *(Apache 2.0)* | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)<br>[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)<br>[vllm-project/vllm](https://github.com/vllm-project/vllm) | Synthesizes quantitative `DICOM SR` findings + prior radiology reports + EHR clinical notes into a schema-validated draft impression and differential checklist. | **Tier 1 – Tier 3** (On-prem H100/L40S servers keeping live PHI inside hospital VPC). |
| **5. Clinical Review & Human-in-the-Loop** | ![OHIF](https://img.shields.io/badge/OHIF-Web%20Viewer-0EA5E9?style=flat-square) **OHIF Viewer** *(MIT)* | [OHIF/Viewers](https://github.com/OHIF/Viewers) | Displays 2D/3D imaging with AI segmentation overlays (`DICOM SEG`) alongside draft findings so radiologists/clinicians can accept, edit, or reject before PACS/EHR commit. | **Tier 1 – Tier 3** (Zero-footprint web review portals). |
| **6. Guardrails & Clinical Audit** | ![NeMo Guardrails](https://img.shields.io/badge/NVIDIA-NeMo%20Guardrails-76B900?style=flat-square) **NeMo Guardrails** *(Apache 2.0)*<br>![Langfuse](https://img.shields.io/badge/Langfuse-OSS%20Tracing-000000?style=flat-square) **Langfuse OSS** *(MIT)* | [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails)<br>[langfuse/langfuse](https://github.com/langfuse/langfuse) | Enforces groundedness to imaging/EHR facts (preventing unsupported diagnostic claims) and logs full model version, prompt, and clinician override telemetry. | **Tier 1 – Tier 3** (HIPAA audit trail & clinical QA). |

---

## Path 2: Clinical Analytics & Research (De-Identified Cohorts, Longitudinal Graphs & Model R&D)

**Objective:** Batch/continuous ingestion of historical EHR notes + PACS imaging, automated PHI de-identification, entity deduplication, **temporal knowledge graph construction** (tracking disease progression and clinical protocol changes over time), cohort discovery, and new model training.

### End-to-End Analytics & Research Pipeline & Recommended OSS Stack

| Pipeline Stage | Logo & Tool (License) | GitHub Repository | Research & Analytics Function (EHR + PACS) | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| **1. Cohort Extraction & PHI Scrubbing** | ![CTP](https://img.shields.io/badge/RSNA-CTP-1E3A8A?style=flat-square) **RSNA CTP** *(Apache 2.0)*<br>![Presidio](https://img.shields.io/badge/Microsoft-Presidio-0078D4?style=flat-square) **Microsoft Presidio** *(MIT)* | [johnperry/CTP](https://github.com/johnperry/CTP)<br>[data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio) | Strips DICOM header PHI, shifts dates consistently per patient pseudonym, redacts burned-in pixel text (Presidio Image Redactor), and scrubs free-text EHR notes. | **Tier 2 – Tier 3** (IRB-approved research data warehouses). |
| **2. Batch ETL & Document Parsing** | ![Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?style=flat-square) **Apache Airflow** *(Apache 2.0)*<br>![Docling](https://img.shields.io/badge/IBM-Docling-054ADA?style=flat-square) **IBM Docling** *(MIT)* | [apache/airflow](https://github.com/apache/airflow)<br>[docling-project/docling](https://github.com/docling-project/docling) | Orchestrates nightly cohort extraction, parses scanned pathology/radiology PDFs and structured EHR discharge summaries into clean Markdown/JSON. | **Tier 2 – Tier 3** ($100\text{ TB}+$ multi-year hospital archives). |
| **3. Embeddings & Multimodal Vector Store** | ![BGE-M3](https://img.shields.io/badge/BAAI-BGE--M3-1E40AF?style=flat-square) **BGE-M3 / EmbeddingGemma 2** *(MIT / Apache 2.0)*<br>![Qdrant](https://img.shields.io/badge/Qdrant-Vector%20DB-DC244C?style=flat-square) **Qdrant / pgvector** *(Apache 2.0 / PostgreSQL)* | [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding)<br>[qdrant/qdrant](https://github.com/qdrant/qdrant) | Generates dense + sparse clinical text embeddings and multimodal image-report embeddings for semantic cohort discovery ("Find all smokers with spiculated upper-lobe nodules"). | **Tier 1 – Tier 3** ($1\text{M} - 500\text{M}+$ clinical notes & series vectors). |
| **4. Longitudinal & Temporal Knowledge Graph** | ![Graphiti](https://img.shields.io/badge/Zep-Graphiti-6366F1?style=flat-square) **Graphiti** *(Apache 2.0)*<br>![LightRAG](https://img.shields.io/badge/HKUDS-LightRAG-10B981?style=flat-square) **LightRAG** *(MIT)* | [getzep/graphiti](https://github.com/getzep/graphiti)<br>[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Deduplicates clinical concepts across scattered notes, links serial imaging studies to EHR treatments, and tracks **temporal timelines** (lesion progression & guideline/protocol shifts over time). | **Tier 2 – Tier 3** (Longitudinal oncology, chronic disease, and protocol-evolution research). |
| **5. Annotation & Model R&D** | ![MONAI Label](https://img.shields.io/badge/MONAI-Label-008080?style=flat-square) **MONAI Label** *(Apache 2.0)*<br>![3D Slicer](https://img.shields.io/badge/3D%20Slicer-Workbench-2563EB?style=flat-square) **3D Slicer** *(BSD-Style)*<br>![nnU-Net](https://img.shields.io/badge/DKFZ-nnU--Net-1E40AF?style=flat-square) **nnU-Net** *(Apache 2.0)* | [Project-MONAI/MONAILabel](https://github.com/Project-MONAI/MONAILabel)<br>[Slicer/Slicer](https://github.com/Slicer/Slicer)<br>[MIC-DKFZ/nnUNet](https://github.com/MIC-DKFZ/nnUNet) | Active-learning radiologist labeling, radiomics feature extraction, and training/benchmarking custom 3D segmentation and classification models. | **Tier 1 – Tier 2** (Academic medical centers & internal AI R&D labs). |
| **6. Cohort Analytics & Evaluation** | ![Ragas](https://img.shields.io/badge/ExplodingGradients-Ragas-10B981?style=flat-square) **Ragas & Promptfoo** *(Apache 2.0 / MIT)* | [explodinggradients/ragas](https://github.com/explodinggradients/ragas)<br>[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Evaluates longitudinal summarization faithfulness, checks for demographic/scanner bias across cohorts, and validates models before promotion to Path 1. | **Tier 1 – Tier 3** (Reproducible clinical research & pre-deployment validation). |