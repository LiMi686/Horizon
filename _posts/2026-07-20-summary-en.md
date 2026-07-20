---
layout: default
title: "Horizon Summary: 2026-07-20 (EN)"
date: 2026-07-20
lang: en
---

> From 109 items, 34 important content pieces were selected

---

1. [Leaked Email: Altman Proposed Open-Sourcing GPT-3-Level Model](#item-1) ⭐️ 9.0/10
2. [LLMs' Verbalizable Representations Form Global Workspace](#item-2) ⭐️ 9.0/10
3. [China's open-weights AI strategy is winning](#item-3) ⭐️ 8.0/10
4. [Hacker wipes Romania's land registry database](#item-4) ⭐️ 8.0/10
5. [AI Writing on arXiv: Sharp Rise, Detection Limits](#item-5) ⭐️ 8.0/10
6. [Frontier AI Lab Economics and Open-Weight Shifts](#item-6) ⭐️ 8.0/10
7. [Ben Thompson Proposes US Law to Boost Open AI Models](#item-7) ⭐️ 8.0/10
8. [KTransformers: Flexible Framework for Heterogeneous LLM Inference](#item-8) ⭐️ 8.0/10
9. [GitHub Releases Official Copilot SDK for Six Platforms](#item-9) ⭐️ 8.0/10
10. [PostHog Launches Self-Driving Mode for AI-Powered Product Development](#item-10) ⭐️ 8.0/10
11. [Windows Terminal: Modern Open-Source Command-Line for Windows](#item-11) ⭐️ 8.0/10
12. [Cua: Open-Source Infrastructure for Scaling Computer-Use 2.0](#item-12) ⭐️ 8.0/10
13. [Build Your Own X: Learn by Recreating Tech](#item-13) ⭐️ 8.0/10
14. [LingBot-Map: Streaming 3D Reconstruction Foundation Model](#item-14) ⭐️ 8.0/10
15. [Cura 1T: Healthcare LLM with Human-Gated Self-Evolution](#item-15) ⭐️ 8.0/10
16. [Reviewer Precision Doesn't Ensure Critique Uptake in Multi-Agent Math](#item-16) ⭐️ 8.0/10
17. [DrawingVQA: Benchmark for Construction Drawing AI](#item-17) ⭐️ 8.0/10
18. [Ablation Study on ARC-AGI-3 Agent Components](#item-18) ⭐️ 8.0/10
19. [Turning Black-Box RL into Explainable Prolog Programs](#item-19) ⭐️ 8.0/10
20. [Quantum Program Generation Must Prioritize Validity Over Scaling](#item-20) ⭐️ 8.0/10
21. [Stochastic Reset Pathfinding: New Bandit Problem on Graphs](#item-21) ⭐️ 8.0/10
22. [VarRate: Training-Free Variable-Rate KV Cache Compression](#item-22) ⭐️ 8.0/10
23. [SkillCorpus: Unifying 96K Open-Source Agent Skills](#item-23) ⭐️ 8.0/10
24. [PATR: Process-Guided Tree Rollout for Multi-Turn RL](#item-24) ⭐️ 8.0/10
25. [Benchmarking LLMs on Prospective Hypothesis Discovery](#item-25) ⭐️ 8.0/10
26. [RL Boosts Part-Level Visual Grounding in MLLMs](#item-26) ⭐️ 8.0/10
27. [Stable Signal Principle Explains Retraining Dynamics](#item-27) ⭐️ 8.0/10
28. [Prediction-Only Self-Distillation Outperforms Teacher in Regression](#item-28) ⭐️ 8.0/10
29. [Diffusion models recover accurate mixture weights despite score insensitivity](#item-29) ⭐️ 8.0/10
30. [BIHT Convergence Without Normalization Proved Optimal](#item-30) ⭐️ 8.0/10
31. [New Protocol Evaluates Temporal Fidelity in Synthetic Data](#item-31) ⭐️ 8.0/10
32. [AI develops its own hiring biases beyond training data](#item-32) ⭐️ 8.0/10
33. [Alzheimer's sleep loss linked to microglia, not plaques](#item-33) ⭐️ 8.0/10
34. [SORLA Protein Shields Brain from Alzheimer's Tau Tangles](#item-34) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Leaked Email: Altman Proposed Open-Sourcing GPT-3-Level Model](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 9.0/10

A leaked email from Sam Altman to OpenAI's board, dated October 1, 2022, reveals he proposed releasing a GPT-3-level open-source model that can run on consumer hardware, aiming to discourage competitors and hinder new funding. The email was exposed in the Musk v. Altman legal case in 2026. This revelation is highly significant for AI ethics and open-source strategy, as it suggests OpenAI's leadership considered open-sourcing not purely for public benefit but as a competitive tactic. It also fuels the ongoing Musk v. Altman legal battle and raises questions about the true motivations behind AI openness. The email specifically mentions releasing a model with "approximate capability of GPT-3" that can "run locally on consumer hardware," and states the goal is to "discourage others from releasing similarly-powerful models" and "make it harder for new efforts to get funded." The email was written before Stability AI or others released similar models.

rss · Simon Willison · Jul 20, 03:47

**Background**: GPT-3 is a large language model with 175 billion parameters, released by OpenAI in 2020. OpenAI initially chose not to open-source GPT-2 due to misuse concerns, and later GPT-3 was also not open-sourced. By 2026, running LLMs on consumer hardware has become feasible due to advances in quantization and hardware, with models like Llama 3 and Mistral available locally.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-3">GPT-3 - Wikipedia</a></li>
<li><a href="https://www.birjob.com/blog/edge-inference-2026">Local LLM Inference on Consumer Hardware in 2026: Strix... | BirJob</a></li>

</ul>
</details>

**Tags**: `#openai`, `#sam-altman`, `#open-source`, `#ai-ethics`, `#gpt-3`

---

<a id="item-2"></a>
## [LLMs' Verbalizable Representations Form Global Workspace](https://arxiv.org/abs/2607.15495) ⭐️ 9.0/10

Researchers at Anthropic introduced the Jacobian lens, a new interpretability technique that identifies a small set of internal representations (J-space) in large language models that function as a global workspace, enabling verbal report, deliberate control, and flexible reasoning. This work provides a practical window into LLMs' unspoken thinking, revealing strategic deliberation and misaligned dispositions that never appear in outputs, which could significantly improve AI safety and alignment audits. The J-space carries coherent content only in an intermediate band of layers, holds on the order of tens of concepts at a time, and is broadcast by the model's weights more widely than other representations; post-training installs the Assistant's point of view in the workspace.

rss · arXiv - NLP · Jul 20, 04:00

**Background**: Global workspace theory (GWT), proposed by Bernard Baars in 1988, posits that consciousness arises from a centralized mechanism that integrates and broadcasts selected information to specialized processors. The Jacobian lens reads out what an internal activation is disposed to make the model say, analogous to probing conscious access in humans.

<details><summary>References</summary>
<ul>
<li><a href="https://explainx.ai/blog/what-is-j-lens-jacobian-lens-claude-interpretability-2026">What Is the J-Lens? Anthropic Jacobian Lens Guide</a></li>
<li><a href="https://github.com/anthropics/jacobian-lens">GitHub - anthropics/jacobian-lens: Companion code for the global workspace interpretability paper · GitHub</a></li>
<li><a href="https://www.anthropic.com/research/global-workspace">A global workspace in language models \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#large language models`, `#global workspace theory`, `#cognitive science`, `#AI safety`

---

<a id="item-3"></a>
## [China's open-weights AI strategy is winning](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

An analysis argues that China's open-weights AI models are outperforming proprietary US models due to lower costs and strong ecosystem effects, echoing historical trends where free or low-end solutions dominate. This shift could reshape the global AI landscape, making advanced AI more accessible and reducing the dominance of US proprietary models, with significant implications for startups, enterprises, and AI governance. The article notes that 80% of startups are using Chinese models, though some commenters question this figure. Open-weights models are not fully open-source but allow free use and fine-tuning, with hosting costs only.

hackernews · benwerd · Jul 20, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48979269)

**Background**: Open-weights AI models are models whose trained parameters (weights) are publicly released, allowing anyone to download, run, and fine-tune them, but the training data and code may not be fully open. This contrasts with proprietary models like GPT-4 or Claude, which are only accessible via API and controlled by their creators. Historically, free and low-end solutions (e.g., Linux, Windows) have often defeated expensive proprietary alternatives in computing markets.

<details><summary>References</summary>
<ul>
<li><a href="https://lmmarketcap.com/open-source-ai-models">Best Open Source AI Models & LLM Leaderboard (2026)</a></li>
<li><a href="https://www.gumloop.com/blog/open-weight-ai-models">7 best open weight AI models I've tested in 2026 - gumloop.com</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the historical parallel, noting that free/low-end solutions have consistently won in computing. Some question the claim that 80% of startups use Chinese models, citing personal experience with US models. Others highlight that open-weights models are not truly open-source, but still offer cost advantages.

**Tags**: `#AI`, `#open-source`, `#China`, `#industry analysis`, `#economics`

---

<a id="item-4"></a>
## [Hacker wipes Romania's land registry database](https://news.risky.biz/risky-bulletin-hacker-wipes-romanias-entire-land-registry-database/) ⭐️ 8.0/10

A hacker breached Romania's National Agency for Cadastre and Land Registration (ANCPI) and wiped the entire land registry database, but officials claim to have an offline backup and are rebuilding systems from scratch. This incident threatens the integrity of land ownership records, which could cause societal chaos if not restored, and highlights vulnerabilities in critical national infrastructure. The hacker, identified as Zakaria Mahdjoub from Algeria, claimed to have deleted backups, but ANCPI appears to have had an offline copy. The agency is migrating applications to Romania's Government Cloud, coordinated by the Special Telecommunications Service (STS).

hackernews · speckx · Jul 20, 13:28 · [Discussion](https://news.ycombinator.com/item?id=48978605)

**Background**: Land registry databases are critical for proving property ownership and facilitating real estate transactions. Offline backups are essential for recovery from ransomware or destructive attacks, as they are not accessible from the network and thus immune to remote deletion.

**Discussion**: Commenters noted that the incident may stem from corruption, with IT contracts awarded to cronies who neglect security. Others drew parallels to a similar data loss event in South Korea and discussed the hacker's possible motives regarding extradition.

**Tags**: `#cybersecurity`, `#data breach`, `#critical infrastructure`, `#Romania`, `#backup`

---

<a id="item-5"></a>
## [AI Writing on arXiv: Sharp Rise, Detection Limits](https://unslop.run/blog/measuring-ai-writing-on-arxiv) ⭐️ 8.0/10

A study measured AI-written text in arXiv papers using a tuned detector, finding that by January 2026, 39% of all papers and 65% of computer science papers were flagged as AI-written, with a pre-ChatGPT false positive rate of only 0.4%. This rapid increase in AI-generated academic text raises serious concerns about research integrity, peer review, and the reliability of scientific literature, especially in fields like computer science where adoption is highest. The detector was deliberately tuned to avoid false positives, achieving a pre-ChatGPT detection rate of ~0.4%. Mathematics showed minimal change, barely rising above 0.7%, while computer science peaked at 65%.

hackernews · dopamine_daddy · Jul 20, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48981206)

**Background**: arXiv is a free, open-access repository for scholarly preprints in fields like physics, mathematics, and computer science. AI text detectors analyze features such as word repetition and uniformity to distinguish machine-written from human-written text, but they can produce false positives, especially with formal or technical writing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ArXiv">arXiv - Wikipedia</a></li>
<li><a href="https://arxiv.org/">arXiv.org e-Print archive</a></li>
<li><a href="https://www.grammarly.com/blog/ai/how-do-ai-detectors-work/">How Do AI Detectors Work? Key Methods and Limitations | Grammarly</a></li>

</ul>
</details>

**Discussion**: Community comments highlight skepticism about detection reliability: one user uploaded pre-2012 papers and got high AI scores (27-74%), suggesting detectors may flag formal academic writing as AI. Others question whether detectors can ever reliably distinguish human and AI text, especially when human writing mimics LLM patterns.

**Tags**: `#AI detection`, `#arXiv`, `#academic integrity`, `#LLM impact`, `#measurement`

---

<a id="item-6"></a>
## [Frontier AI Lab Economics and Open-Weight Shifts](https://www.emergingtrajectories.com/lh/frontier-lab-economics/) ⭐️ 8.0/10

An analysis of frontier AI lab economics highlights the impact of open-weight releases like Kimi K3 and Qwen 3.8, and discusses Anthropic's potential unraveling amid competitive dynamics and a conflict-of-interest controversy with Figma. This analysis matters because it reveals how commoditization of AI models and ASIC specialization could reshape the competitive landscape, potentially undermining the business models of frontier labs like Anthropic and OpenAI. The community discussion notes that open-weight models are becoming 'good enough' for many tasks, and that the winner may be the one who burns models to ASICs fastest. The Figma-Anthropic conflict involves a board resignation and allegations of proprietary information misuse.

hackernews · cl42 · Jul 20, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48980019)

**Background**: Frontier AI labs like OpenAI, Anthropic, and Google DeepMind compete to develop the most capable large language models (LLMs). Open-weight models, which allow others to run and fine-tune the models, are increasingly matching proprietary ones in performance, threatening the revenue of frontier labs. ASICs (application-specific integrated circuits) are custom chips designed for AI workloads, offering higher efficiency than GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.computeforecast.com/blogs/ai-asics-vs-gpus/">The Moment of AI ASICs: Specialization Is the New Scale</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia">The custom AI ASIC state of play (May 2026) - Tom's Hardware</a></li>
<li><a href="https://www.linkedin.com/pulse/valuation-validation-economic-test-frontier-ai-still-has-lynes-2296e">Valuation Is Not Validation: The Economic Test Frontier AI Still Has to...</a></li>

</ul>
</details>

**Discussion**: Commenters debate whether model commoditization will erode frontier lab profits, with some arguing that users pay a premium for slightly better models. Others highlight the Figma conflict as a serious breach of trust, while some note that hype cycles are shortening and a plateau may be near.

**Tags**: `#AI`, `#economics`, `#open-source`, `#competition`, `#Anthropic`

---

<a id="item-7"></a>
## [Ben Thompson Proposes US Law to Boost Open AI Models](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 8.0/10

Ben Thompson proposed that the US should pass a law making training data collection fair use and banning terms of service that prohibit distillation, to help US open models compete with Chinese counterparts. This proposal could reshape US AI policy by legalizing common practices and fostering innovation, potentially leveling the playing field in US-China AI competition. Thompson also noted that Alibaba's release of Qwen 3.8 Max as open weights may have been influenced by Xi Jinping's speech encouraging open source and sharing.

rss · Simon Willison · Jul 20, 17:09

**Background**: Distillation is a technique where a smaller 'student' model learns from a larger 'teacher' model, often by querying its API. Fair use for AI training data is a contentious legal issue, with ongoing debates about whether using copyrighted data for training constitutes fair use. Open-weight models release trained parameters but not the full training code or data, unlike open-source models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/how-distillation-makes-ai-models-smaller-and-cheaper-20250718/">How Distillation Makes AI Models Smaller and Cheaper</a></li>
<li><a href="https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright">Artificial intelligence and copyright - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/pulse/frontier-ai-models-closed-vs-open-weight-source-varadaraj-pandurangan-yrdue">Frontier AI Models: Closed vs Open Weight vs Open Source</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open models`, `#distillation`, `#fair use`, `#US-China competition`

---

<a id="item-8"></a>
## [KTransformers: Flexible Framework for Heterogeneous LLM Inference](https://github.com/kvcache-ai/ktransformers) ⭐️ 8.0/10

KTransformers is a flexible framework for cutting-edge LLM inference and fine-tuning optimizations, supporting CPU-GPU heterogeneous computing. It recently added Day0 support for models like MiniMax-M3, GLM-5.2, and DeepSeek-V4-Flash, and introduced CPU-GPU expert scheduling and native BF16/FP8 precision. This framework enables efficient deployment of large models on consumer hardware, lowering the barrier for researchers and developers. Its heterogeneous approach can significantly reduce inference costs and improve performance on mixed hardware setups. KTransformers v0.6.1 separates inference and SFT entry points, and supports AVX2-only CPU backend. It also features CPU-GPU expert scheduling for mixture-of-experts models and native BF16/FP8 per-channel precision.

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: Large language models (LLMs) require significant computational resources for inference and fine-tuning. Heterogeneous computing leverages both CPU and GPU to optimize performance, especially for models with mixture-of-experts architectures. KTransformers is a research project that implements these optimizations in a flexible framework.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2603.28772">Federated Inference for Heterogeneous LLM Communication and...</a></li>
<li><a href="https://github.com/sooskesia/Heterogeneous-LLM-Inference">GitHub - sooskesia/ Heterogeneous - LLM - Inference : your...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#inference`, `#fine-tuning`, `#optimization`, `#framework`

---

<a id="item-9"></a>
## [GitHub Releases Official Copilot SDK for Six Platforms](https://github.com/github/copilot-sdk) ⭐️ 8.0/10

GitHub has released the official Copilot SDK, providing libraries for Node.js/TypeScript, Python, Go, .NET, Rust, and Java that expose the same agent runtime used by Copilot CLI. Developers can now programmatically integrate Copilot's agentic workflows into their own applications. This SDK lowers the barrier for developers to build custom AI agents powered by GitHub Copilot, enabling a new wave of tooling and automation. It marks a shift from Copilot being a standalone assistant to a platform that can be embedded in any application. The SDK is available on npm, PyPI, NuGet, Go modules, crates.io, and Maven Central, with cookbooks and API docs for each language. It handles planning, tool invocation, and file edits, so developers only need to define agent behavior.

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: GitHub Copilot is an AI pair programmer that suggests code in real time inside editors. The Copilot Agent extends this capability to autonomously plan and execute multi-step tasks, and the SDK exposes that agent runtime for custom integrations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for ...</a></li>
<li><a href="https://github.com/features/copilot/agents">GitHub Copilot · Agents on GitHub</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-sdk">Copilot SDK - GitHub Docs</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#Multi-platform`

---

<a id="item-10"></a>
## [PostHog Launches Self-Driving Mode for AI-Powered Product Development](https://github.com/PostHog/posthog) ⭐️ 8.0/10

PostHog, an open-source product analytics platform, has introduced a self-driving mode that automatically converts product signals (errors, rage clicks, failed queries) into researched reports and pull requests for developers to review and merge. This feature significantly reduces the manual effort required to diagnose and fix product issues, enabling teams to build self-driving products that proactively improve themselves. It positions PostHog as a comprehensive developer tool integrating AI observability, analytics, session replay, and more. PostHog's suite includes product analytics, web analytics, session replay, feature flags, experiments, error tracking, logs, surveys, and a data warehouse. The platform can be managed via Slack, web, desktop, or the Model Context Protocol (MCP).

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: PostHog is an open-source platform that provides tools for understanding user behavior and improving products. AI observability refers to monitoring and analyzing AI system behavior in production, while session replay records user interactions for debugging. The Model Context Protocol (MCP) is an open standard for connecting AI systems with external tools and data.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_observability">AI observability</a></li>
<li><a href="https://en.wikipedia.org/wiki/Session_replay">Session replay</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#analytics`, `#open-source`, `#developer-tools`, `#AI-observability`

---

<a id="item-11"></a>
## [Windows Terminal: Modern Open-Source Command-Line for Windows](https://github.com/microsoft/terminal) ⭐️ 8.0/10

Microsoft's Windows Terminal and console host repository on GitHub provides a modern, feature-rich terminal application for Windows, replacing the classic Windows Console. It supports multiple tabs, split panes, GPU-accelerated text rendering, and customization. This project modernizes the command-line experience on Windows, benefiting millions of developers and IT professionals. It integrates seamlessly with WSL, PowerShell, and Command Prompt, enhancing productivity and aligning Windows with modern terminal emulators. Windows Terminal is open-source under the MIT license and available via the Microsoft Store, GitHub releases, and package managers like winget and Chocolatey. It includes a preview channel called Windows Terminal Canary for early feature testing.

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: Windows Console (conhost.exe) has been the default terminal for decades, lacking modern features like tabs and GPU acceleration. Windows Terminal, first released in 2019, addresses these limitations while maintaining compatibility with existing console applications. The repository also includes the console host code, enabling community contributions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Windows_Terminal">Windows Terminal - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/windows/terminal/">An overview on Windows Terminal | Microsoft Learn</a></li>
<li><a href="https://en.wikipedia.org/wiki/Windows_Console">Windows Console - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#terminal`, `#windows`, `#microsoft`, `#open-source`, `#command-line`

---

<a id="item-12"></a>
## [Cua: Open-Source Infrastructure for Scaling Computer-Use 2.0](https://github.com/trycua/cua) ⭐️ 8.0/10

Cua has been released as an open-source project providing drivers, cross-OS fleets, and benchmarks for scaling computer-use 2.0 in training, evaluation, and data generation. This project enables AI agents to control desktop applications in the background across macOS, Windows, and Linux, which is crucial for training and evaluating computer-use agents at scale. Cua includes background drivers that allow agents to click, type, and verify without stealing cursor focus, and supports both X11 and Wayland on Linux. It also provides sandboxes, SDKs, and benchmarks for reinforcement learning environments.

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: Computer-use 2.0 reverses the traditional model where the AI model directly controls the screen; instead, a main agent owns the task and calls the desktop only when needed. This approach improves efficiency and allows more complex workflows. Cua provides the infrastructure to implement this paradigm across multiple operating systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/trycua/cua">trycua/ cua : Scale computer-use 2.0 with open - source drivers ...</a></li>
<li><a href="https://cua.ai/blog/computer-use-2-ai-engineer-worlds-fair">Computer-Use 2.0 | Cua Blog</a></li>
<li><a href="https://cua.ai/">Cua : Scale computer fleets for computer-use agents</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#computer-use`, `#benchmarks`, `#AI/ML`, `#systems`

---

<a id="item-13"></a>
## [Build Your Own X: Learn by Recreating Tech](https://github.com/codecrafters-io/build-your-own-x) ⭐️ 8.0/10

The 'build-your-own-x' repository on GitHub curates step-by-step guides for recreating popular technologies from scratch, covering topics from 3D renderers to programming languages. This resource empowers developers to deeply understand how technologies work by building them, which is more effective than passive learning. It has become a widely shared reference in the developer community for hands-on education. The repository includes guides for over 20 categories, such as databases, Git, Docker, and operating systems. Each guide is a well-written tutorial that walks through the entire process of building a simplified version of the technology.

rss · GitHub Trending - Daily (All) · Jul 20, 22:52

**Background**: The 'learning by building' approach is inspired by Richard Feynman's quote: 'What I cannot create, I do not understand.' This repository aggregates external tutorials and resources, making it a one-stop collection for developers who want to learn through hands-on projects.

**Tags**: `#learning`, `#tutorials`, `#open-source`, `#programming`, `#curriculum`

---

<a id="item-14"></a>
## [LingBot-Map: Streaming 3D Reconstruction Foundation Model](https://github.com/Robbyant/lingbot-map) ⭐️ 8.0/10

LingBot-Map is a feed-forward 3D foundation model for streaming 3D reconstruction, introduced by the Robbyant team. It uses a Geometric Context Transformer to achieve real-time reconstruction at ~20 FPS on 518×378 resolution over sequences exceeding 10,000 frames. This work addresses a key challenge in 3D vision and robotics: online, real-time 3D reconstruction from streaming video with bounded memory. Its feed-forward design and high efficiency could enable practical applications in autonomous navigation, SLAM, and interactive 3D understanding. The model introduces Geometric Context Attention (GCA), which maintains three complementary contexts: an anchor for coordinate grounding, a local pose-reference window for dense geometry, and a trajectory memory for long-range drift correction. It also employs paged KV cache attention for efficient streaming inference.

rss · GitHub Trending - Python · Jul 20, 22:52

**Background**: Streaming 3D reconstruction aims to recover camera poses and 3D geometry from a video stream in real time, which is crucial for robotics and AR/VR. Traditional methods often rely on iterative optimization (e.g., bundle adjustment) that is computationally expensive and not suitable for online settings. Recent feed-forward models like DUSt3R have shown promise but struggle with long sequences and memory constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/geometric-context-transformer-gct">Geometric Context Transformer (GCT)</a></li>
<li><a href="https://paperswithcode.co/paper/2604.14141">Geometric Context Transformer for Streaming... | Papers with Code</a></li>
<li><a href="https://huggingface.co/papers/2604.14141.md">Title: Geometric Context Transformer for Streaming 3D Reconstruction</a></li>

</ul>
</details>

**Tags**: `#3D reconstruction`, `#foundation model`, `#computer vision`, `#deep learning`, `#streaming data`

---

<a id="item-15"></a>
## [Cura 1T: Healthcare LLM with Human-Gated Self-Evolution](https://arxiv.org/abs/2607.15314) ⭐️ 8.0/10

Researchers introduced Cura 1T, a healthcare-specialized large language model trained via a human-gated self-evolution loop that iteratively improves across patient consultation, clinical reasoning, diagnosis, and electronic health record tasks. Cura 1T addresses multi-task degradation in healthcare AI by using a data-centered loop that refines training mixtures from observed failures, achieving top performance across healthcare benchmarks while remaining competitive on general reasoning tasks. The model employs a training agent that plans target capabilities, trains the model, evaluates benchmark trajectories, and refines the data mixture in each evolution round, using targeted synthetic and curated examples rather than a single generic medical-data update.

rss · arXiv - AI · Jul 20, 04:00

**Background**: Healthcare LLMs must handle diverse tasks like patient consultation, clinical reasoning, diagnosis, and EHR tool use, but improving one task can degrade others. Human-gated self-evolution loops incorporate human oversight to prevent capability degradation and safety drift during autonomous evolution, as explored in recent research on self-evolving agents.

<details><summary>References</summary>
<ul>
<li><a href="https://www.actava.ai/cura/cura-technical-report.pdf">Cura 1 T : Specialized Model for Agentic Healthcare</a></li>
<li><a href="https://huggingface.co/papers/2607.15314">Paper page - Cura 1 T : Specialized Model for Agentic Healthcare</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#healthcare AI`, `#self-evolution`, `#multi-task learning`, `#clinical reasoning`

---

<a id="item-16"></a>
## [Reviewer Precision Doesn't Ensure Critique Uptake in Multi-Agent Math](https://arxiv.org/abs/2607.15388) ⭐️ 8.0/10

A new study on 4,181 Omni-MATH problems shows that in multi-agent math reasoning, high reviewer precision (0.861) does not guarantee critique uptake, and broadcast-style peer discussion outperforms hierarchical planner-executor-reviewer pipelines. This challenges the common assumption that adding a dedicated reviewer improves system accuracy, revealing that critique uptake—not just detection—is critical for multi-agent reasoning systems, with implications for designing more effective agent architectures. The broadcast-style peer discussion achieved higher final accuracy than the PER pipeline, despite having lower reviewer precision (0.644 vs 0.861). Forcing explicit acknowledgment in PER lowered accuracy, while embedding reviewer guidance in the solver's context partially improved follow-through.

rss · arXiv - AI · Jul 20, 04:00

**Background**: Multi-agent math reasoning systems often use hierarchical designs where a planner, executor, and reviewer work in sequence, assuming the reviewer's error detection will lead to corrections. This paper empirically separates reviewer detection quality from critique uptake, showing that even precise reviewers may fail to influence the final answer if the system does not act on their critiques.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.15388">Precise but Uncoupled: Reviewer Precision Does Not Guarantee ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#math reasoning`, `#AI`, `#critique uptake`, `#agent architecture`

---

<a id="item-17"></a>
## [DrawingVQA: Benchmark for Construction Drawing AI](https://arxiv.org/abs/2607.15418) ⭐️ 8.0/10

Researchers introduced DrawingVQA, the first benchmark to evaluate multimodal large language models on real-world construction drawings, with 33 drawings and 92 expert-curated QA pairs across three reasoning depths. This benchmark addresses a critical gap in evaluating AI on complex visual-textual engineering documents, potentially accelerating AI integration into construction workflows and improving efficiency in architecture and civil engineering. The benchmark uses a dual categorization framework to jointly analyze performance across seven construction-engineering and four MLLM capability dimensions, revealing a substantial gap between model and expert performance at higher reasoning depths.

rss · arXiv - AI · Jul 20, 04:00

**Background**: Construction drawings are complex documents that combine geometry, symbols, tables, annotations, and domain-specific text, unlike natural images or simple floor plans. Multimodal large language models (MLLMs) process both text and images, but their performance on such specialized documents has been underexplored. DrawingVQA fills this gap by providing a structured evaluation framework.

<details><summary>References</summary>
<ul>
<li><a href="https://pulseaugur.com/cluster/151839-new-drawingvqa-benchmark-tests-mllms-on-complex-construction-drawings">New DrawingVQA benchmark tests MLLMs on complex construction ...</a></li>

</ul>
</details>

**Tags**: `#multimodal LLM`, `#benchmark`, `#construction drawings`, `#visual-textual reasoning`, `#engineering AI`

---

<a id="item-18"></a>
## [Ablation Study on ARC-AGI-3 Agent Components](https://arxiv.org/abs/2607.15439) ⭐️ 8.0/10

This paper systematically ablates components of an ARC-AGI-3 agent—executable world models, simplification, and verification—to determine their individual contributions, finding that stronger models and reasoning effort consistently improve performance. This study clarifies which design choices drive performance on the ARC-AGI-3 benchmark, a key test of agentic reasoning, guiding future research toward verification and model scaling rather than complex world models. The verification variant, which requires exact replay of recorded observations, ranked first in all settings but used substantially more resources; with gpt-5.6-sol it solved all public games at both reasoning efforts, achieving ~99% RHAE.

rss · arXiv - AI · Jul 20, 04:00

**Background**: ARC-AGI-3 is an interactive benchmark for agentic intelligence, requiring agents to explore, infer goals, build internal models, and plan actions in novel environments without explicit instructions. The benchmark extends static grid tasks into multi-turn reasoning problems under partial observability.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://chatpaper.com/paper/311239">Do Coding Agents Need Executable World Models , Simplification...</a></li>

</ul>
</details>

**Tags**: `#ARC-AGI`, `#world models`, `#program synthesis`, `#AI reasoning`, `#ablation study`

---

<a id="item-19"></a>
## [Turning Black-Box RL into Explainable Prolog Programs](https://arxiv.org/abs/2607.15459) ⭐️ 8.0/10

Researchers propose a three-stage post-hoc method that converts a deep reinforcement learning policy into an ordered rule list expressed as a Prolog program, with formal guarantees including a return-loss bound and monotonic improvement. The approach is demonstrated on discrete and continuous control tasks, achieving exact optimal return on a key-and-door task and matching neural teacher performance on Acrobot and CartPole. This work bridges the gap between opaque deep RL models and human-understandable, verifiable decision-making, which is critical for safety-critical applications like autonomous driving or healthcare. By providing formal guarantees, it enables trust and certification of RL policies, advancing the field of explainable AI. The method extracts a frozen PPO teacher, induces an ordered rule list via relational learning, and outputs a Prolog program executable by an off-the-shelf logic engine. A subsequent expansion stage edits rules only when policy evaluation certifies a return increase, ensuring monotonic improvement. For continuous observations, the conversion is possible with a propositional threshold instantiation that achieves O(1/B) disagreement and exponential cost in observation dimension for oblique decision boundaries.

rss · arXiv - AI · Jul 20, 04:00

**Background**: Deep reinforcement learning (RL) policies are often black-box neural networks, making it hard to understand or verify their decisions. Prolog is a logic programming language well-suited for building expert systems because it can represent knowledge as rules and perform inference. This paper combines these areas by distilling a neural policy into a readable Prolog rule list, offering formal guarantees on performance and fidelity.

<details><summary>References</summary>
<ul>
<li><a href="https://www.metalevel.at/prolog/expertsystems">Expert Systems in Prolog - metalevel.at</a></li>
<li><a href="https://en.wikipedia.org/wiki/Proximal_policy_optimization">Proximal policy optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rule_induction">Rule induction - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#explainable AI`, `#reinforcement learning`, `#Prolog`, `#interpretability`, `#formal guarantees`

---

<a id="item-20"></a>
## [Quantum Program Generation Must Prioritize Validity Over Scaling](https://arxiv.org/abs/2607.15313) ⭐️ 8.0/10

A new position paper argues that probabilistic scaling alone cannot ensure validity in quantum circuit generation, proposing a shift to verifier-centric agents with hierarchical constraints. This challenges the dominant scaling hypothesis in AI for quantum computing, potentially redirecting research toward verification-aware architectures that could produce more reliable quantum programs. The paper highlights a syntax-semantics gap in quantum circuits and notes that the valid subset of circuit designs decays exponentially with qubit count, making post-hoc filtering intractable.

rss · arXiv - Machine Learning · Jul 20, 04:00

**Background**: Quantum circuit synthesis involves decomposing quantum operations into executable gate sequences. Hilbert space for N qubits has dimension 2^N, enabling exponential computational power but also making validity checking hard. Current AI approaches often treat quantum program generation as a language modeling task, but this paper argues that physical constraints require different methods.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Quantum_synthesis">Quantum synthesis</a></li>
<li><a href="https://www.linkedin.com/pulse/quantum-trajectory-towards-technologies-from-mathew-chandrankunnel-888oc">Quantum Trajectory towards Quantum Technologies - From Hilbert ...</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#machine learning`, `#program synthesis`, `#verification`

---

<a id="item-21"></a>
## [Stochastic Reset Pathfinding: New Bandit Problem on Graphs](https://arxiv.org/abs/2607.15440) ⭐️ 8.0/10

Researchers introduced Stochastic Reset Pathfinding (SRP), a new episodic learning problem on directed graphs with unknown edge success probabilities, and proposed PathUCB and PathTS algorithms with path-level regret bounds. SRP bridges combinatorial cascading bandits and network optimization, with direct applications to quantum repeater networks, Lightning Network payment routing, and unreliable mesh networks, enabling efficient learning under reset constraints. The path-level regret bound for PathUCB decomposes regret via a per-path complexity combining prefix and suffix reliability, complementing edge-level CCB bounds. Experiments show PathTS performs best empirically but fails on adversarial instances.

rss · arXiv - Machine Learning · Jul 20, 04:00

**Background**: Cascading bandits are a class of combinatorial bandits where the agent selects a list of items and observes outcomes until the first failure. SRP extends this to graph paths with resets, where the agent commits to a source-to-goal path and resets to source upon any edge failure. The optimal policy is open-loop due to global reset structure.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15440">[2607.15440] Stochastic Reset Pathfinding: Path-Level Regret ...</a></li>
<li><a href="https://arxiv.org/abs/1502.02763">[1502.02763] Cascading Bandits: Learning to Rank in the ...</a></li>
<li><a href="https://arxiv.org/abs/1507.04208">[1507.04208] Combinatorial Cascading Bandits</a></li>

</ul>
</details>

**Tags**: `#bandit algorithms`, `#reinforcement learning`, `#graph theory`, `#network optimization`, `#regret analysis`

---

<a id="item-22"></a>
## [VarRate: Training-Free Variable-Rate KV Cache Compression](https://arxiv.org/abs/2607.15498) ⭐️ 8.0/10

VarRate introduces a training-free variable-rate KV cache compression technique that allocates rank based on query salience, avoiding irreversible token eviction and achieving better accuracy than prior methods. This method addresses a critical memory bottleneck in long-context LLM inference, enabling more efficient deployment of large models without sacrificing accuracy. It outperforms existing training-free compression methods and matches the accuracy of training-based approaches at a fraction of the overhead. At a matched 20% budget on LongBench, VarRate stays within 0.8 points of the uncompressed model on both Llama-3.1-8B and Qwen2.5-7B. Against KVzip, a method designed for query-agnostic reuse, it is accuracy-equivalent in three of four settings and within a point overall, at about one-eighth the prefill overhead.

rss · arXiv - NLP · Jul 20, 04:00

**Background**: KV cache stores key-value pairs from previous tokens to accelerate LLM inference, but its memory grows with sequence length, becoming a bottleneck for long-context models. Existing training-free compression methods either evict tokens irreversibly (e.g., SnapKV, Ada-KV) or apply uniform low-rank coding, both of which suffer accuracy degradation under certain conditions. VarRate proposes variable-rate coding that keeps all tokens but allocates rank adaptively based on query salience.

<details><summary>References</summary>
<ul>
<li><a href="https://gigagpu.com/kv-cache-vs-model-quantization/">KV Cache vs Model Quantization: What to Compress GIGAGPU</a></li>
<li><a href="https://grokipedia.com/page/SnapKV">SnapKV</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#KV cache compression`, `#long-context`, `#training-free`, `#efficiency`

---

<a id="item-23"></a>
## [SkillCorpus: Unifying 96K Open-Source Agent Skills](https://arxiv.org/abs/2607.15557) ⭐️ 8.0/10

SkillCorpus aggregates, curates, and evaluates over 96,000 open-source SKILL.md files into a structured taxonomy and retrieval system, achieving consistent performance gains on real-world LLM agent benchmarks. This is the first end-to-end framework that consolidates the fragmented open skill ecosystem and quantifies its benefits for LLM agents, addressing a critical gap in agent capability extension and retrieval. The pipeline filters ~821,000 crawled skills down to 96,401, organized by a 16-class taxonomy and three quality facets (utility, robustness, safety), paired with a fine-tuned retrieval-and-selection stack. Gains are largest on SkillsBench (+7.5 pp), with an operational analysis revealing coverage and harness boundaries.

rss · arXiv - NLP · Jul 20, 04:00

**Background**: Agent skills are SKILL.md files that package reusable procedural knowledge for LLM agents, allowing on-demand loading of specialized capabilities. Public repositories host many such skills, but they are fragmented, redundant, and uneven in quality, making consolidation and evaluation challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15557">[2607.15557] SkillCorpus: Consolidating and Evaluating the ...</a></li>
<li><a href="https://arxiv.org/html/2607.15557v1">SkillCorpus: Consolidating and Evaluating the Open Skill ...</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/how-to-implement-agent-skills">How to Write and Implement Agent Skills | DigitalOcean</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#skill ecosystem`, `#retrieval`, `#taxonomy`, `#open-source`

---

<a id="item-24"></a>
## [PATR: Process-Guided Tree Rollout for Multi-Turn RL](https://arxiv.org/abs/2607.15610) ⭐️ 8.0/10

Researchers propose PATR, a quality-aware rollout framework that uses process feedback to selectively branch from promising states in multi-turn reinforcement learning for LLM agents, reducing wasted computation on dead-end trajectories. This method improves training efficiency and performance on long-horizon agentic tasks, achieving up to +5.0 points on SWE-Bench and +9.3 points on FrozenLake, which could accelerate the development of more capable LLM agents. PATR uses a process scorer to evaluate partial trajectories, reuses shared prefixes, and conservatively stops degenerate paths, remaining compatible with standard policy optimization methods like GRPO and RLOO.

rss · arXiv - NLP · Jul 20, 04:00

**Background**: Current multi-turn RL methods for LLM agents, such as GRPO and RLOO, rely on independent complete trajectory sampling, which wastes budget on uninformative dead-ends. Process reward models provide step-level feedback, enabling more efficient exploration by focusing on promising intermediate states.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15610">Process Reward Informed Tree Rollout for Effective Multi - Turn RL</a></li>
<li><a href="https://arxiv.org/html/2607.15610">Process Reward Informed Tree Rollout for Effective Multi - Turn RL</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#LLM agents`, `#multi-turn RL`, `#process reward`, `#tree rollout`

---

<a id="item-25"></a>
## [Benchmarking LLMs on Prospective Hypothesis Discovery](https://arxiv.org/abs/2607.15766) ⭐️ 8.0/10

The paper introduces Prospective Hypothesis Discovery (PHD) and HypoArena, a benchmark with 988 cases across six scientific domains, to evaluate LLMs' ability to autonomously construct hypothesis spaces from inconclusive evidence. This work addresses an underexplored aspect of scientific discovery—the pre-conclusion stage—and provides a standardized evaluation framework that could guide future AI-assisted research. HypoArena includes HypoData (988 cases) and HypoEval, which combines bidirectional pairwise judgments with Bradley–Terry–Davidson aggregation and six-dimensional rubric scoring. Experiments on 15 frontier LLMs show capability stratification and model-dependent effects.

rss · arXiv - NLP · Jul 20, 04:00

**Background**: LLMs typically excel at answering specific questions but struggle with open-ended tasks like generating hypotheses from incomplete data. Prospective Hypothesis Discovery (PHD) focuses on the pre-conclusion stage of scientific inquiry, where researchers must formulate testable hypotheses from anomalous observations or fragmented records. The Retrospective Context Regression pipeline reconstructs pre-conclusion contexts from completed expert documents by removing explicit conclusions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15766">[2607.15766] Before the Action: Benchmarking LLMs on ...</a></li>
<li><a href="https://huggingface.co/datasets/HypoArena/HypoData">HypoArena/HypoData · Datasets at Hugging Face</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmark`, `#scientific discovery`, `#hypothesis generation`, `#AI evaluation`

---

<a id="item-26"></a>
## [RL Boosts Part-Level Visual Grounding in MLLMs](https://arxiv.org/abs/2607.15374) ⭐️ 8.0/10

Researchers propose Object-Part Hierarchical Reflective Grounding (OP-HRG), a coarse-to-fine reasoning strategy that first localizes the parent object then the part, trained with a part-aware GRPO reinforcement learning framework. A 4B model using this approach outperforms 7B grounding LLMs and SAM3 on PascalPart, PartImageNet, and InstructPart. This work addresses a critical limitation of multimodal LLMs: their inability to accurately ground parts from language queries. By achieving state-of-the-art results with a smaller model, it demonstrates that reinforcement learning and hierarchical reasoning can significantly improve fine-grained visual understanding, with potential applications in robotics, medical imaging, and augmented reality. OP-HRG includes a self-check step that reflects on the result and can re-encode the predicted crop for correction. The part-aware GRPO framework uses stage-wise rewards to train the pipeline, enabling a 4B model to surpass larger models and even SAM3 on part-level segmentation tasks.

rss · arXiv - Computer Vision · Jul 20, 04:00

**Background**: Multimodal large language models (MLLMs) can ground whole objects from free-form text, but they struggle with part-level queries because they lack an object-part hierarchy and treat parts like objects in a single step. Visual grounding is the task of localizing an image region described by a natural language phrase. Reinforcement learning from group relative policy optimization (GRPO) is a technique that optimizes policy using group-based rewards.

<details><summary>References</summary>
<ul>
<li><a href="https://aissential.tech/articles/0a7c5be1-03d5-4561-805a-2babb7d6106a">Reasoning-Guided Part-Level Visual Grounding via ...</a></li>

</ul>
</details>

**Tags**: `#multimodal LLM`, `#visual grounding`, `#reinforcement learning`, `#object-part hierarchy`, `#computer vision`

---

<a id="item-27"></a>
## [Stable Signal Principle Explains Retraining Dynamics](https://arxiv.org/abs/2607.15623) ⭐️ 8.0/10

A new paper introduces the 'stable signal principle' to explain when and why retraining in performative prediction converges to fixed points, even under strong model influence. This work addresses a key open problem in performative prediction, providing theoretical guarantees for retraining stability that could impact real-world machine learning systems subject to feedback loops. The paper proves that with a nonzero stable signal, repeated risk minimization with suitable regularization converges geometrically to the stable signal direction, regardless of model influence strength.

rss · arXiv - Data Science & Statistics · Jul 20, 04:00

**Background**: Performative prediction occurs when a model's predictions influence the data it aims to predict, creating feedback loops. Retraining, or repeated risk minimization, is a common strategy to adapt to such shifts, but its convergence under strong model influence was not well understood. The stable signal principle posits that a model-independent component in the target ensures retraining converges.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2002.06673">[2002.06673] Performative Prediction</a></li>
<li><a href="https://proceedings.mlr.press/v119/perdomo20a.html">Performative Prediction</a></li>
<li><a href="https://arxiv.org/abs/2310.16608">[2310.16608] Performative Prediction: Past and Future</a></li>

</ul>
</details>

**Tags**: `#performative prediction`, `#retraining`, `#machine learning theory`, `#feedback loops`

---

<a id="item-28"></a>
## [Prediction-Only Self-Distillation Outperforms Teacher in Regression](https://arxiv.org/abs/2607.15450) ⭐️ 8.0/10

A new theoretical analysis shows that in self-distillation without original labeled data, a mixed predictor combining teacher and student predictions can achieve strictly lower risk than the teacher alone for ridge regression under proportional asymptotics. This work addresses a critical gap in knowledge distillation literature by proving that prediction-only self-distillation can improve performance even when labeled data is unavailable, which is common in deployment scenarios. The optimal mixing weight cannot be identified from unlabeled data alone, but can be consistently estimated using a small labeled calibration set in a single post-training step. The results extend to binary logistic regression as well.

rss · arXiv - Data Science & Statistics · Jul 20, 04:00

**Background**: Self-distillation is a technique where a model is retrained using its own predictions. In the prediction-only regime, the original training data is no longer available, and only the trained predictor and fresh unlabeled covariates are accessible. This paper studies a fresh-X prediction-mixed scheme where a student is trained on teacher-pseudo-labeled fresh covariates, and the final predictor is an affine combination of teacher and student predictions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15450">[2607.15450] Prediction-Only Distillation in Linear and Logistic Regression</a></li>
<li><a href="https://www.emergentmind.com/topics/self-distillation-mechanism">Self - Distillation Mechanism</a></li>
<li><a href="https://proceedings.neurips.cc/paper/2020/file/2288f691b58edecadcc9a8691762b4fd-Paper.pdf">Self - Distillation Ampli es Regularization</a></li>

</ul>
</details>

**Tags**: `#self-distillation`, `#ridge regression`, `#theoretical analysis`, `#machine learning`, `#knowledge distillation`

---

<a id="item-29"></a>
## [Diffusion models recover accurate mixture weights despite score insensitivity](https://arxiv.org/abs/2607.15485) ⭐️ 8.0/10

A new paper resolves the paradox that diffusion models can accurately recover mixture weights even when the score function is insensitive to them, introducing the Diffusion Score Sensitivity Index (DSSI) to quantify parameter estimation accuracy. This work provides a theoretical foundation for understanding mode coverage and weight estimation in score-based generative models, which is critical for applications like image generation and scientific data modeling where correct relative frequencies matter. The DSSI measures the variation in the diffusion score matching (DSM) loss with respect to parameter changes, and the authors prove that for Gaussian mixtures, mixture weight estimation errors are on the same order as the DSM loss under mild conditions.

rss · arXiv - Data Science & Statistics · Jul 20, 04:00

**Background**: Diffusion models generate data by reversing a noising process, learning the score function (gradient of log-density) to guide generation. A known issue is that they sometimes fail to capture correct mode amplitudes (mixture weights) in multimodal distributions, even when all modes appear. This paper explains why accurate weight recovery is still possible through intermediate noise levels.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15485">[2607.15485] Diffusion models recover accurate mixture weights despite score function insensitivity</a></li>
<li><a href="https://arxiv.org/html/2607.15485">Diffusion models recover accurate mixture weights despite score function insensitivity</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#score-based generative models`, `#mixture weights`, `#theoretical analysis`, `#machine learning`

---

<a id="item-30"></a>
## [BIHT Convergence Without Normalization Proved Optimal](https://arxiv.org/abs/2607.15530) ⭐️ 8.0/10

This paper proves a universal, sample-optimal convergence theorem for the original Binary Iterative Hard Thresholding (BIHT) algorithm without per-iteration normalization, resolving a decade-old open problem in 1-bit compressed sensing. This result shows that per-iteration normalization is unnecessary for optimal recovery in the noiseless setting, simplifying the algorithm and deepening theoretical understanding of sparse recovery from 1-bit measurements. The theorem requires O(s/ε) measurements for an s-sparse unit vector to achieve directional error at most ε, matching the optimal sample complexity of normalized BIHT. Under sign corruptions, the paper proves a sharp separation: BIHT without normalization reaches a robust error floor but cannot achieve last-iterate convergence, while normalized BIHT can.

rss · arXiv - Data Science & Statistics · Jul 20, 04:00

**Background**: 1-bit compressed sensing recovers a sparse signal from only the signs of linear measurements, which is efficient for hardware with severe quantization. Binary Iterative Hard Thresholding (BIHT) is a popular greedy algorithm that alternates between a gradient-like step and hard thresholding. Prior analyses required normalizing each iterate to the unit sphere to prove convergence, leaving the original algorithm's behavior unresolved.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15530">[2607.15530] On the Role of Normalization in Binary Iterative Hard Thresholding for 1-bit Compressed Sensing</a></li>
<li><a href="https://arxiv.org/abs/2207.03427">[2207.03427] Binary Iterative Hard Thresholding Converges with Optimal Number of Measurements for 1-Bit Compressed Sensing</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3680542">Binary Iterative Hard Thresholding Converges with Optimal Number of Measurements for 1-Bit Compressed Sensing | Journal of the ACM</a></li>

</ul>
</details>

**Tags**: `#compressed sensing`, `#sparse recovery`, `#iterative hard thresholding`, `#1-bit measurements`, `#signal processing`

---

<a id="item-31"></a>
## [New Protocol Evaluates Temporal Fidelity in Synthetic Data](https://arxiv.org/abs/2607.15606) ⭐️ 8.0/10

Researchers propose a taxonomy-guided evaluation protocol for temporal fidelity in synthetic sequential tabular data, revealing that conventional static evaluations miss critical failures like backward timestamps or impossible trajectories. This work addresses a critical gap in generative model evaluation, ensuring synthetic data used for privacy-preserving sharing in healthcare, finance, and other domains maintains realistic temporal dynamics, which is essential for downstream reliability. The protocol characterizes datasets along four properties (time representation, sampling regularity, trajectory dependence, schema linking) and measures timestamp validity, cross-sectional structure, within-entity dynamics, and time-varying relational structure across eight generative models and thirteen datasets.

rss · arXiv - Data Science & Statistics · Jul 20, 04:00

**Background**: Synthetic sequential tabular data, such as patient records or financial transactions, are generated to preserve privacy while enabling data sharing. Conventional evaluation methods pool records into static distributions, ignoring temporal order and dependencies, which can mask severe temporal inconsistencies. This paper introduces a taxonomy to classify datasets and then applies targeted temporal metrics.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.10643v1">Evaluation metrics for temporal preservation in synthetic longitudinal...</a></li>
<li><a href="https://www.computer.org/csdl/proceedings-article/cai/2024/540900a541/1Z06CMwY19K">Evaluating Temporal Fidelity in Synthetic Time-series Electronic...</a></li>
<li><a href="https://arxiv.org/pdf/2408.10548">Language Modeling on Tabular Data : A Survey of</a></li>

</ul>
</details>

**Tags**: `#synthetic data`, `#temporal fidelity`, `#tabular data`, `#generative models`, `#evaluation`

---

<a id="item-32"></a>
## [AI develops its own hiring biases beyond training data](https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/) ⭐️ 8.0/10

New research reveals that large language models (LLMs) used in hiring can develop their own biases from experience, stereotyping job applicants more than humans do. This challenges the assumption that AI bias only stems from training data, raising urgent fairness concerns as AI agents with memory become more common in hiring. The research specifically examines LLMs that can remember user interactions, showing they may amplify biases over time beyond what was present in their original training data.

rss · MIT Technology Review · Jul 20, 08:39

**Background**: AI hiring tools are increasingly used to screen résumés before human review. Previous work focused on biases inherited from training data, but this study shows LLMs can also learn new biases from their own interactions, a phenomenon less understood.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/20/1140655/ai-biases-hiring-humans/">AI is more likely than humans to form biases when hiring | MIT Technology Review</a></li>
<li><a href="https://arxiv.org/html/2507.02087v1">Evaluating the Promise and Pitfalls of LLMs in Hiring Decisions</a></li>
<li><a href="https://www.nist.gov/news-events/news/2022/03/theres-more-ai-bias-biased-data-nist-report-highlights">There’s More to AI Bias Than Biased Data, NIST Report ...</a></li>

</ul>
</details>

**Tags**: `#AI bias`, `#LLMs`, `#hiring`, `#fairness`, `#research`

---

<a id="item-33"></a>
## [Alzheimer's sleep loss linked to microglia, not plaques](https://www.sciencedaily.com/releases/2026/07/260719035931.htm) ⭐️ 8.0/10

Researchers discovered that overactive microglia cause sleep loss in Alzheimer's mice by triggering inflammation, and temporarily removing these cells restored over two hours of sleep per day without clearing amyloid plaques. This finding challenges the prevailing focus on amyloid plaques as the primary driver of Alzheimer's symptoms, highlighting neuroinflammation as a key therapeutic target for sleep disruption and potentially other non-cognitive symptoms. The study used mice with amyloid plaques and temporarily depleted microglia using a CSF1R inhibitor, which restored deep sleep. The effect was independent of plaque burden, suggesting microglia-driven inflammation directly impairs sleep regulation.

rss · ScienceDaily Health · Jul 20, 10:05

**Background**: Microglia are the brain's resident immune cells, making up about 10% of all brain cells. In Alzheimer's disease, amyloid plaques accumulate between neurons, but their role in symptoms like sleep loss is debated. This study provides a new mechanism linking microglial overactivation to sleep disruption.

<details><summary>References</summary>
<ul>
<li><a href="https://sitn.hms.harvard.edu/flash/2022/microglia-the-protectors-of-the-brain/">Microglia : The protectors of the brain - Science in the News</a></li>
<li><a href="https://www.nia.nih.gov/news/amyloid-structure-linked-different-types-alzheimers-disease">Amyloid structure linked to different types of Alzheimer’s disease | National Institute on Aging</a></li>

</ul>
</details>

**Tags**: `#Alzheimer's`, `#microglia`, `#sleep`, `#neuroinflammation`, `#neuroscience`

---

<a id="item-34"></a>
## [SORLA Protein Shields Brain from Alzheimer's Tau Tangles](https://www.sciencedaily.com/releases/2026/07/260718010140.htm) ⭐️ 8.0/10

Researchers discovered that the SORLA protein protects against tau tangles in Alzheimer's disease, with mice engineered to produce extra SORLA showing less tau accumulation, brain atrophy, and neuronal damage. This finding identifies a novel protective mechanism against Alzheimer's pathology and suggests SORLA as a potential drug target, which could lead to new treatments for the disease affecting millions worldwide. The study, published in ScienceDaily, used mouse models to show that SORLA reduces tau aggregation and maintains healthy neuronal connections; the protein is already known to bind amyloid precursor protein (APP) and regulate its trafficking.

rss · ScienceDaily Health · Jul 20, 05:28

**Background**: Alzheimer's disease is characterized by two hallmark brain abnormalities: amyloid plaques and tau tangles. Tau tangles are abnormal accumulations of tau protein inside neurons that disrupt cell function and lead to neurodegeneration. SORLA (also known as SORL1) is a transmembrane receptor involved in intracellular sorting of proteins like APP, and its genetic variants have been linked to increased Alzheimer's risk.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SORL1">SORL1 - Wikipedia</a></li>
<li><a href="https://www.alzforum.org/alzpedia/sorla-sorl1">SORLA (SORL1) - ALZFORUM</a></li>
<li><a href="https://www.nia.nih.gov/health/alzheimers-causes-and-risk-factors/what-happens-brain-alzheimers-disease">What Happens to the Brain in Alzheimer ' s Disease? | National Institute...</a></li>

</ul>
</details>

**Tags**: `#Alzheimer's`, `#neuroscience`, `#protein research`, `#drug discovery`

---