---
layout: default
title: "Horizon Summary: 2026-05-19 (EN)"
date: 2026-05-19
lang: en
---

> From 93 items, 37 important content pieces were selected

---

1. [llama.cpp: High-Performance LLM Inference on Local Hardware](#item-1) ⭐️ 9.0/10
2. [NVIDIA Releases Sana: Efficient Linear Diffusion Transformer](#item-2) ⭐️ 9.0/10
3. [Simon Willison's 5-Minute LLM Recap at PyCon US 2026](#item-3) ⭐️ 8.0/10
4. [Benedict Evans: AI Eats the World Spring 2026](#item-4) ⭐️ 8.0/10
5. [Supertonic: Fast On-Device Multilingual TTS via ONNX](#item-5) ⭐️ 8.0/10
6. [RuView Turns WiFi Signals into Privacy-Preserving Sensors](#item-6) ⭐️ 8.0/10
7. [CloakBrowser: Stealth Chromium Evades Bot Detection](#item-7) ⭐️ 8.0/10
8. [ShadowBroker: Open-Source Geospatial Intelligence Platform](#item-8) ⭐️ 8.0/10
9. [Articraft: LLM-Powered Scalable Articulated 3D Asset Generation](#item-9) ⭐️ 8.0/10
10. [AgentWall: Runtime Safety Layer for Local AI Agents](#item-10) ⭐️ 8.0/10
11. [ANNEAL: LLM Agents Repair Process Knowledge via Symbolic Patches](#item-11) ⭐️ 8.0/10
12. [AI Agent Lets Scientists Automate Labs via Natural Language](#item-12) ⭐️ 8.0/10
13. [Skim: Speculative Execution for Efficient Web Agents](#item-13) ⭐️ 8.0/10
14. [LLM Negotiators Fail at Strategic Bargaining](#item-14) ⭐️ 8.0/10
15. [TTE-Flash: Latent Think Tokens Boost Multimodal Embeddings](#item-15) ⭐️ 8.0/10
16. [LinAlg-Bench Reveals LLM Math Failure Threshold at 4x4 Matrices](#item-16) ⭐️ 8.0/10
17. [Real-Time Diffusion Model on Apple M3 Ultra at 22.7 FPS](#item-17) ⭐️ 8.0/10
18. [IBPO: Counterfactual Credit Assignment for LLM Reasoning](#item-18) ⭐️ 8.0/10
19. [SignMuon: 1-bit Distributed Optimizer Cuts Communication by 32x](#item-19) ⭐️ 8.0/10
20. [Adversarial Action Removal in Self-Play RL](#item-20) ⭐️ 8.0/10
21. [Decision Capacity Threshold Causes Collapse in Self-Play RL](#item-21) ⭐️ 8.0/10
22. [AdaGraph: Graph-Native Clustering Defeats Curse of Dimensionality](#item-22) ⭐️ 8.0/10
23. [Language Game Enables Dialogue with Non-Neural Systems](#item-23) ⭐️ 8.0/10
24. [Scaling Laws for Skills in LLM Agent Systems](#item-24) ⭐️ 8.0/10
25. [CHI-Bench: Benchmarking AI Agents on Complex Healthcare Workflows](#item-25) ⭐️ 8.0/10
26. [LAD-Inspired Pre-Pretraining Boosts LLM Data Efficiency](#item-26) ⭐️ 8.0/10
27. [Retrieval-Based Legal Annotation Outperforms Generative LLMs](#item-27) ⭐️ 8.0/10
28. [Noise2Params: Unifying Event Camera Model via Photon Statistics](#item-28) ⭐️ 8.0/10
29. [GeoSym127K: Scalable Neuro-Symbolic Engine for Geometric Reasoning](#item-29) ⭐️ 8.0/10
30. [StreamPro: Proactive Decision-Making in Streaming Video](#item-30) ⭐️ 8.0/10
31. [TaTok: Adaptive Image Tokenization with Global Tokens](#item-31) ⭐️ 8.0/10
32. [StAD: Fast Likelihood Estimation for Diffusion Models via Stein Operator](#item-32) ⭐️ 8.0/10
33. [Prediction-Intervention Games and Invariant Sets](#item-33) ⭐️ 8.0/10
34. [Fourier Analysis Reveals Simplicity Bias in Neural Networks](#item-34) ⭐️ 8.0/10
35. [Stochastic Operator Networks for Uncertainty in SPDEs](#item-35) ⭐️ 8.0/10
36. [Noisy Inductive Matrix Completion Achieves Sample Efficiency](#item-36) ⭐️ 8.0/10
37. [Anduril and Meta's AR Glasses for Drone Warfare](#item-37) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp: High-Performance LLM Inference on Local Hardware](https://github.com/ggml-org/llama.cpp) ⭐️ 9.0/10

llama.cpp is a C/C++ library that enables efficient inference of large language models on consumer hardware, including CPUs and GPUs. It has gained massive community adoption and continues to add features like multimodal support and Hugging Face cache integration. This project democratizes access to LLMs by allowing users to run them locally without expensive cloud infrastructure, enhancing privacy and enabling offline use. Its high performance and broad hardware support make it a key tool for the open-source AI ecosystem. llama.cpp uses the GGML tensor library and supports integer quantization for reduced memory usage. Recent updates include multimodal support in llama-server, a VS Code extension for FIM completions, and native GGUF support on Hugging Face Inference Endpoints.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: Large language models (LLMs) typically require powerful GPUs and significant memory, making local deployment challenging. llama.cpp leverages the GGML tensor library, which is optimized for commodity hardware and supports various quantization techniques to reduce model size and memory footprint. This allows models like LLaMA to run on devices ranging from laptops to Raspberry Pis.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml-org/ggml: Tensor library for machine learning</a></li>
<li><a href="https://ggml.ai/">ggml.ai</a></li>

</ul>
</details>

**Discussion**: The community has shown strong enthusiasm, with discussions focusing on packaging improvements for downstream consumers and guides for using the new WebUI. There is also positive feedback on the collaboration with NVIDIA for gpt-oss model support.

**Tags**: `#LLM`, `#inference`, `#C++`, `#machine learning`, `#open source`

---

<a id="item-2"></a>
## [NVIDIA Releases Sana: Efficient Linear Diffusion Transformer](https://github.com/NVlabs/Sana) ⭐️ 9.0/10

NVIDIA has released Sana, an efficiency-oriented codebase for high-resolution image and video generation, featuring a linear diffusion transformer architecture that reduces quadratic complexity to near-linear. The release includes multiple model variants such as SANA, SANA-1.5, SANA-Sprint, SANA-Video, SANA-WM, and Sol-RL, with support for up to 4096×4096 resolution and deployment on laptop GPUs. Sana significantly lowers the computational barrier for high-resolution image synthesis, making it feasible to run on consumer-grade hardware like a single RTX 3090. Its linear attention mechanism and deep compression autoencoder set a new efficiency standard in generative AI, potentially accelerating adoption in creative tools, gaming, and embodied AI applications. Sana uses a deep compression autoencoder that compresses images 8× more than traditional autoencoders, and its linear attention reduces complexity from O(N^2) to near O(N). The codebase includes complete training and inference pipelines, with demos available for 4-bit quantization, ControlNet, and SANA-Sprint on a single RTX 3090.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: Diffusion models are a class of generative models that iteratively denoise random noise to produce high-quality images. Traditional diffusion transformers (DiTs) use quadratic-complexity attention, which becomes computationally expensive at high resolutions. Linear attention approximates standard attention with near-linear complexity, enabling efficient scaling to larger images. Sana builds on this concept with additional optimizations like deep compression autoencoders and efficient training recipes.

<details><summary>References</summary>
<ul>
<li><a href="https://nvlabs.github.io/Sana/">Efficient High-Resolution Image Synthesis</a></li>
<li><a href="https://arxiv.org/abs/2410.10629">[2410.10629] SANA: Efficient High-Resolution Image Synthesis with ...</a></li>

</ul>
</details>

**Discussion**: The community has shown strong interest, with the repository gaining significant stars and forks. Discussions on Discord and GitHub highlight enthusiasm for the linear attention approach and the ability to run on consumer GPUs, though some users have raised questions about compatibility with existing workflows and the learning curve for custom training.

**Tags**: `#diffusion models`, `#image synthesis`, `#NVIDIA`, `#transformer`, `#generative AI`

---

<a id="item-3"></a>
## [Simon Willison's 5-Minute LLM Recap at PyCon US 2026](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) ⭐️ 8.0/10

Simon Willison presented a lightning talk at PyCon US 2026 summarizing the last six months of LLM developments, using his annotated presentation tool to highlight the November 2025 inflection point where the 'best' model changed hands five times among Anthropic, OpenAI, and Google. This talk provides a concise, high-value overview of rapid LLM advancements, helping developers and researchers quickly grasp key trends and model shifts, especially the intense competition in coding capabilities. Willison used his 'pelican riding a bicycle' SVG test to illustrate model differences, noting that models like Claude Sonnet 4.5, GPT-5.1, Gemini 3, GPT-5.1 Codex Max, and Claude Opus successively claimed the top spot starting in November 2025.

rss · Simon Willison · May 19, 01:09 · [Discussion](https://news.ycombinator.com/item?id=48188183)

**Background**: Simon Willison is a well-known Python developer and creator of the Datasette project. His annotated presentation tool allows speakers to add detailed notes and alt text to slide images, making talks more accessible and shareable. The 'pelican riding a bicycle' test is a whimsical benchmark he uses to evaluate LLM image generation capabilities on a task unlikely to be in training data.

<details><summary>References</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/19/5-minute-llms/">The last six months in LLMs in five minutes</a></li>
<li><a href="https://tools.simonwillison.net/annotated-presentations">Annotated Presentation Creator - tools.simonwillison.net</a></li>
<li><a href="https://us.pycon.org/2026/schedule/presentation/175/">Lightning Talks - PyCon US 2026</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters discussed the practical limitations of LLMs for non-programmers and in complex coding tasks, with some noting that while models have improved, they still struggle with full application development. Others highlighted a security inflection point in Spring 2026.

**Tags**: `#LLMs`, `#AI`, `#PyCon`, `#lightning talk`, `#Simon Willison`

---

<a id="item-4"></a>
## [Benedict Evans: AI Eats the World Spring 2026](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf) ⭐️ 8.0/10

Benedict Evans released his Spring 2026 presentation 'AI eats the world', a 79-slide deck analyzing the AI industry's evolution from scaling debates to product deployment. The deck provides a high-value temporal view of AI platform shifts, highlighting model commoditization and the movement of value up the stack to applications, workflows, and proprietary data. Evans' provisional thesis states that models look likely to become infrastructure, while value moves up-stack into apps, workflows, product, proprietary data/context, GTM, and new questions enabled by cheap automation.

hackernews · topherjaynes · May 18, 12:49 · [Discussion](https://news.ycombinator.com/item?id=48179021)

**Background**: Benedict Evans is a well-known tech analyst who publishes semi-annual presentations on macro and strategic tech trends. His Spring 2026 deck is the latest in a series tracking AI's impact, following earlier versions from November 2024 and May 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ben-evans.com/presentations">Presentations — Benedict Evans</a></li>
<li><a href="https://news.ycombinator.com/item?id=48179021">AI eats the world (Spring 26) [pdf] | Hacker News</a></li>
<li><a href="https://www.techtwitter.com/articles/ai-is-eating-the-world-79-slide-deck-from-benedict-evans">"AI Is Eating The World" 79 slide deck from Benedict Evans</a></li>

</ul>
</details>

**Discussion**: Commenters on Hacker News appreciated the temporal view and debated model commoditization, with some comparing AI labs to mobile telecoms or cloud providers. One commenter noted that mega models may hide inefficiency, likening the current approach to the mainframe era.

**Tags**: `#AI`, `#industry analysis`, `#platform shifts`, `#Benedict Evans`, `#technology trends`

---

<a id="item-5"></a>
## [Supertonic: Fast On-Device Multilingual TTS via ONNX](https://github.com/supertone-inc/supertonic) ⭐️ 8.0/10

Supertone Inc. released Supertonic, an open-source multilingual text-to-speech system that runs entirely on-device via ONNX Runtime, supporting 31 languages with a compact 99M-parameter model. Supertonic enables high-quality, low-latency TTS on edge devices without cloud dependency, preserving privacy and reducing costs, which is significant for accessibility, IoT, and mobile applications. The model outputs 44.1kHz 16-bit WAV audio, supports expression tags like <laugh> and <breath>, and provides SDKs for Python, Node.js, WebGPU, Java, C++, C#, Go, Swift, iOS, Rust, and Flutter.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: ONNX Runtime is a cross-platform machine learning inference accelerator that supports models from PyTorch, TensorFlow, and other frameworks. WebGPU enables GPU-accelerated inference directly in browsers. Supertonic leverages these technologies to run TTS locally on diverse hardware, including Raspberry Pi and e-readers.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform, high performance ML inferencing and training accelerator · GitHub</a></li>
<li><a href="https://onnxruntime.ai/docs/">ONNX Runtime | onnxruntime</a></li>
<li><a href="https://onnxruntime.ai/">ONNX Runtime | Home</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#ONNX`, `#multilingual`, `#on-device`, `#open-source`

---

<a id="item-6"></a>
## [RuView Turns WiFi Signals into Privacy-Preserving Sensors](https://github.com/ruvnet/RuView) ⭐️ 8.0/10

RuView is a new open-source platform that uses commodity WiFi signals to detect presence, track movement, and monitor vital signs like breathing and heart rate, all without cameras or wearables. This technology enables privacy-preserving sensing for smart homes, healthcare, and security, potentially replacing cameras in sensitive areas while using existing WiFi infrastructure. RuView runs on low-cost ESP32 nodes (as low as $9 each) and uses Channel State Information (CSI) from WiFi signals, with pose estimation achieving PCK@20 around 2.5% without cameras, targeting 35%+ with camera supervision.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: WiFi sensing works by analyzing how radio waves are disturbed by human movement and breathing, using Channel State Information (CSI) from standard WiFi hardware. Previous research like DensePose from WiFi at Carnegie Mellon University demonstrated pose estimation from WiFi signals, but RuView brings this to practical edge devices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NTUMARS/Awesome-WiFi-CSI-Sensing">GitHub - NTUMARS/Awesome-WiFi-CSI-Sensing: A list of awesome papers and cool resources on WiFi CSI sensing. · GitHub</a></li>
<li><a href="https://info.support.huawei.com/info-finder/encyclopedia/en/CSI+Sensing.html">What Is CSI Sensing? - Huawei</a></li>
<li><a href="https://github.com/espressif/esp-csi">GitHub - espressif/esp-csi: Applications based on Wi-Fi CSI (Channel state information), such as indoor positioning, human detection · GitHub</a></li>

</ul>
</details>

**Tags**: `#WiFi sensing`, `#spatial intelligence`, `#vital sign monitoring`, `#privacy-preserving`, `#IoT`

---

<a id="item-7"></a>
## [CloakBrowser: Stealth Chromium Evades Bot Detection](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser is an open-source stealth Chromium browser that applies 49 source-level C++ patches to modify browser fingerprints, passing all 30 bot detection tests and achieving a 0.9 reCAPTCHA v3 score. This project addresses a critical pain point in web automation and scraping by providing a drop-in replacement for Playwright that bypasses advanced anti-bot systems like Cloudflare Turnstile and DataDome, potentially saving developers significant time and resources. CloakBrowser is available via pip and npm, auto-downloads the modified Chromium binary, and includes a humanize=True flag that simulates human-like mouse movements and typing patterns to further evade behavioral detection.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: Browser fingerprinting is a technique used by websites to identify and track users based on unique browser and device characteristics, such as canvas rendering, WebGL, and audio signals. Automated browsers like Playwright are often detected by anti-bot services because they expose automation signals, leading to blocks or CAPTCHAs. CloakBrowser patches these signals at the C++ source level, making it indistinguishable from a normal browser.

<details><summary>References</summary>
<ul>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques : 6 Top Methods Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>
<li><a href="https://www.techtimes.com/articles/316664/20260515/cloakhqs-open-source-chromium-fork-defeats-cloudflare-datadome-perimeterx-without-configuration.htm">CloakHQ's Open-Source Chromium Fork Defeats Cloudflare, DataDome, and ...</a></li>

</ul>
</details>

**Tags**: `#web automation`, `#browser fingerprinting`, `#anti-bot`, `#Playwright`, `#stealth browser`

---

<a id="item-8"></a>
## [ShadowBroker: Open-Source Geospatial Intelligence Platform](https://github.com/BigBodyCobain/Shadowbroker) ⭐️ 8.0/10

ShadowBroker is a new open-source geospatial intelligence platform that aggregates real-time data from over 60 public sources, including corporate jets, spy satellites, and seismic events, into a unified map interface with AI integration for correlation analysis. This platform democratizes access to global telemetry data that was previously scattered across multiple tools, enabling analysts, researchers, and the public to monitor and correlate events in real time. Its open-source nature allows full auditability and self-hosting, addressing privacy concerns. Built with Next.js, MapLibre GL, FastAPI, and Python, it features 35+ toggleable data layers, including SAR ground-change detection, and multiple visual modes (DEFAULT, SATELLITE, FLIR, NVG, CRT). It includes an optional Shodan connector for operator-supplied API access.

rss · GitHub Trending - Daily (All) · May 19, 06:31

**Background**: Open-source intelligence (OSINT) involves collecting and analyzing publicly available data for intelligence purposes. Many global telemetry sources, such as aircraft ADS-B, maritime AIS, and satellite orbital data, are already public but scattered across different platforms. ShadowBroker aggregates these into a single interface, making it easier to spot correlations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/BigBodyCobain/Shadowbroker">GitHub - BigBodyCobain/ Shadowbroker : Open-source intelligence for...</a></li>
<li><a href="https://www.explainx.ai/tools/shadowbroker">Shadowbroker — AI tool | explainx.ai | explainx.ai</a></li>
<li><a href="https://beta.pinokio.co/apps/github-com-dsrpt-shadowbroker-pinokio">Shadowbroker on Pinokio</a></li>

</ul>
</details>

**Tags**: `#OSINT`, `#geospatial intelligence`, `#open-source`, `#AI`, `#real-time data`

---

<a id="item-9"></a>
## [Articraft: LLM-Powered Scalable Articulated 3D Asset Generation](https://github.com/mattzh72/articraft) ⭐️ 8.0/10

Articraft is an open-source agentic system that uses LLMs to programmatically generate articulated 3D assets from text descriptions, bypassing traditional manual modeling tools. This approach enables scalable, automated creation of simulation-ready articulated objects, which could significantly accelerate 3D content pipelines for robotics, gaming, and VR/AR applications. The system generates assets by having an LLM write Python code against a custom SDK, producing objects with semantic parts, robust geometry, and physical joints. It supports multiple LLM providers and includes a local viewer for inspection.

rss · GitHub Trending - Python · May 19, 06:31

**Background**: Articulated 3D assets—objects with moving parts like hinges or joints—are traditionally created manually in tools like Blender, which is time-consuming and hard to scale. Articraft reframes the problem as code generation, leveraging LLMs' ability to write programs that build such assets programmatically.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/mattzh72/articraft">mattzh72/articraft: An Agentic System for Scalable Articulated ...</a></li>
<li><a href="https://articraft3d.github.io/">Articraft: An Agentic System for Scalable Articulated 3 D Asset ...</a></li>
<li><a href="https://www.alphaxiv.org/audio/2605.15187">Articraft: An Agentic System for Scalable Articulated 3 D Asset ...</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#LLM`, `#computer graphics`, `#AI`, `#open source`

---

<a id="item-10"></a>
## [AgentWall: Runtime Safety Layer for Local AI Agents](https://arxiv.org/abs/2605.16265) ⭐️ 8.0/10

AgentWall is a new runtime safety layer that intercepts every proposed AI agent action before execution, evaluates it against a declarative policy, and requires human approval for sensitive operations. This addresses a critical gap in AI agent safety by enforcing policies at the execution boundary, preventing unsafe actions like file deletion or credential exfiltration in local environments. AgentWall achieves 92.9% policy enforcement accuracy with sub-millisecond overhead across 14 benchmark tests, and is implemented as a policy-enforcing MCP proxy and OpenClaw plugin.

rss · arXiv - AI · May 19, 04:00

**Background**: AI agents are evolving from passive text generators to active actors that can execute commands, modify files, and call APIs. Existing safety measures like model alignment and input filtering do not control actions at runtime, leaving local environments vulnerable.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.16265v1">AgentWall: A Runtime Safety Layer for Local AI Agents</a></li>
<li><a href="https://agentwall.dev/">AgentWall - Stop your AI agent before it goes too far</a></li>
<li><a href="https://github.com/reesepj/agentwall">GitHub - reesepj/agentwall: Runtime defense for agentic AI. Control ...</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#autonomous agents`, `#runtime security`, `#local AI`

---

<a id="item-11"></a>
## [ANNEAL: LLM Agents Repair Process Knowledge via Symbolic Patches](https://arxiv.org/abs/2605.16309) ⭐️ 8.0/10

ANNEAL introduces a neuro-symbolic approach that enables LLM agents to autonomously repair recurring execution errors by generating governed symbolic patches to a process knowledge graph, without modifying model weights. This addresses a critical limitation in self-evolving agents—persistent fault elimination with safety guarantees—and could enable more reliable deployment of LLM agents in complex, real-world tasks. The core mechanism, Failure-Driven Knowledge Acquisition (FDKA), localizes the responsible operator, synthesizes a typed patch via constrained LLM generation, and validates it through multi-dimensional scoring, symbolic guardrails, and canary testing before commit.

rss · arXiv - AI · May 19, 04:00

**Background**: LLM agents often fail repeatedly on the same fault because the underlying process knowledge—operator schemas, preconditions, and constraints—remains unrepaired. Existing self-evolving methods update prompts, memory, or weights but do not directly repair the symbolic structures encoding task execution. ANNEAL fills this gap by combining neural generation with symbolic governance.

**Tags**: `#LLM Agents`, `#Neuro-Symbolic AI`, `#Self-Evolving Systems`, `#Knowledge Graphs`, `#AI Safety`

---

<a id="item-12"></a>
## [AI Agent Lets Scientists Automate Labs via Natural Language](https://arxiv.org/abs/2605.16552) ⭐️ 8.0/10

Researchers present an AI agent architecture that integrates large language models with the Experiment Orchestration System (EOS), enabling scientists to create and monitor automated lab protocols using natural language. The agent achieves a 97% first-attempt protocol generation success rate and reduces required interface actions by an order of magnitude. This breakthrough lowers the barrier to laboratory automation, allowing scientists without programming expertise to design and run complex experiments. It accelerates scientific discovery in materials science, drug development, and biology by making autonomous labs more accessible and efficient. The AI agent operates under an agentic loop with automated validation and error correction, supporting the full experimental lifecycle from protocol creation to result analysis. A visual graph editor renders protocols as interactive node-based diagrams, enabling seamless switching between AI-assisted and manual construction.

rss · arXiv - AI · May 19, 04:00

**Background**: Laboratory automation traditionally requires scientists to write code and manage complex software to coordinate instruments and robots. The Experiment Orchestration System (EOS) is a software framework that serves as the foundation for self-driving labs, handling task scheduling, device control, and optimization campaigns. This work integrates LLMs into EOS to allow natural language interaction.

<details><summary>References</summary>
<ul>
<li><a href="https://unc-robotics.github.io/eos/index.html">The Experiment Orchestration System ( EOS ) — EOS</a></li>
<li><a href="https://ieeexplore.ieee.org/document/11128578/">The Experiment Orchestration System ( EOS )... | IEEE Xplore</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#laboratory automation`, `#large language models`, `#scientific discovery`, `#orchestration`

---

<a id="item-13"></a>
## [Skim: Speculative Execution for Efficient Web Agents](https://arxiv.org/abs/2605.16565) ⭐️ 8.0/10

Skim introduces a speculative execution framework that uses offline profiling and lightweight verification to bypass expensive LLM inference for routine web agent tasks, reducing median per-task cost by 1.9x and latency by 33.4% with no accuracy loss. This work addresses the high cost and latency of current web agents, which rely on frontier-model inference and ReAct-style planning for every step. By exploiting predictable website structures, Skim makes web agents more practical for real-world deployment, potentially enabling broader adoption of AI-driven automation. Skim's offline profiler captures stable URL patterns, answer formats, and task-to-trajectory mappings per site. At runtime, it matches queries to templates, synthesizes URLs, and extracts answers using a small model, with a lightweight verifier gating fast-path outputs; rare misspeculations fall back to the full agent, warm-started by the fast path's final URL.

rss · arXiv - AI · May 19, 04:00

**Background**: Web agents are AI systems that autonomously perform tasks on websites, often using large language models (LLMs) for planning and reasoning. ReAct-style planning interleaves reasoning traces with actions, but this is computationally expensive. Speculative execution is a technique from computer architecture where predictions are made to speed up processing, and here it is applied to web agents to skip unnecessary LLM calls for routine queries.

**Tags**: `#web agents`, `#speculative execution`, `#LLM efficiency`, `#systems`

---

<a id="item-14"></a>
## [LLM Negotiators Fail at Strategic Bargaining](https://arxiv.org/abs/2605.16575) ⭐️ 8.0/10

A new study on arXiv reveals that large language model agents can model counterparty preferences but fail to translate that knowledge into strategic bargaining, often making concessions that undermine their own interests. This finding highlights a critical limitation of LLMs in multi-agent strategic reasoning, with implications for AI alignment and real-world negotiation applications where strategic trade-offs are essential. The study uses a controlled multi-attribute bargaining environment and finds that even when agents accurately model counterparty preferences, they do not consistently pair concessions with gains on their own high-value attributes, leading to final agreements heavily dictated by opening anchors.

rss · arXiv - AI · May 19, 04:00

**Background**: Negotiation involves inferring what the other side wants and using that information to make advantageous offers over multiple turns. Strategic reasoning enables agents to cooperate, communicate, and compete effectively. This study tests whether LLM agents can perform such reasoning in a bargaining setting.

<details><summary>References</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/Strategic-Reasoning-with-Language-Models-Gandhi-Sadigh/f1a3cd5cc340f47e3e966709f7dfddef23460aa2">[PDF] Strategic Reasoning with Language Models | Semantic Scholar</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#negotiation`, `#AI alignment`, `#multi-agent systems`, `#strategic reasoning`

---

<a id="item-15"></a>
## [TTE-Flash: Latent Think Tokens Boost Multimodal Embeddings](https://arxiv.org/abs/2605.16638) ⭐️ 8.0/10

TTE-Flash replaces costly explicit Chain-of-Thought reasoning with latent think tokens for multimodal embeddings, achieving comparable performance at constant inference cost. The TTE-Flash-2B model outperforms its explicit-CoT counterpart on the MMEB-v2 benchmark. This work addresses a critical efficiency bottleneck in reasoning-based multimodal representations, enabling high-quality embeddings without prohibitive computational overhead. It could accelerate applications like retrieval, classification, and video understanding. The method optimizes think tokens using CoT generation loss and embedding tokens via contrastive loss, with two architectural designs for token extraction and training. Zero-shot evaluation across 15 video datasets shows scaling behavior with more think tokens and suggests adaptive budget allocation.

rss · arXiv - AI · May 19, 04:00

**Background**: Universal Multimodal Embedding (UME) benefits from Chain-of-Thought (CoT) reasoning, but generating explicit CoT traces is computationally expensive. Latent think tokens are internal representations that guide reasoning without producing explicit text, offering a more efficient alternative.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/thinking-tokens">Thinking Tokens</a></li>
<li><a href="https://arxiv.org/html/2505.16782v1">Reasoning Beyond Language: A Comprehensive Survey on Latent ...</a></li>
<li><a href="https://www.luiscardoso.dev/blog/neuralese">Thinking Without Words | Luis Cardoso</a></li>

</ul>
</details>

**Tags**: `#multimodal embeddings`, `#chain-of-thought`, `#latent reasoning`, `#efficiency`, `#representation learning`

---

<a id="item-16"></a>
## [LinAlg-Bench Reveals LLM Math Failure Threshold at 4x4 Matrices](https://arxiv.org/abs/2605.16675) ⭐️ 8.0/10

Researchers introduced LinAlg-Bench, a diagnostic benchmark that evaluates 10 frontier LLMs on linear algebra tasks across 3x3, 4x4, and 5x5 matrices, revealing a sharp behavioral threshold at 4x4 scale where models transition from execution errors to computational abandonment. This benchmark provides a structured failure analysis pipeline that identifies specific error types, suggesting that LLM mathematical reasoning failures are due to working memory limits rather than knowledge gaps, which could guide improvements in model architecture and training. The benchmark includes 660 SymPy-certified problems across 9 task types, with a three-stage forensic pipeline that classified 1,156 failures into ten primary error tags, including tool roleplay and constraint-consistent confabulation as novel failure modes.

rss · arXiv - AI · May 19, 04:00

**Background**: Large language models (LLMs) often struggle with complex mathematical reasoning, but previous benchmarks focused on overall accuracy without analyzing failure patterns. SymPy is an open-source Python library for symbolic mathematics used to certify correct answers. The forensic pipeline automates error classification, revealing structural constraints in LLM reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SymPy">SymPy</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmark`, `#mathematical reasoning`, `#linear algebra`, `#failure analysis`

---

<a id="item-17"></a>
## [Real-Time Diffusion Model on Apple M3 Ultra at 22.7 FPS](https://arxiv.org/abs/2605.16259) ⭐️ 8.0/10

Researchers achieved real-time camera-to-image transformation at 22.7 FPS on Apple M3 Ultra by combining CoreML conversion of the SDXS-512 distillation-specialized model with a 3-thread camera pipeline. This work demonstrates that optimization strategies for CUDA GPUs do not directly transfer to Apple Silicon's unified memory architecture, providing practical guidelines for deploying diffusion models on non-NVIDIA platforms. The study explored 10 optimization phases including CoreML conversion, quantization, Token Merging, Neural Engine utilization, and knowledge distillation, finding that quantization and parallel inference were ineffective on Apple Silicon.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Diffusion models are a class of generative AI models that produce high-quality images by iteratively denoising random noise. Real-time inference on consumer hardware typically relies on NVIDIA GPUs and CUDA optimizations, but Apple Silicon uses a unified memory architecture that behaves differently. Token Merging (ToMe) speeds up transformers by merging redundant tokens, and SDXS-512 is a distilled model designed for fast inference.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/docs/diffusers/v0.19.0/optimization/tome">Token Merging</a></li>
<li><a href="https://arxiv.org/abs/2303.17604">[2303.17604] Token Merging for Fast Stable Diffusion</a></li>
<li><a href="https://huggingface.co/IDKiro/sdxs-512-dreamshaper">IDKiro/ sdxs - 512 -dreamshaper · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#Apple Silicon`, `#real-time inference`, `#model optimization`, `#img2img`

---

<a id="item-18"></a>
## [IBPO: Counterfactual Credit Assignment for LLM Reasoning](https://arxiv.org/abs/2605.16302) ⭐️ 8.0/10

Researchers propose Implicit Behavior Policy Optimization (IBPO), a counterfactual comparison-based credit assignment framework that reduces gradient variance in multi-step reasoning with large language models. This addresses a critical bottleneck in reinforcement learning for LLMs—sparse terminal rewards causing unstable training—and could significantly improve performance on complex reasoning tasks like math and code generation. IBPO samples multiple reasoning trajectories under the same input and uses their differences as an implicit advantage estimator to provide step-sensitive learning signals, transforming sparse rewards into dense feedback.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Reinforcement learning for multi-step reasoning with LLMs often relies on sparse terminal rewards, which are propagated equally to all intermediate steps, causing high gradient variance and inefficient updates. Credit assignment is the problem of measuring each action's contribution to future rewards, and counterfactual reasoning compares alternative decisions to isolate an action's effect. Prior work like Counterfactual Credit Assignment (CCA) and COMA explored similar ideas in model-free and multi-agent settings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2011.09464">[2011.09464] Counterfactual Credit Assignment in Model-Free...</a></li>
<li><a href="https://kunkuang.github.io/papers/KDD21-ShapleyMARL.pdf">Shapley Counterfactual Credits for Multi-Agent Reinforcement ...</a></li>
<li><a href="https://proceedings.mlr.press/v139/mesnard21a/mesnard21a.pdf">Counterfactual Credit Assignment in Model-Free Reinforcement ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#credit assignment`, `#multi-step reasoning`, `#counterfactual reasoning`

---

<a id="item-19"></a>
## [SignMuon: 1-bit Distributed Optimizer Cuts Communication by 32x](https://arxiv.org/abs/2605.16311) ⭐️ 8.0/10

Researchers propose SignMuon, a distributed optimizer that combines signSGD's majority-vote sign aggregation with Muon's polar-step framework, achieving O(1/sqrt(T)) convergence with only 1-bit gradient communication per iteration. This work addresses the communication bottleneck in distributed training of large neural networks, offering a 32x bandwidth reduction over float32 while maintaining strong convergence guarantees and practical performance gains. SignMuon uses Newton-Schulz iteration for local polar decomposition, transmits only entrywise signs aggregated by majority vote, and achieves 92.15% validation accuracy on CIFAR-10/ResNet-50 across 330 configurations.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Distributed training often requires communicating full-precision gradients, which becomes a bottleneck as model sizes grow. SignSGD reduces communication by transmitting only gradient signs, while Muon leverages matrix structure via polar steps for better optimization. SignMuon combines both approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon : An optimizer for hidden layers in neural networks</a></li>
<li><a href="https://grokipedia.com/page/newtonschulz-iteration">Newton–Schulz iteration</a></li>

</ul>
</details>

**Tags**: `#distributed training`, `#optimization`, `#communication efficiency`, `#deep learning`

---

<a id="item-20"></a>
## [Adversarial Action Removal in Self-Play RL](https://arxiv.org/abs/2605.16312) ⭐️ 8.0/10

This paper introduces adversarial action masking in self-play reinforcement learning, where an attacker selectively removes legal actions from a victim's action set, causing substantial damage across multiple algorithms and domains. This work identifies action availability as a distinct robustness surface in self-play RL, highlighting a new vulnerability that could impact the safety and reliability of RL systems in competitive environments. The attack persists across Q-learning, PPO, NFSP, neural NFSP, and DQN victims, transfers across agents, is amplified by self-play, and shows no recovery under extended masked training.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Self-play reinforcement learning is a technique where an agent improves by playing against itself, commonly used in games like chess and Go. Action masking is a method to restrict an agent's available actions, often used to enforce game rules. This paper studies a novel adversarial attack that exploits action masking to remove critical actions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://arxiv.org/pdf/2006.14171">A Closer Look at Invalid Action Masking in Policy Gradient Algorithms</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#adversarial attack`, `#self-play`, `#robustness`, `#AI safety`

---

<a id="item-21"></a>
## [Decision Capacity Threshold Causes Collapse in Self-Play RL](https://arxiv.org/abs/2605.16315) ⭐️ 8.0/10

A new study reveals a sharp threshold in decision capacity that determines whether self-play reinforcement learning agents collapse under asymmetric rule perturbations, with the boundary at zero reach-weighted contingent action capacity. This finding is significant for multi-agent reinforcement learning and AI safety, as it identifies a fundamental mechanism that can cause catastrophic failure in self-play systems, which are widely used in game AI and autonomous training. The collapse is characterized by rapid convergence to a deterministic exploitation attractor at near-maximal loss, and it is fully reversible upon action restoration. The phenomenon intensifies under function approximation and is timing-invariant.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Self-play reinforcement learning involves an agent training by playing against copies of itself, commonly used in games like Go and poker. Decision capacity refers to the set of actions an agent can take in different states; reach-weighted contingent action capacity measures the number of decision points reachable under a policy. Asymmetric rule perturbations alter the rules for one agent, potentially causing co-adaptation issues.

**Tags**: `#reinforcement learning`, `#self-play`, `#multi-agent systems`, `#AI safety`, `#game theory`

---

<a id="item-22"></a>
## [AdaGraph: Graph-Native Clustering Defeats Curse of Dimensionality](https://arxiv.org/abs/2605.16320) ⭐️ 8.0/10

Researchers introduced AdaGraph, a graph-native clustering algorithm that operates entirely within kNN graph topology to overcome the curse of dimensionality, requiring no pre-specified cluster count and handling noise natively. AdaGraph enables scientific discovery in high-dimensional domains like genomics and materials science where traditional distance-based clustering fails, potentially transforming unsupervised learning for high-dimensional data analysis. AdaGraph pairs with Graph-SCOPE, a topology-based cluster validity index, which achieved mean ARI=0.900 on synthetic benchmarks from d=10 to d=5000, outperforming Silhouette, Davies-Bouldin, and Calinski-Harabasz. It also demonstrated a 62% relative improvement over HDBSCAN on text clustering (20NG-6cat).

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Clustering high-dimensional data is challenging because Euclidean distance becomes uninformative—a phenomenon known as the curse of dimensionality. Traditional clustering algorithms rely on distance metrics, making them ineffective in high dimensions. AdaGraph uses kNN graph topology, which preserves meaningful relational structure even in arbitrarily high dimensions, fundamentally dissolving the curse.

<details><summary>References</summary>
<ul>
<li><a href="https://inria.hal.science/hal-01407514/document">Nearest Neighbors Graph Construction: Peer Sampling to the Rescue</a></li>
<li><a href="https://jmlr.csail.mit.edu/papers/volume21/19-1032/19-1032.pdf">I.e., although the topology of the original graph might</a></li>

</ul>
</details>

**Tags**: `#clustering`, `#high-dimensional data`, `#graph algorithms`, `#unsupervised learning`, `#curse of dimensionality`

---

<a id="item-23"></a>
## [Language Game Enables Dialogue with Non-Neural Systems](https://arxiv.org/abs/2605.16321) ⭐️ 8.0/10

A new framework treats communication with non-neural biological systems as a language game, using reinforcement learning to train only linear interfaces while keeping internal dynamics frozen, allowing systems like gene regulatory networks to 'speak' through their own behavior. This approach challenges current AI-centric methods where large language models speak on behalf of biological systems, potentially enabling direct, authentic communication with diverse non-human intelligences and opening new avenues in AI, biology, and philosophy. The framework uses a language model to route human prompts to the game whose semantics best match, designing an environmental state where the desired action is the rational response, letting the system reply through behavior without altering any system parameters.

rss · arXiv - Machine Learning · May 19, 04:00

**Background**: Non-neural biological systems like gene regulatory networks and microbial consortia are increasingly recognized as substrates of computation and decision-making. Traditional approaches use large language models as proxies to interpret these systems, but the paper argues this silences the system's own intelligence. Inspired by Wittgenstein's philosophy that meaning is in use, the authors treat communication as a game where the system's states gain meaning through interaction and reward.

**Tags**: `#reinforcement learning`, `#biological computation`, `#language games`, `#non-human intelligence`, `#philosophy of mind`

---

<a id="item-24"></a>
## [Scaling Laws for Skills in LLM Agent Systems](https://arxiv.org/abs/2605.16508) ⭐️ 8.0/10

A new paper identifies two coupled scaling laws for skill libraries in LLM agent systems: routing accuracy decays logarithmically with library size, and correct execution can rescue difficult decisions by about 4x. These laws provide actionable insights for designing scalable AI agent systems, showing that performance depends not only on model capability but also on skill library structure, granularity, and exposure policy. The study involved 15 frontier LLMs, 1,141 real-world skills, and over 3 million routing or execution decisions. Law-guided optimization improved held-out routing accuracy from 71.3% to 91.7% and reduced hijack from 22.4% to 4.1%.

rss · arXiv - NLP · May 19, 04:00

**Background**: LLM agent systems often use skill libraries—collections of reusable functions or tools—to perform complex tasks. As these libraries grow, understanding how scaling affects performance is critical for efficient system design.

**Tags**: `#LLM agents`, `#scaling laws`, `#skill libraries`, `#AI systems`, `#empirical study`

---

<a id="item-25"></a>
## [CHI-Bench: Benchmarking AI Agents on Complex Healthcare Workflows](https://arxiv.org/abs/2605.16679) ⭐️ 8.0/10

Researchers introduced CHI-Bench, a benchmark for evaluating AI agents on end-to-end, long-horizon healthcare workflows that require policy density, multi-role composition, and multilateral interactions. The benchmark includes 30 agent configurations, with the best agent achieving only 28.0% task resolution and no agent exceeding 20% on strict pass^3. This benchmark highlights critical gaps in current AI agents' ability to handle policy-dense, multi-role, and irreversible enterprise workflows, which are common in healthcare and other regulated industries. The findings suggest that similar performance gaps likely exist in other domains, underscoring the need for more robust agent architectures. CHI-Bench simulates three healthcare domains (prior authorization, utilization management, care management) using a high-fidelity simulator with 20 apps exposed via 87 MCP tools and a 1,290+ document operations handbook. When executing all tasks in a single session, performance drops to 3.8%, indicating severe challenges in long-horizon task execution.

rss · arXiv - NLP · May 19, 04:00

**Background**: AI agents are increasingly used to automate complex workflows, but existing benchmarks often focus on simple, single-role tasks with limited policy constraints. Healthcare operations involve intricate rules, multiple roles (e.g., provider, payer, patient), and multi-turn interactions, making them a challenging testbed for agent capabilities. CHI-Bench is designed to fill this gap by providing a realistic and comprehensive evaluation environment.

**Tags**: `#AI agents`, `#healthcare automation`, `#benchmark`, `#workflow automation`, `#multi-role`

---

<a id="item-26"></a>
## [LAD-Inspired Pre-Pretraining Boosts LLM Data Efficiency](https://arxiv.org/abs/2605.16758) ⭐️ 8.0/10

This paper introduces LAD-inspired pre-pretraining on a formal language called MP-STRUCT, which encodes hierarchical composition, feature-based dependencies, and long-distance displacement via MERGE, AGREE, and MOVE operations. A brief 500-step pre-pretraining with MP-STRUCT matches strong formal-language baselines in token efficiency and imparts human-like resistance to structurally implausible languages. This work addresses the data efficiency gap between LLMs and humans, potentially reducing the amount of natural language data needed for training. It also bridges cognitive science and NLP by showing that innate structural biases can be effectively instilled via pre-pretraining on a carefully designed formal language. The MP-STRUCT language is not definable in C-RASP, a formal bound on transformer expressivity, challenging the prior hypothesis that effective pre-pretraining languages must be both hierarchically expressive and circuit-theoretically learnable. The study identifies functional landmarks that reduce dependency resolution ambiguity as a key driver of MP-STRUCT's effectiveness.

rss · arXiv - NLP · May 19, 04:00

**Background**: Large Language Models (LLMs) require vast amounts of text data to achieve human-like language understanding, whereas humans learn language from limited exposure, partly due to innate biases hypothesized as the Language Acquisition Device (LAD). Pre-pretraining (PPT) on synthetic formal languages has been explored to inject useful inductive biases into LLMs before main training. Prior work focused on highly expressive formal languages like k-Shuffle Dyck, which are both hierarchically structured and learnable by transformers.

**Tags**: `#large language models`, `#language acquisition`, `#pre-pretraining`, `#formal languages`, `#NLP`

---

<a id="item-27"></a>
## [Retrieval-Based Legal Annotation Outperforms Generative LLMs](https://arxiv.org/abs/2605.16767) ⭐️ 8.0/10

Researchers propose a retrieval-based method for multi-label legal annotation that uses a frozen retrieval model and k-nearest neighbors, avoiding retraining and outperforming generative LLMs like GPT-5.2 in accuracy and efficiency. This approach offers a practical, data-efficient, and hallucination-free alternative for legal annotation, especially in high-cardinality and rapidly changing label spaces, potentially reducing compute costs by 20-30 times. On the Eurlex dataset with 100 labels, retrieval with Qwen-8B improved Macro-F1 from 40.41 (GPT-5.2 zero-shot) to 49.12, while reducing compute by 20-30 times compared to fine-tuning. With only 100 training samples, retrieval nearly doubled Micro-F1 over hierarchical Legal-BERT on ECtHR-A (48.29 vs. 27.87).

rss · arXiv - NLP · May 19, 04:00

**Background**: Multi-label legal annotation involves assigning multiple labels from large, evolving taxonomies to lengthy legal documents. Traditional parametric encoders require retraining when labels change, and generative LLMs can hallucinate labels outside the taxonomy, becoming costly as label space grows.

**Tags**: `#legal annotation`, `#retrieval`, `#multi-label classification`, `#data efficiency`, `#NLP`

---

<a id="item-28"></a>
## [Noise2Params: Unifying Event Camera Model via Photon Statistics](https://arxiv.org/abs/2605.16317) ⭐️ 8.0/10

Researchers developed Noise2Params, a method that uses a unified probabilistic model based on photon statistics to determine event camera parameters from noise recordings of static scenes. This work provides a quantitative foundation for event camera calibration and noise-aware algorithm design, potentially improving performance in photon-limited regimes and reducing the need for specialized dynamic light sources. The model unifies static noise events and step response curves (S-curves) into a single analytical framework, deriving three probability distributions (exact Poisson, saddle-point, Gaussian) covering all intensity regimes.

rss · arXiv - Computer Vision · May 19, 04:00

**Background**: Event cameras are bio-inspired sensors that report pixel-level brightness changes asynchronously, but their noise and response characteristics are often modeled separately. This work bridges that gap by grounding the model in photon statistics, revealing the connection between noise events and S-curves.

**Tags**: `#event cameras`, `#probabilistic model`, `#computer vision`, `#sensor calibration`

---

<a id="item-29"></a>
## [GeoSym127K: Scalable Neuro-Symbolic Engine for Geometric Reasoning](https://arxiv.org/abs/2605.16371) ⭐️ 8.0/10

Researchers introduce GeoSym127K, a large-scale dataset of 127K questions with symbolic ground truths and 55K answer-verified Chain-of-Thought pairs, generated by a novel neuro-symbolic engine called GeoSym Engine. The engine uses a type-conditional grammar and an analytic SymGT Solver to produce high-precision geometric diagrams and exact symbolic solutions. This work addresses key limitations of Large Multimodal Models (LMMs) in geometric reasoning, such as visual hallucinations and lack of precise Chain-of-Thought data. The GeoSym Engine enables scalable generation of high-quality training data, leading to significant performance gains on diagram-dependent and multi-step geometry tasks, with the Qwen3-VL-8B model achieving a +22.21% improvement on MathVerse Vision-Only subset. The dataset includes 51K high-resolution images and is difficulty-stratified. The authors also introduce GeoSym-Bench, an expert-curated benchmark of 511 complex samples for rigorous evaluation. Applying reinforcement learning with verifiable rewards (RLVR) via GRPO shows that initializing from structural SFT checkpoints further elevates performance.

rss · arXiv - Computer Vision · May 19, 04:00

**Background**: Large Multimodal Models (LMMs) combine vision and language capabilities but often fail at geometric reasoning due to visual hallucinations and lack of precise step-by-step reasoning data. Neuro-symbolic AI integrates neural networks with symbolic reasoning to combine pattern recognition with logical precision. The SymGT Solver is an analytic solver that derives exact symbolic ground truths for geometric problems, similar to SMT solvers used in formal verification.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SMT_solver">SMT solver</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#geometric reasoning`, `#neuro-symbolic`, `#dataset`, `#LMM`

---

<a id="item-30"></a>
## [StreamPro: Proactive Decision-Making in Streaming Video](https://arxiv.org/abs/2605.16381) ⭐️ 8.0/10

Researchers introduced StreamPro-Bench, a benchmark for proactive streaming video understanding, and StreamPro, a two-stage training framework that achieves 41.5 on the benchmark, far surpassing the previous best of 10.4. This work shifts video understanding from reactive 'see-then-answer' to proactive decision-making, enabling AI systems to make timely and reliable decisions under partial observations, which is critical for real-time applications like autonomous driving and surveillance. The benchmark evaluates models on Perception Understanding, Temporal Reasoning, and Proactive Agency; the framework uses CB-Stream Loss for supervised fine-tuning and GRPO with multi-grained rewards to optimize both correctness and timing.

rss · arXiv - Computer Vision · May 19, 04:00

**Background**: Traditional video benchmarks follow a 'see-then-answer' paradigm where responses are triggered only after explicit evidence appears, failing to evaluate proactive reasoning. Proactive understanding requires models to decide when to respond under incomplete observations, balancing early prediction against sufficient evidence.

**Tags**: `#video understanding`, `#proactive decision-making`, `#benchmark`, `#streaming video`, `#AI`

---

<a id="item-31"></a>
## [TaTok: Adaptive Image Tokenization with Global Tokens](https://arxiv.org/abs/2605.16384) ⭐️ 8.0/10

TaTok introduces a theoretically grounded adaptive image tokenization framework that uses global tokens and dynamic token filtering to reduce redundancy and improve reconstruction quality, achieving a 1.3x gFID improvement and 8.7x inference speedup. This work addresses a fundamental limitation in discrete image tokenization—fixed-rate compression ignoring variable information density—which can significantly improve the efficiency and quality of image processing and generative models. TaTok introduces global tokens to model mutual information across patch tokens and a Dynamic Token Filtering (DTF) algorithm based on cumulative conditional entropy to eliminate redundancy, achieving state-of-the-art performance.

rss · arXiv - Computer Vision · May 19, 04:00

**Background**: Discrete image tokenization converts images into sequences of discrete tokens for processing by models like transformers. Current methods compress all content at a fixed rate, leading to redundancy in low-information regions and information loss in high-detail areas. TaTok adaptively allocates tokens based on information richness, inspired by information entropy theory.

**Tags**: `#image tokenization`, `#information entropy`, `#computer vision`, `#deep learning`, `#generative models`

---

<a id="item-32"></a>
## [StAD: Fast Likelihood Estimation for Diffusion Models via Stein Operator](https://arxiv.org/abs/2605.16486) ⭐️ 8.0/10

StAD introduces a distillation method that uses the Langevin-Stein operator to predict the divergence of probability flow ODEs without computing the Jacobian, enabling faster and more accurate likelihood estimation for diffusion and flow-based models. This addresses a key computational bottleneck in likelihood estimation for generative models, which is crucial for Bayesian analysis and other workflows, and the method shows improved variance and speed over existing stochastic estimators like Hutchinson. StAD is validated on CIFAR-10, ImageNet, and other density estimation tasks, consistently outperforming the Hutchinson and Hutch++ estimators in variance and speed. The method also generalizes to a varied class of generative models and can satisfy the Stein class under regularity conditions.

rss · arXiv - Data Science & Statistics · May 19, 04:00

**Background**: Diffusion and flow-based models use a probability flow ODE (PF-ODE) to transport probability mass, and likelihood estimation requires computing the trace of the Jacobian of the PF-ODE. Exact computation is O(D^2) and stochastic estimators like Hutchinson provide O(D) but with noisy estimates. StAD leverages the Langevin-Stein operator to learn the divergence directly, avoiding Jacobian computation.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Hutchinson_Trace_Estimator">Hutchinson Trace Estimator</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#likelihood estimation`, `#normalizing flows`, `#density estimation`, `#machine learning`

---

<a id="item-33"></a>
## [Prediction-Intervention Games and Invariant Sets](https://arxiv.org/abs/2605.16828) ⭐️ 8.0/10

This paper introduces prediction-intervention games, a Stackelberg game framework where a leader chooses a prediction function and a follower intervenes on covariates. It proves that predictors based on the stable blanket, an invariant subset, are always at least as good as those based on causal parents under two common follower objectives. This work bridges causal inference and game theory, offering a principled way to design robust predictors against strategic interventions. It has implications for machine learning systems deployed in adversarial or interactive environments, such as recommendation systems or automated decision-making. The stable blanket is a specific invariant subset that generalizes the causal parents. The paper provides worst-case risk bounds and sufficient conditions for stable-blanket predictors to be optimal, and tests strategies on simulated and real-world data.

rss · arXiv - Data Science & Statistics · May 19, 04:00

**Background**: In causal inference, the causal parents of a target variable are its direct causes. Invariant prediction aims to find subsets of covariates that remain predictive under distribution shifts. Stackelberg games model leader-follower dynamics where the leader commits first. This paper combines these ideas to handle strategic interventions.

**Tags**: `#causal inference`, `#game theory`, `#invariant prediction`, `#machine learning`, `#structural causal models`

---

<a id="item-34"></a>
## [Fourier Analysis Reveals Simplicity Bias in Neural Networks](https://arxiv.org/abs/2605.16913) ⭐️ 8.0/10

This paper uses Fourier analysis to study neural network learning dynamics, showing that networks learn amplitude information before phase information, and introduces a synthetic data model for translation-invariant inputs. 这项工作通过提供对简单性偏好的机制性见解，弥合了理论与实验之间的差距，对于理解神经网络如何高效学习自然图像分布至关重要。 The authors rigorously show that for isotropic inputs, SGD cannot distinguish structured phase information from noise in n << N^3 steps, but power-law spectra can dramatically accelerate learning of phase information.

rss · arXiv - Data Science & Statistics · May 19, 04:00

**Background**: Neural networks trained with gradient descent often exhibit a simplicity bias, learning simpler features before complex ones. Previous analyses focused on isotropic inputs, but natural images have translation-invariance and power-law spectra. Fourier analysis decomposes signals into amplitude (related to pairwise correlations) and phase (encoding edges and higher-order correlations).

**Tags**: `#neural networks`, `#learning dynamics`, `#simplicity bias`, `#Fourier analysis`, `#image classification`

---

<a id="item-35"></a>
## [Stochastic Operator Networks for Uncertainty in SPDEs](https://arxiv.org/abs/2605.17107) ⭐️ 8.0/10

Researchers introduced Stochastic Operator Networks (SON), a framework combining DeepONet with Stochastic Neural Networks to learn solution operators for stochastic PDEs directly from noisy data, outputting both mean solution and uncertainty. This addresses a critical gap in scientific machine learning by enabling uncertainty quantification for SPDEs without requiring prior knowledge of model uncertainties, which is essential for reliable predictions in complex physical systems. The training minimizes a Hamiltonian-type loss optimized via the Stochastic Maximum Principle. Numerical experiments on benchmark SPDEs with multiple uncertainty sources demonstrated accuracy and robustness.

rss · arXiv - Data Science & Statistics · May 19, 04:00

**Background**: Stochastic partial differential equations (SPDEs) model physical systems under uncertainty but require specifying unknown model uncertainties. Deep Operator Networks (DeepONet) learn deterministic solution operators, while Stochastic Neural Networks (SNNs) model probabilistic outputs. This work merges both to handle noisy data.

**Tags**: `#operator learning`, `#uncertainty quantification`, `#stochastic PDEs`, `#deep learning`, `#scientific machine learning`

---

<a id="item-36"></a>
## [Noisy Inductive Matrix Completion Achieves Sample Efficiency](https://arxiv.org/abs/2605.17189) ⭐️ 8.0/10

A new nonconvex projected gradient descent algorithm with spectral initialization achieves sample complexity scaling with side information dimension rather than ambient dimension for noisy inductive matrix completion. This bridges a gap between noiseless and noisy regimes, enabling sample-efficient matrix completion in practical noisy settings, with potential impact on recommender systems and signal processing. The method maintains reduced sample complexity even with inexact side information, and the estimation error is order-optimal with respect to the inexactness. Experiments on MovieLens validate the theory.

rss · arXiv - Data Science & Statistics · May 19, 04:00

**Background**: Matrix completion aims to recover a low-rank matrix from partial observations. Inductive matrix completion (IMC) uses side information (e.g., user/item features) to reduce the search space. Prior work either achieved sample efficiency only in noiseless settings or handled noise but required sample complexity scaling with ambient dimension.

<details><summary>References</summary>
<ul>
<li><a href="https://bigdata.oden.utexas.edu/software/inductive-matrix-completion/">Inductive Matrix Completion | Center for Big Data Analytics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sample_complexity">Sample complexity</a></li>

</ul>
</details>

**Tags**: `#matrix completion`, `#sample complexity`, `#nonconvex optimization`, `#side information`, `#low-rank`

---

<a id="item-37"></a>
## [Anduril and Meta's AR Glasses for Drone Warfare](https://www.technologyreview.com/2026/05/18/1137412/inside-anduril-and-metas-quest-to-make-smart-glasses-for-warfare/) ⭐️ 8.0/10

Anduril revealed new details about its augmented-reality headset prototype with Meta, which could enable soldiers to order drone strikes using eye-tracking and voice commands. This collaboration between a major defense contractor and a leading tech company marks a significant step in integrating consumer AR technology into military operations, potentially changing how warfare is conducted. The headset is being prototyped for the U.S. military, and Quay Barnett, a former Army Special Operations officer, is leading the effort at Anduril.

rss · MIT Technology Review · May 18, 16:01

**Background**: Augmented reality (AR) overlays digital information onto the real world. Anduril is a defense-tech company known for AI-driven surveillance systems, while Meta is a consumer tech giant investing heavily in AR/VR. Their partnership aims to adapt Meta's smart glasses for battlefield use.

**Tags**: `#augmented reality`, `#defense technology`, `#AI`, `#military`, `#Meta`

---