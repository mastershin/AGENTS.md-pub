# Enterprise AI Ecosystem: 100% Free & Permissive Open Source Stack
### Strictly Vetted: Apache 2.0, MIT, BSD-3-Clause & PostgreSQL Licenses Only

This reference architecture includes **exclusively 100% free, permissive open-source software (Apache 2.0, MIT, BSD, PostgreSQL)**.
* **Zero Licensing Lock-in:** Safe for proprietary enterprise modification, internal SaaS deployment, and air-gapped VPCs without copyleft (AGPL/GPL) or Fair-Code/SSPL commercial restrictions.
* **Excluded by Design:** Proprietary SaaS APIs, SSPL/RSAL databases (e.g., Redis, MongoDB), AGPL/ELv2 tools (e.g., Arize Phoenix), Fair-Code tools (e.g., n8n), and non-commercial/restricted weights.

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