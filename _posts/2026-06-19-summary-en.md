---
layout: default
title: "Horizon Summary: 2026-06-19 (EN)"
date: 2026-06-19
lang: en
---

> From 105 items, 40 important content pieces were selected

---

1. [Roboflow's RF-DETR Achieves SOTA Real-Time Detection](#item-1) ⭐️ 9.0/10
2. [ITNet Unifies CNNs, RNNs, and Transformers](#item-2) ⭐️ 9.0/10
3. [DeepSeek-V4 Preview: 1.6T MoE Models with Million-Token Context](#item-3) ⭐️ 9.0/10
4. [ATProto Has No Instances: A Protocol Analogy](#item-4) ⭐️ 8.0/10
5. [Project Valhalla Arrives in JDK 28 After a Decade](#item-5) ⭐️ 8.0/10
6. [EFF Calls for Free Public Court Records](#item-6) ⭐️ 8.0/10
7. [Amateur Uses AI to Propose Decipherment of Linear A](#item-7) ⭐️ 8.0/10
8. [Google Releases TimesFM 2.5 for Time-Series Forecasting](#item-8) ⭐️ 8.0/10
9. [Zhipu AI Releases GLM-5 Series with 1M Context](#item-9) ⭐️ 8.0/10
10. [Codebase-Memory-MCP: Sub-ms Code Intelligence with Knowledge Graph](#item-10) ⭐️ 8.0/10
11. [Lightricks Releases LTX-2: Open-Source Audio-Video Model](#item-11) ⭐️ 8.0/10
12. [OpenMontage: First Open-Source Agentic Video Production System](#item-12) ⭐️ 8.0/10
13. [Deontic Policies for Agentic AI Governance](#item-13) ⭐️ 8.0/10
14. [Systematic Analysis of Diffusion Language Models](#item-14) ⭐️ 8.0/10
15. [Hidden Anchors Explain Multi-Agent LLM Deliberation](#item-15) ⭐️ 8.0/10
16. [DeXposure-Claw: Agentic System for DeFi Risk Supervision](#item-16) ⭐️ 8.0/10
17. [LLMs Blind to Their Own Limits on Clinical Data](#item-17) ⭐️ 8.0/10
18. [Emergent Alignment: LLMs Self-Correct Ethics via Introspection](#item-18) ⭐️ 8.0/10
19. [Computational Identifiability: Bridging Theory and Practice](#item-19) ⭐️ 8.0/10
20. [Guard: Multi-Teacher Distillation for Robust Time-Series Forecasting](#item-20) ⭐️ 8.0/10
21. [Self-play RL with 30 min human data beats imitation learning](#item-21) ⭐️ 8.0/10
22. [TreeTracer Visualizes Hidden LLM Bias via Stochastic Paths](#item-22) ⭐️ 8.0/10
23. [LLM Fine-Tuning Gains from Task Alignment, Not Language Transfer](#item-23) ⭐️ 8.0/10
24. [New Error Taxonomy Reveals LLM Limits in Hardware Design](#item-24) ⭐️ 8.0/10
25. [Positional Bias in Diffusion LLMs: Analysis and Mitigation](#item-25) ⭐️ 8.0/10
26. [Causal Attribution Pruning Boosts LLM Reasoning at Low Sparsity](#item-26) ⭐️ 8.0/10
27. [Survey Indexes 120 Sign-Language Datasets Across 35 Languages](#item-27) ⭐️ 8.0/10
28. [Self-Function Vectors Quantify Aleatoric Uncertainty in ICL](#item-28) ⭐️ 8.0/10
29. [1.3B-Parameter Generative Model for Chest Radiography](#item-29) ⭐️ 8.0/10
30. [LooseControlVideo: 3D Boxes Enable Intuitive Video Control](#item-30) ⭐️ 8.0/10
31. [ImageWAM: Image Editing Replaces Video for Robot Action Models](#item-31) ⭐️ 8.0/10
32. [LIVE: Language-Guided Vision Embeddings for Controllable Perception](#item-32) ⭐️ 8.0/10
33. [Learning Asynchronous Schedules for Faster Diffusion Training](#item-33) ⭐️ 8.0/10
34. [Stochastic Hi-Fi Decomposes Scalar Interactions into Uniqueness, Redundancy, Synergy](#item-34) ⭐️ 8.0/10
35. [Solver-Free Training for Predict-then-Optimize](#item-35) ⭐️ 8.0/10
36. [AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge](#item-36) ⭐️ 8.0/10
37. [OPE for Missingness-Aware Policies in MDPs with MNAR Rewards](#item-37) ⭐️ 8.0/10
38. [Startup Claims Breakthrough in LLM Bottleneck](#item-38) ⭐️ 8.0/10
39. [ALS patient becomes first long-term BCI power user](#item-39) ⭐️ 8.0/10
40. [Alzheimer's Trigger May Be Amyloid-Tau Interference](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Roboflow's RF-DETR Achieves SOTA Real-Time Detection](https://github.com/roboflow/rf-detr) ⭐️ 9.0/10

Roboflow released RF-DETR, a real-time object detection and segmentation model that achieves state-of-the-art results on the COCO benchmark and was accepted at ICLR 2026. RF-DETR sets a new accuracy-latency Pareto frontier for real-time detection, making it highly suitable for deployment in latency-sensitive applications like autonomous driving and robotics. RF-DETR uses a DINOv2 vision transformer backbone and supports object detection, instance segmentation, and keypoint detection in a single API; the base model is Apache 2.0 licensed, while larger variants require a commercial license.

rss · GitHub Trending - Python · Jun 19, 22:49

**Background**: Object detection models traditionally rely on convolutional neural networks (CNNs) like YOLO, but DETR introduced a Transformer-based end-to-end approach. RF-DETR builds on DETR with neural architecture search to optimize for both accuracy and speed, targeting real-time applications.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/roboflow/rf-detr">GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026] · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2511.09554">[2511.09554] RF-DETR: Neural Architecture Search for Real-Time Detection Transformers</a></li>
<li><a href="https://learnopencv.com/rf-detr-object-detection/">RF-DETR by Roboflow: Fast Real-time Object Detection</a></li>

</ul>
</details>

**Tags**: `#object detection`, `#computer vision`, `#deep learning`, `#real-time`, `#ICLR`

---

<a id="item-2"></a>
## [ITNet Unifies CNNs, RNNs, and Transformers](https://arxiv.org/abs/2606.19538) ⭐️ 9.0/10

Researchers propose ITNet, a learnable integral transform architecture that subsumes convolution, attention, and recurrence as special cases, achieving competitive performance on ImageNet-1K, GLUE, ModelNet40, VQA v2, and NLVR2. This work suggests that the long-standing separation of CNNs, RNNs, and transformers is not fundamental, potentially leading to simpler, more general neural architectures that can adapt their inductive biases from data. ITNet uses a learnable kernel implemented as an MLP that models pairwise interactions, with tiled kernel fusion, importance-weighted Monte Carlo integration, and learned low-rank factorization for efficiency.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Convolutional networks, recurrent networks, and transformers have been mathematically distinct architectures with different inductive biases. An integral transform is a mathematical operation that maps a function to another function via a kernel, and a learnable integral transform allows the kernel to be learned from data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Integral_transform">Integral transform - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inductive_bias">Inductive bias - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#neural architecture`, `#integral transform`, `#unified model`, `#arXiv`

---

<a id="item-3"></a>
## [DeepSeek-V4 Preview: 1.6T MoE Models with Million-Token Context](https://arxiv.org/abs/2606.19348) ⭐️ 9.0/10

DeepSeek AI released a preview of DeepSeek-V4, including two MoE models: DeepSeek-V4-Pro (1.6T total parameters, 49B activated) and DeepSeek-V4-Flash (284B total, 13B activated), both supporting a context length of one million tokens. The series introduces Compressed Sparse Attention (CSA), Heavily Compressed Attention (HCA), Manifold-Constrained Hyper-Connections (mHC), and the Muon optimizer. This release pushes the frontier of open-source large language models, achieving state-of-the-art performance while dramatically reducing inference cost for long-context tasks. The million-token context capability makes long-horizon applications like document analysis and multi-turn reasoning more practical. DeepSeek-V4-Pro requires only 27% of the single-token inference FLOPs and 10% of the KV cache compared to DeepSeek-V3.2 in the one-million-token context setting. The models were pre-trained on over 32 trillion tokens and are available on Hugging Face.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling large total parameter counts with manageable compute. Long-context attention is traditionally expensive due to quadratic complexity; CSA and HCA reduce this by compressing key-value entries and using sparse or dense attention on compressed representations. Hyper-Connections improve residual stream expressiveness, and the Muon optimizer accelerates training convergence.

<details><summary>References</summary>
<ul>
<li><a href="https://dasroot.net/posts/2026/04/deepseek-v4-hybrid-attention-massive-contexts/">Inside DeepSeek V4: Hybrid Attention for Massive Contexts · Technical news about AI, coding and all</a></li>
<li><a href="https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/">DeepSeek AI Releases DeepSeek-V4: Compressed Sparse Attention and Heavily Compressed Attention Enable One-Million-Token Contexts - MarkTechPost</a></li>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#mixture-of-experts`, `#long-context`, `#deep learning`, `#AI research`

---

<a id="item-4"></a>
## [ATProto Has No Instances: A Protocol Analogy](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 8.0/10

Dan Abramov published an article explaining that ATProto, the protocol behind Bluesky, has no concept of 'instances' like Mastodon, using analogies to RSS and email to clarify its architecture. This clarification addresses a common misconception in the decentralized social media space, helping developers and users understand the fundamental architectural differences between ATProto and ActivityPub, which affects how moderation, hosting, and federation work. In ATProto, Personal Data Servers (PDS), Relays, and AppViews are separate services, unlike Mastodon where each instance bundles all functions. This separation allows independent scaling and avoids the 'defederation' problem seen in Mastodon.

hackernews · danabramov · Jun 19, 15:10 · [Discussion](https://news.ycombinator.com/item?id=48599515)

**Background**: ATProto (Authenticated Transfer Protocol) is a decentralized protocol for social networking, used by Bluesky. ActivityPub is the protocol behind Mastodon and the Fediverse. In Mastodon, each server (instance) hosts user data, handles federation, and provides the user interface, leading to issues like server lock-in and defederation. ATProto separates these concerns into distinct services: PDS for user data, Relays for data streaming, and AppViews for application logic.

<details><summary>References</summary>
<ul>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/understanding-atproto">Understanding Atproto - AT Protocol Docs - AT Protocol</a></li>

</ul>
</details>

**Discussion**: Comments on Hacker News debated the accuracy of the RSS analogy, with some arguing that RSS was less dependent on centralized services than ATProto's Relays. Others appreciated the clear explanation of architectural differences but felt the article downplayed the moderation challenges that instances solve.

**Tags**: `#ATProto`, `#ActivityPub`, `#decentralization`, `#Bluesky`, `#protocol design`

---

<a id="item-5"></a>
## [Project Valhalla Arrives in JDK 28 After a Decade](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Project Valhalla introduces value types and heap flattening to the JVM in JDK 28, enabling the JVM to store value objects directly in arrays without object headers or pointers, improving memory density and performance. This is a major JVM enhancement that bridges the gap between object-oriented expressiveness and low-level performance, benefiting Java applications with reduced memory footprint and faster access patterns, especially in data-intensive domains. Value types (inline classes) are identity-less objects that can be flattened in arrays and fields, but heap flattening is limited to objects with representations ≤ 64 bits; larger value types still require indirection.

hackernews · philonoist · Jun 19, 06:35 · [Discussion](https://news.ycombinator.com/item?id=48595511)

**Background**: Project Valhalla is an experimental OpenJDK project announced in July 2014, led by Brian Goetz, aiming to introduce value types to Java. Traditionally, all Java objects have identity and are accessed via references, causing memory overhead and indirection. Value types remove identity, allowing the JVM to store them inline, similar to primitives.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://medium.com/@vishalpriyadarshi/project-valhalla-bringing-value-types-and-performance-efficiency-to-java-83b85e00b791">Project Valhalla : Bringing Value Types and Performance... | Medium</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some appreciate the performance benefits but criticize the complexity and readability cost, such as value types breaking the principle of uniformity (e.g., assignment semantics differ between value and reference classes). Others defend the JVM's evolution, noting that many critics hold outdated views of Java.

**Tags**: `#Java`, `#JVM`, `#Project Valhalla`, `#performance`, `#language design`

---

<a id="item-6"></a>
## [EFF Calls for Free Public Court Records](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 8.0/10

The Electronic Frontier Foundation (EFF) argues that public court records should be free, criticizing the current pay-per-page PACER system and supporting legislation to create a modern, free-access platform. This matters because public access to court records is fundamental to transparency and justice; current fees create a barrier for individuals and organizations, undermining the principle that the law should be freely accessible. PACER charges $0.10 per page (capped at $3.00 per document), but state systems can be more expensive, e.g., Idaho charges $10 per page. The proposed bill would replace PACER and CM/ECF with a modern, unified platform.

hackernews · hn_acker · Jun 19, 17:34 · [Discussion](https://news.ycombinator.com/item?id=48600946)

**Background**: PACER (Public Access to Court Electronic Records) is a system that provides electronic access to federal court records, but users must pay per page. The EFF is a digital rights group advocating for civil liberties online. CourtListener and RECAP are free tools that crowdsource PACER documents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation - Wikipedia</a></li>
<li><a href="https://pacer.uscourts.gov/register-account">Register for an Account | PACER : Federal Court Records</a></li>

</ul>
</details>

**Discussion**: Commenters express frustration with high costs, especially in state courts (e.g., $10/page in Idaho). They praise CourtListener and RECAP as vital stopgap solutions, and hope the proposed legislation makes them obsolete.

**Tags**: `#legal tech`, `#public access`, `#government transparency`, `#PACER`, `#EFF`

---

<a id="item-7"></a>
## [Amateur Uses AI to Propose Decipherment of Linear A](https://aiclambake.com/clamtakes/linear-a/) ⭐️ 8.0/10

An amateur researcher, Tom Di Mino, used Anthropic's Claude Code AI tool to build Python scripts that analyze the Linear A corpus, leading to a proposed decipherment linking the script to an extinct Semitic language. He has reportedly translated over 300 words, a feat never achieved before. If validated, this would be the first successful decipherment of Linear A, a script that has remained undeciphered for over a century, potentially rewriting our understanding of Minoan civilization and its language. It also demonstrates a novel application of AI tools in historical linguistics and epigraphy. The decipherment relies on the 'Libation Formula,' the most studied recurring phrase in Linear A, and uses Claude Code to systematically test hypotheses at scale. The work is currently under review by linguistics experts at Rutgers and Cambridge universities.

hackernews · Kosturdistan · Jun 19, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48600107)

**Background**: Linear A is a writing system used by the Minoans on Crete from 1800 to 1450 BC, and it remains undeciphered since its rediscovery in 1900. It shares many glyphs with Linear B, which was deciphered in the 1950s and found to represent Mycenaean Greek. The corpus of Linear A is extremely fragmentary, with only a handful of longer texts, making decipherment challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A_script">Linear A script</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>

</ul>
</details>

**Discussion**: The community is cautiously optimistic, with many noting the plausibility of the approach and the scale of translation achieved. Some commenters highlight that the work is being reviewed by experts, lending credibility, while others express skepticism due to past unsubstantiated claims about Linear A. The use of Claude Code to build tools rather than as a black-box solver is praised.

**Tags**: `#Linear A`, `#AI`, `#decipherment`, `#archaeology`, `#Claude Code`

---

<a id="item-8"></a>
## [Google Releases TimesFM 2.5 for Time-Series Forecasting](https://github.com/google-research/timesfm) ⭐️ 8.0/10

Google Research has released TimesFM 2.5, a pretrained foundation model for time-series forecasting, with checkpoints available on Hugging Face and integrations with BigQuery ML, Google Sheets, and Vertex Model Garden. TimesFM provides a single pretrained model that can forecast diverse time-series data with zero-shot performance, reducing the need for custom models and enabling broader adoption of AI-driven forecasting in enterprise and productivity tools. TimesFM 2.5 uses 200M parameters (down from 500M), supports up to 16k context length, and offers continuous quantile forecasts up to 1k horizon via an optional 30M quantile head. It also removes the frequency indicator and adds new forecasting flags.

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**Background**: Time-series forecasting predicts future values based on historical data, used in finance, weather, and inventory management. Foundation models are large pretrained models that can be adapted to various tasks with minimal fine-tuning. TimesFM is a decoder-only transformer model trained on 100 billion real-world time points.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/timesfm">GitHub - google-research/timesfm: TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. · GitHub</a></li>
<li><a href="https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/">A decoder - only foundation model for time - series forecasting</a></li>
<li><a href="https://arxiv.org/abs/2310.10688">A decoder - only foundation model for time - series forecasting</a></li>

</ul>
</details>

**Discussion**: The community has actively contributed to TimesFM, with shoutouts to @kashif and @darkpowerxo for fine-tuning examples and unit tests, and @borealBytes for adding agent support. The GitHub repository shows ongoing engagement and collaborative improvements.

**Tags**: `#time-series`, `#foundation model`, `#forecasting`, `#Google Research`, `#ICML 2024`

---

<a id="item-9"></a>
## [Zhipu AI Releases GLM-5 Series with 1M Context](https://github.com/zai-org/GLM-5) ⭐️ 8.0/10

Zhipu AI (via zai-org) released the GLM-5 model series, including GLM-5.2, GLM-5.1, and GLM-5, with GLM-5.2 featuring a solid 1M-token context and improved coding benchmarks. This release advances long-horizon task capabilities, enabling AI agents to handle complex, multi-step workflows over extended contexts, which is critical for real-world software engineering and autonomous systems. GLM-5.2 uses IndexShare to reduce per-token FLOPs by 2.9× at 1M context, and achieves 81.0 on Terminal-Bench 2.1, close to Claude Opus 4.8's 85.0. The model series scales from 355B to 744B parameters with MoE architecture.

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**Background**: Long-horizon tasks require AI to plan and execute over many steps, often with long context windows. GLM-5 series builds on Zhipu's previous GLM models, targeting agentic engineering and complex coding tasks. The models are open-source and available on Hugging Face.

**Tags**: `#AI`, `#LLM`, `#GLM`, `#machine learning`, `#model release`

---

<a id="item-10"></a>
## [Codebase-Memory-MCP: Sub-ms Code Intelligence with Knowledge Graph](https://github.com/DeusData/codebase-memory-mcp) ⭐️ 8.0/10

DeusData released codebase-memory-mcp, a high-performance MCP server that indexes entire codebases into a persistent knowledge graph, achieving sub-millisecond queries and supporting 158 languages via tree-sitter AST analysis. This tool dramatically reduces token usage and tool calls for AI coding agents, enabling faster and more accurate code understanding, which could significantly improve developer productivity and AI-assisted code navigation. It indexes the Linux kernel (28M LOC, 75K files) in 3 minutes, answers structural queries in under 1ms, and ships as a single static binary with zero dependencies for macOS, Linux, and Windows.

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**Background**: MCP (Model Context Protocol) is a protocol that allows AI models to interact with external tools and data sources. A knowledge graph represents code entities (functions, classes) and their relationships, enabling efficient querying without scanning files. Tree-sitter is a parser generator tool that provides fast, incremental parsing for many languages.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/DeusData/codebase-memory-mcp">GitHub - DeusData/ codebase -memory-mcp: High-performance code ...</a></li>
<li><a href="https://codegraph.codes/">CodeGraph — Code Knowledge Graph for Claude Code & Cursor</a></li>
<li><a href="https://lobehub.com/mcp/eviking-codekg">codeKG — Codebase Knowledge Graph | ... · LobeHub</a></li>

</ul>
</details>

**Tags**: `#code intelligence`, `#MCP server`, `#knowledge graph`, `#developer tools`, `#open source`

---

<a id="item-11"></a>
## [Lightricks Releases LTX-2: Open-Source Audio-Video Model](https://github.com/Lightricks/LTX-2) ⭐️ 8.0/10

Lightricks has released LTX-2, an official Python package for inference and LoRA training of their audio-video generative model, along with model checkpoints on HuggingFace. LTX-2 is the first DiT-based audio-video foundation model that combines synchronized audio and video, high fidelity, and multiple performance modes in a single open-source package, potentially democratizing advanced video generation. The model has 22 billion parameters and includes a spatial upscaler for two-stage pipeline; it supports text-to-video, image-to-video, and audio-to-video generation.

rss · GitHub Trending - Python · Jun 19, 22:49

**Background**: DiT (Diffusion Transformer) is a class of generative models that combine diffusion processes with transformer architectures, enabling high-quality video generation. LoRA (Low-Rank Adaptation) is a lightweight fine-tuning technique that reduces trainable parameters, making it easier to adapt large models to specific tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Lightricks/LTX-2">GitHub - Lightricks/ LTX - 2 : Official Python inference and LoRA trainer...</a></li>
<li><a href="https://www.ynetnews.com/tech-and-digital/article/hklbzavrgx">Lightricks unveils powerful AI video model challenging OpenAI and...</a></li>
<li><a href="https://huggingface.co/docs/diffusers/training/lora">LoRA · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#video generation`, `#audio-video model`, `#LoRA`, `#open source`

---

<a id="item-12"></a>
## [OpenMontage: First Open-Source Agentic Video Production System](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage, the world's first open-source agentic video production system, has been released with 12 pipelines, 52 tools, and over 500 agent skills, enabling AI coding assistants to produce full videos from plain language descriptions. This project democratizes AI-powered video production by providing a free, open-source alternative to proprietary systems, potentially revolutionizing content creation for individuals and small teams. OpenMontage can create real video videos using free stock footage and open archives, not just image-based animations. It supports multiple AI providers and costs as low as $1.33 for a 60-second animated short.

rss · GitHub Trending - Python · Jun 19, 22:49

**Background**: Agentic video production systems use AI agents to autonomously handle tasks like scripting, asset generation, editing, and composition. OpenMontage is the first open-source system of its kind, contrasting with closed-source commercial tools.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/ OpenMontage : World's first open -source, agentic...</a></li>
<li><a href="https://openalt.pro/en/tools/openmontage-6d3bd03b">OpenMontage — Video AI Tool | OpenAlt</a></li>
<li><a href="https://www.scriptbyai.com/open-ai-video-production-agent/">Free AI Video Production Agent with Real-Footage Pipelines ...</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#video production`, `#AI agents`, `#tooling`, `#generative AI`

---

<a id="item-13"></a>
## [Deontic Policies for Agentic AI Governance](https://arxiv.org/abs/2606.19464) ⭐️ 8.0/10

A new paper proposes AgenticRei, a deontic policy framework that extends beyond traditional access control to govern LLM-driven agentic AI systems, incorporating obligations, prohibitions, dispensations, and conflict resolution. This addresses a critical gap in AI governance, as current policy engines like XACML, Rego, and Cedar cannot handle obligation lifecycle management or meta-policy conflicts, which are essential for enterprise security, privacy, and compliance in agentic systems. AgenticRei uses a deontic policy language built on the Rei framework, expressed as OWL (Web Ontology Language), and evaluated at runtime by a high-performance logic engine outside the LLM. It governs both tool invocations and agent-to-agent messages, and composes with industry frameworks like A2AS.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Deontic logic is a branch of logic that deals with obligations, permissions, and prohibitions. Current policy engines for AI systems primarily focus on authorization (permit/deny) and lack support for managing obligations over time or resolving conflicts between policies. Agentic AI systems, which can autonomously invoke tools and coordinate with other agents, require more comprehensive governance to ensure security and compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2501.05765v1">Deontic Temporal Logic for Formal Verification of AI Ethics - arXiv</a></li>
<li><a href="https://ebiquity.umbc.edu/paper/html/id/1221/Deontic-Policies-for-Runtime-Governance-of-Agentic-AI-Systems">Deontic Policies for Runtime Governance of Agentic AI Systems</a></li>
<li><a href="https://github.com/XMPro/Multi-Agent/blob/main/docs/concepts/deontic-principles.md">Deontic Principles: Rules of Engagement for Agents - GitHub</a></li>

</ul>
</details>

**Tags**: `#AI governance`, `#LLM agents`, `#deontic logic`, `#policy engines`, `#security`

---

<a id="item-14"></a>
## [Systematic Analysis of Diffusion Language Models](https://arxiv.org/abs/2606.19475) ⭐️ 8.0/10

A new paper presents a systematic experimental evaluation of eight state-of-the-art Diffusion Language Models (DLMs) across eight benchmarks covering reasoning, coding, translation, and other tasks, analyzing both generation quality and computational efficiency. This study provides a much-needed standardized comparison of DLMs, helping researchers and practitioners understand the performance-efficiency trade-offs of this emerging paradigm, which could influence future model design and deployment decisions. The analysis includes eight DLMs and examines the impact of inference-time factors such as denoising steps, context length, block size, and parallel unmasking strategies, with controlled comparisons of smaller models trained under identical conditions.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Large Language Models (LLMs) like GPT-4 typically generate text autoregressively, predicting one token at a time. Diffusion Language Models (DLMs) offer an alternative by generating text through iterative denoising, starting from random noise and gradually refining the entire sequence in parallel. This approach can potentially improve efficiency and enable bidirectional context, but systematic comparisons have been lacking.

<details><summary>References</summary>
<ul>
<li><a href="https://breynald.github.io/2025/03/10/dllm/">Diffusion Language Model : The Rise of a New... - Breynald Shelter</a></li>
<li><a href="https://arxiv.org/pdf/2508.10875">A Survey on Diffusion Language Models</a></li>

</ul>
</details>

**Tags**: `#diffusion language models`, `#LLMs`, `#experimental analysis`, `#natural language processing`, `#machine learning`

---

<a id="item-15"></a>
## [Hidden Anchors Explain Multi-Agent LLM Deliberation](https://arxiv.org/abs/2606.19494) ⭐️ 8.0/10

A new paper models multi-agent LLM deliberation as a dynamical system where each agent has a hidden internal belief (anchor) that pulls its opinion, explaining how confidence can exceed initial beliefs—a phenomenon not captured by classical models like DeGroot or Friedkin-Johnsen. This work provides a theoretical foundation for understanding and improving multi-agent LLM reasoning systems, revealing that deliberation can produce outcomes beyond the convex hull of initial opinions, which has implications for designing more effective AI collaboration protocols. The authors show that the hidden anchor can be recovered from deliberation data alone, and that testing whether the recovered anchor predicts held-out runs provides a simple check for anchor-driven behavior. Across three open-weight model families, anchor influence is equally strong, but anchor location varies, and only when it sits far from initial opinions does deliberation escape the convex hull.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Classical opinion dynamics models like DeGroot and Friedkin-Johnsen describe how agents' opinions converge through social influence, but they assume opinions remain within the convex hull of initial beliefs. The convex hull is the smallest convex polygon containing all initial opinion points. This paper introduces a hidden anchor—a persistent internal belief—that allows opinions to escape that hull, matching observed behavior in multi-agent LLM systems.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2603.10756">A Survey on Algorithmic Interventions in Opinion Dynamics</a></li>
<li><a href="https://arxiv.org/abs/2407.10680">Friedkin - Johnsen Model for Opinion Dynamics on Signed Graphs</a></li>
<li><a href="https://www.researchgate.net/publication/321752941_Steering_opinion_dynamics_via_containment_control">(PDF) Steering opinion dynamics via containment control</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#LLM deliberation`, `#opinion dynamics`, `#AI reasoning`, `#mathematical modeling`

---

<a id="item-16"></a>
## [DeXposure-Claw: Agentic System for DeFi Risk Supervision](https://arxiv.org/abs/2606.19501) ⭐️ 8.0/10

Researchers introduced DeXposure-Claw, an agentic system that combines graph time-series forecasting with LLM-based reasoning to provide auditable risk supervision for decentralized finance (DeFi). They also released DeXposure-Bench, a six-axis evaluation benchmark aligned with regulatory standards. This work addresses a critical gap in DeFi risk supervision by providing a structured, auditable framework that reduces false alarms from LLM agents. It could set a new standard for reliable AI-driven financial oversight, benefiting regulators and DeFi platforms alike. The system uses DeXposure-FM, a graph time-series foundation model, to forecast exposure networks, then applies deterministic monitors and confidence gates before generating supervisory tickets. Experiments on five years of real data demonstrated its effectiveness.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Decentralized finance (DeFi) involves complex, fast-moving credit risks across interconnected networks. General-purpose LLM agents often over-interpret weak evidence and recommend high-stakes interventions, while existing evaluations lack regulator-aligned metrics. DeXposure-Claw addresses this by routing LLM decisions through structured evidence and explicit false-intervention rate constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.19501">DeXposure-Claw: An Agentic System for DeFi Risk Supervision</a></li>

</ul>
</details>

**Tags**: `#DeFi`, `#LLM Agents`, `#Risk Supervision`, `#Graph Neural Networks`, `#Financial AI`

---

<a id="item-17"></a>
## [LLMs Blind to Their Own Limits on Clinical Data](https://arxiv.org/abs/2606.19509) ⭐️ 8.0/10

A new study reveals that LLMs exhibit epistemically vacuous confidence on clinical tabular data, outputting near-constant confidence regardless of accuracy, and proposes cross-model attribution divergence to detect such blind spots. This work exposes critical limitations in LLM confidence calibration for high-stakes domains like healthcare, where reliable uncertainty estimation is essential for safe deployment. The study compares Qwen 2.5 7B and XGBoost on a clinical prediction task, finding that LLM confidence tracks prompt format rather than accuracy, and that combining few-shot examples with SHAP-derived feature evidence reduces attribution disagreement from 1.54 to 0.38 and boosts accuracy from 49% to 75.3%.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Epistemic uncertainty refers to uncertainty due to lack of knowledge, as opposed to aleatoric uncertainty from inherent randomness. SHAP is a method for explaining model predictions by assigning importance to each feature. Cross-model attribution divergence measures disagreement between models' feature attributions, which can indicate epistemic blind spots.

<details><summary>References</summary>
<ul>
<li><a href="https://ethanlazuk.com/blog/hamsterdam-research-epistemic-aleatoric-uncertainty/">Epistemic vs. Aleatoric Uncertainty in LLMs & Why... - Ethan Lazuk</a></li>
<li><a href="https://www.emergentmind.com/papers/2406.02543">LLM Uncertainty : Quantifying and Preventing Hallucinations</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#epistemic uncertainty`, `#clinical data`, `#attribution divergence`, `#confidence calibration`

---

<a id="item-18"></a>
## [Emergent Alignment: LLMs Self-Correct Ethics via Introspection](https://arxiv.org/abs/2606.19527) ⭐️ 8.0/10

The paper proposes Emergent Alignment, a method where LLMs self-correct ethical misalignment by adding an introspective conscience step and training with Direct Preference Optimization (DPO), without needing an external judge. This addresses the emergent misalignment problem where fine-tuning can cause broad unethical behaviors, offering a scalable self-alignment technique that enhances AI safety without relying on weaker or stronger models. The method uses a frozen copy of the LLM itself as a judge and extends the training loss with a DPO-based alignment component, effective in training, fine-tuning, adversarial prompting, and zero-shot learning scenarios.

rss · arXiv - AI · Jun 19, 04:00

**Background**: Large Language Models (LLMs) can exhibit emergent misalignment—unethical behaviors arising from narrow fine-tuning, as shown in prior work. Direct Preference Optimization (DPO) is a technique that aligns models with human preferences by training on preference pairs without a separate reward model. Emergent Alignment leverages DPO and an introspective step to steer models away from unethical outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.17424">[2502.17424] Emergent Misalignment: Narrow finetuning can produce...</a></li>
<li><a href="https://huggingface.co/learn/smol-course/unit2/3">Hands-On Exercise: Direct Preference Optimization with...</a></li>

</ul>
</details>

**Tags**: `#LLM alignment`, `#AI safety`, `#Direct Preference Optimization`, `#emergent behavior`, `#self-correction`

---

<a id="item-19"></a>
## [Computational Identifiability: Bridging Theory and Practice](https://arxiv.org/abs/2606.19361) ⭐️ 8.0/10

This paper introduces 'computational identifiability,' a new framework that replaces theoretical identifiability's asymptotic assumptions with a finite computational search procedure for empirical estimators within a desired error tolerance. 该框架解决了理论可识别性的实际局限性，支持在小样本、模糊图结构和混合数据类型下进行因果识别，对机器学习和统计学的实际应用至关重要。 The framework defines identifiability as the existence of a finite search procedure that finds an empirical estimator within error tolerance, conditional on prior distributions and the search procedure itself. Experiments demonstrate its effectiveness on small samples, ambiguous graphs, mixed observational-interventional data, and counterfactual estimands.

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**Background**: Causal identification determines whether a causal effect can be uniquely computed from observed data and assumptions. Traditional theoretical identifiability assumes infinite data and asymptotic properties, which often fail in practice. This paper proposes a computation-bound alternative that works under finite-sample and computational constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19361">Computational Identifiability</a></li>
<li><a href="https://lmyint.github.io/causal_fall_2024/02-identification.html">Causal identification : building intuition – STAT 451</a></li>
<li><a href="https://stats.stackexchange.com/questions/552882/why-do-we-need-identification-in-causal-inference">causality - Why do we need identification in causal inference ?</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#identifiability`, `#computational complexity`, `#machine learning`, `#statistics`

---

<a id="item-20"></a>
## [Guard: Multi-Teacher Distillation for Robust Time-Series Forecasting](https://arxiv.org/abs/2606.19363) ⭐️ 8.0/10

Researchers propose Guard, a multi-teacher distillation framework that dynamically selects and adapts foundation models to train lightweight, robust forecasters for scientific time series, significantly reducing RMSE compared to fixed-weight baselines. This work addresses the critical trade-off between the rich knowledge of large time-series foundation models and their computational cost and domain misalignment, enabling high-precision scientific forecasting on resource-constrained edge devices. Guard uses a Contextual Router to select the best teacher per instance and an Uncertainty-Gated Temperature mechanism to attenuate distillation when teacher confidence diverges from domain reality. It outperforms globally superior FMs on 28.5% of the hardest instances.

rss · arXiv - Machine Learning · Jun 19, 04:00

**Background**: Time-Series Foundation Models (TSFMs) are pre-trained models that capture universal temporal dynamics but often suffer from distributional misalignment when applied zero-shot to specific scientific domains. Knowledge distillation transfers knowledge from large teacher models to smaller student models, but multi-teacher distillation typically uses fixed weights, ignoring instance-wise teacher quality. Guard introduces adaptive routing and uncertainty-aware gating to overcome these limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19363">[2606.19363] When to Trust, How to Distill : Multi -Foundation Model...</a></li>

</ul>
</details>

**Tags**: `#time-series forecasting`, `#foundation models`, `#knowledge distillation`, `#scientific computing`, `#edge AI`

---

<a id="item-21"></a>
## [Self-play RL with 30 min human data beats imitation learning](https://arxiv.org/abs/2606.19370) ⭐️ 8.0/10

Researchers developed a method that combines self-play reinforcement learning with only 30 minutes of human driving demonstrations as a regularization objective, producing driving policies that coordinate effectively with human drivers using 2500x less human data than imitation learning. This approach dramatically reduces the need for expensive human data in autonomous driving, addressing a key bottleneck in scaling self-driving technology. It also solves the behavioral misalignment problem of pure self-play policies, making them compatible with human drivers. The method uses a minimal safe goal-reaching reward plus a regularization term from human demonstrations, training completes in 15 hours on a single consumer-grade GPU. The resulting policies are evaluated against held-out human trajectories and show effective coordination.

rss · arXiv - Machine Learning · Jun 19, 04:00

**Background**: Self-play reinforcement learning trains agents by having them play against themselves in simulation, enabling cheap large-scale training without human data. However, pure self-play often leads to alien driving conventions incompatible with humans. Imitation learning requires massive human demonstrations (e.g., 1250 hours) to achieve similar performance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self- driving car - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#autonomous driving`, `#self-play`, `#human-in-the-loop`, `#behavioral alignment`

---

<a id="item-22"></a>
## [TreeTracer Visualizes Hidden LLM Bias via Stochastic Paths](https://arxiv.org/abs/2606.19344) ⭐️ 8.0/10

Researchers introduced TreeTracer, a visual analytics tool that aggregates hundreds of stochastic LLM generations into syntax-aligned hierarchical structures and visualizes them with a custom Sankey diagram to expose hidden biases. The tool was validated by comparing GPT-2 XL against the constitutionally aligned Apertus models, revealing biases like counterfactual pronoun suppression. This work addresses a critical gap in LLM auditing by making hidden biases visible through aggregated comparison, reducing cognitive load for analysts and supporting systematic bias detection. It has high potential impact on AI fairness research and the development of more equitable language models. TreeTracer uses a perturbation analysis pipeline that replaces ontology-defined terms in prompts, aggregates stochastic generations into syntax-aligned trees, and performs classification-aware node merging with an auxiliary language model. The system also applies contrastive inference to compute and display counterfactual token probabilities, reducing misinterpretation risks.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Large Language Models (LLMs) generate text stochastically, making it hard to detect biases that may only appear in low-probability outputs. Standard auditing methods rely on single outputs or static metrics, which miss hidden biases. TreeTracer aggregates many generations to reveal these biases through visual comparison.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19344">Visualizing Hidden LLM Bias through Stochastic Path Aggregation - arXiv</a></li>
<li><a href="https://arxiv.org/html/2606.19344v1">Visualizing Hidden LLM Bias through Stochastic Path Aggregation - arXiv</a></li>

</ul>
</details>

**Tags**: `#LLM bias`, `#visual analytics`, `#AI fairness`, `#natural language processing`, `#explainability`

---

<a id="item-23"></a>
## [LLM Fine-Tuning Gains from Task Alignment, Not Language Transfer](https://arxiv.org/abs/2606.19346) ⭐️ 8.0/10

A new study fine-tuned seven LLMs (4B–671B parameters) on Arabic and found no evidence of Semitic-specific zero-shot transfer; improvements across all languages suggest gains come from task alignment rather than cross-lingual linguistic relatedness. This challenges the common assumption that cross-lingual transfer in LLMs depends on linguistic similarity, with implications for multilingual NLP training strategies and resource allocation. The study tested dense and Mixture-of-Experts architectures, and a chain-of-thought ablation showed that models benefiting most from fine-tuning also benefit equally from inference-time reasoning, reinforcing the task-alignment interpretation.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Zero-shot cross-lingual transfer refers to a model trained in one language performing well in another without additional fine-tuning. Mixture-of-Experts (MoE) architectures use a router to activate only relevant subnetworks per token, enabling large capacity with lower compute. Chain-of-thought prompting improves reasoning by generating intermediate steps.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/aimstack/aim-and-mlflow-choosing-experiment-tracker-for-zero-shot-cross-lingual-transfer-4bad0a199fc7">Aim and MLflow — Choosing Experiment Tracker for Zero - Shot ...</a></li>
<li><a href="https://www.linkedin.com/posts/amjad-amireh-99822032_mixture-of-experts-moe-mixture-of-experts-activity-7456401344376176640-hXBj">Mixture of Experts AI Architecture for Efficient Language ... | LinkedIn</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**Tags**: `#cross-lingual transfer`, `#large language models`, `#NLP`, `#fine-tuning`, `#multilingual`

---

<a id="item-24"></a>
## [New Error Taxonomy Reveals LLM Limits in Hardware Design](https://arxiv.org/abs/2606.19347) ⭐️ 8.0/10

A new paper introduces an error taxonomy for LLM-generated hardware design code, categorizing failures into syntactic, semantic, solvable functional, and unsolvable functional types, and reveals that frontier models plateau at a 90.8% pass rate on the VerilogEval benchmark due to unsolvable functional errors. This work identifies a critical bottleneck in applying LLMs to hardware design, showing that alignment techniques only teach models to compile but not to reason, which has significant implications for AI-assisted engineering and the development of more capable models. The paper exposes a 'surface convergence gap' where optimizing to fix syntax errors actually worsens deeper functional failures, and finds that repeated sampling can patch solvable errors but RTL coding capacity remains bounded by pretraining knowledge.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: RTL (Register-Transfer Level) coding is a method of describing digital circuits using hardware description languages like Verilog. LLMs have shown promise in generating code but struggle with the parallel temporal logic required for hardware design. The VerilogEval benchmark is a standard evaluation framework for assessing LLM performance on Verilog code completion tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.11053v2">Revisiting VerilogEval : A Year of Improvements in Large-Language...</a></li>
<li><a href="https://github.com/NVlabs/verilog-eval">GitHub - NVlabs/ verilog - eval : Verilog evaluation benchmark for large...</a></li>
<li><a href="https://www.linkedin.com/pulse/accelerating-rtl-design-agentic-ai-multi-agent-llm-driven-y80uc">Accelerating RTL Design with Agentic AI: A Multi-Agent LLM-Driven...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#hardware design`, `#error taxonomy`, `#Verilog`, `#AI generalization`

---

<a id="item-25"></a>
## [Positional Bias in Diffusion LLMs: Analysis and Mitigation](https://arxiv.org/abs/2606.19349) ⭐️ 8.0/10

This paper reveals that query position significantly affects in-context learning in diffusion LLMs due to a spatial recency effect, and proposes a label-free mitigation method called Auto-ICL. This finding challenges the conventional trailing-query template inherited from autoregressive models, and the proposed Auto-ICL method can improve generation quality without requiring ground-truth labels, impacting future dLLM design and deployment. The authors empirically decouple positional variance from example semantic quality, showing they have comparable impact. They introduce Average Confidence (C̄) to track iterative decoding dynamics, which outperforms traditional single-step confidence for dLLMs.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Diffusion Large Language Models (dLLMs) are a non-autoregressive paradigm that generate text via iterative denoising, offering bidirectional context and parallel decoding. Unlike autoregressive LLMs with causal masking, dLLMs allow flexible query placement, but current practices often use trailing-query templates without considering this flexibility.

<details><summary>References</summary>
<ul>
<li><a href="https://koshurai.medium.com/diffusion-large-language-models-dllms-a-paradigm-shift-in-ai-e4aa3b71f298">Diffusion Large Language Models ( dLLMs ): A Paradigm... | Medium</a></li>
<li><a href="https://intuitionlabs.ai/articles/llm-position-bias-primacy-recency-effects">LLM Position Bias: Primacy and Recency Effects in ... | IntuitionLabs</a></li>
<li><a href="https://www.researchgate.net/publication/395034818_Diffusion_Language_Models_Know_the_Answer_Before_Decoding">(PDF) Diffusion Language Models Know the Answer Before Decoding</a></li>

</ul>
</details>

**Tags**: `#Diffusion LLMs`, `#In-Context Learning`, `#Positional Bias`, `#Decoding Dynamics`, `#Attention Mechanism`

---

<a id="item-26"></a>
## [Causal Attribution Pruning Boosts LLM Reasoning at Low Sparsity](https://arxiv.org/abs/2606.19350) ⭐️ 8.0/10

Researchers propose Causal Attribution Pruning (CAP), a training-free method that identifies critical attention heads by measuring their causal impact on reasoning tasks, achieving up to 61% relative accuracy gains over Wanda at 20% sparsity on ARC-Challenge. This work addresses the high inference cost of large language models by enabling more effective pruning that preserves reasoning performance, which is critical for deploying LLMs in resource-constrained environments. CAP uses a small calibration set of reasoning problems to estimate the expected performance degradation when each attention head is masked, then converts these causal scores into weight-level importance for pruning. Evaluations on Llama-3-8B-Instruct and Mistral-7B-Instruct at 10%, 20%, and 50% sparsity show CAP consistently outperforms Wanda at moderate sparsity levels.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Large language models (LLMs) rely on attention heads to process information, and pruning removes less important weights to reduce model size and inference cost. Existing pruning methods like Wanda use weight magnitudes or activation-based criteria, which may not capture the functional importance of attention heads for reasoning tasks. CAP introduces a causal intervention approach to directly measure each head's contribution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19350">Pruning via Causal Attribution Preserves Reasoning Performance in...</a></li>
<li><a href="https://eric-mingjie.github.io/wanda/home.html">A Simple and Effective Pruning Approach for Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2601.04398">Interpreting Transformers Through Attention Head Intervention</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#pruning`, `#causal attribution`, `#reasoning`, `#efficiency`

---

<a id="item-27"></a>
## [Survey Indexes 120 Sign-Language Datasets Across 35 Languages](https://arxiv.org/abs/2606.19352) ⭐️ 8.0/10

A comprehensive survey has indexed 120 sign-language datasets across 35 languages, analyzing challenges like modality imbalance, annotation granularity, and signer bias, and proposing a standardized 24-field datasheet and a public GitHub repository. This work provides a unified foundation for developing inclusive and scalable sign-language technologies, addressing fragmentation and inconsistency that have hindered progress in recognition, translation, and production systems. The survey introduces a 24-field Sign-Language Datasheet to standardize documentation and releases a public GitHub repository (https://github.com/Ginqwerty/Open-Sign-Language) for reproducible evaluation.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: Sign languages are visual languages used by Deaf and Hard-of-Hearing communities. Despite advances in AI-based sign-language recognition and translation, progress has been limited by fragmented datasets, inconsistent annotations, and lack of linguistic coverage. This survey systematically addresses these gaps.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19352">Sign - Language Datasets at Scale: A Comprehensive Survey on...</a></li>
<li><a href="https://arxiv.org/html/2403.02563v1">Systemic Biases in Sign Language AI Research: A Deaf-Led Call to...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s11227-025-07119-8">Data augmentation and debiasing for signers in signer -independent...</a></li>

</ul>
</details>

**Tags**: `#sign language`, `#datasets`, `#survey`, `#annotation`, `#benchmarks`

---

<a id="item-28"></a>
## [Self-Function Vectors Quantify Aleatoric Uncertainty in ICL](https://arxiv.org/abs/2606.19353) ⭐️ 8.0/10

The paper introduces self-function vectors, a method that leverages internal model representations to decompose aleatoric uncertainty in in-context learning, enabling more reliable LLM prediction confidence estimation. It also proposes the first rigorous evaluation protocol for aleatoric uncertainty in ICL, validated on synthetic and real-world tasks. This work addresses a critical gap in LLM reliability by separating aleatoric uncertainty (data noise) from epistemic uncertainty (model ignorance) in in-context learning. The method can be applied to practical tasks like hallucination detection, improving trustworthiness of LLM outputs. Self-function vectors are built upon Bayesian views and mechanistic interpretability of ICL, modeling the latent concept learned during prompting without relying on input or decoding manipulations. The evaluation protocol controls data properties to precisely quantify aleatoric uncertainty separately from epistemic uncertainty.

rss · arXiv - NLP · Jun 19, 04:00

**Background**: In-context learning (ICL) allows LLMs to adapt to new tasks from a few examples without fine-tuning, but predictions are sensitive to prompt design. Aleatoric uncertainty arises from inherent data noise, while epistemic uncertainty stems from model limitations; decomposing them is crucial for reliable predictions. Existing uncertainty quantification methods for LLMs are designed for standard generation tasks and fail to capture ICL dynamics.

<details><summary>References</summary>
<ul>
<li><a href="https://learnmechinterp.com/topics/function-vectors/">Function Vectors | Learn Mechanistic Interpretability</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10994-021-05946-3">Aleatoric and epistemic uncertainty in machine learning : an...</a></li>
<li><a href="https://arxiv.org/pdf/2604.12434">A Bayesian Perspective on the Role of Epistemic Uncertainty for...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#uncertainty quantification`, `#in-context learning`, `#mechanistic interpretability`, `#Bayesian methods`

---

<a id="item-29"></a>
## [1.3B-Parameter Generative Model for Chest Radiography](https://arxiv.org/abs/2606.19460) ⭐️ 8.0/10

Researchers introduced the first billion-parameter generative foundation model for chest radiograph synthesis, with over 1.3 billion parameters trained on 1.2 million radiographs using rectified flow transformers. This model addresses poor generalization of radiographic AI across patient subgroups and institutions, enabling controllable generation and editing to diversify clinical datasets and improve diagnostic model robustness. The model supports controllable generation across demographic subgroups, acquisition views, and a dozen pathologies, and achieves fidelity indistinguishable from real radiographs to clinical experts.

rss · arXiv - Computer Vision · Jun 19, 04:00

**Background**: Rectified flow transformers combine the efficiency of rectified flow (an ODE-based generative method) with the representational power of transformers. Generative foundation models for medical imaging aim to synthesize high-fidelity images to augment training data and evaluate model robustness.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.03206">[2403.03206] Scaling Rectified Flow Transformers for...</a></li>
<li><a href="https://radit-project.github.io/">Scaling Generative Foundation Models for Chest Radiography with...</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#medical imaging`, `#foundation model`, `#chest radiography`, `#rectified flow`

---

<a id="item-30"></a>
## [LooseControlVideo: 3D Boxes Enable Intuitive Video Control](https://arxiv.org/abs/2606.19495) ⭐️ 8.0/10

LooseControlVideo introduces a framework that uses sparse, oriented 3D boxes as a blocking proxy for intuitive 3D spatial control in text-to-video generation, fine-tuned on a novel DNOCS encoding with the Wan 2.2 backbone. This work addresses the critical challenge of multi-object scene orchestration in text-to-video generation, enabling users to author high-level layouts and trajectories while the model handles realistic occlusions and dynamics, significantly outperforming existing 2D-box and flow-based baselines. The method achieves 1.2x to 3x improvement in Trajectory Error, 2x improvement in Rigid Motion Consistency, and 1.5x to 2x increase in Occlusion Accuracy over state-of-the-art layout-conditioned models on nuScenes, HO-3D, and BEHAVE benchmarks.

rss · arXiv - Computer Vision · Jun 19, 04:00

**Background**: Text-to-video generation aims to create videos from textual descriptions. Existing depth-conditioned models require dense, frame-accurate guidance, which is labor-intensive for dynamic scenes. LooseControlVideo uses sparse 3D boxes as a high-level control signal, allowing users to specify object positions and trajectories without dense annotations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19495">LooseControlVideo : Directorial Video Control using Spatial Blocking</a></li>
<li><a href="https://shariqfarooq123.github.io/LooseControlVideo/">LooseControlVideo Project Page</a></li>
<li><a href="https://huggingface.co/papers/2606.19495">Paper page - LooseControlVideo : Directorial Video Control using...</a></li>

</ul>
</details>

**Tags**: `#text-to-video`, `#3D control`, `#video generation`, `#spatial layout`, `#deep learning`

---

<a id="item-31"></a>
## [ImageWAM: Image Editing Replaces Video for Robot Action Models](https://arxiv.org/abs/2606.19531) ⭐️ 8.0/10

ImageWAM proposes a novel framework that repurposes pretrained image editing models for robot action prediction, challenging the dominant video generation approach in world action models. This work significantly reduces computational cost and latency—achieving 1/6 FLOPs and 1/4 latency of video-based WAMs—while maintaining or improving performance, making world action models more practical for real-world robotics. ImageWAM does not decode the target frame at inference; instead, it conditions a flow-matching action expert on KV caches from image-editing denoising, using them as compact world-action context. It outperforms standard VLA baselines and competitive WAMs without additional policy pretraining.

rss · arXiv - Computer Vision · Jun 19, 04:00

**Background**: World Action Models (WAMs) are embodied AI systems that unify predictive world modeling with action generation, typically relying on video generation to predict future frames. However, video generation is computationally expensive and prone to errors from irrelevant details. Image editing offers a more efficient alternative by focusing only on action-relevant transformations between current and target states.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/yuyangalin/ImageWAM">GitHub - yuyangalin/ ImageWAM : ImageWAM : Do World Action Models...</a></li>
<li><a href="https://huggingface.co/papers/2606.19531">Paper page - ImageWAM: Do World Action Models Really Need Video...</a></li>

</ul>
</details>

**Tags**: `#world action models`, `#image editing`, `#robot control`, `#video generation`, `#AI`

---

<a id="item-32"></a>
## [LIVE: Language-Guided Vision Embeddings for Controllable Perception](https://arxiv.org/abs/2606.19584) ⭐️ 8.0/10

Researchers propose LIVE (Language-Instructed Vision Embeddings), a framework that uses language instructions to dynamically guide a vision encoder at inference time, producing task-centric embeddings without task-specific retraining. LIVE reduces visual hallucinations by 34 points on the MMVP benchmark, outperforms much larger vision-language models on VQA, and generalizes to unseen tasks, offering a lightweight path toward adaptive, instruction-driven visual intelligence. LIVE is a vision-encoder-only approach, making it lightweight and efficient enough to run on device. It achieves dynamic, fine-grained control of the encoder by training it to follow textual instructions.

rss · arXiv - Computer Vision · Jun 19, 04:00

**Background**: Traditional vision foundation models are static feature extractors; task adaptation requires large downstream models or fine-tuning. LIVE instead uses language as high-level guidance to steer the vision encoder, producing controllable and generalizable embeddings at inference time.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19584">[2606.19584] Language - Instructed Vision Embeddings for...</a></li>
<li><a href="https://live-embedding.github.io/">LIVE : Language - Instructed Vision Embeddings for Controllable and...</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#vision-language models`, `#foundation models`, `#instruction-driven perception`, `#hallucination reduction`

---

<a id="item-33"></a>
## [Learning Asynchronous Schedules for Faster Diffusion Training](https://arxiv.org/abs/2606.19662) ⭐️ 8.0/10

Researchers propose a method to learn asynchronous schedules for multi-representation diffusion models, achieving 4x training reduction on ImageNet 256x256 while matching or surpassing state-of-the-art FID scores. This work significantly reduces the computational cost of training high-quality diffusion models, making them more accessible for research and deployment, and could accelerate progress in image generation and other generative tasks. The method uses a schedule-corrected objective and a flexible parametric schedule class that is convex and monotone by construction, learned with less than 1% additional compute. With AutoGuidance, a 200-epoch model reaches FID 1.05, matching the 800-epoch SFD-XL baseline.

rss · arXiv - Computer Vision · Jun 19, 04:00

**Background**: Diffusion models generate images by gradually denoising a random noise sample. Multi-representation diffusion models denoise complementary views (e.g., different frequency bands) of an image, and their performance depends on the asynchronous schedule that decides when each view is denoised. Prior work used fixed schedules; this paper learns the schedule from data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19662">Learning When to Denoise: Optimizing Asynchronous Schedules for...</a></li>
<li><a href="https://www.emergentmind.com/topics/asynchronous-diffusion-models">Asynchronous Diffusion Models</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#asynchronous scheduling`, `#image generation`, `#flow matching`, `#efficient training`

---

<a id="item-34"></a>
## [Stochastic Hi-Fi Decomposes Scalar Interactions into Uniqueness, Redundancy, Synergy](https://arxiv.org/abs/2606.19410) ⭐️ 8.0/10

The paper introduces Stochastic Hi-Fi, a post-hoc, retraining-free method that decomposes pairwise interaction scores into uniqueness, redundancy, and synergy components, with theoretical proof and applications to structural causal models and GPT-2. This work addresses a fundamental limitation of scalar interaction indices by disentangling conflated mechanisms, significantly improving interpretability in machine learning models, especially large language models, and enabling more precise analysis of feature interactions. Stochastic Hi-Fi uses interventional masked inference with coupled diamond sampling for variance reduction, provides finite-sample Monte Carlo bounds, and achieves up to 411x larger interaction-magnitude recovery ratios on tabular SCMs compared to scalar baselines.

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**Background**: Signed pairwise interaction scores, such as Shapley-Taylor and Shapley Interaction indices, are commonly used to measure feature interactions in machine learning models. However, these scalar scores conflate three distinct mechanisms: uniqueness, redundancy, and synergy, making interpretation ambiguous. Stochastic Hi-Fi provides a decomposition that separates these mechanisms using interventional inference.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1902.05622">[1902.05622] The Shapley Taylor Interaction Index</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#causal inference`, `#machine learning`, `#feature interaction`, `#LLM`

---

<a id="item-35"></a>
## [Solver-Free Training for Predict-then-Optimize](https://arxiv.org/abs/2606.19587) ⭐️ 8.0/10

Researchers propose a novel training method for predict-then-optimize that eliminates the need for solver calls during gradient evaluation, using a measure transformation principle to create a solver-free surrogate loss. This method dramatically reduces training time by orders of magnitude while maintaining competitive decision quality, making decision-focused learning scalable to larger problems where solver calls are a bottleneck. The method provides theoretical guarantees including Fisher consistency and excess risk bounds, and empirically matches state-of-the-art decision quality with significantly lower computational cost.

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**Background**: In the predict-then-optimize paradigm, machine learning predictions are used as coefficients in downstream optimization problems. Directly minimizing decision regret is challenging because the decision mapping is piecewise constant with zero gradients almost everywhere. Existing methods smooth the differentiation but require expensive solver calls per gradient step, limiting scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/predict-then-optimize-paradigm-9d829742-aae1-4663-9a7f-ac6606541a6b">Predict - Then - Optimize Paradigm</a></li>
<li><a href="https://arxiv.org/html/2601.04062">Smart Predict – then – Optimize Paradigm for Portfolio Optimization in...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#optimization`, `#decision-focused learning`, `#predict-then-optimize`

---

<a id="item-36"></a>
## [AURA: Adaptive Uncertainty-aware Refinement for LLM-as-a-Judge](https://arxiv.org/abs/2606.19714) ⭐️ 8.0/10

AURA is a novel adaptive uncertainty-aware framework that iteratively learns a human-consistency signal and prioritizes uncertain pairwise comparisons for human review, enabling more reliable LLM-as-a-judge auditing. This addresses a critical limitation in LLM evaluation: judge bias and the scarcity of human annotations. By selectively focusing human effort on uncertain cases, AURA can significantly improve the reliability of LLM-as-a-judge systems without requiring full human evaluation. AURA treats trust in a judge as a latent quantity that is progressively refined as evidence accumulates. It provides a compact formulation, a stable refinement procedure, and comprehensive evaluation on both synthetic and real pairwise LLM-answer data.

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**Background**: LLM-as-a-judge is a method where a large language model evaluates AI outputs against defined criteria, but these models often exhibit biases and may not align perfectly with human judgment. Traditional auditing assumes a reliable subset of examples or clean supervision signals are available, which is fragile in practice. AURA addresses this by adaptively learning from limited human verification.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19714">AURA: Adaptive Uncertainty - aware Refinement for LLM-as-a-Judge...</a></li>
<li><a href="https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge">LLM - as - a - Judge - Langfuse</a></li>
<li><a href="https://arxiv.org/pdf/2411.15594">A Survey on LLM - as - a - Judge</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#auditing`, `#uncertainty`, `#human-in-the-loop`, `#NLP`

---

<a id="item-37"></a>
## [OPE for Missingness-Aware Policies in MDPs with MNAR Rewards](https://arxiv.org/abs/2606.20206) ⭐️ 8.0/10

This paper introduces novel methods for off-policy evaluation in finite-horizon Markov decision processes when rewards are missing not at random (MNAR), using shadow variables and a bridge function to correct selection bias. This work addresses a critical gap in offline reinforcement learning by handling MNAR rewards, which are common in healthcare and marketing, enabling more reliable policy evaluation from real-world logged data. The method formalizes a reward-dependent propensity model, uses future states as shadow variables, and introduces a bridge function estimated via a min-max procedure to recover the conditional mean reward without modeling the MNAR mechanism explicitly.

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**Background**: Off-policy evaluation (OPE) estimates the value of a target policy using data collected from a different behavior policy. In many real-world applications, rewards are often missing not at random (MNAR), meaning the missingness depends on the unobserved reward itself, which introduces selection bias. Existing OPE methods typically assume rewards are fully observed or missing at random, limiting their applicability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.16061">Partial Identification under Missing Data Using Weak Shadow ... - arXiv</a></li>
<li><a href="https://arxiv.org/abs/2202.04970">[2202.04970] Off-Policy Fitted Q - Evaluation with Differentiable...</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1002/sam.70045">Neural Estimation of Treatment Bridge Functions for Proximal Causal Inference - Zhang - 2025 - Statistical Analysis and Data Mining: An ASA Data Science Journal - Wiley Online Library</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#off-policy evaluation`, `#missing data`, `#causal inference`

---

<a id="item-38"></a>
## [Startup Claims Breakthrough in LLM Bottleneck](https://www.technologyreview.com/2026/06/19/1139313/a-startup-claims-it-broke-through-a-bottleneck-thats-holding-back-llms/) ⭐️ 8.0/10

Miami-based AI startup Subquadratic emerged from stealth mode claiming to have solved the quadratic attention bottleneck that has limited large language models for nearly a decade. The company has shared results from an independent evaluation to support its claims. If true, this breakthrough could dramatically reduce the computational cost and power consumption of LLMs, enabling much longer context windows and broader deployment. The claim addresses a fundamental limitation of the Transformer architecture that has constrained AI progress. Subquadratic's technology, called SubQ, claims to be the first commercial LLM built on subquadratic attention, with a 12-million-token context window at a fraction of frontier costs. However, details remain sparse and the claims have been met with skepticism from the AI community.

rss · MIT Technology Review · Jun 19, 10:40

**Background**: Large language models like GPT-4 rely on the Transformer architecture, which uses an attention mechanism that scales quadratically with input length. This quadratic complexity makes processing long sequences extremely expensive in terms of memory and computation, limiting context windows to thousands of tokens. Subquadratic attention aims to reduce this complexity, enabling much longer contexts without proportional cost increases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/19/1139313/a-startup-claims-it-broke-through-a-bottleneck-thats-holding-back-llms/">A startup claims it broke through a bottleneck that’s holding back LLMs</a></li>
<li><a href="https://thenextweb.com/news/subquadratic-subq-sparse-attention-llm-bottleneck">A startup says it cracked the bottleneck holding back AI</a></li>
<li><a href="https://www.peremptory.ai/posts/subquadratic-subq-llm-attention-architecture">A Startup Claims to Have Broken the Transformer's Core Bottleneck</a></li>

</ul>
</details>

**Tags**: `#LLMs`, `#startup`, `#AI research`, `#bottleneck`

---

<a id="item-39"></a>
## [ALS patient becomes first long-term BCI power user](https://www.technologyreview.com/2026/06/19/1139270/brain-computer-interface-trials-are-taking-off/) ⭐️ 8.0/10

Casey Harrell, a man with ALS, has become the first long-term power user of a brain-computer interface, using the implant for nearly three years to communicate despite paralysis. This milestone demonstrates that BCI technology can provide sustained, real-world benefit for severely paralyzed individuals, paving the way for broader clinical adoption and improved quality of life. Harrell is unable to speak coherently without the device, which interprets neural signals from his motor cortex to enable communication. The implant has been used for nearly three years, marking the longest continuous use of a BCI for communication.

rss · MIT Technology Review · Jun 19, 09:00

**Background**: A brain-computer interface (BCI) is a direct communication pathway between the brain and an external device, bypassing muscles and nerves. For people with ALS or paralysis, BCIs can decode neural activity to control cursors, spell letters, or operate assistive devices. Previous trials have been short-term, but Harrell's case shows long-term viability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alzforum.org/news/research-news/mind-machine-meld-brain-computer-interfaces-als-paralysis">Mind-machine Meld: Brain-computer Interfaces for ALS , Paralysis</a></li>
<li><a href="https://neurosciencenews.com/als-paralysis-computer-control-implant-5512/">Implant Allows Locked In ALS Patient to Operate... - Neuroscience News</a></li>
<li><a href="https://alsnewstoday.com/news/nih-grants-10-million-launch-us-trial-stentrode-severe-paralysis/">NIH Grants $10M to US Trial of Stentrode Brain Implant for ALS ...</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#neurotechnology`, `#ALS`, `#medical technology`, `#human augmentation`

---

<a id="item-40"></a>
## [Alzheimer's Trigger May Be Amyloid-Tau Interference](https://www.sciencedaily.com/releases/2026/06/260617032209.htm) ⭐️ 8.0/10

Scientists propose that Alzheimer's disease is triggered by amyloid beta interfering with tau protein function, rather than by amyloid plaques alone. This paradigm shift could redirect drug development toward targeting the amyloid-tau interaction, potentially leading to more effective treatments for Alzheimer's disease. The study suggests that amyloid beta disrupts tau's role in stabilizing microtubules, which are essential for neuron structure and transport. This disruption may initiate the neuronal damage that leads to Alzheimer's pathology.

rss · ScienceDaily Health · Jun 19, 02:49

**Background**: Alzheimer's disease is characterized by two hallmark brain abnormalities: amyloid plaques (clumps of amyloid beta protein) and tau tangles (twisted fibers of tau protein). For decades, the dominant hypothesis was that amyloid plaques directly cause the disease. However, treatments targeting plaques have shown limited success, prompting researchers to explore alternative mechanisms. Tau protein normally helps maintain the structural stability of neurons by binding to microtubules.

<details><summary>References</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/35443153/">Regional Aβ- tau interactions promote onset and acceleration of...</a></li>
<li><a href="https://link.springer.com/article/10.1186/s40035-025-00479-4">Dual modulation of amyloid beta and tau aggregation and dissociation...</a></li>
<li><a href="https://int.livhospital.com/neurofibrillary-tangles-tau-protein-guide/">Neurofibrillary Tangles Tau Protein : Guide - Liv Hospital</a></li>

</ul>
</details>

**Tags**: `#Alzheimer's`, `#neuroscience`, `#amyloid beta`, `#tau protein`

---