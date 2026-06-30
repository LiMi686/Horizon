---
layout: default
title: "Horizon Summary: 2026-06-30 (EN)"
date: 2026-06-30
lang: en
---

> From 106 items, 28 important content pieces were selected

---

1. [ATHENA-R1: AI agent for treatment reasoning via RL](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Claude Sonnet 5 with Enhanced Agentic Abilities](#item-2) ⭐️ 8.0/10
3. [Claude Code Steganographically Marks Requests](#item-3) ⭐️ 8.0/10
4. [Anthropic Launches Claude Science for Secure Data Science](#item-4) ⭐️ 8.0/10
5. [shot-scraper video: AI agents record web app demos](#item-5) ⭐️ 8.0/10
6. [CuPy: NumPy/SciPy for GPU Acceleration](#item-6) ⭐️ 8.0/10
7. [openpilot: Open-Source Robotics OS for Driver Assistance](#item-7) ⭐️ 8.0/10
8. [Free-for-Dev: Curated List of Free Cloud Services](#item-8) ⭐️ 8.0/10
9. [VeraCrypt: Disk Encryption Based on TrueCrypt](#item-9) ⭐️ 8.0/10
10. [Google Releases TimesFM 2.5 for Time-Series Forecasting](#item-10) ⭐️ 8.0/10
11. [RSEA: Recursive Self-Evolving Agents via Held-Out Selection](#item-11) ⭐️ 8.0/10
12. [Capability Slice Closes Data-Evaluation Loop in LLM Pre-training](#item-12) ⭐️ 8.0/10
13. [GPTNT: Benchmark for Real-Time Multimodal Agent Collaboration](#item-13) ⭐️ 8.0/10
14. [IMCBench: Benchmarking Multimodal LLMs in Medical Conversations](#item-14) ⭐️ 8.0/10
15. [COMPASS: Unified Multimodal Framework for Composition Intent](#item-15) ⭐️ 8.0/10
16. [BV-Blend Stabilizes Critic-Free RL with Verifiable Rewards](#item-16) ⭐️ 8.0/10
17. [SciDraw-Bench: Benchmark for Scientific Figure Generation](#item-17) ⭐️ 8.0/10
18. [Liquid Substrate Necessary for Mesh Intelligence](#item-18) ⭐️ 8.0/10
19. [RL Researchers Must Distinguish Solving Simulators vs. Using as Proxy](#item-19) ⭐️ 8.0/10
20. [Deep Monomial Networks: Math Explains Simpler Model Bias](#item-20) ⭐️ 8.0/10
21. [LLMs' Theory of Mind Emerges Late, Remains Fragile](#item-21) ⭐️ 8.0/10
22. [Turn-Averaged SAEs for Long-Context Interpretability](#item-22) ⭐️ 8.0/10
23. [Static Fibonacci Spacing Outperforms Learned Dilation in Sparse Attention](#item-23) ⭐️ 8.0/10
24. [SEAD: Entropy-Guided On-Policy Distillation Boosts LLM Training](#item-24) ⭐️ 8.0/10
25. [Validating LLM Construct Measurement with Grain Calibration](#item-25) ⭐️ 8.0/10
26. [Probing Phonological Perception in Sign Language Models](#item-26) ⭐️ 8.0/10
27. [RADIANT-PET: LLM + RL Boosts PET/CT Lesion Segmentation](#item-27) ⭐️ 8.0/10
28. [Bidirectional Autoregressive Latent Diffusion for MHD](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ATHENA-R1: AI agent for treatment reasoning via RL](https://arxiv.org/abs/2606.28692) ⭐️ 9.0/10

Researchers introduced ATHENA-R1, an AI agent trained via reinforcement learning over 212 biomedical tools to perform treatment reasoning for all FDA-approved drugs since 1939, without human-annotated traces. ATHENA-R1 significantly outperforms existing models, including GPT-5, on drug and treatment reasoning benchmarks, and its self-learning framework could accelerate clinical decision support without costly human annotations. ATHENA-R1 achieved 94.7% accuracy on open-ended drug reasoning and 82.9% on treatment reasoning, 17.8 and 10.7 points above GPT-5. It also generated adverse-event hypotheses validated in EHR data from 5.4 million patients.

rss · arXiv - AI · Jun 30, 04:00

**Background**: Treatment reasoning is a complex iterative process that integrates disease context, comorbidities, and medications. Reinforcement learning (RL) is a machine learning paradigm where agents learn optimal actions through trial and error, and has been increasingly applied in personalized medicine for sequential decision-making.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12096033/">Reinforcement Learning in Personalized Medicine: A Comprehensive Review of Treatment Optimization Strategies - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41746-024-01316-0">A Primer on Reinforcement Learning in Medicine for Clinicians | npj Digital Medicine</a></li>

</ul>
</details>

**Tags**: `#AI`, `#biomedical`, `#reinforcement learning`, `#clinical decision support`, `#treatment reasoning`

---

<a id="item-2"></a>
## [Anthropic Releases Claude Sonnet 5 with Enhanced Agentic Abilities](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic has released Claude Sonnet 5, a faster and more capable model with improved agentic abilities and instruction following, though it shows weaknesses in trivia and tool-calling tasks. This release is significant because Sonnet 5 offers a better price/quality/speed compromise for agent-assisted development, potentially making autonomous AI agents more accessible and practical for real-world applications. Community benchmarks show Sonnet 5 performs at GLM-5.2 level at 2x cost but also 2x faster; it scores 0/3 on trivia, 45/100 on combined tool-calling, and 77 on puzzle solving. The cost per task chart suggests using Opus instead of Sonnet 5 at higher effort levels.

hackernews · marinesebastian · Jun 30, 17:59 · [Discussion](https://news.ycombinator.com/item?id=48736605)

**Background**: Agentic AI refers to systems that can perceive, reason, and act autonomously to accomplish goals with limited supervision. Tool calling allows LLMs to invoke external functions or APIs by generating structured requests, enabling them to perform real-world tasks beyond text generation.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/agentic-ai/">What is Agentic AI? - Agentic AI Explained - AWS</a></li>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>

</ul>
</details>

**Discussion**: Community feedback is mixed: some users praise Sonnet 5's improved instruction following and one-shotting of complex tasks, while others note its weaknesses in trivia and tool-calling, and question its cost-effectiveness compared to Opus at higher effort levels.

**Tags**: `#AI`, `#LLM`, `#Claude`, `#Anthropic`, `#agentic`

---

<a id="item-3"></a>
## [Claude Code Steganographically Marks Requests](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

Claude Code, Anthropic's AI coding assistant, has been found to embed invisible Unicode markers into system prompts to steganographically mark outgoing requests. This practice was discovered and reported by a security researcher, revealing a lack of transparency about the tool's behavior. This raises serious concerns about user consent and software transparency, as the tool runs code on users' machines without clear disclosure. It could also have legal implications under laws like the CFAA, and undermines trust in AI development tools. The steganographic markers are hidden in Unicode characters that are invisible to users, and the likely intent is to detect API resellers, unauthorized gateways, or model distillation attacks. The implementation has been criticized as sloppy, as it could have been done more subtly.

hackernews · kirushik · Jun 30, 15:44 · [Discussion](https://news.ycombinator.com/item?id=48734373)

**Background**: Steganography is the practice of hiding information within other data, such as images or text, to avoid detection. In this case, Claude Code uses invisible Unicode characters to embed markers in the system prompt, which are then sent to Anthropic's servers. This technique is distinct from encryption, as it conceals the very existence of the hidden data.

<details><summary>References</summary>
<ul>
<li><a href="https://thereallo.dev/blog/claude-code-prompt-steganography">Claude Code Is Steganographically Marking Requests</a></li>
<li><a href="https://spawn-queue.acm.org/doi/10.1145/3806226">In Code They Think; In Proof We Trust | Queue</a></li>

</ul>
</details>

**Discussion**: The community is divided: some view the steganography as a reasonable measure to prevent misuse by Chinese firms, while others condemn it as a violation of user trust and potentially illegal under the CFAA. Critics also note the sloppy implementation and call for greater transparency and sandboxing of development tools.

**Tags**: `#AI`, `#security`, `#ethics`, `#steganography`, `#transparency`

---

<a id="item-4"></a>
## [Anthropic Launches Claude Science for Secure Data Science](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic has launched Claude Science, a new tool that runs a local server and web-based UI, enabling data science tasks in locked-down environments with integrations for databases and HPC clusters. This product addresses a critical gap for researchers in secure environments like pharma, where connecting to sensitive data is often impossible with cloud-based tools, potentially accelerating scientific discovery in regulated industries. Claude Science is distinct from Claude Code and Cowork as it runs a local server with a browser-based UI, allowing it to operate in air-gapped or tightly controlled networks. It supports integrations with institutional clusters and various databases.

hackernews · lebovic · Jun 30, 17:07 · [Discussion](https://news.ycombinator.com/item?id=48735770)

**Background**: Data science in highly regulated industries often requires working with sensitive data that cannot leave local networks. Traditional cloud-based AI tools are unsuitable for such environments, creating a need for on-premises solutions that combine AI capabilities with local data access.

**Discussion**: Community comments highlight the product's value for secure environments, with one builder of a connected HPC tool noting its integrations with institutional clusters. A domain expert tested it for RNAi biopesticide design and found it competent but not exceptional, noting caveats like using mammalian design rules.

**Tags**: `#AI`, `#data science`, `#Anthropic`, `#research tools`, `#HPC`

---

<a id="item-5"></a>
## [shot-scraper video: AI agents record web app demos](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison released shot-scraper 1.10 with a new 'video' command that accepts a storyboard.yml file and uses Playwright to record a video of a web application routine. The tool is designed to let coding agents automatically produce video demos of their work. This tool addresses a practical need in AI agent development: proving that code actually works by producing visual demos. It enables agents to autonomously create shareable video evidence of their accomplishments, which is valuable for debugging, documentation, and stakeholder communication. The storyboard.yml file can define a local server to start, viewport size, cursor visibility, wait conditions, JavaScript overrides (e.g., for clipboard mocking), and a sequence of scenes with actions like clicks and pauses. The command supports --auth for cookie-based authentication and outputs video in WebM or MP4 format.

rss · Simon Willison · Jun 30, 16:54

**Background**: shot-scraper is a CLI tool by Simon Willison for taking screenshots and scraping websites using Playwright. The new 'video' command extends it to record full video demos, building on the idea that AI coding agents should produce demos to prove their work actually runs. Playwright is a browser automation library that can record videos of page interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot-scraper video</a></li>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper/">Release: shot-scraper 1.10 - Simon Willison's Weblog</a></li>
<li><a href="https://github.com/simonw/shot-scraper/issues">Issues · simonw/shot-scraper - GitHub</a></li>

</ul>
</details>

**Tags**: `#developer-tools`, `#AI-agents`, `#video-recording`, `#playwright`, `#automation`

---

<a id="item-6"></a>
## [CuPy: NumPy/SciPy for GPU Acceleration](https://github.com/cupy/cupy) ⭐️ 8.0/10

CuPy is an open-source library that provides NumPy- and SciPy-compatible APIs for GPU-accelerated computing, supporting NVIDIA CUDA and AMD ROCm platforms. It enables users to run existing NumPy/SciPy code on GPUs with minimal changes. CuPy significantly accelerates numerical computing tasks by leveraging GPU parallelism, making it valuable for data science, machine learning, and scientific computing. It serves as a drop-in replacement for NumPy/SciPy, lowering the barrier for GPU adoption. CuPy supports both CUDA and ROCm backends, with binary wheels available for Linux and Windows. It also provides low-level CUDA features like RawKernels, Streams, and direct CUDA Runtime API calls.

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**Background**: NumPy and SciPy are fundamental Python libraries for numerical computing, but they run on CPUs. CuPy extends their functionality to GPUs, which excel at parallel operations, enabling faster computation for large arrays and complex mathematical operations.

**Tags**: `#GPU computing`, `#NumPy`, `#SciPy`, `#Python`, `#machine learning`

---

<a id="item-7"></a>
## [openpilot: Open-Source Robotics OS for Driver Assistance](https://github.com/commaai/openpilot) ⭐️ 8.0/10

openpilot, an open-source operating system for robotics, now supports over 300 car models for upgrading driver assistance systems. It is available on GitHub under the MIT license. openpilot democratizes access to advanced driver assistance technology, enabling enthusiasts and researchers to experiment with and improve autonomous driving capabilities. Its open-source nature fosters community innovation and accelerates development in the robotics and automotive sectors. To use openpilot, users need a supported device (e.g., comma four), compatible car, and a car harness. The software can be installed via a URL, and prebuilt branches are available for stable releases.

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**Background**: openpilot is developed by comma.ai, a company focused on building a self-driving car platform. It runs on custom hardware like the comma four and provides features such as adaptive cruise control and lane keeping. The project is one of the most popular open-source autonomous driving systems on GitHub.

**Tags**: `#autonomous driving`, `#open source`, `#robotics`, `#driver assistance`, `#comma.ai`

---

<a id="item-8"></a>
## [Free-for-Dev: Curated List of Free Cloud Services](https://github.com/ripienaar/free-for-dev) ⭐️ 8.0/10

The ripienaar/free-for-dev GitHub repository, maintained by over 1600 contributors, continues to be updated with a comprehensive list of SaaS, PaaS, and IaaS offerings that provide free tiers for developers and DevOps practitioners. This resource saves developers significant time by aggregating free-tier services in one place, helping them make informed infrastructure decisions without costly trials. It is widely referenced in the developer community and serves as a go-to guide for cost-effective cloud usage. The list explicitly excludes self-hosted software and requires free tiers to last at least one year if time-bucketed; it also mandates TLS support in free tiers. The repository is opinionated and focuses on infrastructure-related services, not general free tools.

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**Background**: SaaS, PaaS, and IaaS are cloud service models that provide software, platforms, and infrastructure over the internet. Many providers offer free tiers with limited resources to attract developers, but finding and comparing them can be time-consuming. This curated list, started by R.I. Pienaar, has grown through community contributions to become a trusted reference.

**Tags**: `#devops`, `#free-tier`, `#SaaS`, `#PaaS`, `#IaaS`

---

<a id="item-9"></a>
## [VeraCrypt: Disk Encryption Based on TrueCrypt](https://github.com/veracrypt/VeraCrypt) ⭐️ 8.0/10

VeraCrypt is a disk encryption software derived from TrueCrypt 7.1a, incorporating security enhancements and ongoing maintenance. The GitHub repository provides source code for Windows, Linux, macOS, FreeBSD, and OpenBSD. VeraCrypt addresses security vulnerabilities in TrueCrypt while maintaining compatibility, making it a trusted tool for protecting sensitive data. Its open-source nature and cross-platform support ensure broad adoption among security-conscious users. The repository includes pre-built EFI boot loader binaries and detailed build instructions for Windows, requiring Visual Studio and Windows SDK. Official binaries are digitally signed with IDRIX's GlobalSign certificate, adding approximately 10 KiB to file sizes.

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**Background**: TrueCrypt was a popular disk encryption tool that was abruptly discontinued in 2014 amid security concerns. VeraCrypt was forked from TrueCrypt 7.1a to continue development and fix vulnerabilities, such as those found in the TrueCrypt audit. It uses stronger key derivation algorithms (e.g., PBKDF2 with higher iterations) and addresses other security issues.

**Tags**: `#encryption`, `#security`, `#open-source`, `#disk-encryption`, `#cryptography`

---

<a id="item-10"></a>
## [Google Releases TimesFM 2.5 for Time-Series Forecasting](https://github.com/google-research/timesfm) ⭐️ 8.0/10

Google Research has released TimesFM 2.5, a pretrained foundation model for time-series forecasting, with checkpoints available on Hugging Face and integrations into BigQuery ML, Google Sheets, and Vertex Model Garden. This release democratizes access to state-of-the-art time-series forecasting, enabling enterprises and developers to leverage a powerful foundation model without extensive training. Its integration into Google products like BigQuery ML simplifies deployment at scale. TimesFM 2.5 uses 200M parameters (down from 500M), supports up to 16k context length, and offers continuous quantile forecasts up to 1k horizon via an optional 30M quantile head. It also includes a Flax version for faster inference and fine-tuning support via LoRA.

rss · GitHub Trending - Python · Jun 30, 23:04

**Background**: Time-series forecasting predicts future values based on historical data, used in finance, weather, and inventory management. Foundation models are large pretrained models that can be adapted to various tasks with minimal fine-tuning. TimesFM is a decoder-only transformer model published at ICML 2024.

**Discussion**: The community has actively contributed to TimesFM, with shoutouts to contributors like @kashif and @darkpowerxo for fine-tuning examples, and @borealBytes for adding agent support. The open-source release has been well-received, with ongoing improvements and unit tests added.

**Tags**: `#time-series forecasting`, `#foundation model`, `#Google Research`, `#machine learning`, `#ICML 2024`

---

<a id="item-11"></a>
## [RSEA: Recursive Self-Evolving Agents via Held-Out Selection](https://arxiv.org/abs/2606.28374) ⭐️ 8.0/10

Researchers introduced RSEA, a recursive self-evolving LLM agent that improves its natural-language state via a strict keep-better gate using held-out data, outperforming baselines across four benchmarks. This work provides a principled approach to recursive self-improvement of LLM agents without weight updates, addressing the problem of regression in context evolution, which is crucial for reliable autonomous agents. RSEA carries a three-layer natural-language state (strategy, skills, playbook) and commits a candidate only if it does not regress on a disjoint held-out split. It achieved 69.3% on ALFWorld (vs. 64.6% for ReAct) and 79.4% with retry, but concrete-workflow induction (AWM) was best on tool-use tasks.

rss · arXiv - AI · Jun 30, 04:00

**Background**: LLM agents often improve by evolving natural-language artifacts like prompts or workflows without updating model weights. However, unguarded evolution can cause performance collapse on some tasks, as seen with Dynamic Cheatsheet on WebShop (score 0.14 vs. ReAct's 0.43). RSEA's held-out selection ensures monotone-safe evolution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.28374">[2606.28374] Recursive Self-Evolving Agents via Held-Out Selection - arXiv</a></li>
<li><a href="https://artificialintelligenceherald.com/ai/rsea-recursive-self-evolving-agents-held-out-selection-2026">RSEA Recursive Self-Evolving Agents via Held-Out Selection - AI Herald</a></li>
<li><a href="https://www.machinebrief.com/news/rsea-a-new-direction-in-ais-evolutionary-tactics-36cc">RSEA: A New Direction in AI's Evolutionary Tactics - Machine Brief</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#self-improvement`, `#benchmarking`, `#natural-language state`, `#recursive evolution`

---

<a id="item-12"></a>
## [Capability Slice Closes Data-Evaluation Loop in LLM Pre-training](https://arxiv.org/abs/2606.28471) ⭐️ 8.0/10

The paper introduces the 'capability slice' as a unit to bridge data and evaluation in LLM pre-training, enabling systematic localization of model weaknesses through a structured taxonomy and mapping rules. This work addresses a practical gap in LLM optimization by replacing intuitive inference with a routine, auditable method for translating benchmark failures into targeted data interventions, potentially improving model efficiency and performance. The capability slice groups evaluation samples by background condition, task type, solving operation, and output constraint, balancing precision and stability. Two case studies demonstrate the loop's ability to correctly rule data in or out, including recovering BBH performance by fixing a masked <EOS> loss.

rss · arXiv - AI · Jun 30, 04:00

**Background**: In LLM pre-training, data shapes model capability prospectively, while evaluation reveals it retrospectively through noisy scores. Engineers often rely on intuition to infer data fixes from benchmark failures due to incompatible vocabularies between data and evaluation. The capability slice provides a common unit to close this feedback loop.

**Tags**: `#LLM`, `#evaluation`, `#data-centric AI`, `#pre-training`, `#model capability`

---

<a id="item-13"></a>
## [GPTNT: Benchmark for Real-Time Multimodal Agent Collaboration](https://arxiv.org/abs/2606.28514) ⭐️ 8.0/10

Researchers introduced GPTNT, a benchmark built on the cooperative game Keep Talking and Nobody Explodes, to evaluate real-time collaboration between multimodal agents under time pressure and information asymmetry. This benchmark fills a gap in existing evaluations by testing collaboration under realistic conditions like time pressure and imperfect communication, which are crucial for deploying AI in human-agent teams. In GPTNT, one agent sees and manipulates the bomb but lacks defusal instructions, while the other has instructions but cannot see the bomb; neither can succeed alone, and current state-of-the-art models fail to defuse a single bomb in real time.

rss · arXiv - AI · Jun 30, 04:00

**Background**: Multimodal agents combine vision, language, and action to solve tasks. Existing benchmarks often test component capabilities in isolation, ignoring the combined challenges of time pressure, information asymmetry, and imperfect communication that occur in real-world collaboration.

**Tags**: `#multimodal agents`, `#benchmark`, `#multi-agent collaboration`, `#real-time communication`, `#AI evaluation`

---

<a id="item-14"></a>
## [IMCBench: Benchmarking Multimodal LLMs in Medical Conversations](https://arxiv.org/abs/2606.28556) ⭐️ 8.0/10

Researchers introduced IMCBench, a benchmark that pairs real clinical images with synthetic patient profiles to evaluate multimodal LLMs in multi-turn medical conversations across safety, accuracy, and uncertainty dimensions. Eight frontier models from four families (Claude, GPT, Nova, Llama) were scored on a 1-5 scale using LLM-as-Jury calibrated against expert clinicians. This benchmark addresses a critical gap by combining multimodal inputs with multi-turn conversations, providing a more realistic evaluation for medical AI. The findings that accurate clinical description does not guarantee safe guidance highlight the need for multi-dimensional evaluation frameworks in healthcare AI. Claude Opus 4.6 achieved the highest overall score (3.61), but no model dominated all dimensions; safety degraded for malignant and rare conditions (Δ = -0.27 each). Ablation studies showed that removing visual input or EHR context reduced safety scores by 0.18 and 0.23 on average, respectively.

rss · arXiv - AI · Jun 30, 04:00

**Background**: Large language models and vision-language models have shown promise in clinical applications like decision support and triaging. However, existing medical AI benchmarks either support multi-turn dialogues without images or provide multimodal inputs for single-turn QA, lacking a realistic combination. IMCBench fills this gap by using real clinical images and synthetic profiles to simulate patient-clinician interactions.

**Tags**: `#multimodal LLM`, `#medical AI`, `#benchmark`, `#clinical conversation`, `#vision-language model`

---

<a id="item-15"></a>
## [COMPASS: Unified Multimodal Framework for Composition Intent](https://arxiv.org/abs/2606.28696) ⭐️ 8.0/10

COMPASS introduces a unified multimodal framework that uses a shared expert token to enable both composition perception and composition-guided generation within a single system. This addresses a key limitation in current multimodal models, which struggle with fine-grained composition recognition and controllable generation, potentially enabling more precise image editing and layout control. The framework uses a Mixture-of-Experts (MoE) backbone with a shared expert token τ_c, and is trained on Comp-11, a large-scale dataset with 11-class taxonomy and reasoning-augmented annotations.

rss · arXiv - AI · Jun 30, 04:00

**Background**: Unified multimodal models aim to handle both understanding and generation tasks, but they often fail at fine-grained composition tasks like object placement. COMPASS bridges this gap by introducing a dedicated composition intent token that guides both perception and generation.

**Tags**: `#multimodal`, `#composition`, `#generation`, `#MoE`, `#computer vision`

---

<a id="item-16"></a>
## [BV-Blend Stabilizes Critic-Free RL with Verifiable Rewards](https://arxiv.org/abs/2606.28707) ⭐️ 8.0/10

Researchers introduced BV-Blend, a critic-free reinforcement learning framework that stabilizes advantage estimation by combining prompt-local on-policy statistics with semantic-cluster-conditioned historical moments, addressing the zero-advantage issue in GRPO when all rollouts in a prompt group receive identical rewards. This work improves training stability and performance for aligning large language models using verifiable rewards, particularly in cold-start regimes with binary verifiers, without the memory and compute overhead of critic-based methods like PPO. BV-Blend maintains EMA-tracked reward moments for each semantic cluster, derives a confidence weight from a standard error of the mean (SEM) proxy, and blends historical and prompt-local baseline and variance statistics into a standardized advantage for PPO-style clipped updates.

rss · arXiv - AI · Jun 30, 04:00

**Background**: Group Relative Policy Optimization (GRPO) is a critic-free RL method that avoids training a value function, reducing memory and compute compared to PPO. However, GRPO's advantage estimation relies on within-group reward statistics and can become unstable when all responses in a group receive identical rewards, leading to zero advantages and stalled learning. BV-Blend addresses this by incorporating historical reward moments from semantically similar prompts.

**Tags**: `#reinforcement learning`, `#large language models`, `#RLHF`, `#advantage estimation`, `#GRPO`

---

<a id="item-17"></a>
## [SciDraw-Bench: Benchmark for Scientific Figure Generation](https://arxiv.org/abs/2606.28406) ⭐️ 8.0/10

Researchers introduced SciDraw-Bench, a benchmark of 32 structured tasks across eight figure types and ten disciplines, designed to evaluate scientific figure generation by text-to-image and multimodal models. Existing benchmarks only evaluate natural images, but SciDraw-Bench fills a critical gap by measuring text fidelity, semantic correctness, structural quality, and convention adherence, which are essential for scientific figures. The benchmark uses a four-dimensional evaluation protocol including OCR-based text fidelity and VLM-based semantic correctness, and a pilot study showed that a domain-specific system (SciDraw AI) outperformed general-purpose models on all dimensions, with text fidelity being the hardest.

rss · arXiv - Machine Learning · Jun 30, 04:00

**Background**: Text-to-image models like DALL-E and Stable Diffusion can generate natural images, but scientific figures require precise labels, correct relationships, and adherence to disciplinary conventions. Existing benchmarks like GenEval and T2I-CompBench do not test these aspects. SciDraw-Bench provides machine-checkable specifications for each task to enable automated evaluation.

**Tags**: `#AI`, `#benchmark`, `#scientific figures`, `#text-to-image`, `#multimodal`

---

<a id="item-18"></a>
## [Liquid Substrate Necessary for Mesh Intelligence](https://arxiv.org/abs/2606.28413) ⭐️ 8.0/10

A new arXiv paper proves that optimal estimation in a mesh of sovereign agents requires an adaptive timescale and gap-aware processing, which fixed-gain filters and gap-blind networks cannot achieve. This work establishes fundamental theoretical constraints for decentralized multi-agent systems, with implications for distributed AI, adaptive systems, and mesh intelligence architectures. The paper proves two necessary conditions: an adaptive timescale is necessary (fixed-gain filters are strictly suboptimal), and gap-aware processing is necessary (gap-blind networks cannot recover the missing dependence at any width or depth).

rss · arXiv - Machine Learning · Jun 30, 04:00

**Background**: A mesh of sovereign agents has no central clock, model, or coordinator; each agent must estimate a latent state from irregular observations. The paper shows that only continuous-time liquid networks satisfy both necessary conditions, while LSTMs satisfy only the first and fixed continuous-time filters satisfy only the second.

**Tags**: `#mesh intelligence`, `#distributed systems`, `#adaptive estimation`, `#multi-agent systems`, `#theoretical computer science`

---

<a id="item-19"></a>
## [RL Researchers Must Distinguish Solving Simulators vs. Using as Proxy](https://arxiv.org/abs/2606.28433) ⭐️ 8.0/10

A position paper argues that RL researchers often conflate two distinct uses of simulators: solving the simulator itself versus using it as a proxy for real-world deployment, leading to misdirected research efforts. This distinction is crucial because the constraints, algorithms, and evaluation metrics differ fundamentally between the two settings, and failing to clarify which is being used can produce misleading conclusions and hinder progress toward general-purpose decision-making. The paper provides examples and simple experiments showing how solutions optimized purely for simulator performance (e.g., exploiting simulator quirks) may not transfer to real-world deployment, and calls for clearer empirical practices.

rss · arXiv - Machine Learning · Jun 30, 04:00

**Background**: Reinforcement learning research often uses benchmark simulators to develop and test algorithms before real-world deployment. However, the goal of achieving high scores in these simulators can inadvertently shift focus to solving the simulator itself, which is a different research problem.

**Tags**: `#reinforcement learning`, `#simulators`, `#research methodology`, `#benchmarking`

---

<a id="item-20"></a>
## [Deep Monomial Networks: Math Explains Simpler Model Bias](https://arxiv.org/abs/2606.28464) ⭐️ 8.0/10

A new paper uses polynomial algebra and Mason's Theorem to prove that critical points in deep monomial networks correspond exactly to subnetworks, providing a mathematical foundation for Occam's razor-like implicit bias in deep learning. This work offers a rigorous mathematical explanation for why deep neural networks tend to converge to simpler functions, which is a fundamental question in deep learning theory and could guide the design of more interpretable and efficient architectures. The analysis focuses on fully-connected networks with monomial activations and uses Mason's Theorem (the polynomial version) to show that for sufficiently large activation degree, criticality occurs precisely at parameter configurations where some neurons are inactive or redundant.

rss · arXiv - Machine Learning · Jun 30, 04:00

**Background**: Singular Learning Theory (SLT) studies the geometry of loss landscapes in overparameterized models, where singularities (rank-deficient points) dominate. Implicit bias refers to the tendency of gradient-based optimization to favor simpler solutions without explicit regularization. This paper bridges SLT and polynomial algebra to explain that bias.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/singular-learning-theory">Singular Learning Theory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mason's_theorem">Mason's theorem</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#singular learning theory`, `#implicit bias`, `#neural networks`, `#mathematical theory`

---

<a id="item-21"></a>
## [LLMs' Theory of Mind Emerges Late, Remains Fragile](https://arxiv.org/abs/2606.28524) ⭐️ 8.0/10

A new study traces the developmental trajectory of mental state reasoning in LLMs, showing that false belief task performance emerges late in pretraining, depends on model size and training volume, and is most improved by post-training interventions like SFT and DPO. This work provides a developmental perspective on theory of mind in LLMs, addressing construct validity concerns and revealing fragility that has implications for AI safety and interpretability. The study uses the Olmo2 and Pythia model suites, finding that false belief performance is fragile: non-factive verbs like 'thinks' increase false belief attributions even in true belief conditions, and situation models show incoherence regarding agent knowledge states.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: Theory of mind is the ability to attribute mental states to others, and false belief tasks are a classic test. Recent work suggests LLMs can pass such tasks, but concerns about construct validity remain. This study adopts a developmental approach, tracking abilities across training stages.

**Tags**: `#LLMs`, `#theory of mind`, `#mentalizing`, `#AI safety`, `#cognitive science`

---

<a id="item-22"></a>
## [Turn-Averaged SAEs for Long-Context Interpretability](https://arxiv.org/abs/2606.28548) ⭐️ 8.0/10

Researchers introduce turn-averaged sparse autoencoders (SAEs) that represent entire human or assistant turns with fixed-size feature vectors, enabling efficient feature discovery and attribution in long model transcripts. This addresses a key scaling limitation of standard SAEs, which require features proportional to context length, making long-context interpretability practical for mechanistic interpretability research. Turn-averaged SAEs reconstruct the average model activation across a turn rather than individual token activations, and the paper shows they describe high-level turn characteristics more completely than per-token features when judged by an LLM.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: Sparse autoencoders (SAEs) are a common tool for extracting interpretable features from language models by learning sparse representations of activations. Standard SAEs operate on individual token activations, so analyzing long conversations or documents requires processing many token-level features, which scales poorly.

**Tags**: `#sparse autoencoders`, `#interpretability`, `#mechanistic interpretability`, `#long-context`, `#language models`

---

<a id="item-23"></a>
## [Static Fibonacci Spacing Outperforms Learned Dilation in Sparse Attention](https://arxiv.org/abs/2606.28560) ⭐️ 8.0/10

A new paper proposes a static per-layer stagger of Fibonacci-spaced offsets for sparse self-attention, which improves perplexity over learned dilation and reduces inference latency by roughly five times. This finding challenges the common practice of learning attention patterns and offers a simpler, more efficient alternative that also enables extrapolation to longer sequences, which is critical for scaling transformer models. The study trains 21 language models with 60M parameters and compares four alpha-setting methods; the static stagger achieves parity with learned Fibonacci attention while being base-agnostic and much faster.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: Sparse attention reduces the quadratic complexity of standard self-attention by limiting each query to attend to a subset of keys. Common approaches include fixed patterns like sliding windows or learned patterns via learned dilation. This work explores a static Fibonacci-spaced pattern with a per-layer scalar alpha that compresses or expands the spacing.

**Tags**: `#sparse attention`, `#transformer`, `#efficiency`, `#deep learning`, `#NLP`

---

<a id="item-24"></a>
## [SEAD: Entropy-Guided On-Policy Distillation Boosts LLM Training](https://arxiv.org/abs/2606.28562) ⭐️ 8.0/10

SEAD introduces an entropy-guided supervision method for on-policy distillation that selectively skips ~50% of tokens, anneals KL divergence from forward to reverse, and uses a competence-gated curriculum, achieving +4.8 average accuracy on OLMo-3 models (7B-32B) across six math benchmarks. This work addresses a key inefficiency in on-policy distillation—uniform supervision ignoring student competence—and demonstrates significant gains on large models, potentially reducing training cost and improving LLM performance in math reasoning tasks. SEAD uses joint teacher-student entropy to partition tokens into zones with tailored divergences or zero gradient, a cosine schedule to anneal from forward to reverse KL divergence, and a competence-gated curriculum that introduces prompts from easy to hard; ablations confirm super-additive interactions among components.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: On-policy distillation (OPD) is a knowledge distillation technique where the student model generates its own token sequences for training, unlike offline distillation that uses fixed teacher outputs. In OPD, teacher supervision quality depends on student competence: incoherent rollouts yield noisy gradients, while already-mastered tokens produce redundant ones. Existing methods supervise uniformly, wasting computation at token, phase, and prompt scales. SEAD uses entropy as a unified probe to detect this competence-dependent degradation and adapt supervision accordingly.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/On-policy_distillation">On-policy distillation</a></li>

</ul>
</details>

**Tags**: `#knowledge distillation`, `#on-policy distillation`, `#LLM training`, `#entropy`, `#curriculum learning`

---

<a id="item-25"></a>
## [Validating LLM Construct Measurement with Grain Calibration](https://arxiv.org/abs/2606.28574) ⭐️ 8.0/10

This paper introduces grain calibration, a method to validate whether large language models (LLMs) measure theoretical constructs correctly, not just reliably, by decomposing constructs into clause-level components and testing each against text with extractive evidence. This addresses a critical gap in current LLM validation practices, which often conflate reliability with construct validity, and provides a theoretically grounded solution that could improve the methodological rigor of NLP and social science research. Grain calibration uses an explicit, theory-derived rule to combine component results, making the reasoning process transparent and enabling diagnosis of whether a component was missed or an adjacent construct mistaken.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: In social science and NLP, researchers often use LLMs to code text for theoretical constructs (e.g., sentiment, bias). Reliability (agreement with human annotators) is commonly checked, but construct validity—whether the LLM actually measures the intended concept—is rarely assessed. Grain calibration aims to fill this gap.

**Tags**: `#LLM`, `#construct validity`, `#NLP`, `#measurement`, `#methodology`

---

<a id="item-26"></a>
## [Probing Phonological Perception in Sign Language Models](https://arxiv.org/abs/2606.28667) ⭐️ 8.0/10

A new study probes phonological sensitivity in sign language recognition models, revealing that pose-based models excel at handshape contrasts while pixel-based models better capture location changes. This work addresses a critical gap in understanding whether SLR models learn abstract linguistic features or low-level correlations, with implications for both NLP and linguistics. The study used minimal pairs and human behavioral data to evaluate models trained on American Sign Language, finding that pose-based models achieve a correlation of r~0.49 with human perceptual similarity judgments.

rss · arXiv - NLP · Jun 30, 04:00

**Background**: Sign languages are compositional systems where meaning arises from combining sublexical phonological parameters like handshape, location, and movement. Deep learning models for sign language recognition have improved on translation benchmarks, but it was unclear if they truly understand these phonological features.

**Tags**: `#sign language recognition`, `#phonological perception`, `#deep learning`, `#linguistics`, `#model interpretability`

---

<a id="item-27"></a>
## [RADIANT-PET: LLM + RL Boosts PET/CT Lesion Segmentation](https://arxiv.org/abs/2606.28392) ⭐️ 8.0/10

Researchers propose RADIANT-PET, a framework that combines a permissive segmentation model with LLM-based adjudication and reinforcement learning (GRPO) to improve PET/CT lesion segmentation accuracy. This work addresses a critical clinical challenge by reducing false positives from physiologic tracer uptake, potentially improving oncology diagnostics and treatment planning. The framework uses Group Relative Policy Optimization (GRPO) to fine-tune a local LLM for lesion-level reasoning, and achieves the largest improvements when radiology reports are provided as additional context.

rss · arXiv - Computer Vision · Jun 30, 04:00

**Background**: PET/CT is a common imaging modality for cancer diagnosis, but distinguishing malignant lesions from benign tracer uptake is difficult. Traditional segmentation models operate at the voxel level and often produce false positives. RADIANT-PET introduces a reasoning layer using LLMs to mimic clinical interpretation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Group_Relative_Policy_Optimization">Group Relative Policy Optimization</a></li>

</ul>
</details>

**Tags**: `#medical imaging`, `#segmentation`, `#large language models`, `#reinforcement learning`, `#oncology`

---

<a id="item-28"></a>
## [Bidirectional Autoregressive Latent Diffusion for MHD](https://arxiv.org/abs/2606.29620) ⭐️ 8.0/10

A new bidirectional autoregressive latent diffusion model is proposed for forward and inverse magnetohydrodynamics (MHD), enabling self-supervised uncertainty estimation and non-invasive plasma diagnostics. This work advances scientific machine learning by providing a method that can estimate uncertainty without ground truth, which is crucial for reliable plasma diagnostics and fusion energy research. The model predicts multiple fields (density, pressure, velocity, magnetic field) and uses bidirectional flow consistency as a self-supervised metric for uncertainty and error estimation at test time.

rss · arXiv - Data Science & Statistics · Jun 30, 04:00

**Background**: Magnetohydrodynamics (MHD) studies the interaction between electrically conducting fluids and magnetic fields, with applications in astrophysics and fusion energy. Forward problems simulate MHD evolution, while inverse problems infer initial or boundary conditions from observations. Latent diffusion models are generative models that learn data distributions in a compressed latent space.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1212.3447">Forward and inverse problems in fundamental and applied ... - arXiv</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/gamm.200790005">Forward and inverse problems in MHD: Numerical and experimental ...</a></li>
<li><a href="https://link.springer.com/article/10.1140/epjst/e2013-01793-3">Forward and inverse problems in fundamental and applied ...</a></li>

</ul>
</details>

**Tags**: `#magnetohydrodynamics`, `#latent diffusion`, `#uncertainty estimation`, `#plasma diagnostics`, `#scientific machine learning`

---