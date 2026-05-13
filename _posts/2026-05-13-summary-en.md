---
layout: default
title: "Horizon Summary: 2026-05-13 (EN)"
date: 2026-05-13
lang: en
---

> From 94 items, 40 important content pieces were selected

---

1. [Six Critical CVEs in dnsmasq: Remote Code Execution Risks](#item-1) ⭐️ 9.0/10
2. [LLMs-from-scratch: Build a GPT-like LLM in PyTorch](#item-2) ⭐️ 9.0/10
3. [First Global 10m Agricultural Field Boundary Map Released](#item-3) ⭐️ 9.0/10
4. [GitHub Repo Aims to Restore Bambu Network Support](#item-4) ⭐️ 8.0/10
5. [Elevator: Deterministic Static Binary Translation Without Heuristics](#item-5) ⭐️ 8.0/10
6. [Needle: 26M Parameter Tool-Calling Model Distilled from Gemini](#item-6) ⭐️ 8.0/10
7. [Scrcpy v4.0 Released with Flexible Virtual Displays](#item-7) ⭐️ 8.0/10
8. [DuckDB Launches Quack Client-Server Protocol](#item-8) ⭐️ 8.0/10
9. [Obsidian Unveils New Community Site and Automated Plugin Review](#item-9) ⭐️ 8.0/10
10. [CloakBrowser: Stealth Chromium Bypasses All Bot Detection](#item-10) ⭐️ 8.0/10
11. [Fish Speech: SOTA Open-Source Multilingual TTS](#item-11) ⭐️ 8.0/10
12. [LiteLLM: Open-Source AI Gateway for 100+ LLMs](#item-12) ⭐️ 8.0/10
13. [Open Interpreter: Natural Language Interface for Computers](#item-13) ⭐️ 8.0/10
14. [MetaGPT: Multi-Agent Framework for AI Software Development](#item-14) ⭐️ 8.0/10
15. [ByteDance Open-Sources UI-TARS for GUI Automation](#item-15) ⭐️ 8.0/10
16. [VLM Reliability Lies in Hidden States, Not Attention](#item-16) ⭐️ 8.0/10
17. [Auto-Rubric as Reward: Explicit Rubrics for Robust Multimodal Alignment](#item-17) ⭐️ 8.0/10
18. [Embeddings for Preferences, Not Semantics](#item-18) ⭐️ 8.0/10
19. [Free-Energy Framework Distinguishes Capability Elicitation from Creation](#item-19) ⭐️ 8.0/10
20. [MemQ: Q-Learning with Provenance DAGs for LLM Agents](#item-20) ⭐️ 8.0/10
21. [LLMs Learn Graphs In-Context via Dual Mechanisms](#item-21) ⭐️ 8.0/10
22. [Adaptive Steering for Discrete Diffusion Language Models](#item-22) ⭐️ 8.0/10
23. [Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization](#item-23) ⭐️ 8.0/10
24. [LLM Diversity Collapse Traced to Calibration Issues](#item-24) ⭐️ 8.0/10
25. [ClinicalBench: Stress-Testing Assertion-Aware Retrieval for Clinical QA](#item-25) ⭐️ 8.0/10
26. [Bicameral Model: Hidden-State Coupling Between LLMs](#item-26) ⭐️ 8.0/10
27. [DP's Effect on LLM Social Bias: Mixed Results](#item-27) ⭐️ 8.0/10
28. [Instructions Shape Production, Not Processing in LLMs](#item-28) ⭐️ 8.0/10
29. [ReVision Cuts Visual Token Use by 46% for Computer Agents](#item-29) ⭐️ 8.0/10
30. [Hebatron: Hebrew-Specialized MoE Language Model](#item-30) ⭐️ 8.0/10
31. [ReAD: Reinforcement-Guided Capability Distillation for LLMs](#item-31) ⭐️ 8.0/10
32. [HiDream-O1-Image: Unified Pixel-Space Diffusion Transformer](#item-32) ⭐️ 8.0/10
33. [Background-Invariant VLM Representations via Linear Structure](#item-33) ⭐️ 8.0/10
34. [Perspectivist Classifier Predicts Political Sentiment by Identity](#item-34) ⭐️ 8.0/10
35. [ABRA: A New Benchmark for Radiology AI Agents](#item-35) ⭐️ 8.0/10
36. [Uniform Scaling Limits in AdamW-Trained Transformers](#item-36) ⭐️ 8.0/10
37. [Thompson Sampling for Adaptive Policy Under Unknown Network Interference](#item-37) ⭐️ 8.0/10
38. [Post-ADC Inference: Valid Inference After Active Data Collection](#item-38) ⭐️ 8.0/10
39. [Minimax Rates and Spectral Distillation for Tree Ensembles](#item-39) ⭐️ 8.0/10
40. [Anchor-Guided Variance-Aware Reward Modeling Resolves Non-Identifiability](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Six Critical CVEs in dnsmasq: Remote Code Execution Risks](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT has released six CVEs for serious security vulnerabilities in dnsmasq, including remote heap overflow, infinite loops, and buffer overflow, affecting millions of devices. These vulnerabilities allow remote code execution and denial-of-service attacks on a widely-used DNS/DHCP server in embedded devices, routers, and Android, posing a significant threat to network infrastructure. A remote attacker can cause a large out-of-bounds write on the heap via DNS queries, trigger infinite loops with malformed DNS responses, or exploit malicious DHCP requests for buffer overflow.

hackernews · chizhik-pyzhik · May 12, 18:12 · [Discussion](https://news.ycombinator.com/item?id=48112042)

**Background**: dnsmasq is a lightweight, open-source DNS forwarder and DHCP server commonly used in home routers, IoT devices, and Android. It is designed for small networks and has low resource requirements. The Common Vulnerabilities and Exposures (CVE) system provides a standardized reference for publicly known security vulnerabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heap_overflow">Heap overflow</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community expresses urgency for memory-safe language adoption, noting that most recent vulnerabilities stem from memory-unsafe languages like C. Users also lament the widespread use of dnsmasq in devices that rarely receive updates, amplifying the risk.

**Tags**: `#security`, `#dnsmasq`, `#CVE`, `#memory safety`, `#embedded systems`

---

<a id="item-2"></a>
## [LLMs-from-scratch: Build a GPT-like LLM in PyTorch](https://github.com/rasbt/LLMs-from-scratch) ⭐️ 9.0/10

Sebastian Raschka released the official code repository for his book 'Build a Large Language Model (From Scratch)', providing step-by-step PyTorch implementations for developing, pretraining, and finetuning a ChatGPT-like LLM. This resource demystifies LLMs by teaching how to build one from scratch, making advanced AI concepts accessible to students, researchers, and practitioners, and bridging the gap between theory and practice. The repository includes code for a small but functional GPT-like model with around 33K parameters, and also supports loading larger pretrained weights for finetuning. It uses only PyTorch without external LLM libraries.

rss · GitHub Trending - Daily (All) · May 13, 14:40

**Background**: Large language models (LLMs) like GPT-4 power many AI applications, but their internal workings are often opaque. This book and repository aim to teach the inner mechanics by guiding readers through implementing a GPT-like model from scratch, covering tokenization, attention mechanisms, training, and finetuning.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/rasbt/LLMs-from-scratch">GitHub - rasbt/LLMs- from - scratch : Implement a ChatGPT- like LLM in...</a></li>
<li><a href="https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/1633437167">Build a Large Language Model (From Scratch): Raschka, Sebastian: 9781633437166: Amazon.com: Books</a></li>
<li><a href="https://www.goodreads.com/book/show/209234015-build-a-large-language-model">Build a Large Language Model (From Scratch) by Sebastian Raschka | Goodreads</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#PyTorch`, `#GPT`, `#deep learning`, `#tutorial`

---

<a id="item-3"></a>
## [First Global 10m Agricultural Field Boundary Map Released](https://arxiv.org/abs/2605.11055) ⭐️ 9.0/10

Researchers have created the first global agricultural field boundary map at 10m resolution for 2024-2025, comprising 3.17 billion polygons across 241 countries, using a U-Net model on Sentinel-2 imagery. This dataset fills a critical gap by providing a globally consistent, openly available field-level unit for crop monitoring, food security, and environmental analysis, replacing pixel-level products. The map achieved a mean pixel-level recall of 0.85 validated against ground truth in 24 countries, with F1 scores of 0.89, 0.88, and 0.74 for Austria, Latvia, and Finland respectively. A 500m confidence layer is included to indicate prediction reliability.

rss · arXiv - Computer Vision · May 13, 04:00

**Background**: Agricultural field boundaries are essential for precision agriculture and policy, but global maps have been unavailable. The U-Net model is a deep learning architecture for image segmentation, trained here on the Fields of The World dataset, which covers diverse agricultural landscapes across 24 countries. Sentinel-2 provides free, high-resolution satellite imagery.

<details><summary>References</summary>
<ul>
<li><a href="https://fieldsofthe.world/">Fields of The World: A Global Field Boundary Ecosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/U-Net">U-Net - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#remote sensing`, `#agriculture`, `#deep learning`, `#geospatial`, `#field boundaries`

---

<a id="item-4"></a>
## [GitHub Repo Aims to Restore Bambu Network Support](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

A GitHub repository (FULU-Foundation/OrcaSlicer-bambulab) has been created to restore full Bambu Network support for Bambu Lab printers, following a controversial firmware update that removed local printing capabilities. This effort highlights the growing tension between user rights and manufacturer control in the 3D printing community, as Bambu Lab's firmware update sparked widespread backlash for restricting local printing and requiring cloud authentication. The repository appears to be a clone of the prior state of OrcaSlicer that supported full local network printing before Bambu Lab's changes. Bambu Lab's new system introduces two modes: default/Cloud mode requiring Bambu Studio or Bambu Connect, and LAN mode with limited functionality.

hackernews · Murfalo · May 12, 21:55 · [Discussion](https://news.ycombinator.com/item?id=48115127)

**Background**: Bambu Lab is a Shenzhen-based 3D printer manufacturer founded by former DJI engineers. In early 2025, the company announced a firmware update that introduced an Authorization Control System, which initially required cloud authentication even for local LAN printing, later partially backtracking after community backlash.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bambu_Lab">Bambu Lab - Wikipedia</a></li>
<li><a href="https://consumerrights.wiki/w/Wiki/Bambu_Lab_Authorization_Control_System">Bambu Lab Authorization Control System - Consumer Rights Wiki</a></li>

</ul>
</details>

**Discussion**: Community comments express strong frustration, with users calling the removal of local printing functionality 'theft' and criticizing Bambu Lab's approach. Some users compare Bambu Lab's system unfavorably to Ubiquiti's more user-friendly remote access model, while others note that the initial backlash forced Bambu Lab to partially backtrack on LAN mode requirements.

**Tags**: `#3D printing`, `#open source`, `#firmware`, `#maker community`, `#Bambu Lab`

---

<a id="item-5"></a>
## [Elevator: Deterministic Static Binary Translation Without Heuristics](https://arxiv.org/abs/2605.08419) ⭐️ 8.0/10

Researchers present Elevator, the first fully-static binary translator that converts entire x86-64 executables to AArch64 without using heuristics, debug info, or source code, achieving deterministic translation with performance comparable to QEMU's JIT. This work enables certification in regulated industries (aviation, medical devices) where JIT is unacceptable because the translated code must be deterministic and auditable. It also opens the door for static binary translation to be used in performance-critical scenarios without runtime fallbacks. Elevator considers all possible interpretations of every byte and produces separate translations for each feasible one ahead of time, leading to a 50x increase in .text section size. It supports multithreading and exception handling in principle, though these are out of scope for the current project.

hackernews · matt_d · May 13, 04:25 · [Discussion](https://news.ycombinator.com/item?id=48117810)

**Background**: Binary translation converts executable code from one instruction set architecture (ISA) to another. Static binary translation aims to translate all code before execution, but traditional approaches rely on heuristics to distinguish code from data, which can fail and require runtime fallbacks. QEMU uses just-in-time (JIT) compilation for dynamic translation, which is faster than interpretation but non-deterministic and unsuitable for certification.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">[2605.08419] Deterministic Fully-Static Whole-Binary Translation without Heuristics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_translation">Binary translation - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2605.08419">Deterministic Fully-Static Whole-Binary Translation without Heuristics</a></li>

</ul>
</details>

**Discussion**: Commenters highlight the certification angle as the most compelling use case, noting that regulated industries cannot use JIT. Others discuss the 50x code size increase as a reasonable trade-off for determinism, and express curiosity about handling indirect jumps and VM-protected binaries.

**Tags**: `#binary translation`, `#static analysis`, `#compilers`, `#performance`, `#systems`

---

<a id="item-6"></a>
## [Needle: 26M Parameter Tool-Calling Model Distilled from Gemini](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus has released Needle, a 26 million parameter tool-calling model distilled from Gemini, which uses only attention and gating layers with no MLPs, achieving 6000 tok/s prefill and 1200 tok/s decode on consumer devices. This demonstrates that tiny, efficient models can handle tool calling effectively, enabling on-device agentic AI on budget phones, wearables, and IoT devices without relying on cloud APIs. The model was pretrained on 200B tokens using 16 TPU v6e for 27 hours, then post-trained on 2B tokens of synthesized function-calling data for 45 minutes. It outperforms larger models like FunctionGemma-270M and Qwen-0.6B on single-shot function calling, but has limited conversational scope.

hackernews · HenryNdubuaku · May 12, 18:03 · [Discussion](https://news.ycombinator.com/item?id=48111896)

**Background**: Tool calling (or function calling) allows LLMs to interact with external tools like APIs, databases, or sensors, enabling agentic behavior. Model distillation transfers knowledge from a large teacher model (e.g., Gemini) to a smaller student model, reducing computational cost. Traditional transformers use MLPs for reasoning, but Needle's architecture shows that for retrieval-and-assembly tasks, attention and gating suffice.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>

</ul>
</details>

**Discussion**: Commenters expressed interest in the model's discriminatory power for complex tool use, with one noting that simple weather queries were already solvable a decade ago. Others raised concerns about Google's potential anti-distillation defenses and suggested publishing a live demo. There was also excitement about the possibility of embedding tiny models in command-line tools for natural language argument parsing.

**Tags**: `#tool calling`, `#model distillation`, `#on-device AI`, `#function calling`, `#efficient models`

---

<a id="item-7"></a>
## [Scrcpy v4.0 Released with Flexible Virtual Displays](https://github.com/Genymobile/scrcpy/releases/tag/v4.0) ⭐️ 8.0/10

Scrcpy v4.0 introduces flexible virtual displays that can be resized dynamically, along with performance improvements and new features for Android screen mirroring and control. This update enhances the versatility of scrcpy, making it even more valuable for Android developers, testers, and power users who need to interact with multiple displays or resize windows on the fly. The new --flex-display (or -x) flag allows the virtual display to resize with the client window, and scrcpy v4.0 also includes various performance optimizations and bug fixes.

hackernews · xnx · May 12, 20:50 · [Discussion](https://news.ycombinator.com/item?id=48114356)

**Background**: Scrcpy is a free and open-source tool that lets users display and control Android devices from a desktop computer via USB or wirelessly, with low latency and no root required. It is widely used by developers for app testing, demonstrations, and remote control. Virtual displays, introduced in v3.0, allow mirroring a separate display from the device, and v4.0 makes them flexible.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md">scrcpy/doc/virtual_display.md at master · Genymobile/scrcpy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Scrcpy">scrcpy - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed excitement about the flexible display feature, with one user calling scrcpy an 'incredible project' that blew their mind. Others shared creative use cases, such as using a phone as a network bridge or controlling Android from iOS via scrcpy-mobile.

**Tags**: `#Android`, `#open-source`, `#screen mirroring`, `#tooling`, `#release`

---

<a id="item-8"></a>
## [DuckDB Launches Quack Client-Server Protocol](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB announced 'Quack', a new client-server protocol that enables remote connections and concurrent writers, allowing horizontal scaling and easier data exploration. This addresses a key limitation of DuckDB's embedded nature, enabling it to be used in multi-user, networked environments and scaling out across machines, which broadens its applicability in data engineering and analytics. The Quack protocol supports the full DuckDB feature set over the wire and is optimized for performance. It is available as a beta extension, allowing any two DuckDB processes on a network to act as client and server.

hackernews · aduffy · May 12, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48111765)

**Background**: DuckDB is an embedded, in-process SQL OLAP database management system, traditionally designed for single-process use. A client-server protocol allows remote access and concurrent operations, which is standard for most databases but was previously missing in DuckDB.

<details><summary>References</summary>
<ul>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack : The DuckDB Client - Server Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">The quack : protocol allows you to introduce remote access to DuckDB .</a></li>
<li><a href="https://motherduck.com/blog/duckdb-client-server/">If It Quacks Like a Duck : DuckDB Gets a Client - Server Protocol</a></li>

</ul>
</details>

**Discussion**: The community is highly positive, with users expressing excitement about solving real-world problems like remote access and horizontal scaling. Some users noted the need for clearer documentation on concurrent writes, while others debated DuckDB's evolving identity.

**Tags**: `#DuckDB`, `#database`, `#client-server protocol`, `#scalability`, `#data engineering`

---

<a id="item-9"></a>
## [Obsidian Unveils New Community Site and Automated Plugin Review](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian announced a new community site and an automated review system to streamline plugin submissions, addressing developer burnout and submission bottlenecks that had made it nearly impossible to submit new plugins. This update is critical for the Obsidian ecosystem, as it removes a major scaling bottleneck and reduces developer frustration, ensuring the plugin marketplace can continue to grow sustainably. The new system includes automated checks for malicious code, but some community members argue that proper sandboxing with an explicit permission system would be more effective for security.

hackernews · xz18r · May 12, 15:45 · [Discussion](https://news.ycombinator.com/item?id=48109970)

**Background**: Obsidian is a popular note-taking app with an open plugin API that allows users to extend its functionality. The plugin ecosystem has grown rapidly, with thousands of plugins, but the manual review process became a bottleneck, causing long delays and developer burnout.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin">Submit your plugin - Developer Documentation</a></li>
<li><a href="https://docs.obsidian.md/Plugins/Releasing/Submission+requirements+for+plugins">Submission requirements for plugins - Developer Documentation</a></li>

</ul>
</details>

**Discussion**: The community expressed relief and excitement, with many acknowledging the severity of the previous bottleneck. However, some users raised security concerns, suggesting that automated checks are insufficient and that a sandboxed permission system is needed. CEO kepano responded, noting the team's ongoing efforts and openness to feedback.

**Tags**: `#Obsidian`, `#plugin ecosystem`, `#developer tools`, `#community management`, `#scaling`

---

<a id="item-10"></a>
## [CloakBrowser: Stealth Chromium Bypasses All Bot Detection](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser is a stealth Chromium browser that passes all 30 bot detection tests by applying 49 source-level C++ fingerprint patches, and serves as a drop-in replacement for Playwright and Puppeteer. This project addresses a critical pain point in web scraping and automation by providing a free, open-source solution that evades advanced anti-bot systems like Cloudflare Turnstile and reCAPTCHA v3, potentially saving developers significant time and cost. CloakBrowser modifies Chromium at the C++ source level rather than using JavaScript injections or config patches, ensuring fingerprints appear identical to a normal browser. It also includes a humanize=True flag for realistic mouse movements and typing patterns.

rss · GitHub Trending - Daily (All) · May 13, 14:40

**Background**: Browser automation tools like Playwright and Puppeteer are widely used for testing and scraping, but many websites deploy anti-bot systems that detect automation signals. Traditional stealth approaches often rely on JavaScript patches or configuration tweaks, which are easily detected. CloakBrowser instead patches the Chromium binary itself, making it indistinguishable from a real user's browser.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/CloakHQ/CloakBrowser">GitHub - CloakHQ/CloakBrowser: Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. · GitHub</a></li>
<li><a href="https://cloakbrowser.dev/">CloakBrowser — Stealth Chromium for Browser Automation</a></li>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps | Playwright</a></li>

</ul>
</details>

**Tags**: `#browser automation`, `#bot detection`, `#web scraping`, `#Playwright`, `#fingerprinting`

---

<a id="item-11"></a>
## [Fish Speech: SOTA Open-Source Multilingual TTS](https://github.com/fishaudio/fish-speech) ⭐️ 8.0/10

Fish Speech, developed by Fish Audio, is a state-of-the-art open-source text-to-speech system that supports multilingual speech synthesis with high naturalness and emotional expressiveness. This project democratizes access to high-quality TTS technology, enabling developers and researchers to build applications with realistic voice generation without relying on proprietary services. The model is trained on over 10 million hours of audio across approximately 50 languages, and achieves the lowest Word Error Rate on Seed-TTS Eval among evaluated models, including closed-source systems.

rss · GitHub Trending - Python · May 13, 14:40

**Background**: Text-to-speech (TTS) systems convert written text into spoken audio. Open-source TTS models like Fish Speech allow anyone to use, modify, and deploy the technology, fostering innovation in voice applications, accessibility tools, and content creation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/fishaudio/fish-speech">GitHub - fishaudio/fish-speech: SOTA Open Source TTS · GitHub</a></li>
<li><a href="https://speech.fish.audio/">Fish Audio</a></li>
<li><a href="https://huggingface.co/fishaudio/fish-speech-1.5">fishaudio/fish-speech-1.5 · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#open-source`, `#AI`, `#speech synthesis`, `#GitHub trending`

---

<a id="item-12"></a>
## [LiteLLM: Open-Source AI Gateway for 100+ LLMs](https://github.com/BerriAI/litellm) ⭐️ 8.0/10

BerriAI's LiteLLM is an open-source AI gateway that provides a unified SDK and proxy server to call over 100 LLM APIs using the OpenAI format, with built-in cost tracking, guardrails, and load balancing. LiteLLM simplifies multi-provider LLM integration, reducing development overhead and enabling teams to switch or combine models without rewriting code, which accelerates AI application development and deployment. LiteLLM supports providers including Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, and NVIDIA NIM, and offers enterprise features like virtual keys, spend tracking, and an admin dashboard.

rss · GitHub Trending - Python · May 13, 14:40

**Background**: An AI gateway acts as middleware to manage LLM API calls, handling integration, routing, security, and optimization. Guardrails are safety controls that monitor and dictate user interactions with LLMs, while load balancing distributes requests across resources to optimize performance and avoid overload.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/API_gateway">API gateway</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-gateway">What Is An AI Gateway? | IBM</a></li>
<li><a href="https://www.wiz.io/academy/ai-security/llm-guardrails">LLM Guardrails Explained: Securing AI Applications in Production | Wiz</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#API Gateway`, `#OpenAI`, `#Python`, `#AI/ML`

---

<a id="item-13"></a>
## [Open Interpreter: Natural Language Interface for Computers](https://github.com/openinterpreter/open-interpreter) ⭐️ 8.0/10

Open Interpreter is an open-source tool that allows users to control their computer via natural language, executing code (Python, JavaScript, Shell) locally through a ChatGPT-like terminal interface. This project democratizes AI-assisted automation by providing a free, local alternative to GPT-4's code interpreter, enabling developers and non-developers to automate tasks like data analysis, file editing, and web research through simple conversation. Open Interpreter defaults to OpenAI's GPT-4o but supports other providers and local models; it requires user approval before executing any code for safety.

rss · GitHub Trending - Python · May 13, 14:40

**Background**: Large language models (LLMs) like GPT-4 can generate code but typically run in sandboxed environments. Open Interpreter brings this capability to the user's local machine, allowing the LLM to directly interact with the operating system, files, and applications.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openinterpreter/open-interpreter">GitHub - openinterpreter/open-interpreter: A natural language interface for computers · GitHub</a></li>
<li><a href="https://docs.openinterpreter.com/getting-started/introduction">Introduction - Open Interpreter</a></li>
<li><a href="https://docs.openinterpreter.com/code-execution/usage">Usage - Open Interpreter</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#natural-language-interface`, `#automation`, `#Python`

---

<a id="item-14"></a>
## [MetaGPT: Multi-Agent Framework for AI Software Development](https://github.com/FoundationAgents/MetaGPT) ⭐️ 8.0/10

MetaGPT is a multi-agent framework that assigns distinct roles (e.g., product manager, architect, engineer) to GPT agents to collaboratively complete complex software development tasks from a single natural language requirement. It has recently launched MGX (MetaGPT X), the world's first AI agent development team, and its paper AFlow was accepted as an oral presentation (top 1.8%) at ICLR 2025. This framework represents a significant step toward natural language programming, potentially lowering the barrier to software development by allowing non-programmers to generate code through simple requirements. It also showcases how multi-agent collaboration can overcome the limitations of single LLM agents in complex, multi-step tasks. MetaGPT encodes Standard Operating Procedures (SOPs) into prompt sequences, enabling structured collaboration among agents. The framework outputs user stories, competitive analysis, requirements, data structures, APIs, and documents from a one-line input.

rss · GitHub Trending - Python · May 13, 14:40

**Background**: Natural language programming aims to enable users to create software using everyday language rather than traditional programming languages. MetaGPT builds on this concept by using multiple LLM agents, each with a specific role, to simulate a software company's workflow. The framework leverages GPT models and has gained significant traction on GitHub.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/FoundationAgents/MetaGPT">GitHub - FoundationAgents/MetaGPT: 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming</a></li>
<li><a href="https://arxiv.org/abs/2308.00352">[2308.00352] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework</a></li>
<li><a href="https://docs.deepwisdom.ai/main/en/guide/get_started/introduction.html">MetaGPT: The Multi-Agent Framework | MetaGPT</a></li>

</ul>
</details>

**Tags**: `#multi-agent`, `#LLM`, `#software development`, `#AI framework`, `#natural language programming`

---

<a id="item-15"></a>
## [ByteDance Open-Sources UI-TARS for GUI Automation](https://github.com/bytedance/UI-TARS) ⭐️ 8.0/10

ByteDance has open-sourced UI-TARS, a native GUI agent framework that includes models, a paper, and deployment tools, with the latest version UI-TARS-2 released on September 4, 2025, featuring enhanced capabilities in GUI, game, code, and tool use. UI-TARS represents a shift from heavily wrapped commercial models to an end-to-end native agent that outperforms existing frameworks, potentially transforming software testing, accessibility, and desktop automation by making GUI interaction more efficient and accessible. UI-TARS-1.5 is built on a vision-language model and uses reinforcement learning for advanced reasoning, achieving state-of-the-art results on standard benchmarks. The framework includes a desktop app (UI-TARS-desktop) and integrates with Midscene.js for web automation.

rss · GitHub Trending - Python · May 13, 14:40

**Background**: GUI automation traditionally relies on scripted workflows or commercial AI models with custom prompts. UI-TARS is a native agent that perceives screenshots as input and performs human-like interactions (keyboard and mouse), eliminating the need for expert-crafted prompts and workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bytedance/ui-tars">GitHub - bytedance/UI-TARS: Pioneering Automated GUI Interaction with Native Agents · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2501.12326">[2501.12326] UI-TARS: Pioneering Automated GUI Interaction with Native Agents</a></li>
<li><a href="https://seed.bytedance.com/en/ui-tars">Introducing UI-TARS-1.5 - ByteDance Seed</a></li>

</ul>
</details>

**Tags**: `#GUI automation`, `#AI agents`, `#open-source`, `#ByteDance`, `#software testing`

---

<a id="item-16"></a>
## [VLM Reliability Lies in Hidden States, Not Attention](https://arxiv.org/abs/2605.08200) ⭐️ 8.0/10

A new paper debunks the Attention-Confidence Assumption in vision-language models (VLMs), showing that attention maps are near-zero predictors of correctness (R_pb=0.001). It introduces the VLM Reliability Probe (VRP) pipeline to mechanistically analyze reliability across three VLM families (LLaVA-1.5, PaliGemma, Qwen2-VL). This challenges a common intuition in VLM interpretability and AI safety, suggesting that attention sharpness is misleading for trustworthiness. The findings could steer future research toward hidden-state geometry and sparse late-layer circuits for reliability monitoring. The study found that a single hidden-state linear probe achieves AUROC>0.95 on POPE for two of three families, while self-consistency at K=10 is the strongest behavioral predictor (R_pb=0.43). Causal ablations reveal a sharp architectural split: late-fusion LLaVA concentrates reliability in a fragile late bottleneck, whereas early-fusion PaliGemma and Qwen2-VL distribute it widely.

rss · arXiv - AI · May 13, 04:00

**Background**: Vision-language models (VLMs) process both images and text to generate outputs. The Attention-Confidence Assumption posits that models are more reliable when attention maps are sharply focused on relevant regions. Mechanistic interpretability aims to understand model internals by analyzing components like attention heads and hidden states.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.16320">[2406.16320] What Do VLMs NOTICE? A Mechanistic Interpretability Pipeline for Gaussian-Noise-free Text-Image Corruption and Evaluation</a></li>
<li><a href="https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/">Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025</a></li>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#interpretability`, `#mechanistic interpretability`, `#AI reliability`, `#attention`

---

<a id="item-17"></a>
## [Auto-Rubric as Reward: Explicit Rubrics for Robust Multimodal Alignment](https://arxiv.org/abs/2605.08354) ⭐️ 8.0/10

Auto-Rubric as Reward (ARR) introduces a framework that converts implicit human preferences into explicit, compositional rubrics for reward modeling in multimodal generative AI, and proposes Rubric Policy Optimization (RPO) to distill these rubrics into robust binary rewards for reinforcement learning. This work addresses reward hacking and scalar collapse in RLHF by externalizing implicit preferences into interpretable rubrics, enabling more reliable and data-efficient multimodal alignment. It outperforms pairwise reward models and VLM judges on text-to-image generation and image editing benchmarks. ARR externalizes a VLM's internalized preference knowledge as prompt-specific rubrics before any pairwise comparison, suppressing evaluation biases like positional bias. RPO then uses rubric-conditioned preference decisions to stabilize policy gradients, replacing opaque scalar regression.

rss · arXiv - AI · May 13, 04:00

**Background**: Reinforcement Learning from Human Feedback (RLHF) typically reduces multi-dimensional human preferences to scalar or pairwise labels, which can lead to reward hacking and loss of nuance. Recent Rubrics-as-Reward (RaR) methods attempt to use explicit criteria, but generating reliable rubrics at scale remains challenging. ARR builds on this by automatically generating rubrics from a VLM's implicit knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://cameronrwolfe.substack.com/p/rubric-rl">Rubric-Based Rewards for RL - Deep (Learning) Focus</a></li>
<li><a href="https://arxiv.org/html/2510.14738">AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning</a></li>
<li><a href="https://arxiv.org/abs/2507.17746">[2507.17746] Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains</a></li>

</ul>
</details>

**Tags**: `#RLHF`, `#multimodal generative models`, `#reward modeling`, `#AI alignment`, `#rubrics`

---

<a id="item-18"></a>
## [Embeddings for Preferences, Not Semantics](https://arxiv.org/abs/2605.08360) ⭐️ 8.0/10

A new arXiv paper identifies that standard text embeddings fail to capture preferential similarity needed for collective decision-making, and proposes a framework using synthetic training data to break the correlation between semantic and preferential signals. This work addresses a fundamental gap in applying AI to democratic processes and fair clustering, potentially enabling more accurate preference aggregation from free-form text opinions. The paper formalizes the problem as an invariance issue where text embeddings encode both preference-relevant stance and semantic nuisance like style, and shows that synthetic data designed to break the correlation improves preference prediction across 11 online deliberation datasets.

rss · arXiv - AI · May 13, 04:00

**Background**: Facility location problems and fair clustering are optimization techniques that rely on distance metrics to represent similarity. Standard text embeddings like those from BERT measure semantic similarity, which correlates with but is not equivalent to preferential similarity—how much a person agrees with a statement. This paper highlights that using semantic embeddings directly can lead to incorrect preference aggregation when the correlation breaks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Facility_location_problem">Facility location problem - Wikipedia</a></li>
<li><a href="https://www.fairclustering.com/">Fair Clustering Tutorial</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#collective decision-making`, `#fair clustering`, `#preference learning`, `#AI alignment`

---

<a id="item-19"></a>
## [Free-Energy Framework Distinguishes Capability Elicitation from Creation](https://arxiv.org/abs/2605.08368) ⭐️ 8.0/10

A new arXiv paper proposes a free-energy-based framework to operationally distinguish capability elicitation from capability creation in LLM post-training, introducing the concept of 'accessible support'. This framework clarifies a central debate in post-training research by providing a principled way to determine whether a method merely reweights existing behaviors or expands the model's reachable behavioral space, which could guide more effective training strategies. The paper defines 'accessible support' as the set of behaviors a model can practically produce under finite budgets, and argues that SFT and RL both reweight a pretrained reference distribution, with the key difference being whether the update remains close to the base model.

rss · arXiv - AI · May 13, 04:00

**Background**: Large language model post-training typically involves supervised fine-tuning (SFT) and reinforcement learning (RL), but the distinction between imitation and discovery has been debated. The free-energy principle, originating from neuroscience, describes how systems minimize variational free energy to maintain stability, and has been applied to machine learning for understanding perception and action.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Free_energy_principle">Free energy principle - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2107.00140">[2107.00140] Applications of the Free Energy Principle to Machine Learning and Neuroscience</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8871280/">The Free Energy Principle for Perception and Action: A Deep Learning Perspective - PMC</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#post-training`, `#capability elicitation`, `#free-energy`, `#AI alignment`

---

<a id="item-20"></a>
## [MemQ: Q-Learning with Provenance DAGs for LLM Agents](https://arxiv.org/abs/2605.08374) ⭐️ 8.0/10

MemQ introduces a method that applies TD(λ) eligibility traces to memory Q-values, propagating credit backward through a provenance DAG that records which memories were retrieved when each new memory was created. This addresses a key limitation in current LLM agent memory systems, which treat memories independently and ignore dependency chains. By improving credit assignment, MemQ achieves the highest success rates across six diverse benchmarks, with gains up to +5.7 percentage points on multi-step tasks. Credit weight decays as (γλ)^d with DAG depth d, replacing temporal distance with structural proximity. The method is formalized as an Exogenous-Context MDP, decoupling the exogenous task stream from the endogenous memory store.

rss · arXiv - AI · May 13, 04:00

**Background**: Episodic memory in LLM agents stores past experiences for retrieval, but current methods evaluate each memory's quality independently. TD(λ) eligibility traces are a reinforcement learning technique that assigns credit to states based on recency and frequency, typically along a temporal sequence. A provenance DAG records the dependency relationships between memories, showing which memories were used to create others.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuglr.medium.com/eligibility-trace-in-temporal-difference-learning-391aa94ba091">Eligibility trace in Temporal difference learning | by Guilin Zhu | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_decision_process">Markov decision process - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#LLM agents`, `#episodic memory`, `#credit assignment`, `#provenance DAG`

---

<a id="item-21"></a>
## [LLMs Learn Graphs In-Context via Dual Mechanisms](https://arxiv.org/abs/2605.08405) ⭐️ 8.0/10

A new paper uses a graph random-walk task to provide causal evidence that LLMs encode both local and global graph structures simultaneously during in-context learning, challenging the view that it is merely pattern matching. 这一发现表明上下文学习涉及真正的结构推理和模式匹配，可能影响我们理解和改进LLM推理与泛化能力的方式。 Using PCA, the authors found that at intermediate mixture ratios, both graph topologies are encoded in orthogonal principal subspaces. Activation patching and steering experiments causally confirmed that late-layer representations carry graph-family information.

rss · arXiv - AI · May 13, 04:00

**Background**: In-context learning (ICL) allows LLMs to perform new tasks without weight updates by conditioning on a prompt with examples. Activation patching is a mechanistic interpretability technique that replaces internal activations to test causal relationships. The graph random-walk task involves predicting the next node in a walk on one of two possible graphs, requiring the model to infer the underlying structure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lakera.ai/blog/what-is-in-context-learning">What is In-context Learning, and how does it work: The Beginner’s Guide | Lakera – Protecting AI teams that disrupt the world.</a></li>
<li><a href="https://www.neelnanda.io/mechanistic-interpretability/attribution-patching">Attribution Patching: Activation Patching At Industrial Scale — Neel Nanda</a></li>
<li><a href="https://en.wikipedia.org/wiki/Random_walk">Random walk - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#in-context learning`, `#causal inference`, `#graph learning`, `#interpretability`

---

<a id="item-22"></a>
## [Adaptive Steering for Discrete Diffusion Language Models](https://arxiv.org/abs/2605.10971) ⭐️ 8.0/10

This paper identifies that uniform intervention schedules degrade controlled generation in discrete diffusion language models (DLMs) and proposes an adaptive scheduler that concentrates interventions on steps where target attributes are actively forming. This work addresses a critical gap in DLM research by providing a mechanistic understanding of attribute formation, enabling precise multi-attribute control without quality degradation, which is essential for practical applications like content moderation and personalized generation. The adaptive scheduler achieves up to 93% steering strength on simultaneous three-attribute control, outperforming the strongest baseline by up to 15 percentage points, and its advantage is governed by a single dispersion statistic of the commitment distribution.

rss · arXiv - Machine Learning · May 13, 04:00

**Background**: Discrete diffusion language models generate text by iteratively denoising all positions in parallel, unlike autoregressive models that generate tokens sequentially. Controlled generation methods for DLMs have been imported from autoregressive models but apply uniform intervention at every step, which this paper shows degrades quality. Sparse autoencoders are used to interpret model internals by learning sparse features from activations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.13759">[2506.13759] Discrete Diffusion in Large Language and Multimodal Models: A Survey</a></li>
<li><a href="https://arxiv.org/abs/2309.08600">[2309.08600] Sparse Autoencoders Find Highly Interpretable Features in Language Models</a></li>
<li><a href="https://arxiv.org/abs/2507.07050">[2507.07050] Discrete Diffusion Models for Language Generation</a></li>

</ul>
</details>

**Tags**: `#diffusion language models`, `#controlled generation`, `#mechanistic interpretability`, `#sparse autoencoders`, `#NLP`

---

<a id="item-23"></a>
## [Vertex-Softmax: Tight Transformer Verification via Exact Softmax Optimization](https://arxiv.org/abs/2605.10974) ⭐️ 8.0/10

The paper introduces Vertex-Softmax, a method that exactly optimizes the softmax function over interval constraints for transformer verification, proving vertex optimality and a threshold structure theorem with log-linear complexity. This work provides the tightest sound bound obtainable from score intervals alone, significantly improving certified verification rates for attention-based neural networks, which is crucial for safety-critical AI systems. Vertex-Softmax achieves log-linear complexity in sequence length and is integrated into a CROWN-style verifier with formal soundness guarantees, outperforming alpha-CROWN and branch-and-bound baselines at a fraction of their cost on MNIST, Fashion-MNIST, and CIFAR-10.

rss · arXiv - Machine Learning · May 13, 04:00

**Background**: Certified verification of neural networks aims to provide formal guarantees on model behavior under input perturbations. For transformers, bounding the softmax function over interval constraints is a key challenge, as existing relaxations introduce slack. CROWN is a framework for neural network verification that uses convex relaxations to compute output bounds.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/IBM/CROWN-Robustness-Certification">CROWN: A Neural Network Verification Framework for ... - GitHub</a></li>
<li><a href="https://arxiv.org/abs/1811.00866">Efficient Neural Network Robustness Certification with General Activation ...</a></li>

</ul>
</details>

**Tags**: `#transformer verification`, `#softmax optimization`, `#formal verification`, `#neural network verification`, `#CROWN`

---

<a id="item-24"></a>
## [LLM Diversity Collapse Traced to Calibration Issues](https://arxiv.org/abs/2605.11128) ⭐️ 8.0/10

A new paper introduces a validity-diversity framework that attributes LLM output diversity collapse to two forms of miscalibration: order calibration (valid tokens not reliably ranked above invalid ones) and shape calibration (probability mass overly concentrated on few valid tokens). This work provides a theoretical explanation for why LLMs produce repetitive or narrow outputs, which is critical for improving creative generation, scientific discovery, and AI safety. It suggests that diversity collapse is not just a sampling heuristic issue but a fundamental distributional problem. The framework decomposes the bottleneck into order and shape miscalibration, and shows that local failures compound across decoding steps, leading to strong sequence-level diversity loss. Empirical tests across 14 language models confirm that miscalibration is a general issue.

rss · arXiv - NLP · May 13, 04:00

**Background**: LLMs generate text by predicting the next token probability distribution at each step. Decoding strategies like top-k or top-p sampling rely on the model's confidence ranking and probability shape. When these are miscalibrated, the model either includes invalid tokens or concentrates on too few valid ones, reducing diversity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11128v1">Calibration is the Diversity Bottleneck in LLMs - arXiv</a></li>
<li><a href="https://arxiv.org/html/2504.12522">Evaluating the Diversity and Quality of LLM Generated Content</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#diversity`, `#calibration`, `#decoding`, `#AI safety`

---

<a id="item-25"></a>
## [ClinicalBench: Stress-Testing Assertion-Aware Retrieval for Clinical QA](https://arxiv.org/abs/2605.11143) ⭐️ 8.0/10

Researchers introduced ClinicalBench, a 400-question benchmark over 43 MIMIC-IV patients, and EpiKG, an assertion-aware retrieval method that uses assertion labels and temporality tags in a patient knowledge graph to route retrieval by question intent, achieving a +22.0 percentage point improvement in exact-match accuracy over a dense-RAG baseline. This work addresses a critical gap in clinical QA by focusing on retrieval over real EHR notes, where negation, temporality, and attribution can flip correct answers, and demonstrates that assertion-aware retrieval significantly outperforms standard methods, which is vital for safe clinical decision support. The primary endpoint, based on 50 unanimous-strict items adjudicated by two external physicians, showed a +22.0 percentage point gain (p=0.0192). Physician adjudication revealed that 56% of auto-generated reference answers were defective, highlighting the need for human validation in clinical QA benchmarks.

rss · arXiv - NLP · May 13, 04:00

**Background**: Clinical question answering over electronic health records (EHRs) is challenging because notes contain negated findings (e.g., 'no chest pain'), temporal constraints (e.g., 'history of' vs. 'current'), and attribution issues (e.g., family vs. patient). Standard retrieval-augmented generation (RAG) methods often ignore these nuances, leading to incorrect answers. EpiKG addresses this by building a patient knowledge graph where each fact is annotated with an assertion label (e.g., present, absent) and a temporality tag (e.g., past, current), and then routes retrieval based on the question's intent.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11143">ClinicalBench: Stress-Testing Assertion -Aware Retrieval for...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00521-025-11666-9">A survey on retrieval-augmentation generation (RAG) models for healthcare applications | Neural Computing and Applications | Springer Nature Link</a></li>
<li><a href="https://aclanthology.org/2024.cl4health-1.23.pdf">Revisiting the MIMIC-IV Benchmark: Experiments Using ...</a></li>

</ul>
</details>

**Tags**: `#clinical QA`, `#retrieval`, `#EHR`, `#benchmark`, `#NLP`

---

<a id="item-26"></a>
## [Bicameral Model: Hidden-State Coupling Between LLMs](https://arxiv.org/abs/2605.11167) ⭐️ 8.0/10

The Bicameral Model introduces a trainable neural interface that allows two frozen language models to communicate through continuous hidden states, enabling tool use without text serialization. On arithmetic, coupling two 0.5B models with a calculator raised accuracy from 36% to 96%. This work demonstrates a new paradigm for tool-augmented LLMs, achieving large accuracy gains with minimal added parameters. It could enable more efficient and capable multi-model systems without retraining large models. The interface includes a translation network and a learned suppression gate (~1% of combined parameters) that learns a selective communication protocol from task loss alone. The auxiliary model can generate problem-specific code from hidden-state signals without seeing the problem text.

rss · arXiv - NLP · May 13, 04:00

**Background**: Existing multi-model systems communicate by generating text, which serializes every exchange through the output vocabulary. The Bicameral Model instead uses a continuous, concurrent channel via hidden states, allowing two models to run in lockstep at every generation step.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11167v1">Bidirectional Hidden-State Coupling Between Parallel Language Models</a></li>
<li><a href="https://d2l.ai/chapter_recurrent-modern/bi-rnn.html">10.4. Bidirectional Recurrent Neural Networks — Dive into Deep Learning 1.0.3 documentation</a></li>

</ul>
</details>

**Tags**: `#language models`, `#multi-model systems`, `#tool-augmented LLMs`, `#neural interfaces`, `#machine learning`

---

<a id="item-27"></a>
## [DP's Effect on LLM Social Bias: Mixed Results](https://arxiv.org/abs/2605.11195) ⭐️ 8.0/10

A systematic evaluation reveals that differential privacy (DP) reduces social bias in LLMs for sentence scoring tasks but not across all tasks, highlighting a gap between logit-level and output-level bias. This study is significant because it challenges the assumption that privacy guarantees automatically improve fairness, showing that DP's impact on bias is task-dependent and requires multi-paradigm evaluation. The evaluation used DP-SGD to train a pretrained LLM and compared it against non-DP baselines across four paradigms: sentence scoring, text completion, tabular classification, and question answering.

rss · arXiv - NLP · May 13, 04:00

**Background**: Differential privacy (DP) is a framework that limits how much individual training data points can influence a model, often implemented via DP-SGD. Social bias in LLMs refers to systematic unfairness in model outputs based on attributes like gender or race. Logit-level bias refers to biases in the raw output scores before token selection, while output-level bias refers to biases in the final generated text.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.02617">[2206.02617] Individual Privacy Accounting for Differentially Private Stochastic Gradient Descent</a></li>
<li><a href="https://arxiv.org/pdf/2605.11195">How Does Differential Privacy Affect Social Bias in LLMs?</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/logit-bias">Logit Bias - LLM Parameter Guide - Vellum AI</a></li>

</ul>
</details>

**Tags**: `#differential privacy`, `#social bias`, `#LLMs`, `#fairness`, `#privacy`

---

<a id="item-28"></a>
## [Instructions Shape Production, Not Processing in LLMs](https://arxiv.org/abs/2605.11206) ⭐️ 8.0/10

A new study reveals that instructions in language models primarily influence output production rather than input processing, using probing and attention-based interventions across five binary judgment tasks. This finding challenges common assumptions about how instructions work in LLMs, suggesting that improving instruction-following may require focusing on the production stage rather than input encoding. The asymmetry was confirmed across model families and tasks, and it sharpens with model scale and instruction-tuning, which disproportionately affect the production stage.

rss · arXiv - NLP · May 13, 04:00

**Background**: Probing is a technique used to analyze internal representations of neural networks by training classifiers on hidden states. Attention-based interventions manipulate attention patterns to study causal effects on model behavior. This study applies these methods to understand how instructions influence language models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.01333">Probing Language Models for Pre-training Data Detection - arXiv</a></li>
<li><a href="https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and">Probing Classifiers: Promises, Shortcomings, and Advances</a></li>
<li><a href="https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition">Attention Mechanism in LLMs: An Intuitive Explanation</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#instruction-following`, `#cognitive science`, `#probing`, `#attention`

---

<a id="item-29"></a>
## [ReVision Cuts Visual Token Use by 46% for Computer Agents](https://arxiv.org/abs/2605.11212) ⭐️ 8.0/10

Researchers introduced ReVision, a method that reduces visual token usage by approximately 46% in computer-use agents by removing redundant patches across consecutive screenshots, while improving success rate by 3% on average across three benchmarks. This addresses a key bottleneck in computer-use agents—the high token cost of visual history—enabling longer trajectory processing under fixed budgets and revealing that past performance saturation was due to token inefficiency, not limited usefulness of history. ReVision uses a learned patch selector that compares patch representations across consecutive screenshots while preserving spatial structure, and was evaluated on OSWorld, WebTailBench, and AgentNetBench using Qwen2.5-VL-7B with 5 history screenshots.

rss · arXiv - NLP · May 13, 04:00

**Background**: Computer-use agents (CUAs) automate GUI interactions by processing screenshots as visual tokens in multimodal language models. As trajectories lengthen, token costs grow rapidly, limiting history integration. Previous work observed performance saturation when adding more history, but ReVision shows this was due to redundant tokens, not diminishing returns.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/daixiangzi/Awesome-Token-Compress">GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer - Using Agent | OpenAI</a></li>

</ul>
</details>

**Tags**: `#computer-use agents`, `#visual token reduction`, `#multimodal language models`, `#GUI automation`, `#efficiency`

---

<a id="item-30"></a>
## [Hebatron: Hebrew-Specialized MoE Language Model](https://arxiv.org/abs/2605.11255) ⭐️ 8.0/10

Researchers introduced Hebatron, the first open-weight Hebrew-specialized Mixture-of-Experts language model based on NVIDIA's Nemotron-3 architecture, achieving 73.8% Hebrew reasoning accuracy with only 3B active parameters. This work addresses the scarcity of high-quality Hebrew NLP resources and demonstrates that efficient MoE architectures can achieve competitive performance for low-resource languages, potentially lowering the barrier for other languages. The model uses a three-phase easy-to-hard curriculum with anti-forgetting anchoring, followed by SFT on 2M bilingual samples, and supports native context lengths up to 65,536 tokens with ~9x inference throughput compared to dense models.

rss · arXiv - NLP · May 13, 04:00

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling larger total capacity with similar computational cost. Nemotron-3 is NVIDIA's sparse MoE architecture combining Mamba and Transformer layers. Hebrew NLP has historically lacked large open models, with prior work like DictaLM and AlephBERT being smaller or dense.

<details><summary>References</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf">Nemotron 3 Super: Open, Efficient Mixture-of-Experts ...</a></li>
<li><a href="https://arxiv.org/abs/2309.14568">[2309.14568] Introducing DictaLM -- A Large Generative Language Model for Modern Hebrew</a></li>
<li><a href="https://arxiv.org/abs/2104.04052">[2104.04052] AlephBERT:A Hebrew Large Pre-Trained Language Model to Start-off your Hebrew NLP Application With</a></li>

</ul>
</details>

**Tags**: `#NLP`, `#Mixture-of-Experts`, `#Hebrew`, `#Language Model`, `#Efficient Inference`

---

<a id="item-31"></a>
## [ReAD: Reinforcement-Guided Capability Distillation for LLMs](https://arxiv.org/abs/2605.11290) ⭐️ 8.0/10

Researchers propose ReAD, a reinforcement-guided capability distillation framework that explicitly models cross-capability transfer to improve task-specific LLM compression under a fixed token budget. This work addresses a key limitation in existing capability distillation methods that treat capabilities independently, offering a more efficient and effective way to compress LLMs while preserving task-relevant abilities. ReAD uses an uncertainty-aware contextual bandit to adaptively allocate the distillation budget based on expected utility gains, and experiments show it reduces harmful spillover and wasted distillation effort compared to strong baselines.

rss · arXiv - NLP · May 13, 04:00

**Background**: Capability distillation applies knowledge distillation to selected model capabilities to compress a large language model into a smaller one while preserving needed abilities. However, existing methods often treat capabilities as independent and overlook cross-capability transfer, which can lead to suboptimal performance under a fixed token budget.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.14216">Understanding Accuracy and Capability in LLM Reasoning - arXiv</a></li>
<li><a href="https://nebius.com/blog/posts/concept-behind-distilling-llm">The concept behind distilling an LLM - Nebius</a></li>
<li><a href="https://iclr.cc/virtual/2026/poster/10006741">Knowledge Fusion of Large Language Models via Modular SkillPacks</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#knowledge distillation`, `#model compression`, `#reinforcement learning`, `#capability transfer`

---

<a id="item-32"></a>
## [HiDream-O1-Image: Unified Pixel-Space Diffusion Transformer](https://arxiv.org/abs/2605.11061) ⭐️ 8.0/10

HiDream-O1-Image introduces a natively unified pixel-space Diffusion Transformer that maps raw image pixels, text tokens, and task conditions into a single shared token space, eliminating the need for separate encoders or VAEs. This architecture represents a paradigm shift from modular to end-to-end visual generation, potentially simplifying model design and improving scalability; with only 8B parameters, it matches or surpasses larger models like 27B Qwen-Image, and a 200B+ version sets new state-of-the-art benchmarks. The model uses a Unified Transformer (UiT) architecture that treats diverse generation and editing tasks as in-context reasoning, and it has been scaled to over 200B parameters (HiDream-O1-Image-Pro) with superior performance.

rss · arXiv - Computer Vision · May 13, 04:00

**Background**: Traditional image generation models rely on separate text encoders (e.g., CLIP) and variational autoencoders (VAEs) to compress images into latent space, which introduces complexity and information loss. Pixel-space Diffusion Transformers operate directly on raw pixels, avoiding the need for such modular components. HiDream-O1-Image extends this by unifying all modalities into a single token space, enabling a truly end-to-end approach.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.20645">PixelDiT: Pixel Diffusion Transformers for Image Generation - arXiv</a></li>
<li><a href="https://pixeldit.github.io/">PixelDiT: Pixel Diffusion Transformers</a></li>

</ul>
</details>

**Tags**: `#image generation`, `#diffusion transformer`, `#unified architecture`, `#multimodal`, `#AI research`

---

<a id="item-33"></a>
## [Background-Invariant VLM Representations via Linear Structure](https://arxiv.org/abs/2605.11107) ⭐️ 8.0/10

A new pre-training method exploits the linear additivity of VLM embedding spaces to decompose scene representations into foreground and background components, achieving over 90% worst-group accuracy on Waterbirds under perfect spurious correlation. This work addresses a critical robustness issue in VLMs by providing a practical, data-efficient approach to remove background bias without requiring real-world debiased data, which could significantly improve VLM reliability in real-world deployment. The method uses synthetic data to construct background-invariant representations and demonstrates strong sim-to-real transfer. It achieves the first worst-group accuracy exceeding 90% on Waterbirds under 100% spurious correlation (no minority-group examples in training).

rss · arXiv - Computer Vision · May 13, 04:00

**Background**: Vision-language models (VLMs) like CLIP are known to suffer from spurious correlations, such as associating waterbirds with water backgrounds. The Waterbirds dataset is a benchmark for this issue, where the task is to classify birds as waterbirds or landbirds, but backgrounds are spuriously correlated with labels. Previous methods often require group annotations or debiased data, which are expensive to obtain.

<details><summary>References</summary>
<ul>
<li><a href="https://kempnerinstitute.harvard.edu/research/deeper-learning/interpreting-the-linear-structure-of-vision-language-model-embedding-spaces/">Interpreting the Linear Structure of Vision-Language Model Embedding Spaces - Kempner Institute</a></li>
<li><a href="https://arxiv.org/abs/2204.02070">Improving Worst-group Accuracy with Spurious Attribute Estimation - arXiv</a></li>
<li><a href="https://arxiv.org/pdf/2510.02818">Mitigating Spurious Correlation via Distributionally Robust Learning...</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#robustness`, `#spurious correlations`, `#representation learning`, `#CLIP`

---

<a id="item-34"></a>
## [Perspectivist Classifier Predicts Political Sentiment by Identity](https://arxiv.org/abs/2605.11166) ⭐️ 8.0/10

A new paper introduces the Perspectivist Visual Political Sentiment (PVPS) classifier, which learns from 82,000 evaluations by 5,575 U.S. adults to predict how different political and social identity groups evaluate the same image, preserving disagreement rather than averaging it away. This work challenges standard single-score approaches in computational social science by showing that political images convey different meanings to different audiences, with implications for political communication, AI fairness, and the validity of automated sentiment analysis. The PVPS classifier was applied to studies of protest imagery, revealing that perceived violence and emotional mechanisms change substantively when audience identity is considered. The model returns an evaluative profile recording who agrees, who diverges, and along which identity lines.

rss · arXiv - Computer Vision · May 13, 04:00

**Background**: Political and social identities strongly shape how people evaluate political information, a well-established finding in political science. However, most computational tools produce single sentiment scores, implicitly assuming that an image means the same thing to everyone. Perspectivism in AI aims to preserve multiple valid perspectives rather than forcing consensus.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2408.04103">[2408.04103] Decoding Visual Sentiment of Political Imagery</a></li>
<li><a href="https://arxiv.org/html/2405.05860v1">The Perspectivist Paradigm Shift: Assumptions and Challenges of Capturing Human Labels</a></li>

</ul>
</details>

**Tags**: `#computational social science`, `#political sentiment`, `#perspectivism`, `#AI fairness`, `#visual sentiment analysis`

---

<a id="item-35"></a>
## [ABRA: A New Benchmark for Radiology AI Agents](https://arxiv.org/abs/2605.11224) ⭐️ 8.0/10

ABRA is a new benchmark for radiology AI agents that requires them to navigate real DICOM environments using 21 function-calling tools, covering 655 tasks across three difficulty levels and eight task types. Unlike existing benchmarks that use pre-selected images, ABRA tests agents in a realistic clinical workflow, revealing that current models achieve high execution but low outcome scores due to perception bottlenecks. The benchmark uses OHIF Viewer and Orthanc DICOM server, with tasks including viewer control, metadata QA, annotation, and BI-RADS reporting; automatic scoring evaluates planning, execution, and outcome.

rss · arXiv - Computer Vision · May 13, 04:00

**Background**: Radiology AI agents are designed to assist radiologists by interacting with medical imaging systems. DICOM is the standard format for medical images, and tools like OHIF Viewer and Orthanc server are commonly used in clinical settings. BI-RADS is a standardized system for breast imaging reporting.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/OHIF/Viewers">GitHub - OHIF / Viewers : OHIF zero-footprint DICOM viewer and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orthanc_(server)">Orthanc (server) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI Benchmark`, `#Radiology`, `#Medical AI`, `#Agent`, `#DICOM`

---

<a id="item-36"></a>
## [Uniform Scaling Limits in AdamW-Trained Transformers](https://arxiv.org/abs/2605.11059) ⭐️ 8.0/10

A new paper proves that the hidden-state dynamics of transformers trained with AdamW converge uniformly to solutions of forward-backward ODEs, with explicit convergence rates depending on depth L and number of attention heads H. This provides the first rigorous theoretical analysis of transformer scaling limits under AdamW optimization, offering insights into how depth and attention heads affect training dynamics, which could guide architecture design and training practices. The convergence rate is O(L^{-1} + L^{-1/3} H^{-1/2}), and the limiting ODE system reduces to a McKean–Vlasov ODE when attention heads lack causal masking. The bounds are uniform over compact initial conditions and independent of token count and embedding dimension under AdamW adaptation.

rss · arXiv - Data Science & Statistics · May 13, 04:00

**Background**: Transformers are deep neural networks widely used in NLP and beyond, often trained with the AdamW optimizer. Understanding their behavior as depth increases is crucial for scaling models. This work models hidden states as an interacting particle system coupled via attention, a perspective that connects transformer dynamics to mean-field theories in physics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/McKean–Vlasov_process">McKean–Vlasov process - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2007.02876">arXiv:2007.02876v2 [stat.ML] 20 Jul 2020 A Mathematical Theory of Attention</a></li>
<li><a href="https://optimization.cbe.cornell.edu/index.php?title=AdamW">AdamW - Cornell University Computational Optimization Open Textbook - Optimization Wiki</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#deep learning theory`, `#optimization`, `#scaling limits`, `#attention mechanism`

---

<a id="item-37"></a>
## [Thompson Sampling for Adaptive Policy Under Unknown Network Interference](https://arxiv.org/abs/2605.11191) ⭐️ 8.0/10

This paper proposes a Thompson sampling algorithm that jointly learns the unknown interference network and optimizes individual-level treatment allocations in adaptive experiments using a Gibbs sampler. This work addresses a critical gap in adaptive experimentation by handling unknown network interference, which is common in social networks and online platforms, enabling more effective policy learning and causal inference. The algorithm achieves a Bayesian regret bound of order √(nT·B log(en/B)) for exact posterior sampling, and empirically reduces regret by over an order of magnitude compared to existing methods.

rss · arXiv - Data Science & Statistics · May 13, 04:00

**Background**: Adaptive experimentation (e.g., multi-armed bandits) sequentially allocates treatments to maximize cumulative reward, but standard methods assume no interference between units. In many real-world settings, such as social networks, a unit's outcome depends on neighbors' treatments, creating network interference. Existing approaches either assume the network is known or use coarse cluster-level randomization, which can be inefficient.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thompson_sampling">Thompson sampling - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gibbs_sampling">Gibbs sampling - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6935347/">Causal Inference Under Interference And Network Uncertainty - PMC</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#reinforcement learning`, `#network interference`, `#Thompson sampling`, `#adaptive experimentation`

---

<a id="item-38"></a>
## [Post-ADC Inference: Valid Inference After Active Data Collection](https://arxiv.org/abs/2605.11511) ⭐️ 8.0/10

A new framework called post-ADC inference is proposed to enable valid statistical inference when data is collected adaptively and the inferential target is chosen post-hoc. It provides valid p-values and confidence intervals that correct for biases from both active data collection and data-driven target construction. This addresses a fundamental issue in black-box optimization and sequential model-based optimization, where conventional inference fails due to adaptive sampling bias. The framework has broad applicability and does not require assumptions on the black-box function or surrogate model, making it practical for real-world use. The method builds on selective inference and imposes only assumptions on observation noise. Empirical results show valid inference for data collected by GP-UCB and TPE algorithms.

rss · arXiv - Data Science & Statistics · May 13, 04:00

**Background**: Active data collection (ADC) adaptively selects data points, often in black-box optimization, leading to biased samples. Post-hoc inference refers to statistical analyses specified after seeing the data, which can introduce additional bias. Sequential model-based optimization (SMBO) methods like TPE and GP-UCB concentrate evaluations in promising regions, exacerbating the bias.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post_hoc">Post hoc - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2603.08002v1">Post - Hoc Large-Sample Statistical Inference</a></li>
<li><a href="https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/11-LION5-SMAC.pdf">Sequential Model-Based Optimization for General Algorithm Conﬁguration</a></li>

</ul>
</details>

**Tags**: `#statistical inference`, `#active data collection`, `#black-box optimization`, `#sequential model-based optimization`

---

<a id="item-39"></a>
## [Minimax Rates and Spectral Distillation for Tree Ensembles](https://arxiv.org/abs/2605.11841) ⭐️ 8.0/10

This paper derives minimax-optimal convergence rates for random forest regression and introduces spectral distillation methods to compress tree ensembles while maintaining predictive performance. It provides the first minimax-optimal convergence result for random forests, bridging a gap in statistical learning theory, and offers practical compression techniques that can reduce model size by orders of magnitude for resource-constrained applications. The spectral viewpoint reveals that leading eigenfunctions of the kernel operator (for RFs) or singular vectors of the smoother matrix (for GBMs) capture dominant predictive directions, enabling distillation via nonlinear maps.

rss · arXiv - Data Science & Statistics · May 13, 04:00

**Background**: Tree ensembles like random forests and gradient boosting are widely used but lack complete theoretical understanding. Minimax optimality characterizes the best possible convergence rate under worst-case scenarios, and spectral methods analyze operators via eigenvalues and eigenvectors.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.11841">Minimax Rates and Spectral Distillation for Tree Ensembles - arXiv</a></li>
<li><a href="https://arxiv.org/html/2605.11841v1">Minimax Rates and Spectral Distillation for Tree Ensembles - arXiv</a></li>

</ul>
</details>

**Tags**: `#random forests`, `#gradient boosting`, `#spectral methods`, `#model compression`, `#statistical learning theory`

---

<a id="item-40"></a>
## [Anchor-Guided Variance-Aware Reward Modeling Resolves Non-Identifiability](https://arxiv.org/abs/2605.11865) ⭐️ 8.0/10

Researchers propose Anchor-guided Variance-aware Reward Modeling, a framework that resolves the non-identifiability issue in Gaussian reward models for pluralistic preferences by augmenting preference data with two coarse response-level anchor labels, and provide theoretical guarantees including a non-asymptotic convergence rate. This work addresses a fundamental limitation of Bradley-Terry reward models in pluralistic preference settings, enabling more accurate reward modeling and improved downstream RLHF performance, which is critical for aligning large language models with diverse human values. The method proves that two anchors are sufficient for identification, develops a joint training objective, and establishes a non-asymptotic convergence rate for both reward mean and variance functions. It consistently improves reward modeling and downstream RLHF (PPO and best-of-N selection) across simulations and four real-world datasets.

rss · arXiv - Data Science & Statistics · May 13, 04:00

**Background**: Standard Bradley-Terry reward models assume a single scalar reward per response, which fails to capture disagreement in pluralistic preferences. Gaussian reward models jointly predict mean and variance to express uncertainty, but suffer from non-identifiability: different parameter pairs can yield the same likelihood from pairwise preferences alone. This paper introduces anchor labels—coarse human judgments of response quality—to break this symmetry.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.11865">[2605.11865] Variance-aware Reward Modeling with Anchor Guidance</a></li>

</ul>
</details>

**Tags**: `#reward modeling`, `#preference learning`, `#RLHF`, `#pluralistic preferences`, `#machine learning`

---