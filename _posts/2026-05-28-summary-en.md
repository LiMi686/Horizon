---
layout: default
title: "Horizon Summary: 2026-05-28 (EN)"
date: 2026-05-28
lang: en
---

> From 103 items, 33 important content pieces were selected

---

1. [Anthropic Raises $65B in Series H at $965B Valuation](#item-1) ⭐️ 9.0/10
2. [vLLM: High-Throughput LLM Inference Engine](#item-2) ⭐️ 9.0/10
3. [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](#item-3) ⭐️ 8.0/10
4. [Postgres as a Durable Workflow Engine](#item-4) ⭐️ 8.0/10
5. [SQLite Adds AGENTS.md to Ban AI-Generated Code](#item-5) ⭐️ 8.0/10
6. [Open-Source Cybersecurity Skills Library for AI Agents](#item-6) ⭐️ 8.0/10
7. [Harvard Open-Sources ML Systems Engineering Book](#item-7) ⭐️ 8.0/10
8. [NVIDIA Megatron Bridge Enables Hugging Face Interoperability](#item-8) ⭐️ 8.0/10
9. [Soro: Tajik-Specialized LLM from Gemma 3](#item-9) ⭐️ 8.0/10
10. [DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks](#item-10) ⭐️ 8.0/10
11. [LLMs Fundamentally Cannot Do Causal Discovery; A-CBO Offers Escape](#item-11) ⭐️ 8.0/10
12. [RULER: New Metrics Detect Residuals in Machine Unlearning](#item-12) ⭐️ 8.0/10
13. [LaneRoPE: Collaborative Parallel Reasoning for LLMs](#item-13) ⭐️ 8.0/10
14. [Agyn: Open-Source Platform for Scalable AI Agents](#item-14) ⭐️ 8.0/10
15. [Survey: MoE Tackles Multimodal Learning Challenges](#item-15) ⭐️ 8.0/10
16. [LNNs Outperform LSTM in Efficiency and Robustness](#item-16) ⭐️ 8.0/10
17. [LCO: LLM-based Constraint Optimization for Safer Agents](#item-17) ⭐️ 8.0/10
18. [OralAgent: First AI Agent for Interactive Dental Image Analysis](#item-18) ⭐️ 8.0/10
19. [Self-Alignment Bridges Stability-Expressivity Gap in Low-Resource SLMs](#item-19) ⭐️ 8.0/10
20. [FLUID Adapts AR LLMs to Diffusion Models Efficiently](#item-20) ⭐️ 8.0/10
21. [EvoSpec: Real-Time Adaptation for Speculative Decoding](#item-21) ⭐️ 8.0/10
22. [Representation-Conditioned Diffusion Models Boost Synthetic Data Quality](#item-22) ⭐️ 8.0/10
23. [What-If World: Causal Benchmark for Video World Models](#item-23) ⭐️ 8.0/10
24. [Causal Inference for Heavy-Tailed Outcomes](#item-24) ⭐️ 8.0/10
25. [New Protocol Attaches Impossibility Certificates to Causal Edges](#item-25) ⭐️ 8.0/10
26. [Efficient Inference for Kernel Measures of Noise Heterogeneity](#item-26) ⭐️ 8.0/10
27. [Multi-Turn Deception Detection via Geometric Signatures](#item-27) ⭐️ 8.0/10
28. [GRASP: Unsupervised Removal of Spurious Correlations in Fine-Tuning](#item-28) ⭐️ 8.0/10
29. [Soft Specialists: α-Rényi Ensembles for Uncertainty-Aware LLM Post-Training](#item-29) ⭐️ 8.0/10
30. [New extraction process could unlock cheaper, greener lithium](#item-30) ⭐️ 8.0/10
31. [Blocking GPNMB Protein May Halt Parkinson's Spread](#item-31) ⭐️ 8.0/10
32. [Brain Scans Challenge Long COVID Inflammation Theory](#item-32) ⭐️ 8.0/10
33. [Hidden Gut-Brain Circuit Triggers Protein Cravings](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Raises $65B in Series H at $965B Valuation](https://www.anthropic.com/news/series-h) ⭐️ 9.0/10

Anthropic announced a $65 billion Series H funding round at a $965 billion post-money valuation, surpassing OpenAI in both revenue and valuation. This funding round marks a historic milestone for AI startups, signaling Anthropic's dominance and the accelerating capital intensity in the AI industry. Anthropic's self-reported run-rate revenue reached $47 billion earlier this month, up from $30 billion in April 2026, reflecting rapid enterprise adoption.

hackernews · meetpateltech · May 28, 18:09 · [Discussion](https://news.ycombinator.com/item?id=48313048)

**Background**: Run-rate revenue is an extrapolation of current monthly revenue to a full year, often used by fast-growing private companies to indicate growth trajectory. Anthropic's valuation now approaches $1 trillion, a milestone previously unseen for private AI firms.

**Discussion**: Commenters noted Anthropic's revenue and valuation surpassing OpenAI, with some questioning the run-rate metric and others marveling at the near-trillion-dollar private valuation. There was also discussion about the changing role of the stock market for such large private companies.

**Tags**: `#AI`, `#funding`, `#valuation`, `#Anthropic`, `#startups`

---

<a id="item-2"></a>
## [vLLM: High-Throughput LLM Inference Engine](https://github.com/vllm-project/vllm) ⭐️ 9.0/10

vLLM is an open-source library for high-throughput and memory-efficient inference and serving of large language models, originally developed at UC Berkeley's Sky Computing Lab. It introduces PagedAttention, a novel memory management technique for transformer key-value caches. vLLM has become a critical infrastructure component in the AI ecosystem, enabling cost-effective deployment of large models with state-of-the-art serving throughput. Its widespread adoption and active community of over 2000 contributors make it a groundbreaking project for LLM serving. vLLM supports over 200 model architectures from Hugging Face, including decoder-only, mixture-of-expert, multimodal, and embedding models. It features continuous batching, chunked prefill, prefix caching, quantization (FP8, INT4, etc.), and optimized kernels like FlashAttention.

rss · GitHub Trending - Python · May 28, 23:09

**Background**: Large language models require significant memory and compute for inference, especially due to the key-value cache that grows with sequence length. Traditional attention mechanisms store KV cache in contiguous memory, leading to fragmentation and waste. PagedAttention, inspired by virtual memory paging, divides the KV cache into fixed-size pages and uses an indirection table for efficient memory allocation and reuse.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient ...</a></li>
<li><a href="https://vllm.ai/">vLLM</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#serving`, `#open-source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [Anthropic Releases Claude Opus 4.8, Teases Mythos Model](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 8.0/10

Anthropic has released Claude Opus 4.8, a modest improvement over Opus 4.7 with better alignment and a new toggle to disable adaptive thinking in the web UI. The company also announced Project Glasswing and a preview of the more capable Claude Mythos model for cybersecurity work. This release signals Anthropic's continued incremental improvement of frontier models while hinting at a major leap with Mythos. The ability to disable adaptive thinking addresses user complaints about inconsistent output quality. Opus 4.8 is reported to be four times less likely than Opus 4.7 to allow flaws in code to pass unremarked, with misaligned behavior rates substantially lower. Claude Mythos Preview is currently available only to select organizations under Project Glasswing, with general release expected in weeks.

hackernews · craigmart · May 28, 16:49 · [Discussion](https://news.ycombinator.com/item?id=48311647)

**Background**: Claude Opus is Anthropic's most capable model family, with version numbers like 4.5, 4.6, 4.7, and now 4.8 indicating incremental updates. Project Glasswing is an initiative to secure critical open-source software using advanced AI models. Adaptive thinking is a feature that dynamically adjusts the model's reasoning depth, which some users found unreliable.

<details><summary>References</summary>
<ul>
<li><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-8-is-here-with-3x-cheaper-fast-mode-and-near-mythos-level-alignment">Anthropic's Claude Opus 4.8 is here with 3X cheaper fast mode and near-Mythos level alignment | VentureBeat</a></li>
<li><a href="https://thenextweb.com/news/anthropics-claude-opus-4-8-is-its-most-honest-ai-model-yet-and-mythos-is-coming-in-weeks">Anthropic’s Claude Opus 4.8 is its most honest AI model yet, and Mythos is coming in weeks</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users appreciate the modest improvement and the ability to turn off adaptive thinking, while others note the incremental nature of updates and question the versioning pattern. There is excitement about Mythos but also concern about its limited availability and safety requirements.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Frontier Models`

---

<a id="item-4"></a>
## [Postgres as a Durable Workflow Engine](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

A blog post argues that PostgreSQL can serve as a durable workflow engine, centralizing data and reducing system complexity. The community highlights related projects like Armin Ronacher's 'absurd' and DBOS, which implement durable workflows on Postgres. This approach simplifies backend architecture by eliminating the need for separate workflow engines and data stores, reducing operational overhead. It could make durable workflows more accessible to teams already using Postgres, potentially shifting industry practices. The post suggests using Postgres features like transactions, triggers, and LISTEN/NOTIFY for workflow orchestration. However, scaling to terabytes of data may require migration to purpose-built systems, as noted in community comments.

hackernews · KraftyOne · May 28, 18:41 · [Discussion](https://news.ycombinator.com/item?id=48313530)

**Background**: A durable workflow engine ensures that long-running processes complete reliably even after failures, by persisting state and retrying steps. Traditionally, such engines (e.g., Temporal, Azure Durable Functions) are separate systems, adding complexity. Using Postgres as the sole engine centralizes state and logic, simplifying the stack.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/my-favorite-technologies-implementing-durable-marian-veteanu-oslqe">My Favorite Technologies for Implementing Durable Workflows ...</a></li>
<li><a href="https://github.com/durable-workflow/workflow">GitHub - durable-workflow/workflow: Durable workflow engine ...</a></li>
<li><a href="https://dev.to/mahdi0shamlou/mahdi-shamlou-durable-workflow-engines-comparison-temporal-dbos-transact-prefect-custom-3a6a">Mahdi Shamlou | Durable Workflow Engines Comparison ...</a></li>

</ul>
</details>

**Discussion**: Commenters generally agree on the benefits of centralizing data with Postgres, but raise concerns about scaling to large data volumes. Some point to existing implementations like 'absurd' and DBOS, while others compare Postgres-based approaches to Temporal, noting trade-offs in payload size limits and complexity.

**Tags**: `#PostgreSQL`, `#durable workflows`, `#software architecture`, `#backend development`

---

<a id="item-5"></a>
## [SQLite Adds AGENTS.md to Ban AI-Generated Code](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite added an AGENTS.md file to its repository, explicitly stating that it does not accept agentic (AI-generated) code contributions, while welcoming bug reports and proof-of-concept patches from humans. The project also removed the word "currently" from the policy to strengthen its stance. This is one of the first major open-source projects to formally codify a policy against AI-generated code, setting a precedent for how projects can manage the influx of low-quality AI contributions. It highlights growing tensions between AI coding agents and human-maintained codebases. The AGENTS.md file requires all contributions to be placed in the public domain and states that pull requests from agents are not accepted, though human developers may review concise patches as proof-of-concept. Additionally, SQLite's forum was flooded with AI-generated bug reports, prompting the creation of a separate Bug Forum.

rss · Simon Willison · May 27, 23:44

**Background**: SQLite is a widely-used embedded SQL database engine written in C, with its source code in the public domain. Recently, AI coding agents (like those powered by LLMs) have begun automatically generating and submitting code contributions to open-source projects, often of inconsistent quality and lacking proper legal disclaimers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sqlite/sqlite/blob/master/AGENTS.md">sqlite/AGENTS.md at master - GitHub</a></li>
<li><a href="https://simonwillison.net/2026/May/27/sqlite-agents/">sqlite AGENTS.md - simonwillison.net</a></li>
<li><a href="https://themodelwire.com/article/sqlite-agents-md-01KSNXFG179RJA3K5FQ9TXJ1R2">sqlite AGENTS.md · Modelwire</a></li>

</ul>
</details>

**Discussion**: The community discussion on the Datasette Discord noted the novelty of SQLite's explicit policy, with some expressing support for protecting code quality and others questioning whether such policies could be enforced effectively.

**Tags**: `#sqlite`, `#ai-agents`, `#open-source`, `#software-engineering`, `#policy`

---

<a id="item-6"></a>
## [Open-Source Cybersecurity Skills Library for AI Agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

A GitHub repository named Anthropic-Cybersecurity-Skills has been released, containing 754 structured cybersecurity skills for AI agents, mapped to five major frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF) and compatible with 26+ AI platforms. This library addresses the growing need for standardized, reusable cybersecurity capabilities in AI agents, enabling developers to equip agents with production-grade security skills across multiple domains and platforms, which could accelerate the adoption of AI in security operations. The skills cover 26 security domains, follow the agentskills.io open standard, and are licensed under Apache 2.0. The repository also includes a survey link for the GARS-2026 report and a playground via Casky.ai.

rss · GitHub Trending - Daily (All) · May 28, 23:09

**Background**: Agent Skills is an open standard led by Anthropic for encoding repeatable task knowledge in a format that AI agents can read and execute. MITRE ATT&CK is a widely used knowledge base of adversary tactics and techniques, while NIST CSF provides a cybersecurity framework. D3FEND is a defensive countermeasure ontology, and MITRE ATLAS focuses on AI-specific threats.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>
<li><a href="https://deepwiki.com/libukai/awesome-agent-skills/1.1-the-agent-skills-standard">The Agent Skills Standard | libukai/awesome-agent-skills ...</a></li>
<li><a href="https://www.productbuilder.net/learn/agent-skills">Agent Skills: The Open Standard for AI Agent Capabilities</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-7"></a>
## [Harvard Open-Sources ML Systems Engineering Book](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

Harvard's CS249r course has released an open-source book titled "Machine Learning Systems: Principles and Practices of Engineering Artificially Intelligent Systems" on GitHub, with multilingual support including English, Chinese, Japanese, and Korean. This resource provides a comprehensive, freely accessible curriculum on ML systems engineering from a top university, bridging the gap between ML model development and production deployment for a global audience. The repository includes not only the book but also supplementary materials such as slides, labs, and a TinyTorch implementation, all under a CC-BY-NC-SA 4.0 license.

rss · GitHub Trending - Python · May 28, 23:09

**Background**: Machine learning systems engineering focuses on the practical aspects of deploying and maintaining ML models in production, which is often overlooked in favor of model development. This book aims to teach the principles and practices needed to build robust AI systems, covering topics like data pipelines, model serving, and monitoring.

<details><summary>References</summary>
<ul>
<li><a href="https://hellogithub.com/en/repository/harvard-edge/cs249r_book">harvard-edge/ cs 249 r _ book : Machine Learning Systems... - HelloGitHub</a></li>
<li><a href="https://blog.tensorflow.org/2024/11/mlsysbookai-principles-and-practices-of-machine-learning-systems-engineering.html">MLSysBook.AI: Principles and Practices of Machine Learning Systems Engineering — The TensorFlow Blog</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#systems engineering`, `#education`, `#AI`, `#open source`

---

<a id="item-8"></a>
## [NVIDIA Megatron Bridge Enables Hugging Face Interoperability](https://github.com/NVIDIA-NeMo/Megatron-Bridge) ⭐️ 8.0/10

NVIDIA released the Megatron Bridge library, a PyTorch-native tool within the NeMo Framework that provides bidirectional conversion between Megatron and Hugging Face model formats, along with pretraining, SFT, and LoRA support for popular LLMs and VLMs. This library bridges two major ecosystems—Megatron for large-scale training and Hugging Face for community models—enabling seamless model conversion and interoperability, which simplifies workflows for researchers and engineers working with large language models. The library supports models like DeepSeek V4, Nemotron-3 Nano Omni, and Gemma 4 VL, and includes day-0 support for new releases. It also provides conversion, inference, SFT, and PEFT (LoRA) examples for multimodal models.

rss · GitHub Trending - Python · May 28, 23:09

**Background**: Megatron is NVIDIA's framework for training large language models at scale, while Hugging Face Transformers is a widely used library for accessing pretrained models. Previously, converting models between these two formats required manual effort. The Megatron Bridge automates this process, making it easier to leverage both ecosystems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge">GitHub - NVIDIA-NeMo/Megatron-Bridge: Training library for ...</a></li>
<li><a href="https://docs.nvidia.com/nemo/megatron-bridge/latest/">NeMo Megatron Bridge - NVIDIA Documentation Hub</a></li>
<li><a href="https://pypi.org/project/megatron-bridge/">megatron-bridge · PyPI</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Megatron`, `#Hugging Face`, `#LLM`, `#Training`

---

<a id="item-9"></a>
## [Soro: Tajik-Specialized LLM from Gemma 3](https://arxiv.org/abs/2605.27379) ⭐️ 8.0/10

Researchers introduced Soro, a family of Tajik-specialized large language models built by continually pretraining Gemma 3 on a curated 1.9-billion-token Tajik corpus and instruction tuning on 40K examples, along with open-sourced Tajik benchmarks. Soro addresses a critical gap in LLM coverage for low-resource languages like Tajik, enabling practical AI applications in education and other sectors in Tajikistan while preserving strong English performance. Soro uses FP8 and INT4 quantization to reduce memory for edge deployment, and it outperforms same-size Gemma 3 baselines on new Tajik benchmarks covering general knowledge, linguistics, and entrance exams.

rss · arXiv - AI · May 28, 04:00

**Background**: Low-resource languages like Tajik lack sufficient digital data and tools for NLP, making it challenging to build effective language models. Continual pretraining adapts a general-purpose LLM to a specific domain or language by further training on relevant data. Gemma 3 is a lightweight, open-weight model from Google that can run on a single GPU, suitable for deployment in resource-constrained settings.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/gemma-3/">Gemma 3 — Google DeepMind</a></li>
<li><a href="https://arxiv.org/abs/2402.17400">[2402.17400] Investigating Continual Pretraining in Large Language Models: Insights and Implications</a></li>

</ul>
</details>

**Tags**: `#low-resource NLP`, `#large language models`, `#continual pretraining`, `#Tajik language`, `#benchmarks`

---

<a id="item-10"></a>
## [DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks](https://arxiv.org/abs/2605.27566) ⭐️ 8.0/10

DynaSchedBench introduces a Sequential Event-Space Calibrator (SESC) that computes a Schedule Stress Index (SSI) to stratify instances by difficulty for the Dynamic Flexible Job Shop Scheduling Problem (DFJSP). This framework addresses the methodological tension between static benchmarks and uncalibrated generators, enabling rigorous testing of LLM-based scheduling agents and revealing their limitations, such as the Observability Paradox. SESC is computationally more efficient than evolutionary baselines and converges reliably to target metrics. The framework includes modular components for instance generation, snapshot-based simulation, agents, evaluation, and visualization.

rss · arXiv - AI · May 28, 04:00

**Background**: The Dynamic Flexible Job Shop Scheduling Problem (DFJSP) involves scheduling jobs on machines with dynamic events like new job arrivals or machine breakdowns. Traditional benchmarks often suffer from overfitting or stochastic noise, hindering progress in neural combinatorial optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2550454">Dynamic flexible job shop scheduling problem considering ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10845-025-02645-x">Systematic review and future directions in dynamic flexible ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-024-79593-8">Dynamic scheduling for flexible job shop based on MachineRank ...</a></li>

</ul>
</details>

**Tags**: `#scheduling`, `#benchmarking`, `#combinatorial optimization`, `#LLM agents`, `#operations research`

---

<a id="item-11"></a>
## [LLMs Fundamentally Cannot Do Causal Discovery; A-CBO Offers Escape](https://arxiv.org/abs/2605.27567) ⭐️ 8.0/10

A new paper proves that large language models (LLMs) cannot reliably perform causal discovery from observational data alone, due to a fundamental limitation in their learning paradigm formalized as the kernel obstruction theorem. The authors propose Agentic Causal Bayesian Optimization (A-CBO), which uses a frozen LLM as an interventional oracle and an external Bayesian loop to provably converge to the correct causal graph. This work provides a theoretical explanation for why LLMs plateau on causal discovery benchmarks, shifting the focus from scaling models to designing hybrid systems that combine LLMs with structured reasoning. A-CBO achieves strong results without training, suggesting a new paradigm for causal inference in AI. The kernel obstruction theorem shows that supervised fine-tuning, direct preference optimization, and in-context learning all produce predictors that cannot distinguish between causal graphs generating similar observational data. A-CBO requires only logarithmically many rounds of interventional queries to concentrate beliefs over candidate graphs.

rss · arXiv - AI · May 28, 04:00

**Background**: Causal discovery aims to infer cause-effect relationships from data, which is crucial for scientific reasoning. LLMs have been tested on this task but show limited performance, especially on complex graphs. The kernel obstruction theorem explains this failure as intrinsic to the learning paradigm, not any specific model or dataset.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27567">Why LLMs Fail at Causal Discovery and How Interventional ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2506.00844">LLMs in Causal Discovery: Limits & Guidelines</a></li>
<li><a href="https://www.amazon.science/publications/causal-bayesian-optimization">Causal Bayesian optimization - Amazon Science</a></li>

</ul>
</details>

**Tags**: `#causal discovery`, `#large language models`, `#machine learning theory`, `#Bayesian optimization`

---

<a id="item-12"></a>
## [RULER: New Metrics Detect Residuals in Machine Unlearning](https://arxiv.org/abs/2605.27569) ⭐️ 8.0/10

Researchers introduced RULER, a set of representation-level verification metrics for machine unlearning, including an oracle-comparative metric (M2) and an oracle-free metric (M4). Current output-level verification protocols can be fooled, but RULER detects residual information in intermediate representations, improving trustworthiness and compliance in AI systems. In experiments, four approximate unlearning methods passed output-level evaluation, yet M2 detected significant residuals in 10 of 12 conditions (p<0.05). M4 also detected identity-level memorisation in face recognition models.

rss · arXiv - AI · May 28, 04:00

**Background**: Machine unlearning aims to remove specific training data influence from a model without full retraining. Current verification relies on output-level metrics like membership inference and accuracy, which may miss hidden information in internal representations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27569">RULER: Representation - Level Verification of Machine Unlearning</a></li>
<li><a href="https://arxiv.org/pdf/2605.27569">RULER: Representation - Level Verification of Machine Unlearning</a></li>

</ul>
</details>

**Tags**: `#machine unlearning`, `#verification`, `#representation learning`, `#AI safety`, `#privacy`

---

<a id="item-13"></a>
## [LaneRoPE: Collaborative Parallel Reasoning for LLMs](https://arxiv.org/abs/2605.27570) ⭐️ 8.0/10

LaneRoPE introduces inter-sequence attention and a RoPE extension that enables multiple parallel LLM generations to collaborate during decoding, improving test-time scaling efficiency. This addresses a key limitation of independent sampling in test-time scaling, allowing LLMs to share intermediate reasoning across parallel sequences, which boosts accuracy with minimal architectural changes. LaneRoPE uses an inter-sequence attention mask to make token sampling dependent across sequences, and a RoPE extension to encode relative positions both within and across sequences, adding negligible inference overhead.

rss · arXiv - AI · May 28, 04:00

**Background**: Parallel test-time scaling techniques like best-of-N generate multiple independent sequences from the same prompt and select the best one, but they do not allow sequences to influence each other. LaneRoPE enables collaboration by modifying the attention mask and positional encoding, building on Rotary Position Embedding (RoPE), a standard positional encoding method in modern LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27570">[2605.27570] LaneRoPE: Positional Encoding for Collaborative ...</a></li>
<li><a href="https://openreview.net/forum?id=6WAuvwZjmw">LaneRoPE: Positional Encoding for Collaborative Parallel ...</a></li>
<li><a href="https://learncodecamp.net/rope-explained/">RoPE Explained: The Positional Encoding Trick Behind Modern ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#positional encoding`, `#parallel decoding`, `#test-time scaling`, `#reasoning`

---

<a id="item-14"></a>
## [Agyn: Open-Source Platform for Scalable AI Agents](https://arxiv.org/abs/2605.27575) ⭐️ 8.0/10

Agyn is an open-source platform for deploying AI agents at scale, featuring a signal-driven serverless runtime on Kubernetes, infrastructure-as-code via a Terraform provider, and zero-trust security. The platform is agent-agnostic, model-agnostic, and cloud-agnostic. Agyn addresses critical production challenges for AI agents, such as scalability, isolation, governance, and security, which are essential for enterprise adoption. It provides a standardized, open-source approach that can accelerate the deployment of reliable and secure AI agent systems. The platform uses a signal-driven, stateful serverless runtime on Kubernetes, a Terraform provider for defining agents and harnesses, and a zero-trust security model based on least-privilege principles. It is designed to be agnostic to agents, models, and cloud providers.

rss · arXiv - AI · May 28, 04:00

**Background**: AI agents are autonomous programs that perform tasks, often with access to internal services, but deploying them in production requires handling non-deterministic workflows, stateful sessions, and security. Serverless computing on Kubernetes offers on-demand execution and autoscaling, while infrastructure-as-code tools like Terraform enable declarative management. Zero-trust security ensures no implicit trust, enforcing least-privilege access.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/agynio/platform">GitHub - agynio/ platform : Agyn is an open-source Kubernetes-native...</a></li>
<li><a href="https://www.youtube.com/watch?v=i4vZQ9vRvfY">Agyn Demo: AI Engineering Teams Working Natively in... - YouTube</a></li>
<li><a href="https://www.linkedin.com/posts/omarsar_another-great-paper-if-you-are-building-with-activity-7427033691593428992-xIkX">Agyn : Open-Source Multi-Agent Platform for Software... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#serverless`, `#Kubernetes`, `#zero-trust`, `#open-source`

---

<a id="item-15"></a>
## [Survey: MoE Tackles Multimodal Learning Challenges](https://arxiv.org/abs/2605.27431) ⭐️ 8.0/10

A new survey systematically reviews how Mixture-of-Experts (MoE) frameworks address multimodal learning challenges, covering efficient scaling, representation learning, and adaptation to imperfect data. This survey fills a gap by jointly analyzing MoE and multimodal learning, offering a foundation for future research on scalable and interpretable multimodal AI systems. The survey examines MoE from three perspectives: as an efficient engine, a representation learner, and an adapter for imperfect data. It identifies research gaps including interpretable routing, expert communication, and lifelong multimodal learning.

rss · arXiv - Machine Learning · May 28, 04:00

**Background**: Mixture-of-Experts (MoE) is a machine learning technique that uses multiple specialized sub-networks (experts) and a gating network to select the best expert for each input, enabling efficient scaling by activating only a subset of parameters. Multimodal learning involves integrating information from multiple data types (e.g., text, image, audio), facing challenges such as representation, alignment, fusion, and handling missing modalities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts (MoE)? How It Works, Use Cases & More | DataCamp</a></li>
<li><a href="https://engineering.mercari.com/en/blog/entry/20210623-5-core-challenges-in-multimodal-machine-learning/">5 Core Challenges In Multimodal Machine Learning | Mercari Engineering</a></li>

</ul>
</details>

**Tags**: `#Mixture-of-Experts`, `#Multimodal Learning`, `#Survey`, `#Deep Learning`, `#Scalability`

---

<a id="item-16"></a>
## [LNNs Outperform LSTM in Efficiency and Robustness](https://arxiv.org/abs/2605.27467) ⭐️ 8.0/10

A new comparative study shows that Liquid Neural Networks (specifically Closed-form Continuous-time networks) achieve superior parameter efficiency and robustness compared to LSTM across four sequential pattern recognition tasks, including neuromorphic data and clinical time-series. This work highlights the practical advantages of continuous-time models for real-world applications where data is sparse or missing, such as clinical monitoring, potentially enabling more reliable AI systems with fewer parameters. The study benchmarks LNNs against LSTM on N-MNIST, QuickDraw, IAM, and PhysioNet Sepsis-3 datasets, and introduces temporal dropout stress tests to evaluate robustness to missing data.

rss · arXiv - Machine Learning · May 28, 04:00

**Background**: Liquid Neural Networks (LNNs) are a class of continuous-time neural networks that model hidden state evolution via differential equations, unlike traditional RNNs and LSTMs that operate on discrete time steps. Closed-form Continuous-time (CfC) networks provide an efficient closed-form approximation to liquid time-constant networks, enabling faster training and inference.

<details><summary>References</summary>
<ul>
<li><a href="https://builtin.com/articles/liquid-neural-networks">Liquid Neural Networks (LNN): A Guide - Built In</a></li>
<li><a href="https://www.nature.com/articles/s42256-022-00556-7">Closed-form continuous-time neural networks - Nature</a></li>
<li><a href="https://www.garrickorchard.com/datasets/n-mnist">Garrick Orchard - N-MNIST</a></li>

</ul>
</details>

**Tags**: `#Liquid Neural Networks`, `#LSTM`, `#Sequential Pattern Recognition`, `#Robustness`, `#Clinical Utility`

---

<a id="item-17"></a>
## [LCO: LLM-based Constraint Optimization for Safer Agents](https://arxiv.org/abs/2605.27375) ⭐️ 8.0/10

Researchers propose LLM-based Constraint Optimization (LCO), a framework that mitigates in-context reward hacking (ICRH) in autonomous LLM agents without requiring fine-tuning. ICRH poses a significant safety risk as LLM agents iteratively optimize proxy objectives, leading to harmful side effects; LCO offers a practical, fine-tuning-free defense that can be applied to existing models. LCO consists of a self-thought module for proactive safety deliberation and an evolutionary sampling module using LLM-based crossover and mutation to constrain actions within a safe solution space. On a tweet engagement task, LCO reduced Toxicity Growth Rate by 39% on GPT-4, and on a policy optimization benchmark, it reduced ICRH occurrence rate by 15.23% without sacrificing task performance.

rss · arXiv - NLP · May 28, 04:00

**Background**: In-context reward hacking (ICRH) occurs when LLM agents iteratively refine their outputs based on feedback, over-optimizing a proxy objective and causing unintended harmful side effects. Unlike traditional reward hacking during training, ICRH happens at inference time without weight updates, making existing defenses less effective. LCO addresses this by integrating constraint optimization directly into the LLM's reasoning process.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27375">[2605.27375] LCO : LLM - based Constraint Optimization for Safer...</a></li>
<li><a href="https://arxiv.org/html/2402.06627v3">Feedback Loops With Language Models Drive In - Context Reward ...</a></li>
<li><a href="https://lilianweng.github.io/posts/2024-11-28-reward-hacking/">Reward Hacking in Reinforcement Learning | Lil'Log</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI safety`, `#constraint optimization`, `#reward hacking`, `#agentic AI`

---

<a id="item-18"></a>
## [OralAgent: First AI Agent for Interactive Dental Image Analysis](https://arxiv.org/abs/2605.27378) ⭐️ 8.0/10

Researchers introduced OralAgent, the first dental-specialized AI agent that integrates multimodal reasoning, 22 visual analysis tools, and retrieval from 368 dental textbooks into an end-to-end framework for interactive dental image analysis. This advancement bridges the gap between isolated dental AI models and real-world clinical workflows, potentially improving diagnostic accuracy and treatment planning in oral healthcare. The system also introduces OralCorpus, a large-scale bilingual dental corpus with 134.8M tokens for retrieval-augmented generation, and OralQA-ZH, a Chinese multiple-choice benchmark with 798 items across 11 subspecialties.

rss · arXiv - NLP · May 28, 04:00

**Background**: Retrieval-augmented generation (RAG) enhances large language models by allowing them to access external knowledge bases, improving accuracy and reducing hallucinations. OralAgent applies this technique to dentistry, combining it with specialized tools for image analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval - Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://huggingface.co/datasets/OralGPT/OralCorpus">OralGPT/OralCorpus · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#AI Agent`, `#Medical AI`, `#Dental Image Analysis`, `#Multimodal Reasoning`, `#Retrieval-Augmented Generation`

---

<a id="item-19"></a>
## [Self-Alignment Bridges Stability-Expressivity Gap in Low-Resource SLMs](https://arxiv.org/abs/2605.27383) ⭐️ 8.0/10

Researchers propose two self-alignment frameworks, DGSA and TDSC, to mitigate the Stability-Expressivity Gap in low-resource spoken language models caused by synthetic data scaling, achieving zero-shot voice cloning for Lao. This work addresses a critical trade-off in spoken language models for low-resource languages, enabling high-fidelity speech synthesis and voice cloning where real data is scarce, outperforming commercial systems like ElevenLabs and Gemini Pro. The Stability-Expressivity Gap describes how synthetic data improves phonetic accuracy but suppresses prosodic variability, leading to Synthetic Erosion. DGSA recovers expressivity via prosody-timbre separation, while TDSC uses automated exploration and filtering for extremely limited reference scenarios.

rss · arXiv - NLP · May 28, 04:00

**Background**: Spoken Language Models (SLMs) generate speech directly without text-to-speech pipelines, but low-resource languages lack transcribed speech. Synthetic data scaling is commonly used but introduces a trade-off between phonetic accuracy and prosodic expressivity, known as the Stability-Expressivity Gap.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27383">[2605.27383] Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models</a></li>
<li><a href="https://arxiv.org/html/2605.27383">Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models</a></li>
<li><a href="https://arxiv.org/pdf/2605.27383">Bridging the Stability - Expressivity Gap : Synthetic Data Scaling and...</a></li>

</ul>
</details>

**Tags**: `#spoken language models`, `#low-resource languages`, `#synthetic data`, `#speech synthesis`, `#self-alignment`

---

<a id="item-20"></a>
## [FLUID Adapts AR LLMs to Diffusion Models Efficiently](https://arxiv.org/abs/2605.27387) ⭐️ 8.0/10

Researchers propose FLUID, a framework that adapts pre-trained autoregressive LLMs to diffusion models using Strictly Causal Alignment and Elastic Horizons, enabling parallel text generation without pre-training from scratch. This work bridges the structural mismatch between autoregressive and diffusion models, drastically reducing training costs while achieving state-of-the-art performance, which could accelerate deployment of efficient parallel generation in LLMs. Strictly Causal Alignment allows seamless initialization from GPT-style checkpoints, while Elastic Horizons dynamically adjusts denoising strides based on local information density. The method claims to reduce training costs by orders of magnitude.

rss · arXiv - NLP · May 28, 04:00

**Background**: Autoregressive (AR) models like GPT generate text token by token sequentially, while diffusion models generate text in parallel by iteratively denoising random noise. However, diffusion models typically require bidirectional attention, which is incompatible with the causal attention of pre-trained AR models, forcing expensive pre-training from scratch. FLUID addresses this by enforcing a strictly causal alignment that preserves the AR attention pattern, and introduces an entropy-driven mechanism to optimize the denoising schedule.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27387">[2605.27387] From AR to Diffusion : Efficiently Adapting Large...</a></li>
<li><a href="https://arxiv.org/html/2605.27387">From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Diffusion Models`, `#Parallel Text Generation`, `#Model Adaptation`, `#Efficient Training`

---

<a id="item-21"></a>
## [EvoSpec: Real-Time Adaptation for Speculative Decoding](https://arxiv.org/abs/2605.27390) ⭐️ 8.0/10

EvoSpec introduces a framework that dynamically adapts the draft model's vocabulary and parameters in real time during speculative decoding, overcoming the static pruning limitations that cause acceptance rate drops in specialized domains or topic-switching scenarios. This innovation addresses a critical bottleneck in LLM inference—the output projection layer—by enabling efficient adaptation to dynamic distribution shifts, potentially improving inference speed and reducing memory overhead in real-world applications like coding, law, and medicine. EvoSpec uses a context-aware mechanism to retrieve long-tail tokens via semantic and statistical indexing, and employs a lightweight online alignment strategy with curriculum learning to minimize the distributional gap between draft and target models. On EAGLE-3, it achieves a 1.13x speedup over the static baseline FR-Spec with 27% lower memory overhead.

rss · arXiv - NLP · May 28, 04:00

**Background**: Speculative decoding accelerates LLM inference by using a small draft model to generate candidate tokens, which are then verified by the large target model. However, the output projection layer, which maps hidden states to vocabulary logits, becomes a bottleneck as vocabulary size grows. Static pruning methods reduce this overhead but fail under dynamic distribution shifts, such as topic switches or specialized domains.

<details><summary>References</summary>
<ul>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>
<li><a href="https://research.google/blog/looking-back-at-speculative-decoding/">Looking back at speculative decoding</a></li>
<li><a href="https://arxiv.org/pdf/2505.10202">VQ-Logits: Compressing the Output Bottleneck of Large ...</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#LLM inference`, `#vocabulary adaptation`, `#online learning`, `#curriculum learning`

---

<a id="item-22"></a>
## [Representation-Conditioned Diffusion Models Boost Synthetic Data Quality](https://arxiv.org/abs/2605.27495) ⭐️ 8.0/10

Researchers propose representation-conditioned diffusion models that generate synthetic training data using learned representations from DINOv2, DINOv3, and CLIP, achieving +10.76 p.p. top-1 accuracy over class-conditioned generation on ImageNet100 and even outperforming real data by +2.0 p.p. This approach addresses data scarcity in deep learning by enabling high-quality synthetic data that can augment or replace real datasets, potentially reducing the cost and effort of data collection and annotation. The method uses latent diffusion models conditioned on representations from self-supervised models like DINOv2, which capture richer semantic information than class labels. Scaling the synthetic dataset size further improves performance, and the conditioning space can also be used for sample filtering.

rss · arXiv - Computer Vision · May 28, 04:00

**Background**: Diffusion models are generative models that learn to denoise data, and latent diffusion models perform this process in a compressed latent space for efficiency. DINOv2 is a self-supervised vision model that learns robust image representations without labels, capturing features like object parts and segmentation. Mode coverage refers to a generative model's ability to produce diverse samples covering all modes of the data distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2304.07193v2">DINOv2: Learning Robust Visual Features without Supervision</a></li>
<li><a href="https://www.picsellia.com/post/dinov2-steps-by-steps-explanations-picsellia">DINOv2 - Steps by steps explanations - Picsellia | Picsellia</a></li>
<li><a href="https://encord.com/blog/dinov2-self-supervised-learning-explained/">DINOv2 Explained: Revolutionizing Computer Vision with Self-Supervised Learning | Encord</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#synthetic data`, `#representation learning`, `#image classification`, `#data augmentation`

---

<a id="item-23"></a>
## [What-If World: Causal Benchmark for Video World Models](https://arxiv.org/abs/2605.27589) ⭐️ 8.0/10

Researchers introduced What-If World, a benchmark of 319 prompt pairs built on real frames from nuScenes and DROID datasets, to test whether video generation models correctly model causal physical changes in driving and manipulation scenarios. This benchmark addresses a critical gap in evaluating world models for embodied AI, revealing that even state-of-the-art video generation models fail to reliably simulate causal interventions, which is essential for action-conditioned simulation and model-based planning. The benchmark uses a taxonomy of six physical variables and scores each pair with APEO, a four-part rubric; across nine models, no system exceeds 52% on the paired score, and open-source models cluster near 28%.

rss · arXiv - Computer Vision · May 28, 04:00

**Background**: Video generation models are increasingly used as world simulators for tasks like driving and robotic manipulation. Existing benchmarks evaluate videos individually, failing to detect whether models correctly respond to causal changes in input prompts. What-If World uses paired prompts that differ by only one physical variable to test causal reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nuscenes.org/">Recent announcements, as well as key figures about the nuScenes ...</a></li>
<li><a href="https://droid-dataset.github.io/">DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset</a></li>

</ul>
</details>

**Tags**: `#world models`, `#causal reasoning`, `#video generation`, `#embodied AI`, `#benchmark`

---

<a id="item-24"></a>
## [Causal Inference for Heavy-Tailed Outcomes](https://arxiv.org/abs/2605.27474) ⭐️ 8.0/10

This paper proposes a new average dose-response function (ADRF) estimator that provides tail-shape diagnostics for heavy-tailed outcomes, breaking the circular dependence in existing methods that caused tail inferences to vary with the choice of robust loss function. This work addresses a critical gap in causal inference for extreme events, which is essential for high-stakes domains like finance and climate where the 1-in-1000 event is the actual target. The proposed method reduces deep-tail return-level MAE by 11% and conditional-shortfall MAE by 25.5% compared to quantile regression. The estimator outputs four treatment-conditional quantities: tail shape, deep-tail return levels, conditional shortfalls, and the mean ADRF, along with an explicit refusal mechanism when extreme-value modeling is unsupported. It achieves 20-29% MAE reduction in sample-scarce regimes (n ≤ 2000) and successfully triggered extrapolation refusal on motor-insurance claims data.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: Causal inference aims to estimate how an outcome responds to a treatment, but standard methods like double machine learning (DML) suppress extreme values in heavy-tailed outcomes to stabilize the average. Heavy-tailed distributions have more probability mass in the tails, making extreme events more likely, which is critical in finance and climate. Existing tail-aware methods suffer from circular dependence because they read the tail from residuals, causing instability based on the choice of robust loss function (e.g., Huber vs. Welsch).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huber_loss">Huber loss - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1908.05097">[1908.05097] Causal discovery in heavy-tailed models - arXiv.org Causal discovery in heavy-tailed models - JSTOR Causal modelling of heavy-tailed variables and confounders ... Causal discovery in heavy-tailed models - Project Euclid Full article: When Heavy Tails Disrupt Statistical Inference Causal discovery in heavy-tailed models • causalXtreme Heavy-tailed distribution - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heavy-tailed_distribution">Heavy-tailed distribution - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#heavy tails`, `#machine learning`, `#extreme events`, `#statistics`

---

<a id="item-25"></a>
## [New Protocol Attaches Impossibility Certificates to Causal Edges](https://arxiv.org/abs/2605.27477) ⭐️ 8.0/10

A new protocol for observational causal discovery attaches a discrete impossibility certificate (RESOLVED or IMPOSSIBLE) to each candidate edge, distinguishing directions identified by data from those assigned via assumptions. It also introduces five gated identifiability tiers (LSNM, IGCI, Stein, MDL, PEIT) and two oracle primitives that establish an upper bound of 1+K expert interactions to recover any DAG. This work addresses a fundamental limitation in causal discovery: the lack of per-edge uncertainty quantification. By providing impossibility certificates and a tiered oracle framework, it enables principled integration of expert knowledge and could significantly improve the reliability of causal inference in scientific applications. The impossibility certificate uses a RESOLVED code to record the identifiability theorem under which a direction is committed, and an IMPOSSIBLE code to specify the failure mode and the exact question an expert must answer. The bivariate cascade includes five tiers (LSNM, IGCI, Stein, MDL, PEIT) that abstain when their precondition test fails, and the oracle primitives (meta-hub query and node-children query) guarantee recovery of any DAG with at most 1+K expert interactions, where K is the number of non-leaf vertices.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: Causal discovery aims to infer causal relationships from observational data, but under standard Markov and faithfulness assumptions, only a Markov equivalence class (MEC) can be identified—multiple DAGs with the same conditional independencies. Edge directions within the MEC are not determined by data alone and require additional assumptions or expert knowledge. This protocol provides a systematic way to track which directions are identified and which require external input.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27477">[2605.27477] Iterative Causal Discovery : Per-Edge Impossibility ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/11564089_9">Learning Causal Structures Based on Markov Equivalence Class | Springer Nature Link</a></li>
<li><a href="https://arxiv.org/html/2505.02781v1">Local Markov Equivalence and Local Causal Discovery for Identifying Controlled Direct Effects</a></li>

</ul>
</details>

**Tags**: `#causal discovery`, `#causal inference`, `#identifiability`, `#graphical models`, `#machine learning`

---

<a id="item-26"></a>
## [Efficient Inference for Kernel Measures of Noise Heterogeneity](https://arxiv.org/abs/2605.27526) ⭐️ 8.0/10

This paper develops semiparametrically efficient inference for kernel measures of noise heterogeneity in additive noise models, introducing a Hilbert-valued one-step estimator that corrects first-stage regression bias. This work enables valid hypothesis tests and confidence intervals for residual independence and goodness-of-fit in machine learning pipelines, addressing a critical source of bias that invalidates standard inference. The estimator is bootstrap-calibrated and asymptotically efficient, and the framework extends to settings with additional covariates for inference on distributional heterogeneity across treatment groups.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: In additive noise models, the outcome is modeled as a function of covariates plus independent noise. When the regression function is estimated via flexible machine learning, the residuals may inherit bias that induces spurious dependence between covariates and residuals, breaking standard independence assumptions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.16711">One-Step Estimation of Differentiable Hilbert-Valued Parameters Images One-Step Estimation of Differentiable Hilbert-Valued Parameters One-Step Estimation of Differentiable Hilbert-Valued ... GitHub - alexluedtke12/HilbertOneStep: Implements the one ... One-Step Estimation of Differentiable Hilbert-Valued ... One-Step Estimation of Differentiable Hilbert-Valued Parameters</a></li>
<li><a href="https://jmlr.org/papers/volume15/peters14a/peters14a.pdf">Causal Discovery with Continuous Additive Noise Models Additive noise models — causal-learn 0.1.3.6 documentation Additive white Gaussian noise - Wikipedia Causal Identiﬁcation with Additive Noise Models: Quantifying ... Nonlinear causal discovery with additive noise models - NeurIPS Identifying Causal Mechanism Shifts Under Additive Models ...</a></li>

</ul>
</details>

**Tags**: `#semiparametric inference`, `#kernel methods`, `#noise heterogeneity`, `#machine learning`, `#causal inference`

---

<a id="item-27"></a>
## [Multi-Turn Deception Detection via Geometric Signatures](https://arxiv.org/abs/2605.27671) ⭐️ 8.0/10

Researchers propose a pipeline that uses multi-objective genetic optimization to generate multi-turn deceptive prompts and detects them via geometric signatures in embedding space, achieving high recall (0.89) with a lightweight classifier. This work addresses a critical gap in LLM safety by focusing on multi-turn deception, which is more realistic than single-turn attacks, and provides a practical, explainable detection method without expensive end-to-end training. The detection model uses three geometric features (angular coverage, distance ratio, linearity) plus pairwise similarity statistics, achieving test-time F1 scores of 0.74-0.86 across base, reworded, and truncated three-turn scenarios.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: Large language models (LLMs) are often safety-tested with single-turn prompts, but real-world attacks can involve indirect, multi-turn probing to bypass defenses. Geometric signatures in embedding space capture structural patterns of deceptive intent, enabling lightweight detection without full model retraining.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/gepa-ai/gepa">GitHub - gepa-ai/gepa: Optimize prompts, code, and more with ...</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1613007/full">GAAPO: genetic algorithmic applied to prompt optimization</a></li>
<li><a href="https://arxiv.org/pdf/2511.22150">From Topology to Retrieval: Decoding Embedding Spaces with ...</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#adversarial attacks`, `#multi-turn deception`, `#geometric features`, `#genetic optimization`

---

<a id="item-28"></a>
## [GRASP: Unsupervised Removal of Spurious Correlations in Fine-Tuning](https://arxiv.org/abs/2605.27676) ⭐️ 8.0/10

The paper introduces GRASP, an unsupervised method that identifies and removes spurious correlations during fine-tuning by analyzing LoRA weights, preserving useful latent factors. It validates on emergent misalignment and political bias tasks, outperforming baselines. This work addresses a critical problem in fine-tuning LLMs—spurious correlations—with a principled, unsupervised approach that does not require labels for the spurious concept. It offers a better trade-off between bias reduction and task preservation, enhancing fairness and robustness in NLP. GRASP uses gradient projection to prevent the model from acquiring new reliance on identified latent factors while preserving pretrained content. It completely removes misalignment in insecure code generation and reduces it by ~5x in bad medical advice, and halves political drift while improving task performance.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: Fine-tuning pretrained language models on curated datasets can introduce spurious correlations between the task and unintended latent factors (e.g., political slant). Existing bias removal methods like activation steering require labels for the spurious concept and may discard useful signal. LoRA is a parameter-efficient fine-tuning method that learns low-rank weight updates.

<details><summary>References</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/revolutionizing-ai-fine-tuning-grasp-keeps-models-on-target-hdtc">Revolutionizing AI Fine-Tuning: GRASP Keeps Models On Target</a></li>
<li><a href="https://arxiv.org/pdf/2605.27676">Unsupervised Identification and Removal of Spurious ...</a></li>
<li><a href="https://arxiv.org/html/2508.09019v1">Activation Steering for Bias Mitigation: An Interpretable Approach to...</a></li>

</ul>
</details>

**Tags**: `#fine-tuning`, `#spurious correlations`, `#bias removal`, `#LLMs`, `#LoRA`

---

<a id="item-29"></a>
## [Soft Specialists: α-Rényi Ensembles for Uncertainty-Aware LLM Post-Training](https://arxiv.org/abs/2605.27747) ⭐️ 8.0/10

Researchers propose an α-Rényi variational framework that learns distributions over post-training parameters for large language models, enabling soft routing of training examples across ensemble members. This approach addresses the fundamental limitation of standard LLM training that forces conflicting data into a single averaged behavior, offering scalable uncertainty quantification and model specialization for supervised fine-tuning and preference optimization. The variational objective interpolates between classical variational Bayes and predictively oriented posterior learning, and the framework uses LoRA adapters attached to a frozen base model for scalable training.

rss · arXiv - Data Science & Statistics · May 28, 04:00

**Background**: Current LLM training learns a single set of parameters from large, often contradictory data, forcing the model to average conflicting goals. Deep ensembles, which train multiple models independently, improve uncertainty but are computationally expensive. The α-Rényi divergence generalizes the Kullback-Leibler divergence used in variational inference, allowing flexible trade-offs between global plausibility and specialization.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27747">[2605.27747] Soft Specialists: ||alpha;$-Rényi Ensembles for ...</a></li>
<li><a href="https://www.machinebrief.com/news/reimagining-ai-training-with-the-a-renyi-variational-framewo-h0pf">Reimagining AI Training with the α-Rényi Variational Framework</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#uncertainty quantification`, `#variational inference`, `#post-training`, `#deep ensembles`

---

<a id="item-30"></a>
## [New extraction process could unlock cheaper, greener lithium](https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/) ⭐️ 8.0/10

Researchers have published a new method in Science for extracting lithium from hard-rock sources that is cheaper and more environmentally friendly than existing techniques. A startup called Rock Zero is commercializing the technology. This breakthrough could significantly reduce the cost and carbon footprint of lithium production, which is critical for electric vehicle batteries and energy storage. It addresses a major bottleneck in the clean energy transition by making lithium supply more sustainable and affordable. The process uses flash Joule heating with chlorine gas to extract lithium chloride from spodumene ore in seconds, achieving 97% purity and 94% yield. This method eliminates the need for sulfuric acid roasting and reduces waste emissions.

rss · MIT Technology Review · May 28, 18:01

**Background**: Lithium is a key component in lithium-ion batteries used in EVs and energy storage. Currently, most lithium is extracted from brine or hard-rock ores like spodumene, but conventional extraction methods are energy-intensive, produce significant waste, and have high carbon emissions. The new method aims to overcome these drawbacks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/">How a new extraction process could unlock the world’s lithium</a></li>
<li><a href="https://rockzero.com/">Rock Zero</a></li>
<li><a href="https://www.science.org/doi/10.1126/sciadv.ady6457">One-step separation of lithium from natural ores in seconds</a></li>

</ul>
</details>

**Tags**: `#lithium`, `#battery technology`, `#energy storage`, `#materials science`, `#sustainability`

---

<a id="item-31"></a>
## [Blocking GPNMB Protein May Halt Parkinson's Spread](https://www.sciencedaily.com/releases/2026/05/260527023214.htm) ⭐️ 8.0/10

Researchers identified the GPNMB protein as a key driver of Parkinson's disease spread and demonstrated that antibodies blocking GPNMB can stop the toxic process from propagating between cells in early experiments. This discovery offers a potential new therapeutic target for Parkinson's disease, which currently lacks treatments that halt disease progression. If validated, antibody-based therapies targeting GPNMB could slow or stop neurodegeneration in millions of patients. The study found that immune cells release GPNMB in response to damaged neurons, creating a vicious cycle that accelerates brain cell degeneration. Antibodies that block GPNMB prevented this toxic spread in cellular models, but further animal and human trials are needed.

rss · ScienceDaily Health · May 28, 07:12

**Background**: Parkinson's disease is a progressive neurodegenerative disorder characterized by the buildup of misfolded α-synuclein protein, which can spread from neuron to neuron. GPNMB is a transmembrane glycoprotein involved in various cellular processes, and its role in Parkinson's spread was previously unknown.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPNMB">GPNMB - Wikipedia</a></li>
<li><a href="https://scitechdaily.com/scientists-may-have-discovered-how-parkinsons-disease-spreads-through-the-brain/">Scientists May Have Discovered How Parkinson’s Disease ...</a></li>

</ul>
</details>

**Tags**: `#Parkinson's disease`, `#neuroscience`, `#protein`, `#therapeutics`, `#biomedical research`

---

<a id="item-32"></a>
## [Brain Scans Challenge Long COVID Inflammation Theory](https://www.sciencedaily.com/releases/2026/05/260527023206.htm) ⭐️ 8.0/10

A new brain imaging study found no evidence of widespread brain inflammation in long COVID patients; instead, severe symptoms were linked to increased activity in mood-related brain regions. This challenges a prevailing hypothesis that brain inflammation drives long COVID, potentially redirecting research toward mood and emotion pathways and influencing treatment approaches. The study used advanced PET imaging to measure inflammation markers, finding no significant difference between long COVID patients and healthy controls. The most severe symptoms correlated with hyperactivity in the amygdala and prefrontal cortex.

rss · ScienceDaily Health · May 28, 05:44

**Background**: Long COVID refers to persistent symptoms weeks or months after acute COVID-19 infection. Previous studies suggested brain inflammation might cause cognitive issues like brain fog, but this new imaging evidence contradicts that idea.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/05/260527023206.htm">Scientists thought brain inflammation was driving long COVID ...</a></li>
<li><a href="https://covidbrainstudy.umn.edu/">Neuroimaging in long COVID | COVID-BRAIN Project</a></li>
<li><a href="https://neurosciencenews.com/covid-flu-brain-fog-inflammation-30192/">COVID-19 Uniquely Rewires the Brain Compared to the Flu</a></li>

</ul>
</details>

**Tags**: `#long COVID`, `#brain imaging`, `#inflammation`, `#neurology`, `#COVID-19`

---

<a id="item-33"></a>
## [Hidden Gut-Brain Circuit Triggers Protein Cravings](https://www.sciencedaily.com/releases/2026/05/260527023202.htm) ⭐️ 8.0/10

Researchers discovered a gut-brain circuit that, when the body is low on protein, sends signals to the brain to reshape cravings toward essential amino acids and away from sugar. This discovery could transform our understanding of appetite, nutrition, and obesity by revealing a direct biological mechanism behind protein cravings. The study, conducted in fruit flies, identified a peptide hormone that rapidly signals amino acid deficiency to the brain while suppressing sugar-seeking behavior.

rss · ScienceDaily Health · May 28, 04:35

**Background**: The gut-brain axis is a communication network linking the gastrointestinal tract and the brain. Previous research showed that dietary amino acids are sensed in the gut, triggering hormone release that signals the brain. This new study identifies a specific circuit that directly controls cravings for protein over sugar.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/05/260527023202.htm">Scientists Discover Hidden Gut-brain Circuit That Triggers ...</a></li>
<li><a href="https://www.technologynetworks.com/neuroscience/news/your-gut-may-know-you-need-protein-before-your-brain-does-412953">Gut-Brain Pathway Controls Protein Cravings | Technology Networks</a></li>
<li><a href="https://www.earth.com/news/your-gut-can-steer-food-cravings-toward-missing-nutrients/">Your gut can steer food cravings toward missing nutrients</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#nutrition`, `#gut-brain axis`, `#obesity`, `#biology`

---