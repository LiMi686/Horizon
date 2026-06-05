---
layout: default
title: "Horizon Summary: 2026-06-05 (EN)"
date: 2026-06-05
lang: en
---

> From 105 items, 36 important content pieces were selected

---

1. [NVIDIA Launches Cosmos Open Platform for Physical AI](#item-1) ⭐️ 9.0/10
2. [Microsoft Open Sources pg_durable for PostgreSQL Durable Execution](#item-2) ⭐️ 8.0/10
3. [Google Releases Gemma 4 QAT Models for Efficient On-Device AI](#item-3) ⭐️ 8.0/10
4. [Claude-Generated Code May Have Introduced Bugs in rsync](#item-4) ⭐️ 8.0/10
5. [IP KVM Shootout: PiKVM V4 Plus Tops Homelab Test](#item-5) ⭐️ 8.0/10
6. [Russian Satellite Cosmos 2546 Linked to GNSS Interference](#item-6) ⭐️ 8.0/10
7. [Ladybird Browser Bans Public PRs Due to AI Code Concerns](#item-7) ⭐️ 8.0/10
8. [AI Enthusiasts vs. Skeptics: Race Against Time or Entropy](#item-8) ⭐️ 8.0/10
9. [Coding Interview University: A Comprehensive CS Study Plan](#item-9) ⭐️ 8.0/10
10. [GitHub Releases Official Multi-Platform Copilot SDK](#item-10) ⭐️ 8.0/10
11. [Trivy: Comprehensive Open Source Security Scanner](#item-11) ⭐️ 8.0/10
12. [Ontology-Grounded Framework for AI Agent Pre-Deployment Assurance](#item-12) ⭐️ 8.0/10
13. [AI Emotional Dependence Arises Incidental to Task Interactions](#item-13) ⭐️ 8.0/10
14. [PEEL Framework Detects LLM Distortions in Research](#item-14) ⭐️ 8.0/10
15. [Curation-Bench: Can AI Agents Automate Data Curation?](#item-15) ⭐️ 8.0/10
16. [Study Reveals How Mathematicians Use AI for Proof Formalization](#item-16) ⭐️ 8.0/10
17. [Intervention Timing Fails for Autonomous Agents](#item-17) ⭐️ 8.0/10
18. [Stereological Theory Reveals Massive Blind Spots in LLM Benchmarks](#item-18) ⭐️ 8.0/10
19. [Errorquake-10k: New Benchmark for LLM Error Severity](#item-19) ⭐️ 8.0/10
20. [Mechanistic Interpretability of Temporal Preferences in LLMs](#item-20) ⭐️ 8.0/10
21. [State Commitment Learning Improves LM Reasoning Reliability](#item-21) ⭐️ 8.0/10
22. [Large-Step GD Restores Symmetry in Deep Linear Networks](#item-22) ⭐️ 8.0/10
23. [Differentiable Framework Automates Token Reduction Search](#item-23) ⭐️ 8.0/10
24. [Alpha-RTL: Test-Time Training for RTL Hardware Optimization](#item-24) ⭐️ 8.0/10
25. [Epidemiological Model Analyzes AI Model Collapse from Synthetic Data](#item-25) ⭐️ 8.0/10
26. [MCBench: New Benchmark for Omni LLM Safety](#item-26) ⭐️ 8.0/10
27. [LANTERN: Zero-LLM-Call Memory Layer Recovers 78.3% Lost Facts](#item-27) ⭐️ 8.0/10
28. [VideoKR: New Benchmark for Knowledge-Intensive Video Understanding](#item-28) ⭐️ 8.0/10
29. [Cross-Model Safety Steering for Generative Models](#item-29) ⭐️ 8.0/10
30. [RePHO: Physics-Guided Human-Object Interaction Reconstruction](#item-30) ⭐️ 8.0/10
31. [Biomazon: Multimodal Benchmark for Amazon Forest Structure](#item-31) ⭐️ 8.0/10
32. [Tri-SfSVD: Sparse Functional SVD for Biclustering and Triclustering](#item-32) ⭐️ 8.0/10
33. [Action-Conditional Conformal Prediction for Risk-Averse Decisions](#item-33) ⭐️ 8.0/10
34. [Efficient Algorithm for Finding Most Influential Sets](#item-34) ⭐️ 8.0/10
35. [Meta AI hack exposes new AI security risks beyond Mythos](#item-35) ⭐️ 8.0/10
36. [World's first AI-designed vaccine tested in humans](#item-36) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NVIDIA Launches Cosmos Open Platform for Physical AI](https://github.com/NVIDIA/cosmos) ⭐️ 9.0/10

NVIDIA has released Cosmos, an open platform of world models, datasets, and tools for building Physical AI in robotics, autonomous vehicles, and smart infrastructure. This platform democratizes access to advanced world models, enabling developers to accelerate the development of autonomous systems that can perceive and act in the real world. Cosmos includes generative world foundation models (WFMs), tokenizers, guardrails, and an accelerated data pipeline, with support for integrations like Diffusers and vLLM-Omni.

rss · GitHub Trending - Daily (All) · Jun 5, 23:01

**Background**: World models are AI systems that learn an internal representation of the physical world, enabling them to predict outcomes and plan actions. Physical AI refers to AI that operates in real-world environments through sensors and actuators, as seen in robots and autonomous vehicles.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nvidia.com/en-us/ai/cosmos/">Physical AI with World Foundation Models | NVIDIA Cosmos</a></li>
<li><a href="https://github.com/nvidia-cosmos">NVIDIA Cosmos - GitHub</a></li>
<li><a href="https://arxiv.org/abs/2501.03575">[2501.03575] Cosmos World Foundation Model Platform for ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Physical AI`, `#world models`, `#robotics`, `#autonomous vehicles`

---

<a id="item-2"></a>
## [Microsoft Open Sources pg_durable for PostgreSQL Durable Execution](https://github.com/microsoft/pg_durable) ⭐️ 8.0/10

Microsoft has open-sourced pg_durable, a PostgreSQL extension that enables in-database durable execution for workflow orchestration, built with pgrx and Rust libraries duroxide. This brings durable execution directly into PostgreSQL, reducing reliance on external services like Temporal and simplifying workflow reliability for Postgres users. pg_durable runs entirely inside the PostgreSQL server as a background worker, exposing a SQL DSL for defining function graphs and ensuring deterministic replay after failures.

hackernews · coffeemug · Jun 5, 15:59 · [Discussion](https://news.ycombinator.com/item?id=48414367)

**Background**: Durable execution is a programming paradigm that automatically persists workflow progress to survive crashes and restarts. Traditionally, this requires external platforms like Temporal or Azure Durable Functions. pg_durable embeds this capability directly into PostgreSQL, allowing workflows to be defined and executed within the database itself.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/pg_durable">GitHub - microsoft/pg_durable</a></li>
<li><a href="https://news.ycombinator.com/item?id=48414367">pg_durable: Microsoft open sources in-database durable ...</a></li>
<li><a href="https://dev.to/franckpachot/getting-started-with-pgdurable-durable-workflows-inside-postgresql-3980">Getting Started with pg_durable: Durable Workflows Inside ...</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion shows strong interest, with comparisons to Temporal and other queue solutions. Some users question the limitation when workflows span heterogeneous systems, while others appreciate the in-database approach but prefer queue logic in code for version control.

**Tags**: `#PostgreSQL`, `#durable execution`, `#open source`, `#workflow orchestration`, `#Microsoft`

---

<a id="item-3"></a>
## [Google Releases Gemma 4 QAT Models for Efficient On-Device AI](https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/) ⭐️ 8.0/10

Google has released Gemma 4 models with quantization-aware training (QAT), enabling near-lossless compression for on-device inference on mobile and laptop hardware. This release makes powerful AI models practical for consumer devices, reducing memory and compute requirements while maintaining high accuracy, which could accelerate on-device AI adoption. The QAT models include checkpoints for the popular Q4_0 format and a novel mobile-specific quantization format, with the 12B Q4_0 model requiring only 6.7GB VRAM, fitting comfortably within 16GB.

hackernews · theanonymousone · Jun 5, 16:18 · [Discussion](https://news.ycombinator.com/item?id=48414653)

**Background**: Quantization-aware training (QAT) simulates quantization during training to minimize quality loss when the model is later compressed, unlike post-training quantization (PTQ) which can degrade performance. This technique is crucial for deploying large language models on resource-constrained devices like phones and laptops.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/quantization-aware-training-gemma-4/">Gemma 4 with quantization-aware training</a></li>
<li><a href="https://unsloth.ai/docs/models/gemma-4/qat">Gemma 4 QAT | Unsloth Documentation</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview | Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: The community is impressed with the Gemma ecosystem's rapid advancement, with users reporting successful local runs on Mac and noting that third-party quants (e.g., from Unsloth) can achieve near-100% accuracy compared to the unquantized BF16 model. Some commenters observed that the timing coincides with Apple's WWDC, suggesting strategic positioning.

**Tags**: `#quantization`, `#Gemma`, `#on-device AI`, `#model compression`, `#efficiency`

---

<a id="item-4"></a>
## [Claude-Generated Code May Have Introduced Bugs in rsync](https://alexispurslane.github.io/rsync-analysis/) ⭐️ 8.0/10

An analysis of rsync commits suggests that code written with Claude may have introduced bugs, particularly by forcing calloc over malloc in a way that degrades performance and correctness. The analysis points to a specific commit that unconditionally replaced malloc with calloc, which was later reverted. This case highlights the risks of blindly trusting LLM-generated code, especially in critical system utilities like rsync. It sparks debate on how to responsibly integrate AI assistance into software engineering without compromising code quality. The analysis uses a custom methodology to attribute bugs to commits, but critics note it does not control for commit complexity, security intensity, or bug severity. Only two Claude-coauthored commits were identified, raising questions about statistical significance.

hackernews · logicprog · Jun 5, 12:43 · [Discussion](https://news.ycombinator.com/item?id=48411635)

**Background**: rsync is a widely used file synchronization tool written in C. The functions malloc and calloc both allocate memory, but calloc also zero-initializes it, which can be slower for large allocations. Unconditionally replacing malloc with calloc can introduce performance regressions and hide bugs by masking uninitialized memory issues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/C_dynamic_memory_allocation">C dynamic memory allocation - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2505.16339v1">Rethinking Code Review Workflows with LLM Assistance: An Empirical Study</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed views: some criticize the analysis methodology as too blunt, while others worry that pressuring maintainers will discourage responsible AI disclosure. There is also debate over whether the small number of Claude commits makes the findings statistically meaningful.

**Tags**: `#LLM`, `#code quality`, `#rsync`, `#software engineering`, `#AI safety`

---

<a id="item-5"></a>
## [IP KVM Shootout: PiKVM V4 Plus Tops Homelab Test](https://www.jeffgeerling.com/blog/2026/i-tested-every-ip-kvm/) ⭐️ 8.0/10

Jeff Geerling published a comprehensive comparison of IP KVM devices for homelab use, testing PiKVM V4 Plus, JetKVM, GL.iNet KVM, and others, with PiKVM V4 Plus emerging as the top performer. This comparison provides valuable guidance for sysadmins and homelab enthusiasts choosing remote management hardware, highlighting trade-offs between open-source flexibility, cost, and features like HDMI and PoE support. The PiKVM V4 Plus is based on Raspberry Pi and offers full BIOS-level control, while JetKVM has a hardware revision that fixes earlier HDMI and PoE issues but is hard to distinguish from the old version. Intel vPro AMT provides a built-in KVM in compatible CPUs without extra hardware.

hackernews · vquemener · Jun 5, 14:30 · [Discussion](https://news.ycombinator.com/item?id=48413072)

**Background**: An IP KVM (Keyboard, Video, Mouse over IP) allows remote control of a computer's BIOS and OS as if physically present. PiKVM is an open-source KVM over IP solution using a Raspberry Pi, while Intel vPro AMT is a firmware-based remote management technology built into certain Intel CPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IPKVM">IPKVM</a></li>
<li><a href="https://pikvm.org/">KVM over IP - PiKVM</a></li>
<li><a href="https://jetkvm.com/">JetKVM - Control any computer remotely</a></li>

</ul>
</details>

**Discussion**: Commenters shared specific use cases, such as a YC company using PiKVM for AI-driven BIOS navigation, and noted that JetKVM's hardware revision fixes earlier issues but is hard to identify. Intel vPro AMT was mentioned as a built-in alternative, though it requires compatible hardware.

**Tags**: `#IP KVM`, `#homelab`, `#hardware`, `#remote management`, `#PiKVM`

---

<a id="item-6"></a>
## [Russian Satellite Cosmos 2546 Linked to GNSS Interference](https://arxiv.org/abs/2606.03673) ⭐️ 8.0/10

A research paper identifies Russian satellite Cosmos 2546 (NORAD ID 45608) as a source of GNSS interference across Europe since 2019, using a combination of techniques to pinpoint the satellite with high confidence. This finding has significant implications for aviation and maritime safety, as GNSS interference can disrupt navigation systems. It also highlights potential geopolitical tensions, with community discussions linking the interference to recent drone incidents in the Black Sea region. The satellite belongs to Russia's Edinaya Kosmicheskaya Sistema (EKS), an early warning constellation, which the paper suggests is collectively responsible for wide-area transient GNSS degradation. The interference has been observed since 2019, affecting regions including Romania and Poland.

hackernews · mimorigasaka · Jun 5, 08:32 · [Discussion](https://news.ycombinator.com/item?id=48409664)

**Background**: GNSS (Global Navigation Satellite System) includes constellations like GPS, GLONASS, and Galileo, providing positioning, navigation, and timing services. Interference can be either jamming (overpowering signals with noise) or spoofing (broadcasting fake signals). The EKS constellation is designed for missile warning but its signals can inadvertently or deliberately disrupt GNSS frequencies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.n2yo.com/satellite/?s=45608">COSMOS 2546 Satellite details 2020-031A NORAD 45608</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Kosmos_satellites_(2501–2750)">List of Kosmos satellites (2501–2750) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments express interest in the technical identification of the satellite and discuss real-world impacts, such as daily jamming experienced by construction projects near Ukraine. Some users link the interference to recent Ukrainian drone incidents near Romania, suggesting Russian electronic warfare may have caused loss of control.

**Tags**: `#GNSS`, `#interference`, `#satellite`, `#geopolitics`, `#research`

---

<a id="item-7"></a>
## [Ladybird Browser Bans Public PRs Due to AI Code Concerns](https://simonwillison.net/2026/Jun/5/andreas-kling/#atom-everything) ⭐️ 8.0/10

Ladybird browser announced it will no longer accept public pull requests, citing that AI-generated code undermines the assumption of good faith and responsibility for changes. This policy shift highlights growing tensions in open-source governance as AI-generated code becomes prevalent, forcing projects to rethink trust and accountability models. Andreas Kling stated that the effort once implied by a substantial patch is no longer a reliable proxy for good faith, and that responsibility for code entering the browser must rest with the introducer.

rss · Simon Willison · Jun 5, 11:10

**Background**: Ladybird is an open-source, privacy-focused web browser developed by the Ladybird Browser Initiative, a nonprofit funded by donations from companies like Cloudflare and Shopify. It originated as part of SerenityOS and is now a standalone project with alpha release planned for 2026. The decision reflects broader debates in the open-source community about how to handle AI-generated contributions, which raise issues of licensing, security, and accountability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_(web_browser)">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://www.redhat.com/en/blog/when-bots-commit-ai-generated-code-open-source-projects">When bots commit: AI-generated code in open source projects</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#ai-ethics`, `#ladybird`, `#software-governance`

---

<a id="item-8"></a>
## [AI Enthusiasts vs. Skeptics: Race Against Time or Entropy](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything) ⭐️ 8.0/10

Charity Majors articulates the opposing pressures on AI enthusiasts and skeptics in software teams, highlighting both the urgency of adoption and the risks of technical debt. This insight captures a nuanced, widely-discussed tension in AI adoption, with clear relevance to software engineering teams facing existential threats from both competition and system degradation. Majors recommends treating this as both a leadership and engineering challenge, and notes that there is no natural feedback loop connecting enthusiasts with skeptics, making it a fascinating organizational design problem.

rss · Simon Willison · Jun 4, 23:55

**Background**: Technical debt refers to the cost of maintaining a system due to expedient short-term solutions, while software entropy describes the degradation of software over time without deliberate intervention. Both concepts are central to the tension between rapid AI adoption and maintaining system reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Software_rot">Software rot - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software engineering`, `#technology adoption`, `#risk management`

---

<a id="item-9"></a>
## [Coding Interview University: A Comprehensive CS Study Plan](https://github.com/jwasham/coding-interview-university) ⭐️ 8.0/10

John Washam's Coding Interview University repository on GitHub provides a detailed, self-paced study plan covering computer science fundamentals for software engineering interviews, with the author having successfully landed a job at Amazon after following it. This resource democratizes access to structured interview preparation, helping aspiring software engineers systematically learn key topics. Its proven success story and high community engagement make it a trusted guide for job seekers targeting top tech companies. The plan recommends studying 8-12 hours per day for several months, but the author notes that most people won't need to study as much. It includes translations in over 15 languages and covers topics like data structures, algorithms, system design, and more.

rss · GitHub Trending - Daily (All) · Jun 5, 23:01

**Background**: Technical interviews at major tech companies often test candidates on computer science fundamentals beyond typical coding bootcamp curricula. Many self-taught developers lack a formal CS background, making structured resources like this valuable. The repository has gained over 300,000 stars on GitHub, reflecting its widespread adoption.

**Tags**: `#interview preparation`, `#computer science`, `#study plan`, `#software engineering`

---

<a id="item-10"></a>
## [GitHub Releases Official Multi-Platform Copilot SDK](https://github.com/github/copilot-sdk) ⭐️ 8.0/10

GitHub has released the official Copilot SDK, providing multi-platform libraries (npm, PyPI, NuGet, Go, Rust, Java) that expose the same agent runtime used by Copilot CLI, allowing developers to embed Copilot's agentic workflows into their own applications. This SDK enables developers to integrate GitHub Copilot's planning, tool invocation, and file editing capabilities into any application, significantly lowering the barrier to building AI-powered developer tools and workflows. The SDK supports six languages: Node.js/TypeScript, Python, Go, .NET, Rust, and Java, with each package available on its respective package manager. It provides a production-tested agent runtime that handles orchestration, so developers only need to define agent behavior.

rss · GitHub Trending - Daily (All) · Jun 5, 23:01

**Background**: GitHub Copilot is an AI-powered code completion tool that has evolved to include agentic capabilities, allowing it to plan and execute multi-step tasks. The Copilot CLI is a command-line interface that exposes these agentic workflows. The new SDK packages this same engine into libraries for popular programming languages, making it accessible for custom integrations.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for ...</a></li>
<li><a href="https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/">Build an agent into any app with the GitHub Copilot SDK</a></li>
<li><a href="https://github.com/features/copilot/agents">GitHub Copilot · Agents on GitHub</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`

---

<a id="item-11"></a>
## [Trivy: Comprehensive Open Source Security Scanner](https://github.com/aquasecurity/trivy) ⭐️ 8.0/10

Trivy is an open-source security scanner that detects vulnerabilities, misconfigurations, secrets, and SBOMs across containers, Kubernetes, code repositories, and cloud environments. It has gained significant community adoption and is trending on GitHub. Trivy provides a unified scanning solution for multiple targets and scanners, simplifying security workflows for DevOps and security teams. Its broad coverage and integrations make it a key tool for software supply chain security. Trivy supports scanning container images, filesystems, Git repositories, virtual machine images, and Kubernetes. It can find OS packages, software dependencies (SBOM), known vulnerabilities (CVEs), IaC misconfigurations, secrets, and software licenses.

rss · GitHub Trending - Daily (All) · Jun 5, 23:01

**Background**: A software bill of materials (SBOM) is a nested inventory of components used to build a software artifact, crucial for supply chain security. Trivy is developed by Aqua Security and is one of the most popular open-source vulnerability scanners, with integrations like GitHub Actions and a Kubernetes operator.

<details><summary>References</summary>
<ul>
<li><a href="https://trivy.dev/">Trivy</a></li>
<li><a href="https://www.aquasec.com/products/trivy/">Trivy Open Source Vulnerability Scanner | Aqua</a></li>
<li><a href="https://en.wikipedia.org/wiki/SBOM">SBOM</a></li>

</ul>
</details>

**Tags**: `#security`, `#container`, `#kubernetes`, `#vulnerability-scanning`, `#open-source`

---

<a id="item-12"></a>
## [Ontology-Grounded Framework for AI Agent Pre-Deployment Assurance](https://arxiv.org/abs/2606.04037) ⭐️ 8.0/10

A new ontology-grounded verification framework for enterprise AI agents is proposed, combining an Agent Operational Envelope, automated scenario generation, and machine-verifiable Trust Certificates. A pilot across four regulated industries generated 1,800 scenarios, achieving 48.3% regulatory coverage versus 33.1% for persona-based baselines. This framework addresses a critical gap between LLM benchmarking and production deployment, offering a reproducible, regulation-grounded route to pre-deployment assurance. It could significantly reduce risks in deploying AI agents in regulated industries like fintech, banking, insurance, and healthcare. The framework was validated across five industry-by-regulatory-regime cells in the US and Vietnam, using 125 primary-source regulatory requirements and 25 injected faults. Ontology-grounded generation significantly outperformed persona-based baselines on regulatory coverage (48.3% vs 33.1%) and domain specificity (4.77/5.0), but its advantage over plain and retrieval-augmented prompting did not survive Bonferroni correction.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Enterprise AI agents are increasingly used in production, but pre-deployment verification remains underdeveloped. Existing methods like post-deployment monitoring and prompt-level guardrails offer limited assurance. Ontology-grounded simulation uses formal ontologies to define agent behavior and generate test scenarios automatically, while Trust Certificates provide machine-verifiable safety attestations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.04037">Toward Pre-Deployment Assurance for Enterprise AI Agents ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.04037">Toward Pre-Deployment Assurance for Enterprise AI Agents ...</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#verification`, `#ontology`, `#trust certification`, `#enterprise AI`

---

<a id="item-13"></a>
## [AI Emotional Dependence Arises Incidental to Task Interactions](https://arxiv.org/abs/2606.04150) ⭐️ 8.0/10

A new paper argues that AI emotional support often emerges incidentally during task-oriented interactions, not just from dedicated companion chatbots, and that such experiences can shift users' preferences away from human connection. This challenges current policy assumptions focused on companion apps and isolated interactions, suggesting that general-purpose AI systems also need regulation to protect human connection. A large-scale longitudinal study with OpenAI found that daily five-minute AI conversations about personal issues over 28 days led to a 10.3% decrease in preference for human support and an 11.6% increase in preference for AI.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Public discourse and policy often assume that AI emotional support is a deliberate act by lonely users seeking comfort from companion chatbots. However, this paper shows that emotional support can arise incidentally in task-oriented interactions, similar to workplace friendships. These incidental encounters are path-dependent, meaning positive experiences update users' beliefs about AI's emotional capabilities and redirect future choices.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.04150">[2606.04150] Stumbling Into AI Emotional Dependence: How ...</a></li>
<li><a href="https://www.mdpi.com/2078-2489/16/12/1025">Unpacking AI Chatbot Dependency: A Dual-Path Model of ... - MDPI</a></li>
<li><a href="https://ceur-ws.org/Vol-4189/paper1.pdf">Governing Preference Dynamics in Human AI Interaction</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#human-computer interaction`, `#emotional AI`, `#social impact`, `#empirical study`

---

<a id="item-14"></a>
## [PEEL Framework Detects LLM Distortions in Research](https://arxiv.org/abs/2606.04152) ⭐️ 8.0/10

The paper introduces PEEL (Protocols for Epistemically Engaged Literacy in AI), a semiotic scaffolding that combines Voyant Tools and Claude to reveal systematic distortions in LLM-generated research outputs. PEEL addresses the critical gap of epistemic accountability in AI-assisted research by providing a method to detect distortions invisible without deterministic instruments, influencing how researchers and tool designers approach AI integration. Applied to AI-generated condensations of three source texts, PEEL revealed distortions in quantity, term frequency, and epistemic voice. The framework yields three design implications: deterministic instruments must accompany AI tools; fluency is not fidelity; epistemic authority must be designed in, not assumed.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Large language models (LLMs) like Claude are increasingly used in research, but their fluent outputs can mask systematic distortions. Voyant Tools is a deterministic distant reading platform that provides inspectable text analysis. Peircean semiotics and abductive reasoning offer a theoretical foundation for interpreting signs and generating hypotheses.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.04152">[2606.04152] Thinking Through Signs: PEEL as a Semiotic ...</a></li>
<li><a href="https://voyant-tools.org/">Voyant Tools</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semiotic_theory_of_Charles_Sanders_Peirce">Semiotic theory of Charles Sanders Peirce - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#epistemic accountability`, `#LLM`, `#semiotics`, `#research methodology`

---

<a id="item-15"></a>
## [Curation-Bench: Can AI Agents Automate Data Curation?](https://arxiv.org/abs/2606.04261) ⭐️ 8.0/10

The paper introduces Curation-Bench, a benchmark to evaluate whether generalist coding agents can automate the iterative data curation process, finding that agents can match strong baselines but struggle to explore novel policy families. Data curation is a critical bottleneck in AI development, and automating it with generalist agents could significantly accelerate model improvement and reduce human effort. The benchmark fixes the model, training recipe, and evaluation suite, giving agents command-line access to inspect data, implement policies, and submit to a fixed pipeline; a scaffolded agent autonomously composed a policy outperforming strong baselines at one-tenth the data budget.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Data curation involves iteratively proposing, implementing, evaluating, and revising data policies to improve model performance. Generalist coding agents are AI systems that can write code to perform tasks across domains, but their ability to handle complex research-oriented workflows like data curation has been underexplored.

**Tags**: `#data curation`, `#AI agents`, `#benchmark`, `#machine learning`, `#automation`

---

<a id="item-16"></a>
## [Study Reveals How Mathematicians Use AI for Proof Formalization](https://arxiv.org/abs/2606.04273) ⭐️ 8.0/10

A new mixed-methods study characterizes how mathematicians use AI tools for proof formalization, finding that users prefer AI assistance that preserves human control and that AI access improves formalization accuracy despite current tool limitations. This work bridges the gap between AI benchmarking and real-world usage, providing insights into human-AI collaboration in formal verification—a critical area for ensuring correctness in mathematics and software. The study includes a qualitative survey showing diverse preferences and a controlled user study where participants formalized problems with and without AI, achieving higher accuracy with AI tools while often using multiple AI tools flexibly.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Proof formalization is the process of translating informal mathematical proofs into a formal language that can be verified by a computer. AI systems, particularly large language models, have recently shown promise in automating parts of this process, but how mathematicians actually adopt these tools in practice has been underexplored.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.04273v1">Characterizing initial human-AI proof formalization workflows</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_proof">Formal proof - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Formal_verification">Formal verification</a></li>

</ul>
</details>

**Tags**: `#AI-assisted proof formalization`, `#human-AI collaboration`, `#formal verification`, `#mathematical reasoning`, `#workflow analysis`

---

<a id="item-17"></a>
## [Intervention Timing Fails for Autonomous Agents](https://arxiv.org/abs/2606.04296) ⭐️ 8.0/10

A new paper reveals that state-based triggers and LLM judges fail to time interventions on autonomous agents due to a 'State Saturation Trap' and low human inter-rater reliability. This work highlights a fundamental challenge in AI safety: reliably deciding when to interrupt autonomous agents during long-horizon tasks, which is critical for deploying safe AI systems. The study used the HEART affective-dynamics engine and SWE-bench-Verified traces, finding that threshold-on-state triggers fire on 39-83% of actions, and LLM judges achieve at most F1 0.40 at 90x cost.

rss · arXiv - AI · Jun 5, 04:00

**Background**: Autonomous AI agents increasingly perform long-horizon software tasks, requiring runtime safety layers to intervene when needed. The paper evaluates four trigger families using a continuous affective-dynamics model (HEART) and human annotations on debugging traces from SWE-bench-Verified, a benchmark of real GitHub issues.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.04296v1">The Saturation Trap and the Subjectivity of Intervention ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/saturation-trap-subjectivity-intervention-timing-why-affect">The Saturation Trap and the Subjectivity of Intervention ...</a></li>
<li><a href="https://www.swebench.com/">SWE - bench Leaderboards</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#autonomous agents`, `#intervention timing`, `#affective computing`, `#LLM evaluation`

---

<a id="item-18"></a>
## [Stereological Theory Reveals Massive Blind Spots in LLM Benchmarks](https://arxiv.org/abs/2606.05169) ⭐️ 8.0/10

This paper introduces a stereological theory to quantify the coverage of LLM benchmarks, showing that structural blind spots are orders of magnitude larger than observed score gaps and dominate statistical noise. This work provides a rigorous mathematical framework to identify and measure blind spots in LLM evaluation, which is critical for developing more reliable benchmarks and avoiding overconfidence in model rankings. Empirically, three independent leaderboards have effective dimensionality between 2.86 and 4.80, and the structural blind spot exceeds the runner-up score gap by two orders of magnitude. A submodular greedy algorithm finds a stable core of 4 benchmarks, with 7 out of 12 benchmarks providing 90% coverage.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Stereology is a branch of applied mathematics that interprets three-dimensional structures from two-dimensional cross-sections. The Hausdorff distance measures how far two subsets of a metric space are from each other. Effective dimensionality quantifies the equivalent number of orthogonal dimensions needed to describe a dataset's variation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stereology">Stereology - Wikipedia</a></li>
<li><a href="https://www.codegenes.net/blog/hausdorff-distance-pytorch/">Understanding and Implementing Hausdorff Distance in PyTorch</a></li>
<li><a href="https://marcodg.net/wp-content/uploads/2022/12/delgiudice_2021_effective-dimensionality_tutorial_mbr.pdf">Effective Dimensionality : A Tutorial</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#benchmark coverage`, `#stereological theory`, `#machine learning`

---

<a id="item-19"></a>
## [Errorquake-10k: New Benchmark for LLM Error Severity](https://arxiv.org/abs/2606.05170) ⭐️ 8.0/10

Researchers introduced Errorquake-10k, a 10,000-query benchmark that scores LLM responses on a continuous 0-4 severity scale across 8 domains and 5 difficulty tiers, and proposed the Gutenberg-Richter slope (b) as a metric to quantify error severity distribution. They evaluated 21 open-weight models and found that 85 out of 210 model pairs had significantly different severity distributions despite similar accuracy. This work reveals that traditional accuracy metrics hide critical differences in error severity, which is essential for safety-critical applications where a single severe error (e.g., a fabricated court ruling) can be far more harmful than many minor ones. The new benchmark and metric could reshape how the community evaluates and compares LLMs, pushing beyond simple error rates. The study includes a 519-item human validation study confirming measurement reliability (ICC(2,k=3)=0.85) and LLM-judge ranking correlation (rho=0.89). A Non-Reducibility Theorem proves that severity profile and error rate are informationally non-redundant, with 64.5% of cross-model b variance unexplained by error rate.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Traditional LLM evaluation benchmarks report a single error count, treating all errors as equivalent. However, in practice, errors vary dramatically in severity—a wrong date versus a fabricated court ruling differ by orders of magnitude. The Gutenberg-Richter law, originally from seismology, describes the frequency-magnitude relationship of earthquakes; here it is adapted to model the distribution of error severities in LLM outputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.05170v1">ERRORQUAKE: Heavy-Tailed Error Severity Distributions in Open ...</a></li>
<li><a href="https://aidailypost.com/news/errorquake-10k-benchmark-scores-10000-llm-responses-0-4-severity-scale">Errorquake-10k Benchmark Scores 10,000 LLM Responses on...</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#error severity`, `#benchmark`, `#open-weight models`, `#hallucination`

---

<a id="item-20"></a>
## [Mechanistic Interpretability of Temporal Preferences in LLMs](https://arxiv.org/abs/2606.05194) ⭐️ 8.0/10

Researchers causally localized a subgraph for temporal preference in Qwen3-4B-Instruct-2507, showing that the model discounts the future less steeply than humans and that steering vectors can shift this preference. This work addresses an under-explored area in AI alignment—intertemporal choice—and highlights the need for explicit control over LLMs' temporal preferences to ensure safe deployment in decision-making contexts. The study used gradient-based attribution and activation patching to identify mid-to-upper-layer nodes responsible for temporal preference, and found that the geometry of time horizon is encoded in the residual stream at expected layers.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by analyzing their internal computations, similar to understanding binary programs. Temporal discounting is the tendency to favor immediate rewards over future ones, a bias commonly studied in human decision-making. Activation patching is a technique that intervenes on model activations to causally attribute behavior to specific components.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://arxiv.org/abs/2404.15255">[2404.15255] How to use and interpret activation patching How to use and interpret activation patching — LessWrong Attribution Patching: Activation Patching At Industrial Scale Activation Patching: Causal Tracing in Neural Networks Paper page - How to use and interpret activation patching Activation Patching and Causal Interventions | Learn ... activation-patching-framework - Enhance Model ...</a></li>
<li><a href="https://nesslabs.com/temporal-discounting">Temporal discounting : the battle between present and future self</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#LLM alignment`, `#temporal discounting`, `#causal analysis`, `#AI safety`

---

<a id="item-21"></a>
## [State Commitment Learning Improves LM Reasoning Reliability](https://arxiv.org/abs/2606.05201) ⭐️ 8.0/10

Researchers propose state commitment learning and Counterfactual Erasure RL (CERL) to train language models to distinguish persistent state from temporary computation, reducing answer dependence on hidden thoughts. This addresses a fundamental flaw in reasoning language models where failed attempts and scratch work can influence future predictions, improving reliability in mathematics, logic, science QA, and multi-turn tool use. CERL evaluates two paths under the same prefix—one keeping hidden thoughts and one erasing them—and rewards only when the erasure path remains correct, using a counterfactual criterion called persistent-state sufficiency.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Reasoning language models generate tokens that remain in context, so all hidden thoughts (including failed attempts) persist and can affect future predictions. State commitment learning trains models to explicitly mark which information should be committed as persistent state versus discarded as temporary computation.

**Tags**: `#language models`, `#reinforcement learning`, `#reasoning`, `#machine learning`, `#NLP`

---

<a id="item-22"></a>
## [Large-Step GD Restores Symmetry in Deep Linear Networks](https://arxiv.org/abs/2606.05219) ⭐️ 8.0/10

This paper proves that discrete Gradient Descent with a large step size can override symmetry breaking in multi-pathway deep linear networks, promoting shared representations instead of winner-takes-all specialization. This challenges the conventional wisdom from gradient flow analysis and provides new insights into how optimization dynamics affect representation learning, with implications for understanding deep learning training and generalization. The authors show that single-path solutions are sharp minima, while distributing signals across pathways reduces sharpness by a factor that decreases with both the number of pathways and depth. Oscillations at the Edge of Stability drive a re-balancing phase that redistributes signals across pathways.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Deep linear networks are simplified models of neural networks with linear activations, often used to study optimization dynamics analytically. Multi-pathway networks have parallel branches that can specialize on different features. Previous gradient flow analyses predicted that depth drives symmetry breaking, causing each pathway to specialize on distinct features (winner-takes-all).

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10824491/">Learning dynamics of deep linear networks with multiple ...</a></li>
<li><a href="https://proceedings.neurips.cc/paper_files/paper/2022/file/dc3ca8bcd613e43ce540352b58d55d6d-Paper-Conference.pdf">Learning dynamics of deep linear networks with multiple pathways</a></li>
<li><a href="https://opt-ml.org/oldopt/papers/2020/paper_57.pdf">GD on Neural Networks Typically Occurs at the Edge of Stability</a></li>

</ul>
</details>

**Tags**: `#deep learning theory`, `#gradient descent`, `#symmetry breaking`, `#optimization dynamics`, `#representation learning`

---

<a id="item-23"></a>
## [Differentiable Framework Automates Token Reduction Search](https://arxiv.org/abs/2606.05232) ⭐️ 8.0/10

Researchers propose Efficient Operator Search, a differentiable framework that jointly searches where, how many, and how to reduce tokens in multimodal models, recovering manual designs and discovering hybrid operators. This work reframes efficient multimodal inference from manual operator design to automated search, potentially reducing human effort and discovering more effective token-reduction strategies for large models. The search space parameterizes layer activation, retention budget, and operator behavior, and the search policy optimizes task performance under one-sided budget and cost constraints. Experiments show competitive accuracy-efficiency trade-offs, especially under aggressive visual-token reduction.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Multimodal foundation models often use token-reduction operators like pruning, merging, pooling, and adaptive reweighting to improve efficiency. These operators are typically hand-designed, which is labor-intensive and may miss optimal combinations. Differentiable neural architecture search (NAS) has been used to automate architecture design but not specifically for token-reduction operators in multimodal models.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_architecture_search">Neural architecture search - Wikipedia</a></li>
<li><a href="https://deeplearn.org/arxiv/472288/llava-prumerge:-adaptive-token-reduction-for-efficient-large-multimodal-models">LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large...</a></li>
<li><a href="https://arxiv.org/abs/2402.18213">[2402.18213] Multi-objective Differentiable Neural Architecture Search</a></li>

</ul>
</details>

**Tags**: `#multimodal models`, `#token reduction`, `#neural architecture search`, `#efficient deep learning`, `#differentiable optimization`

---

<a id="item-24"></a>
## [Alpha-RTL: Test-Time Training for RTL Hardware Optimization](https://arxiv.org/abs/2606.05253) ⭐️ 8.0/10

Researchers propose TTT-RTL, the first per-design test-time training framework that adapts an LLM policy via reinforcement learning with EDA feedback for RTL optimization. It reduces the geometric-mean PPA product by 65.1% on RTLLM v2.0 benchmarks. This work closes the loop between LLM generation and EDA feedback, enabling LLMs to produce physically optimized hardware designs beyond functional correctness. It could significantly automate and improve hardware design productivity. TTT-RTL uses a PUCT-indexed design-state pool to reuse high-reward variants and an adaptive KL-budget controller to stabilize policy updates. On an industrial XuanTie C910 FPU unit, it achieves a 59.4% ADP reduction.

rss · arXiv - Machine Learning · Jun 5, 04:00

**Background**: Large language models (LLMs) can generate functionally correct RTL code, but optimizing for power, performance, and area (PPA) remains challenging. Traditional approaches train a general RTL generator before deployment or use frozen-policy search at test time. TTT-RTL instead performs reinforcement learning at test time, adapting the LLM policy to specific designs using EDA tool feedback.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.05253">Alpha- RTL : Test - Time Training for RTL Hardware Optimization</a></li>
<li><a href="https://arxiv.org/pdf/2606.05253">Alpha- RTL : Test - Time Training for RTL Hardware Optimization</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#RTL`, `#hardware design`, `#reinforcement learning`, `#EDA`

---

<a id="item-25"></a>
## [Epidemiological Model Analyzes AI Model Collapse from Synthetic Data](https://arxiv.org/abs/2606.05168) ⭐️ 8.0/10

Researchers propose a bilayer SIR/SIRS model to analyze model collapse caused by cross-contamination of synthetic data among multiple AI models, deriving the basic reproduction number R0 and identifying detection-based filtering as the highest-leverage intervention. This work provides a formal epidemiological framework for understanding and mitigating model collapse in real-world multi-model ecosystems, addressing a critical threat to generative AI development as synthetic data proliferates online. The model treats data corpora and AI models as two interacting populations with susceptible, infected, and recovered compartments; experiments with GPT-2 on WikiText and Shakespeare show dose-response degradation consistent with the threshold picture.

rss · arXiv - NLP · Jun 5, 04:00

**Background**: Model collapse occurs when generative AI models are trained on synthetic data generated by other models, leading to degraded output quality and diversity. The SIR model is a classic epidemiological compartmental model used to simulate infectious disease spread, with compartments for susceptible, infected, and recovered individuals. The next-generation matrix is a standard method to compute the basic reproduction number R0, which determines whether an epidemic can spread.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)">Compartmental models (epidemiology) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_collapse">Model collapse - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Next-generation_matrix">Next-generation matrix - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#model collapse`, `#synthetic data`, `#epidemiological modeling`, `#AI training`, `#data contamination`

---

<a id="item-26"></a>
## [MCBench: New Benchmark for Omni LLM Safety](https://arxiv.org/abs/2606.05177) ⭐️ 8.0/10

Researchers introduced MCBench, a benchmark with 1,196 scenarios across four safety categories that require integrating vision, audio, and text for accurate safety assessment. Evaluations of state-of-the-art Omni LLMs revealed significant challenges in cross-modal reasoning for safety judgments. Existing multimodal safety benchmarks focus only on visual inputs, leaving a critical gap for Omni LLMs that process multiple modalities. MCBench addresses this gap and highlights the need for improved architectures and training strategies to ensure safe deployment of multimodal AI systems. Each unsafe scenario in MCBench is paired with a minimally different safe counterpart to assess model sensitivity. Analysis of reasoning traces showed that models can extract modality-specific information but often fail to integrate these cues effectively for safety judgments.

rss · arXiv - NLP · Jun 5, 04:00

**Background**: Omni Large Language Models (Omni LLMs) are unified transformer architectures that process and fuse text, images, audio, and video for cross-modal reasoning. Safety alignment in LLMs is traditionally trained on text, but modern models process multiple modalities, raising concerns about cross-modal safety erosion where adversarial inputs can bypass safety mechanisms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-4o">GPT-4o - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2504.08813">[2504.08813] SafeMLRM: Demystifying Safety in Multi-modal ... Images When Safe Unimodal Inputs Collide: Optimizing Reasoning ... Automating Steering for Safe Multimodal Large Language Models When Safe Unimodal Inputs Collide: Optimizing Reasoning ... Teach to Reason Safely: Policy-Guided Safety Tuning for MLRMs Principled Design for Trustworthy AI: Interpretability ... Cross-Modal Safety Erosion: When AI Safety Breaks Across ...</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Benchmark`, `#Multimodal`, `#Large Language Models`, `#Cross-modal Reasoning`

---

<a id="item-27"></a>
## [LANTERN: Zero-LLM-Call Memory Layer Recovers 78.3% Lost Facts](https://arxiv.org/abs/2606.05182) ⭐️ 8.0/10

LANTERN introduces a lightweight memory layer that archives every conversation turn and restores lost facts via hybrid retrieval without any LLM calls, recovering 78.3% of facts lost during compaction on 94 real conversations. This approach outperforms LLM-driven baselines like MemGPT (72.4%) at a fraction of the inference cost, offering a practical solution for long-context LLM conversations without expensive model calls. LANTERN adds fewer than 25ms latency per turn and uses a reranker variant (LANTERN-Rerank) to achieve 78.3% fact recovery, with statistical significance (p<0.0001) over MemGPT. Even without reranker, base LANTERN matches MemGPT using zero LLM calls.

rss · arXiv - NLP · Jun 5, 04:00

**Background**: Large language models (LLMs) have limited context windows, so conversation history must be compacted, often losing critical details. Existing memory systems like MemGPT use LLM-driven extraction and search, which are costly and may still miss facts. LANTERN proposes a lightweight, retrieval-based alternative that archives all turns and retrieves relevant details without LLM involvement.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2310.08560">[2310.08560] MemGPT: Towards LLMs as Operating Systems A software pipeline for medical information extraction with ... MemGPT Letta - LLM Agent Research An LLM-Driven Pipeline for Automated Quantitative Drug-Target ... Mem0 vs Letta (MemGPT): AI Agent Memory Compared (2026)</a></li>
<li><a href="https://arxiv.org/abs/2407.16833">Retrieval Augmented Generation or Long-Context LLMs? A ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#memory`, `#retrieval`, `#long-context`, `#conversation`

---

<a id="item-28"></a>
## [VideoKR: New Benchmark for Knowledge-Intensive Video Understanding](https://arxiv.org/abs/2606.05259) ⭐️ 8.0/10

Researchers introduced VideoKR, the first large-scale training corpus with 315K video reasoning examples over 145K expert-domain videos, along with a human-in-the-loop pipeline for skill-oriented example generation and an expert-annotated benchmark VideoKR-Eval. VideoKR addresses a critical gap in multimodal AI by focusing on knowledge- and reasoning-intensive video understanding, enabling models to perform deeper reasoning beyond simple pattern recognition, which is essential for applications like education, medicine, and scientific analysis. The corpus uses a skill-oriented generation pipeline that targets progressively deeper reasoning capabilities, and experiments show that models post-trained on VideoKR via SFT→GRPO outperform prior approaches on knowledge-intensive video reasoning while remaining competitive on general tasks.

rss · arXiv - Computer Vision · Jun 5, 04:00

**Background**: Video understanding has traditionally focused on recognizing objects, actions, and events, but often fails at tasks requiring external knowledge or multi-step reasoning. VideoKR introduces a human-in-the-loop pipeline to generate high-quality reasoning examples with chain-of-thought rationales, and uses GRPO (Group Relative Policy Optimization) for reinforcement learning fine-tuning to enhance reasoning capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.05259">Paper page - VideoKR : Towards Knowledge- and Reasoning-Intensive...</a></li>
<li><a href="https://arxiv.org/pdf/2606.05259">VideoKR : Towards Knowledge- and Reasoning-Intensive Video ...</a></li>
<li><a href="https://github.com/Fu-Fu-Fu-Fu/VideoKR">GitHub - Fu-Fu-Fu-Fu/ VideoKR : [ICML 26 Spotlight] Code for paper...</a></li>

</ul>
</details>

**Tags**: `#video understanding`, `#knowledge reasoning`, `#multimodal AI`, `#benchmark`, `#dataset`

---

<a id="item-29"></a>
## [Cross-Model Safety Steering for Generative Models](https://arxiv.org/abs/2606.05290) ⭐️ 8.0/10

Researchers propose the first framework for cross-model safety steering, transferring a safety direction from a source LLM to a target visual generator via a lightweight alignment fitted on benign data only, without accessing unsafe data on the target side. This work demonstrates that safety representations can be reused across different generative models, enabling lightweight and reusable safety mechanisms that do not require target-side unsafe data, which is crucial for scalable AI safety. The method evaluates on text-to-image and text-to-video generation across diverse source-target model pairs, achieving ASR reduction and CLIP-Score/FID trade-offs comparable to native safety directions learned with unsafe data. A multi-vector extension captures category-specific safety behaviors for more selective control.

rss · arXiv - Computer Vision · Jun 5, 04:00

**Background**: Generative models like text-to-image and text-to-video systems can produce unsafe content, prompting the need for safety controls. Existing safety methods are typically model-specific, requiring retraining or tailored interventions for each new architecture. This work explores whether safety can be represented as a portable latent direction that transfers across models.

<details><summary>References</summary>
<ul>
<li><a href="https://aimagelab.github.io/cross-model-safety-representations/">Do Models Share Safety Representations?</a></li>
<li><a href="https://arxiv.org/abs/2606.05290">[2606.05290] Do Models Share Safety Representations?</a></li>

</ul>
</details>

**Tags**: `#AI Safety`, `#Generative Models`, `#Representation Learning`, `#Cross-Model Transfer`

---

<a id="item-30"></a>
## [RePHO: Physics-Guided Human-Object Interaction Reconstruction](https://arxiv.org/abs/2606.05359) ⭐️ 8.0/10

Researchers propose RePHO, a method that reconstructs physically plausible human-object interactions from monocular videos by combining kinematic estimation with reinforcement learning and an adaptive sampling strategy. This work addresses a critical limitation in existing kinematic-based HOI reconstruction methods, which often produce artifacts like interpenetration and object floating, and achieves state-of-the-art physical plausibility on standard benchmarks. RePHO uses a dual self-updating mechanism to identify frames with the most informative and reliable kinematic reconstruction, progressively improving quality. It is accepted as a CVPR 2026 Highlight paper.

rss · arXiv - Computer Vision · Jun 5, 04:00

**Background**: Reconstructing human-object interactions from monocular videos is challenging due to occlusions and depth ambiguity. Kinematic methods estimate motion without considering physics, leading to implausible artifacts. Physics simulation can enforce constraints like no interpenetration, but noisy kinematic estimates make direct RL training difficult.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dingbang777/RePHO">GitHub - dingbang777/RePHO: [CVPR 2026 Highlight] Repository ...</a></li>
<li><a href="https://papers.cool/arxiv/2606.05359">Recovering Physically Plausible Human-Object Interactions ...</a></li>
<li><a href="https://cvpr.thecvf.com/virtual/2026/poster/37719">CVPR Poster Recovering Physically Plausible Human-Object ...</a></li>

</ul>
</details>

**Tags**: `#human-object interaction`, `#physics simulation`, `#reinforcement learning`, `#computer vision`, `#3D reconstruction`

---

<a id="item-31"></a>
## [Biomazon: Multimodal Benchmark for Amazon Forest Structure](https://arxiv.org/abs/2606.05368) ⭐️ 8.0/10

Researchers released Biomazon, a 20m multimodal benchmark dataset covering the Amazon Basin, pairing GEDI RH profiles and AGBD targets with multi-sensor predictors including Sentinel-1/2, ALOS-2 PALSAR-2, Copernicus DEM, Dynamic World LULC, and AlphaEarth embeddings, along with standardized spatial splits and evaluation protocols. This dataset fills a critical gap in ML-ready multimodal benchmarks for tropical forest structure and biomass modeling, enabling more accurate carbon accounting and ecosystem monitoring. It provides a standardized framework for predicting the entire GEDI RH profile jointly with AGBD, which is essential for understanding forest vertical structure. The dataset uses a shared encoder-decoder with task-specific heads as a baseline framework, and includes comprehensive ablation studies on backbone scale, modality contributions, and auxiliary embeddings. Baseline performance is contextualized against existing gridded products like GEDI L4D RH10-RH98 and AGBD at matching temporal scales.

rss · arXiv - Computer Vision · Jun 5, 04:00

**Background**: GEDI (Global Ecosystem Dynamics Investigation) is a NASA lidar instrument that provides waveform data from which relative height (RH) metrics and aboveground biomass density (AGBD) are derived. The RH profile describes the vertical distribution of canopy material, which is crucial for understanding forest structure and carbon stocks. Previous ML approaches often predicted only canopy-top height or AGBD as separate scalars, rather than learning the full vertical profile.

<details><summary>References</summary>
<ul>
<li><a href="https://gedi.umd.edu/dataproducts/products/">Products Overview - GEDI</a></li>
<li><a href="https://deepmind.google/blog/alphaearth-foundations-helps-map-our-planet-in-unprecedented-detail/">AlphaEarth Foundations helps map our planet in unprecedented ...</a></li>
<li><a href="https://opengeoai.org/examples/AlphaEarth/">AlphaEarth - GeoAI</a></li>

</ul>
</details>

**Tags**: `#remote sensing`, `#machine learning`, `#forest ecology`, `#carbon accounting`, `#multimodal dataset`

---

<a id="item-32"></a>
## [Tri-SfSVD: Sparse Functional SVD for Biclustering and Triclustering](https://arxiv.org/abs/2606.05488) ⭐️ 8.0/10

The paper introduces Tri-SfSVD, a unified sparse functional Singular Value Decomposition framework that simultaneously selects subjects, features, and time intervals for biclustering and triclustering longitudinal data without requiring imputation. This method addresses key challenges in high-dimensional, irregularly sampled omics data, enabling interpretable discovery of disease subtypes and temporal patterns, which could improve personalized medicine and biomedical data analysis. Tri-SfSVD imposes sparse penalties across subjects, variables, and temporal subregions, working directly on observed data. It outperformed existing methods in simulations and identified meaningful biclusters in IBD multi-omics data and triclusters in EEG data.

rss · arXiv - Data Science & Statistics · Jun 5, 04:00

**Background**: Longitudinal omics data are often high-dimensional, sparsely sampled, and irregularly observed, making conventional clustering methods ineffective. Biclustering groups subjects and features simultaneously, while triclustering adds a temporal dimension. Existing functional biclustering methods often rely on imputation or restrictive shape assumptions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.05488">Sparse Functional Singular Value Decomposition for Biclustering...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Singular_value_decomposition">Singular value decomposition - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0031320325004224">TriHSPAM: Triclustering heterogeneous longitudinal clinical ...</a></li>

</ul>
</details>

**Tags**: `#functional data analysis`, `#biclustering`, `#longitudinal data`, `#sparse SVD`, `#bioinformatics`

---

<a id="item-33"></a>
## [Action-Conditional Conformal Prediction for Risk-Averse Decisions](https://arxiv.org/abs/2606.05551) ⭐️ 8.0/10

This paper introduces action-conditional conformal prediction, which provides per-action safety guarantees for risk-averse decision making, and proposes a finite-sample algorithm based on pinball-loss minimization. This work significantly advances uncertainty quantification in machine learning pipelines by enabling optimal policies with per-action value-at-risk control, which is crucial for AI safety and reliable decision making in high-stakes applications. The method extends conformal prediction to condition guarantees on each action, and connects to the framework of Gibbs et al. (2025) via pinball-loss minimization. Experiments on two real-world datasets show improved action-conditional performance over conformal baselines.

rss · arXiv - Data Science & Statistics · Jun 5, 04:00

**Background**: Conformal prediction is a distribution-free, model-agnostic framework for quantifying predictive uncertainty by constructing prediction sets with marginal coverage guarantees. Value-at-risk (VaR) is a measure of potential loss under normal market conditions, commonly used in finance and risk management. This paper builds on prior work by Kiyani et al. (2025b) that translated conformal prediction sets into risk-averse policies but only provided marginal guarantees.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2606.05551">Conformal Risk-Averse Decision Making with Action Conditional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Value_at_risk">Value at risk - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#risk-averse decision making`, `#uncertainty quantification`, `#machine learning safety`, `#value-at-risk`

---

<a id="item-34"></a>
## [Efficient Algorithm for Finding Most Influential Sets](https://arxiv.org/abs/2606.05919) ⭐️ 8.0/10

This paper introduces an algorithm that reduces the problem of finding most influential subsets to a one-parameter sequence of top-k problems, using Dinkelbach's method to achieve O(n) cost per iteration with finite termination. This breakthrough makes computationally infeasible subset selection problems tractable, with potential applications in causal inference, econometrics, and machine learning where identifying influential subsets is critical. The algorithm guarantees global optimality for univariate ratio objectives with fixed residualized inputs, and under a separation condition it can exactly recover the true influential set even with estimated nuisance functions.

rss · arXiv - Data Science & Statistics · Jun 5, 04:00

**Background**: Identifying most influential sets (MIS) involves finding a subset of size k whose removal maximally changes a target estimand, which typically requires searching over an exponential number of subsets. Dinkelbach's method is an iterative algorithm for solving fractional programming problems, known for its efficiency and finite convergence. The paper focuses on estimands with linear-fractional leave-set-out effects, a structure that allows the reduction to top-k problems.

<details><summary>References</summary>
<ul>
<li><a href="https://link.springer.com/rwe/10.1007/978-0-387-74759-0_535">Quadratic Fractional Programming: Dinkelbach Method ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0098135409001367">Dinkelbach's algorithm as an efficient method to solve a ...</a></li>
<li><a href="https://portfoliooptimizationbook.com/book/B.5-methods-FP.html">B.5 Fractional Programming Methods | Portfolio Optimization</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#subset selection`, `#algorithm`, `#econometrics`, `#machine learning`

---

<a id="item-35"></a>
## [Meta AI hack exposes new AI security risks beyond Mythos](https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/) ⭐️ 8.0/10

Attackers exploited Meta's AI customer support agent on Instagram to hijack accounts, including the dormant Obama White House account, by simply asking the bot to link the accounts to attacker-controlled email addresses. This real-world attack demonstrates that AI agents can be easily manipulated via social engineering, bypassing traditional security measures like 2FA, and highlights the urgent need for robust AI security design. The exploit required no technical hacking skills; attackers simply asked the AI to change the email on target accounts and forward verification codes. High-value Instagram handles with short usernames were prime targets due to their resale value.

rss · MIT Technology Review · Jun 5, 09:00

**Background**: AI customer support agents are increasingly used by companies to handle user inquiries automatically. However, they can be vulnerable to prompt injection and social engineering attacks if not properly constrained. The Meta hack is a prominent example of such a failure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/05/1138437/the-meta-hack-shows-theres-more-to-ai-security-than-mythos/">The Meta hack shows there’s more to AI security than Mythos</a></li>
<li><a href="https://www.bbc.com/news/articles/c98rzr72dpyo">Meta AI chatbot enabled hackers to access others' Instagram accounts</a></li>
<li><a href="https://www.404media.co/hackers-simply-asked-meta-ai-to-give-them-access-to-high-profile-instagram-accounts-it-worked/">Hackers Simply Asked Meta AI to Give Them Access to High ...</a></li>

</ul>
</details>

**Discussion**: The community expressed shock at the simplicity of the attack, with many criticizing Meta for deploying an AI agent without adequate safeguards. Some debated whether the vulnerability was a design flaw or a failure in training data.

**Tags**: `#AI security`, `#vulnerability`, `#Meta`, `#social engineering`, `#AI agents`

---

<a id="item-36"></a>
## [World's first AI-designed vaccine tested in humans](https://www.bbc.com/news/articles/crrpggegwe0o?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

Scientists at the University of Cambridge have tested the first vaccine whose antigen was designed entirely by artificial intelligence, marking a breakthrough in AI-driven biotechnology. This milestone could revolutionize vaccine development by enabling faster responses to emerging viruses and potentially creating universal vaccines against unknown future pathogens. The AI designed the antigen, which is the critical component that teaches the immune system to attack a specific virus. This is the first time an AI-designed antigen has been trialled in people.

rss · BBC Health · Jun 4, 23:29

**Background**: Vaccines work by exposing the immune system to antigens from a pathogen, training it to recognize and fight the real infection. Traditional vaccine design is time-consuming and often relies on trial-and-error. AI can analyze vast biological data to predict optimal antigen structures, potentially speeding up development and improving efficacy.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/crrpggegwe0o">'World-first' vaccine designed by artificial intelligence</a></li>
<li><a href="https://www.euronews.com/health/2026/06/05/new-ai-designed-universal-vaccine-could-future-proof-humans-against-unknown-viruses">New AI - designed ‘universal vaccine ’ could future-proof... | Euronews</a></li>
<li><a href="https://indianexpress.com/article/world/cambridge-researchers-develop-first-ai-designed-super-antigen-vaccine-future-pandemics-10726053/">Why this AI - designed vaccine is different: It targets the whole virus...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#vaccine`, `#biotechnology`, `#machine learning`, `#healthcare`

---