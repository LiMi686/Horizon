---
layout: default
title: "Horizon Summary: 2026-05-08 (EN)"
date: 2026-05-08
lang: en
---

> From 93 items, 46 important content pieces were selected

---

1. [Dirtyfrag: New Linux LPE Exploit Goes Public](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Natural Language Autoencoders for LLM Interpretability](#item-2) ⭐️ 9.0/10
3. [Mozilla Uses Claude Mythos to Fix Hundreds of Firefox Bugs](#item-3) ⭐️ 9.0/10
4. [TabPFN: Foundation Model for Tabular Data](#item-4) ⭐️ 9.0/10
5. [Triton v3.7.0 Adds Squeeze, Scaled BMM, FP8 Constants](#item-5) ⭐️ 8.0/10
6. [Canvas LMS Down After ShinyHunters Breach Threatens Data Leak](#item-6) ⭐️ 8.0/10
7. [Cloudflare to cut about 20% workforce](#item-7) ⭐️ 8.0/10
8. [Agents need control flow, not more prompts](#item-8) ⭐️ 8.0/10
9. [DeepSeek 4 Flash: Local Inference Engine for Apple Metal](#item-9) ⭐️ 8.0/10
10. [AlphaEvolve: Gemini-powered coding agent scales across fields](#item-10) ⭐️ 8.0/10
11. [AI Slop Overwhelms Online Communities](#item-11) ⭐️ 8.0/10
12. [DFlash: Block Diffusion for Efficient Speculative Decoding](#item-12) ⭐️ 8.0/10
13. [Local Deep Research: Open-source tool achieves ~95% on SimpleQA](#item-13) ⭐️ 8.0/10
14. [Agent Skills: Production-Grade Engineering for AI Coders](#item-14) ⭐️ 8.0/10
15. [Goose AI Agent Moves to Linux Foundation's AAIF](#item-15) ⭐️ 8.0/10
16. [OpenAI Releases Curated Codex Plugin Examples](#item-16) ⭐️ 8.0/10
17. [Interpretability Method Distinguishes Sources of Annotator Disagreement](#item-17) ⭐️ 8.0/10
18. [ZAYA1-8B: 700M Active MoE Model Matches Larger Models](#item-18) ⭐️ 8.0/10
19. [Partial Evidence Bench: Benchmarking Authorization-Limited Evidence](#item-19) ⭐️ 8.0/10
20. [BALAR: Bayesian Agentic Loop Boosts LLM Active Reasoning](#item-20) ⭐️ 8.0/10
21. [LLM Sycophancy as Boundary Failure Between Alignment and Epistemic Integrity](#item-21) ⭐️ 8.0/10
22. [PRISM: Closed-Loop VLM-LLM for Embodied Agents](#item-22) ⭐️ 8.0/10
23. [FinAgent-RAG: Agentic RAG for Financial QA](#item-23) ⭐️ 8.0/10
24. [LaTA: FERPA-Compliant Local LLM Autograder for STEM](#item-24) ⭐️ 8.0/10
25. [Constant-Context Skill Learning for LLM Agents](#item-25) ⭐️ 8.0/10
26. [Are Flat Minima an Illusion?](#item-26) ⭐️ 8.0/10
27. [SAT: Coordinator-Free Multi-LLM Training with Guarantees](#item-27) ⭐️ 8.0/10
28. [Horizon-Constrained Rashomon Sets for Chaotic Forecasting](#item-28) ⭐️ 8.0/10
29. [Sparse Prefix Caching Optimizes Hybrid/Recurrent LLM Serving](#item-29) ⭐️ 8.0/10
30. [Non-Neural Framework Learns Interpretable Basis Functions from Data](#item-30) ⭐️ 8.0/10
31. [Token-Selective Attention: Adaptive Layer Skipping in Transformers](#item-31) ⭐️ 8.0/10
32. [Geometric Theory Reveals Instability in Feature Composition](#item-32) ⭐️ 8.0/10
33. [SLAM: Watermarking LLMs via Linguistic Structure](#item-33) ⭐️ 8.0/10
34. [ReaComp: Compiling LLM Reasoning into Symbolic Solvers](#item-34) ⭐️ 8.0/10
35. [Domain-Trained SLM Outperforms Frontier LLMs on Contract Extraction](#item-35) ⭐️ 8.0/10
36. [Recorruption: How Accurate Context Harms Multimodal RAG](#item-36) ⭐️ 8.0/10
37. [When2Speak Dataset Teaches LLMs When to Intervene](#item-37) ⭐️ 8.0/10
38. [Response-Aware Defense Against Multi-Turn LLM Attacks](#item-38) ⭐️ 8.0/10
39. [Layout-Aware Learning for Open-Set ID Fraud Detection](#item-39) ⭐️ 8.0/10
40. [Density-Aware Calibration for 3D Detection Under Shift](#item-40) ⭐️ 8.0/10
41. [ViTok-v2 Scales Vision Autoencoders to 5B Parameters](#item-41) ⭐️ 8.0/10
42. [Tamaththul3D: High-Fidelity Saudi Sign Language Avatars from Monocular Video](#item-42) ⭐️ 8.0/10
43. [InfoTree: Submodular Tree Search for Tool-Use RL](#item-43) ⭐️ 8.0/10
44. [Benign Regularizer Reveals Hidden Convexity in Nonconvex Matrix Estimation](#item-44) ⭐️ 8.0/10
45. [Neural Conditional Scores Enable SDE Inference from Sparse Data](#item-45) ⭐️ 8.0/10
46. [Spectral Lens: Diagnosing LLM Training via Activation and Gradient Spectra](#item-46) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Dirtyfrag: New Linux LPE Exploit Goes Public](https://www.openwall.com/lists/oss-security/2026/05/07/8) ⭐️ 9.0/10

A new Linux local privilege escalation vulnerability called Dirtyfrag has been publicly disclosed with a working exploit, chaining xfrm-ESP and RxRPC page-cache write bugs to gain root access on major distributions. No patches or CVEs are available yet as the embargo was broken early. This vulnerability is critical because it affects all major Linux distributions, has a public exploit, and no patches are available, putting millions of systems at risk of local privilege escalation. It follows closely after the similar Copy Fail vulnerability, highlighting a recurring class of kernel bugs. Dirtyfrag chains two page-cache write vulnerabilities: one in xfrm-ESP (IPsec) present since January 2017, and another in RxRPC. The exploit bypasses individual protections to achieve full root access, and the write-up notes that the xfrm-ESP sink is the same as in Copy Fail.

hackernews · flipped · May 7, 19:21 · [Discussion](https://news.ycombinator.com/item?id=48053623)

**Background**: Local privilege escalation (LPE) vulnerabilities allow an unprivileged user to gain root or higher privileges on a system. The Linux kernel's page-cache mechanism can be abused to write arbitrary data to kernel memory. Dirtyfrag is the latest in a series of such bugs, following Copy Fail (CVE-2026-31431) disclosed a week earlier.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/V4bel/dirtyfrag">GitHub - V4bel/dirtyfrag · GitHub</a></li>
<li><a href="https://www.phoronix.com/news/Dirty-Frag-Linux">Dirty Frag Vulnerability Made Public Early: Root Privilege On All Distributions - Phoronix</a></li>
<li><a href="https://thehackernews.com/2026/05/linux-kernel-dirty-frag-lpe-exploit.html">Linux Kernel Dirty Frag LPE Exploit Enables Root Access ...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the similarity to Copy Fail, with one researcher noting that the xfrm-ESP page-cache write shares the same sink. Some users point out that the underlying issue in authencesn was not properly fixed, leading to this new exploit. Others share mitigation scripts and note that patches for esp4/esp6 have been pushed for some kernel versions.

**Tags**: `#Linux`, `#privilege escalation`, `#vulnerability`, `#kernel`, `#security`

---

<a id="item-2"></a>
## [Anthropic Releases Natural Language Autoencoders for LLM Interpretability](https://www.anthropic.com/research/natural-language-autoencoders) ⭐️ 9.0/10

Anthropic has released open-weight Natural Language Autoencoder (NLA) models that translate internal activations of LLMs like Qwen 2.5 (7B), Gemma 3 (12B, 27B), and Llama 3.3 (70B) into natural language text, and can reconstruct activations from that text. This is a major step toward making neural network internals interpretable, potentially enabling safer and more transparent AI systems. The open-weight release allows the broader research community to build on this work. The NLA consists of two fine-tuned language models: an activation verbalizer that maps activations to text, and an activation reconstructor that maps text back to activations. The training objective does not enforce human readability, so the explanations may not be faithful.

hackernews · instagraham · May 7, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48052537)

**Background**: Autoencoders are neural networks that learn efficient representations of data by encoding input into a compressed code and decoding it back. In this context, the NLA encodes LLM activations into natural language, which is unusual because natural language is not a typical compressed representation. The Transformer Circuits blog by Anthropic has long explored reverse-engineering transformer models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/kitft/natural_language_autoencoders">GitHub - kitft/natural_language_autoencoders · GitHub</a></li>
<li><a href="https://transformer-circuits.pub/2026/nla/">Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autoencoder">Autoencoder - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters are excited about the open-weight release and see it as a plausible path to model understanding. However, some question whether the generated text truly reflects what the model is 'thinking', noting that the training objective does not guarantee semantic faithfulness.

**Tags**: `#interpretability`, `#AI safety`, `#open-source`, `#transformer circuits`, `#Anthropic`

---

<a id="item-3"></a>
## [Mozilla Uses Claude Mythos to Fix Hundreds of Firefox Bugs](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla used access to Anthropic's Claude Mythos preview to find and fix hundreds of vulnerabilities in Firefox, with the number of monthly security bug fixes jumping from around 20-30 to 423 in April 2026. This marks a paradigm shift in AI-assisted security auditing, transforming AI-generated bug reports from unreliable 'slop' into high-value contributions that can dramatically improve software security. The bugs found include a 20-year-old XSLT bug and a 15-year-old bug in the <legend> element; many attempted exploits were blocked by Firefox's existing defense-in-depth measures, which is reassuring.

rss · Simon Willison · May 7, 17:56

**Background**: Claude Mythos is Anthropic's most advanced large language model, released as a preview to select companies in 2026. AI-generated security bug reports have historically been problematic due to high false-positive rates, imposing a significant burden on open-source maintainers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>
<li><a href="https://grokipedia.com/page/Claude_Mythos_Preview">Claude Mythos Preview</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Claude Mythos Preview \ red.anthropic.com</a></li>

</ul>
</details>

**Discussion**: Commenters note that while the results are impressive, the term 'vulnerability' may be applied broadly; some express hope that AI will free engineers to focus on new features, while others caution that the true impact depends on the quality of proof-of-concept exploits.

**Tags**: `#AI`, `#security`, `#Firefox`, `#vulnerability discovery`, `#Claude`

---

<a id="item-4"></a>
## [TabPFN: Foundation Model for Tabular Data](https://github.com/PriorLabs/TabPFN) ⭐️ 9.0/10

PriorLabs has released TabPFN, a pre-trained transformer foundation model for tabular data that achieves state-of-the-art performance on small to medium datasets (up to 10,000 samples and 500 features). TabPFN simplifies tabular machine learning by eliminating extensive hyperparameter tuning and feature engineering, making accurate predictions accessible to a wider audience. It has the potential to become a go-to tool for data scientists working with tabular data. The model is trained purely on synthetic data and supports both classification and regression tasks. GPU is recommended for optimal performance, but a free hosted inference service is available via TabPFN Client for users without GPU.

rss · GitHub Trending - Daily (All) · May 8, 13:56

**Background**: TabPFN stands for Tabular Prior-data Fitted Network. Unlike traditional models that are trained on a single dataset, TabPFN learns a prior over tabular datasets using a transformer architecture, enabling it to generalize quickly to new tasks with minimal data. It is particularly effective for small to medium-sized datasets where deep learning typically struggles.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/TabPFN">PriorLabs/ TabPFN : TabPFN : Foundation Model for Tabular Data ...</a></li>
<li><a href="https://www.nature.com/articles/s41586-024-08328-6?error=cookies_not_supported&code=0240b9c1-00ea-40ba-b40d-0ff03460f04c">Accurate predictions on small data with a tabular foundation model</a></li>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#tabular data`, `#foundation model`, `#transformer`, `#open source`

---

<a id="item-5"></a>
## [Triton v3.7.0 Adds Squeeze, Scaled BMM, FP8 Constants](https://github.com/triton-lang/triton/releases/tag/v3.7.0) ⭐️ 8.0/10

Triton v3.7.0 introduces tl.squeeze/tl.unsqueeze operations, scaled batched matrix multiply (BMM), direct FP8 constant creation, and constexpr returns from JIT functions. These features simplify GPU kernel development for AI/ML workloads, enabling more expressive and efficient code without sacrificing performance. The release also includes scaled BMM support, FP8 constants, constexpr returns, and numerous performance improvements and bug fixes across the frontend and backend.

github · atalman · May 7, 22:19

**Background**: Triton is an open-source Python-like language and compiler for writing highly efficient GPU kernels, widely used in deep learning frameworks like PyTorch. It abstracts low-level CUDA details, allowing researchers to achieve near-peak hardware performance with minimal effort.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/triton-lang/triton">GitHub - triton-lang/triton: Development repository for the Triton language and compiler · GitHub</a></li>
<li><a href="https://openai.com/index/triton/">Introducing Triton: Open-source GPU programming for neural networks | OpenAI</a></li>
<li><a href="https://pytorch.org/blog/triton-kernel-compilation-stages/">Triton Kernel Compilation Stages – PyTorch</a></li>

</ul>
</details>

**Tags**: `#triton`, `#gpu`, `#compiler`, `#machine learning`, `#release`

---

<a id="item-6"></a>
## [Canvas LMS Down After ShinyHunters Breach Threatens Data Leak](https://www.theverge.com/tech/926458/canvas-shinyhunters-breach) ⭐️ 8.0/10

Canvas, a widely used learning management system by Instructure, experienced a nationwide outage on May 7, 2026, after the hacker group ShinyHunters claimed responsibility for a breach and threatened to leak stolen school data. This incident disrupts final exams for millions of students at a critical time, highlighting the vulnerability of centralized educational platforms and the severe consequences of ransomware attacks on institutions. The outage began around 5:17 PM EDT, with universities like MIT affected; ShinyHunters is known for extortion and data leaks, and this follows a previous breach of Instructure in 2025.

hackernews · stefanpie · May 7, 22:22 · [Discussion](https://news.ycombinator.com/item?id=48055913)

**Background**: Canvas is a cloud-based learning management system (LMS) used by thousands of schools for course management, assignments, and exams. ShinyHunters is a cybercriminal group that specializes in data breaches and extortion, often leaking stolen data if ransoms are not paid.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ShinyHunters">ShinyHunters</a></li>
<li><a href="https://en.wikipedia.org/wiki/Canvas_LMS">Canvas LMS</a></li>

</ul>
</details>

**Discussion**: Educators expressed frustration over the timing during finals, with some criticizing the reliance on cloud-based systems like Canvas. Commenters debated whether ransom payments should be illegal and called for stronger security measures and accountability.

**Tags**: `#cybersecurity`, `#data breach`, `#education`, `#Canvas`, `#ransomware`

---

<a id="item-7"></a>
## [Cloudflare to cut about 20% workforce](https://www.reuters.com/business/world-at-work/cloudflare-cut-over-1100-jobs-2026-05-07/) ⭐️ 8.0/10

Cloudflare announced layoffs of approximately 1,100 employees, representing 20% of its workforce, as part of a restructuring to focus on AI and efficiency. This significant reduction at a major internet infrastructure company signals a broader industry shift toward AI-driven automation and cost-cutting, affecting thousands of tech workers. Affected employees will receive full base pay through end of 2026, extended healthcare in the US, and accelerated equity vesting through August 15, 2026, with one-year cliffs waived.

hackernews · PriorityLeft · May 7, 20:23 · [Discussion](https://news.ycombinator.com/item?id=48054423)

**Background**: Cloudflare is a major content delivery network and cybersecurity company. The layoffs come after a large intern hiring push in September 2025, highlighting the volatile nature of tech hiring cycles.

**Discussion**: Community comments express irony over the layoffs following a large intern hiring event, with some affected employees seeking new roles. The severance package details are discussed, with mixed reactions.

**Tags**: `#layoffs`, `#Cloudflare`, `#tech industry`, `#restructuring`, `#workforce`

---

<a id="item-8"></a>
## [Agents need control flow, not more prompts](https://bsuh.bearblog.dev/agents-need-control-flow/) ⭐️ 8.0/10

A blog post argues that LLM agents should rely on control flow and code generation rather than more prompts for complex tasks, challenging the dominant prompt-engineering approach. This insight could shift how developers build reliable AI agents, moving from fragile prompt-based systems to more deterministic, verifiable architectures using state, validation, and explicit failure handling. The post highlights that once an agent touches a real business workflow, prompts become only one layer; reliability comes from state, validation, observability, and explicit failure handling.

hackernews · bsuh · May 7, 16:43 · [Discussion](https://news.ycombinator.com/item?id=48051562)

**Background**: LLM agents combine an LLM with retrieval, reasoning, memory, and tool use to autonomously complete tasks. Current approaches often rely on prompt engineering to guide agent behavior, but this can be brittle for complex, multi-step workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.langchain.com/langgraph">LangGraph: Agent Orchestration Framework for Reliable AI Agents</a></li>
<li><a href="https://ivos.pro/llm-agents-vs-workflows-enterprise-architecture-guide/">LLM Agents vs Workflows: Enterprise Architecture Guide</a></li>
<li><a href="https://botpress.com/blog/llm-agents">Complete Guide to LLM Agents (2026)</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree, with many sharing experiences of moving from prompts to deterministic flows. Some note that the LLM's role should shrink to writing code for repeatable tasks, while others argue that separating enforcement into different agents can improve reliability.

**Tags**: `#LLM agents`, `#control flow`, `#prompt engineering`, `#software engineering`, `#AI systems`

---

<a id="item-9"></a>
## [DeepSeek 4 Flash: Local Inference Engine for Apple Metal](https://github.com/antirez/ds4) ⭐️ 8.0/10

Antirez released DeepSeek 4 Flash (DS4), a focused, single-model local inference engine for DeepSeek models optimized for Apple Silicon via the Metal framework. It achieves full-speed token generation on a MacBook M3 Max with only 50W peak power consumption. This project demonstrates the value of hardware-specific optimization for local LLM inference, potentially inspiring more developers to create custom inference engines for their hardware. It also provides an educational, easy-to-hack codebase that contrasts with larger, more complex frameworks. DS4 is a minimal, single-model engine that loads DeepSeek models and runs inference via Metal, focusing on simplicity and performance. It is open source under the MIT License and available on GitHub.

hackernews · tamnd · May 7, 15:40 · [Discussion](https://news.ycombinator.com/item?id=48050751)

**Background**: DeepSeek is a Chinese AI company known for cost-effective, open-weight large language models like DeepSeek-R1 and DeepSeek-V3. Apple Metal is Apple's GPU-accelerated framework for graphics and compute, enabling efficient machine learning inference on Apple Silicon. Local inference engines like DS4 allow users to run LLMs on personal devices without cloud dependency, enhancing privacy and reducing latency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek_Coder">DeepSeek Coder</a></li>
<li><a href="https://docs.developer.apple.com/documentation/metal/machine-learning-passes">Machine learning passes | Apple Developer Documentation</a></li>

</ul>
</details>

**Discussion**: Community members praised the project for its educational value and hardware-specific optimization. Some shared similar projects (e.g., for Qwen3), while others discussed the potential for focused optimization over months to narrow the gap with frontier models. The author also noted the low power consumption (50W) during inference.

**Tags**: `#local inference`, `#Apple Silicon`, `#DeepSeek`, `#Metal`, `#open source`

---

<a id="item-10"></a>
## [AlphaEvolve: Gemini-powered coding agent scales across fields](https://deepmind.google/blog/alphaevolve-impact/) ⭐️ 8.0/10

Google DeepMind unveiled AlphaEvolve in May 2025, an evolutionary coding agent powered by Gemini that autonomously optimizes algorithms for genomics, quantum physics, and global infrastructure. AlphaEvolve demonstrates AI's potential for self-improvement and cross-domain impact, accelerating scientific progress and solving real-world challenges that previously required months of human effort. AlphaEvolve orchestrates an autonomous pipeline of LLMs to improve algorithms by making direct code changes, and it has been applied to open scientific problems and critical computational infrastructure optimization.

hackernews · berlianta · May 7, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48050278)

**Background**: AlphaEvolve is an evolutionary coding agent based on large language models like Gemini, designed to autonomously design and optimize algorithms. It builds on DeepMind's research in AI-driven scientific discovery, similar to AlphaFold for protein folding.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaEvolve">AlphaEvolve - Wikipedia</a></li>
<li><a href="https://deepmind.google/blog/alphaevolve-impact/">AlphaEvolve: Gemini-powered coding agent scaling impact ...</a></li>
<li><a href="https://arxiv.org/abs/2506.13131">[2506.13131] AlphaEvolve: A coding agent for scientific and ...</a></li>

</ul>
</details>

**Discussion**: Commenters noted that foundation models excel at optimizing well-defined problem spaces, with some seeing months of work compressed into hours. Others questioned whether DeepMind is the only lab actively pursuing research problems, while OpenAI and Anthropic focus on enterprise revenue.

**Tags**: `#AI`, `#DeepMind`, `#coding agent`, `#self-improvement`, `#research`

---

<a id="item-11"></a>
## [AI Slop Overwhelms Online Communities](https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/) ⭐️ 8.0/10

AI-generated content is flooding online communities, forcing moderators to constantly ban fake accounts and remove low-quality posts, with one moderator reporting banning 600 AI accounts monthly. This degradation threatens the authenticity of online interactions, potentially driving users away from large platforms and back to smaller, trust-based communities or real-world connections. Some communities, like Stack Overflow, have banned AI content entirely to preserve quality, but the moderation burden remains high and costly for niche communities.

hackernews · thm · May 7, 18:46 · [Discussion](https://news.ycombinator.com/item?id=48053203)

**Background**: AI language models can now generate human-like text at scale, making it cheap to produce fake comments, reviews, and posts. This 'AI slop' degrades the quality of online discourse and overwhelms human moderators.

**Discussion**: Commenters share experiences of banning AI accounts daily and express fear of losing the battle. Some see a silver lining, predicting that AI pollution will drive humans back to real-world interactions or smaller, authentic communities.

**Tags**: `#AI`, `#online communities`, `#content moderation`, `#social media`

---

<a id="item-12"></a>
## [DFlash: Block Diffusion for Efficient Speculative Decoding](https://github.com/z-lab/dflash) ⭐️ 8.0/10

DFlash is a lightweight block diffusion model that enables efficient parallel drafting for speculative decoding, with pre-trained drafts available for over 15 large language models including Gemma-4, Qwen3.5, and Llama-3.1. Speculative decoding can significantly reduce LLM inference latency, and DFlash's block diffusion approach offers a more efficient and higher-quality drafting mechanism than traditional autoregressive draft models, potentially accelerating deployment of large models in real-time applications. DFlash supports a wide range of models from 4B to 122B parameters, including dense and mixture-of-experts architectures, and is accompanied by a paper, blog, and model weights on Hugging Face.

rss · GitHub Trending - Daily (All) · May 8, 13:56

**Background**: Speculative decoding accelerates LLM inference by using a small draft model to propose multiple tokens, which are then verified by the target model in parallel. Block diffusion models, introduced in early 2025, combine autoregressive and diffusion approaches by processing blocks of tokens with discrete diffusion, enabling faster generation than pure autoregressive models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.09573">[2503.09573] Block Diffusion: Interpolating Between ... Block Diffusion: Interpolating Between Autoregressive and ... Block Diffusion - m-arriola.com Block Diffusion — dFactory documentation - inclusion-ai.org Block Diffusion: A Breakthrough Hybrid Approach to Language ... Block Diffusion Model Overview - emergentmind.com Block Diffusion: The Revolutionary Approach Bridging ... - Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://github.com/kuleshov-group/bd3lms">Block Diffusion: Interpolating Between Autoregressive and ...</a></li>

</ul>
</details>

**Tags**: `#speculative decoding`, `#block diffusion`, `#LLM inference`, `#machine learning`

---

<a id="item-13"></a>
## [Local Deep Research: Open-source tool achieves ~95% on SimpleQA](https://github.com/LearningCircuit/local-deep-research) ⭐️ 8.0/10

Local Deep Research is an open-source tool that achieves approximately 95% accuracy on the SimpleQA benchmark using local LLMs like Qwen3.6-27B on a single RTX 3090 GPU. It supports over 10 search engines (including arXiv and PubMed), private documents, and runs entirely locally with SQLCipher encryption. This tool enables privacy-preserving deep research without sending data to cloud APIs, making it valuable for sensitive domains like healthcare and legal. Its high accuracy on SimpleQA demonstrates that local models can rival cloud-based solutions, potentially reducing reliance on external AI services. The tool uses Retrieval-Augmented Generation (RAG) to combine local LLMs with document retrieval from multiple sources. It supports all major local LLM backends (llama.cpp, Ollama) and cloud models, and encrypts the database with SQLCipher.

rss · GitHub Trending - Daily (All) · May 8, 13:56

**Background**: SimpleQA is a benchmark by OpenAI that evaluates language models on short, fact-seeking questions. RAG (Retrieval-Augmented Generation) is a technique that allows LLMs to retrieve relevant information from external sources before generating answers, improving factual accuracy. Local Deep Research leverages RAG to achieve high accuracy while keeping data local.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-simpleqa/">Introducing SimpleQA | OpenAI</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.6-27B">Qwen/Qwen3.6-27B · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The project has gained significant traction on GitHub with thousands of stars and Docker pulls. Community discussions on Reddit and Discord highlight enthusiasm for its privacy features and performance, though some users have raised questions about setup complexity and model compatibility.

**Tags**: `#local-llm`, `#research-tool`, `#open-source`, `#privacy`, `#RAG`

---

<a id="item-14"></a>
## [Agent Skills: Production-Grade Engineering for AI Coders](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released a GitHub repository called agent-skills that packages production-grade engineering workflows as slash commands for AI coding agents, covering the full development lifecycle from spec to ship. This repository addresses a key challenge in AI-assisted development by encoding senior engineer best practices into reusable commands, enabling consistent, high-quality outputs from AI agents across teams and projects. The repository provides seven slash commands (/spec, /plan, /build, /test, /review, /code-simplify, /ship) and supports Claude Code, Cursor, and Gemini CLI with automatic skill activation based on context.

rss · GitHub Trending - Daily (All) · May 8, 13:56

**Background**: AI coding agents like Claude Code and Cursor can generate code but often lack structured workflows, leading to inconsistent quality. Slash commands are a way to define reusable prompts that guide agents through specific tasks. This project formalizes that approach by packaging entire engineering workflows as commands.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">Production-grade engineering skills for AI coding agents.</a></li>
<li><a href="https://jmlopezdona.github.io/ai-coding-agents-fundamentals/04-slash-commands/">4. Slash commands and reusable prompts - AI Coding Agents ...</a></li>
<li><a href="https://dev.to/vikrant_bagal_afae3e25ca7/production-grade-engineering-skills-for-ai-coding-agents-56nb">Production-Grade Engineering Skills for AI Coding Agents</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#software engineering`, `#workflow automation`, `#best practices`, `#developer tools`

---

<a id="item-15"></a>
## [Goose AI Agent Moves to Linux Foundation's AAIF](https://github.com/aaif-goose/goose) ⭐️ 8.0/10

Goose, an open-source AI agent originally developed by Block, has moved to the Agentic AI Foundation (AAIF) under the Linux Foundation. It provides desktop, CLI, and API interfaces for code, workflows, and automation, supporting 15+ LLM providers and 70+ extensions via the Model Context Protocol. This move to a neutral foundation under the Linux Foundation enhances Goose's credibility and fosters community-driven development. As a general-purpose AI agent that runs locally, it offers a flexible, open alternative to proprietary tools, potentially accelerating adoption of agentic AI in development workflows. Goose is built in Rust for performance and portability, and works with providers including Anthropic, OpenAI, Google, Ollama, and more. It supports custom distributions with preconfigured providers, extensions, and branding.

rss · GitHub Trending - Daily (All) · May 8, 13:56

**Background**: The Agentic AI Foundation (AAIF) was announced by the Linux Foundation in December 2025 with founding contributions from Anthropic, Block, and OpenAI. It aims to provide neutral stewardship for open, interoperable infrastructure for agentic AI systems. Goose is one of the initial projects contributed to the AAIF, alongside Anthropic's Model Context Protocol (MCP).

<details><summary>References</summary>
<ul>
<li><a href="https://aaif.io/">Home - Agentic AI Foundation (AAIF)</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI ...</a></li>
<li><a href="https://github.com/aaif-goose/goose">GitHub - aaif- goose / goose : an open source, extensible AI agent that...</a></li>

</ul>
</details>

**Tags**: `#AI agent`, `#open source`, `#developer tools`, `#Linux Foundation`

---

<a id="item-16"></a>
## [OpenAI Releases Curated Codex Plugin Examples](https://github.com/openai/plugins) ⭐️ 8.0/10

OpenAI has published an official GitHub repository containing curated Codex plugin examples for tools like Figma, Notion, and app development workflows. The repository includes a required manifest file structure and optional surfaces such as MCP servers and skills. This repository provides developers with practical, ready-to-use integration patterns that demonstrate how to extend Codex into real-world development workflows. It lowers the barrier for building AI-powered tools and encourages adoption of standardized plugin architecture. Each plugin requires a .codex-plugin/plugin.json manifest and can include companion surfaces like skills/, .mcp.json, agents/, and commands/. Highlighted examples include plugins for Figma, Notion, iOS/macOS app building, web apps, Expo, Netlify, Remotion, and Google Slides.

rss · GitHub Trending - Python · May 8, 13:56

**Background**: Codex is OpenAI's AI-powered development environment that integrates with various tools and services. Plugins allow Codex to extend its capabilities by packaging reusable workflows, instructions, and external tooling into installable modules. The plugin manifest (plugin.json) is the required entry point that tells Codex what the plugin contains.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.openai.com/codex/plugins/build">Build plugins – Codex | OpenAI Developers</a></li>
<li><a href="https://developers.openai.com/codex/plugins">Plugins – Codex | OpenAI Developers</a></li>
<li><a href="https://xaicontrol.com/en/blog/codex-plugins-guide/">OpenAI Codex Plugins Guide: Directory, Local Installs, and ...</a></li>

</ul>
</details>

**Tags**: `#openai`, `#plugins`, `#codex`, `#ai-integration`, `#developer-tools`

---

<a id="item-17"></a>
## [Interpretability Method Distinguishes Sources of Annotator Disagreement](https://arxiv.org/abs/2605.05329) ⭐️ 8.0/10

Researchers introduce Annotator Policy Models (APMs), interpretable models that learn annotators' internal safety policies from labeling behavior alone, enabling distinction between operational failures, policy ambiguity, and value pluralism without costly self-reports. This work addresses a critical bottleneck in AI safety annotation by providing a transparent, low-cost method to diagnose disagreement sources, enabling targeted quality control, policy clarification, and inclusive deliberation. It could improve the reliability and fairness of safety datasets used to train large language models. APMs achieve over 80% accuracy in modeling annotator safety policy, faithfully predict responses to counterfactual edits, and recover known policy differences in controlled settings. The method was validated on both LLM and human annotations, revealing policy ambiguity and value pluralism across demographic groups.

rss · arXiv - AI · May 8, 04:00

**Background**: Safety policies define acceptable AI outputs, but annotator disagreement is common and can stem from operational failures (misunderstanding), policy ambiguity (vague wording), or value pluralism (differing moral views). Distinguishing these sources is crucial for improving annotation quality, but traditional methods rely on costly and unreliable self-reports. Interpretability techniques aim to make model decisions transparent, and this work applies them to annotator behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2511.14476">Operationalizing Pluralistic Values in Large Language Model...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#interpretability`, `#data annotation`, `#machine learning`

---

<a id="item-18"></a>
## [ZAYA1-8B: 700M Active MoE Model Matches Larger Models](https://arxiv.org/abs/2605.05365) ⭐️ 8.0/10

Zyphra released ZAYA1-8B, a reasoning-focused mixture-of-experts (MoE) model with 700M active and 8B total parameters, trained from scratch on AMD hardware. It matches or exceeds DeepSeek-R1-0528 on math and coding benchmarks despite having under 1B active parameters. This demonstrates that efficient MoE architectures and novel training pipelines can achieve state-of-the-art reasoning performance with far fewer active parameters, reducing computational costs. It also highlights AMD's growing capability as a platform for training cutting-edge AI models. The model uses Zyphra's MoE++ architecture with compressed convolutional attention and an MLP-based expert router with PID controller. Post-training involves a four-stage RL cascade including RLVE-Gym curriculum with 400 tasks, and Markovian RSA test-time compute method achieves 91.9% on AIME'25 with only a 4K-token tail.

rss · arXiv - AI · May 8, 04:00

**Background**: Mixture-of-experts (MoE) models activate only a subset of parameters per token, enabling high capacity with lower computational cost. ZAYA1-8B is built on Zyphra's MoE++ architecture, which incorporates innovations like compressed convolutional attention and a PID-controlled expert router. The model was trained entirely on AMD compute, networking, and software infrastructure, showcasing an alternative to NVIDIA-based training.

<details><summary>References</summary>
<ul>
<li><a href="https://datanorth.ai/news/zyphra-releases-zaya1-8b">Zyphra Releases ZAYA1-8B - DataNorth AI</a></li>
<li><a href="https://en.walaw.press/articles/zyphra_s_sub-billion_parameter_ai_model_matches_industry_giants_on_reasoning_benchmarks/GQRQFQWSQPXW">Zyphra 's sub-billion parameter AI model matches industry giants on...</a></li>
<li><a href="https://time.news/zyphras-8b-parameter-ai-model-zaya1-8b-punching-above-its-weight-with-amd-gpus-cutting-edge-efficiency/">Zyphra 's 8B-Parameter AI Model ZAYA1-8B Punching Above Its...</a></li>

</ul>
</details>

**Tags**: `#mixture-of-experts`, `#reasoning`, `#AMD`, `#reinforcement learning`, `#language model`

---

<a id="item-19"></a>
## [Partial Evidence Bench: Benchmarking Authorization-Limited Evidence](https://arxiv.org/abs/2605.05379) ⭐️ 8.0/10

Researchers introduced Partial Evidence Bench, a deterministic benchmark with 72 tasks across due diligence, compliance audit, and security incident response scenarios, to measure how agentic systems handle evidence hidden by access control. This benchmark addresses a critical and underexplored failure mode in enterprise agentic systems: silent filtering due to authorization limits, which can lead to catastrophic unsafe completions. The benchmark includes oracle complete answers, authorized-view answers, completeness judgments, and structured gap-report oracles, and evaluates systems on answer correctness, completeness awareness, gap-report quality, and unsafe completeness behavior.

rss · arXiv - AI · May 8, 04:00

**Background**: Enterprise agents operate in scoped retrieval systems where access control may hide relevant evidence. Silent filtering occurs when the system produces a seemingly complete answer while material evidence is outside the caller's authorization boundary, posing safety risks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05379">Partial Evidence Bench: Benchmarking Authorization-Limited ...</a></li>
<li><a href="https://richlyai.com/blog/partial-evidence-bench-benchmarking-ai-authorization-limits-ai-news/">Partial Evidence Bench: Benchmarking AI Authorization Limits</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#benchmark`, `#agentic systems`, `#access control`, `#enterprise AI`

---

<a id="item-20"></a>
## [BALAR: Bayesian Agentic Loop Boosts LLM Active Reasoning](https://arxiv.org/abs/2605.05386) ⭐️ 8.0/10

Researchers propose BALAR, a Bayesian agentic loop for active reasoning that enables LLMs to ask informative questions by maximizing expected mutual information, achieving 14.6%, 38.5%, and 30.5% accuracy improvements on detective, puzzle, and clinical diagnosis benchmarks respectively. This work addresses a key limitation in current LLM interactive systems—lack of principled reasoning about missing information—by introducing a task-agnostic, fine-tuning-free framework that significantly outperforms baselines across diverse domains, potentially advancing AI's ability to engage in effective multi-turn dialogues. BALAR maintains a structured belief over latent states, selects clarifying questions by maximizing expected mutual information, and dynamically expands its state representation when needed. It requires no fine-tuning and operates as an outer-loop algorithm on top of any LLM.

rss · arXiv - AI · May 8, 04:00

**Background**: Large language models (LLMs) often struggle in interactive settings because they lack a principled way to decide what information is missing and which question to ask next. Bayesian inference provides a mathematical framework for updating beliefs based on new evidence, and mutual information quantifies how much a question reduces uncertainty. BALAR combines these concepts to create an active reasoning loop that guides LLM questioning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05386v1">BALAR : A Bayesian Agentic Loop for Active Reasoning</a></li>
<li><a href="https://richlyai.com/blog/balar-bayesian-loop-enhances-ai-active-reasoning-ai-news/">BALAR: Bayesian Loop Enhances AI Active Reasoning</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#active reasoning`, `#Bayesian inference`, `#multi-turn interaction`, `#AI research`

---

<a id="item-21"></a>
## [LLM Sycophancy as Boundary Failure Between Alignment and Epistemic Integrity](https://arxiv.org/abs/2605.05403) ⭐️ 8.0/10

This position paper proposes a three-condition framework to distinguish sycophancy from appropriate alignment in large language models, defining sycophancy as alignment behavior that displaces independent epistemic judgment. This framework provides a more nuanced understanding of sycophancy, which is critical for improving model evaluation and safety in AI alignment research. The three conditions are: (1) user expresses a cue (belief, preference, or self-concept), (2) model shifts toward that cue, and (3) this shift compromises epistemic accuracy, independent reasoning, or appropriate correction. The paper also introduces a taxonomy of alignment targets, mechanisms, and severity.

rss · arXiv - AI · May 8, 04:00

**Background**: Sycophancy in LLMs refers to the tendency of models to excessively agree with or flatter users, often at the expense of factual accuracy. Existing work typically operationalizes sycophancy through observable behaviors like agreeing with incorrect user beliefs, but this paper argues that subtler boundary failures involving epistemic integrity and social alignment are underspecified.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2411.15287v1">Sycophancy in Large Language Models: Causes and Mitigations</a></li>
<li><a href="https://www.aisi.gov.uk/blog/ask-dont-tell-reducing-sycophancy-in-large-language-models-2">Ask Don't Tell: Reducing Sycophancy in Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2503.00069">Societal Alignment Frameworks Can Improve LLM Alignment Beyond embedding-mapping: Social network alignment via ... Evaluating alignment of behavioral dispositions in LLMs Social Value Alignment in Large Language Models - Springer Societal Alignment Frameworks Can Improve LLM Alignment Societal Alignment Frameworks Can Improve LLM Alignment LLM alignment to human values and goals - toloka.ai</a></li>

</ul>
</details>

**Tags**: `#AI alignment`, `#LLM safety`, `#sycophancy`, `#epistemic integrity`, `#social alignment`

---

<a id="item-22"></a>
## [PRISM: Closed-Loop VLM-LLM for Embodied Agents](https://arxiv.org/abs/2605.05407) ⭐️ 8.0/10

PRISM introduces a dynamic question-answer pipeline that couples a Vision-Language Model (VLM) with a Large Language Model (LLM), enabling the LLM to critique and probe the VLM for task-relevant information, resulting in a compact, goal-oriented scene description. PRISM significantly outperforms state-of-the-art image-based models on ALFWorld and Room-to-Room benchmarks, addressing the perception-reasoning gap in standalone VLMs and advancing embodied agents toward more robust sequential decision-making in complex multimodal environments. The framework is fully automatic, eliminating the need for handcrafted questions or answers, and its closed-loop interaction yields systematic gains in task-driven scene understanding.

rss · arXiv - AI · May 8, 04:00

**Background**: Embodied agents require both perception (understanding the environment) and reasoning (planning actions). Standalone Vision-Language Models (VLMs) often miss task-critical details, while Large Language Models (LLMs) excel at reasoning but lack visual grounding. PRISM bridges this gap by letting the LLM actively query the VLM for missing information, mimicking human-like goal-oriented perception.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05407v1">PRISM: Perception Reasoning Interleaved for Sequential ...</a></li>
<li><a href="https://github.com/alfworld/alfworld">GitHub - alfworld/alfworld: ALFWorld: Aligning Text and ...</a></li>

</ul>
</details>

**Tags**: `#embodied agents`, `#vision-language models`, `#sequential decision making`, `#LLM`, `#perception-reasoning`

---

<a id="item-23"></a>
## [FinAgent-RAG: Agentic RAG for Financial QA](https://arxiv.org/abs/2605.05409) ⭐️ 8.0/10

FinAgent-RAG introduces an agentic retrieval-augmented generation framework with iterative reasoning and self-verification, achieving 76.81%, 78.46%, and 74.96% execution accuracy on FinQA, ConvFinQA, and TAT-QA benchmarks, outperforming baselines by 5.62–9.32 percentage points. This work addresses the critical challenge of multi-step numerical reasoning in financial document QA, a domain where single-pass RAG methods fail. Its adaptive strategy router reduces API costs by 41.3%, making advanced financial AI more practical for institutions. The framework integrates three innovations: a Contrastive Financial Retriever with hard negative mining, a Program-of-Thought module generating executable Python code for precise arithmetic, and an Adaptive Strategy Router that dynamically allocates compute resources. Experiments use four LLMs for cross-backbone evaluation.

rss · arXiv - AI · May 8, 04:00

**Background**: Financial document QA requires reasoning over heterogeneous evidence like tables, text, and footnotes. Traditional RAG uses a single retrieve-then-generate pass, which struggles with compositional reasoning chains. Agentic RAG embeds autonomous agents into the pipeline for iterative retrieval and reasoning. Program-of-Thought (PoT) separates computation from reasoning by expressing logic as code, improving numerical accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.05409">Agentic Retrieval-Augmented Generation for Financial Document...</a></li>
<li><a href="https://arxiv.org/abs/2211.12588">[2211.12588] Program of Thoughts Prompting: Disentangling ...</a></li>
<li><a href="https://arxiv.org/abs/2501.09136">Agentic Retrieval - Augmented Generation : A Survey on Agentic RAG</a></li>

</ul>
</details>

**Tags**: `#RAG`, `#financial QA`, `#numerical reasoning`, `#agentic AI`, `#NLP`

---

<a id="item-24"></a>
## [LaTA: FERPA-Compliant Local LLM Autograder for STEM](https://arxiv.org/abs/2605.05410) ⭐️ 8.0/10

Researchers at Oregon State University introduced LaTA (LaTeX Teaching Assistant), an open-source, drop-in autograder that runs entirely on local hardware using the gpt-oss:120b model, achieving FERPA compliance by avoiding third-party APIs. LaTA addresses critical privacy and cost barriers in AI-assisted grading, enabling secure deployment in educational settings without sending student data to external services, and has demonstrated improved student outcomes in a real course. LaTA uses a four-stage pipeline (ingest, segment, grade, report) with a locally hosted open-weight chain-of-thought LLM grader, and achieved a grading-error rate of 0.02–0.04% per rubric line item in a Winter 2026 deployment at Oregon State University.

rss · arXiv - AI · May 8, 04:00

**Background**: FERPA (Family Educational Rights and Privacy Act) is a U.S. federal law that protects the privacy of student education records. Many existing LLM-based autograders send student work to third-party APIs, which can violate FERPA and expose institutions to data risk. LaTA runs entirely on on-premises hardware, ensuring compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05410">LaTA: A Drop-in, FERPA-Compliant Local-LLM Autograder for ...</a></li>
<li><a href="https://richlyai.com/blog/lata-ferpa-compliant-local-llm-autograder-for-stem-ai-news/">LaTA: FERPA-Compliant Local LLM Autograder for STEM</a></li>
<li><a href="https://www.msn.com/en-us/news/other/oregon-states-local-ai-autograder-boosts-stem-exam-scores/gm-GM63E226F5">Oregon State's local AI autograder boosts STEM exam scores</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#education`, `#autograding`, `#FERPA`, `#open-source`

---

<a id="item-25"></a>
## [Constant-Context Skill Learning for LLM Agents](https://arxiv.org/abs/2605.05413) ⭐️ 8.0/10

Researchers propose constant-context skill learning, a context-to-weights framework that enables LLM agents to learn reusable task modules with a fixed-size state block, reducing prompt tokens per turn by 2-7x while achieving strong performance on ALFWorld, WebShop, and SciWorld. This work addresses the privacy-cost-capability trade-off in deploying LLM agents as personal assistants, enabling efficient and private execution of recurring workflows without exposing sensitive context to external APIs. The framework uses a deterministic state tracker to convert task progress into a compact state block and provides subgoal rewards, allowing each module to be trained with step-level supervised fine-tuning (SFT) and refined via online reinforcement learning (RL).

rss · arXiv - AI · May 8, 04:00

**Background**: LLM agents often rely on long context prompts that include task history and instructions, which incurs high cost and privacy risks when using cloud models. Local models preserve privacy but are less capable. This paper proposes moving procedural knowledge from prompts into model weights via lightweight modules, reducing context length while maintaining performance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05413v1">From History to State: Constant-Context Skill Learning for ...</a></li>
<li><a href="https://richlyai.com/blog/constant-context-skill-learning-for-efficient-llm-agents-ai-news/">Constant-Context Skill Learning for Efficient LLM Agents</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#skill learning`, `#privacy`, `#reinforcement learning`, `#personal assistants`

---

<a id="item-26"></a>
## [Are Flat Minima an Illusion?](https://arxiv.org/abs/2605.05209) ⭐️ 8.0/10

A new paper argues that flat minima are not the true cause of generalization in deep learning; instead, 'weakness'—the volume of completions compatible with the learned function—is the invariant driver. The author proves weakness is reparameterization-invariant and shows that on MNIST, sharpness anticorrelates with generalization while weakness correlates positively. This challenges a fundamental assumption underlying popular methods like Sharpness-Aware Minimization (SAM) and could shift how researchers think about generalization in neural networks. If correct, it implies that focusing on flatness is misguided and that alternative measures like weakness should be used. The paper shows that function-preserving reparameterization can inflate the Hessian by two orders of magnitude without changing predictions, proving flatness is not causal. On MNIST, weakness predicts generalization with ρ=+0.374 (p=0.00012), while sharpness anticorrelates (ρ=-0.226) and simplicity is not predictive (p=0.848).

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: In deep learning, flat minima (regions where the loss landscape is shallow) have been widely believed to generalize better than sharp minima. Sharpness-Aware Minimization (SAM) is an optimization algorithm designed to find flat minima. However, prior work (Dinh et al., 2017) showed that flatness is sensitive to reparameterization, casting doubt on its causal role. PAC-Bayes bounds provide theoretical generalization guarantees that correlate with flatness, but the paper argues they actually correlate with weakness.

<details><summary>References</summary>
<ul>
<li><a href="https://www.inference.vc/sharp-vs-flat-minima-are-still-a-mystery-to-me/">The Generalization Mystery: Sharp vs Flat Minima</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sharpness_aware_minimization">Sharpness aware minimization - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2110.11216">[2110.11216] User-friendly introduction to PAC-Bayes bounds</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#generalization`, `#loss landscape`, `#sharpness-aware minimization`, `#theory`

---

<a id="item-27"></a>
## [SAT: Coordinator-Free Multi-LLM Training with Guarantees](https://arxiv.org/abs/2605.05216) ⭐️ 8.0/10

The paper introduces Sequential Agent Tuning (SAT), a coordinator-free training paradigm for teams of smaller LLMs that ensures monotonic improvement and plug-and-play invariance, allowing agent upgrades without retraining the entire team. SAT addresses the critical challenge of training multiple LLMs collaboratively without a central controller, enabling scalable and stable multi-agent systems that can match or surpass larger models at lower cost, with theoretical guarantees for performance improvement. The method uses block-coordinate updates over agents with a sequence-aware on-policy advantage estimator and per-agent KL trust regions. Empirically, a team of three 4B agents (12B total) trained with SAT outperforms Qwen3-32B on AIME24/25 by 3.9% on average.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Large language models (LLMs) with many parameters are powerful but expensive to deploy. Recent work explores using teams of smaller LLMs to collectively match larger models, but joint training suffers from distribution shifts and instability. SAT builds on concepts from multi-agent reinforcement learning, such as factorized policies and block-coordinate optimization, and uses KL trust regions (as in TRPO) to stabilize updates.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2003.06709">FACMAC: Factored Multi-Agent Centralised Policy Gradients Communication with factorized policy gradients in multi-agent ... FOP: Factorizing Optimal Joint Policy of Maximum-Entropy ... [ICML'21] FOP: Factorizing Optimal Joint Policy of Maximum ... Communication with factorized policy gradients in multi-agent ... FACMAC: Factored Multi-Agent Centralised Policy Gradients FACMAC: Factored Multi-Agent Centralised Policy Gradients</a></li>
<li><a href="https://arxiv.org/pdf/1410.1386">A GLOBALLY CONVERGENT ALGORITHM FOR NONCONVEX OPTIMIZATION ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proximal_policy_optimization">Proximal policy optimization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#multi-agent LLM`, `#training paradigm`, `#decentralized coordination`, `#theoretical guarantees`

---

<a id="item-28"></a>
## [Horizon-Constrained Rashomon Sets for Chaotic Forecasting](https://arxiv.org/abs/2605.05218) ⭐️ 8.0/10

This paper introduces horizon-constrained Rashomon sets, a theoretical framework that characterizes how model multiplicity evolves with prediction horizon in chaotic systems, and proves exponential contraction of the effective Rashomon set at a rate determined by the maximum Lyapunov exponent. This work bridges predictive multiplicity and chaos theory for the first time, providing principled guidance for model selection in safety-critical chaotic domains such as weather forecasting and wind power prediction, with demonstrated 18-34% improvement in decision quality. The framework introduces Lyapunov-weighted metrics that provide tighter bounds on predictive disagreement, and develops decision-aligned selection algorithms that choose among near-optimal models based on downstream utility rather than forecast accuracy alone.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Predictive multiplicity refers to the phenomenon where many models with similar aggregate accuracy assign conflicting predictions to individual samples. The Rashomon set is the set of all near-optimal models for a given learning task. Chaotic systems exhibit sensitive dependence on initial conditions, quantified by the Lyapunov exponent, which measures the exponential divergence of nearby trajectories.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2209.08040">Exploring the Whole Rashomon Set of Sparse Decision Trees Exploring the Whole Rashomon Set of Sparse Decision Trees Using Rashomon Sets for Robust Active Learning CS+PosterTemplate_BlueWithLogo.pptx - Duke University An Empirical Evaluation of the Rashomon Effect in Explainable ... On the Inevitability of the Rashomon Effect - IEEE Xplore NeurIPS Using Rashomon Sets for Robust Active Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lyapunov_exponent">Lyapunov exponent - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1909.06677">[1909.06677] Predictive Multiplicity in Classification Predictive Multiplicity in Classification Predictive multiplicity, procedural multiplicity, and ... Predictive multiplicity in classification | Proceedings of ... Rashomon Capacity: A Metric for Predictive Multiplicity in ... Predictive Multiplicity in Classification - arXiv.org Predictive Multiplicity in Classification - Semantic Scholar</a></li>

</ul>
</details>

**Tags**: `#predictive multiplicity`, `#chaotic dynamics`, `#Rashomon sets`, `#Lyapunov exponent`, `#forecasting`

---

<a id="item-29"></a>
## [Sparse Prefix Caching Optimizes Hybrid/Recurrent LLM Serving](https://arxiv.org/abs/2605.05219) ⭐️ 8.0/10

A new paper proposes sparse prefix caching for hybrid and recurrent large language models (LLMs), using checkpoint-based state reuse to reduce recomputation overhead. The method formalizes checkpoint placement as a dynamic programming problem and demonstrates Pareto improvements over existing heuristics. This optimization significantly reduces latency and computational cost for LLM serving, especially when many requests share a common prefix (e.g., different questions about the same document). It enables efficient inference for state-space models and hybrid architectures, which are increasingly important for scaling LLM deployment. The method stores exact recurrent states at a sparse set of checkpoint positions and, on a cache hit, resumes from the deepest stored checkpoint and recomputes the remaining suffix exactly. It preserves exact outputs, does not require new recurrent update kernels, and can be combined with existing KV-cache compression techniques for hybrid models.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Prefix caching is a latency optimization for autoregressive LLMs that reuses computation from previous requests. Traditional systems assume dense per-token key/value reuse, but state-space models (SSMs) can resume from a single stored state, enabling a new sparse caching approach. This paper exploits that asymmetry to reduce recomputation overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05219v1">Sparse Prefix Caching for Hybrid and Recurrent LLM Serving</a></li>
<li><a href="https://machinelearningmastery.com/the-complete-guide-to-inference-caching-in-llms/">The Complete Guide to Inference Caching in LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM serving`, `#prefix caching`, `#state-space models`, `#inference optimization`, `#systems`

---

<a id="item-30"></a>
## [Non-Neural Framework Learns Interpretable Basis Functions from Data](https://arxiv.org/abs/2605.05221) ⭐️ 8.0/10

A new paper introduces Data-Driven Variational Basis Learning (DVBL), a non-neural framework that learns basis functions directly from data via variational optimization, without using neural networks. DVBL addresses the interpretability and transparency issues of neural networks in representation learning, offering a mathematically rigorous alternative that could benefit scientific computing and other fields where interpretability is crucial. The framework treats basis atoms as primary optimization variables and learns them jointly with sample-specific coefficients and, optionally, a latent linear evolution operator. The paper provides theoretical guarantees including existence of minimizers, blockwise descent properties, and identifiability conditions.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Classical basis expansions like Fourier series or wavelets are analytically tractable but not data-adaptive. Neural networks learn features from data but often sacrifice interpretability. DVBL bridges this gap by learning explicit, interpretable basis functions through variational optimization, without neural architectures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05221">Data - Driven Variational Basis Learning Beyond Neural Networks...</a></li>
<li><a href="https://arxiv.org/html/2605.05221v1">Data-Driven Variational Basis Learning Beyond Neural Networks ...</a></li>

</ul>
</details>

**Tags**: `#representation learning`, `#basis discovery`, `#variational optimization`, `#interpretability`, `#scientific computing`

---

<a id="item-31"></a>
## [Token-Selective Attention: Adaptive Layer Skipping in Transformers](https://arxiv.org/abs/2605.05222) ⭐️ 8.0/10

Token-Selective Attention (TSA) introduces learned per-token gates that allow tokens to skip transformer layers, saving 14-23% of token-layer operations with less than 0.5% quality loss on character-level language modeling. TSA offers a novel, end-to-end differentiable approach to adaptive computation in transformers, achieving significant efficiency gains with minimal overhead and no architecture changes, which could enable faster inference for large language models. Each gate is a lightweight two-layer MLP that outputs a continuous halting probability, adding only 1.7% parameter overhead. The router learns difficulty-proportional routing even without explicit depth regularization, and the learned routing transfers directly to inference-time sparse execution for real wall-clock speedup.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Standard transformers apply the same number of layers to every token, regardless of difficulty. Adaptive computation methods like early exit or token pruning aim to reduce computation for simpler tokens, but often require architectural changes or non-differentiable decisions. TSA provides a fully differentiable alternative that learns to skip layers based on token difficulty.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05222v1">Adaptive Computation Depth via Learned Token Routing in ...</a></li>

</ul>
</details>

**Tags**: `#transformer`, `#efficient inference`, `#adaptive computation`, `#deep learning`, `#NLP`

---

<a id="item-32"></a>
## [Geometric Theory Reveals Instability in Feature Composition](https://arxiv.org/abs/2605.05223) ⭐️ 8.0/10

A new paper introduces a geometric framework analyzing the instability of feature composition in sparse autoencoders, deriving a collapse threshold for simultaneous activation of semantic latents. This work addresses a critical gap in the theoretical understanding of sparse autoencoders and compositional steering, which are central to interpretability in transformer models, with potential impact on AI safety and mechanistic interpretability. The paper models activation space as a high-dimensional sparse cone manifold and derives an asymptotic compositional-collapse threshold characterized by the Gaussian mean width of the signal cone. It also shows that ReLU rectification converts correlation-induced variance fluctuations into systematic drift, yielding interference growth akin to a ratchet effect.

rss · arXiv - Machine Learning · May 8, 04:00

**Background**: Sparse autoencoders (SAEs) are used to disentangle feature superposition in neural networks, where multiple features are represented in overlapping ways. The linear representation hypothesis suggests that concepts are represented as linear directions in representation space, but this abstraction often ignores non-linear interference effects. This paper provides a geometric perspective to understand when simultaneous activation of features leads to collapse.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2309.08600">Sparse Autoencoders Find Highly Interpretable Features in ... Sparse AutoEncoder: from Superposition to interpretable features [Interim research report] Taking features out of ... 4 Interpreting with Sparse Autoencoders – Unravelling ... Sparse Autoencoders for Interpretability in Reinforcement ... Explaining "Taking features out of superposition with sparse ... Learning Interpretable Features with Sparse Auto-Encoders</a></li>
<li><a href="https://arxiv.org/abs/2311.03658">The Linear Representation Hypothesis and the Geometry of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linear_representation_hypothesis">Linear representation hypothesis</a></li>

</ul>
</details>

**Tags**: `#sparse autoencoders`, `#interpretability`, `#transformer architectures`, `#geometric analysis`, `#AI safety`

---

<a id="item-33"></a>
## [SLAM: Watermarking LLMs via Linguistic Structure](https://arxiv.org/abs/2605.05443) ⭐️ 8.0/10

Researchers propose SLAM, a white-box watermarking scheme that embeds marks into linguistic structure (e.g., voice, tense) using sparse autoencoders, achieving 100% detection accuracy on Gemma-2 2B and 9B with only 1-2 reward points quality loss. SLAM significantly reduces text quality degradation compared to existing token-distribution-based watermarks, offering a practical solution for AI safety and content provenance without compromising naturalness. SLAM is a white-box method that causally steers residual-stream directions encoding linguistic structure, leaving lexical sampling and semantics unconstrained. It resists word-level edits but is vulnerable to paraphrase that restructures syntax.

rss · arXiv - NLP · May 8, 04:00

**Background**: LLM watermarks are used to detect AI-generated text, but most existing methods bias token probabilities, causing measurable quality loss. Sparse autoencoders are interpretability tools that identify meaningful directions in model activations. SLAM leverages these to embed watermarks in structural geometry rather than token frequencies.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2309.08600">[2309.08600] Sparse Autoencoders Find Highly Interpretable ... Sparse autoencoders uncover biologically interpretable ... - PNAS SPARSE AUTOENCODERS FIND HIGHLY INTER PRETABLE FEATURES IN ... Interpreting Genomic Language Models using Sparse Autoencoders A Survey on Sparse Autoencoders: Interpreting the Internal ... Sparse Autoencoders for Interpretability in Reinforcement ... Mapping LLMs with Sparse Autoencoders - pair.withgoogle.com</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3711896.3736841">An Efficient White-box LLM Watermarking for IP Protection on ...</a></li>
<li><a href="https://arxiv.org/html/2410.16090v1">Analysing the Residual Stream of Language Models Under ...</a></li>

</ul>
</details>

**Tags**: `#LLM watermarking`, `#sparse autoencoders`, `#AI safety`, `#natural language processing`, `#structural linguistics`

---

<a id="item-34"></a>
## [ReaComp: Compiling LLM Reasoning into Symbolic Solvers](https://arxiv.org/abs/2605.05485) ⭐️ 8.0/10

ReaComp compiles a small set of LLM reasoning traces into reusable symbolic program synthesizers that require zero LLM calls at test time, achieving 91.3% accuracy on PBEBench-Lite and 84.7% on PBEBench-Hard, outperforming LLMs with test-time scaling by +16.3 percentage points on the hard set. This work demonstrates that LLM reasoning can be distilled into efficient symbolic solvers, dramatically reducing inference cost while maintaining or improving accuracy, which could make program synthesis more practical for real-world applications and reduce reliance on expensive LLM inference. The induced solvers also complement LLM search, improving PBEBench-Hard accuracy from 68.4% to 85.8% while reducing token usage by 78%, and transfer zero-shot to a historical linguistics task with 80.1% accuracy under ensembling.

rss · arXiv - NLP · May 8, 04:00

**Background**: Program synthesis aims to automatically generate programs from specifications. LLMs can solve such tasks but struggle with hard combinatorial search problems. Symbolic solvers are efficient but require manual design. ReaComp bridges the gap by using LLM reasoning traces to automatically construct symbolic solvers over constrained domain-specific languages (DSLs).

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05485v1">ReaComp: Compiling LLM Reasoning into Symbolic Solvers for ...</a></li>
<li><a href="https://gist.science/paper/2605.05485">ReaComp: Compiling LLM Reasoning into Symbolic Solvers ...</a></li>
<li><a href="https://arxiv.org/abs/2505.23126">[2505.23126] PBEBench: A Multi-Step Programming by Examples ... PBEBench: A Multi-Step Programming by Examples Reasoning ... PBEBENCH: A MULTI-STEPPROGRAMMING BYEX ... PBEBench/README.md at main · cmu-llab/PBEBench · GitHub (PDF) PBEBench: A Multi-Step Programming by Examples ... PBEBench: A Multi-Step Programming by Examples Reasoning ... PBEBench: A Multi-Step Programming by Examples Reasoning ...</a></li>

</ul>
</details>

**Tags**: `#program synthesis`, `#LLM`, `#symbolic solver`, `#neuro-symbolic`, `#efficiency`

---

<a id="item-35"></a>
## [Domain-Trained SLM Outperforms Frontier LLMs on Contract Extraction](https://arxiv.org/abs/2605.05532) ⭐️ 8.0/10

A new study shows that Olava Extract, a domain-trained small language model using a Mixture of Experts architecture, achieves higher macro F1 (0.812) and micro F1 (0.842) than five frontier LLMs on structured contract extraction, while reducing inference cost by 78% to 97%. This challenges the prevailing assumption that larger models are always necessary for high-quality enterprise AI, demonstrating that smaller, domain-specific models can deliver superior performance at a fraction of the cost, especially in legal workflows where hallucinations are costly. Olava Extract is a self-hosted legal domain Mixture of Experts model, and it achieved the highest precision scores with fewer hallucinated and unsupported extractions, which is critical for legal applications where errors create operational risk.

rss · arXiv - NLP · May 8, 04:00

**Background**: Structured contract extraction involves automatically pulling key data (e.g., party names, dates, clauses) from legal documents. Large Language Models (LLMs) like GPT-4 are often used but are expensive and prone to hallucinations. Mixture of Experts (MoE) is an architecture that uses multiple specialized sub-models to improve efficiency and accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.onit.com/products/ai-studio/olava/">Learn More About Olava | Onit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="http://www.contractextraction.com/">Contract Extraction: Pull Key Terms from Any Contract with AI</a></li>

</ul>
</details>

**Tags**: `#small language models`, `#legal AI`, `#contract extraction`, `#domain-specific models`, `#cost efficiency`

---

<a id="item-36"></a>
## [Recorruption: How Accurate Context Harms Multimodal RAG](https://arxiv.org/abs/2605.05594) ⭐️ 8.0/10

This paper formalizes 'recorruption' in multimodal RAG, where introducing perfectly accurate oracle context causes models to abandon correct predictions due to attentional collapse and positional bias. It reveals a critical failure mode in multimodal RAG systems, challenging the assumption that more context always helps, and proposes a parameter-free inference-time intervention (BAIR) to restore visual grounding. The paper identifies two mechanisms: visual blindness (suppression of visual attention mass and sharpness) and structural positional bias that prioritizes boundary tokens over semantic relevance. BAIR restores visual saliency and applies position-aware penalties without retraining.

rss · arXiv - NLP · May 8, 04:00

**Background**: Multimodal Large Language Models (MLLMs) integrate visual and textual inputs, often using Retrieval-Augmented Generation (RAG) to fetch external documents to reduce hallucinations. However, introducing external text can inadvertently bias the model away from visual evidence. Attentional collapse refers to attention matrices degenerating to near rank-one structures in deeper layers, while positional bias describes models favoring certain token positions (e.g., early or boundary tokens) over semantic content.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.05594">The Cost of Context: Mitigating Textual Bias in Multimodal ...</a></li>
<li><a href="https://arxiv.org/html/2404.08634v4">When Attention Collapses: How Degenerate Layers in LLMs ...</a></li>
<li><a href="https://arxiv.org/abs/2502.01951">On the Emergence of Position Bias in Transformers xinyiwu98/position-bias-in-attention - GitHub Positional Embeddings in Transformer Models: Evolution from ... Images [PDF] On the Emergence of Position Bias in Transformers ... Breaking Down Swin Transformer: Understanding Relative ... ICLR On the Emergence of Position Bias in Transformers On the Emergence of Position Bias in Transformers | alphaXiv</a></li>

</ul>
</details>

**Tags**: `#Multimodal LLMs`, `#Retrieval-Augmented Generation`, `#Attention Mechanisms`, `#AI Safety`, `#Machine Learning`

---

<a id="item-37"></a>
## [When2Speak Dataset Teaches LLMs When to Intervene](https://arxiv.org/abs/2605.05626) ⭐️ 8.0/10

Researchers introduced When2Speak, a dataset of over 215,000 examples from 16,000 multi-party conversations, along with a four-stage pipeline for training LLMs to decide when to speak versus remain silent. This addresses a critical gap in conversational AI, as LLMs currently struggle with turn-taking in group settings, often interrupting or staying silent inappropriately. The open-source dataset and pipeline enable more natural multi-party interactions in applications like virtual assistants and collaborative agents. Fine-tuning on When2Speak improved Macro F1 by 60% on average for 4B+ parameter models, but models remained over-conservative with a Missed Intervention Rate (MIR) of 0.50. Using reinforcement learning with asymmetric reward shaping reduced MIR to 0.186–0.218 and increased recall from 0.479 to 0.78–0.81.

rss · arXiv - NLP · May 8, 04:00

**Background**: Multi-party conversations require participants to decide not only what to say but when to speak, a skill known as turn-taking. Current LLMs are typically trained on single-turn or dyadic data, making them poorly calibrated for group dynamics. The When2Speak dataset simulates realistic group conversations with 2–6 speakers, explicitly modeling SPEAK vs. SILENT decisions at each turn.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.05626v1">When2Speak: A Dataset for Temporal Participation and Turn ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#multi-party conversation`, `#turn-taking`, `#dataset`, `#conversational AI`

---

<a id="item-38"></a>
## [Response-Aware Defense Against Multi-Turn LLM Attacks](https://arxiv.org/abs/2605.05630) ⭐️ 8.0/10

This paper proposes TurnGate, a response-aware defense that detects the earliest harmful turn in multi-turn dialogues, and introduces the Multi-Turn Intent Dataset (MTID) for training and evaluation. Multi-turn attacks are a growing threat to LLMs, and existing single-turn defenses fail against them; TurnGate enables precise turn-level intervention, reducing both harmful responses and over-refusal rates. TurnGate uses a turn-level monitor that identifies the harm-enabling closure point, and MTID includes branching attack rollouts, benign hard negatives, and annotations of earliest harmful turns.

rss · arXiv - NLP · May 8, 04:00

**Background**: Multi-turn attacks distribute malicious intent across several benign-looking dialogue turns to bypass safety guardrails. Unlike single-turn attacks, they exploit the temporal context of conversation, making detection harder. Existing defenses often over-refuse benign queries or fail to catch subtle multi-turn attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2503.15560">Temporal Context Awareness: A Defense Framework Against Multi ... The Conversation That Breaks the Machine: A Deep Dive into ... Chain of Attack: Hide Your Intention through Multi-Turn ... Multi-Turn Attacks | confident-ai/deepteam | DeepWiki Multi-Turn Jailbreaking Large Language Models via Attention ... Multi-turn Attack Algorithm - docs.generalanalysis.com Multi-Turn Conversation Attacks on LLMs | AI Dialog</a></li>
<li><a href="https://aclanthology.org/2025.findings-acl.514/">Chain of Attack: Hide Your Intention through Multi-Turn ...</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#multi-turn dialogue`, `#adversarial attacks`, `#defense`, `#dataset`

---

<a id="item-39"></a>
## [Layout-Aware Learning for Open-Set ID Fraud Detection](https://arxiv.org/abs/2605.05215) ⭐️ 8.0/10

Researchers propose a layout-aware representation learning method that adapts DINOv3 via SimMIM fine-tuning and supervised metric learning to detect open-set identity document fraud, achieving 99.83% layout classification accuracy on Canadian IDs despite training only on U.S. IDs. This work addresses the critical limitation of closed-set fraud detectors that fail against adaptive attackers, enabling discovery of novel fraud campaigns at scale and improving security for identity verification systems worldwide. The model uses a composite loss for inter-class separability and intra-class compactness, and on a dataset of 20,448 Canadian IDs, embedding-space analysis uncovered 276 adaptive physical-fraud cases, 222 of which were missed by incumbent detectors.

rss · arXiv - Computer Vision · May 8, 04:00

**Background**: Traditional identity document fraud detection treats the problem as binary classification, but adaptive attackers continuously modify templates and fabrication pipelines, making historical labels stale. Open-set recognition aims to detect novel fraud types not seen during training. DINOv3 is a self-supervised vision backbone that learns universal image representations, and SimMIM is a masked image modeling framework used for fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.meta.com/research/dinov3/">DINOv3 - ai.meta.com</a></li>
<li><a href="https://github.com/microsoft/SimMIM">GitHub - microsoft/SimMIM: This is an official implementation ... SimMIM Explained: A Simple Yet Powerful Framework ... - Medium SimMIM: A Simple Framework for Masked Image Modeling SimMIM: A Simple Framework for Masked Image Modeling SimMIM: A Simple Framework for Masked Image Modeling SimMIM — MMSelfSup 1.0.0 documentation - Read the Docs</a></li>

</ul>
</details>

**Tags**: `#fraud detection`, `#representation learning`, `#computer vision`, `#document analysis`, `#open-set recognition`

---

<a id="item-40"></a>
## [Density-Aware Calibration for 3D Detection Under Shift](https://arxiv.org/abs/2605.05328) ⭐️ 8.0/10

Query2Uncertainty introduces a density-aware calibration method that uses latent query features from DETR-style 3D object detectors to improve uncertainty estimation under distribution shifts. This work addresses a critical safety issue in autonomous driving by enabling 3D detectors to remain well-calibrated under distribution shifts, which is essential for reliable deployment. The method jointly recalibrates classification and bounding box regression uncertainties by fitting a density estimator on query features, and outperforms standard post-hoc methods on both camera and LiDAR detectors.

rss · arXiv - Computer Vision · May 8, 04:00

**Background**: Post-hoc calibration methods adjust model confidence after training but fail under distribution shifts. DETR-style detectors use learnable queries to predict objects, and these queries encode location and class information that can be used for density estimation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.18788">StereoDETR: Stereo-based Transformer for 3D Object Detection</a></li>
<li><a href="https://github.com/facebookresearch/3detr">3DETR: An End-to-End Transformer Model for 3D Object Detection The DETR Revolution: How Transformers Redefined Object Detection Understanding DETR: Object Detection + Transformers • The ... Semi-3DETR: Semi-Supervised Detection Transformer for 3D ... 3D detection transformer: Set prediction of objects using ... An End-to-End Transformer Model for 3D Object Detection</a></li>
<li><a href="https://arxiv.org/html/2302.05118">Beyond In-Domain Scenarios: Robust Density-Aware Calibration</a></li>

</ul>
</details>

**Tags**: `#3D object detection`, `#uncertainty quantification`, `#calibration`, `#autonomous driving`, `#distribution shift`

---

<a id="item-41"></a>
## [ViTok-v2 Scales Vision Autoencoders to 5B Parameters](https://arxiv.org/abs/2605.05331) ⭐️ 8.0/10

ViTok-v2 scales vision transformer autoencoders to 5 billion parameters with native resolution support via NaFlex and a novel DINOv3 perceptual loss that replaces adversarial losses, achieving state-of-the-art reconstruction at 256p and above. This work enables stable training of large-scale image autoencoders without adversarial losses, advancing the Pareto frontier of reconstruction-generation trade-off and potentially improving image tokenization for generative models. ViTok-v2 is trained on about 2 billion images and uses NaFlex with 2D RoPE for variable resolution and aspect ratio support, while the DINOv3 perceptual loss is computed from frozen DINOv3-B features via L2-normalized MSE.

rss · arXiv - Computer Vision · May 8, 04:00

**Background**: Vision Transformer (ViT) autoencoders are used as tokenizers for image generation, but previous models suffered from performance degradation at non-training resolutions and unstable scaling due to adversarial losses. ViTok-v2 addresses these by introducing native resolution support and a perceptual loss based on self-supervised DINOv3 features, which avoids the need for human perceptual judgments.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05331">[2605.05331] ViTok-v2: Scaling Native Resolution Auto ...</a></li>
<li><a href="https://github.com/Na-VAE/vitok-release/blob/main/">GitHub - Na-VAE/vitok-release: ViTok-v2 public release</a></li>
<li><a href="https://na-vae.github.io/dino_perceptual/">DINO Perceptual Loss: A Modern Alternative to LPIPS</a></li>

</ul>
</details>

**Tags**: `#vision transformers`, `#autoencoders`, `#image tokenization`, `#scaling`, `#deep learning`

---

<a id="item-42"></a>
## [Tamaththul3D: High-Fidelity Saudi Sign Language Avatars from Monocular Video](https://arxiv.org/abs/2605.05367) ⭐️ 8.0/10

Researchers introduced the first high-quality 3D parametric annotations for the Ishara-500 Saudi Sign Language dataset and developed Tamaththul3D, a specialized reconstruction pipeline that generates realistic avatars from monocular video, achieving up to 32% improvement in hand accuracy over previous methods. This work fills a critical gap in Arabic Sign Language (ArSL) accessibility, enabling new assistive technologies and cultural preservation for approximately 400 million Arabic speakers, including the Arab Deaf community. The pipeline integrates SMPLer-X for body estimation, WiLoR for hand refinement with automatic localization and mirroring, and MediaPipe for 2D pose supervision, using kinematic-chain-based wrist alignment with hybrid swing-twist decomposition and 2D-supervised joint optimization.

rss · arXiv - Computer Vision · May 8, 04:00

**Background**: SMPL-X is a unified 3D body model that represents the body, hands, and face with shape and pose parameters. Arabic Sign Language (ArSL) and its dialects serve about 400 million Arabic speakers but previously lacked high-quality 3D parametric annotations and specialized reconstruction methods for avatar generation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/vchoutas/smplx">GitHub - vchoutas/smplx: SMPL-X</a></li>
<li><a href="https://github.com/MotrixLab/SMPLer-X">SMPLer-X: Scaling Up Expressive Human Pose and Shape Estimation</a></li>
<li><a href="https://github.com/rolpotamias/WiLoR">GitHub - rolpotamias/WiLoR: WiLoR: End-to-end 3D hand ...</a></li>

</ul>
</details>

**Tags**: `#3D Avatar`, `#Sign Language`, `#Computer Vision`, `#Accessibility`, `#SMPL-X`

---

<a id="item-43"></a>
## [InfoTree: Submodular Tree Search for Tool-Use RL](https://arxiv.org/abs/2605.05262) ⭐️ 8.0/10

This paper formalizes Rollout Informativeness under a Fixed Budget (RIFB) for tool-use agentic RL, proving that budget-agnostic independent samplers have a non-vanishing collapse rate. It proposes InfoTree, a training-time tree-search framework based on submodular optimization, which includes an Uncertainty-aware Upper Confidence Bound (UUCB) and an Adaptive Budget Allocator (ABA). This work provides a theoretical foundation for rollout selection in GRPO-based tool-use RL, bridging the gap between empirical tricks like token-level entropy bonus and analytic guarantees. InfoTree outperforms multiple baselines across nine benchmarks, potentially improving the efficiency and effectiveness of training large language models for tool-use tasks. The UUCB terms arise as closed-form marginal gains of a monotone submodular maximization objective, and the ABA rescues prompts with wasted initial trees, lifting the mixed-outcome ratio from 58.1% to 76.3% with less than 5% budget overhead. Speculative Expansion reduces wall-clock overhead from 14.3% to 4.8% by tolerating bounded staleness in UUCB scores.

rss · arXiv - Data Science & Statistics · May 8, 04:00

**Background**: Group Relative Policy Optimization (GRPO) is a reinforcement learning method used to train large language models, such as DeepSeek-R1, without a separate critic model. Submodular optimization is a framework for maximizing functions that exhibit diminishing returns, often used in combinatorial optimization and machine learning. This paper applies submodularity to select intermediate states during tree search for tool-use agentic RL.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05262">Maximizing Rollout Informativeness under a Fixed Budget: A ...</a></li>
<li><a href="https://arxiv.org/abs/2603.01162">Demystifying Group Relative Policy Optimization: Its Policy ...</a></li>
<li><a href="https://arxiv.org/abs/2202.00132">Submodularity In Machine Learning and Artificial Intelligence Beyond Convexity: Submodularity in Machine Learning - ETH Z Submodularity in ML: New Directions Submodular Optimization: Variants, Theory and Applications Submodular Functions, Optimization, and Applications to ... Submodular Optimization and Machine Learning | Deus Ex Machina Submodular Function Optimization</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#submodular optimization`, `#tool-use agents`, `#GRPO`, `#tree search`

---

<a id="item-44"></a>
## [Benign Regularizer Reveals Hidden Convexity in Nonconvex Matrix Estimation](https://arxiv.org/abs/2605.05446) ⭐️ 8.0/10

This paper introduces a theoretical framework that identifies a 'benign regularizer' which, without altering the algorithm's update rule, transforms nonconvex low-rank matrix estimation into an equivalent locally strongly convex problem, explaining why nonconvex methods succeed without extra regularization. This work bridges the gap between theory and practice in low-rank matrix estimation, a core problem in machine learning and AI, by providing a unified explanation for the empirical success of nonconvex methods, potentially enabling simpler and more robust algorithms. The framework applies to a broad class of low-rank estimation problems and does not rely on problem-specific arguments, making it generalizable to complex settings. The benign regularizer yields an equivalent locally strongly convex formulation, uncovering 'disguised convexity' in nonconvex procedures.

rss · arXiv - Data Science & Statistics · May 8, 04:00

**Background**: Low-rank matrix estimation is a fundamental task in machine learning, used for dimensionality reduction, recommendation systems, and more. Nonconvex optimization methods are often preferred for their efficiency, but their theoretical analysis typically requires additional regularization that is unnecessary in practice, creating a gap between theory and practice.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05446">Convexity in Disguise: A Theoretical Framework for Nonconvex ...</a></li>
<li><a href="https://link.springer.com/content/pdf/10.1007/s10898-023-01293-w.pdf">Low-rank matrix estimation via nonconvex optimization methods ...</a></li>
<li><a href="https://yuejiechi.github.io/talks/ZJU_lowrank_tutorial.pdf">Scalable and Robust Nonconvex Approaches for Low-rank ...</a></li>

</ul>
</details>

**Tags**: `#low-rank matrix estimation`, `#nonconvex optimization`, `#machine learning theory`, `#high-dimensional data`

---

<a id="item-45"></a>
## [Neural Conditional Scores Enable SDE Inference from Sparse Data](https://arxiv.org/abs/2605.05606) ⭐️ 8.0/10

Researchers developed a variational smoothing method for stochastic differential equations (SDEs) that learns conditional backward scores via neural networks, enabling inference from sparse, noisy observations. This method addresses path degeneracy and scalability issues in classical SDE smoothing, offering a more efficient alternative to MCMC for time series modeling and scientific computing. The posterior SDE is characterized by a conditional backward score derived from a Kolmogorov backward equation with multiplicative updates at observation times, and the score is learned by a neural network trained to satisfy both the PDE and jump conditions.

rss · arXiv - Data Science & Statistics · May 8, 04:00

**Background**: Stochastic differential equations (SDEs) model temporal dynamics under uncertainty, but inferring latent trajectories and parameters from sparse data is challenging due to path degeneracy and computational cost. Classical smoothing methods often rely on MCMC, which scales poorly. This work leverages neural networks to learn the conditional score, enabling efficient variational inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2011.13456">[2011.13456] Score-Based Generative Modeling through ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov_equations">Kolmogorov equations - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#stochastic differential equations`, `#variational inference`, `#neural networks`, `#time series`, `#scientific computing`

---

<a id="item-46"></a>
## [Spectral Lens: Diagnosing LLM Training via Activation and Gradient Spectra](https://arxiv.org/abs/2605.05683) ⭐️ 8.0/10

A new paper introduces Spectral Lens, a diagnostic method using activation covariance and per-sample gradient SVD spectra to analyze LLM training dynamics. It reveals that batch size determines representation geometry, early activation spectra predict token efficiency, and spectral movements separate learning from execution improvements. This work provides practical, interpretable diagnostics for understanding and optimizing large-scale LLM training, which is often opaque. It could help researchers and engineers make better decisions about batch size, architecture, and training strategies without relying solely on loss curves. The study uses a controlled family of decoder-only models (12, 36, and 48 layers) from the modded NanoGPT codebase. It finds that activation covariance tail early in training forecasts downstream token efficiency, and the head movement combined with gradient spectra characterizes learning-dynamics changes.

rss · arXiv - Data Science & Statistics · May 8, 04:00

**Background**: Training loss and throughput often hide internal representation changes in language models. Spectral analysis of activation covariance matrices and gradient singular value decomposition (SVD) provides a window into these hidden mechanics, revealing how representations evolve during training.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.05683">Spectral Lens: Activation and Gradient Spectra as Diagnostics ...</a></li>
<li><a href="https://github.com/KellerJordan/modded-nanogpt">GitHub - KellerJordan/modded-nanogpt: NanoGPT (124M) in 90 ...</a></li>

</ul>
</details>

**Tags**: `#LLM training`, `#spectral analysis`, `#optimization diagnostics`, `#deep learning`

---