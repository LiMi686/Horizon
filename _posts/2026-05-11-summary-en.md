---
layout: default
title: "Horizon Summary: 2026-05-11 (EN)"
date: 2026-05-11
lang: en
---

> From 90 items, 38 important content pieces were selected

---

1. [Nvidia Releases CUDA-Oxide: Rust-to-CUDA Compiler](#item-1) ⭐️ 9.0/10
2. [HumanNet: One-Million-Hour Human-Centric Video Dataset](#item-2) ⭐️ 9.0/10
3. [Feedforward Neural Networks Have Finite Sample Complexity](#item-3) ⭐️ 9.0/10
4. [Developer returns to hand-written code, warns of AI cognitive debt](#item-4) ⭐️ 8.0/10
5. [AI may end software engineering as a lifetime career](#item-5) ⭐️ 8.0/10
6. [Mythos AI Finds Curl Vulnerability, Hype Questioned](#item-6) ⭐️ 8.0/10
7. [NYT Issues Editor's Note After AI-Generated Quote Published](#item-7) ⭐️ 8.0/10
8. [ByteDance Open-Sources Multimodal AI Agent Stack](#item-8) ⭐️ 8.0/10
9. [Agent Skills: Production-Grade Workflows for AI Coding Agents](#item-9) ⭐️ 8.0/10
10. [CloakBrowser: Stealth Chromium Passes All Bot Detection Tests](#item-10) ⭐️ 8.0/10
11. [GenericAgent: Self-Evolving Agent Grows Skill Tree from 3K-Line Seed](#item-11) ⭐️ 8.0/10
12. [Memori: Agent-Native Memory Infrastructure for LLMs](#item-12) ⭐️ 8.0/10
13. [GraphDC: Divide-and-Conquer Multi-Agent System for Graph Reasoning](#item-13) ⭐️ 8.0/10
14. [Longer Reasoning Chains Increase Position Bias in LLMs](#item-14) ⭐️ 8.0/10
15. [Spectral Diagnostic Detects Hidden Coalitions in Multi-Agent AI](#item-15) ⭐️ 8.0/10
16. [CASCADE: Case-Based Continual Adaptation for LLMs During Deployment](#item-16) ⭐️ 8.0/10
17. [LLM Agent Memory Evolution: Storage to Experience](#item-17) ⭐️ 8.0/10
18. [Weblica: Scalable Training Environments for Visual Web Agents](#item-18) ⭐️ 8.0/10
19. [SCALAR: Iterative Critique Boosts LLM Physics Reasoning](#item-19) ⭐️ 8.0/10
20. [RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory](#item-20) ⭐️ 8.0/10
21. [LKV: Learned KV Cache Eviction for Efficient LLM Inference](#item-21) ⭐️ 8.0/10
22. [PND: Training-Free Decoding Reduces VLM Hallucination](#item-22) ⭐️ 8.0/10
23. [Strain and Vorticity in Flow Matching Error](#item-23) ⭐️ 8.0/10
24. [Toeplitz MLP Mixer: Efficient Sub-Quadratic Sequence Model](#item-24) ⭐️ 8.0/10
25. [Germline-Absorbing Diffusion Improves Antibody Design](#item-25) ⭐️ 8.0/10
26. [Domain-level metacognitive monitoring in 33 LLMs](#item-26) ⭐️ 8.0/10
27. [IntentGrasp Benchmark Reveals LLM Intent Understanding Gaps](#item-27) ⭐️ 8.0/10
28. [Human-Centered LLM Framework Proposed](#item-28) ⭐️ 8.0/10
29. [LLMs Fail to Adjust to Retrieved Information Certainty](#item-29) ⭐️ 8.0/10
30. [Measure Transport Theory Explains Visual Text Compression](#item-30) ⭐️ 8.0/10
31. [LookWhen: Efficient Video Recognition via Token Selection](#item-31) ⭐️ 8.0/10
32. [Scaling Laws for Knowledge Transfer in 3D Medical Imaging](#item-32) ⭐️ 8.0/10
33. [HSA: Heterogeneous Step Allocation for Efficient Video DiTs](#item-33) ⭐️ 8.0/10
34. [Attention Mechanisms: Random Matrix Insights on Signal Recovery](#item-34) ⭐️ 8.0/10
35. [Neural Operator Learns Conditional Distributions from Any Joint Density](#item-35) ⭐️ 8.0/10
36. [Kernel Selection as Model Selection for MMD Tests](#item-36) ⭐️ 8.0/10
37. [Interpretable IRT Framework for Scalable LLM Evaluation](#item-37) ⭐️ 8.0/10
38. [TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching](#item-38) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nvidia Releases CUDA-Oxide: Rust-to-CUDA Compiler](https://nvlabs.github.io/cuda-oxide/index.html) ⭐️ 9.0/10

Nvidia Labs has released CUDA-oxide 0.1, an experimental Rust-to-CUDA compiler that compiles standard Rust code directly to PTX, enabling GPU kernel development in Rust without DSLs or foreign function bindings. This marks Nvidia's official foray into supporting Rust for GPU programming, potentially bringing Rust's memory safety and performance to CUDA development, which could significantly impact the GPU computing ecosystem by offering a safer alternative to CUDA C++. CUDA-oxide is a custom rustc backend that supports single-source compilation, meaning host and device code reside in the same file and are built with a single cargo oxide build command. It compiles Rust directly to PTX, the intermediate representation for NVIDIA GPUs.

hackernews · adamnemecek · May 11, 15:55 · [Discussion](https://news.ycombinator.com/item?id=48096692)

**Background**: CUDA is Nvidia's parallel computing platform and programming model for GPU acceleration, traditionally programmed in C++ with extensions. Rust is a systems programming language known for memory safety without garbage collection. CUDA-oxide aims to combine Rust's safety guarantees with CUDA's performance, though GPU kernel programming inherently involves unsafe operations due to hardware constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NVlabs/cuda-oxide">GitHub - NVlabs/cuda-oxide: cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.</a></li>
<li><a href="https://nvlabs.github.io/cuda-oxide/index.html">The cuda-oxide Book — cuda-oxide</a></li>
<li><a href="https://www.phoronix.com/news/NVIDIA-CUDA-Oxide-0.1">NVIDIA Releases CUDA-Oxide 0.1 For Experimental Rust-To-CUDA Compiler - Phoronix</a></li>

</ul>
</details>

**Discussion**: The community is excited about CUDA-oxide as a potential drop-in replacement for existing Rust CUDA crates, with interest in build time comparisons and the handling of Rust's memory model. Concerns were raised about overhead from Rust's safety features like bounds checks potentially increasing register usage and lowering kernel concurrency, as well as the ability to share structs between host and device.

**Tags**: `#CUDA`, `#Rust`, `#GPU Programming`, `#Compilers`, `#Nvidia`

---

<a id="item-2"></a>
## [HumanNet: One-Million-Hour Human-Centric Video Dataset](https://arxiv.org/abs/2605.06747) ⭐️ 9.0/10

Researchers introduced HumanNet, a one-million-hour human-centric video dataset with interaction-centric annotations including captions, motion descriptions, and hand/body signals, designed to scale embodied intelligence learning. This dataset provides a scalable and cost-effective alternative to robot-specific data for training embodied foundation models, potentially accelerating progress in human activity understanding, motion generation, and human-to-robot transfer. HumanNet spans both first-person and third-person perspectives, covering fine-grained activities, human-object interactions, tool use, and long-horizon behaviors. A validation experiment showed that continued training with 1000 hours of egocentric video from HumanNet outperformed training with 100 hours of real-robot data from Magic Cobot.

rss · arXiv - Computer Vision · May 11, 04:00

**Background**: Embodied intelligence aims to create AI systems that perceive and act in the physical world. While vision and language models have scaled using internet data, learning physical interaction has been limited by the lack of large, diverse, and richly annotated human activity datasets. HumanNet addresses this gap by curating unstructured internet video into a structured resource for embodied learning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://arxiv.org/abs/2412.00115">[2412.00115] OpenHumanVid: A Large-Scale High-Quality Dataset for Enhancing Human-Centric Video Generation</a></li>

</ul>
</details>

**Tags**: `#embodied intelligence`, `#human-centric video`, `#dataset`, `#human-object interaction`, `#motion learning`

---

<a id="item-3"></a>
## [Feedforward Neural Networks Have Finite Sample Complexity](https://arxiv.org/abs/2605.07097) ⭐️ 9.0/10

A new paper proves that any fixed feedforward neural network whose layers are definable in an o-minimal structure has finite sample complexity in the agnostic PAC model, covering MLPs, CNNs, GNNs, and transformers. This result unifies the PAC learnability of modern feedforward architectures under a single theoretical framework, showing that finite-sample learnability is a baseline property rather than a differentiator, shifting focus to inductive biases, scalability, and optimization. The result holds even with unbounded parameters and covers operations like linear projections, residual connections, attention, pooling, normalization, and admissible positional encodings, but excludes recurrent architectures.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: PAC learning is a framework for analyzing whether a learning algorithm can achieve low error with high probability given finite samples. The VC dimension measures the capacity of a hypothesis class; finite VC dimension implies PAC learnability. O-minimal structures are model-theoretic structures where every definable set is a finite union of intervals and points, ensuring 'tame' behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/O-minimal_structure">O-minimal structure</a></li>
<li><a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/VC_dimension">VC dimension</a></li>

</ul>
</details>

**Tags**: `#PAC learning`, `#neural networks`, `#o-minimal structures`, `#VC dimension`, `#deep learning theory`

---

<a id="item-4"></a>
## [Developer returns to hand-written code, warns of AI cognitive debt](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/) ⭐️ 8.0/10

A developer published a blog post arguing for a return to hand-written code after experiencing the downsides of AI-generated code, sparking a debate on cognitive debt and code quality. This discussion highlights a growing concern in the software engineering community that AI-generated code may increase cognitive debt, where developers lack understanding of the code they rely on, leading to long-term maintenance challenges. The post and community comments emphasize that AI-generated code can create a false sense of productivity, with developers eventually facing a codebase they cannot comprehend or modify safely. The term 'cognitive debt' is used to describe the hidden cost of using code without full understanding.

hackernews · dropbox_miner · May 11, 01:23 · [Discussion](https://news.ycombinator.com/item?id=48090029)

**Background**: Cognitive debt, also called comprehension debt, refers to the mental overhead incurred when developers work with code they do not fully understand, often generated by AI. It parallels technical debt but affects human cognition rather than code structure. The concept has gained attention as AI-assisted coding tools like GitHub Copilot become widespread.

<details><summary>References</summary>
<ul>
<li><a href="https://newsletter.getdx.com/p/cognitive-debt-the-hidden-risk-in">Cognitive debt : The hidden risk in AI-driven software development</a></li>
<li><a href="https://productera.io/blog/cognitive-debt-ai-first-startup">Cognitive Debt Is Eating Your AI-First Startup | Productera</a></li>
<li><a href="https://www.linkedin.com/pulse/cognitive-debt-crisis-architecture-disruption-agentic-markus-eisele-98ygf">The Cognitive Debt Crisis - The Architecture of Disruption - Agentic...</a></li>

</ul>
</details>

**Discussion**: Community comments largely agree with the post, sharing personal experiences of cognitive debt. One commenter notes that only those who don't read generated code think it's fine, while another describes a progression where AI takes over more coding tasks until the codebase becomes unmanageable. Some suggest rules for using AI safely, such as only generating code the developer could write themselves.

**Tags**: `#AI-assisted coding`, `#software engineering`, `#code quality`, `#cognitive debt`

---

<a id="item-5"></a>
## [AI may end software engineering as a lifetime career](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/) ⭐️ 8.0/10

An article and community discussion argue that AI, particularly large language models (LLMs), could make software engineering a less viable long-term career, as reliance on AI may lead to skill atrophy and reduced problem-solving ability. This debate affects millions of software engineers worldwide, as it questions the future value of their skills and the sustainability of their careers in an AI-augmented industry. Commenters distinguish between engineers who use AI to augment their reasoning and those who replace it, warning that the latter group risks long-term skill degradation. Experienced engineers who leverage AI as a tool may become even more productive.

hackernews · movis · May 11, 14:34 · [Discussion](https://news.ycombinator.com/item?id=48095550)

**Background**: Software engineering has traditionally been seen as a stable, high-demand career. However, the rapid advancement of AI code generation tools like GPT-4 and Copilot has sparked concerns that junior and mid-level roles may be automated, reducing the need for human developers over time.

**Discussion**: The discussion is nuanced: some commenters argue that experienced engineers who use AI as a tool remain highly valuable, while others warn that excessive reliance on AI leads to skill atrophy. A key insight is that only a small fraction of a developer's time is spent writing code, with most time dedicated to understanding problems and formulating solutions.

**Tags**: `#software engineering`, `#AI`, `#career`, `#LLM`, `#future of work`

---

<a id="item-6"></a>
## [Mythos AI Finds Curl Vulnerability, Hype Questioned](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/) ⭐️ 8.0/10

Daniel Stenberg reported that Mythos AI, an AI model from Anthropic, found a vulnerability in curl, but only five issues were discovered, far fewer than expected. The community discussion questions whether the hype around Mythos is justified, given curl's simplicity and the modest results. This matters because curl is a widely used tool, and AI-driven vulnerability detection is a hot topic. The modest results suggest that AI hype may outpace actual capability, influencing how organizations invest in security tools. Mythos found only five issues in curl, which Daniel Stenberg described as 'not particularly dangerous.' The community notes that curl is a relatively simple, well-hardened tool, so the lack of findings may reflect curl's quality rather than Mythos's weakness.

hackernews · TangerineDream · May 11, 06:39 · [Discussion](https://news.ycombinator.com/item?id=48091737)

**Background**: curl is a command-line tool and library for transferring data with URLs, used by billions of devices. Mythos is an AI model from Anthropic, part of the Claude family, designed to analyze code for vulnerabilities. The hype around Mythos suggested it would find a 'tsunami' of vulnerabilities, but this test on curl produced modest results.

<details><summary>References</summary>
<ul>
<li><a href="https://curl.se/docs/vulnall.html">curl - Vulnerability Table</a></li>
<li><a href="https://www.bbc.com/news/articles/c2ev24yx4rmo">Claude Mythos : Finance ministers and top bankers raise serious...</a></li>

</ul>
</details>

**Discussion**: Commenters like rzmmm and apexalpha argue the hype is primarily marketing, with apexalpha noting it helped secure budget. srcreigh suggests curl's simplicity limits the test's relevance, while EMM_386 points out that zero bugs could mean curl is well-hardened. Overall, the sentiment is skeptical of Mythos's claimed effectiveness.

**Tags**: `#curl`, `#vulnerability`, `#AI`, `#security`, `#hype`

---

<a id="item-7"></a>
## [NYT Issues Editor's Note After AI-Generated Quote Published](https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything) ⭐️ 8.0/10

The New York Times published an editor's note on April 14, 2026, acknowledging that a quotation attributed to Canadian Conservative leader Pierre Poilievre in an article was actually an AI-generated summary of his views, not a real quote. This incident underscores the critical risk of AI hallucinations in journalism, where AI-generated content can be mistaken for fact, eroding trust in media. It highlights the urgent need for human verification of AI outputs in newsrooms. The reporter failed to verify the AI tool's output, and the article was later corrected to include an actual quote from a Poilievre speech, which did not contain the word 'turncoats' as the AI had suggested.

rss · Simon Willison · May 10, 23:58

**Background**: AI hallucination refers to when an AI model generates false or misleading information presented as fact. In journalism, AI tools are sometimes used to summarize or draft content, but without careful human oversight, they can produce plausible-sounding but entirely fabricated quotes, as happened here.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://particlenews.medium.com/3-ways-particle-detects-and-avoids-hallucinations-in-news-summaries-c1a02d06f602">3 Ways Particle Detects and Avoids Hallucinations in News... | Medium</a></li>
<li><a href="https://phoue.co.kr/en/posts/ai-hallucination-plausible-lies-and-how-to-address-them/">AI Hallucination : Plausible Lies and How to Address Them</a></li>

</ul>
</details>

**Tags**: `#ai-ethics`, `#hallucinations`, `#generative-ai`, `#journalism`

---

<a id="item-8"></a>
## [ByteDance Open-Sources Multimodal AI Agent Stack](https://github.com/bytedance/UI-TARS-desktop) ⭐️ 8.0/10

ByteDance has released UI-TARS-desktop, an open-source multimodal AI agent stack that includes Agent TARS (a general CLI/Web UI agent) and UI-TARS Desktop (a native GUI agent for desktop and browser control). This release lowers the barrier for developers to build and deploy multimodal AI agents that can control computers and browsers, potentially accelerating automation in software testing, workflow management, and personal productivity. Agent TARS integrates with MCP tools and supports human-like task completion via multimodal LLMs, while UI-TARS Desktop provides both local and remote operators for computer and browser control.

rss · GitHub Trending - Daily (All) · May 11, 18:37

**Background**: Multimodal AI agents combine vision and language understanding to interact with graphical user interfaces (GUIs) similarly to humans. ByteDance's UI-TARS model, which powers UI-TARS Desktop, is a vision-language model trained to interpret and act on screen content. The open-source release includes two complementary projects: Agent TARS for general-purpose agent workflows and UI-TARS Desktop for direct desktop automation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bytedance/UI-TARS-desktop">bytedance/UI- TARS -desktop: The Open-Source Multimodal AI Agent ...</a></li>
<li><a href="https://agent-tars.com/">Agent TARS - Open-source Multimodal AI Agent Stack</a></li>
<li><a href="https://ui-tarsai.com/">Bytedance UI - TARS AI Desktop : AI Agent for Computer Control</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#multimodal`, `#agent`, `#desktop`

---

<a id="item-9"></a>
## [Agent Skills: Production-Grade Workflows for AI Coding Agents](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released a GitHub repository called 'agent-skills' that packages senior engineer workflows and quality gates into slash commands for AI coding agents like Claude Code, Cursor, and Gemini CLI. This project bridges the gap between ad-hoc AI prompting and disciplined software engineering, enabling AI agents to follow consistent, production-grade practices across the entire development lifecycle. The repository provides seven slash commands (/spec, /plan, /build, /test, /review, /code-simplify, /ship) that map to development phases, and skills activate automatically based on context (e.g., API design triggers api-and-interface-design).

rss · GitHub Trending - Daily (All) · May 11, 18:37

**Background**: AI coding agents like Claude Code and Cursor can generate code but often lack structured engineering workflows. 'Agent Skills' encodes best practices from senior engineers into reusable skills that guide agents through specification, planning, building, testing, review, and shipping.

<details><summary>References</summary>
<ul>
<li><a href="https://addyosmani.com/blog/agent-skills/">AddyOsmani .com - Agent Skills</a></li>
<li><a href="https://pyshine.com/Agent-Skills-Production-Grade-Engineering-for-AI/">Agent Skills : Production - Grade Engineering Skills for AI ... | PyShine</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software engineering`, `#workflows`, `#developer tools`, `#best practices`

---

<a id="item-10"></a>
## [CloakBrowser: Stealth Chromium Passes All Bot Detection Tests](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser is a new open-source stealth Chromium browser that applies 49 source-level C++ fingerprint patches to bypass all major bot detection systems, achieving a perfect 30/30 test score. It serves as a drop-in replacement for Playwright and Puppeteer, requiring only three lines of code to integrate. This project addresses a critical pain point in web automation and scraping, where bot detection systems like Cloudflare Turnstile and reCAPTCHA v3 frequently block automated browsers. By providing a free, open-source solution that passes all detection tests, CloakBrowser could significantly reduce friction for developers and researchers who rely on browser automation. The browser uses 49 source-level C++ patches covering canvas, WebGL, audio, fonts, GPU, screen, WebRTC, network timing, automation signals, and CDP input behavior. It also includes a humanize=True flag that simulates human-like mouse curves, keyboard timing, and scroll patterns, and has achieved a 0.9 reCAPTCHA v3 score.

rss · GitHub Trending - Daily (All) · May 11, 18:37

**Background**: Browser fingerprinting is a technique used by websites to identify and block automated browsers by collecting unique attributes like screen resolution, fonts, and WebGL renderer. Traditional approaches to bypass detection include patching JavaScript APIs or using headless browsers, but these are often detected by advanced anti-bot systems. CloakBrowser modifies the Chromium source code at the C++ level, making the browser appear identical to a normal user's browser.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zenrows.com/blog/browser-fingerprinting">What Is Browser Fingerprinting and How to Bypass It? - ZenRows</a></li>
<li><a href="https://www.browserscan.net/bot-detection">BrowserScan - Robot Detection /WebDriver | BrowserScan</a></li>
<li><a href="https://bot.incolumitas.com/">Bot / Headless Chrome Detection Tests</a></li>

</ul>
</details>

**Tags**: `#web automation`, `#bot detection`, `#browser fingerprinting`, `#open source`, `#Playwright`

---

<a id="item-11"></a>
## [GenericAgent: Self-Evolving Agent Grows Skill Tree from 3K-Line Seed](https://github.com/lsdefine/GenericAgent) ⭐️ 8.0/10

GenericAgent is a minimal, self-evolving autonomous agent framework that grows a skill tree from a ~3,300-line seed code, achieving full system control with 6x less token consumption compared to other agents. This approach significantly reduces token usage and cost while enabling agents to autonomously expand their capabilities, which could make AI agents more practical and scalable for real-world system control tasks. The core code is only ~3,000 lines, with a ~100-line Agent Loop and 9 atomic tools that control browser, terminal, filesystem, keyboard/mouse, screen vision, and mobile devices via ADB. It supports models like Claude, Gemini, Kimi, and MiniMax.

rss · GitHub Trending - Daily (All) · May 11, 18:37

**Background**: Traditional AI agents often rely on large context windows (200K–1M tokens) and pre-defined skill libraries, leading to high cost and limited adaptability. GenericAgent instead uses a self-evolution mechanism that crystallizes execution paths into reusable skills, keeping context under 30K tokens.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lsdefine/GenericAgent">GitHub - lsdefine/ GenericAgent : Self - evolving agent : grows skill tree...</a></li>
<li><a href="https://www.genericagent.org/">GenericAgent - Self - Evolving Agents for Real System Work</a></li>
<li><a href="https://a-gnt.com/agents/genericagent">a-gnt // GenericAgent — AI Agent for Claude, ChatGPT & More</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Self-Evolution`, `#Token Efficiency`, `#Skill Tree`, `#GitHub Trending`

---

<a id="item-12"></a>
## [Memori: Agent-Native Memory Infrastructure for LLMs](https://github.com/MemoriLabs/Memori) ⭐️ 8.0/10

Memori Labs has released Memori, an open-source, LLM-agnostic memory infrastructure that converts agent actions and conversations into structured, persistent state for production systems. This addresses a critical gap in building reliable LLM agents by providing persistent memory that works across sessions and models, enabling more coherent and context-aware AI applications. Memori is LLM, datastore, and framework agnostic, offering both TypeScript and Python SDKs, and integrates with existing stacks via a cloud service (Memori Cloud) or self-hosted options.

rss · GitHub Trending - Python · May 11, 18:37

**Background**: LLM agents often lack long-term memory, forgetting context across sessions or when switching models. Memori captures each chat turn, classifies it into facts, preferences, rules, and summaries, and persists them for recall.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MemoriLabs/Memori">MemoriLabs/Memori: Memori is agent-native memory infrastructure .</a></li>
<li><a href="https://memorilabs.ai/">Memori – Agent-native memory infrastructure</a></li>
<li><a href="https://www.truefoundry.com/blog/truemem-building-a-model-agnostic-memory-layer-for-ai">How to Build Persistent Memory for AI Applications</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#agent memory`, `#infrastructure`, `#AI`, `#open source`

---

<a id="item-13"></a>
## [GraphDC: Divide-and-Conquer Multi-Agent System for Graph Reasoning](https://arxiv.org/abs/2605.06671) ⭐️ 8.0/10

Researchers propose GraphDC, a divide-and-conquer multi-agent framework that decomposes large graphs into smaller subgraphs, assigns each to a specialized agent for local reasoning, and uses a master agent to integrate results, significantly improving LLM performance on graph algorithmic tasks. This work addresses a critical limitation of LLMs in handling complex graph structures, enabling scalable and robust reasoning on large graphs, which is essential for applications in knowledge graphs, network analysis, and scientific discovery. GraphDC's hierarchical design reduces the reasoning burden on individual agents and alleviates computational bottlenecks. Experiments show it consistently outperforms existing methods, especially on larger graph instances where direct end-to-end reasoning is less reliable.

rss · arXiv - AI · May 11, 04:00

**Background**: Large Language Models (LLMs) have shown strong potential for mathematical reasoning but struggle with graph algorithmic tasks due to graphs' complex topology and need for multi-step reasoning. Existing methods often fail on larger graphs because they attempt direct end-to-end reasoning, which becomes unreliable as graph size increases. Divide-and-conquer is a classic algorithm design paradigm that breaks a problem into smaller subproblems, solves them independently, and combines the results.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.22597">Are Large-Language Models Graph Algorithmic Reasoners? - arXiv</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#graph algorithms`, `#multi-agent systems`, `#scalability`, `#AI reasoning`

---

<a id="item-14"></a>
## [Longer Reasoning Chains Increase Position Bias in LLMs](https://arxiv.org/abs/2605.06672) ⭐️ 8.0/10

A new study finds that longer chain-of-thought reasoning trajectories in large language models exacerbate position bias in multiple-choice QA, contrary to the assumption that more thinking reduces bias. This challenges the common belief that reasoning models are more robust, revealing a hidden vulnerability that could affect reliability in high-stakes evaluations and applications. Across 13 reasoning-mode configurations, 12 showed a positive correlation between trajectory length and Position Bias Score (PBS), with truncation experiments providing causal evidence that later continuations shift toward position-preferred options.

rss · arXiv - AI · May 11, 04:00

**Background**: Position bias refers to LLMs' tendency to favor certain answer positions (e.g., 'A' over 'B') regardless of content. Chain-of-thought (CoT) reasoning is a technique that prompts models to generate step-by-step reasoning before answering, often used to improve accuracy and reduce biases.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@lyx_62906/the-hidden-position-bias-in-llms-why-your-ai-might-fail-when-its-asked-to-choose-26d59516f6ee">The Hidden Position Bias in LLMs : Why Your AI Might Fail... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_reasoning">Chain-of-thought reasoning</a></li>

</ul>
</details>

**Tags**: `#chain-of-thought`, `#position bias`, `#reasoning models`, `#LLM evaluation`, `#cognitive bias`

---

<a id="item-15"></a>
## [Spectral Diagnostic Detects Hidden Coalitions in Multi-Agent AI](https://arxiv.org/abs/2605.06696) ⭐️ 8.0/10

Researchers introduced a spectral diagnostic method that constructs mutual-information graphs from internal neural representations of agents and applies spectral partitioning to detect hidden coalitions before behavioral changes occur. This method addresses a critical gap in AI safety by enabling early detection of emergent coalitions that could lead to collusion or misalignment in multi-agent systems, offering a scalable monitoring tool for distributed AI. The method was validated in multi-agent reinforcement learning environments and with large language models, successfully recovering programmed coalition structures and rejecting false positives from behavioral coordination without informational coupling.

rss · arXiv - AI · May 11, 04:00

**Background**: Multi-agent AI systems consist of multiple interacting agents that can form coalitions, creating emergent group-level organization. Observing behavior alone is often insufficient to distinguish genuine informational coupling from spurious similarity, as coalitions may form at the level of internal representations before any behavioral change. Spectral partitioning is a technique that uses eigenvalues of a graph's Laplacian to find optimal cuts, commonly used in community detection.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06696">Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graph_partition">Graph partition - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#AI safety`, `#coalition detection`, `#spectral partitioning`, `#mutual information`

---

<a id="item-16"></a>
## [CASCADE: Case-Based Continual Adaptation for LLMs During Deployment](https://arxiv.org/abs/2605.06702) ⭐️ 8.0/10

CASCADE introduces a novel framework for deployment-time learning in LLMs, enabling agents to improve from experience without modifying model parameters, using an evolving episodic memory and contextual bandit formulation with no-regret guarantees. This work addresses a key limitation of current LLMs—the inability to learn during deployment—and formalizes a third stage in the LLM lifecycle, potentially enabling continuously improving AI systems across diverse applications. CASCADE improves macro-averaged success rate by 20.9% over zero-shot prompting across 16 diverse tasks, consistently outperforming gradient-based and memory-based baselines.

rss · arXiv - AI · May 11, 04:00

**Background**: Large language models (LLMs) typically stop learning after training, unlike natural intelligence that adapts continuously. Deployment-time learning (DTL) is a new paradigm that allows LLMs to improve from interactions during deployment without parameter updates, using episodic memory to store and reuse past experiences.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2501.13121">[2501.13121] Episodic Memories Generation and Evaluation...</a></li>
<li><a href="https://github.com/miguelalcocker/episodic-memory-llm">GitHub - miguelalcocker/ episodic - memory - llm : Persistent Episodic ...</a></li>
<li><a href="https://huggingface.co/papers/2407.09450">Paper page - Human-like Episodic Memory for Infinite Context LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#continual learning`, `#deployment-time learning`, `#contextual bandit`, `#episodic memory`

---

<a id="item-17"></a>
## [LLM Agent Memory Evolution: Storage to Experience](https://arxiv.org/abs/2605.06716) ⭐️ 8.0/10

This survey proposes a three-stage evolutionary framework for LLM agent memory mechanisms: Storage, Reflection, and Experience, bridging the gap between OS engineering and cognitive science. This framework provides a unified perspective on memory design for LLM agents, which is crucial for advancing agent capabilities in long-range consistency, dynamic environments, and continual learning. The three stages are formally defined: Storage preserves trajectories, Reflection refines them, and Experience abstracts them. The survey also explores proactive exploration and cross-trajectory abstraction as transformative mechanisms in the Experience stage.

rss · arXiv - AI · May 11, 04:00

**Background**: LLM-based agents integrate external tools and planning capabilities, but their memory mechanisms have been fragmented across different fields. Short-term memory handles immediate context, while long-term memory persists across tasks. This survey aims to unify these views into an evolutionary framework.

<details><summary>References</summary>
<ul>
<li><a href="https://www.rohan-paul.com/p/augmenting-llm-agents-with-long-term">Augmenting LLM Agents with Long-Term Memory - Rohan's Bytes</a></li>
<li><a href="https://www.emergentmind.com/videos/memory-mechanisms-in-llm-agents-b4da59c4">Memory Mechanisms in LLM Agents</a></li>
<li><a href="https://gist.github.com/Moenupa/5b9b341bfb52aa1bf150d8f35de831cf">Memory Literature Review · GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#memory mechanisms`, `#survey`, `#AI`, `#cognitive science`

---

<a id="item-18"></a>
## [Weblica: Scalable Training Environments for Visual Web Agents](https://arxiv.org/abs/2605.06761) ⭐️ 8.0/10

Weblica introduces a framework that uses HTTP-level caching and LLM-based environment synthesis to create scalable, reproducible web environments for training visual web agents, achieving state-of-the-art performance with the Weblica-8B model. This addresses a key bottleneck in web agent research by enabling scalable RL training across thousands of diverse environments, outperforming open-weight baselines and competing with API models, which could accelerate the development of robust web agents. Weblica leverages HTTP-level caching to capture and replay stable visual states while preserving interactive behavior, and uses LLM-based synthesis grounded in real-world websites to generate diverse training tasks. The Weblica-8B model outperforms similar-sized open-weight baselines on multiple benchmarks with fewer inference steps.

rss · arXiv - AI · May 11, 04:00

**Background**: Visual web agents are AI systems that interact with web interfaces by processing screenshots and performing actions like clicking or typing. Training such agents is challenging due to the web's dynamic nature and the need for diverse, reproducible environments. Existing methods rely on limited offline trajectories or simulated environments, failing to capture real-world diversity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.02439v3">WebGym: Scaling Training Environments for Visual Web Agents with...</a></li>
<li><a href="https://jykoh.com/vwa">VisualWebArena: Evaluating Multimodal Agents on Realistic Visual ...</a></li>

</ul>
</details>

**Tags**: `#web agents`, `#reinforcement learning`, `#LLM`, `#scalable environments`, `#AI`

---

<a id="item-19"></a>
## [SCALAR: Iterative Critique Boosts LLM Physics Reasoning](https://arxiv.org/abs/2605.06772) ⭐️ 8.0/10

Researchers introduced SCALAR, an Actor-Critic-Judge pipeline that systematically evaluates how iterative critique improves LLM performance on quantum field theory and string theory problems, finding multi-turn dialogue consistently outperforms single-shot attempts. This work provides a controlled testbed for understanding which interaction structures between researchers and AI agents enhance scientific discovery, with implications for designing more effective AI assistants in theoretical physics and beyond. The study varied Actor persona, Critic feedback strategy, and model scale, finding that increasing model scale (e.g., from DeepSeek-R1 8B to 70B) improved easier problems but did not resolve the hardest bottlenecks, and that Critic strategy mattered most in asymmetric Actor-Critic pairings.

rss · arXiv - AI · May 11, 04:00

**Background**: Large language models (LLMs) are increasingly used for research-level reasoning in physics. The Actor-Critic framework, borrowed from reinforcement learning, involves an Actor proposing solutions and a Critic providing feedback; SCALAR adds an independent Judge for evaluation. This work explores how different pairings and feedback strategies affect performance on complex theoretical physics problems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">deepseek-ai/ DeepSeek - R 1 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI reasoning`, `#theoretical physics`, `#agentic AI`, `#critique`

---

<a id="item-20"></a>
## [RateQuant: Optimal Mixed-Precision KV Cache Quantization via Rate-Distortion Theory](https://arxiv.org/abs/2605.06675) ⭐️ 8.0/10

RateQuant introduces a rate-distortion theory-based method for optimal mixed-precision KV cache quantization, identifying and solving the distortion model mismatch failure mode that degrades performance in existing approaches. This work addresses a critical memory bottleneck in LLM serving by enabling more efficient KV cache compression, potentially reducing memory usage while maintaining model quality, which is vital for scaling LLMs to longer contexts. RateQuant fits a per-quantizer distortion model from a small calibration set and solves bit allocation via reverse waterfilling from rate-distortion theory. On Qwen3-8B at 2.5 average bits, it reduces KIVI's perplexity from 49.3 to 14.9 and improves QuaRot by 6.6 PPL, with calibration taking only 1.6 seconds on a single GPU.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: KV cache stores previously computed key-value pairs during LLM generation, growing linearly with sequence length and becoming a major memory bottleneck. Quantization reduces the bit-width of these values, but existing methods assign the same bit-width to all attention heads, ignoring varying head importance. Mixed-precision quantization aims to allocate more bits to important heads, but RateQuant reveals that different quantizers have different distortion curves, and using one quantizer's model for another can cause distortion model mismatch, making performance worse than uniform quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rate-distortion_theory">Rate-distortion theory</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>
<li><a href="https://grokipedia.com/page/Progressive_Mixed-Precision_KV_Cache_Quantization">Progressive Mixed-Precision KV Cache Quantization</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#KV cache quantization`, `#mixed-precision`, `#rate-distortion theory`, `#efficient inference`

---

<a id="item-21"></a>
## [LKV: Learned KV Cache Eviction for Efficient LLM Inference](https://arxiv.org/abs/2605.06676) ⭐️ 8.0/10

LKV introduces an end-to-end differentiable framework for KV cache eviction in LLMs, comprising LKV-H for learning per-head budgets and LKV-T for token importance scoring, achieving near-lossless performance with only 15% KV cache retention on LongBench. This work addresses a critical bottleneck in long-context LLM inference by replacing heuristic-based cache management with a learned, task-optimized approach, potentially enabling more efficient deployment of large models in memory-constrained environments. LKV-H learns global budgets per attention head via a differentiable relaxation, while LKV-T computes intrinsic token importance without materializing attention matrices, bypassing heuristic proxies like attention sinks.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: Large Language Models (LLMs) use a Key-Value (KV) cache to store intermediate attention states, which grows linearly with sequence length and becomes a memory bottleneck for long-context inference. Existing compression methods rely on heuristic rules for budget allocation and token selection, often leading to suboptimal performance.

**Tags**: `#LLM`, `#KV cache`, `#compression`, `#efficient inference`, `#deep learning`

---

<a id="item-22"></a>
## [PND: Training-Free Decoding Reduces VLM Hallucination](https://arxiv.org/abs/2605.06679) ⭐️ 8.0/10

Researchers propose Positive-and-Negative Decoding (PND), a training-free inference framework that reduces object hallucination in Vision-Language Models by amplifying visual evidence and penalizing linguistic priors during decoding. Object hallucination is a critical flaw in VLMs that undermines trust in multimodal AI; PND offers a practical, retraining-free solution that can be applied to existing models, potentially improving reliability in real-world applications. PND introduces a dual-path contrast: a positive path that amplifies visual evidence and a negative path that constructs counterfactuals to penalize prior-dominant generation. Experiments on POPE, MME, and CHAIR benchmarks demonstrate state-of-the-art performance without retraining.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: Vision-Language Models (VLMs) like LLaVA generate text based on both visual input and language priors, but often over-rely on linguistic context, causing object hallucination—describing objects not present in the image. Existing mitigation methods typically require additional training or fine-tuning, which is resource-intensive. PND intervenes directly at inference time, adjusting the decoding process to favor visual grounding.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.06679">Breaking the Illusion: When Positive Meets Negative in Multimodal...</a></li>
<li><a href="https://www.machinebrief.com/news/reining-in-ais-imagination-with-positive-and-negative-decodi-fgk4">Reining in AI's Imagination with Positive - and - Negative ... | Machine Brief</a></li>

</ul>
</details>

**Tags**: `#Vision-Language Models`, `#Object Hallucination`, `#Decoding Strategy`, `#Multimodal AI`, `#Inference-time Intervention`

---

<a id="item-23"></a>
## [Strain and Vorticity in Flow Matching Error](https://arxiv.org/abs/2605.06680) ⭐️ 8.0/10

This paper proves that strain causes exponential error amplification in flow matching numerical integration, while vorticity contributes only linearly, and proposes weighted Jacobian regularization to mitigate error. This theoretical insight can improve the efficiency of generative models like Stable Diffusion 3 by reducing the number of integration steps needed, lowering inference cost without sacrificing quality. The analysis decomposes the velocity Jacobian into strain rate S and vorticity Ω, showing strain controls error via logarithmic norm. Experiments on 2D data achieve up to 2.7x lower error at NFE=5, and CIFAR-10 fine-tuning improves FID by 14% at NFE=10.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: Flow matching is a generative modeling technique that learns a velocity field to transform noise into data via ordinary differential equations (ODEs). The number of function evaluations (NFE) determines inference cost, and integration error affects sample quality. The logarithmic norm is a tool from numerical analysis used to bound error growth in ODE solvers.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logarithmic_norm">Logarithmic norm - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#flow matching`, `#numerical integration`, `#generative modeling`, `#Jacobian regularization`

---

<a id="item-24"></a>
## [Toeplitz MLP Mixer: Efficient Sub-Quadratic Sequence Model](https://arxiv.org/abs/2605.06683) ⭐️ 8.0/10

Researchers introduced the Toeplitz MLP Mixer (TMM), a transformer-like architecture that replaces attention with triangular-masked Toeplitz matrix multiplication, achieving O(dn log n) time and O(dn) space complexity during training and O(dn) at inference prefill. TMM addresses the quadratic complexity bottleneck of transformers, enabling more efficient processing of long sequences while retaining more input information and improving copying ability, which is crucial for large language models. TMM uses triangular-masked Toeplitz matrices over the sequence dimension, which are structured matrices enabling fast multiplication via FFT. Despite lacking input modulation or state maintenance, TMM achieves better training efficiency and information retention than comparable sub-quadratic architectures.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: Transformers rely on attention mechanisms with quadratic complexity in sequence length, limiting their scalability to long contexts. Sub-quadratic architectures like state space models and linear attention aim to reduce this complexity. Toeplitz matrices are constant along diagonals and enable O(n log n) matrix-vector multiplication via FFT, making them suitable for efficient sequence mixing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06683">[2605.06683] Toeplitz MLP Mixers are Low Complexity...</a></li>
<li><a href="https://arxiv.org/html/2605.06683">Toeplitz MLP Mixers are Low Complexity, Information-Rich Sequence...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#architecture`, `#efficiency`, `#transformers`, `#sequence models`

---

<a id="item-25"></a>
## [Germline-Absorbing Diffusion Improves Antibody Design](https://arxiv.org/abs/2605.06720) ⭐️ 8.0/10

Researchers introduced a classifier-guided discrete diffusion model with germline-absorbing noise for conditional generation of antibody sequences, achieving 46% non-germline residue prediction accuracy, up from 26%. This approach addresses key limitations of protein language models in antibody design, such as germline bias and lack of flexible conditional generation, potentially accelerating computational antibody therapeutics development. The model uses germline absorbing diffusion, where the germline sequence serves as the absorbing state, and supports conditioning on any off-the-shelf classifier, outperforming EvoProtGrad on hydrophobicity and binding affinity tasks.

rss · arXiv - Machine Learning · May 11, 04:00

**Background**: Antibody design often relies on protein language models (pLMs), but these models tend to memorize germline sequences and struggle with conditional generation. Discrete diffusion models offer a probabilistic framework for generating sequences, and classifier guidance enables targeted property optimization.

**Tags**: `#antibody design`, `#discrete diffusion`, `#protein language models`, `#computational biology`, `#generative models`

---

<a id="item-26"></a>
## [Domain-level metacognitive monitoring in 33 LLMs](https://arxiv.org/abs/2605.06673) ⭐️ 8.0/10

A study of 33 frontier LLMs reveals systematic domain-level variation in metacognitive monitoring quality, with Applied/Professional knowledge being the easiest and Formal Reasoning/Natural Science the hardest to monitor. This finding highlights that aggregate metacognitive scores mask important within-model variation, which is critical for AI safety and deployment decisions in specific application areas. The study used 1,500 MMLU items across six domains, computing Type-2 AUROC from verbalized confidence scores, and found that within-family profile-shape clustering was significant for Anthropic, Google-Gemini, and Qwen but not for DeepSeek, Google-Gemma, or OpenAI.

rss · arXiv - NLP · May 11, 04:00

**Background**: Metacognitive monitoring refers to an LLM's ability to accurately assess its own confidence in its outputs. The MMLU benchmark tests knowledge across multiple domains, and Type-2 AUROC is a metric for evaluating the quality of confidence calibration.

**Tags**: `#LLM`, `#metacognition`, `#AI evaluation`, `#MMLU`, `#benchmarking`

---

<a id="item-27"></a>
## [IntentGrasp Benchmark Reveals LLM Intent Understanding Gaps](https://arxiv.org/abs/2605.06832) ⭐️ 8.0/10

Researchers introduced IntentGrasp, a large-scale benchmark for evaluating LLM intent understanding, and found that even frontier models like GPT-5.4 score below 60% on the All Set and below 25% on the challenging Gem Set. This benchmark highlights a critical weakness in current LLMs—intent understanding—which is essential for building reliable AI assistants, and proposes Intentional Fine-Tuning (IFT) that significantly improves performance, pointing to a path for safer and more capable AI. IntentGrasp includes 262,759 training instances and two evaluation sets (All Set with 12,909 cases and Gem Set with 470 cases) derived from 49 corpora across 12 domains; 17 out of 20 tested models performed worse than random guessing (15.2%) on the Gem Set, while estimated human performance is ~81.1%.

rss · arXiv - NLP · May 11, 04:00

**Background**: Intent understanding is the ability of an LLM to correctly infer the user's underlying goal or request from their input. Despite advances in language models, systematic evaluation of this capability has been lacking. IntentGrasp fills this gap by providing a diverse, large-scale benchmark.

**Tags**: `#LLM`, `#benchmark`, `#intent understanding`, `#NLP`, `#evaluation`

---

<a id="item-28"></a>
## [Human-Centered LLM Framework Proposed](https://arxiv.org/abs/2605.06901) ⭐️ 8.0/10

A new paper introduces a framework for Human-Centered Large Language Models (HCLLMs) that integrates ethical, economic, and technical considerations across the entire development pipeline, from design to deployment. This framework addresses the growing need for responsible AI by ensuring that human values and priorities are considered at every stage of LLM development, not just post-training, which could influence industry practices and policy. The framework combines perspectives from NLP, HCI, and responsible AI, offering specific recommendations for system design, data sourcing, model training, evaluation, and deployment, with a case study on the future of work.

rss · arXiv - NLP · May 11, 04:00

**Background**: Large Language Models (LLMs) like GPT-4 are neural networks trained on vast text data for language generation. While powerful, they often lack explicit consideration of human values, leading to ethical concerns. This paper proposes a systematic approach to embed human-centeredness throughout the LLM lifecycle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/top-content/artificial-intelligence/human-ai-collaboration/building-human-centered-large-language-models/">Building Human - Centered Large Language Models</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Human-Computer Interaction`, `#Responsible AI`, `#NLP`, `#Ethics`

---

<a id="item-29"></a>
## [LLMs Fail to Adjust to Retrieved Information Certainty](https://arxiv.org/abs/2605.06919) ⭐️ 8.0/10

A new study evaluates eight LLMs on context-certainty obedience and finds systematic failures, but proposes an interaction strategy combining reminders, recalibration, and simplification that reduces obedience errors by 25%. This work highlights a critical underexplored limitation in retrieval-augmented generation (RAG) systems, which is especially concerning for high-stakes domains like medicine and finance where uncertain information is common. The study tested eight LLMs and found they struggle to recall prior knowledge after uncertain context, misinterpret certainties, and overtrust complex contexts. The proposed interaction strategy reduces errors without modifying model weights.

rss · arXiv - NLP · May 11, 04:00

**Background**: Retrieval-augmented generation (RAG) systems combine LLMs with external knowledge retrieval to improve factual accuracy. However, retrieved information often comes with varying levels of certainty (e.g., confidence scores, hedging language). This study systematically examines how well LLMs handle such uncertainty.

**Tags**: `#LLM`, `#Retrieval-Augmented Generation`, `#Uncertainty`, `#Reliability`, `#Interaction Design`

---

<a id="item-30"></a>
## [Measure Transport Theory Explains Visual Text Compression](https://arxiv.org/abs/2605.06708) ⭐️ 8.0/10

A new paper formulates visual text compression (VTC) as a measure transport problem, introducing a principled framework to quantify task-relevant information loss when rendering text as images for vision-language models. This work addresses a critical gap in understanding why compression ratios don't predict downstream performance, enabling label-free routing and adaptive foveation that improve efficiency and accuracy across 24 NLP datasets. The framework decomposes transport cost into precision cost (within-patch aggregation) and coverage cost (cross-patch fragmentation), both estimable without downstream labels. Their label-free routing rule matches the per-dataset oracle on 17/24 datasets (70.8%) and improves average task score by +3.3% with -10.3% average tokens.

rss · arXiv - Computer Vision · May 11, 04:00

**Background**: Visual text compression (VTC) renders long text into images and re-encodes them with a vision-language model, often producing 3-20x fewer decoder tokens than subword tokenization. However, token savings do not reliably translate to better task performance, and the compression ratio alone cannot predict when visual encoding helps or hurts. Measure transport is a mathematical framework from optimal transport theory that compares probability distributions by considering the cost of moving mass from one distribution to another.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Information_theory">Information theory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Glyph_visual-text_compression">Glyph (visual-text compression)</a></li>

</ul>
</details>

**Tags**: `#visual text compression`, `#measure transport`, `#vision-language models`, `#long-context processing`, `#information theory`

---

<a id="item-31"></a>
## [LookWhen: Efficient Video Recognition via Token Selection](https://arxiv.org/abs/2605.06809) ⭐️ 8.0/10

LookWhen introduces a selector-extractor framework that learns when, where, and what to compute, using a shallow selector to score tokens and a deep extractor to process only the top-K tokens, reducing computational cost while approximating full-video representations. This work addresses the computational redundancy in video transformers, achieving a better accuracy-computation trade-off across multiple benchmarks, and could enable more efficient video understanding on resource-constrained devices. The selector pre-training uses a nearest-neighbor distance to rank tokens by uniqueness, and the extractor is distilled from both a video teacher and an image teacher with normalized frame-wise representations. LookWhen achieves up to 6.7x speedup over InternVideo2-B at equal accuracy.

rss · arXiv - Computer Vision · May 11, 04:00

**Background**: Video transformers process videos by splitting them into spatiotemporal tokens, but the computational cost grows superlinearly with token count. Videos contain significant redundancy, so not all tokens are equally informative. LookWhen exploits this by selecting only the most informative tokens for processing.

**Tags**: `#video recognition`, `#efficient deep learning`, `#transformer`, `#token selection`, `#distillation`

---

<a id="item-32"></a>
## [Scaling Laws for Knowledge Transfer in 3D Medical Imaging](https://arxiv.org/abs/2605.06859) ⭐️ 8.0/10

This paper discovers asymmetric knowledge transfer and power-law scaling in 3D medical imaging domains, proposing a scaling-law optimization for data allocation that outperforms data-proportional sampling by up to 58%. This work provides a principled framework for data allocation in multi-modal pretraining of 3D medical imaging foundation models, which could significantly improve efficiency and performance across diverse clinical tasks. The derived allocations reveal a hub-and-island structure where highly transferable domains (hubs) benefit many others, while isolated domains (islands) require direct investment. The transfer-aware allocation generalizes to unseen budgets with a correlation of r=0.989.

rss · arXiv - Computer Vision · May 11, 04:00

**Background**: Vision foundation models are expanding from 2D to 3D medical imaging, where unified pretraining across modalities like CT, MRI, and PET could provide foundational models for diverse clinical tasks. Current mixture strategies for combining heterogeneous imaging domains are largely heuristic. This paper introduces scaling laws to guide data allocation in such multi-modal pretraining.

**Tags**: `#scaling laws`, `#medical imaging`, `#transfer learning`, `#vision foundation models`, `#3D`

---

<a id="item-33"></a>
## [HSA: Heterogeneous Step Allocation for Efficient Video DiTs](https://arxiv.org/abs/2605.06892) ⭐️ 8.0/10

Researchers propose Heterogeneous Step Allocation (HSA), a training-free inference method that assigns varying denoising steps to tokens based on velocity dynamics, reducing computational cost in diffusion transformers for video generation. HSA解决了视频生成中的一个关键效率瓶颈，能够在显著减少运行时间的同时保持高质量输出，这对扩散Transformer的实际部署至关重要。 HSA introduces a KV-cache synchronization mechanism to handle sequence-length mismatches and a cached Euler update to advance skipped tokens without extra model evaluations. It outperforms prior caching methods on Wan-2 and LTX-2 models, especially at 50% and 25% runtimes.

rss · arXiv - Computer Vision · May 11, 04:00

**Background**: Diffusion Transformers (DiTs) achieve state-of-the-art video generation but require many denoising steps per token, leading to high computational cost. Standard inference applies uniform steps to all tokens, ignoring that human vision can skip redundant motion. HSA leverages velocity dynamics to allocate steps heterogeneously.

**Tags**: `#Diffusion Transformers`, `#Video Generation`, `#Efficient Inference`, `#KV-cache`, `#Deep Learning`

---

<a id="item-34"></a>
## [Attention Mechanisms: Random Matrix Insights on Signal Recovery](https://arxiv.org/abs/2605.06826) ⭐️ 8.0/10

This paper derives exact spectral characterizations for sample covariance matrices from pooled sequence representations, revealing phase transitions in signal recovery governed by attention weights and vocabulary structure. This work provides a rigorous theoretical foundation for understanding how attention mechanisms help in signal recovery, which could guide the design of more efficient transformer models and attention-based architectures. The analysis shows that optimal attention weights maximizing signal-to-noise ratio are given by the top eigenvector of the positional correlation matrix, and parameter-free causal self-attention with τ/d score scaling yields deterministic harmonic weights that improve signal recovery over mean pooling when early tokens carry more signal.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: Random matrix theory (RMT) studies the spectral properties of large random matrices and has found applications in high-dimensional statistics and machine learning. The Marchenko-Pastur law describes the eigenvalue distribution of sample covariance matrices, and its free multiplicative convolution generalizes this to structured settings. Attention mechanisms in transformers weight token contributions dynamically, and understanding their theoretical properties is crucial for model interpretability and improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution">Marchenko – Pastur distribution - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#attention`, `#random matrix theory`, `#deep learning theory`, `#signal recovery`, `#transformers`

---

<a id="item-35"></a>
## [Neural Operator Learns Conditional Distributions from Any Joint Density](https://arxiv.org/abs/2605.06873) ⭐️ 8.0/10

This paper proposes learning a single neural operator that maps any joint density to its conditional distribution, amortizing over joint-conditional pairs, with theoretical guarantees of arbitrary accuracy. This work provides theoretical underpinnings for general-purpose, amortized probabilistic conditioning, potentially enabling foundation models for Bayesian inference and advancing uncertainty quantification in machine learning. The authors prove continuity of the conditioning operator over suitable density classes and demonstrate the framework on Gaussian mixtures using neural operators.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: Probabilistic conditioning is the process of updating a distribution of a random variable given another variable, fundamental to uncertainty quantification. Traditional methods learn a conditional distribution for a fixed joint distribution, while this work aims to learn an operator that works for any joint density. Neural operators are deep learning architectures that learn mappings between function spaces, originally developed for solving partial differential equations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_operators">Neural operators</a></li>

</ul>
</details>

**Tags**: `#probabilistic conditioning`, `#neural operators`, `#uncertainty quantification`, `#machine learning`, `#amortized inference`

---

<a id="item-36"></a>
## [Kernel Selection as Model Selection for MMD Tests](https://arxiv.org/abs/2605.06883) ⭐️ 8.0/10

This paper introduces Complexity-Penalized MMD (CP-MMD), a criterion that treats kernel selection as a model selection problem, enabling grid-free optimization over continuous kernel classes while preventing overfitting. CP-MMD resolves a fundamental limitation in nonparametric two-sample testing by mathematically accounting for optimization complexity, ensuring unconditional Type-I validity and maximizing test power across linear, polynomial, and deep kernel regimes. The penalty in CP-MMD bounds the empirical MMD by the complexity of the kernel search space, derived from a two-sample uniform concentration inequality. This allows direct maximization over continuous parametric classes like scalar bandwidths and deep network parameters.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: The Maximum Mean Discrepancy (MMD) is a statistic used to test whether two distributions are different, but its power depends on the choice of kernel. Data-driven kernel optimization violates the i.i.d. assumption, leading to overfitting in ratio-based methods or limited scalability in aggregation methods. CP-MMD addresses this by framing kernel selection as a model selection problem with a complexity penalty.

**Tags**: `#kernel methods`, `#two-sample test`, `#MMD`, `#model selection`, `#statistical learning theory`

---

<a id="item-37"></a>
## [Interpretable IRT Framework for Scalable LLM Evaluation](https://arxiv.org/abs/2605.07046) ⭐️ 8.0/10

Researchers propose a novel framework that reformulates Item Response Theory (IRT) for LLM evaluation as constrained matrix factorization, using majorization-minimization for stable and efficient parameter estimation. The method achieves orders-of-magnitude speedups over traditional IRT approaches on benchmarks like MATH-500 and Open LLM Leaderboard. Current LLM evaluation relies on average accuracy, ignoring item heterogeneity and output stochasticity. This framework provides interpretable ability estimates and item characteristics, enabling more principled benchmark design and fairer model comparisons, which is crucial as LLMs become widely deployed. The framework reformulates IRT as a sequence of constrained matrix factorization subproblems, with theoretical guarantees for identifiability and convergence. Experiments show it maintains comparable or higher estimation accuracy while being significantly faster than competing methods.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: Item Response Theory (IRT) is a psychometric paradigm that models the probability of a correct response as a function of latent ability and item parameters (difficulty, discrimination). Traditional IRT estimation methods are computationally expensive and numerically unstable for large-scale LLM evaluation. The proposed approach addresses these limitations by leveraging majorization-minimization and matrix factorization techniques.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Item_response_theory">Item response theory</a></li>

</ul>
</details>

**Tags**: `#Large Language Models`, `#Evaluation`, `#Item Response Theory`, `#Matrix Factorization`, `#Scalability`

---

<a id="item-38"></a>
## [TRACE: Transport Alignment Conformal Prediction via Diffusion and Flow Matching](https://arxiv.org/abs/2605.07100) ⭐️ 8.0/10

TRACE introduces a novel nonconformity score for conformal prediction that leverages transport alignment in diffusion and flow matching models, avoiding restrictive assumptions and likelihood evaluations. This work enables valid and informative conformal prediction regions for multi-dimensional outputs, which is crucial for uncertainty quantification in complex generative models and reliable AI systems. The method averages denoising or velocity-matching errors along stochastic transport trajectories to produce scalar scores, and it is calibrated using split conformal prediction to guarantee marginal coverage under exchangeability.

rss · arXiv - Data Science & Statistics · May 11, 04:00

**Background**: Conformal prediction is a framework that provides finite-sample, distribution-free coverage guarantees for prediction sets. However, existing nonconformity scores for multi-dimensional outputs often rely on restrictive geometric assumptions or require explicit likelihood evaluation, limiting their applicability. Diffusion and flow matching models are generative models that learn data distributions via stochastic transport processes.

**Tags**: `#conformal prediction`, `#diffusion models`, `#flow matching`, `#uncertainty quantification`, `#machine learning`

---