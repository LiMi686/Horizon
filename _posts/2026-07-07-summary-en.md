---
layout: default
title: "Horizon Summary: 2026-07-07 (EN)"
date: 2026-07-07
lang: en
---

> From 111 items, 30 important content pieces were selected

---

1. [EU Parliament Advances Controversial Chat Control Proposal](#item-1) ⭐️ 9.0/10
2. [Gemma 4: Open-Weight Multimodal Models with MoE and Thinking Mode](#item-2) ⭐️ 9.0/10
3. [Kokoro: Local, CPU-Friendly High-Quality TTS](#item-3) ⭐️ 8.0/10
4. [EU Mandates Driver Monitoring Cameras in All New Cars](#item-4) ⭐️ 8.0/10
5. [Microsoft Lays Off id Software's idTech Engine Team](#item-5) ⭐️ 8.0/10
6. [Astro 7.0 Launches with Rust-Based Compiler](#item-6) ⭐️ 8.0/10
7. [sqlite-utils 4.0 Introduces Schema Migrations](#item-7) ⭐️ 8.0/10
8. [Tencent Releases Hy3: 295B MoE Model with 21B Active Parameters](#item-8) ⭐️ 8.0/10
9. [GitHub Repo Leaks System Prompts of Major AI Chatbots](#item-9) ⭐️ 8.0/10
10. [Addy Osmani Releases Agent Skills for AI Coding Agents](#item-10) ⭐️ 8.0/10
11. [RuView: WiFi-Based Spatial Intelligence Without Cameras](#item-11) ⭐️ 8.0/10
12. [nanoGPT: Simple, Fast GPT Training Repo by Karpathy](#item-12) ⭐️ 8.0/10
13. [Anthropic releases financial services AI agents](#item-13) ⭐️ 8.0/10
14. [iFLYTEK Unveils Unified Multimodal Foundation Model for Embodied AI](#item-14) ⭐️ 8.0/10
15. [Internal Pluralism Challenges Pairwise Comparisons](#item-15) ⭐️ 8.0/10
16. [REDI: Open-Source Framework Automates Scientific Data Readiness](#item-16) ⭐️ 8.0/10
17. [SwarmResearch: Multi-Agent Orchestration for Open-Ended Discovery](#item-17) ⭐️ 8.0/10
18. [OCM: Object-Centric Environment Modeling for LLM Agents](#item-18) ⭐️ 8.0/10
19. [Oyster-II: RL-Based Constructive Safety Alignment for LLMs](#item-19) ⭐️ 8.0/10
20. [VERITAS: A General-Purpose Replication Tool for Science](#item-20) ⭐️ 8.0/10
21. [Five Failure Modes in AI Safety Benchmark Audits](#item-21) ⭐️ 8.0/10
22. [GRAFT: Per-Word Pronunciation Control in Zero-Shot TTS](#item-22) ⭐️ 8.0/10
23. [Risk Aversion Generalization in LLMs Across 98 Orders of Magnitude](#item-23) ⭐️ 8.0/10
24. [Why LLMs Fail at CBT-Guided Affective Reasoning](#item-24) ⭐️ 8.0/10
25. [Decision framework for cross-habitat marine species recognition](#item-25) ⭐️ 8.0/10
26. [CORA: Per-Slice Coherent Orthogonal Rotation for SVD-Based Low-Rank Adaptation](#item-26) ⭐️ 8.0/10
27. [Benign Overfitting Impossible in Diffusion Models](#item-27) ⭐️ 8.0/10
28. [Sequential Correlations Change In-Context Learning](#item-28) ⭐️ 8.0/10
29. [RoBAS: Robust Bayes-Assisted Conformal Prediction](#item-29) ⭐️ 8.0/10
30. [Optimal MoE Model Averaging for Conditional Generative Models](#item-30) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [EU Parliament Advances Controversial Chat Control Proposal](https://www.heise.de/en/news/Showdown-in-Strasbourg-The-unexpected-return-of-Chat-Control-1-0-11356680.html) ⭐️ 9.0/10

The EU Parliament passed the first round of the Chat Control proposal in a procedural vote, making it harder to block in the second reading by requiring an absolute majority for amendments. This move raises significant concerns about mass surveillance and encryption, as the proposal could mandate scanning of private messages for child sexual abuse material, potentially undermining end-to-end encryption. The procedural tactic requires an absolute majority of 361 votes for amendments or rejection on Thursday, while a simple majority suffices for the other side, and many MEPs may have already left for summer break.

hackernews · miroljub · Jul 7, 15:16 · [Discussion](https://news.ycombinator.com/item?id=48819008)

**Background**: Chat Control, formally the Child Sexual Abuse Regulation (CSAR), was proposed by the European Commission in May 2022 to combat child sexual abuse online. Critics argue it would enable mass surveillance of private communications and weaken encryption, as it may require platforms to scan messages for illegal content.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chat_Control">Chat Control - Wikipedia</a></li>
<li><a href="https://edri.org/our-work/chat-control-what-is-actually-going-on/">Chat Control: What is actually going on? - European Digital Rights (EDRi)</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration over the EU repeatedly pushing unpopular laws, with some citing Jean-Claude Juncker's quote about step-by-step legislation. Others noted the tactical advantage for proponents and doubted enough 'no' votes could be found by Thursday.

**Tags**: `#privacy`, `#EU legislation`, `#surveillance`, `#encryption`, `#politics`

---

<a id="item-2"></a>
## [Gemma 4: Open-Weight Multimodal Models with MoE and Thinking Mode](https://arxiv.org/abs/2607.02770) ⭐️ 9.0/10

Google's Gemma team released Gemma 4, a new family of open-weight multimodal language models featuring dense and Mixture-of-Experts (MoE) architectures ranging from 2.3B to 31B parameters, along with improved vision and audio encoders and a thinking mode for enhanced reasoning. This release advances open-weight AI by introducing architectural innovations like MoE and encoder-free design, enabling strong performance on STEM and multimodal benchmarks while rivaling larger frontier models, which could accelerate research and deployment of efficient, capable multimodal systems. The 12B model uses a unified encoder-free architecture that processes raw audio and image patches via linear projections, reducing parameters and enabling local deployment on 16GB RAM. The thinking mode allows models to generate reasoning traces before answering, improving inference quality.

rss · arXiv - NLP · Jul 7, 04:00

**Background**: Mixture-of-Experts (MoE) is a neural network design that activates only a subset of parameters per input, improving efficiency without sacrificing capacity. Traditional multimodal models use separate encoders for each modality, which adds latency and memory. Gemma 4's encoder-free approach eliminates these separate encoders, feeding raw data directly into the language model.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.11181">[2507.11181] Mixture of Experts in Large Language Models - arXiv.org</a></li>
<li><a href="https://ai.google.dev/gemma/docs/capabilities/thinking">Thinking mode in Gemma | Google AI for Developers</a></li>
<li><a href="https://betterstack.com/community/guides/ai/gemma-4-12b-encoder/">Gemma 4 12B: Encoder-Free Multimodal Architecture with Linear ...</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#multimodal AI`, `#open-source`, `#mixture-of-experts`, `#reasoning`

---

<a id="item-3"></a>
## [Kokoro: Local, CPU-Friendly High-Quality TTS](https://ariya.io/2026/03/local-cpu-friendly-high-quality-tts-text-to-speech-with-kokoro/) ⭐️ 8.0/10

Kokoro, an open-source TTS model with 82 million parameters, now enables high-quality text-to-speech on CPU without requiring a GPU, and supports manual IPA pronunciation guides. This makes high-quality TTS accessible to users without dedicated GPUs, lowering the barrier for local speech synthesis in accessibility tools, content consumption, and voice interfaces. Kokoro-82M is particularly efficient on Apple Silicon via the mlx-audio library, and community extensions like a Chrome extension allow reading any webpage with sentence highlighting.

hackernews · speckx · Jul 7, 18:24 · [Discussion](https://news.ycombinator.com/item?id=48821576)

**Background**: Text-to-speech (TTS) converts written text into spoken audio. Many high-quality TTS models require powerful GPUs, limiting local use. Kokoro's CPU-friendly design and IPA support address this gap, enabling accurate pronunciation of homographs and foreign words.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kokoro_TTS">Kokoro TTS</a></li>
<li><a href="https://kokorottsai.com/">Kokoro TTS: Advanced AI Text-to-Speech Model with 82M parameters</a></li>

</ul>
</details>

**Discussion**: Community members praise Kokoro for its CPU efficiency and IPA support, with some building Chrome extensions or Linux tools around it. Users note limitations with single-word utterances and homograph disambiguation, but overall sentiment is positive.

**Tags**: `#TTS`, `#accessibility`, `#open-source`, `#AI`, `#CPU`

---

<a id="item-4"></a>
## [EU Mandates Driver Monitoring Cameras in All New Cars](https://allaboutcookies.org/eu-mandatory-distracted-driver-system) ⭐️ 8.0/10

Starting from July 2024, the European Union requires every new car and van sold to include an infrared driver-monitoring camera as part of the General Safety Regulation. This regulation aims to reduce accidents caused by driver distraction, but it also raises significant privacy and usability concerns, as drivers may feel surveilled and annoyed by the system's alerts. The camera monitors eye and head movements to detect drowsiness or distraction, and it must comply with strict data protection rules, though privacy advocates argue the safeguards are insufficient.

hackernews · nickslaughter02 · Jul 7, 20:50 · [Discussion](https://news.ycombinator.com/item?id=48823557)

**Background**: Driver monitoring systems are part of a broader trend of Advanced Driver Assistance Systems (ADAS) that include features like lane-keeping assist and adaptive cruise control. Surveys show that many drivers find these features annoying and often turn them off, which could undermine the safety benefits of the mandate.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cryptopolitan.com/eu-car-rules-driver-cameras-and-higher-costs/">New EU car rules bring driver-facing cameras, and higher costs</a></li>
<li><a href="https://reclaimthenet.org/eu-mandates-driver-facing-cameras-in-new-cars-from-today">EU Mandates Driver-Facing Cameras in New Cars From Today</a></li>
<li><a href="https://allaboutcookies.org/eu-mandatory-distracted-driver-system">All Cars Sold in the EU Now Require a Camera Aimed at Your Face. It's ...</a></li>

</ul>
</details>

**Discussion**: Commenters are divided: some appreciate the potential safety benefits, citing personal experience with Ford's Blue Cruise system, while others criticize the poor user experience of modern driver-assist features, comparing them to Boeing's alarm confusion. Many express frustration with mandatory features that cannot be turned off.

**Tags**: `#regulation`, `#automotive`, `#privacy`, `#safety`, `#driver monitoring`

---

<a id="item-5"></a>
## [Microsoft Lays Off id Software's idTech Engine Team](https://gamefromscratch.com/microsoft-fire-idtech-team-at-id-software/) ⭐️ 8.0/10

Microsoft has laid off the entire idTech engine development team at id Software, the studio behind the Doom and Quake franchises. This move signals a shift away from proprietary engine development toward reliance on third-party engines like Unreal Engine. This decision could lead to homogenization of game technology across Microsoft's studios, reducing technical diversity and innovation. It also raises concerns about industry consolidation, as Epic Games' Unreal Engine gains even more dominance. The layoffs specifically targeted the team responsible for idTech, the engine powering games like Doom Eternal and the upcoming Indiana Jones and the Great Circle. No official statement from Microsoft has confirmed the exact number of affected employees.

hackernews · bauc · Jul 7, 15:33 · [Discussion](https://news.ycombinator.com/item?id=48819244)

**Background**: idTech is a series of proprietary game engines developed by id Software, known for pushing technical boundaries in first-person shooters. Historically, id Software open-sourced older engines under the GNU General Public License. The shift to Unreal Engine could affect future titles from id Software and other Microsoft studios.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech">id Tech - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_tech_5_engine">Id tech 5 engine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Id_Tech_7">id Tech 7 - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed strong criticism, arguing that Microsoft is sacrificing unique technical culture for cost-cutting and homogenization. Some noted that this could strengthen Epic's monopoly on game engines, while others questioned the lack of evidence in the original article.

**Tags**: `#game engines`, `#Microsoft`, `#id Software`, `#corporate strategy`, `#industry consolidation`

---

<a id="item-6"></a>
## [Astro 7.0 Launches with Rust-Based Compiler](https://astro.build/blog/astro-7/) ⭐️ 8.0/10

Astro 7.0 introduces a Rust-based compiler and Markdown pipeline, reducing dependencies from 247 in v6 to 190 in v7. This shift to Rust improves build performance and reduces dependency complexity, setting a trend for the JavaScript ecosystem to move toward more efficient, lower-overhead tooling. The Rust compiler and Markdown pipeline were contributed by community member Princesseuh. Astro remains a static site generator that supports multiple UI frameworks and can also produce dynamic server-rendered pages.

hackernews · saikatsg · Jul 7, 18:30 · [Discussion](https://news.ycombinator.com/item?id=48821653)

**Background**: Astro is a web framework for content-driven websites, known for its lightweight output and support for multiple UI frameworks. It started as a static site generator but now also supports server-side rendering. The use of Rust for tooling follows a broader trend in the web ecosystem, as seen with tools like SWC and Turbopack.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/withastro/astro">GitHub - withastro/astro: The web framework for content-driven websites. ⭐️ Star to support our work!</a></li>
<li><a href="https://dev.to/tylerlwsmith/first-impressions-of-astro-what-i-liked-and-disliked-22nj">First impressions of Astro: what I liked and disliked - DEV Community</a></li>

</ul>
</details>

**Discussion**: Community members praised the dependency reduction and performance improvements. Some expressed concerns about breaking changes across major versions, while others appreciated Astro's simplicity for building static sites with modern tooling.

**Tags**: `#web development`, `#astro`, `#rust`, `#javascript`, `#framework`

---

<a id="item-7"></a>
## [sqlite-utils 4.0 Introduces Schema Migrations](https://simonwillison.net/2026/Jul/7/sqlite-utils-4/#atom-everything) ⭐️ 8.0/10

sqlite-utils 4.0, released on July 7, 2026, adds database schema migrations, nested transactions via db.atomic(), and support for compound foreign keys. This major version addresses long-standing pain points for SQLite users, providing a structured migration system that simplifies schema evolution and enhances data integrity with compound foreign keys. Migrations are defined in Python files using the Migrations class and the table.transform() method, which implements SQLite's recommended pattern for complex schema changes. The release also includes breaking changes detailed in an upgrade guide.

rss · Simon Willison · Jul 7, 19:32

**Background**: sqlite-utils is a Python library and CLI tool for manipulating SQLite databases. Schema migrations allow developers to apply incremental changes to database schemas while tracking which changes have been applied, which is essential for production database management.

<details><summary>References</summary>
<ul>
<li><a href="https://sqlite-utils.datasette.io/en/latest/changelog.html">Changelog - sqlite-utils</a></li>
<li><a href="https://github.com/simonw/sqlite-migrate">GitHub - simonw/sqlite-migrate: A simple database migration system for SQLite, based on sqlite-utils · GitHub</a></li>
<li><a href="https://github.com/simonw/sqlite-utils/issues/117">Support for compound (composite) foreign keys · Issue #117 · simonw/sqlite-utils</a></li>

</ul>
</details>

**Tags**: `#sqlite`, `#python`, `#database`, `#migrations`, `#open source`

---

<a id="item-8"></a>
## [Tencent Releases Hy3: 295B MoE Model with 21B Active Parameters](https://simonwillison.net/2026/Jul/6/hy3/#atom-everything) ⭐️ 8.0/10

Tencent has released Hy3, a 295B-parameter Mixture-of-Experts (MoE) model with 21B active parameters and 3.8B MTP layer parameters, available under the Apache 2.0 license. It outperforms similar-size models and rivals flagship open-source models with 2-5x more parameters. Hy3 demonstrates that efficient MoE architectures can achieve competitive performance with much fewer active parameters, potentially lowering the cost of deploying large language models. Its permissive license and availability on OpenRouter (free until July 21) make it accessible to a wide range of developers and researchers. The full model is 598GB on Hugging Face, with an FP8 quantized version at 300GB, and supports a context length of 256K tokens. It was developed by the Tencent Hy Team and incorporates feedback from over 50 products during its preview phase.

rss · Simon Willison · Jul 6, 23:57

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that uses multiple specialized sub-networks (experts) and a gating mechanism to activate only a subset of experts per input token, enabling larger total parameters with lower computational cost. MTP (Multi-Token Prediction) is a technique where a lightweight drafter model predicts multiple future tokens to accelerate inference. FP8 quantization reduces model size and speeds up inference by storing weights in 8-bit floating-point format.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://arxiv.org/abs/2208.09225">[2208.09225] FP8 Quantization: The Power of the Exponent</a></li>
<li><a href="https://ai.google.dev/gemma/docs/mtp/mtp">Gemma 4 Multi-Token Prediction (MTP) using Hugging Face ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#LLM`, `#MoE`, `#Tencent`

---

<a id="item-9"></a>
## [GitHub Repo Leaks System Prompts of Major AI Chatbots](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 8.0/10

A GitHub repository named 'system_prompts_leaks' has been collecting and publishing the hidden system prompts of major AI chatbots including Claude, ChatGPT, Gemini, Grok, and others, with regular updates as of July 2026. This leak provides unprecedented transparency into the secret instructions that govern AI behavior, enabling researchers, developers, and users to understand and audit how these models are constrained and directed. The repository includes prompts from Claude Fable 5, Opus 4.8, ChatGPT 5.5 Thinking, GPT 5.5 Codex, Gemini 3.5 Flash, and many more, with diffs showing changes between versions. It has been featured in The Washington Post.

rss · GitHub Trending - Daily (All) · Jul 7, 22:54

**Background**: System prompts are hidden instructions that define an AI chatbot's behavior, personality, and constraints. They are typically kept secret by companies to prevent manipulation. System prompt leakage occurs when users coax the model into revealing these instructions, often through prompt injection techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly. · GitHub</a></li>
<li><a href="https://learn.snyk.io/lesson/llm-system-prompt-leakage/">System prompt leakage in LLMs | Tutorial and examples | Snyk Learn</a></li>
<li><a href="https://www.hexnode.com/blogs/explained/what-is-system-prompt-leakage/">What is System prompt leakage? - Hexnode Blogs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#system prompts`, `#reverse engineering`, `#LLM`, `#open source`

---

<a id="item-10"></a>
## [Addy Osmani Releases Agent Skills for AI Coding Agents](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released agent-skills, a GitHub repository containing 24 production-grade engineering skills packaged as slash commands for AI coding agents to follow consistent workflows and best practices. This addresses a critical gap where AI agents often skip engineering processes, leading to technical debt; by embedding senior engineer workflows into agents, it can significantly improve code quality and development consistency. The skills include commands like /spec, /plan, /build, /test, /review, /webperf, /code-simplify, and /ship, with an auto mode that generates plans and implements tasks autonomously after approval. They are inspired by Google's engineering culture, incorporating concepts like Hyrum's Law and the test pyramid.

rss · GitHub Trending - Daily (All) · Jul 7, 22:54

**Background**: AI coding agents like Claude Code, Cursor, and Copilot can generate code but often lack structured engineering discipline. Agent-skills packages workflows from senior engineers into reusable skills that agents can execute via slash commands, enforcing best practices across the development lifecycle.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub</a></li>
<li><a href="https://dev.to/vikrant_bagal_afae3e25ca7/production-grade-engineering-skills-for-ai-coding-agents-56nb">Production-Grade Engineering Skills for AI Coding Agents - DEV Community</a></li>
<li><a href="https://dev.to/_46ea277e677b888e0cd13/agent-skills-19-production-grade-skills-that-make-ai-coding-agents-work-like-senior-engineers-5bi9">agent-skills: 19 Production-Grade Skills That Make AI Coding Agents Work Like Senior Engineers - DEV Community</a></li>

</ul>
</details>

**Discussion**: The community has responded positively, with discussions on DEV and Hacker News praising the project for addressing a real need. Some users noted the potential for customization and integration with existing tools, while others expressed interest in seeing more domain-specific skills.

**Tags**: `#AI agents`, `#software engineering`, `#best practices`, `#developer tools`

---

<a id="item-11"></a>
## [RuView: WiFi-Based Spatial Intelligence Without Cameras](https://github.com/ruvnet/RuView) ⭐️ 8.0/10

RuView is an open-source platform that uses commodity WiFi signals to perform real-time spatial intelligence, vital sign monitoring, and presence detection, all without cameras or wearables. This technology could revolutionize smart homes and privacy-sensitive environments by enabling non-intrusive sensing through walls and in darkness, with seamless integration into major smart home ecosystems like Home Assistant, Apple Home, and Google Home. RuView uses a $9 ESP32 board to capture WiFi channel state information (CSI) and a pretrained model (ruvnet/wifi-densepose-pretrained) to infer 21 entities per node, including raw signals and semantic states like 'someone-sleeping' or 'fall-risk-elevated'.

rss · GitHub Trending - Daily (All) · Jul 7, 22:54

**Background**: WiFi sensing leverages the fact that WiFi signals are affected by objects and people in their path. By analyzing changes in channel state information (CSI), it is possible to detect motion, breathing, and even heart rate. RuView builds on this principle, using machine learning to extract high-level spatial intelligence from CSI data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WiFi_Sensing">WiFi Sensing - Wikipedia</a></li>
<li><a href="https://github.com/ruvnet/RuView">GitHub - ruvnet/RuView: π RuView turns commodity WiFi signals into real-time spatial intelligence, vital sign monitoring, and presence detection — all without a single pixel of video.</a></li>
<li><a href="https://github.com/davidakpele/wifi-densepose">GitHub - davidakpele/wifi-densepose: Production-ready implementation of InvisPose - a revolutionary WiFi-based dense human pose estimation system that enables real-time full-body tracking through walls using commodity mesh routers · GitHub</a></li>

</ul>
</details>

**Tags**: `#WiFi sensing`, `#spatial intelligence`, `#vital sign monitoring`, `#smart home`, `#privacy`

---

<a id="item-12"></a>
## [nanoGPT: Simple, Fast GPT Training Repo by Karpathy](https://github.com/karpathy/nanoGPT) ⭐️ 8.0/10

Andrej Karpathy's nanoGPT repository provides a minimal, efficient implementation for training and finetuning medium-sized GPT models, reproducing GPT-2 (124M) on a single 8XA100 node in about 4 days. The codebase consists of only ~300 lines for training and ~300 lines for the model definition. nanoGPT lowers the barrier for researchers and enthusiasts to experiment with GPT architectures, enabling rapid prototyping and educational exploration. Its simplicity and performance make it a valuable resource for the deep learning community. The repository includes a character-level Shakespeare example that trains in about 3 minutes on an A100 GPU. It supports loading pretrained GPT-2 weights from OpenAI and can be easily hacked for custom needs.

rss · GitHub Trending - Python · Jul 7, 22:55

**Background**: GPT (Generative Pre-trained Transformer) is a type of large language model developed by OpenAI, known for its ability to generate coherent text. nanoGPT is a rewrite of Karpathy's earlier minGPT, focusing on efficiency over education. The repository uses PyTorch and relies on datasets like OpenWebText for training.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/karpathy/nanogpt">GitHub - karpathy/nanoGPT: The simplest, fastest repository for training/finetuning medium-sized GPTs. · GitHub</a></li>
<li><a href="https://github.com/karpathy/minGPT">GitHub - karpathy/minGPT: A minimal PyTorch re-implementation ...</a></li>
<li><a href="https://github.com/jcpeterson/openwebtext">GitHub - jcpeterson/openwebtext: Open clone of OpenAI's ...</a></li>

</ul>
</details>

**Discussion**: The community widely praises nanoGPT for its clarity and performance, with many using it as a starting point for GPT experiments. Some users note that the repository is now deprecated in favor of nanochat, but it remains a popular educational tool.

**Tags**: `#GPT`, `#training`, `#deep learning`, `#NLP`, `#open source`

---

<a id="item-13"></a>
## [Anthropic releases financial services AI agents](https://github.com/anthropics/financial-services) ⭐️ 8.0/10

Anthropic released a set of reference agents, skills, and data connectors for financial services workflows, available as Claude Cowork plugins or via the Claude Managed Agents API. This release provides ready-to-use AI agents for high-value financial tasks like pitch decks and market research, enabling faster adoption of AI in regulated industries with flexible deployment options. The repository includes agents such as Pitch Agent, Market Researcher, and GL Reconciler, each shipping as both a Cowork plugin and a Managed Agent template. All outputs require human sign-off and do not execute transactions.

rss · GitHub Trending - Python · Jul 7, 22:55

**Background**: Claude Cowork is Anthropic's collaborative workspace where plugins extend Claude's capabilities. Claude Managed Agents API provides a hosted infrastructure for running autonomous agents. These agents target investment banking, equity research, private equity, and wealth management workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/finance-agents">Agents for financial services \ Anthropic</a></li>
<li><a href="https://support.claude.com/en/articles/13837440-use-plugins-in-claude">Use plugins in Claude | Claude Help Center</a></li>
<li><a href="https://platform.claude.com/docs/en/managed-agents/overview">Claude Managed Agents overview - Claude Platform Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#financial services`, `#Anthropic`, `#Claude`, `#agents`

---

<a id="item-14"></a>
## [iFLYTEK Unveils Unified Multimodal Foundation Model for Embodied AI](https://arxiv.org/abs/2607.02542) ⭐️ 8.0/10

iFLYTEK-Embodied-Omni is a unified multimodal foundation model that jointly models vision, language, and action within a single framework, using shared multimodal self-attention to enable brain-cerebellum collaboration for embodied agents. This approach addresses key limitations of cascaded pipelines in embodied AI by eliminating interface bottlenecks and reducing compound prediction errors, potentially advancing general-purpose robotics and autonomous systems. The model comprises three components: a vision-language model (VLM), a video generation model (VGM), and an action generation model (AGM), trained in a four-stage strategy on a comprehensive dataset combining action-annotated and action-free embodied videos.

rss · arXiv - AI · Jul 7, 04:00

**Background**: Embodied agents are intelligent systems that interact with the physical world through a body, such as robots. Multimodal foundation models integrate multiple data types (e.g., vision, language) to enable general-purpose understanding and reasoning. The brain-cerebellum analogy in AI separates high-level planning (brain) from low-level motor control (cerebellum), a concept explored in recent embodied AI research.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_agent">Embodied agent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#multimodal learning`, `#foundation model`, `#robotics`, `#vision-language-action`

---

<a id="item-15"></a>
## [Internal Pluralism Challenges Pairwise Comparisons](https://arxiv.org/abs/2607.02672) ⭐️ 8.0/10

A new paper formalizes the concept of internal pluralism, showing that local pairwise comparisons can fail to capture global priorities like proportionality and egalitarianism in decision rule learning. This challenges fundamental assumptions in participatory design and AI alignment, potentially reshaping how we elicit and model human preferences for automated decision-making. The paper identifies two failures: global priorities cannot be captured locally, and forced comparisons can cause behavioral distortions due to internal conflict. It suggests allowing indecision reduces the number of queries needed.

rss · arXiv - AI · Jul 7, 04:00

**Background**: Pairwise comparisons are commonly used in preference learning and social choice to infer how people want decision rules to behave. Internal pluralism refers to an individual holding multiple authoritative priorities that may conflict. This work bridges social choice theory and AI alignment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Egalitarianism">Egalitarianism - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pluralism_(political_theory)">Pluralism (political theory) - Wikipedia</a></li>
<li><a href="https://proceedings.mlr.press/v238/tatli24a.html">Learning Populations of Preferences via Pairwise Comparison ...</a></li>

</ul>
</details>

**Tags**: `#AI alignment`, `#participatory design`, `#social choice theory`, `#preference learning`, `#pluralism`

---

<a id="item-16"></a>
## [REDI: Open-Source Framework Automates Scientific Data Readiness](https://arxiv.org/abs/2607.02771) ⭐️ 8.0/10

Researchers introduced REDI, an open-source framework that automates the transformation of raw scientific datasets into AI-ready data through a five-stage pipeline with provenance tracking and FAIR compliance, demonstrated across climate, proteomics, materials science, and nuclear fusion. REDI addresses a critical bottleneck in scientific AI by unifying automated data transformation, readiness assessment, provenance tracking, and agent-native deployment, potentially accelerating AI-driven discoveries across multiple scientific domains. REDI's pipeline includes ingest, preprocess, transform, structure, and output stages, with per-stage instrumentation for reproducibility; its companion tool SetGo automates FAIR compliance and catalog publication. Preliminary results show near-ideal parallel scaling to 100 nodes on Frontier for climate data.

rss · arXiv - AI · Jul 7, 04:00

**Background**: Scientific datasets from leadership computing facilities often require substantial transformation before they can be used for AI training, but existing tools lack a unified approach. FAIR (Findable, Accessible, Interoperable, Reusable) principles guide data management to ensure long-term usability. REDI aims to fill this gap by providing a comprehensive, automated pipeline.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02771">[2607.02771] Automated Data Readiness for Scientific AI</a></li>
<li><a href="https://arxiv.org/html/2607.02771">Automated Data Readiness for Scientific AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/FAIR_data">FAIR data - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#scientific AI`, `#data readiness`, `#provenance`, `#FAIR`, `#HPC`

---

<a id="item-17"></a>
## [SwarmResearch: Multi-Agent Orchestration for Open-Ended Discovery](https://arxiv.org/abs/2607.02807) ⭐️ 8.0/10

SwarmResearch introduces a shepherd-subagent architecture where a Shepherd Agent uses global context to steer a population of Search Agents operating in separate git branches, improving exploration diversity in long-running coding agents. This approach addresses a key limitation of existing long-running coding agents that tend to converge on a single approach, and achieves better or comparable solutions on 13/15 open-ended optimization tasks compared to state-of-the-art methods. SwarmResearch's orchestrator-guided scaling adapts parallelism at different search depths, outperforming fixed scaling of serial and parallel agents. The system is evaluated on open-ended optimization tasks against LLM-guided evolution and multi-agent baselines.

rss · arXiv - AI · Jul 7, 04:00

**Background**: Long-running coding agents like AutoResearch can persistently discover optimizations but often converge to a single high-level approach, missing superior alternatives. This is partly due to accumulating context in a single agent and exposing only one program state for editing. SwarmResearch's shepherd-subagent architecture mitigates this by maintaining global context for the shepherd and local context for each search agent.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.11446">LLM Guided Evolution -- The Automation of Models Advancing Models LLM Guided Evolution - The Automation of Models Advancing Models clint-kristopher-morris/llm-guided-evolution - GitHub LLM Guided Evolution - The Automation of Models Advancing Models Paper page - LLM Guided Evolution -- The Automation of Models ... LLM-Guided Evolution: An Autonomous Model Optimization for ... GitHub - llm-inference-aad/llm-inference: LLM Guided ...</a></li>
<li><a href="https://github.com/karpathy/autoresearch">GitHub - karpathy/autoresearch: AI agents running research on ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#LLM agents`, `#code generation`, `#evolutionary optimization`, `#software engineering`

---

<a id="item-18"></a>
## [OCM: Object-Centric Environment Modeling for LLM Agents](https://arxiv.org/abs/2607.02846) ⭐️ 8.0/10

Researchers propose Object-Centric Environment Modeling (OCM), which organizes agent experience into executable object and procedure knowledge bases, achieving the best average rank across benchmarks and reducing invalid actions. OCM addresses key limitations of symbolic memory for LLM agents by using executable code bases with online verification, potentially improving agent reliability and reusability in complex environments. OCM maintains two connected code bases: object knowledge (Python classes for entities and mechanisms) and procedure knowledge (reusable interaction patterns). It operates online, updating and verifying both bases after each episode, and uses progressive knowledge disclosure to inspect code signatures before reading full source.

rss · arXiv - AI · Jul 7, 04:00

**Background**: LLM agents often use free-form textual memory to store experience, but this becomes hard to maintain and reuse. Symbolic approaches learn executable skills or world models, but they may store local procedures or assume simplified dynamics. OCM builds an object-centric executable model that explicitly represents environment entities and their interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02846">Object-Centric Environment Modeling for Agentic Tasks</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#symbolic memory`, `#environment modeling`, `#object-centric`, `#code generation`

---

<a id="item-19"></a>
## [Oyster-II: RL-Based Constructive Safety Alignment for LLMs](https://arxiv.org/abs/2607.02914) ⭐️ 8.0/10

Oyster-II introduces a reinforcement learning (RL) framework for constructive safety alignment in large language models, addressing safety generalization failures and safety chain-of-thought over-generalization observed in supervised fine-tuning approaches. This work advances LLM safety by enabling models to handle sensitive queries constructively rather than refusing them, while maintaining helpfulness and trustworthiness, which is critical for real-world deployment. Oyster-II adopts a Zero-RL paradigm with a multi-stage RL strategy, and evaluations show it surpasses Qwen3-14B and Oyster-I on safety dimensions, achieving cross-scale performance comparable to Qwen3-Max and Qwen3.5-397B.

rss · arXiv - AI · Jul 7, 04:00

**Background**: Large language models (LLMs) often use refusal-oriented alignment to avoid generating harmful content, but this can fail to serve legitimate user needs. The constructive safety paradigm, pioneered by Oyster-I, aims to provide thoughtful, response-oriented safety rather than blanket refusal. However, Oyster-I's supervised fine-tuning (SFT) approach suffers from insufficient safety generalization and safety chain-of-thought over-generalization, where safety reasoning is applied too broadly to benign queries. Oyster-II overcomes these limitations by using reinforcement learning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.19672">[2507.19672] Alignment and Safety in Large Language Models: Safety Mechanisms, Training Paradigms, and Emerging Challenges</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#safety alignment`, `#reinforcement learning`, `#AI safety`

---

<a id="item-20"></a>
## [VERITAS: A General-Purpose Replication Tool for Science](https://arxiv.org/abs/2607.02931) ⭐️ 8.0/10

Researchers introduced VERITAS, a domain-agnostic replication framework that uses CLI coding agents to automatically extract claims from a paper, run experiments, and produce a weighted Replication Score along with a log of fixes and a patched codebase. VERITAS addresses the replication crisis in science by automating the costly and slow manual verification process, enabling scalable and objective reproducibility checks across disciplines like computer science, social science, medicine, and astrophysics. VERITAS achieved state-of-the-art performance on CORE-Bench and ReplicationBench, outperforming two strong Claude Code baselines on every metric across 65 papers. The framework is built around CLI coding agents, which have direct filesystem and shell access, allowing autonomous issue resolution.

rss · arXiv - AI · Jul 7, 04:00

**Background**: The replication crisis refers to the widespread failure to reproduce scientific findings, with studies showing that roughly half of social science papers cannot be replicated. Manual replication is slow and expensive, prompting the use of AI coding agents to automate parts of the process. CLI coding agents are AI tools that run in the terminal and can autonomously read, write, and execute code, making them suitable for automating research verification.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02931">VERITAS: Towards a General-Purpose Replication Tool for ...</a></li>
<li><a href="https://github.com/bradAGI/awesome-cli-coding-agents">GitHub - bradAGI/awesome-cli-coding-agents: Curated directory of terminal-native AI coding agents and the harnesses that orchestrate them. Covers open-source tools (Pi, OpenCode, Aider, Goose), platform agents (Claude Code, Codex, Gemini CLI), parallel runners, autonomous loops, and agent infrastructure. · GitHub</a></li>
<li><a href="https://www.science.org/content/article/across-social-sciences-half-research-doesn-t-replicate">Across the social sciences, half of research doesn’t replicate | Science | AAAS</a></li>

</ul>
</details>

**Tags**: `#reproducibility`, `#AI agents`, `#scientific computing`, `#automation`, `#research tools`

---

<a id="item-21"></a>
## [Five Failure Modes in AI Safety Benchmark Audits](https://arxiv.org/abs/2607.02586) ⭐️ 8.0/10

A new paper identifies five failure modes (F1–F5) in perturbation-based construct-validity audits for AI safety benchmarks, demonstrating through a case study that common audit practices can produce non-confirmatory results. This work exposes critical vulnerabilities in audit methodologies used for AI safety evaluation, which could undermine trust in governance frameworks that rely on such audits. It calls for more rigorous due-diligence protocols to ensure audit conclusions are reliable. The paper proposes a six-point due-diligence gate as a withholding and disclosure protocol for assurance-grade evidence, but notes it is not a route to benchmark-validity verdicts. The case study uses two open-weight instruction-tuned models and five safety benchmarks.

rss · arXiv - Machine Learning · Jul 7, 04:00

**Background**: Perturbation-based construct-validity audits are a common method to evaluate whether AI safety benchmarks actually measure what they claim. These audits involve systematically altering inputs to test model robustness. The paper argues that implementation details invisible in reported numbers can silently manufacture audit conclusions, leading to false confidence.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-025-09538-2.pdf">A comprehensive analysis of perturbation methods in ...</a></li>
<li><a href="https://futureoflife.org/ai-safety-index-summer-2025/">AI Safety Index: Summer 2025 - Future of Life Institute</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#benchmark auditing`, `#AI governance`, `#evaluation methodology`

---

<a id="item-22"></a>
## [GRAFT: Per-Word Pronunciation Control in Zero-Shot TTS](https://arxiv.org/abs/2607.02633) ⭐️ 8.0/10

GRAFT introduces a per-word pronunciation conditioning mechanism for zero-shot text-to-speech, allowing a short spoken sample to control the pronunciation of a specific word while preserving the target voice. This addresses a key limitation of existing TTS systems that mispronounce rare proper nouns, loanwords, and technical terms, improving pronunciation accuracy without sacrificing speaker similarity or naturalness. GRAFT uses voice conversion during training-data construction to disentangle the hint speaker from the target speaker, so the pronunciation hint can come from any voice. In a blind English listening study, human raters ranked GRAFT first by a clear margin.

rss · arXiv - Machine Learning · Jul 7, 04:00

**Background**: Zero-shot TTS systems like VALL-E use neural codec language modeling to synthesize speech in a target voice from text alone, but they inherit text ambiguity and often mispronounce uncommon words. Phoneme-conditioned models offer some control but lack direct acoustic handles for per-word pronunciation. GRAFT bridges this gap by conditioning on a short audio sample of the target word.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2301.02111">[2301.02111] Neural Codec Language Models are Zero-Shot Text to Speech Synthesizers</a></li>
<li><a href="https://arxiv.org/abs/2407.05407">CosyVoice: A Scalable Multilingual Zero-shot Text-to-speech ... Zero-Shot TTS | VoiceBox GitHub - zai-org/GLM-TTS: GLM-TTS: Controllable & Emotion ... MaskGCT: Zero-Shot Text-to-Speech with Masked Generative ... Home | VoiceBox OmniVoice: Free AI Voice Generator & Voice Cloning</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#pronunciation control`, `#zero-shot TTS`, `#speech synthesis`, `#neural codec`

---

<a id="item-23"></a>
## [Risk Aversion Generalization in LLMs Across 98 Orders of Magnitude](https://arxiv.org/abs/2607.02755) ⭐️ 8.0/10

Researchers introduced RiskAverseOOD, a benchmark to test whether risk aversion trained on low-stakes gambles generalizes to astronomically high stakes, and found that Qwen3-8B's risk aversion partially generalizes across 98 orders of magnitude. This work addresses a critical AI safety problem: if misaligned AIs are risk-averse, they may prefer cooperation over rebellion, limiting potential harm. Demonstrating that risk aversion can generalize OOD is a promising step toward reliable AI failsafes. Using SFT, DPO, and activation steering, the team induced risk aversion in Qwen3-8B, achieving 70%, 52%, and 39% rates of choosing the safe 'Cooperate' option respectively, up from a 2% baseline. The effects replicated across model sizes and families including Gemma-3-12B-IT and Llama-3.1-8B-Instruct.

rss · arXiv - Machine Learning · Jul 7, 04:00

**Background**: Out-of-distribution (OOD) generalization refers to a model's ability to perform well on data from a distribution different from its training distribution. In AI safety, training models to be risk-averse on low-stakes scenarios is feasible, but ensuring that this behavior holds for extremely high-stakes situations is crucial for preventing catastrophic outcomes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2108.13624">[2108.13624] Towards Out-Of-Distribution Generalization: A Survey</a></li>
<li><a href="https://github.com/QwenLM/Qwen3">GitHub - QwenLM/Qwen3: Qwen3 is the large language model ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#risk aversion`, `#out-of-distribution generalization`, `#alignment`, `#language models`

---

<a id="item-24"></a>
## [Why LLMs Fail at CBT-Guided Affective Reasoning](https://arxiv.org/abs/2607.02885) ⭐️ 8.0/10

A new paper investigates why large language models (LLMs) score up to 96% on CBT licensing exams but fail to apply CBT effectively in therapy dialogues, and proposes a knowledge-guided framework using Beck's Cognitive Conceptualization, SNOMED CT concepts, and Multiple Chain-of-Thought (MCoT) prompting. This work highlights a critical gap between theoretical knowledge and practical application of LLMs in mental health, providing a metric (Protocol Leverage Force) to measure behavioral change and guiding the development of more effective AI therapy tools. The framework decomposes user narratives into Beck's Cognitive Conceptualization structure, grounds them in clinical SNOMED CT concepts validated via Natural Language Inference, and uses MCoT to select among three therapeutic strategies: Validation & Reflection, Socratic Questioning, or Alternative Perspectives.

rss · arXiv - NLP · Jul 7, 04:00

**Background**: Cognitive Behavioral Therapy (CBT) is a structured psychotherapy that examines interactions between thoughts, feelings, and behaviors. Beck's Cognitive Conceptualization is a framework for understanding a client's core beliefs and automatic thoughts. SNOMED CT is a comprehensive clinical terminology system. Chain-of-Thought prompting encourages step-by-step reasoning in LLMs, and MCoT extends this to multiple reasoning paths.

<details><summary>References</summary>
<ul>
<li><a href="https://beckinstitute.org/about/understanding-cbt/">Understanding CBT - Beck Institute</a></li>
<li><a href="https://en.wikipedia.org/wiki/SNOMED_CT">SNOMED CT - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2503.12605">[2503.12605] Multimodal Chain-of-Thought Reasoning: A Comprehensive Survey</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Cognitive Behavioral Therapy`, `#affective reasoning`, `#mental health`, `#knowledge-guided AI`

---

<a id="item-25"></a>
## [Decision framework for cross-habitat marine species recognition](https://arxiv.org/abs/2607.02559) ⭐️ 8.0/10

A study quantifies the trade-off between labeling effort and recognition accuracy for transferring vision systems across marine habitats, proposing a decision framework that recommends using frozen DINOv2 with a linear classifier and only 10-20 labeled images per species. This framework provides ecologists with evidence-based guidance to deploy reliable automated recognition at new sites with minimal annotation effort, potentially reducing labeling costs by an order of magnitude and accelerating large-scale marine monitoring. The benchmark spans five datasets, three oceans, and three taxonomic groups (fish, corals, invertebrates), evaluating four models (DINOv2, CLIP, ResNet-50, EfficientNet-B4) under four adaptation strategies across 968 runs. Frozen DINOv2 with a linear classifier (1,538 trainable parameters) matched or outperformed fully fine-tuned convolutional baselines four orders of magnitude larger.

rss · arXiv - Computer Vision · Jul 7, 04:00

**Background**: Automated image recognition is increasingly used in ecology to scale monitoring, but deploying models at new sites typically requires extensive labeled data. Transfer learning and few-shot learning aim to reduce this burden by adapting pre-trained models with minimal new labels. DINOv2 is a self-supervised vision foundation model that learns robust features without labels, while LoRA and Visual Prompt Tuning are parameter-efficient fine-tuning methods.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/facebookresearch/dinov2">GitHub - facebookresearch/dinov2: PyTorch code and models for the DINOv2 self-supervised learning method. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/LoRA_(machine_learning)">LoRA (machine learning) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2203.12119">[2203.12119] Visual Prompt Tuning - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#computer vision`, `#ecology`, `#transfer learning`, `#few-shot learning`, `#marine biology`

---

<a id="item-26"></a>
## [CORA: Per-Slice Coherent Orthogonal Rotation for SVD-Based Low-Rank Adaptation](https://arxiv.org/abs/2607.02576) ⭐️ 8.0/10

Researchers introduced CORA (Coherent Orthogonal Rotation Adaptation), a new parameter-efficient fine-tuning method that applies per-slice orthogonal rotations and diagonal scaling to SVD-based low-rank adaptation, preserving the coupled geometry of pretrained singular bases. CORA achieves superior performance on commonsense reasoning and code generation tasks while using about 8× fewer parameters than LoRA, making it a highly efficient alternative for fine-tuning large models. CORA uses only ½ m (r−1) trainable parameters per linear layer, roughly 4× fewer than LoRA at the same rank, and outperforms LoRA, DoRA, PiSSA, and MiLoRA on benchmarks.

rss · arXiv - Data Science & Statistics · Jul 7, 04:00

**Background**: Parameter-efficient fine-tuning (PEFT) methods like LoRA adapt pretrained models with low-rank updates, but they often ignore the coupled geometry between left and right singular bases. Recent minimum-perturbation theory suggests that stable fine-tuning follows a coherent SVD rotation, where a single orthogonal matrix acts on both bases. CORA extends this idea to a per-slice level, enabling more efficient and theoretically grounded adaptation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.02576v1">CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based ...</a></li>
<li><a href="https://zliu-math.github.io/assets/pdf/FW_LoRA_NeurIPS_2026.pdf">CORA: Per-Slice Coherent Orthogonal Rotation for SVD-based ...</a></li>

</ul>
</details>

**Tags**: `#parameter-efficient fine-tuning`, `#low-rank adaptation`, `#singular value decomposition`, `#orthogonal rotation`, `#machine learning`

---

<a id="item-27"></a>
## [Benign Overfitting Impossible in Diffusion Models](https://arxiv.org/abs/2607.02671) ⭐️ 8.0/10

A new paper proves that benign overfitting and double descent cannot occur in diffusion models, showing that overfitting and good generalization cannot coexist unless sample size grows exponentially with data dimension. This challenges a widely held assumption that diffusion models, like other deep learning models, benefit from benign overfitting, and reveals that generalization in generative models follows fundamentally different mechanisms, motivating new theoretical developments. The paper identifies that regression benefits from alignment between target and empirical covariance, while score matching in diffusion models lacks such alignment, making overfitting irreparably harmful. Implicit regularization from time-smoothness and early stopping can prevent overfitting.

rss · arXiv - Data Science & Statistics · Jul 7, 04:00

**Background**: Benign overfitting is a phenomenon where overparameterized models fit noisy training data perfectly yet still generalize well, challenging classical bias-variance tradeoff. Double descent describes a test error curve that first decreases, then increases, then decreases again as model complexity grows. Diffusion models generate data by reversing a noise process, using score matching to estimate gradients of the data distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Overfitting">Overfitting - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Double_descent">Double descent - Wikipedia</a></li>
<li><a href="https://fanpu.io/blog/2023/score-based-diffusion-models/">Score-Based Diffusion Models | Fan Pu Zeng</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#generalization`, `#overfitting`, `#deep learning theory`, `#score matching`

---

<a id="item-28"></a>
## [Sequential Correlations Change In-Context Learning](https://arxiv.org/abs/2607.03660) ⭐️ 8.0/10

This paper extends in-context learning (ICL) theory to sequentially correlated prompts, showing that correlations induce an effective context length and reduce test error for correlated queries. Real-world data often exhibits sequential correlations, so this work bridges a gap between ICL theory and practical scenarios, and reveals that softmax attention may be better matched to correlated tasks than linear attention. The authors present a solvable linear attention model and validate predictions on realistic transformers, identifying two distinct effects: within-context correlations shorten effective context length, and query-context correlations reduce test error.

rss · arXiv - Data Science & Statistics · Jul 7, 04:00

**Background**: In-context learning (ICL) allows transformers to perform new tasks using only examples in the prompt without parameter updates. Prior theoretical work on ICL often assumed independent and identically distributed (i.i.d.) prompt examples, which is unrealistic for sequential data like text or time series.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.05200">[2506.05200] Transformers Meet In-Context Learning: A ... [2212.07677] Transformers learn in-context by gradient descent Understanding in-context learning in transformers | ICLR ... Trained Transformers Learn Linear Models In-Context In-context Learning and Induction Heads In-Context Convergence of Transformers - yuhuang42.org In-Context Learning with Representations: Contextual ...</a></li>
<li><a href="https://arxiv.org/abs/2212.07677">[2212.07677] Transformers learn in-context by gradient descent Understanding in-context learning in transformers | ICLR ... Trained Transformers Learn Linear Models In-Context In-context Learning and Induction Heads In-Context Convergence of Transformers - yuhuang42.org In-Context Learning with Representations: Contextual ...</a></li>
<li><a href="https://iclr-blogposts.github.io/2024/blog/understanding-icl/">Understanding in-context learning in transformers | ICLR ...</a></li>

</ul>
</details>

**Tags**: `#in-context learning`, `#transformers`, `#linear regression`, `#sequence models`, `#theory`

---

<a id="item-29"></a>
## [RoBAS: Robust Bayes-Assisted Conformal Prediction](https://arxiv.org/abs/2607.04236) ⭐️ 8.0/10

The paper introduces RoBAS (Robust Bayes-Assisted Shrinkage), a framework that constructs nonconformity scores for conformal prediction that adapt to the quality of the prior, improving efficiency under correct priors and maintaining robustness under misspecified ones. This work addresses a key limitation of Bayes-assisted conformal prediction—degradation under prior misspecification—making it more practical for real-world applications where priors may be imperfect, thereby enhancing reliability of uncertainty quantification in AI systems. RoBAS has two instantiations: one using a heavy-tailed Bayesian working model and a closed-form empirical Bayes shrinkage score. When the prior is unreliable, the scores revert to the Distance-To-Average (DTA) score, a robust non-informative baseline.

rss · arXiv - Data Science & Statistics · Jul 7, 04:00

**Background**: Conformal prediction is a framework for uncertainty quantification that produces prediction sets with guaranteed coverage under exchangeability. It relies on nonconformity scores that measure how atypical a new point is relative to a calibration set. Bayes-assisted conformal prediction integrates Bayesian modeling to improve efficiency, but can suffer when the prior is misspecified.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/nonconformity-score">Nonconformity Score in Conformal Prediction</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#Bayesian inference`, `#robust statistics`, `#uncertainty quantification`, `#machine learning`

---

<a id="item-30"></a>
## [Optimal MoE Model Averaging for Conditional Generative Models](https://arxiv.org/abs/2607.04360) ⭐️ 8.0/10

The paper proposes an optimal model averaging framework for conditional generative models, introducing StaticMA with fixed weights and MoEMA, an input-adaptive mixture-of-experts method using maximum mean discrepancy. This framework allows practitioners to combine multiple conditional generative models without requiring tractable densities, improving performance across tabular, image, and text modalities, which is crucial for real-world applications where model selection is challenging. The methods are sample-based and use maximum mean discrepancy (MMD) to measure conditional distribution differences. MoEMA parameterizes input-dependent weights via a softmax neural-network gate and is proven asymptotically optimal.

rss · arXiv - Data Science & Statistics · Jul 7, 04:00

**Background**: Conditional generative models learn to sample from a target distribution given input conditions. Model averaging combines multiple models to improve robustness, but traditional methods often require density evaluation. Maximum mean discrepancy (MMD) is a kernel-based metric for comparing distributions without density estimation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.04360">[2607.04360] Optimal Mixture-of-Experts Model Averaging for ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kernel_embedding_of_distributions">Kernel embedding of distributions - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#generative models`, `#model averaging`, `#mixture of experts`, `#conditional distributions`, `#machine learning`

---