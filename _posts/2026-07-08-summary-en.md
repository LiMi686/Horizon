---
layout: default
title: "Horizon Summary: 2026-07-08 (EN)"
date: 2026-07-08
lang: en
---

> From 104 items, 39 important content pieces were selected

---

1. [TypeScript 7.0 Announced with Up to 11.9x Speedup](#item-1) ⭐️ 9.0/10
2. [GitHub repo leaks system prompts from major AI chatbots](#item-2) ⭐️ 9.0/10
3. [NTK Exponentially Suboptimal for Compositional Learning](#item-3) ⭐️ 9.0/10
4. [Mistral Releases Robostral Navigate for Map-Less Navigation](#item-4) ⭐️ 8.0/10
5. [OpenAI Launches GPT-Live Voice Mode with GPT-5.5 Delegation](#item-5) ⭐️ 8.0/10
6. [OpenBSD use-after-free bug allows local root escalation](#item-6) ⭐️ 8.0/10
7. [EU Revives Private Message Scanning Rules](#item-7) ⭐️ 8.0/10
8. [Cloudflare Meerkat: Leaderless Global Consensus](#item-8) ⭐️ 8.0/10
9. [RuView: See Through Walls with WiFi Signals](#item-9) ⭐️ 8.0/10
10. [Tencent Cloud Launches CubeSandbox for AI Agent Security](#item-10) ⭐️ 8.0/10
11. [.NET Team Releases Curated AI Agent Skills for C#](#item-11) ⭐️ 8.0/10
12. [Kyutai Releases Pocket TTS: CPU-Only Text-to-Speech](#item-12) ⭐️ 8.0/10
13. [Anthropic Launches Official Claude Code Plugin Directory](#item-13) ⭐️ 8.0/10
14. [OpenMed: Local-First Healthcare AI for Clinical NER & HIPAA De-identification](#item-14) ⭐️ 8.0/10
15. [LLMForge: Multi-Model Framework for Text-to-CAD Generation](#item-15) ⭐️ 8.0/10
16. [FirstResearch: Auditable LLM Scientific Questions](#item-16) ⭐️ 8.0/10
17. [In-Process Memory Cuts Latency 1000x for Language Agents](#item-17) ⭐️ 8.0/10
18. [Akashic: Low-Overhead LLM Inference with MemAttention](#item-18) ⭐️ 8.0/10
19. [New Geometric Framework Distinguishes True AI from Pattern Matching](#item-19) ⭐️ 8.0/10
20. [Design-CP Enables Memory-Efficient Protein Nanoparticle Design](#item-20) ⭐️ 8.0/10
21. [Granularity Paradox: Finer Data Hurts Forecast Accuracy](#item-21) ⭐️ 8.0/10
22. [LLM Agent Harness as Learnable Control via Offline RL](#item-22) ⭐️ 8.0/10
23. [Benchmarking KV-Cache Optimizations for Long-Context LLM Serving](#item-23) ⭐️ 8.0/10
24. [LLM Conformity Mostly Due to Repeated Wrong Answers, Not Social Influence](#item-24) ⭐️ 8.0/10
25. [LLM Moral Shifts Are Artifacts of Yes-No Framing](#item-25) ⭐️ 8.0/10
26. [Revisiting PPL-WER Relation in Modern End-to-End ASR](#item-26) ⭐️ 8.0/10
27. [CanvasAgent: AI Agent Orchestrates Visual Tools for Image Creation](#item-27) ⭐️ 8.0/10
28. [Ground3D-LMM: Unified 3D Point Grounding and Metric Reasoning](#item-28) ⭐️ 8.0/10
29. [Natural Dataset Correlations Act as Backdoor Triggers](#item-29) ⭐️ 8.0/10
30. [Bayesian 3DGS with Uncertainty and Adaptive Complexity](#item-30) ⭐️ 8.0/10
31. [MuCoDi: Multi-Teacher Distillation for Edge Pathology AI](#item-31) ⭐️ 8.0/10
32. [Training-Free 3D Shape Abstraction via Generative Models](#item-32) ⭐️ 8.0/10
33. [Unified Theory for Deep Neural Networks Beyond ReLU](#item-33) ⭐️ 8.0/10
34. [Continual Learning: Rethinking Retention for Better Adaptation](#item-34) ⭐️ 8.0/10
35. [Power-Calibrated Framework for LLM Watermarking](#item-35) ⭐️ 8.0/10
36. [Width-Robust Learnability in Mean-Field Bayesian Neural Networks](#item-36) ⭐️ 8.0/10
37. [Boosting with List-Decodable Codes](#item-37) ⭐️ 8.0/10
38. [EmTech AI 2026 Highlights Rise of AI Platforms](#item-38) ⭐️ 8.0/10
39. [New weight loss pill beats oral Ozempic in major trial](#item-39) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TypeScript 7.0 Announced with Up to 11.9x Speedup](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) ⭐️ 9.0/10

Microsoft announced TypeScript 7.0, a major version release that delivers dramatic performance improvements, achieving up to 11.9x speedup on large codebases like VS Code. This release significantly reduces compilation times for large TypeScript projects, enhancing developer productivity and making TypeScript more viable for even larger codebases. The speedup numbers from Microsoft's testing show VS Code going from 125.7s to 10.6s (11.9x), Sentry from 139.8s to 15.7s (8.9x), and other projects seeing 7-9x improvements.

hackernews · DanRosenwasser · Jul 8, 16:06 · [Discussion](https://news.ycombinator.com/item?id=48833715)

**Background**: TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, widely used for large-scale web applications. Version 7.0 represents a major leap in performance, likely due to architectural improvements or a potential rewrite in Rust, as hinted by community discussions.

**Discussion**: The community is highly positive about the performance gains, with users sharing benchmarks and congratulating the team. Some concerns were raised about compatibility with tools like ts-jest and the complexity of tsconfig scoping for mixed environments.

**Tags**: `#TypeScript`, `#performance`, `#programming languages`, `#release`

---

<a id="item-2"></a>
## [GitHub repo leaks system prompts from major AI chatbots](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 9.0/10

A GitHub repository called 'system_prompts_leaks' has been collecting and regularly updating leaked system prompts from major AI providers including Anthropic, OpenAI, Google, and xAI, covering models like Claude Fable 5, GPT-5.5, Gemini 3.5 Flash, and Grok. This repository provides rare transparency into proprietary AI behavior, enabling researchers, developers, and safety advocates to analyze how these models are instructed, which is crucial for understanding AI alignment and prompt engineering. The repository includes diffs between model versions (e.g., Claude Opus 4.8 to Fable 5) and has been featured in The Washington Post, indicating broad impact. It is updated regularly and welcomes pull requests.

rss · GitHub Trending - Daily (All) · Jul 8, 22:57

**Background**: System prompts are hidden instructions that guide an AI chatbot's behavior, often kept secret by companies. Leaking them can reveal how models are aligned, what constraints they have, and how they handle sensitive topics. Prompt engineering is the practice of designing these inputs to achieve desired outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system prompts from Anthropic - Claude Fable 5, Opus 4.8, Claude Code, Claude Design. OpenAI - ChatGPT 5.5 Thinking, GPT 5.5 Instant, Codex. Google - Gemini 3.5 Flash, 3.1 Pro, Antigravity. xAI - Grok, Cursor, Copilot, VS Code, Perplexity, and more. Updated regularly. · GitHub</a></li>
<li><a href="https://learn.snyk.io/lesson/llm-system-prompt-leakage/">System prompt leakage in LLMs | Tutorial and examples | Snyk Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_engineering">Prompt engineering</a></li>

</ul>
</details>

**Tags**: `#AI`, `#system prompts`, `#prompt engineering`, `#transparency`, `#GitHub`

---

<a id="item-3"></a>
## [NTK Exponentially Suboptimal for Compositional Learning](https://arxiv.org/abs/2607.06382) ⭐️ 9.0/10

A new paper proves that the neural tangent kernel (NTK) estimator can require exponentially more samples than optimally trained ReLU networks for compositional tasks, establishing a rigorous dichotomy between Fourier and architectural complexity. This result provides the first quantitative explanation of when and why trained neural networks outperform their NTK limit, a fundamental question in deep learning theory with implications for understanding generalization and designing better architectures. The paper shows that for the depth-L iterated sawtooth function, NTK regression needs Ω(4^L) samples while the minimax optimal rate is polynomial in L. Numerical experiments on sparse parity models confirm a 4-6 orders of magnitude test error gap between two-layer networks and NTK.

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: The neural tangent kernel (NTK) is a kernel that describes the training dynamics of infinitely wide neural networks, allowing them to be analyzed via kernel methods. Compositional learning refers to tasks where the target function can be expressed as a composition of simpler functions, which neural networks are empirically good at but kernel methods struggle with. Minimax rates characterize the best possible worst-case performance of an estimator given a fixed sample size.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_tangent_kernel">Neural tangent kernel - Wikipedia</a></li>
<li><a href="https://lilianweng.github.io/posts/2022-09-08-ntk/">Some Math behind Neural Tangent Kernel | Lil'Log - GitHub Pages Neural Tangent Kernels Overview - emergentmind.com Neural Tangent Kernel (NTK) Overview - emergentmind.com Understanding the Evolution of the Neural Tangent Kernel at ... 16. Neural tangent kernels - University of British Columbia A Brief Introduction to the Neural Tangent Kernel A</a></li>
<li><a href="https://www.stat.cmu.edu/~larry/=sml/minimax.pdf">Minimax Theory 1 Introduction 2 Definitions and Notation</a></li>

</ul>
</details>

**Tags**: `#deep learning theory`, `#neural tangent kernel`, `#compositional learning`, `#minimax rates`, `#ReLU networks`

---

<a id="item-4"></a>
## [Mistral Releases Robostral Navigate for Map-Less Navigation](https://mistral.ai/news/robostral-navigate/) ⭐️ 8.0/10

Mistral AI has released Robostral Navigate, an 8-billion-parameter robotics navigation model that enables robots to navigate without a pre-existing map using only a single RGB camera and natural language instructions. This model achieves state-of-the-art performance on the R2R-CE benchmark and represents a significant step toward unified embodied AI, potentially enabling hobbyists and researchers to build autonomous robots that can navigate unfamiliar environments without costly mapping. Robostral Navigate is trained entirely in simulation and uses a pointing-based navigation approach combined with reinforcement learning for continuous improvement. The model is not openly available, which may limit hobbyist access.

hackernews · ottomengis · Jul 8, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48832212)

**Background**: Traditional robot navigation often relies on pre-built maps of the environment, which can be time-consuming to create and impractical in dynamic settings. Map-less navigation, also known as visual navigation, uses camera input and AI to guide robots without a map, addressing the 'kidnapped robot problem' where a robot must orient itself from an unknown location.

<details><summary>References</summary>
<ul>
<li><a href="https://mistral.ai/news/robostral-navigate/">Robostral Navigate: single-camera AI navigation | Mistral AI</a></li>
<li><a href="https://cryptobriefing.com/mistral-robostral-navigate-robotics-model/">Mistral AI unveils Robostral Navigate, an 8B robotics model that could reshape industrial automation investing</a></li>
<li><a href="https://x.com/MistralAI/status/2074856309438980145">Mistral AI on X: "Announcing Robostral Navigate, our first model for embodied navigation: an 8B robotics navigation model that guides robots to autonomously perform tasks specified with natural language. Single RGB camera. State-of-the-art on R2R-CE. https://t.co/UlmUsXNxhX" / X</a></li>

</ul>
</details>

**Discussion**: The community is excited about the map-less navigation capability, with many expressing interest in using it for hobbyist projects like farm robots. However, some note that the model is not openly available, and concerns about privacy (e.g., stalking) were raised regarding similar vision-based geolocation models.

**Tags**: `#robotics`, `#navigation`, `#AI`, `#Mistral`, `#deep learning`

---

<a id="item-5"></a>
## [OpenAI Launches GPT-Live Voice Mode with GPT-5.5 Delegation](https://openai.com/index/introducing-gpt-live/) ⭐️ 8.0/10

OpenAI announced GPT-Live, a new full-duplex voice mode for ChatGPT that can delegate complex queries to GPT-5.5 in the background, enabling longer and more productive conversations. The mode is available as GPT-Live-1 for paid users and GPT-Live-1-mini for free users. This advancement bridges the gap between voice assistants and frontier AI models, allowing users to have natural, real-time conversations without sacrificing intelligence. It could significantly boost productivity for hands-free tasks like brainstorming, research, and note-taking. GPT-Live uses a full-duplex architecture, meaning it can listen and speak simultaneously, and it can show attentiveness with phrases like "mhmm" or stay quiet when needed. However, the initial release lacks tool integration, meaning users cannot access connectors, documents, or apps during voice mode.

hackernews · logickkk1 · Jul 8, 17:03 · [Discussion](https://news.ycombinator.com/item?id=48834405)

**Background**: Previous voice modes in ChatGPT were limited to a separate, less capable model that lagged behind the latest text-based models. GPT-Live solves this by delegating complex tasks to GPT-5.5, OpenAI's most advanced model released in April 2026, which excels at coding, research, and data analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-gpt-live/">Introducing GPT-Live | OpenAI</a></li>
<li><a href="https://openai.com/index/introducing-gpt-5-5/">Introducing GPT‑5.5 - OpenAI</a></li>
<li><a href="https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/">OpenAI releases new voice models for more natural live ...</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users praise the natural conversation flow and background delegation, while others criticize the lack of tool integration and express philosophical concerns about AI replacing human relationships. A notable bug report involves the model interrupting and laughing inappropriately.

**Tags**: `#OpenAI`, `#voice AI`, `#GPT-Live`, `#AI assistants`, `#productivity`

---

<a id="item-6"></a>
## [OpenBSD use-after-free bug allows local root escalation](https://nvd.nist.gov/vuln/detail/cve-2026-57589) ⭐️ 8.0/10

A use-after-free vulnerability (CVE-2026-57589) in OpenBSD allows a local attacker to escalate privileges to root. The bug was discovered as part of OpenAI's Patch the Planet initiative in collaboration with Trail of Bits. This vulnerability is significant because OpenBSD is renowned for its security focus, and a local privilege escalation to root undermines its security guarantees. It also highlights the growing role of AI-assisted bug finding in open-source security. The vulnerability is a use-after-free, a common memory corruption issue where a program continues to use a pointer after the memory it points to has been freed. The exploit requires local access, meaning an attacker must already have a user account on the system.

hackernews · linggen · Jul 8, 13:24 · [Discussion](https://news.ycombinator.com/item?id=48831658)

**Background**: A use-after-free vulnerability occurs when a program dereferences a pointer that points to memory that has already been freed, potentially leading to arbitrary code execution. OpenBSD has a strong security record, famously claiming only two remote holes in the default install in over two decades. The Patch the Planet initiative pairs AI models from OpenAI with security engineers from Trail of Bits to find and fix vulnerabilities in critical open-source projects.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/patch-the-planet/">Patch the Planet: a Daybreak initiative to support open ...</a></li>
<li><a href="https://learn.snyk.io/lesson/use-after-free/">Use after free vulnerability | Tutorial & Examples | Snyk Learn</a></li>

</ul>
</details>

**Discussion**: Community members noted that the bug was found via Patch the Planet, an OpenAI and Trail of Bits initiative. Some praised OpenBSD's security culture, while others questioned why the vulnerability wasn't listed on OpenBSD's security page yet.

**Tags**: `#OpenBSD`, `#security`, `#vulnerability`, `#privilege escalation`, `#AI-assisted bug finding`

---

<a id="item-7"></a>
## [EU Revives Private Message Scanning Rules](https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/) ⭐️ 8.0/10

The European Parliament has approved an urgent procedure to fast-track legislation that would revive the EU's expired 'Chat Control 1.0' rules, allowing online platforms to voluntarily scan private communications for child sexual abuse material (CSAM). A decisive vote is scheduled for July 9. This move threatens end-to-end encryption (E2EE) and could set a precedent for mass surveillance of private communications, impacting privacy and civil liberties for millions of EU citizens and potentially influencing global encryption policies. The urgent procedure passed with 331 votes in favor and 304 against, indicating deep division. The revived rules are voluntary for now, but a more mandatory 'Chat Control 2.0' is also being discussed, which would mandate scanning and ban E2EE.

hackernews · ggirelli · Jul 8, 16:53 · [Discussion](https://news.ycombinator.com/item?id=48834296)

**Background**: Chat Control refers to EU legislative proposals to combat child sexual abuse material (CSAM) by requiring or allowing platforms to scan private messages. End-to-end encryption ensures only the communicating users can read messages, and scanning would break that privacy. The debate pits child protection against privacy rights.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberinsider.com/eu-now-one-step-away-from-reviving-private-message-scanning-rules/">EU now one step away from reviving private message scanning rules</a></li>
<li><a href="https://cybernews.com/security/chat-control-eu-scanning-messages/">Will the EU start scanning your private messages? - Cybernews</a></li>
<li><a href="https://cyberscoop.com/potential-eu-law-sparks-global-concerns-encryption-privacy/">Potential EU law sparks global concerns over end-to-end ...</a></li>

</ul>
</details>

**Discussion**: Commenters express strong opposition, with some noting that the Internet Watch Foundation is pushing for client-side scanning. Others call this 'Terminator legislation' that will keep returning, and distinguish between voluntary Chat Control 1.0 and the more dangerous mandatory 2.0. One user urges EU citizens to contact representatives via fightchatcontrol.eu.

**Tags**: `#privacy`, `#encryption`, `#EU legislation`, `#surveillance`, `#technology policy`

---

<a id="item-8"></a>
## [Cloudflare Meerkat: Leaderless Global Consensus](https://blog.cloudflare.com/meerkat-introduction/) ⭐️ 8.0/10

Cloudflare Research has introduced Meerkat, a globally distributed consensus service based on the QuePaxa algorithm, which achieves leaderless asynchronous consensus without relying on timeouts. This is the first production implementation of an asynchronous consensus algorithm (QuePaxa), which can maintain progress even under extreme network fluctuations, potentially improving reliability for globally distributed systems. Meerkat uses hedging to launch redundant operations across nodes, and it orders all operations (including reads) through global consensus, which may increase read latency but simplifies consistency.

hackernews · bobnamob · Jul 8, 13:18 · [Discussion](https://news.ycombinator.com/item?id=48831565)

**Background**: Traditional consensus protocols like Paxos and Raft rely on timeouts and leaders to make progress, which can fail under network asynchrony. Asynchronous consensus protocols like QuePaxa avoid timeouts entirely, making them more robust in adverse conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.cloudflare.com/meerkat-introduction/">Introducing Meerkat: an experiment in global consensus</a></li>
<li><a href="https://bford.info/pub/os/quepaxa/quepaxa.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus QuePaxa: Escaping the Tyranny of Timeouts in Consensus GitHub - dedis/quepaxa: This is the code repository for ... September 4, 2024 “Next-Generation Secure Distributed ... QuePaxa: Escaping the tyranny of timeouts in consensus Artifact Review Summary: QuePaxa: Escaping the tyranny of ...</a></li>
<li><a href="https://expolab.org/ecs265-fall-2023/slices/QuePaxa-DDS.pdf">QuePaxa: Escaping the Tyranny of Timeouts in Consensus</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Meerkat is the first production implementation of an asynchronous consensus algorithm, with some questioning its performance for reads and others appreciating its robustness for messy networks. There was also skepticism about building custom consensus in production.

**Tags**: `#distributed systems`, `#consensus`, `#cloudflare`, `#asynchronous`, `#quePaxa`

---

<a id="item-9"></a>
## [RuView: See Through Walls with WiFi Signals](https://github.com/ruvnet/RuView) ⭐️ 8.0/10

RuView is an open-source platform that uses commodity WiFi signals to detect people, monitor vital signs like breathing and heart rate, and track movement through walls without cameras or wearables. This technology enables privacy-preserving spatial intelligence for smart homes, healthcare, and elderly care, potentially replacing cameras in sensitive areas while providing richer data. RuView integrates with Home Assistant, Apple Home, Google Home, and Alexa via MQTT or Matter bridge, and ships 21 entities per node including inferred states like 'someone-sleeping' and 'fall-risk-elevated'.

rss · GitHub Trending - Daily (All) · Jul 8, 22:57

**Background**: WiFi sensing uses Channel State Information (CSI) from standard WiFi signals to detect changes in the environment caused by human presence and movement. Unlike cameras, it works through walls and in darkness, preserving privacy. The technology has been advancing with AI, enabling pose estimation and vital sign monitoring from commodity hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ruvnet/RuView">GitHub - ruvnet/RuView: π RuView turns commodity WiFi signals ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/WiFi_Sensing">WiFi Sensing - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2024/02/27/1088154/wifi-sensing-tracking-movements/">How Wi-Fi sensing became usable tech - MIT Technology Review</a></li>

</ul>
</details>

**Tags**: `#WiFi sensing`, `#spatial intelligence`, `#privacy-preserving`, `#smart home`, `#computer vision`

---

<a id="item-10"></a>
## [Tencent Cloud Launches CubeSandbox for AI Agent Security](https://github.com/TencentCloud/CubeSandbox) ⭐️ 8.0/10

Tencent Cloud has open-sourced CubeSandbox, an instant, concurrent, secure, and lightweight sandbox service built on RustVMM and KVM, designed specifically for AI agents. As AI agents become more autonomous, sandboxing is critical to prevent malicious code execution and data breaches; CubeSandbox provides hardware-level isolation with sub-60ms startup and under 5MB memory overhead, making it practical for production use. CubeSandbox supports both single-node and multi-node cluster deployment, is compatible with the E2B SDK, and has been accepted into the CNCF Landscape. It is licensed under Apache 2.0 and available on PyPI.

rss · GitHub Trending - Daily (All) · Jul 8, 22:57

**Background**: AI agents often need to execute untrusted code or access external tools, which poses security risks. Sandboxing isolates these executions in a secure environment. Traditional sandboxes can be slow or resource-heavy, but CubeSandbox uses microVM technology (RustVMM + KVM) to achieve fast startup and low overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/TencentCloud/CubeSandbox">GitHub - TencentCloud/CubeSandbox: Instant, Concurrent ...</a></li>
<li><a href="https://docs.cubesandbox.com/">Cube Sandbox</a></li>
<li><a href="https://northflank.com/blog/how-to-sandbox-ai-agents">How to sandbox AI agents in 2026: MicroVMs, gVisor ...</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Sandbox`, `#Security`, `#Cloud Computing`, `#Tencent Cloud`

---

<a id="item-11"></a>
## [.NET Team Releases Curated AI Agent Skills for C#](https://github.com/dotnet/skills) ⭐️ 8.0/10

Microsoft's .NET team has released a curated set of skills and custom agents for AI coding agents on GitHub, covering areas like C# language server integration, debugging, NuGet management, and .NET MAUI development. This official repository provides developers with production-ready, standardized skills that can significantly improve AI-assisted .NET development, reducing boilerplate and ensuring best practices. The repository includes 12 plugins such as dotnet, dotnet-advanced, dotnet-data, dotnet-diag, dotnet-msbuild, dotnet-nuget, dotnet-upgrade, dotnet-maui, dotnet-ai, dotnet-template-engine, dotnet-test, and dotnet-test-migration, each targeting specific .NET development tasks.

rss · GitHub Trending - Daily (All) · Jul 8, 22:57

**Background**: AI coding agents are tools that use large language models to automate software development tasks. The Agent Skills standard, originally developed by Anthropic, provides a format for packaging reusable skills that agents can execute. This repository follows that standard, making the skills compatible with multiple agent platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills Overview - Agent Skills</a></li>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>

</ul>
</details>

**Tags**: `#.NET`, `#AI Agents`, `#C#`, `#Developer Tools`, `#GitHub`

---

<a id="item-12"></a>
## [Kyutai Releases Pocket TTS: CPU-Only Text-to-Speech](https://github.com/kyutai-labs/pocket-tts) ⭐️ 8.0/10

Kyutai Labs has open-sourced Pocket TTS, a lightweight text-to-speech library with only 100 million parameters that runs efficiently on CPUs, achieving ~6x real-time speed on a MacBook Air M4. It supports voice cloning, audio streaming, and multiple languages including English, French, German, Portuguese, Italian, and Spanish. Pocket TTS democratizes high-quality TTS by eliminating the need for GPUs or cloud APIs, enabling on-device inference for privacy-sensitive and offline applications. Its small size and low latency make it suitable for edge devices, accessibility tools, and real-time assistants. The model has 100 million parameters, uses only 2 CPU cores, and achieves ~200ms latency to first audio chunk. It supports Python 3.10–3.14, requires PyTorch 2.5+, and can run in-browser via client-side implementations.

rss · GitHub Trending - Daily (All) · Jul 8, 22:57

**Background**: Traditional TTS systems often require powerful GPUs or paid cloud APIs, limiting their use on personal devices or in privacy-focused scenarios. Pocket TTS is part of a growing trend of CPU-efficient AI models that bring advanced capabilities to everyday hardware. Kyutai Labs is a French nonprofit AI research lab known for open-source releases.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/kyutai-labs/pocket-tts">GitHub - kyutai-labs/pocket-tts: A TTS that fits in your CPU ...</a></li>
<li><a href="https://kyutai.org/pocket-tts/">Pocket TTS: a high-quality TTS with voice cloning that runs ...</a></li>
<li><a href="https://kyutai.org/tts/">Kyutai TTS</a></li>

</ul>
</details>

**Tags**: `#text-to-speech`, `#machine learning`, `#open source`, `#CPU inference`, `#audio generation`

---

<a id="item-13"></a>
## [Anthropic Launches Official Claude Code Plugin Directory](https://github.com/anthropics/claude-plugins-official) ⭐️ 8.0/10

Anthropic has released an official, curated directory of high-quality plugins for Claude Code on GitHub, including both internal and third-party plugins. Users can install plugins directly via the Claude Code plugin system using commands like `/plugin install {name}@claude-plugins-official`. This marks a significant step toward a structured ecosystem for Claude Code, enabling developers to easily extend its capabilities with trusted plugins. It could accelerate adoption of Claude Code in software engineering workflows by providing a centralized marketplace for tools and integrations. The directory is split into `/plugins` for Anthropic-maintained plugins and `/external_plugins` for third-party submissions, which must meet quality and security standards. Plugin names are immutable slugs, but renames can be handled via a `renames` map in the marketplace configuration.

rss · GitHub Trending - Python · Jul 8, 22:57

**Background**: Claude Code is an AI-powered coding assistant developed by Anthropic, and plugins extend its functionality with custom slash commands, agents, skills, and MCP servers. The Model Context Protocol (MCP) is an open standard for connecting AI models to external tools and data sources. This directory provides a structured way to discover and install such extensions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-plugins-official">anthropics/claude-plugins-official - GitHub</a></li>
<li><a href="https://claude.com/plugins">Plugins for Claude | Claude by Anthropic</a></li>
<li><a href="https://github.com/anthropics/claude-code/tree/main/plugins">claude-code/plugins at main · anthropics/claude-code · GitHub</a></li>

</ul>
</details>

**Tags**: `#Claude Code`, `#plugins`, `#AI tools`, `#developer tools`, `#Anthropic`

---

<a id="item-14"></a>
## [OpenMed: Local-First Healthcare AI for Clinical NER & HIPAA De-identification](https://github.com/maziyarpanahi/openmed) ⭐️ 8.0/10

OpenMed is an open-source toolkit that provides 1,000+ medical models for clinical named entity recognition (NER) and HIPAA-compliant PII de-identification, running entirely on-device without cloud dependency. This addresses critical privacy and compliance needs in healthcare AI by enabling sensitive patient data to stay on-premises, reducing risk of data breaches and simplifying HIPAA compliance for developers and healthcare institutions. The toolkit supports 12 languages, includes 247 PII checkpoints, and can be used via Python, Swift, REST services, or browser-based Transformers.js with WebGPU acceleration.

rss · GitHub Trending - Python · Jul 8, 22:57

**Background**: Clinical NER extracts medical entities like diseases and medications from unstructured text, while HIPAA PII de-identification removes personal identifiers to protect patient privacy. Traditional cloud-based AI solutions require sending data externally, which poses compliance risks. OpenMed leverages Apple's MLX framework for on-device inference on Apple Silicon, and also supports other platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ml-explore/mlx">GitHub - ml-explore/mlx: MLX: An array framework for Apple ... Exploring LLMs with MLX and the Neural Accelerators in the M5 ... MLX MLX — MLX 0.32.0 documentation - GitHub Pages What Is MLX? A Practical Introduction to Apple's Machine ... mlx · PyPI</a></li>
<li><a href="https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html">Guidance Regarding Methods for De-identification of Protected ... 45 CFR 164.514 -- Other requirements relating to uses and ... De-identification of Protected Health Information: 2026 Update Guidance on De-identification of Protected Health Information HIPAA PII Identifiers: Mapping General PII to PHI’s 18 ... De-Identification: The Ultimate Guide to Protecting Privacy ... Overview of the De-identification Service in Azure Health ...</a></li>

</ul>
</details>

**Tags**: `#healthcare AI`, `#NER`, `#privacy`, `#HIPAA`, `#open source`

---

<a id="item-15"></a>
## [LLMForge: Multi-Model Framework for Text-to-CAD Generation](https://arxiv.org/abs/2607.05573) ⭐️ 8.0/10

LLMForge is a multi-model text-to-CAD framework that integrates LLMs and VLMs to generate parametric 3D designs from natural language, evaluated on a benchmark of 97 engineering problems with two critique regimes: IterTracer (analytic visual metrics) and IterVision (VLM semantic critic). This work bridges the gap between natural language and parametric CAD design, potentially automating mechanical part design and reducing manual effort in engineering workflows. The multi-model approach and iterative refinement could enable scalable, automated design for industrial applications. The framework uses JSON-schema validation, analytic feature scoring, mesh synthesis, and multi-round iterative refinement. Under IterTracer, the top four models achieved a mean score of 0.885–0.890 with 98.97% mesh success; IterVision with Qwen2.5-VL-72B achieved 100% watertight mesh generation but struggled with rotationally symmetric geometries like cylinders.

rss · arXiv - AI · Jul 8, 04:00

**Background**: Computer-Aided Design (CAD) is essential for mechanical part design, but generating parametric models from text descriptions remains challenging. Large Language Models (LLMs) and Vision-Language Models (VLMs) have shown promise in code generation and visual reasoning, making them suitable for automating CAD generation. This paper introduces a benchmark of 97 engineering problems spanning four geometry families to evaluate text-to-CAD systems.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05573v1">Foundation Models for Automatic CAD Generation - arXiv.org</a></li>
<li><a href="https://aissential.tech/articles/784de9fd-8381-4992-ac6f-343e3cfa5e4f">Foundation Models for Automatic CAD Generation — AIssential</a></li>
<li><a href="https://www.risewave.com/foundation-models-for-automatic-cad-generation/">Foundation Models for Automatic CAD Generation</a></li>

</ul>
</details>

**Tags**: `#CAD generation`, `#foundation models`, `#LLM`, `#VLM`, `#3D design`

---

<a id="item-16"></a>
## [FirstResearch: Auditable LLM Scientific Questions](https://arxiv.org/abs/2607.05682) ⭐️ 8.0/10

FirstResearch introduces a structured Research Question Certificate that records primitive definitions, assumptions, mechanism model, falsifiable hypothesis, minimal decisive test, and failure update rule, making LLM-generated scientific hypotheses auditable before execution. This framework addresses a critical gap in transparency and reproducibility of AI-assisted scientific discovery, potentially enabling researchers to trust and inspect LLM-generated hypotheses before costly experiments. In evaluations using DeepSeek and Gemini judges, FirstResearch scored 4.86/5 vs 4.38/5 for the strongest baseline, and removing the certificate dropped scores below 1/5, highlighting the certificate's importance.

rss · arXiv - AI · Jul 8, 04:00

**Background**: LLM agents for scientific discovery often generate research questions that sound plausible but lack explicit mechanisms, falsifiers, or assumptions, making them hard to audit. Falsifiability is a key principle in science: a hypothesis must be testable and potentially disprovable. FirstResearch enforces this by requiring a falsifiable hypothesis and a minimal decisive test in its certificate.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05682v1">Auditable Question Formation for LLM Scientific Discovery Agents - arXiv</a></li>
<li><a href="https://en.wikipedia.org/wiki/Falsifiability">Falsifiability - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#scientific discovery`, `#auditability`, `#AI agents`, `#research methodology`

---

<a id="item-17"></a>
## [In-Process Memory Cuts Latency 1000x for Language Agents](https://arxiv.org/abs/2607.05690) ⭐️ 8.0/10

A new paper proposes moving memory inside the language agent loop using in-process stores, achieving ~100 microsecond retrieval latency—three orders of magnitude faster than networked stores. Experiments show this reduces redundant actions from 7.2/12 to 0.0/12 and improves recall from 0/5 to 3.6-4.8/5 across GPT-5-class models. This paradigm shift addresses a fundamental latency bottleneck in language agent design, enabling memory to function as extended working memory rather than an external tool. It could significantly improve the efficiency and reliability of AI agents that rely on iterative reasoning and action loops. The in-process store achieved p50 latency of 80-165 microseconds for store operations, while the dominant per-step cost shifted to embedding (~200-400ms over network). Pairing with a small local embedder reduced complete operation to ~40 microseconds. The store never lost a fact in 244 writes; all misses were due to the agent's read policy.

rss · arXiv - AI · Jul 8, 04:00

**Background**: Language agents operate in a loop—observe, reason, act—but traditionally query external memory stores once per turn, incurring tens to hundreds of milliseconds latency. The extended-mind thesis suggests that if a tool is constantly and directly available, it becomes part of the cognitive system. This paper applies that principle to agent memory by using in-process stores that are fast enough to be treated as extended working memory.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05690">[2607.05690] Memory in the Loop: In-Process Retrieval as ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Extended_mind_thesis">Extended mind thesis - Wikipedia</a></li>
<li><a href="https://layra4.dev/pattern/agent-loop">Agent Loop Pattern: The Think-Act-Observe Cycle Behind LLM ...</a></li>

</ul>
</details>

**Tags**: `#language agents`, `#memory systems`, `#latency optimization`, `#AI architecture`

---

<a id="item-18"></a>
## [Akashic: Low-Overhead LLM Inference with MemAttention](https://arxiv.org/abs/2607.05708) ⭐️ 8.0/10

Akashic introduces MemAttention, a memory system that organizes context into bounded chunks with semantic relationships, improving LLM inference efficiency and accuracy without replaying full history. This addresses a critical bottleneck in LLM-based agent systems where long contexts degrade performance, potentially enabling more efficient and scalable multi-turn interactions and tool use. Akashic uses hardware-software co-designed memory placement to co-locate likely co-retrieved chunks, reducing I/O overhead. It achieves up to 10.2 points accuracy improvement, 1.21x throughput gain, and 1.88x sustainable request rate over prior baselines.

rss · arXiv - AI · Jul 8, 04:00

**Background**: LLM-based agent systems accumulate context over multiple turns, tool calls, and sessions. Replaying full history for each request is costly and can exceed context limits, hurting efficiency and accuracy. MemAttention organizes context into bounded chunks and models cross-chunk semantic relationships, preserving relevant evidence without full replay.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05708">Akashic: A Low-Overhead LLM Inference Service with MemAttention</a></li>
<li><a href="https://theaicronicle.com/en/news/tools/akashic-memattention-llm-inference-efficiency">Akashic: Revolutionizing LLM Memory with MemAttention</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#memory management`, `#agent systems`, `#hardware-software co-design`, `#context optimization`

---

<a id="item-19"></a>
## [New Geometric Framework Distinguishes True AI from Pattern Matching](https://arxiv.org/abs/2607.05436) ⭐️ 8.0/10

A new paper introduces Statistically Meaningful Geometry (SMG), a fiber bundle framework that models over-parameterized learning systems as infinite-dimensional non-parametric Orlicz fiber bundles, and proves that under persistent out-of-distribution stimuli, continuous optimization fails and triggers a gauge symmetry break, leading to the emergence of new causal axes. This work provides a potential mathematical foundation to certify whether large models like LLMs exhibit genuine intelligence or merely sophisticated pattern matching, which could transform AI for Science into an engine of autonomous paradigm shifts. The framework predicts a critical time T_crit = π^2 / K_max for the onset of gauge symmetry breaking, and uses a Structural G-Entropy step-jump of +1.0 to signal genuine discovery. It also introduces a Minimal Energy Path Criterion and a Causal Invariance Filter to distinguish discovery from hallucination.

rss · arXiv - Machine Learning · Jul 8, 04:00

**Background**: Fiber bundles are a topological concept where a total space locally looks like a product of a base space and a fiber. Information geometry uses statistical manifolds to study probability distributions. Over-parameterized models like LLMs have many parameters, raising questions about whether they truly understand or just interpolate data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05436">[2607.05436] Statistically Meaningful Geometry and Gauge ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fiber_bundle">Fiber bundle - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2210.07641.pdf">AFFINE STATISTICAL BUNDLE MODELED ON A GAUSSIAN ORLICZ ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#geometry`, `#intelligence`, `#statistical learning`, `#theoretical AI`

---

<a id="item-20"></a>
## [Design-CP Enables Memory-Efficient Protein Nanoparticle Design](https://arxiv.org/abs/2607.05439) ⭐️ 8.0/10

Design-CP introduces two context-parallel inference strategies for RFdiffusion 3 that distribute quadratic activations across multiple GPUs, enabling the design of large protein nanoparticles that previously exceeded single-GPU memory limits. This work addresses a key memory bottleneck in all-atom generative protein models, making it feasible to design large multimeric complexes like icosahedral nanoparticles on modest GPU clusters, which could democratize computational structural biology. The two strategies are 1D row-sharding and 2D grid sharding with ring attention; 2D sharding achieves better wall-clock scaling. The method preserves pretrained weights and works out of the box with strong point-group symmetry constraints.

rss · arXiv - Machine Learning · Jul 8, 04:00

**Background**: RFdiffusion 3 is a generative protein model that can design large multimeric complexes, but its quadratic token- and atom-pair representations cause memory to grow rapidly with chain count. Context parallelism (CP) is a technique that partitions input tensors along the sequence dimension across GPUs, reducing peak memory usage. Ring attention is a specific CP variant that overlaps communication with computation for efficient scaling.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ipd.uw.edu/2025/12/rfdiffusion3-now-available/">RFdiffusion3 now available – Institute for Protein Design</a></li>
<li><a href="https://arxiv.org/abs/2411.01783">[2411.01783] Context Parallelism for Scalable Million-Token ...</a></li>
<li><a href="https://arxiv.org/abs/2310.01889">[2310.01889] Ring Attention with Blockwise Transformers for ...</a></li>

</ul>
</details>

**Tags**: `#protein design`, `#parallel computing`, `#generative models`, `#structural biology`, `#deep learning`

---

<a id="item-21"></a>
## [Granularity Paradox: Finer Data Hurts Forecast Accuracy](https://arxiv.org/abs/2607.05450) ⭐️ 8.0/10

A new paper formalizes the 'Granularity Paradox' in time-series forecasting, showing that finer temporal disaggregation (e.g., monthly to daily) improves in-sample fit but degrades out-of-sample accuracy due to recursive error compounding. This challenges the common practice of using higher-frequency data to improve forecasts, revealing a fundamental trade-off that practitioners must consider when choosing data granularity. The study benchmarks 10 models across six granularities on a 13-year public procurement dataset, finding that recursive autoregressive and seasonal models degrade severely at high frequencies, while LSTM shows a U-shaped error curve and Linear Regression remains stable.

rss · arXiv - Machine Learning · Jul 8, 04:00

**Background**: Time-series forecasting often uses recursive multi-step forecasting, where each prediction feeds into the next, causing errors to compound. The paper introduces a consensus-dissensus diagnostic to identify models whose standard metrics mask cumulative error propagation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05450v1">The Granularity Paradox: How Temporal Disaggregation Inflates ...</a></li>
<li><a href="https://letsdatascience.com/blog/multi-step-time-series-forecasting-recursive-direct-and-hybrid-strategies">Multi-Step Time Series Forecasting: Recursive vs Direct</a></li>
<li><a href="https://openforecast.org/2024/05/25/recursive-vs-direct-forecasting-strategy/">Recursive vs Direct Forecasting Strategy - Open Forecasting</a></li>

</ul>
</details>

**Tags**: `#time-series forecasting`, `#machine learning`, `#granularity`, `#recursive error`, `#empirical study`

---

<a id="item-22"></a>
## [LLM Agent Harness as Learnable Control via Offline RL](https://arxiv.org/abs/2607.05458) ⭐️ 8.0/10

This paper proposes treating the LLM agent execution harness as a learnable MDP controller trained via offline reinforcement learning, introducing a new metric called Harness Maturity Score to separate task quality from harness behavior. This work opens a new direction for improving LLM agents by optimizing the harness control layer rather than just prompts or models, potentially leading to more reliable and efficient agent systems. The controller is trained using advantage-weighted regression from offline rollouts with only terminal task-rubric rewards, and experiments across six domains show consistent improvements in verification behavior and selective gains in final task quality.

rss · arXiv - Machine Learning · Jul 8, 04:00

**Background**: LLM agents typically consist of a language model and an execution harness that manages tool calls, memory, and workflow. Traditionally, the harness is hand-crafted and fixed, while improvements focus on the model or prompts. This paper formalizes the harness as a Markov decision process (MDP) that can be optimized via offline reinforcement learning, using advantage-weighted regression (AWR) to learn a lightweight controller from pre-collected data.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xbpeng/awr">GitHub - xbpeng/awr: Implementation of advantage-weighted ... A -WEIGHTED REGRESSION: SIMPLE AND O -P REINFORCEMENT ... Advantage-Weighted Regression: Simple and Scalable Off-Policy ... Advantage Weighted Regression: Simple and Scalable Off-Policy ... 离线强化学习(Offline RL)系列3: (算法篇) AWR(Advantage-Weighted ..... Advantage-Weighted Regression (AWR) - emergentmind.com</a></li>
<li><a href="https://arxiv.org/pdf/1910.00177">A -WEIGHTED REGRESSION: SIMPLE AND O -P REINFORCEMENT ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#reinforcement learning`, `#offline RL`, `#control`, `#harness`

---

<a id="item-23"></a>
## [Benchmarking KV-Cache Optimizations for Long-Context LLM Serving](https://arxiv.org/abs/2607.05399) ⭐️ 8.0/10

A new benchmark systematically compares KV-cache compression techniques (KIVI, TurboQuant, SnapKV, CaM) on long-context LLM serving, revealing that compression ratio alone is a poor predictor of end-to-end performance. This benchmark provides actionable guidance for practitioners deploying long-context LLMs, showing that workload-aware selection of KV-cache mechanisms is crucial rather than one-size-fits-all compression. The evaluation uses Llama-3.1-8B-Instruct and Mistral-7B-Instruct-v0.3 on LongBench-style tasks, measuring task quality, throughput, time-to-first-token, and realized compression ratio across context-length buckets.

rss · arXiv - NLP · Jul 8, 04:00

**Background**: KV-cache stores key-value pairs from previous tokens to accelerate attention computation in LLMs, but its memory footprint grows linearly with context length, becoming a bottleneck for long-context serving. Compression techniques like quantization, pruning, and merging aim to reduce this memory usage, but their effectiveness varies across workloads and metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2603.20397">KV Cache Optimization Strategies for Scalable and Efficient ...</a></li>
<li><a href="https://arxiv.org/html/2508.06297v1">KV Cache Compression for Inference Efficiency in LLMs: A Review</a></li>
<li><a href="https://github.com/THUDM/LongBench">GitHub - THUDM/LongBench: LongBench v2 and LongBench (ACL 25 ...</a></li>

</ul>
</details>

**Tags**: `#KV-cache`, `#LLM serving`, `#benchmarking`, `#long-context`, `#compression`

---

<a id="item-24"></a>
## [LLM Conformity Mostly Due to Repeated Wrong Answers, Not Social Influence](https://arxiv.org/abs/2607.05545) ⭐️ 8.0/10

A new paper introduces a speaker-free condition to show that 66.5% of LLM conformity effects persist even after removing the peer speaker, revealing a confound in standard benchmarks that conflate repeated wrong answers with social influence. This finding challenges the common interpretation of LLM conformity as social influence, with implications for AI safety and benchmark design, as models may be more susceptible to repeated misinformation than to peer pressure. The study tested six open-weight LLMs across seven QA and reasoning datasets, finding that the speaker-free condition caused harmful revision in 66.5% of initially correct cases, compared to 10.3% under a plain re-ask. The effect persisted even with paraphrased answers and in open-ended settings.

rss · arXiv - NLP · Jul 8, 04:00

**Background**: LLM conformity benchmarks typically present a model with a question and a peer's wrong answer, then measure how often the model changes its correct answer to match the peer. This paper reveals that such benchmarks conflate two cues: the presence of a speaker and the repeated wrong answer itself, making it impossible to attribute changes to social influence alone.

<details><summary>References</summary>
<ul>
<li><a href="https://paperreading.club/page?id=423273">Most LLM Conformity Needs No Speaker: Measuring the Speaker ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#conformity`, `#benchmarking`, `#AI safety`, `#NLP`

---

<a id="item-25"></a>
## [LLM Moral Shifts Are Artifacts of Yes-No Framing](https://arxiv.org/abs/2607.05552) ⭐️ 8.0/10

A new paper introduces a crossed symmetrization method to show that frontier LLMs' moral judgments are nearly invariant to wording and answer order, while small models exhibit model-specific biases. This work challenges prior claims that LLMs have unstable moral reasoning, revealing that apparent shifts are due to yes-no bias rather than genuine changes in judgment, which has implications for AI alignment and evaluation. The method recovers a coherent internal moral scale for frontier models with cross-form incoherence of 0.12–0.21 on a ±1 axis, and shows that the yes-no artifact is substantial only in Claude models (story-averaged -0.32 to -0.86), while being near zero for GPT-5.5 and Gemini.

rss · arXiv - NLP · Jul 8, 04:00

**Background**: Large language models are increasingly used to make binary moral judgments, but prior work reported that their answers shift under logically irrelevant changes in wording, such as swapping yes/no labels. This raised concerns about the reliability of LLM moral reasoning. The new paper uses a psychometric battery called crossed symmetrization to disentangle the effect of question framing from the model's underlying moral stance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05552v1">The yes–no bias of large language models reflects answer ...</a></li>
<li><a href="https://www.siliconreport.com/llm-moral-shifts-are-an-artifact-of-yes-no-question-framing-5aaa0715">LLM 'Moral Shifts' Are an Artifact of Yes-No Question Framing</a></li>
<li><a href="https://www.pnas.org/doi/10.1073/pnas.2412015122">Large language models show amplified cognitive biases in ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#moral judgment`, `#bias`, `#psychometrics`, `#AI alignment`

---

<a id="item-26"></a>
## [Revisiting PPL-WER Relation in Modern End-to-End ASR](https://arxiv.org/abs/2607.05612) ⭐️ 8.0/10

A new paper re-evaluates the linear relationship between language model perplexity (PPL) and ASR word error rate (WER) for modern end-to-end systems, including those using LLMs, and finds that internal language modeling capacity changes this relation. This challenges a long-held assumption in ASR research and could influence how language models are integrated into modern end-to-end systems, especially with the rise of LLMs. The study shows that internal language model (ILM) subtraction changes the observed PPL-WER relation, indicating that the decoder's internal LM must be considered when interpreting external LM quality. It also examines how encoder context length and LLM perplexities fit into the trend.

rss · arXiv - NLP · Jul 8, 04:00

**Background**: Historically, language model perplexity (PPL) has been used as a proxy for ASR word error rate (WER), with a roughly linear relationship in log-log space. Modern end-to-end ASR systems, such as attention-based encoder-decoder models, already contain internal language modeling capacity, which complicates this relationship. External LMs, including neural LMs and LLMs, can be combined with these systems through different strategies like ILM subtraction.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05612">[2607.05612] Revisiting the Relation Between Language Model ...</a></li>
<li><a href="https://arxiv.org/abs/2102.01380">Internal Language Model Training for Domain-Adaptive End-to ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0167639301000413">Testing the correlation of word error rate and perplexity</a></li>

</ul>
</details>

**Tags**: `#ASR`, `#language model`, `#perplexity`, `#end-to-end`, `#LLM`

---

<a id="item-27"></a>
## [CanvasAgent: AI Agent Orchestrates Visual Tools for Image Creation](https://arxiv.org/abs/2607.05465) ⭐️ 8.0/10

Researchers introduced CanvasAgent, a tool-augmented multimodal agent that learns to orchestrate heterogeneous visual tools for complex image creation and editing, along with CanvasCraft, a large-scale dataset of 140K executable trajectories and 10K RL task specifications. CanvasAgent addresses a gap in multimodal agents by moving beyond perception-augmented reasoning to active manipulation-centered visual creation, enabling complex multi-step workflows that require generation, editing, segmentation, composition, and enhancement. CanvasAgent is first trained with supervised fine-tuning (SFT) on CanvasCraft trajectories, then optimized with GRPO using a hybrid reward combining outcome- and process-level signals. During rollout, it inspects intermediate results, tracks visual assets, and adapts tool decisions to the evolving visual state.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: Complex image creation often requires multiple tools (e.g., generation, segmentation, inpainting, compositing) working together. Existing multimodal agents are mostly optimized for perception tasks like visual question answering, not for orchestrating tools that actively transform images. CanvasAgent and CanvasCraft provide a supervised framework to learn such multi-tool workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05465v1">Enabling Complex Image Creation and Editing via Visual Tool ... - arXiv</a></li>
<li><a href="https://huggingface.co/papers/2607.05465">CanvasAgent: Enabling Complex Image Creation and Editing via ...</a></li>
<li><a href="https://huggingface.co/datasets/GML-FMGroup/CanvasCraftSFT/tree/main">GML-FMGroup/CanvasCraftSFT at main - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#multimodal AI`, `#image editing`, `#tool orchestration`, `#dataset`, `#agent`

---

<a id="item-28"></a>
## [Ground3D-LMM: Unified 3D Point Grounding and Metric Reasoning](https://arxiv.org/abs/2607.05493) ⭐️ 8.0/10

Researchers propose Ground3D-LMM, a unified large multimodal model that takes point clouds and optional RGB images as input, enabling 3D spatial conversation with point-grounded responses and metric numeric outputs at object and part granularity. This work bridges the gap between conversational 3D LMMs and explicit grounding, making responses verifiable and actionable with real-world measurements, which is crucial for applications like robotics, AR/VR, and autonomous navigation. The model is trained on a large-scale dataset built from ScanNet and ScanNet++ with roughly 2.5M question-answer pairs spanning eight tasks, and includes a manually verified test set for the new 3D Grounded Measurement task.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: 3D large multimodal models (LMMs) typically generate responses without explicit 3D grounding, while 3D grounding models focus on localization without interactive dialogue. Ground3D-LMM combines both capabilities, enabling metric-aware spatial reasoning with point-level grounding.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05493v1">Ground3D-LMM: Fine-Grained 3D Point Grounding and Spatial ...</a></li>

</ul>
</details>

**Tags**: `#3D Vision`, `#Large Multimodal Models`, `#Spatial Reasoning`, `#Point Cloud`, `#Grounding`

---

<a id="item-29"></a>
## [Natural Dataset Correlations Act as Backdoor Triggers](https://arxiv.org/abs/2607.05516) ⭐️ 8.0/10

A new paper discovers that naturally occurring statistical correlations in vision datasets like ImageNet can function as backdoor-like triggers, altering model predictions without any malicious poisoning. This reveals a previously overlooked adversarial surface inherent in standard datasets, suggesting that dataset auditing must consider spurious correlations not only as bias but also as latent attack vectors. The authors identify patterns strongly linked to labels in ImageNet, use statistical controls to remove random correlations, and show these signals transfer across different model architectures, making them more targeted than generic corruptions.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: Adversarial machine learning studies attacks on ML algorithms. Backdoor attacks typically involve maliciously inserting triggers during training. This work shows that even clean datasets can contain natural statistical signals that behave like backdoors, expanding the threat model.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05516v1">Statistical Adversaries: Natural Backdoor-like Features in Vision ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Adversarial_machine_learning">Adversarial machine learning - Wikipedia</a></li>
<li><a href="https://iseeyou.com/insights/the-hidden-dangers-of-statistical-adversaries-in-vision-datasets.php">The Hidden Dangers of Statistical Adversaries in Vision Datasets</a></li>

</ul>
</details>

**Tags**: `#adversarial attacks`, `#dataset auditing`, `#vision`, `#backdoor`, `#robustness`

---

<a id="item-30"></a>
## [Bayesian 3DGS with Uncertainty and Adaptive Complexity](https://arxiv.org/abs/2607.05522) ⭐️ 8.0/10

This paper introduces a rendering-aware Bayesian 3D Gaussian splatting framework that uses Normal-Inverse-Wishart posteriors to track Gaussian geometry and an optional Dirichlet-process extension for adaptive complexity control, providing native uncertainty estimates for active view selection. This work addresses key limitations of standard 3DGS—lack of uncertainty quantification and hand-tuned heuristics—enabling principled decision-making in sparse-view and active-vision scenarios, with potential impact on novel-view synthesis and robotics. In a fixed-budget 16-to-32 active-view task, the NIW-based acquisition improves PSNR by +0.453 dB and LPIPS by -0.0146 over a standard ensemble baseline, while NIW native intervals reduce 95% coverage error by about 17x compared to a shared proxy.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: 3D Gaussian splatting (3DGS) represents scenes as a collection of 3D Gaussians for real-time novel-view synthesis, but its standard training uses point estimates and heuristics without uncertainty. The Normal-Inverse-Wishart (NIW) distribution is a conjugate prior for multivariate normal distributions, enabling closed-form posterior updates. Dirichlet process Gaussian mixture models allow automatic determination of the number of components, providing adaptive complexity control.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Normal-inverse-Wishart_distribution">Normal-inverse-Wishart distribution</a></li>
<li><a href="https://andrewcharlesjones.github.io/journal/dpmm.html">Dirichlet process mixture models - Andy Jones</a></li>
<li><a href="https://arxiv.org/abs/2504.07370">[2504.07370] View-Dependent Uncertainty Estimation of 3D ...</a></li>

</ul>
</details>

**Tags**: `#3D Gaussian Splatting`, `#Bayesian Inference`, `#Novel-View Synthesis`, `#Uncertainty Quantification`, `#Active Vision`

---

<a id="item-31"></a>
## [MuCoDi: Multi-Teacher Distillation for Edge Pathology AI](https://arxiv.org/abs/2607.05533) ⭐️ 8.0/10

Researchers propose MuCoDi, a multi-teacher contrastive distillation framework that trains compact MobileOne and RepViT student models using frozen embeddings from three large pathology foundation models (Virchow2, UNI2, H-Optimus-1). The resulting MuCoEdge models achieve near-teacher performance (e.g., 71.0% external AUROC vs. 71.8% for Virchow2) while reducing model size by orders of magnitude, with the smallest variant having only 6.4M parameters. This work enables deployment of pathology foundation models on edge devices like Raspberry Pi, achieving up to 605× speedup over Virchow2 while retaining clinically useful accuracy. It addresses a critical bottleneck in computational pathology—the high computational cost of large models—paving the way for real-time, on-device analysis in resource-constrained clinical settings. MuCoDi adapts MoCo v3's contrastive distillation objective, using cached teacher embeddings as keys instead of a momentum encoder. Students are pretrained on 14.3M TCGA tiles from only 11.8K whole-slide images and evaluated on 23 clinical tasks. On a Raspberry Pi 5, sub-million-parameter MobileOne students achieve 66.5–66.9% external AUROC with a 605-fold speedup over Virchow2.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: Pathology foundation models (PFMs) like Virchow2, UNI2, and H-Optimus-1 are large neural networks trained on massive histology image datasets, achieving state-of-the-art performance on tasks like cancer classification. However, their size (often hundreds of millions of parameters) and high inference cost make them impractical for local deployment in hospitals. Knowledge distillation is a technique where a smaller student model is trained to mimic the outputs of a larger teacher model, reducing computational requirements while preserving performance. Contrastive distillation, as used in MuCoDi, leverages contrastive learning objectives to align student and teacher representations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05533v1">Multi-Teacher Contrastive Distillation for Edge-Efficient ...</a></li>
<li><a href="https://iseeyou.com/insights/bringing-advanced-pathology-analysis-to-the-edge-with-multi-teacher-contrastive-.php">Bringing Advanced Pathology Analysis to the Edge with Multi ...</a></li>
<li><a href="https://github.com/THU-MIG/RepViT">GitHub - THU-MIG/RepViT: RepViT: Revisiting Mobile CNN From ... RepViT: Revisiting Mobile CNN From ViT Perspective - arXiv.org REPVIT: REVISITING MOBILE CNN FROM VIT PERSPECTIVE RepViT: Revisiting Mobile CNN From ViT Perspective Rep ViT: Revisiting Mobile CNN From ViT Perspective | IEEE ... RepViT: Revisiting Mobile CNN From ViT Perspective</a></li>

</ul>
</details>

**Tags**: `#computational pathology`, `#knowledge distillation`, `#foundation models`, `#edge AI`, `#contrastive learning`

---

<a id="item-32"></a>
## [Training-Free 3D Shape Abstraction via Generative Models](https://arxiv.org/abs/2607.05568) ⭐️ 8.0/10

Researchers propose a training-free pipeline that uses pretrained generative image models and vision-language models to abstract 3D shapes into superquadric primitives from multi-view images, achieving state-of-the-art Chamfer distance on HumanPrim and Toys4K benchmarks. This work demonstrates that large-scale generative models can be directly harnessed for 3D primitive abstraction without fine-tuning, offering a category-agnostic and orientation-invariant solution that previous learning-based methods struggled with. It has potential impact on robotics, simulation, and scene understanding by enabling compact shape representations. The pipeline renders multi-view images, uses a vision-language model to analyze semantic parts, prompts a generative image model to produce color-coded segmentation masks, reprojects them onto the 3D geometry, and fits superquadric primitives via parameter optimization. The method contains no learned parameters and its accuracy is currently bottlenecked by part segmentation quality, not primitive fitting.

rss · arXiv - Computer Vision · Jul 8, 04:00

**Background**: Superquadrics are a family of parametric 3D shapes that extend ellipsoids with variable exponents, enabling compact representation of diverse object parts. Primitive shape abstraction aims to decompose 3D objects into a set of such geometric primitives, which is useful for robotics and scene understanding. Previous methods often require task-specific training and struggle with category generalization or orientation invariance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05568">Harnessing Generative Image Models for Training-Free ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Superquadrics">Superquadrics - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#3D shape abstraction`, `#generative models`, `#vision-language models`, `#robotics`, `#scene understanding`

---

<a id="item-33"></a>
## [Unified Theory for Deep Neural Networks Beyond ReLU](https://arxiv.org/abs/2607.05546) ⭐️ 8.0/10

A new paper develops a unified function space theory for deep fully connected neural networks that works with a broad range of activation functions, not just ReLU, and proves a novel representer theorem and complexity bounds. This work bridges several existing ideas and provides new insights into the relationship between depth and complexity, potentially reshaping how researchers understand the expressivity of deep networks under norm constraints. The theory defines functions recursively as ℓ1-bounded linear combinations of activated functions from preceding layers, and in the univariate ReLU case, it shows a 'depth saturation' result where depth only yields a small constant rescaling without added functional diversity.

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: Deep neural networks are typically analyzed using parameter counts or representational costs, but this paper adopts a function space perspective that controls complexity via norms. The representer theorem is a classical result in kernel methods that ensures optimal solutions can be expressed as finite combinations of kernel evaluations; extending it to deep networks is a significant theoretical advance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05546">[2607.05546] Deep Neural Variation Spaces: A Unifying ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Representer_theorem">Representer theorem - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#deep learning theory`, `#neural networks`, `#function spaces`, `#complexity bounds`, `#representer theorem`

---

<a id="item-34"></a>
## [Continual Learning: Rethinking Retention for Better Adaptation](https://arxiv.org/abs/2607.05609) ⭐️ 8.0/10

This paper challenges the dominant retention-centric view in continual learning, proposing to reframe it as an online optimization problem and introducing Transfer Efficiency as a new metric to balance instability and transient error. This work could shift the focus of continual learning research from merely preventing catastrophic forgetting to optimizing real-time adaptation, potentially leading to more practical algorithms for non-stationary environments. The paper derives a Critical Task Duration threshold beyond which historical knowledge becomes a liability, and validates this on image classification and reinforcement learning benchmarks. It also proposes Predictive Continual Learning, a new class of algorithms that optimize expected future performance.

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: Continual learning aims to enable models to learn from a stream of tasks without forgetting previous knowledge, a challenge known as catastrophic forgetting. Traditional approaches prioritize retaining all past information, often at the cost of slower adaptation to new tasks. This paper argues that in non-stationary environments, retention can be detrimental and proposes a new framework centered on online optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://www.meegle.com/en_us/topics/transfer-learning/transfer-learning-in-continual-learning">Transfer Learning In Continual Learning - meegle.com</a></li>
<li><a href="https://arxiv.org/pdf/2208.06931">A THEORY FOR KNOWLEDGE TRANSFER IN CONTINUAL LEARNING</a></li>

</ul>
</details>

**Tags**: `#continual learning`, `#catastrophic forgetting`, `#online optimization`, `#transfer efficiency`, `#machine learning`

---

<a id="item-35"></a>
## [Power-Calibrated Framework for LLM Watermarking](https://arxiv.org/abs/2607.05694) ⭐️ 8.0/10

This paper introduces a power-calibrated statistical framework for logit-based LLM watermarking that establishes explicit quantitative relationships between hyperparameters, detection power, and distortion, enabling optimal hyperparameter selection without heuristic tuning. This work addresses a critical practical limitation in LLM watermarking—heuristic tuning—by providing a principled, theoretically grounded method for selecting hyperparameters, which is essential for reliable AI-generated content detection and AI safety. The framework transforms watermark design into a guided optimization problem and derives practical parameter selection procedures that achieve Pareto-optimal tradeoffs between detectability and distortion, validated across multiple language models and datasets.

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: Logit-based watermarking embeds imperceptible identifiers into LLM-generated text by modifying the logits (output probabilities) during generation. However, existing methods rely on heuristic tuning of hyperparameters like watermark strength, leading to suboptimal tradeoffs between detectability and semantic distortion. This paper provides a statistical framework to optimize this tradeoff.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.05694v1">Beyond Heuristic Tuning: Power-Calibrated LLM Watermarking</a></li>
<li><a href="https://openreview.net/forum?id=pAeEzS4LwS">Catch-22: Pareto Frontier for Detectability and Robustness in ...</a></li>
<li><a href="https://k1015.github.io/Catch-22-Pareto-Frontier-Watermark-in-LLMs/">Catch-22: Detectability and Robustness in LLM Watermarking</a></li>

</ul>
</details>

**Tags**: `#LLM watermarking`, `#AI safety`, `#statistical framework`, `#hyperparameter optimization`, `#content detection`

---

<a id="item-36"></a>
## [Width-Robust Learnability in Mean-Field Bayesian Neural Networks](https://arxiv.org/abs/2607.05735) ⭐️ 8.0/10

This paper proves a width-robust learnability theorem for Bayesian neural networks at mean-field scaling, showing that a family of Boolean-cube targets is learnable from polynomially many samples at infinite width if and only if it is learnable at polynomial width, if and only if its reduced entropy is polynomially bounded. This result bridges the gap between infinite-width theory and finite-width practice, establishing that the inductive bias of mean-field Bayesian neural networks is width-robust, which is crucial for understanding generalization in deep learning. The proof uses a subsampling technique: from infinitely many hidden neurons in the mean-field solution, one can select polynomially many representatives while preserving the learned function on every input. This subsampling has both an active component (keeping data-dependent low-dimensional statistics) and a lazy component (resampling entropy-dominated directions from the prior).

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: Mean-field scaling is a regime where the network width goes to infinity while the learning rate is scaled appropriately, allowing feature learning beyond the neural tangent kernel. Reduced entropy measures the prior cost of representing a target function. This work connects infinite-width learnability to finite-width learnability via reduced entropy.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05735">[2607.05735] Width-Robust Learnability in Mean-Field Bayesian ...</a></li>
<li><a href="https://arxiv.org/abs/1903.04440">[1903.04440] Mean Field Analysis of Deep Neural Networks A Mean-Field Theory of Training Deep Neural Networks Mean-Field Limits of Neural Networks - emergentmind.com A MEAN-FIELD LIMIT FOR CERTAIN DEEP NEURAL NETWORKS A mean field view of the landscape of two-layer neural networks Mean Field Theory for Neural Networks. Beyond the NTK Regime Mean Field Analysis of Neural Networks: A Law of Large ...</a></li>

</ul>
</details>

**Tags**: `#Bayesian neural networks`, `#mean-field theory`, `#learnability`, `#neural network theory`, `#generalization`

---

<a id="item-37"></a>
## [Boosting with List-Decodable Codes](https://arxiv.org/abs/2607.05791) ⭐️ 8.0/10

A new boosting algorithm achieves optimal round complexity for concept classes closed under XOR by exploiting a connection to list-decodable codes. This result circumvents a known lower bound in boosting, potentially enabling more efficient learning algorithms for certain concept classes. The algorithm uses O(log(1/ε)) calls to a weak learner and a single batch of additional samples, improving over the generic O(log(1/ε)/γ^2) lower bound.

rss · arXiv - Data Science & Statistics · Jul 8, 04:00

**Background**: Boosting is a technique that combines multiple weak learners to form a strong learner. List-decodable codes are error-correcting codes that output a list of possible messages from a corrupted codeword. The paper connects these two concepts by treating the target function as a message and weak hypotheses as corrupted codewords.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/List_decoding">List decoding - Wikipedia</a></li>
<li><a href="https://people.seas.harvard.edu/~salil/pseudorandomness/codes.pdf">List-Decodable Codes</a></li>
<li><a href="https://people.eecs.berkeley.edu/~venkatg/teaching/ECC-fall22/scribes/lecture16.pdf">1 List Decoding - University of California, Berkeley</a></li>

</ul>
</details>

**Tags**: `#boosting`, `#learning theory`, `#list-decodable codes`, `#theoretical computer science`

---

<a id="item-38"></a>
## [EmTech AI 2026 Highlights Rise of AI Platforms](https://www.technologyreview.com/2026/07/08/1140223/emtech-ai-2026-the-rise-of-the-ai-platform/) ⭐️ 8.0/10

At EmTech AI 2026, MIT Technology Review reported that AI platforms are emerging as the dominant trend, enabling organizations to efficiently build, deploy, and manage AI applications through integrated environments. This shift signifies a maturation of the AI industry, moving from custom-built solutions to standardized platforms that lower barriers to entry and accelerate AI adoption across enterprises. The conference featured an exclusive overview of 10 key AI technologies and trends for 2026, emphasizing the role of AI platforms in supporting the full AI lifecycle from data ingestion to deployment monitoring.

rss · MIT Technology Review · Jul 8, 16:26

**Background**: An AI platform is an integrated technology environment that provides tools for developing, training, and running machine learning models, often including MLOps, automation, and data analytics capabilities. Major cloud providers like Microsoft Azure, Red Hat, and IBM offer such platforms to streamline AI workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://event.technologyreview.com/emtech-ai-2026">EmTech AI 2026 in Cambridge, MA</a></li>
<li><a href="https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-an-ai-platform">What is an AI platform? | Microsoft Azure</a></li>
<li><a href="https://www.redhat.com/en/topics/ai/what-is-an-ai-platform">What is an AI platform? - Red Hat</a></li>

</ul>
</details>

**Tags**: `#AI`, `#platforms`, `#industry trends`, `#MIT Technology Review`

---

<a id="item-39"></a>
## [New weight loss pill beats oral Ozempic in major trial](https://www.sciencedaily.com/releases/2026/07/260707054111.htm) ⭐️ 8.0/10

A once-daily pill called orforglipron, developed by Eli Lilly, outperformed oral semaglutide in weight loss and blood sugar control in a major clinical trial. Orforglipron offers a cheaper, more convenient alternative to injectable GLP-1 drugs like Ozempic and Wegovy, potentially expanding global access to obesity treatment. Orforglipron is a small-molecule, non-peptide GLP-1 receptor agonist that does not require refrigeration or special timing with meals, unlike oral semaglutide.

rss · ScienceDaily Health · Jul 8, 05:16

**Background**: GLP-1 receptor agonists are a class of drugs that mimic a hormone to regulate appetite and blood sugar. Injectable versions like semaglutide (Ozempic, Wegovy) have been highly effective but require refrigeration and injections. Oral semaglutide exists but has bioavailability limitations. Orforglipron, approved in the US in April 2026, is a next-generation oral option.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Orforglipron">Orforglipron</a></li>
<li><a href="https://www.nejm.org/doi/full/10.1056/NEJMoa2511774">Orforglipron, an Oral Small-Molecule GLP-1 Receptor Agonist ...</a></li>
<li><a href="https://www.mayoclinic.org/drugs-supplements/semaglutide-oral-route/description/drg-20492085">Semaglutide (oral route) - Side effects & dosage</a></li>

</ul>
</details>

**Tags**: `#weight loss`, `#clinical trial`, `#pharmaceuticals`, `#obesity treatment`

---