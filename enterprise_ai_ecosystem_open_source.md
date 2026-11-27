# Enterprise AI Ecosystem: 100% Free & Permissive Open Source Stack
### Strictly Vetted: Apache 2.0, MIT, BSD-3-Clause & PostgreSQL Licenses Only

This reference architecture includes **exclusively 100% free, permissive open-source software (Apache 2.0, MIT, BSD, PostgreSQL)**.
* **Zero Licensing Lock-in:** Safe for proprietary enterprise modification, internal SaaS deployment, and air-gapped VPCs without copyleft (AGPL/GPL) or Fair-Code/SSPL commercial restrictions.
* **Excluded by Design:** Proprietary SaaS APIs (e.g., Notion, Zep Cloud), managed cloud graph & context platforms (e.g., Amazon Neptune, Azure Cosmos DB, Google Cloud Spanner Graph, Databricks Genie Ontology, AWS Context, Palantir Foundry, Microsoft Fabric IQ), proprietary free-tier binaries (e.g., Ontotext GraphDB Free), SSPL/RSAL databases (e.g., Redis, MongoDB), copyleft/ELv2 tools (e.g., Arize Phoenix, AppFlowy, Docmost, Neo4j GPLv3, ComfyUI GPLv3, XTDB MPL-2.0, Owlready2 LGPL-3.0), Fair-Code/BSL tools (e.g., n8n, Outline), and non-commercial/restricted weights.

> **Scale Tier Legend:**
> * **Tier 1 (Prototyping / Departmental):** $< 100\text{K}$ documents / $< 1\text{M}$ vectors / $< 10\text{ GB}$
> * **Tier 2 (Mid-Market / Production):** $100\text{K} - 10\text{M}$ documents / $1\text{M} - 100\text{M}$ vectors / $10\text{ GB} - 1\text{ TB}$
> * **Tier 3 (Enterprise / Web-Scale):** $> 10\text{M}$ documents / $100\text{M} - 10\text{B}+$ vectors / $1\text{ TB} - 1\text{ PB}+$

---

## 1. Open-Weight LLMs & Inference Engines (Apache 2.0 / MIT)

100% permissively licensed foundation models and self-hosted GPU/CPU inference engines.

| Logo & Product | License | GitHub / Hugging Face Repo | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![vLLM](https://img.shields.io/badge/vLLM-Inference%20Engine-00ADD8?style=flat-square) **vLLM** | **Apache 2.0** | [vllm-project/vllm](https://github.com/vllm-project/vllm) | Enterprise-standard high-throughput LLM serving with PagedAttention, FP8 quantization, and OpenAI-compatible APIs. | **Tier 2 – Tier 3** (Multi-GPU H100/A100/L40S clusters serving high-concurrency production traffic). |
| ![Qwen](https://img.shields.io/badge/Alibaba-Qwen%202.5%20%2F%20Qwen%203-6366F1?style=flat-square) **Qwen (Open Weights: 0.5B–72B+ / Coder)** | **Apache 2.0** *(select variants)* | [QwenLM/Qwen2.5](https://github.com/QwenLM/Qwen2.5) | Top-performing permissively licensed open models for coding (`Qwen-Coder`), math, tool calling, and multilingual enterprise RAG. | **Tier 1 – Tier 3** ($7\text{B}-14\text{B}$ for high-QPS extraction; $32\text{B}-72\text{B}+$ for complex reasoning). |
| ![Mistral](https://img.shields.io/badge/Mistral%20AI-Open%20Models-FA520F?style=flat-square) **Mistral Open Models (Mistral 7B / Nemo / Mixtral)** | **Apache 2.0** | [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) | Fast function calling, European data sovereignty, and Mixture-of-Experts (MoE) cost-efficient inference. | **Tier 1 – Tier 3** (High throughput per GPU dollar for enterprise classification and RAG). |
| ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black) **Hugging Face Transformers** | **Apache 2.0** | [huggingface/transformers](https://github.com/huggingface/transformers) | Standard model loading, LoRA/QLoRA fine-tuning, and pipeline execution across PyTorch/ONNX. | **All Scales** (Core foundation for custom enterprise model training and inference). |
| ![Ollama](https://img.shields.io/badge/Ollama-Local%20Runtime-000000?style=flat-square&logo=ollama&logoColor=white) **Ollama** | **MIT** | [ollama/ollama](https://github.com/ollama/ollama) | Single-command local LLM & embedding deployment on developer laptops, air-gapped workstations, and edge servers. | **Tier 1** ($< 50$ concurrent users; local development and edge nodes). |
| ![llama.cpp](https://img.shields.io/badge/ggml-llama.cpp-10B981?style=flat-square) **llama.cpp** | **MIT** | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Ultra-lightweight C/C++ quantized inference (GGUF) for CPU-only servers, Apple Silicon, and edge hardware. | **Tier 1 – Tier 2** (Cost-sensitive CPU inference and edge deployments). |
| ![SGLang](https://img.shields.io/badge/LMSYS-SGLang-EF4444?style=flat-square) **SGLang** | **Apache 2.0** | [sgl-project/sglang](https://github.com/sgl-project/sglang) | High-speed structured JSON generation and RadixAttention prefix caching for multi-turn agentic workflows. | **Tier 2 – Tier 3** (Agentic workloads with heavy shared system prompts and JSON schemas). |

---

## 2. Agentic AI Orchestration Frameworks (Apache 2.0 / MIT)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-1C3C3C?style=flat-square&logo=langchain&logoColor=white) **LangGraph (OSS Core)** | **MIT** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Stateful cyclical agent graphs, human-in-the-loop interrupts, and durable execution backed by self-hosted PostgreSQL. | **Tier 1 – Tier 3** (Scales horizontally on Kubernetes with Postgres checkpointers). |
| ![Microsoft](https://img.shields.io/badge/Microsoft-Agent%20Framework-0078D4?style=flat-square&logo=microsoft&logoColor=white) **Microsoft Agent Framework** | **MIT** | [microsoft/agent-framework](https://github.com/microsoft/agent-framework) | Enterprise Python & .NET multi-agent orchestration (sequential, concurrent, handoff, group chat) with OpenTelemetry. | **Tier 2 – Tier 3** (Production .NET and Python enterprise microservices). |
| ![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF5A5F?style=flat-square) **CrewAI (OSS Framework)** | **MIT** | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Role-based collaborative agent crews and deterministic event-driven Python Flows. | **Tier 1 – Tier 2** (Departmental automation and structured multi-agent pipelines). |
| ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-Workflows-7C3AED?style=flat-square) **LlamaIndex Workflows** | **MIT** | [run-llama/llama_index](https://github.com/run-llama/llama_index) | Async, event-driven orchestration for agentic RAG and multi-step document reasoning. | **Tier 1 – Tier 3** (Complex knowledge-intensive enterprise workflows). |
| ![AWS](https://img.shields.io/badge/AWS-Strands%20Agents-FF9900?style=flat-square&logo=amazonaws&logoColor=white) **AWS Strands Agents SDK** | **Apache 2.0** | [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) | Cloud-agnostic, model-driven agent harness (Python & TS) supporting Ollama, vLLM, MCP, and OpenTelemetry hooks. | **Tier 2 – Tier 3** (Self-hosted containerized agent services). |
| ![Agno](https://img.shields.io/badge/Agno-AgentOS-10B981?style=flat-square) **Agno** | **Apache 2.0** | [agno-agi/agno](https://github.com/agno-agi/agno) | High-performance Python agent runtime with built-in Postgres memory, vector knowledge, and MCP server generation. | **Tier 1 – Tier 3** (Lightweight, self-hosted multi-agent API platforms). |
| ![AutoGen](https://img.shields.io/badge/Microsoft-AutoGen%20%2F%20AG2-00A4EF?style=flat-square) **Microsoft AutoGen / AG2** | **MIT / Apache 2.0** | [microsoft/autogen](https://github.com/microsoft/autogen) | Asynchronous multi-agent conversation, Docker-sandboxed code execution, and autonomous research teams. | **Tier 1 – Tier 2** (R&D, data analysis, and multi-agent code generation). |
| ![CAMEL](https://img.shields.io/badge/CAMEL--AI-Multi--Agent-F59E0B?style=flat-square) **CAMEL-AI** | **Apache 2.0** | [camel-ai/camel](https://github.com/camel-ai/camel) | Cooperative multi-agent societies, tool-use benchmarks, and synthetic data generation pipelines. | **Tier 1 – Tier 2** (Large-scale agent simulation and synthetic data creation). |

---

## 3. Single-Agent SDKs (Apache 2.0 / MIT)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![PydanticAI](https://img.shields.io/badge/PydanticAI-Type--Safe%20Agents-E92063?style=flat-square&logo=pydantic&logoColor=white) **PydanticAI** | **MIT** | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) | Model-agnostic, strictly type-safe Python agent SDK with structured output validation and dependency injection. | **Tier 1 – Tier 3** (Enterprise backend APIs requiring strict schema guarantees). |
| ![Google](https://img.shields.io/badge/Google-ADK-4285F4?style=flat-square&logo=google&logoColor=white) **Google Agent Development Kit (ADK)** | **Apache 2.0** | [google/adk-python](https://github.com/google/adk-python) | Model-agnostic, deployment-agnostic code-first agent toolkit (Python, TS, Go, Java) with built-in Web UI & eval runner. | **Tier 1 – Tier 3** (Self-hosted Docker/Kubernetes agent engineering). |
| ![OpenAI](https://img.shields.io/badge/OpenAI-Agents%20SDK-412991?style=flat-square&logo=openai&logoColor=white) **OpenAI Agents SDK** | **MIT** | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Minimalist agent loop with handoffs and guardrails; works with any OpenAI-compatible local endpoint (vLLM/Ollama). | **Tier 1 – Tier 3** (Clean, low-overhead agent services). |
| ![Semantic Kernel](https://img.shields.io/badge/Microsoft-Semantic%20Kernel-512BD4?style=flat-square&logo=dotnet&logoColor=white) **Microsoft Semantic Kernel** | **MIT** | [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | Enterprise plugin architecture for C#/.NET, Python, and Java applications. | **Tier 2 – Tier 3** (Enterprise .NET and JVM backends). |
| ![LangChain](https://img.shields.io/badge/LangChain-Core%20%26%20Agents-1C3C3C?style=flat-square&logo=langchain&logoColor=white) **LangChain** | **MIT** | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | Standardized Runnable interface (`LCEL`), tool calling, and $1,000+$ open-source community integrations. | **Tier 1 – Tier 2** (Rapid enterprise prototyping and integration). |

---

## 4. Retrieval-Augmented Generation (RAG) & Knowledge Engines (Apache 2.0 / MIT)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![LlamaIndex](https://img.shields.io/badge/LlamaIndex-OSS%20Framework-7C3AED?style=flat-square) **LlamaIndex (OSS)** | **MIT** | [run-llama/llama_index](https://github.com/run-llama/llama_index) | Advanced chunking, hybrid vector/keyword indexing, reranking, and query decomposition over enterprise data. | **Tier 1 – Tier 3** (Scales to $100\text{M}+$ chunks with distributed vector stores). |
| ![RAGFlow](https://img.shields.io/badge/RAGFlow-Deep%20Doc%20RAG-0EA5E9?style=flat-square) **RAGFlow (Self-Hosted)** | **Apache 2.0** | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) | Turnkey self-hosted RAG server with layout-aware table/scan parsing, visual chunk inspection, and grounded citations. | **Tier 1 – Tier 2** ($10\text{K} - 5\text{M}$ complex documents; runs offline via Docker Compose). |
| ![Unstructured](https://img.shields.io/badge/Unstructured-OSS%20ETL-2563EB?style=flat-square) **Unstructured (OSS Library)** | **Apache 2.0** | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) | Local document partitioning and cleaning for PDFs, DOCX, PPTX, HTML, XLSX, and images. | **Tier 2 – Tier 3** (Batch ingestion pipelines for $1\text{ TB}+$ raw files). |
| ![Haystack](https://img.shields.io/badge/deepset-Haystack-00B388?style=flat-square) **Haystack** | **Apache 2.0** | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | Explicit, strongly-typed DAG pipelines for hybrid retrieval, document routing, and extractive/generative QA. | **Tier 2 – Tier 3** (Production search and RAG microservices). |
| ![DSPy](https://img.shields.io/badge/Stanford-DSPy-8C1515?style=flat-square) **DSPy** | **MIT** | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) | Programmatic prompt & few-shot optimization for multi-hop RAG pipelines using local or hosted models. | **Tier 2 – Tier 3** (Self-optimizing enterprise QA pipelines). |
| ![MS GraphRAG](https://img.shields.io/badge/Microsoft-GraphRAG-0078D4?style=flat-square&logo=microsoft&logoColor=white) **Microsoft GraphRAG** | **MIT** | [microsoft/graphrag](https://github.com/microsoft/graphrag) | Automated entity/relationship extraction and hierarchical community summarization for global corpus sensemaking. | **Tier 1 – Tier 2** ($1\text{K} - 500\text{K}$ documents). |
| ![LightRAG](https://img.shields.io/badge/HKUDS-LightRAG-10B981?style=flat-square) **LightRAG** | **MIT** | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) | Incremental dual-level GraphRAG with fast graph updates and low LLM extraction overhead. | **Tier 1 – Tier 2** ($10\text{K} - 2\text{M}$ dynamic documents). |
| ![Graphiti](https://img.shields.io/badge/Zep-Graphiti-6366F1?style=flat-square) **Graphiti** | **Apache 2.0** | [getzep/graphiti](https://github.com/getzep/graphiti) | Real-time temporal knowledge graph builder with bi-temporal edge invalidation for evolving enterprise facts. | **Tier 2 – Tier 3** (Continuous ingestion of changing business data). |
| ![EmbedChain](https://img.shields.io/badge/Mem0-EmbedChain-EC4899?style=flat-square) **EmbedChain** | **Apache 2.0** | [mem0ai/embedchain](https://github.com/mem0ai/embedchain) | Lightweight YAML/Python wrapper for rapid RAG ingestion across $20+$ data loaders. | **Tier 1** ($< 100\text{K}$ documents; rapid internal PoCs). |

---

## 5. Self-Hosted Embedding Models & Frameworks (Apache 2.0 / MIT)

100% private, zero-API-cost embedding generation running on enterprise CPUs, GPUs, or edge devices.

| Logo & Product | License | GitHub / Hugging Face Link | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![SentenceTransformers](https://img.shields.io/badge/UKPLab-Sentence%20Transformers-FFD21E?style=flat-square) **Sentence Transformers** | **Apache 2.0** | [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) | Training, fine-tuning, and serving dense, sparse, and multimodal embeddings with ONNX/OpenVINO/TensorRT backends. | **All Scales** (Core Python runtime for local enterprise embedding microservices). |
| ![BAAI](https://img.shields.io/badge/BAAI-BGE--M3-1E40AF?style=flat-square) **BGE-M3 (FlagEmbedding)** | **MIT** | [FlagOpen/FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) | Simultaneous dense, sparse (lexical), and ColBERT multi-vector retrieval across $100+$ languages up to $8,192$ tokens. | **Tier 2 – Tier 3** (Gold-standard self-hosted multilingual enterprise RAG). |
| ![Google](https://img.shields.io/badge/Google-EmbeddingGemma%202-4285F4?style=flat-square&logo=google&logoColor=white) **EmbeddingGemma 2** | **Apache 2.0** | [google/embeddinggemma-2](https://huggingface.co/google/embeddinggemma-2) | Compact ($740\text{M}$ params) unified multimodal embeddings (text, code, images, audio, video) with Matryoshka ($128\text{d}-768\text{d}$) truncation. | **Tier 1 – Tier 2** (Edge devices, air-gapped laptops, and low-RAM multimodal search). |
| ![Nomic](https://img.shields.io/badge/Nomic-nomic--embed-10B981?style=flat-square) **Nomic Embed (`v1.5` / `vision`)** | **Apache 2.0** | [nomic-ai/contrastors](https://github.com/nomic-ai/contrastors) | Fully open-data, open-weights $8\text{K}$-context text and vision embeddings with Matryoshka resizing. | **Tier 1 – Tier 3** (Strict open-source compliance and reproducible enterprise indexing). |
| ![HuggingFace](https://img.shields.io/badge/Hugging%20Face-TEI%20(Text%20Embeddings%20Inference)-FFD21E?style=flat-square) **Text Embeddings Inference (TEI)** | **Apache 2.0** | [huggingface/text-embeddings-inference](https://github.com/huggingface/text-embeddings-inference) | High-speed Rust inference server purpose-built for serving local embedding & reranker models with FlashAttention. | **Tier 2 – Tier 3** (High-throughput batch embedding of $1\text{ TB}+$ corpora). |

---

## 6. Model Context Protocol (MCP) Ecosystem (Apache 2.0 / MIT)

### Core SDKs & Server Frameworks
| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![MCP](https://img.shields.io/badge/Anthropic-MCP%20SDKs-000000?style=flat-square) **Official MCP SDKs** | **MIT** | [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Standardized `stdio` and `Streamable HTTP` protocol implementations for Python, TypeScript, C#, Go, and Java. | **All Scales** (Core protocol layer). |
| ![FastMCP](https://img.shields.io/badge/Prefect-FastMCP-0284C7?style=flat-square) **FastMCP** | **Apache 2.0** | [jlowin/fastmcp](https://github.com/jlowin/fastmcp) | Rapidly expose internal Python functions, REST APIs, and databases as authenticated MCP servers. | **Tier 1 – Tier 3** (Standard enterprise Python MCP server framework). |
| ![MCP Registry](https://img.shields.io/badge/MCP-Registry-4F46E5?style=flat-square) **MCP Registry** | **MIT** | [modelcontextprotocol/registry](https://github.com/modelcontextprotocol/registry) | Self-hostable metadata registry for governing approved internal MCP servers across engineering teams. | **Tier 2 – Tier 3** (Enterprise internal developer portals). |

### Remote MCP Servers (Network-Hosted via Streamable HTTP)
| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Deployment & Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![GitHub](https://img.shields.io/badge/GitHub-MCP%20Server-181717?style=flat-square&logo=github&logoColor=white) **GitHub MCP Server** | **MIT** | [github/github-mcp-server](https://github.com/github/github-mcp-server) | Self-hosted Docker or remote MCP integration for repository search, PR automation, and issue tracking. | **Remote HTTP / Containerized**; scales to $10\text{K}+$ repositories. |
| ![Slack](https://img.shields.io/badge/Slack-MCP%20Server-4A154B?style=flat-square&logo=slack&logoColor=white) **Slack MCP Server** | **MIT** | [modelcontextprotocol/servers-archived](https://github.com/modelcontextprotocol/servers) | Self-hosted bot bridge allowing internal agents to read channels and post incident alerts. | **Self-Hosted HTTP / Bot Service**; enterprise workspaces. |
| ![Google Drive](https://img.shields.io/badge/Google%20Drive-MCP%20Server-4285F4?style=flat-square&logo=googledrive&logoColor=white) **Google Drive MCP Server** | **MIT** | [piotr-agier/google-drive-mcp](https://github.com/piotr-agier/google-drive-mcp) | Self-hosted OAuth/Service-Account server exposing Google Drive, Docs, and Sheets to internal agents. | **Self-Hosted HTTP (Team Mode) or Local `stdio`**; organizational Drive search. |

### Local MCP Servers (`stdio` / VPC Sidecar)
| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Deployment & Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-MCP%20Server-4169E1?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL MCP Server** | **MIT** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Read-only SQL querying and schema exploration over internal PostgreSQL databases. | **Local `stdio` / VPC Sidecar**; multi-TB Postgres instances. |
| ![Filesystem](https://img.shields.io/badge/Filesystem-MCP%20Server-64748B?style=flat-square) **Filesystem MCP Server** | **MIT** | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Path-restricted local file operations for sandboxed coding and document processing agents. | **Local `stdio` / Container Sandbox**; single-host storage. |

---

## 7. Open-Source AI Security & PHI/PII Removers (Apache 2.0 / MIT)

### PHI / PII Detection & Redaction (Data Privacy)
| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Microsoft](https://img.shields.io/badge/Microsoft-Presidio-0078D4?style=flat-square&logo=microsoft&logoColor=white) **Microsoft Presidio** | **MIT** | [data-privacy-stack/presidio](https://github.com/data-privacy-stack/presidio) | HIPAA/GDPR PII & PHI anonymization (text & medical images) using spaCy/Transformers NER, regex, and custom recognizers. | **Tier 1 – Tier 3** (Horizontally scalable Kubernetes containers for millions of documents/day). |
| ![GLiNER](https://img.shields.io/badge/Urchade-GLiNER%20PII-10B981?style=flat-square) **GLiNER PII** | **Apache 2.0** | [urchade/GLiNER](https://github.com/urchade/GLiNER) | Fast zero-shot NER models for detecting custom enterprise PII entities without sending data to external APIs. | **Tier 1 – Tier 3** ($< 15\text{ms}$ inference; runs on CPU or GPU). |

### Runtime AI Security & Guardrails (Adversarial & Content Safety)
| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![NVIDIA](https://img.shields.io/badge/NVIDIA-NeMo%20Guardrails-76B900?style=flat-square&logo=nvidia&logoColor=white) **NVIDIA NeMo Guardrails** | **Apache 2.0** | [NVIDIA/NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Programmable input/output rails, jailbreak detection, topic control, and RAG hallucination verification. | **Tier 2 – Tier 3** (Production self-hosted LLM gateways). |
| ![Protect AI](https://img.shields.io/badge/Protect%20AI-LLM%20Guard-1E293B?style=flat-square) **LLM Guard (by Protect AI)** | **MIT** | [protectai/llm-guard](https://github.com/protectai/llm-guard) | Modular prompt injection, toxicity, secret/API-key leakage, and code-injection scanners for self-hosted LLM pipelines. | **Tier 1 – Tier 3** (Drop-in Python/API security middleware). |
| ![Guardrails AI](https://img.shields.io/badge/Guardrails%20AI-OSS%20Framework-0284C7?style=flat-square) **Guardrails AI (Core)** | **Apache 2.0** | [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Output schema validation, regex/PII checks, and structured re-asking loops. | **Tier 1 – Tier 2** (Application-level output validation). |

---

## 8. Open-Source Observability, Tracing & Evaluation (Apache 2.0 / MIT)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Langfuse](https://img.shields.io/badge/Langfuse-OSS%20Core-000000?style=flat-square) **Langfuse (OSS Edition)** | **MIT** | [langfuse/langfuse](https://github.com/langfuse/langfuse) | Full-featured self-hosted LLM tracing, prompt management, cost/token analytics, and LLM-as-a-judge evaluation on ClickHouse. | **Tier 1 – Tier 3** (ClickHouse storage scales to $100\text{M}+$ traces/month with zero license fees). |
| ![Promptfoo](https://img.shields.io/badge/Promptfoo-Red%20Teaming%20%26%20Evals-EF4444?style=flat-square) **Promptfoo** | **MIT** | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | CLI/CI-CD vulnerability scanning (prompt injection, PII leaks), regression testing, and local model benchmarking. | **Tier 1 – Tier 3** (Automated DevSecOps quality gates in GitHub Actions / GitLab CI). |
| ![Ragas](https://img.shields.io/badge/ExplodingGradients-Ragas-10B981?style=flat-square) **Ragas** | **Apache 2.0** | [explodinggradients/ragas](https://github.com/explodinggradients/ragas) | Automated RAG evaluation metrics (Faithfulness, Context Precision/Recall) using local or API judge models. | **Tier 1 – Tier 3** (Batch evaluation of enterprise RAG datasets). |
| ![Helicone](https://img.shields.io/badge/Helicone-OSS%20Proxy-0EA5E9?style=flat-square) **Helicone (Self-Hosted)** | **Apache 2.0** | [Helicone/helicone](https://github.com/Helicone/helicone) | Self-hosted AI proxy for request logging, caching, rate limiting, and latency monitoring. | **Tier 1 – Tier 3** (Centralized telemetry across self-hosted vLLM/Ollama endpoints). |
| ![TruLens](https://img.shields.io/badge/TruLens-RAG%20Evals-29B5E8?style=flat-square) **TruLens** | **MIT** | [truera/trulens](https://github.com/truera/trulens) | OpenTelemetry-compatible feedback functions for groundedness and context relevance scoring. | **Tier 1 – Tier 2** (Local Python evaluation dashboards). |
| ![OpenLLMetry](https://img.shields.io/badge/Traceloop-OpenLLMetry-4F46E5?style=flat-square) **OpenLLMetry (by Traceloop)** | **Apache 2.0** | [traceloop/openllmetry](https://github.com/traceloop/openllmetry) | Pure OpenTelemetry instrumentation exporting LLM/Agent traces directly into existing Grafana, Jaeger, or Prometheus stacks. | **Tier 2 – Tier 3** (Enterprises avoiding new observability databases by reusing Grafana/OTel). |

---

## 9. Open-Source Agent Memory & State Stores (Apache 2.0 / MIT / PostgreSQL)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Mem0](https://img.shields.io/badge/Mem0-OSS%20Memory-8B5CF6?style=flat-square) **Mem0 (OSS)** | **Apache 2.0** | [mem0ai/mem0](https://github.com/mem0ai/mem0) | Self-hosted adaptive memory layer extracting and updating user/agent preferences over Qdrant/pgvector + Neo4j/Memgraph. | **Tier 1 – Tier 3** (Stateful enterprise assistants with persistent cross-session memory). |
| ![Letta](https://img.shields.io/badge/Letta-Stateful%20Agents-000000?style=flat-square) **Letta (OSS Server)** | **Apache 2.0** | [letta-ai/letta](https://github.com/letta-ai/letta) | Self-hosted stateful agent runtime with autonomous core/archival memory editing backed by PostgreSQL. | **Tier 1 – Tier 2** (Persistent autonomous agents with unbounded conversation history). |
| ![LangGraph](https://img.shields.io/badge/LangGraph-PostgresSaver-1C3C3C?style=flat-square&logo=langchain&logoColor=white) **LangGraph Memory (`PostgresSaver` / `Store`)** | **MIT** | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Durable thread checkpointing and semantic long-term memory namespaces stored directly in PostgreSQL. | **Tier 1 – Tier 3** (Zero-additional-infra state persistence for LangGraph deployments). |
| ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-State%20%26%20Memory-4169E1?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL** | **PostgreSQL License** | [postgres/postgres](https://github.com/postgres/postgres) | ACID-compliant transactional memory, audit logs, and relational + vector storage. | **Tier 1 – Tier 3** (Up to $10\text{ TB}+$ operational enterprise databases). |
| ![Valkey](https://img.shields.io/badge/Linux%20Foundation-Valkey-2563EB?style=flat-square) **Valkey (OSS Redis Fork)** | **BSD-3-Clause** | [valkey-io/valkey](https://github.com/valkey-io/valkey) | Permissive BSD-licensed in-memory store for sub-millisecond agent working memory, rate limiting, and caching. | **Tier 2 – Tier 3** ($100\text{K}+$ QPS real-time state without Redis SSPL/RSAL licensing restrictions). |
| ![Chroma](https://img.shields.io/badge/Chroma-Episodic%20Memory-FF6446?style=flat-square) **Chroma** | **Apache 2.0** | [chroma-core/chroma](https://github.com/chroma-core/chroma) | Embedded or single-node semantic memory store for past agent trajectories and tool results. | **Tier 1 – Tier 2** ($< 50\text{M}$ memory vectors). |

---

## 10. Open-Source Vector Databases & Search Engines (Apache 2.0 / BSD / PostgreSQL)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Milvus](https://img.shields.io/badge/Milvus-Distributed%20Vector-00A1EA?style=flat-square) **Milvus (LF AI & Data)** | **Apache 2.0** | [milvus-io/milvus](https://github.com/milvus-io/milvus) | Cloud-native, Kubernetes-orchestrated distributed vector DB with separated compute/storage, GPU indexing, and hybrid search. | **Tier 3 (Billion-Scale)** ($100\text{M} - 10\text{B}+$ vectors / $1\text{ TB} - 1\text{ PB}$; unmatched self-hosted scale). |
| ![Qdrant](https://img.shields.io/badge/Qdrant-Rust%20Vector%20DB-DC244C?style=flat-square) **Qdrant** | **Apache 2.0** | [qdrant/qdrant](https://github.com/qdrant/qdrant) | High-throughput Rust vector engine with advanced metadata filtering, scalar/binary quantization, and distributed clustering. | **Tier 1 – Tier 3** ($500\text{K} - 500\text{M}$ vectors; easiest production binary to operate on K8s). |
| ![Weaviate](https://img.shields.io/badge/Weaviate-Hybrid%20Vector%20DB-01CC67?style=flat-square) **Weaviate** | **BSD-3-Clause** | [weaviate/weaviate](https://github.com/weaviate/weaviate) | Native BM25 + HNSW hybrid search, multi-tenancy, and GraphQL/REST APIs in a single Go binary. | **Tier 1 – Tier 2** ($1\text{M} - 100\text{M}$ vectors; best OSS hybrid keyword + vector retrieval). |
| ![pgvector](https://img.shields.io/badge/pgvector-PostgreSQL%20Extension-4169E1?style=flat-square&logo=postgresql&logoColor=white) **pgvector / pgvectorscale** | **PostgreSQL License** | [pgvector/pgvector](https://github.com/pgvector/pgvector) | Adds HNSW and StreamingDiskANN vector indexing directly into existing enterprise PostgreSQL clusters. | **Tier 1 – Tier 2** ($< 50\text{M}$ vectors; eliminates dual-database sync complexity). |
| ![OpenSearch](https://img.shields.io/badge/OpenSearch-Search%20%26%20Vector-005EB8?style=flat-square) **OpenSearch** | **Apache 2.0** | [opensearch-project/OpenSearch](https://github.com/opensearch-project/OpenSearch) | Distributed BM25 + k-NN vector + neural sparse search engine for massive enterprise document and log repositories. | **Tier 2 – Tier 3** ($1\text{ TB} - 1\text{ PB}$ enterprise search clusters). |
| ![Chroma](https://img.shields.io/badge/Chroma-Embedded%20%26%20Server-FF6446?style=flat-square) **Chroma** | **Apache 2.0** | [chroma-core/chroma](https://github.com/chroma-core/chroma) | Zero-setup embedded Python/JS database and lightweight single-node Docker vector server. | **Tier 1 – Tier 2** ($< 10\text{M}$ vectors; local development and departmental RAG). |
| ![LanceDB](https://img.shields.io/badge/LanceDB-Serverless%20Columnar-F59E0B?style=flat-square) **LanceDB** | **Apache 2.0** | [lancedb/lancedb](https://github.com/lancedb/lancedb) | Disk-based columnar vector & multimodal lakehouse format (S3/object-storage backed) with zero-copy Arrow integration. | **Tier 1 – Tier 3** ($1\text{ TB}+$ multimodal datasets stored directly on S3/MinIO without high RAM bills). |

---

## 11. Open-Source Workflow Automation & Durable Orchestration (Apache 2.0 / MIT)

*(Note: n8n is excluded here due to its Fair-Code Sustainable Use License; the tools below are 100% Apache 2.0 / MIT).*

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Temporal](https://img.shields.io/badge/Temporal-Durable%20Execution-111827?style=flat-square) **Temporal (Self-Hosted)** | **MIT** | [temporalio/temporal](https://github.com/temporalio/temporal) | Code-first durable execution guaranteeing stateful AI agents survive API timeouts, rate limits, and pod restarts. | **Tier 2 – Tier 3** (Mission-critical enterprise agent orchestration at massive scale). |
| ![Apache Airflow](https://img.shields.io/badge/Apache-Airflow-017CEE?style=flat-square&logo=apacheairflow&logoColor=white) **Apache Airflow** | **Apache 2.0** | [apache/airflow](https://github.com/apache/airflow) | Enterprise batch DAG scheduler for automated document crawling, chunking, embedding, and vector index updates. | **Tier 2 – Tier 3** ($1\text{ TB} - 1\text{ PB}$ scheduled RAG ingestion & ML pipelines). |
| ![Prefect](https://img.shields.io/badge/Prefect-OSS%20Orchestrator-024DFD?style=flat-square) **Prefect (OSS Server)** | **Apache 2.0** | [PrefectHQ/prefect](https://github.com/PrefectHQ/prefect) | Self-hosted Python workflow orchestration with dynamic task mapping, retries, and real-time UI. | **Tier 1 – Tier 3** (Python AI data ingestion and batch evaluation pipelines). |
| ![Kestra](https://img.shields.io/badge/Kestra-OSS%20Orchestrator-8405FF?style=flat-square) **Kestra (OSS Edition)** | **Apache 2.0** | [kestra-io/kestra](https://github.com/kestra-io/kestra) | Event-driven & scheduled declarative YAML orchestrator with hundreds of open-source plugins and built-in UI. | **Tier 2 – Tier 3** (Enterprise polyglot automation replacing proprietary low-code runners). |
| ![Activepieces](https://img.shields.io/badge/Activepieces-MIT%20Automation-6366F1?style=flat-square) **Activepieces (MIT Core)** | **MIT** | [activepieces/activepieces](https://github.com/activepieces/activepieces) | Permissively licensed (MIT) open-source visual no-code workflow & AI automation alternative to Zapier/n8n. | **Tier 1 – Tier 2** (Self-hosted visual SaaS/AI workflow builder with zero Fair-Code restrictions). |

---

## 12. Additional Open-Source Enterprise Infrastructure (Apache 2.0 / MIT)

| Category | Logo & Product | License | GitHub Repository | Enterprise Use Cases & Scale |
| :--- | :--- | :--- | :--- | :--- |
| **AI Gateway** | ![LiteLLM](https://img.shields.io/badge/BerriAI-LiteLLM-2563EB?style=flat-square) **LiteLLM Proxy** | **MIT** | [BerriAI/litellm](https://github.com/BerriAI/litellm) | Unified OpenAI-compatible gateway routing across vLLM, Ollama, and cloud APIs with rate limiting & fallbacks (**Tier 1 – Tier 3**). |
| **AI Gateway** | ![Portkey](https://img.shields.io/badge/Portkey-OSS%20Gateway-6366F1?style=flat-square) **Portkey AI Gateway** | **MIT** | [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) | Ultra-low-latency TypeScript/Node gateway with load balancing, retries, and guardrails hooks (**Tier 2 – Tier 3**). |
| **Doc Parsing** | ![Docling](https://img.shields.io/badge/IBM-Docling-054ADA?style=flat-square&logo=ibm&logoColor=white) **IBM Docling** | **MIT** | [docling-project/docling](https://github.com/docling-project/docling) | Local GPU/CPU PDF layout, table, and OCR parser converting complex enterprise docs to Markdown/JSON (**Tier 1 – Tier 3**). |
| **Sandboxing** | ![E2B](https://img.shields.io/badge/E2B-Open%20Infra-F97316?style=flat-square) **E2B Infrastructure & SDK** | **Apache 2.0** | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) | Firecracker microVM orchestration for isolated AI code execution (**Tier 1 – Tier 3**). |
| **Reranking** | ![FlashRank](https://img.shields.io/badge/Prithiviraj-FlashRank-10B981?style=flat-square) **FlashRank / BGE-Reranker** | **Apache 2.0 / MIT** | [PrithivirajDamodaran/FlashRank](https://github.com/PrithivirajDamodaran/FlashRank) | Ultra-fast CPU/ONNX cross-encoder reranking improving RAG precision by $15-25\%$ (**Tier 1 – Tier 3**). |
| **Media / Diffusion** | ![Diffusers](https://img.shields.io/badge/Hugging%20Face-Diffusers-FFD21E?style=flat-square&logo=huggingface&logoColor=black) **Hugging Face Diffusers** | **Apache 2.0** *(weights carry separate licenses)* | [huggingface/diffusers](https://github.com/huggingface/diffusers) | Programmatic Python pipelines for image, video, and audio diffusion generation inside permissive enterprise services (**Tier 1 – Tier 3**). |

#### Copyleft Multimodal Workflow Engine (Reference Only — Excluded from Strict Stack)

| Engine | License (Exclusion Reason) | Ecosystem Role | Permissive Replacement in This Guide |
| :--- | :--- | :--- | :--- |
| ![ComfyUI](https://img.shields.io/badge/ComfyUI-Workflow%20Engine-0F172A?style=flat-square) **ComfyUI** ([Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)) | GPLv3 (copyleft) | Visual node-graph workflow engine and headless API server for open-weight diffusion, video, audio, and 3D generation. | **Hugging Face Diffusers** (`Apache 2.0`) for programmatic pipelines *(or run ComfyUI only if legal approves GPLv3 / isolated service boundaries)* |

---

## 13. Collaborative Knowledge Workspaces & Human-in-the-Loop Action Targets (MIT / BSD)

*(Note: **Notion** [Commercial SaaS], **AppFlowy** [AGPL-3.0 + separate self-hosted commercial server terms], **Outline** [BSL 1.1], and **Docmost** [AGPL-3.0 core + Enterprise] are excluded from the strictly permissive Apache 2.0 / MIT / BSD stack below, but are analyzed in the ecosystem overview and comparison table for architectural reference).*

### Where AppFlowy & Notion Fit in the Ecosystem

Rather than replacing your vector database, LLM gateway, or agent orchestrator, tools like Notion and AppFlowy act as structured human knowledge stores and action targets:

* **Knowledge Source for RAG & Memory:** Docs, wikis, SOPs, runbooks, meeting notes, and relational tables are exported or synced into your ingestion/chunking pipeline and vector database for grounded Q&A.
* **Tool & Action Layer via MCP:** Through MCP servers, AI agents (e.g., LangGraph, PydanticAI, Claude/IDE agents) can read workspace trees, search pages, summarize threads, create specs/runbooks, and update databases. Notion provides an official hosted MCP endpoint ([https://mcp.notion.com/mcp](https://mcp.notion.com/mcp)), while AppFlowy integrates with agents via community/self-hosted MCP servers that interact with AppFlowy Cloud APIs or decode Yjs CRDT pages. In a 100% permissive stack, self-hosted wikis and Git-backed Markdown portals fulfill the same role via `FastMCP` API wrappers or `Filesystem` / `GitHub` MCP servers.
* **Human-in-the-Loop & Artifact Destination:** Agents draft PRDs, release trackers, incident summaries, or structured tables directly into the workspace where humans review, edit, and approve them.

### Strictly Permissive Self-Hosted Knowledge & Wiki Platforms (MIT / BSD)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![BookStack](https://img.shields.io/badge/BookStack-MIT%20Wiki-0288D1?style=flat-square) **BookStack** | **MIT** | [BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) | Self-hosted team wiki (`Shelves → Books → Chapters → Pages`) with WYSIWYG/Markdown editing, RBAC, LDAP/OIDC/SAML SSO, and REST API for RAG ingestion and custom `FastMCP` servers. | **Tier 1 – Tier 2** (Self-hosted enterprise knowledge bases with zero AGPL/BSL restrictions). |
| ![Docusaurus](https://img.shields.io/badge/Meta-Docusaurus-2E8555?style=flat-square&logo=docusaurus&logoColor=white) **Docusaurus** | **MIT** | [facebook/docusaurus](https://github.com/facebook/docusaurus) | Git-backed Markdown/MDX documentation portal with versioning and search; ideal for docs-as-code RAG pipelines and PR-reviewed human-in-the-loop agent drafts. | **Tier 1 – Tier 3** (Versioned engineering docs, SOPs, and internal developer portals). |
| ![MkDocs](https://img.shields.io/badge/MkDocs-Docs--as--Code-526CFE?style=flat-square) **MkDocs** | **BSD-2-Clause** | [mkdocs/mkdocs](https://github.com/mkdocs/mkdocs) | Lightweight Python static documentation generator over plain Git Markdown; effortlessly synced into vector stores or exposed to agents via `Filesystem` / `GitHub` MCP servers. | **Tier 1 – Tier 3** (Air-gapped technical documentation and runbook repositories). |

### Comparison: AppFlowy vs. Notion & Permissive Alternatives

| Tool / Platform | Ecosystem Role | License / Model | Best Enterprise Fit & Scale |
| :--- | :--- | :--- | :--- |
| ![Notion](https://img.shields.io/badge/Notion-Workspace%20%26%20MCP-000000?style=flat-square&logo=notion&logoColor=white) **Notion** ([notion.so](https://www.notion.so)) *(Excluded from strict OSS)* | Cloud collaborative docs, wikis, project databases & official MCP ([mcp.notion.com/mcp](https://mcp.notion.com/mcp)) | Commercial SaaS (Enterprise plans; official remote MCP) | **Full / Commercial stack (Tier 1 – Tier 3).** Great for fast cross-team adoption, structured project/wiki workflows, and OAuth-managed MCP agent access; less suited when air-gapped on-prem or strict open-source licensing is required. |
| ![AppFlowy](https://img.shields.io/badge/AppFlowy-Self--Hosted%20Workspace-8427E0?style=flat-square) **AppFlowy** ([AppFlowy-IO/AppFlowy](https://github.com/AppFlowy-IO/AppFlowy)) *(Excluded from strict OSS)* | Self-hostable Notion-style workspace, docs & relational databases with local/on-prem AI support | AGPL-3.0 (open-source client/core; separate self-hosted commercial license terms) | **Full / OSS + Commercial stack (Tier 1 – Tier 2).** Good fit when you want a self-hosted Notion-like workspace with local/BYO LLMs, provided your legal team accepts AGPL-3.0 / commercial server licensing. |
| ![Wikis](https://img.shields.io/badge/Outline%20%2F%20Docmost-Team%20Wikis-0EA5E9?style=flat-square) **Outline / Docmost** ([outline/outline](https://github.com/outline/outline) / [docmost/docmost](https://github.com/docmost/docmost)) *(Excluded from strict OSS)* | Self-hosted team wikis & documentation (lighter on heavy databases than Notion/AppFlowy) | Varies by repo/edition (e.g., Outline BSL 1.1; Docmost AGPL-3.0 core + Enterprise — verify exact license per release) | **Knowledge / Wiki tier (Tier 1 – Tier 2).** Better if your primary need is clean engineering/company documentation and RAG ingestion rather than full relational database apps. |
| ![Permissive Wikis](https://img.shields.io/badge/BookStack%20%2F%20Docusaurus%20%2F%20MkDocs-Permissive%20OSS-10B981?style=flat-square) **BookStack / Docusaurus / MkDocs** ([BookStackApp/BookStack](https://github.com/BookStackApp/BookStack) / [facebook/docusaurus](https://github.com/facebook/docusaurus) / [mkdocs/mkdocs](https://github.com/mkdocs/mkdocs)) | Strictly permissive self-hosted team wiki (BookStack) and Git-backed docs-as-code portals (Docusaurus, MkDocs) for frictionless RAG & MCP syncing | **MIT** (BookStack, Docusaurus) / **BSD-2-Clause** (MkDocs) — 100% permissive open source | **Strict Permissive OSS / Air-Gapped stack (Tier 1 – Tier 3).** Best fit for this guide's strict permissive policy when SaaS, AGPL-3.0, and BSL 1.1 are disallowed. |

---

## 14. Document Ingestion, Deduplication & Evolving / Temporal Knowledge Graphs (Apache 2.0 / MIT / PostgreSQL)

*(Note: **Zep Cloud** [Commercial SaaS], **Neo4j** [GPLv3 Community / Commercial Enterprise], and **XTDB** [MPL-2.0 weak file-level copyleft] are excluded from the strictly permissive Apache 2.0 / MIT / BSD / PostgreSQL stack below, but are summarized in the reference note for architectural comparison. Pair permissive frameworks with **PostgreSQL + Apache AGE** or **LadybugDB** to keep the full stack 100% permissive).*

To handle scattered, duplicated, and occasionally inaccurate documents while building knowledge incrementally, keeping current truth, and querying/explaining how facts or policies changed over time, standard vector-only RAG usually falls short. Flat vector chunks retrieve semantically similar passages without reliably merging duplicate entities, invalidating outdated rules, or preserving exact historical timelines.

The strongest approach combines **incremental entity/fact extraction + deduplication** with a **temporal or bi-temporal knowledge graph** (tracking both when a policy/fact was true in the real world and when the system ingested or superseded it, while keeping provenance links back to source documents).

### 1. Strictly Permissive Platforms, Frameworks & SDKs (Apache 2.0 / MIT / PostgreSQL)

| Platform / SDK | License | Role & Strengths for This Problem | Temporal & Evolution Model | Best Fit |
| :--- | :--- | :--- | :--- | :--- |
| ![Graphiti](https://img.shields.io/badge/Zep-Graphiti-6366F1?style=flat-square) **Graphiti** ([getzep/graphiti](https://github.com/getzep/graphiti)) | **Apache 2.0** *(verify graph backend license)* | Open-source SDK/framework for real-time, incremental temporal knowledge graphs for AI agents. Updates incrementally as new "episodes" arrive without full batch rebuilds, and traces derived facts back to source episodes. | Bi-temporal edge model: tracks valid intervals and ingestion/expiration timestamps, invalidating superseded edges rather than erasing history. | **Tier 1 – Tier 3.** Custom agent/knowledge stacks needing point-in-time queries ("what was the policy in Q1?") and full source provenance. |
| ![Cognee](https://img.shields.io/badge/Cognee-Graph%20Memory-7C3AED?style=flat-square) **Cognee (OSS)** ([topoteretes/cognee](https://github.com/topoteretes/cognee)) | **Apache 2.0** | Graph-native memory and knowledge platform combining knowledge graphs + vector search in a unified ingestion (`cognify`) pipeline with entity extraction, graph traversal, and time-aware memory. | Supports graph-backed memory, entity/relationship tracking, and temporal/history workflows alongside semantic retrieval. | **Tier 1 – Tier 2.** Hybrid semantic + multi-hop graph retrieval where facts evolve and require structured relationships plus vector recall. |
| ![LightRAG](https://img.shields.io/badge/HKUDS-LightRAG-10B981?style=flat-square) **LightRAG** ([HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)) | **MIT** | Graph-based indexing and retrieval framework that extracts entities/relationships from chunks, performs entity/relation deduplication, and pairs graph structures with key-value/embedding retrieval (supports PostgreSQL + Apache AGE and NetworkX). | Focuses on incremental graph construction and entity/relation deduplication across segmented text. | **Tier 1 – Tier 2.** Teams building custom graph-enhanced RAG pipelines needing entity/edge deduplication and multi-hop context. |
| ![Mem0 & Letta](https://img.shields.io/badge/Mem0%20%26%20Letta-Agent%20Memory-8B5CF6?style=flat-square) **Mem0 (OSS) & Letta (OSS)** ([mem0ai/mem0](https://github.com/mem0ai/mem0) / [letta-ai/letta](https://github.com/letta-ai/letta)) | **Apache 2.0** | Self-hosted agent memory layers/frameworks for persistent and evolving agent state (including graph-enhanced memory variants such as `Mem0g` and stateful agent memory management). | Primarily focused on evolving agent/user memory and retrieval; pair with a temporal graph/store when strict historical policy traversal is required. | **Tier 1 – Tier 3.** Conversational/operational agents accumulating preferences, facts, and state across sessions. |
| ![Apache AGE](https://img.shields.io/badge/PostgreSQL-Apache%20AGE-4169E1?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL + Apache AGE** ([postgres/postgres](https://github.com/postgres/postgres) / [apache/age](https://github.com/apache/age)) | **PostgreSQL License / Apache 2.0** | Unified permissive relational + Cypher property-graph + `pgvector` database replacing Neo4j/XTDB in strict permissive environments. | Models explicit temporal validity on graph edges and append-only bitemporal audit tables via `tstzrange` valid/system-time columns and `btree_gist` exclusion constraints. | **Tier 1 – Tier 3.** Strict Apache/MIT/BSD/PostgreSQL stacks needing governed entity graphs, ACID provenance, and bitemporal audit reconstruction without copyleft licenses. |
| ![LadybugDB](https://img.shields.io/badge/LadybugDB-Embedded%20Graph-E11D48?style=flat-square) **LadybugDB** *(Kùzu successor)* ([LadybugDB/ladybug](https://github.com/LadybugDB/ladybug)) | **MIT** | Embedded columnar property graph database supporting Cypher, vector/full-text search, and Arrow/Parquet integration (active community fork of archived `kuzudb/kuzu`, used with local Cognee/GraphRAG setups). | Supports explicit temporal edge attributes (`valid_from`, `valid_until`, `ingested_at`) in local-first embedded graphs. | **Tier 1 – Tier 2.** Local-first, air-gapped, or serverless embedded knowledge graphs without operating a separate graph cluster. |

#### Non-Permissive / Copyleft Temporal & Graph Engines (Reference Only — Excluded from Strict Stack)

| Platform / Engine | License (Exclusion Reason) | Ecosystem Role & Temporal Model | Permissive Replacement in This Guide |
| :--- | :--- | :--- | :--- |
| ![Zep](https://img.shields.io/badge/Zep-Context%20Engine-3B82F6?style=flat-square) **Zep** ([getzep/zep](https://github.com/getzep/zep)) | Commercial Cloud (+ Apache 2.0 SDKs & archived CE) | Managed temporal knowledge-graph memory platform tracking validity and provenance across episodes. | **Graphiti** (`Apache 2.0`) self-hosted |
| ![Neo4j](https://img.shields.io/badge/Neo4j-Graph%20DB-008CC1?style=flat-square&logo=neo4j&logoColor=white) **Neo4j** ([neo4j/neo4j](https://github.com/neo4j/neo4j)) | GPLv3 (Community) + Commercial Enterprise | Enterprise graph DB widely used as a GraphRAG/Graphiti backing store with schema-level temporal validity windows. | **PostgreSQL + Apache AGE** (`Apache 2.0`) or **LadybugDB** (`MIT`) |
| ![XTDB](https://img.shields.io/badge/XTDB-Bitemporal%20DB-0F766E?style=flat-square) **XTDB** ([xtdb/xtdb](https://github.com/xtdb/xtdb)) | MPL-2.0 (weak file-level copyleft) | Immutable bitemporal database engine natively tracking valid time and system/transaction time for exact point-in-time audit reconstruction. | **PostgreSQL** (`PostgreSQL License`) append-only `tstzrange` bitemporal ledger *(or evaluate MPL-2.0 if legal allows file-level copyleft)* |

### 2. How to Handle Scattered Duplicates, Bad Info & "Explain What Changed"

No single library automatically knows which of two conflicting memos is "true" without rules and provenance. In practice, wire together four capabilities:

* **Pre-Ingestion Deduplication & Delta Detection:**
  * Hash normalized documents/chunks and track source version IDs/timestamps so identical duplicates are skipped and only added, modified, or deleted items trigger re-processing.
  * Run entity and relation resolution (merging variants like `"US Remote Work Policy"`, `"Remote Work Policy v2"`, or aliases) so duplicate mentions map to the same canonical node.
* **Superseding Instead of Destructive Overwrites:**
  * When a newer or authoritative document contradicts an older policy edge/fact, close the old fact's validity window (`valid_until` / `superseded`) and open a new edge rather than deleting the old one.
  * Keep source provenance (document ID, section, effective date, ingestion date) on every extracted claim so you can trace where a fact came from.
* **Handling "Slightly Wrong" or Noisy Documents:**
  * Assign source trust / authority tiers (e.g., `Approved Policy / Signed SOP > Draft / Meeting Notes / Chat`) and require human review or quarantine flags when a low-trust source contradicts a high-trust source.
  * Allow retroactive valid-time corrections when a late document clarifies that a rule actually changed on an earlier date, while keeping the ingestion log intact for auditability.
* **Explaining Changes Over Time to the User:**
  * Query the graph/store for all versions of a topic or edge ordered by effective/valid date (e.g., `version 1 -> version 2 -> current`), pulling the diff between states plus the citing source documents.
  * Have the LLM synthesize a structured timeline: what the rule was, when and how it changed, which source introduced the change, and what applies today.

### 3. Practical Starting Stack (100% Permissive OSS)

* **Temporal entity/fact graphs + provenance:** **Graphiti** (`Apache 2.0`) or **LightRAG** (`MIT`) paired with **PostgreSQL + Apache AGE** (`PostgreSQL License / Apache 2.0`) to avoid Neo4j's `GPLv3` / Commercial terms and Zep's Commercial Cloud. *(Note: verify native Graphiti graph driver support when selecting a backend, as Graphiti officially targets Neo4j/FalkorDB/Neptune).*
* **Hybrid semantic + graph knowledge base:** **Cognee (OSS)** (`Apache 2.0`, backed by **LadybugDB** [`MIT`] or **NetworkX** [`BSD-3-Clause`]) or **LightRAG** (`MIT`), paired with an incremental ingestion/change-detection pipeline and source metadata/trust tags.
* **Strict bitemporal compliance/audit ledger:** **PostgreSQL** (`PostgreSQL License`) append-only `tstzrange` valid-time/system-time tables alongside your document/graph store when policy forbids **XTDB** (`MPL-2.0`).

---

## 15. Open-Source Graph Databases & RDF Triplestores (Apache 2.0 / MIT / BSD / PostgreSQL)

*(Note: **Neo4j** [GPLv3 Community / Commercial Enterprise], **Ontotext GraphDB Free** [Proprietary Free-to-Use Tier — not OSI open source], and managed cloud graph services [**Amazon Neptune**, **Azure Cosmos DB**, **Google Cloud Spanner Graph**] are excluded from the strictly permissive Apache 2.0 / MIT / BSD / PostgreSQL stack below, and are summarized in the reference comparison table for architectural parity. Ontology editors and enterprise context layers sit above these stores in **Section 16**).*

> **Architectural Clarification — RDF Triplestores vs. Property Graph Databases (and Ontologies in Section 16):**
> * **RDF Triplestores** (e.g., *Apache Jena*) store W3C subject–predicate–object triples, query via **SPARQL 1.1/1.2**, and support formal OWL/RDFS/SHACL semantic inference and Linked Data URIs.
> * **Labeled Property Graph (LPG) Databases** (e.g., *PostgreSQL + Apache AGE*, *LadybugDB*) model nodes and edges with key-value properties, queried via **Cypher** for GraphRAG, multi-hop traversal, and entity-relationship memory.
> * **Enterprise Context Layers & Ontology Modeling SDKs** (e.g., *NVIDIA Auto-Ontology*, *AWS Context Ontology Accelerator*, *LinkML*, *Protégé*, *RDFLib/pySHACL*) sit above these storage engines and are covered in **Section 16**.

### Strictly Permissive Graph Databases & RDF Triplestores

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Apache Jena](https://img.shields.io/badge/Apache%20Jena-RDF%20%26%20Fuseki-D22128?style=flat-square) **Apache Jena (TDB2 & Fuseki)** | **Apache 2.0** | [apache/jena](https://github.com/apache/jena) | W3C RDF triplestore (`TDB2`), `Fuseki` SPARQL HTTP server, and OWL/RDFS/SHACL inference engine for governed enterprise semantic knowledge graphs. | **Tier 1 – Tier 3** ($100\text{M} - 1\text{B}+$ RDF triples per TDB2 node; zero-lock-in SPARQL endpoint). |
| ![PostgreSQL + Apache AGE](https://img.shields.io/badge/PostgreSQL-Apache%20AGE-4169E1?style=flat-square&logo=postgresql&logoColor=white) **PostgreSQL + Apache AGE** | **PostgreSQL License / Apache 2.0** | [apache/age](https://github.com/apache/age) | Unified ACID relational + openCypher property-graph + `pgvector` database replacing Neo4j in strict permissive environments. | **Tier 1 – Tier 3** ($10\text{ TB}+$ enterprise Postgres clusters combining SQL, Cypher, and vector search). |
| ![LadybugDB](https://img.shields.io/badge/LadybugDB-Embedded%20Graph-E11D48?style=flat-square) **LadybugDB** *(Kùzu successor)* | **MIT** | [LadybugDB/ladybug](https://github.com/LadybugDB/ladybug) | Embedded columnar property graph database supporting Cypher, vector/full-text search, and Arrow/Parquet integration for local/air-gapped GraphRAG. | **Tier 1 – Tier 2** (Local-first, air-gapped, or serverless embedded knowledge graphs without a separate DB cluster). |

#### Non-Permissive, Proprietary Free-Tier & Managed Cloud Graph Services (Reference Only — Excluded from Strict Stack)

| Platform / Engine | License (Exclusion Reason) | Ecosystem Role & Graph Model | Permissive Replacement in This Guide |
| :--- | :--- | :--- | :--- |
| ![Neo4j](https://img.shields.io/badge/Neo4j-Graph%20DB-008CC1?style=flat-square&logo=neo4j&logoColor=white) **Neo4j** ([neo4j/neo4j](https://github.com/neo4j/neo4j)) | GPLv3 (Community) + Commercial Enterprise / AuraDB | Enterprise Labeled Property Graph DB (Cypher / ISO GQL) with built-in vector/full-text indexes and Graph Data Science (GDS). | **PostgreSQL + Apache AGE** (`Apache 2.0`) or **LadybugDB** (`MIT`) |
| ![GraphDB](https://img.shields.io/badge/Ontotext-GraphDB%20Free-1E293B?style=flat-square) **Ontotext GraphDB Free** ([ontotext.com/products/graphdb](https://www.ontotext.com/products/graphdb/)) | Proprietary Free-to-Use Tier *(not OSI open source; registration key required as of v11+, capped at 2 concurrent queries)* | W3C RDF/SPARQL triplestore with OWL/RDFS reasoning, RDF-star provenance, and vector/full-text indexing. | **Apache Jena (TDB2 & Fuseki)** (`Apache 2.0`) + **Protégé** (`BSD-2-Clause`) |
| ![Amazon Neptune](https://img.shields.io/badge/AWS-Amazon%20Neptune-FF9900?style=flat-square&logo=amazonaws&logoColor=white) **Amazon Neptune** ([aws.amazon.com/neptune](https://aws.amazon.com/neptune/)) | Commercial Managed Service (AWS) | Dual-model managed graph DB supporting Property Graphs (`openCypher`, `Gremlin`) and W3C RDF (`SPARQL`), plus Neptune Analytics. | **PostgreSQL + Apache AGE** (`Apache 2.0`, for LPG) and/or **Apache Jena Fuseki** (`Apache 2.0`, for RDF/SPARQL) |
| ![Azure Cosmos DB](https://img.shields.io/badge/Azure-Cosmos%20DB%20Gremlin-0078D4?style=flat-square&logo=microsoftazure&logoColor=white) **Azure Cosmos DB (for Apache Gremlin)** ([azure.microsoft.com/products/cosmos-db](https://azure.microsoft.com/products/cosmos-db)) | Commercial Managed Service (Azure) | Globally distributed, multi-model managed NoSQL/graph service exposing the Apache TinkerPop `Gremlin` API with multi-region replication. | **PostgreSQL + Apache AGE** (`Apache 2.0`) for Cypher property graphs *(or **Apache TinkerPop / JanusGraph** [`Apache 2.0`] when Gremlin is required)* |
| ![Google Cloud Spanner Graph](https://img.shields.io/badge/Google%20Cloud-Spanner%20Graph-4285F4?style=flat-square&logo=googlecloud&logoColor=white) **Google Cloud Spanner Graph** ([cloud.google.com/spanner/docs/graph/overview](https://cloud.google.com/spanner/docs/graph/overview)) | Commercial Managed Service (GCP) | Globally consistent distributed ISO GQL + SQL unified relational/graph DB with declarative table-to-graph mapping and built-in vector/full-text search. | **PostgreSQL + Apache AGE + pgvector** (`PostgreSQL / Apache 2.0`) for unified relational + property graph + vector workloads |

---

## 16. Open-Source Enterprise Context Layer & AI Ontologies (Apache 2.0 / BSD)

*(Note: **Databricks Genie Ontology** [Commercial Managed Service], **AWS Context** [Managed Service], **Palantir Foundry Ontology (AIP)** [Commercial Enterprise Platform], **Microsoft Fabric IQ & Ontology** [Commercial Managed Service], and **Owlready2** [LGPL-3.0 weak copyleft] are excluded from the strictly permissive Apache 2.0 / MIT / BSD stack below, and are summarized in the reference comparison table with permissive replacements).*

Raw warehouse tables, data lakes, and flat vector chunks cause AI agents to hallucinate—because schema columns (`rev_amt`, `cust_id`), conflicting departmental KPIs, undocumented joins, and access policies are invisible to an LLM at prompt time. An **Enterprise Context Layer** powered by an **Ontology** bridges raw enterprise data to governed, deterministic AI agents using open standards and self-hosted infrastructure.

### 1. Semantic Layer vs. Ontology vs. Context Layer

They overlap, **but they are not the same**: in modern enterprise AI architecture, a **Semantic Layer** is one foundational ingredient *inside* a broader **Context Layer**, while an **Ontology** provides the formal entity, relationship, rule, and action model tying structured and unstructured context together.

| Layer | Primary Consumer | Core Scope | Typical Examples (Permissive OSS First) |
| :--- | :--- | :--- | :--- |
| **Semantic Layer** | BI dashboards, SQL analysts, Text-to-SQL | **Structured metrics & joins:** canonical KPI formulas (`ARR`, `Churn`), dimensions, grain, and rollups over warehouse tables. | `Cube Core` (`Apache 2.0`), `dbt MetricFlow` (`Apache 2.0`) *(commercial ref: LookML, Power BI Semantic Models, Unity Catalog Metric Views)* |
| **Ontology** | Knowledge graphs, formal reasoners, operational apps & agents | **Business world model:** formal entity types, multi-hop relationships, inheritance, validation rules (`OWL 2` / `SHACL` / `LinkML`), and authorized **actions**. | `Protégé` (`BSD-2-Clause`), `LinkML` (`Apache 2.0`), `OpenSPG / KAG` (`Apache 2.0`) *(commercial ref: Palantir Foundry Ontology)* |
| **Context Layer** | AI agents & copilots (typically via **MCP**) | **Unified runtime brain for AI:** combines the **Semantic Layer** (metrics) + **Ontology** (entities/rules/actions) + **unstructured & learned context** (SOPs, wikis, past queries, authority ranking) + **runtime governance** (per-user RBAC, row/column masking, provenance). | `NVIDIA Auto-Ontology` (`Apache 2.0`), `AWS Context Ontology Accelerator` (`Apache 2.0`) *(commercial ref: Databricks Genie Ontology, AWS Context, Microsoft Fabric IQ)* |

```text
AI Agents (Claude, LangGraph, PydanticAI, Custom Agents via MCP)
                              ▲
┌─────────────────────────────┴─────────────────────────────┐
│                    ENTERPRISE CONTEXT LAYER               │
│  Governance (RBAC/RLS) • Authority Ranking • FastMCP      │
│  ┌──────────────────────┐   ┌──────────────────────────┐  │
│  │    Semantic Layer    │ + │         Ontology         │  │
│  │ (KPIs, Metrics, SQL) │   │ (Entities, Rules, Links) │  │
│  └──────────────────────┘   └──────────────────────────┘  │
│              + Unstructured Docs & Learned Usage          │
└─────────────────────────────┬─────────────────────────────┘
                              ▼
    Raw Enterprise Data (Postgres, Lakehouses, Graph DBs, Wikis)
```

* **When a Semantic Layer alone suffices:** If you only need consistent BI numbers and accurate Text-to-SQL over clean warehouse tables, a permissive Semantic Layer (`Cube Core` or `dbt MetricFlow`, both `Apache 2.0`) is often enough.
* **When you need a Context Layer backed by an Ontology:** If AI agents must reason across **tables + unstructured documents + business rules + per-user permissions** (or execute governed actions via MCP), you need a Context Layer—which **consumes** rather than replaces your existing Semantic Layer.

### 2. How to Build a Context Layer on Top of Enterprise Data

1. **Discover & Harvest Metadata (`Scan`):** Extract schemas, foreign keys, lineage, dbt/SQL query logs, and SOPs/wikis from PostgreSQL, open lakehouses, and catalogs to propose candidate business entities, joins, and metrics.
2. **Model & Bind the Ontology (`Semantic + Operational Model`):** Map business concepts (`Customer`, `ARR`, `Shipment`, `Policy`) to physical tables, certified SQL attributes, document provenance, and optional governed actions using open standards (`OWL 2`, `RDF`, `SHACL`, `R2RML`, `LinkML`).
3. **Certify & Resolve Conflicts (`Human-in-the-Loop + Authority Ranking`):** Pair human-curated definitions and owners (**Modeled Knowledge**) with usage-derived query/metric snippets (**Learned Knowledge**), ranking competing departmental definitions deterministically.
4. **Enforce Governance & Runtime Validation (`Security + Guardrails`):** Apply caller RBAC/row-level security in PostgreSQL or policy engines at runtime, and validate generated SQL or extracted facts against certified definitions and **SHACL** shapes.
5. **Serve via MCP & Close the Feedback Loop (`Serve & Learn`):** Expose the Context Layer over self-hosted **Model Context Protocol (MCP)** servers (`FastMCP`) and REST APIs so all agents share one governed source of truth, folding certified fixes back into the ontology.

### 3. Strictly Permissive Context Layer Generators & Ontology SDKs (Apache 2.0 / BSD)

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![NVIDIA](https://img.shields.io/badge/NVIDIA-Auto--Ontology-76B900?style=flat-square&logo=nvidia&logoColor=white) **NVIDIA Auto-Ontology** | **Apache 2.0** *(note: external PRs currently not accepted)* | [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) | Automated `Discover → Certify → Reason & Serve` Python + Next.js context-layer framework extracting DB metadata into PostgreSQL/`pgvector` Terms, SQL Attributes, and Relationships; includes human certification UI, SQL validation/provenance, feedback learning, and MCP/REST/CLI serving. | **Tier 1 – Tier 3** (Self-hosted enterprise Text-to-SQL and database semantic context layers). |
| ![AWS](https://img.shields.io/badge/AWS-Context%20Ontology%20Accelerator-FF9900?style=flat-square&logo=amazonaws&logoColor=white) **AWS Context Ontology Accelerator** | **Apache 2.0** | [aws/context-ontology-accelerator](https://github.com/aws/context-ontology-accelerator) | `Scan → Model → Serve` ontology pipeline scanning JDBC/Glue/data lakes, running LLM-assisted OWL 2 / RDF / R2RML / SHACL induction with human review, and serving via MCP. | **Tier 1 – Tier 3** (W3C standards-based context layer induction over enterprise stores). |
| ![LinkML](https://img.shields.io/badge/LinkML-Schema%20%26%20OntoGPT-2563EB?style=flat-square) **LinkML & OntoGPT** | **Apache 2.0** (LinkML) / **BSD-3-Clause** (OntoGPT) | [linkml/linkml](https://github.com/linkml/linkml) / [monarch-initiative/ontogpt](https://github.com/monarch-initiative/ontogpt) | Code-first YAML ontology/schema framework compiling to Pydantic, JSON Schema, SQL DDL, and OWL/RDF; pairs with OntoGPT (LLM structured extraction), OAK, and Schemasheets. | **Tier 1 – Tier 3** (Engineering-led domain modeling bridging Python types, SQL, and semantic web standards). |
| ![Protégé](https://img.shields.io/badge/Prot%C3%A9g%C3%A9-Ontology%20Editor-2563EB?style=flat-square) **Protégé** *(Ontology Editor)* | **BSD-2-Clause** | [protegeproject/protege](https://github.com/protegeproject/protege) | Design-time OWL 2 / RDF / SHACL ontology modeling workbench (Desktop & WebProtégé) with description-logic reasoners; exports directly to Apache Jena Fuseki. | **Design-Time Tooling** (Authoring schemas/taxonomies from departmental glossaries to multi-thousand-class domain ontologies). |
| ![RDFLib](https://img.shields.io/badge/RDFLib-RDF%20%26%20pySHACL-0EA5E9?style=flat-square) **RDFLib & pySHACL** | **BSD-3-Clause** (RDFLib) / **Apache 2.0** (pySHACL) | [RDFLib/rdflib](https://github.com/RDFLib/rdflib) / [RDFLib/pySHACL](https://github.com/RDFLib/pySHACL) | Core Python SDK for RDF/OWL parsing, serialization, and SPARQL querying (`RDFLib`) paired with automated SHACL constraint validation (`pySHACL`) gating LLM-extracted graphs. | **Tier 1 – Tier 2** (Python knowledge-graph pipelines and CI/runtime schema validation gates). |
| ![ROBOT](https://img.shields.io/badge/OBO-ROBOT%20CLI-4F46E5?style=flat-square) **ROBOT** | **BSD-3-Clause** | [ontodev/robot](https://github.com/ontodev/robot) | CLI and Java library for automated CI/CD OWL ontology reasoning, diffing, merging, modular subsetting, and quality-control pipelines. | **All Scales (CI/CD)** (Automated ontology release engineering and regression checks). |
| ![OpenSPG](https://img.shields.io/badge/OpenSPG-KAG%20Ontology-10B981?style=flat-square) **OpenSPG / KAG** | **Apache 2.0** | [OpenSPG/KAG](https://github.com/OpenSPG/KAG) | Semantic-Property-Graph ontology and Knowledge Augmented Generation framework pairing formal domain schemas/rules with LLM multi-hop logical reasoning. | **Tier 2 – Tier 3** (Domain-specific enterprise GraphRAG requiring strict schema constraints and rule inference). |

#### Managed Cloud, Commercial & Copyleft Context / Ontology Platforms (Reference Only — Excluded from Strict Stack)

| Platform / SDK | License (Exclusion Reason) | Ecosystem Role & Ontology Model | Permissive Replacement in This Guide |
| :--- | :--- | :--- | :--- |
| ![Databricks](https://img.shields.io/badge/Databricks-Genie%20Ontology-FF3621?style=flat-square&logo=databricks&logoColor=white) **Databricks Genie Ontology** ([docs.databricks.com](https://docs.databricks.com/)) | Commercial Managed Service (Databricks) | Modeled Knowledge (Unity Catalog metric views, domains, Pages) + Learned Knowledge (SQL/dbt/BI snippets) with runtime Unity Catalog RBAC and MCP serving. | **NVIDIA Auto-Ontology** (`Apache 2.0`) + **PostgreSQL / `pgvector`** + **FastMCP** (`Apache 2.0`) |
| ![AWS](https://img.shields.io/badge/AWS-AWS%20Context-FF9900?style=flat-square&logo=amazonaws&logoColor=white) **AWS Context** *(Managed Service)* | Commercial Managed Service (AWS) | Enterprise context intelligence layer mapping corporate data stores into a governed knowledge graph with Cedar policies, SQL Firewalls, and MCP serving. | **AWS Context Ontology Accelerator** (`Apache 2.0`, self-hosted) + **Apache Jena Fuseki** (`Apache 2.0`) |
| ![Palantir](https://img.shields.io/badge/Palantir-Foundry%20Ontology-101113?style=flat-square) **Palantir Foundry Ontology (AIP)** ([palantir.com/docs](https://www.palantir.com/docs/)) | Commercial Enterprise Platform (Proprietary) | Operational enterprise ontology uniting semantic objects/properties/links with kinetic actions, write-back functions, and audit trails for AIP agents. | **LinkML** (`Apache 2.0`) + **PostgreSQL + Apache AGE** (`Apache 2.0`) + **FastMCP** (`Apache 2.0`) |
| ![Microsoft](https://img.shields.io/badge/Microsoft-Fabric%20IQ%20Ontology-0078D4?style=flat-square&logo=microsoft&logoColor=white) **Microsoft Fabric IQ & Ontology** ([learn.microsoft.com/fabric](https://learn.microsoft.com/en-us/fabric/)) | Commercial Managed Service (Microsoft Fabric) | OneLake-native ontology workload item mapping tables and event streams to business concepts, bootstrapped from Power BI semantic models. | **NVIDIA Auto-Ontology** (`Apache 2.0`) or **LinkML** (`Apache 2.0`) over open lakehouse/PostgreSQL metadata |
| ![Owlready2](https://img.shields.io/badge/Owlready2-Python%20OWL%202-6366F1?style=flat-square) **Owlready2** ([pwin/owlready2](https://github.com/pwin/owlready2)) | LGPL-3.0 (weak copyleft) | Python ontology-oriented programming SDK mapping OWL 2.0 classes/properties to native Python objects with integrated HermiT/Pellet reasoning. | **RDFLib + pySHACL** (`BSD-3-Clause / Apache 2.0`) or **LinkML** (`Apache 2.0`) |

### 4. Practical Starting Stack (100% Permissive OSS Context Layer)

* **Database-to-Context Layer (Text-to-SQL & Certified Metrics):** **NVIDIA Auto-Ontology** (`Apache 2.0`) backed by **PostgreSQL + `pgvector`** (`PostgreSQL License`)—optionally paired with **Cube Core** or **dbt MetricFlow** (`Apache 2.0`) beneath it for BI-grade SQL metrics—and exposed to agents over its built-in **MCP server**.
* **W3C Standards Ontology & Validation Pipeline:** **AWS Context Ontology Accelerator** (`Apache 2.0`) or **LinkML** (`Apache 2.0`) + **Protégé** (`BSD-2-Clause`) for modeling, **ROBOT** (`BSD-3-Clause`) for CI/CD reasoning, **RDFLib + pySHACL** (`BSD-3-Clause / Apache 2.0`) for ingestion gates, and **Apache Jena Fuseki** (`Apache 2.0`) for SPARQL serving.
* **Operational Graph + Action Context Layer:** **LinkML** (`Apache 2.0`) schemas backed by **PostgreSQL + Apache AGE** (`PostgreSQL License / Apache 2.0`) with governed agent actions exposed via **FastMCP** (`Apache 2.0`).

---

## 17. Open-Source Coding-Agent Harnesses, Skills & Context Optimizers (Apache 2.0 / MIT)

100% permissively licensed developer harnesses, reversible token-compression/AST-graph context optimizers, and portable `SKILL.md` workflow packages for coding agents (Claude Code, Cursor, Codex CLI, Gemini CLI).

### A. Multi-Agent Coding Harnesses & Context Optimizers

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Orca](https://img.shields.io/badge/StablyAI-Orca-0EA5E9?style=flat-square) **Orca** | **MIT** | [stablyai/orca](https://github.com/stablyai/orca) | Cross-platform desktop/mobile coding-agent IDE orchestrating parallel agents in isolated Git worktrees with inline diff review, UI-to-CLI handoff, and automated CI feedback loops. | **Tier 1 – Tier 2** (Concurrent multi-agent engineering workstations). |
| ![Ruflo](https://img.shields.io/badge/Ruflo-Agent%20Swarm%20Harness-6366F1?style=flat-square) **Ruflo** *(formerly Claude Flow)* | **MIT** | [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Multi-agent coding swarm meta-harness coordinating $100+$ specialized agents across hierarchical/mesh topologies with AgentDB HNSW persistent memory, TUI/CLI telemetry, federated workflows, and built-in MCP server. | **Tier 1 – Tier 3** (Large-scale multi-repo refactoring and persistent swarm workflows). |
| ![Headroom](https://img.shields.io/badge/Headroom-Context%20Optimizer-10B981?style=flat-square) **Headroom** | **Apache 2.0** | [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom) | Local-first context optimization layer cutting token waste $20-95\%$ on tool outputs, logs, JSON arrays, and RAG chunks via reversible **Compress-Cache-Retrieve (CCR)** hash lookup; ships as HTTP proxy, CLI wrapper (`headroom wrap`), Python/TS SDK, and MCP server. | **All Scales** (Drop-in cost and latency reduction across coding agents and tool-heavy LLM pipelines). |
| ![Graphify](https://img.shields.io/badge/Graphify-AST%20Knowledge%20Graph-8B5CF6?style=flat-square) **Graphify** | **Apache 2.0** *(legacy MIT dual-retained)* | [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify) | Vectorless, embedding-free knowledge graph builder using local `tree-sitter` AST parsing plus doc/SQL/PDF ingestion with explicit explained edges; integrates as a `/graphify` skill & MCP server for Claude Code, Cursor, Codex, and Gemini CLI. | **Tier 1 – Tier 3** (Deterministic codebase navigation without vector index drift). |
| ![Trail-Code](https://img.shields.io/badge/TrailHQ-Trail--Code-2563EB?style=flat-square) **Trail-Code** | **MIT** | [trailhq/Trail-Code](https://github.com/trailhq/Trail-Code) | Context-engineering CLI (`@trailhq/trail-code`) and local MCP server combining a persistent `tree-sitter` code graph ("Graft Map") with a self-learning team-decisions Markdown layer (`.trail/`) across Claude Code, Cursor, Codex, Gemini CLI, Copilot, Windsurf, and Kiro. | **Tier 1 – Tier 2** (Persistent codebase maps and cross-session architectural memory for coding teams). |
| ![codebase-memory-mcp](https://img.shields.io/badge/MCP-codebase--memory--mcp-0F766E?style=flat-square) **codebase-memory-mcp** | **MIT** | [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)<br>[awesome-copilot `SKILL.md`](https://github.com/github/awesome-copilot/blob/main/skills/codebase-memory-mcp/SKILL.md) | Zero-dependency static C binary local MCP server exposing $17$ code-intelligence tools over a persistent SQLite knowledge graph built via vendored `tree-sitter` grammars ($158+$ languages) and hybrid LSP type resolution (plus CBM Lens visualizer). | **Tier 1 – Tier 3** (Air-gapped/local symbol & call-chain traversal cutting raw file reads and token cost). |

### B. Reusable Agent Skills, Persona Catalogs & Security Audit Workflows

| Logo & Product | License | GitHub Repository | Enterprise Use Cases | Recommended Scale |
| :--- | :--- | :--- | :--- | :--- |
| ![Cloudflare](https://img.shields.io/badge/Cloudflare-Security%20Audit%20Skill-F38020?style=flat-square&logo=cloudflare&logoColor=white) **Cloudflare Security Audit Skill** | **MIT** | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | Six-phase agentic security audit workflow (Recon → Coverage-Led Hunting → Independent Adversarial Verifier → JSON-Schema Validated Findings → Record Re-Verification → Neutral Reporting) backed by durable file-based ledgers (`coverage-ledger.json`, `findings.json`) and zero-dependency Node.js validators. | **Tier 1 – Tier 3** (AppSec reviews, incremental PR/commit security audits, and adversarial vulnerability verification). |
| ![Agency Agents](https://img.shields.io/badge/Agency%20Agents-Persona%20Catalog-EC4899?style=flat-square) **Agency Agents** | **MIT** | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | Local-first catalog of $140-200+$ structured Markdown/YAML specialist agent personas across engineering, product, design, finance, and QA with cross-tool transpilers (Claude Code, Cursor, Copilot, Gemini CLI, Windsurf, Aider) and a Tauri desktop app. | **Tier 1 – Tier 2** (Standardizing reusable role prompts and deliverable checklists across IDE coding agents). |
| ![Awesome Copilot](https://img.shields.io/badge/GitHub-Awesome%20Copilot-181717?style=flat-square&logo=github&logoColor=white) **GitHub Awesome Copilot** | **MIT** *(verify per-skill notices)* | [github/awesome-copilot](https://github.com/github/awesome-copilot) | Official GitHub community library of progressive-loading **Agent Skills** (`SKILL.md`, e.g., `codebase-memory-mcp`), **Custom Agents** (`*.agent.md`), glob-scoped **Instructions** (`*.instructions.md`), and **Prompts** (`*.prompt.md`) for Copilot / VS Code Chat and Agent-Skills clients. | **Tier 1 – Tier 3** (Organization-wide Copilot & IDE agent customization, MCP wiring, and skill sharing). |
| ![Ponytail](https://img.shields.io/badge/Ponytail-YAGNI%20Skill-475569?style=flat-square) **Ponytail** | **MIT** | [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | Minimalist engineering `SKILL.md` enforcing a YAGNI "Solution Ladder" (`/ponytail lite\|full\|ultra` + `/ponytail-review` diff auditor) to curb agent over-engineering and token bloat while preserving security and trust-boundary checks. | **Tier 1 – Tier 3** (Code-quality guardrails against unnecessary abstractions in AI-generated PRs). |

