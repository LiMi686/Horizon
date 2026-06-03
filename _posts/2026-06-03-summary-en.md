---
layout: default
title: "Horizon Summary: 2026-06-03 (EN)"
date: 2026-06-03
lang: en
---

> From 103 items, 40 important content pieces were selected

---

1. [Elixir v1.20 Introduces Gradual Typing](#item-1) ⭐️ 9.0/10
2. [Soundbar Hacked via Bluetooth to Emulate Keyboard](#item-2) ⭐️ 9.0/10
3. [Let's Encrypt Plans Post-Quantum Merkle Tree Certificates](#item-3) ⭐️ 9.0/10
4. [Exact Decomposition of Neural Network Curvature Exponent](#item-4) ⭐️ 9.0/10
5. [NVIDIA Cosmos 3: Omnimodal World Models for Physical AI](#item-5) ⭐️ 9.0/10
6. [Google Releases Gemma 4 12B, an Encoder-Free Multimodal Model](#item-6) ⭐️ 8.0/10
7. [DaVinci Resolve 21 Adds Photo Management and Motion Graphics](#item-7) ⭐️ 8.0/10
8. [Uber Caps AI Tool Spending at $1,500/Month per Tool](#item-8) ⭐️ 8.0/10
9. [Espressif Announces ESP32-S31 with RISC-V and Bitscrambler](#item-9) ⭐️ 8.0/10
10. [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](#item-10) ⭐️ 8.0/10
11. [Anthropic Launches Claude Code: Agentic Terminal Coding Tool](#item-11) ⭐️ 8.0/10
12. [Surya: Open-Source OCR Tool with 90+ Languages](#item-12) ⭐️ 8.0/10
13. [AURA-Mem: Constant Memory for Robot Policies](#item-13) ⭐️ 8.0/10
14. [BehaviorBench: Benchmark for Real-World User Decision Modeling](#item-14) ⭐️ 8.0/10
15. [ChatHealthAI Aligns EHR with LLMs for Clinical Reasoning](#item-15) ⭐️ 8.0/10
16. [Traj-Evolve: Self-Evolving Multi-Agent System for Lung Cancer Detection](#item-16) ⭐️ 8.0/10
17. [Thinking Past the Answer: Harmful Overthinking in LRMs](#item-17) ⭐️ 8.0/10
18. [Human-in-the-Loop Bandits for STR Dynamic Pricing](#item-18) ⭐️ 8.0/10
19. [Class-Split Anomaly Detection Benchmarks May Be Unstable](#item-19) ⭐️ 8.0/10
20. [ReLoRA: Efficiently Restoring LoRA Adapters for Evolving LLMs](#item-20) ⭐️ 8.0/10
21. [Geometry-Aware Tabular Diffusion Boosts Synthesis](#item-21) ⭐️ 8.0/10
22. [IdiomX: A Multilingual Benchmark for Idiom Understanding](#item-22) ⭐️ 8.0/10
23. [LLMs Found Greener Than Average Humans in New Benchmark](#item-23) ⭐️ 8.0/10
24. [Deep Layers May Not Need Context for Value Vectors](#item-24) ⭐️ 8.0/10
25. [Audit Reveals ~39% Errors in NL-to-FOL Benchmarks](#item-25) ⭐️ 8.0/10
26. [Economy of Minds: Emergent Collective Intelligence via Economic Interactions](#item-26) ⭐️ 8.0/10
27. [ALAR: Dual-Mode Reasoning for Efficient LLM Agents](#item-27) ⭐️ 8.0/10
28. [Linear Probes Detect Task Format, Not Reasoning Mode](#item-28) ⭐️ 8.0/10
29. [VLMs Consistent Yet Wrong: Weak Geometric Grounding Revealed](#item-29) ⭐️ 8.0/10
30. [MetaWorld: Scaling Multi-Agent Video World Models from Single-View Data](#item-30) ⭐️ 8.0/10
31. [GeoDrive-Bench: Benchmarking Region-Specific Driving VLMs](#item-31) ⭐️ 8.0/10
32. [Automated Pipeline for Oncology VQA Benchmark from Private Reports](#item-32) ⭐️ 8.0/10
33. [Prioritize Identifying Structure Over Complex Models for Science](#item-33) ⭐️ 8.0/10
34. [Periodic and Soft Target Updates Stabilize Linear Q-Learning](#item-34) ⭐️ 8.0/10
35. [TERA: Scalable Derivative Gaussian Processes via Exact Gradient Reduction](#item-35) ⭐️ 8.0/10
36. [Exact Formula for CoT Generalization Error Revealed](#item-36) ⭐️ 8.0/10
37. [Unifying Calibration Concepts Across Classification and Regression](#item-37) ⭐️ 8.0/10
38. [GLP-1 drugs linked to lower addiction and overdose risks](#item-38) ⭐️ 8.0/10
39. [Scientists Reverse Anxiety by Fixing a Tiny Brain Circuit](#item-39) ⭐️ 8.0/10
40. [Brain scans reveal two distinct autism subtypes](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Elixir v1.20 Introduces Gradual Typing](https://elixir-lang.org/blog/2026/06/03/elixir-v1-20-0-released/) ⭐️ 9.0/10

Elixir v1.20, released on June 3, 2026, introduces a gradual type system based on set-theoretic types, allowing developers to add optional type annotations and receive static type checking without breaking existing code. This marks a paradigm shift for Elixir, enhancing code reliability and developer productivity by catching type errors at compile time while preserving the dynamic flexibility that Elixir developers value. It positions Elixir as a more robust option for large-scale applications. The type system is sound, gradual, and uses semantic subtyping with a dynamic() type for seamless interoperability between typed and untyped code. It does not require changes to the compilation pipeline or runtime, and existing Dialyzer users can gradually migrate.

hackernews · cloud8421 · Jun 3, 19:02 · [Discussion](https://news.ycombinator.com/item?id=48388324)

**Background**: Gradual typing allows developers to mix static and dynamic typing within the same language, adding type annotations incrementally. Elixir's approach is based on set-theoretic types and strong arrows, aiming for soundness and practical static analysis without runtime overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://elixir-lang.org/blog/2023/09/20/strong-arrows-gradual-typing/">Strong arrows: a new approach to gradual typing - The Elixir programming language</a></li>
<li><a href="https://hexdocs.pm/elixir/main/gradual-set-theoretic-types.html">Gradual set-theoretic types — Elixir v1.20.0-rc.4</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gradual_typing">Gradual typing - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is largely positive, with long-time Elixir developers expressing excitement about the type system's potential. Some users compare it to Dialyzer and ask about performance implications, while others note that gradual typing in other languages can cause asymptotic slowdowns, though Elixir's design aims to avoid that.

**Tags**: `#Elixir`, `#gradual typing`, `#programming languages`, `#type systems`

---

<a id="item-2"></a>
## [Soundbar Hacked via Bluetooth to Emulate Keyboard](https://blog.nns.ee/2026/06/03/katana-badusb/) ⭐️ 9.0/10

A researcher exploited a Bluetooth firmware update vulnerability in the Creative Sound Blaster Katana V2X soundbar to wirelessly flash malicious firmware, turning it into a USB keyboard that can execute arbitrary keystrokes on the connected PC. This demonstrates a novel attack vector where a peripheral device can be compromised via Bluetooth without pairing, highlighting serious security negligence by vendors and the potential for widespread supply chain attacks. The attack requires no user interaction or authentication; the researcher also released a third-party patch after Creative dismissed the issue as not a cybersecurity risk. The soundbar's firmware update process over Bluetooth lacked encryption or signing.

hackernews · xx_ns · Jun 3, 10:53 · [Discussion](https://news.ycombinator.com/item?id=48382310)

**Background**: Many USB devices can be reprogrammed to act as a different device class, such as a keyboard, a technique known as BadUSB. Bluetooth firmware updates often lack proper security measures, allowing attackers to inject malicious code if they can connect to the device. The Creative Sound Blaster Katana V2X is a gaming soundbar that connects to a PC via USB and can receive firmware updates over Bluetooth.

<details><summary>References</summary>
<ul>
<li><a href="https://support.creative.com/Products/ProductDetails.aspx?prodID=23937&prodName=Sound+Blaster+Katana+V2X">Creative Worldwide Support - Sound Blaster Katana V2X</a></li>
<li><a href="https://blog.nns.ee/2026/02/20/katana-v2x-re/">Reverse engineering the Creative Katana V2X soundbar to be able to control it from Linux | nns.ee</a></li>

</ul>
</details>

**Discussion**: Commenters expressed outrage at Creative's dismissal of the vulnerability, with some suggesting the attack could be automated into a worm targeting supply chains. Others praised the researcher's thorough work and the release of a third-party patch.

**Tags**: `#security`, `#bluetooth`, `#firmware`, `#vulnerability`, `#hardware hacking`

---

<a id="item-3"></a>
## [Let's Encrypt Plans Post-Quantum Merkle Tree Certificates](https://letsencrypt.org/2026/06/03/pq-certs) ⭐️ 9.0/10

Let's Encrypt announced plans to adopt Merkle Tree Certificates (MTCs) for post-quantum security, marking a major step toward quantum-resistant TLS. This shift addresses the looming threat of quantum computers breaking current public-key cryptography, ensuring long-term security for HTTPS connections. MTCs also integrate transparency into issuance, improving the Web PKI ecosystem. MTCs reduce handshake size by combining a single signature, public key, and inclusion proof, making them smaller than today's Web PKI handshake even with post-quantum algorithms. Each certificate is part of a published Merkle tree, making transparency a property of issuance itself.

hackernews · SGran · Jun 3, 15:06 · [Discussion](https://news.ycombinator.com/item?id=48385114)

**Background**: Post-quantum cryptography (PQC) aims to develop algorithms secure against quantum computer attacks. NIST has standardized several PQC algorithms, but they often have larger key and signature sizes, posing challenges for TLS. Merkle Tree Certificates (MTCs) are a new certificate format designed to efficiently support PQC in TLS by reducing overhead and integrating logging.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ietf.org/archive/id/draft-davidben-tls-merkle-tree-certs-06.html">Merkle Tree Certificates - ietf.org</a></li>
<li><a href="https://blog.cloudflare.com/bootstrap-mtc/">Keeping the Internet fast and secure- introducing Merkle Tree ...</a></li>

</ul>
</details>

**Discussion**: Commenters expressed a mix of excitement and caution, noting that while MTCs streamline decades of cruft, they also lose battle-tested tooling. Some raised concerns about current choices like ed25519 not being quantum-resistant, while others shared resources on hybrid constructions to ease the transition.

**Tags**: `#post-quantum cryptography`, `#TLS`, `#Let's Encrypt`, `#web security`, `#Merkle Tree Certificates`

---

<a id="item-4"></a>
## [Exact Decomposition of Neural Network Curvature Exponent](https://arxiv.org/abs/2606.02596) ⭐️ 9.0/10

A new paper proves the Spectral Alignment Decomposition, which exactly explains why the curvature exponent α varies across layer types (e.g., α≈2 for convolutions, ≈1 for attention). It also derives a spectral transfer identity s=αγ that predicts Hessian decay exponent s from independent measurements with ~2% median error. This theoretical breakthrough provides a unified geometric understanding of loss landscape curvature across architectures, enabling architecture-adaptive preconditioners like Spectral Newton that outperform AdamW on vision tasks. It bridges a gap between empirical observations and rigorous theory in deep learning. The decomposition α = 2 + d log Φ_k / d log σ_k reduces the variation of α to a geometric alignment measure Φ_k between Kronecker factor eigenbases and gradient singular directions. The spectral transfer identity s=αγ is algebraic and validated across 93 layers, five architectures, and three datasets with no free parameters.

rss · arXiv - Machine Learning · Jun 3, 04:00

**Background**: The Hessian matrix of the loss function governs optimization dynamics; its eigenvalue spectrum often follows power laws. The curvature exponent α describes how Hessian eigenvalues scale with gradient singular values, and was known to vary across layers but lacked a theoretical explanation. This work provides the first exact decomposition.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.02596">Spectral Asymptotics of Neural Network Loss Landscapes: An Exact...</a></li>

</ul>
</details>

**Tags**: `#deep learning theory`, `#loss landscape`, `#hessian`, `#spectral analysis`, `#neural networks`

---

<a id="item-5"></a>
## [NVIDIA Cosmos 3: Omnimodal World Models for Physical AI](https://arxiv.org/abs/2606.02800) ⭐️ 9.0/10

NVIDIA released Cosmos 3, a family of omnimodal world models that jointly process and generate language, images, video, audio, and action sequences using a unified mixture-of-transformers architecture. The models achieve state-of-the-art results across multiple understanding and generation tasks, and were ranked as the best open-source text-to-image and image-to-video models by Artificial Analysis, and the best policy model by RoboArena. Cosmos 3 unifies critical modalities for Physical AI into a single framework, subsuming vision-language models, video generators, world simulators, and world-action models. This breakthrough could accelerate the development of embodied agents and autonomous machines that perceive, understand, and act in the real world. The model uses a mixture-of-transformers (MoT) architecture that decouples parameters by modality, reducing pretraining computational costs. NVIDIA has released code, model checkpoints, curated synthetic datasets, and evaluation benchmarks under the Linux Foundation's OpenMDW-1.1 license.

rss · arXiv - Computer Vision · Jun 3, 04:00

**Background**: World models are AI systems that learn an internal representation of the environment, enabling them to simulate and predict future states. Physical AI refers to AI systems that can perceive, understand, and perform actions in the physical world, such as robots and autonomous vehicles. The mixture-of-transformers architecture is a sparse multi-modal transformer design that separates parameters by modality to improve scalability and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02800">[2606.02800] Cosmos 3: Omnimodal World Models for Physical AI</a></li>
<li><a href="https://github.com/nvidia/Cosmos">NVIDIA/cosmos: NVIDIA Cosmos is an open platform of world models ...</a></li>
<li><a href="https://arxiv.org/abs/2411.04996">[2411.04996] Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models</a></li>

</ul>
</details>

**Tags**: `#world models`, `#multimodal AI`, `#Physical AI`, `#mixture-of-transformers`, `#embodied agents`

---

<a id="item-6"></a>
## [Google Releases Gemma 4 12B, an Encoder-Free Multimodal Model](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12b/) ⭐️ 8.0/10

Google has released Gemma 4 12B, a 12-billion-parameter multimodal model that replaces traditional vision encoders with a lightweight embedding module consisting of a single matrix multiplication, positional embedding, and normalizations. This encoder-free architecture allows the model to process images and audio directly without separate encoders, reducing latency and memory usage. This model brings high-performance multimodal intelligence to laptops with 16GB of VRAM, achieving performance approaching 26B models with less than half the memory. The encoder-free design could set a new trend in multimodal AI by simplifying architecture and improving efficiency for edge deployment. The model is available in 5 parameter sizes: E2B, E4B, 12B, 31B, and 26B A4B, with default 16-bit precision. Community benchmarks show decent performance on coding tasks, though some users reported minor syntax errors in generated code.

hackernews · rvz · Jun 3, 16:04 · [Discussion](https://news.ycombinator.com/item?id=48385906)

**Background**: Traditional multimodal models use separate encoders (e.g., SigLIP for vision) to convert images and audio into representations that the language model can process. These encoders add latency and memory overhead. Gemma 4 12B's encoder-free approach integrates multimodal inputs directly into the LLM backbone, making it more efficient for resource-constrained environments like laptops.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/">Introducing Gemma 4 12B - The Keyword</a></li>
<li><a href="https://note.com/zephel01/n/n09bf0bf3405d?hl=en">Gemma 4 12B In-Depth: A New Model Bringing Full-Scale ...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/core">Gemma 4 model overview - Google AI for Developers</a></li>

</ul>
</details>

**Discussion**: The community is actively discussing the encoder-free design, with some users questioning whether the lightweight embedding module is truly 'encoder-free' or just a different form of encoding. Others are excited about the model's efficiency and potential for agentic browsing on platforms like Cerebras. There is also debate about optimal quantization levels, as the model was benchmarked at 16-bit but users are experimenting with Q4 quantizations.

**Tags**: `#multimodal`, `#Google`, `#Gemma`, `#encoder-free`, `#AI`

---

<a id="item-7"></a>
## [DaVinci Resolve 21 Adds Photo Management and Motion Graphics](https://www.blackmagicdesign.com/products/davinciresolve/whatsnew) ⭐️ 8.0/10

Blackmagic Design released DaVinci Resolve 21 at NAB 2026, introducing a new Photo page with Hollywood-grade color tools and seven AI-powered features including media search by content, slate data reading, de-aging, and blemish removal. The update also brings enhanced keyframing, greater graphic format support, and a revamped Fairlight workflow. This update positions DaVinci Resolve as a direct competitor to Adobe Lightroom and After Effects, offering a unified tool for video editing, photo management, and motion graphics. For Linux users, it may become the best photo management and editing option available, challenging existing tools like Darktable and RawTherapee. The Photo page brings advanced color grading tools from the video side to still photography, while the AI features include object removal, face refinement, and automatic metadata extraction. The motion graphics enhancements aim to undercut basic After Effects workflows, though some polish may still be needed before replacing subscriptions.

hackernews · pentagrama · Jun 3, 14:18 · [Discussion](https://news.ycombinator.com/item?id=48384482)

**Background**: DaVinci Resolve is a professional non-linear video editing, color correction, visual effects, and audio post-production application developed by Blackmagic Design. It is known for its high-end color grading capabilities and is available on macOS, Windows, iPadOS, and Linux. The software offers a free version with extensive features and a Studio version for $295.

<details><summary>References</summary>
<ul>
<li><a href="https://www.blackmagicdesign.com/products/davinciresolve/whatsnew">DaVinci Resolve – What’s New | Blackmagic Design</a></li>
<li><a href="https://www.coremicro.com/blogs/news/davinci-resolve-21-new-features-explained">DaVinci Resolve 21: Every Major New Feature, Explained (2026)</a></li>
<li><a href="https://en.wikipedia.org/wiki/DaVinci_Resolve">DaVinci Resolve - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members praised the update, with one user calling it a potential Lightroom replacement on Linux and another noting the motion graphics features could undercut basic After Effects use. Some users expressed frustration with GPU requirements on Linux, while others defended the AI features as valuable workflow improvements.

**Tags**: `#video editing`, `#photo management`, `#motion graphics`, `#Blackmagic Design`, `#Linux`

---

<a id="item-8"></a>
## [Uber Caps AI Tool Spending at $1,500/Month per Tool](https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything) ⭐️ 8.0/10

Uber has capped employee spending on AI coding tools like Claude Code and Cursor at $1,500 per month per tool, after blowing its 2026 AI budget in just four months. This highlights the real cost challenges of widespread coding agent adoption, and sets a precedent for how enterprises may manage AI tool budgets going forward. The cap applies only to agentic coding software, not other AI tools. At $1,500 per tool per engineer, the annual cap per engineer (assuming two tools) is $36,000, roughly 11% of Uber's median software engineer compensation of $330,000.

rss · Simon Willison · Jun 3, 12:01 · [Discussion](https://news.ycombinator.com/item?id=48383056)

**Background**: AI coding agents like Claude Code and Cursor can autonomously write and edit code, but they consume large amounts of tokens, leading to high API costs. Uber's budget was set in 2025 before the rapid adoption of such tools, causing overspending.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.datacamp.com/blog/best-agentic-ide">The 13 Best Agentic IDEs in 2026 - DataCamp</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether the cap is reasonable, with some noting that fully-loaded engineer costs are higher than compensation, making the cap a smaller percentage. Others questioned whether AI providers will lower prices due to competition from Chinese models like DeepSeek.

**Tags**: `#AI`, `#cost management`, `#software engineering`, `#industry news`

---

<a id="item-9"></a>
## [Espressif Announces ESP32-S31 with RISC-V and Bitscrambler](https://www.espressif.com/en/products/socs/esp32-s31) ⭐️ 8.0/10

Espressif has announced the ESP32-S31, a new SoC featuring RISC-V cores with SIMD instructions and a Bitscrambler peripheral for flexible I/O data transformation. This chip strengthens Espressif's RISC-V ecosystem, offering developers a modern, open-architecture alternative to proprietary cores, and the Bitscrambler enables efficient custom protocol handling similar to Raspberry Pi Pico's PIO. The Bitscrambler is a programmable DMA stream processor that can transform data formats on the fly, and the RISC-V cores include SIMD extensions for accelerated signal processing. The chip is expected to target IoT and embedded applications requiring high I/O flexibility.

hackernews · volemo · Jun 3, 16:10 · [Discussion](https://news.ycombinator.com/item?id=48385965)

**Background**: Espressif's ESP32 series has been widely used in IoT and embedded projects. The shift to RISC-V cores reduces reliance on proprietary architectures like Xtensa, enabling easier use of open-source toolchains and languages like Rust. The Bitscrambler peripheral, first introduced in the ESP32-P4, allows custom data manipulation without CPU intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.espressif.com/projects/esp-idf/en/latest/esp32p4/api-reference/peripherals/bitscrambler.html">BitScrambler Driver - ESP32-P4 - — ESP-IDF Programming Guide ...</a></li>
<li><a href="https://github.com/espressif/esp-idf/tree/master/examples/peripherals/bitscrambler">esp-idf/examples/peripherals/bitscrambler at master ... - GitHub</a></li>

</ul>
</details>

**Discussion**: The community is excited about the RISC-V cores and SIMD instructions, noting that it simplifies toolchain setup for Rust development. Some users express confusion over the naming, as many different chips are all called 'ESP32', leading to potential misunderstandings about features and architectures.

**Tags**: `#ESP32`, `#RISC-V`, `#embedded systems`, `#Espressif`, `#SoC`

---

<a id="item-10"></a>
## [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](https://github.com/OpenBMB/VoxCPM) ⭐️ 8.0/10

OpenBMB has released VoxCPM2, a tokenizer-free text-to-speech model with 2 billion parameters trained on over 2 million hours of multilingual speech data, supporting 30 languages, voice design, controllable voice cloning, and 48kHz audio output. VoxCPM2 advances speech synthesis by eliminating discrete tokenization, enabling more natural and expressive speech generation. Its voice design and cloning capabilities from natural language descriptions or short audio clips open new possibilities for creative applications and personalized voice interfaces. VoxCPM2 is built on the MiniCPM-4 backbone and uses a diffusion autoregressive architecture to directly generate continuous speech representations. It supports ultimate cloning that preserves timbre, rhythm, emotion, and style when both reference audio and transcript are provided.

rss · GitHub Trending - Daily (All) · Jun 3, 23:28

**Background**: Traditional TTS systems often use discrete tokenization (e.g., converting audio into tokens) which can lose subtle acoustic details. Tokenizer-free models like VoxCPM2 model speech directly in a continuous latent space, preserving more naturalness and expressiveness. VoxCPM2 is the successor to VoxCPM1.5, with expanded language support and higher audio quality.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/OpenBMB/VoxCPM">GitHub - OpenBMB/VoxCPM: VoxCPM2: Tokenizer - Free TTS for...</a></li>
<li><a href="https://voxcpm.net/">VoxCPM: Tokenizer - Free TTS & Zero-Shot Voice Cloning</a></li>
<li><a href="https://voxcpm2.org/">VoxCPM2 - Advanced AI Voice Generation & Cloning</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#speech synthesis`, `#multilingual`, `#AI`, `#open source`

---

<a id="item-11"></a>
## [Anthropic Launches Claude Code: Agentic Terminal Coding Tool](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic has released Claude Code, an agentic coding tool that operates directly in the terminal, understands codebases, and executes tasks via natural language commands. It is available for macOS, Linux, and Windows via multiple installation methods. Claude Code brings advanced AI-assisted development to the terminal, enabling developers to automate routine tasks, explain complex code, and manage git workflows without leaving their command line. This could significantly boost developer productivity and streamline coding workflows. Claude Code can be installed via curl, Homebrew, WinGet, or PowerShell scripts, with npm installation now deprecated. It also supports plugins to extend functionality and integrates with GitHub via @claude mentions.

rss · GitHub Trending - Python · Jun 3, 23:28

**Background**: Agentic coding tools are AI-powered assistants that can autonomously perform coding tasks, such as editing files, running commands, and debugging, based on natural language instructions. Unlike traditional code completion tools, they understand the entire codebase and can execute multi-step workflows. Claude Code is Anthropic's entry into this growing category, competing with tools like Cursor and Cline.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">anthropics/ claude - code : Claude Code is an agentic coding tool that...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code">Claude Code Tutorial: Setup and Refactoring in Practice | DataCamp</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#developer tools`, `#Anthropic`, `#terminal`, `#agentic coding`

---

<a id="item-12"></a>
## [Surya: Open-Source OCR Tool with 90+ Languages](https://github.com/datalab-to/surya) ⭐️ 8.0/10

Datalab released Surya, a 650M parameter OCR model that achieves 83.3% accuracy on olmOCR-bench and supports 90+ languages for layout analysis, reading order, and table recognition. Surya provides a state-of-the-art, open-source alternative to commercial OCR services, making high-quality document intelligence accessible to developers and researchers worldwide. The model achieves a throughput of 5 pages per second on an RTX 5090 and scores 87.2% on an internal multilingual benchmark. It is licensed under Apache 2.0 for code and OpenRAIL-M for models.

rss · GitHub Trending - Python · Jun 3, 23:28

**Background**: OCR (Optical Character Recognition) converts images of text into machine-readable text. Document layout analysis identifies regions like text blocks, tables, and figures, while reading order arranges them logically. Surya combines these tasks in a single toolkit.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/xinqiyang/suryaocr">GitHub - xinqiyang/suryaocr: Accurate line-level text detection and...</a></li>
<li><a href="https://huggingface.co/pitapo/surya">pitapo/ surya · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Document_layout_analysis">Document layout analysis</a></li>

</ul>
</details>

**Tags**: `#OCR`, `#Document Intelligence`, `#Machine Learning`, `#Open Source`, `#Python`

---

<a id="item-13"></a>
## [AURA-Mem: Constant Memory for Robot Policies](https://arxiv.org/abs/2606.02775) ⭐️ 8.0/10

Researchers propose AURA-Mem, a constant-size recurrent memory with a learned action-gated write policy for robot policies, reducing VRAM usage to 4,224 bytes regardless of episode length, compared to KV-cache which grows 6,061 times larger at 100,000 steps. This addresses a critical memory bottleneck for deploying embodied AI on edge devices, enabling long-running robot episodes without high-bandwidth memory or flash wear concerns, potentially accelerating real-world robotics applications. The gate is trained directly against a closed-loop action-error signal, not reconstruction loss, and on LIBERO-Long benchmarks, AURA-Mem matches the base policy success rate (0.233) while using 7.0 times fewer writes and constant memory.

rss · arXiv - AI · Jun 3, 04:00

**Background**: Vision-Language-Action (VLA) models integrate vision, language, and action for robot control, but their KV-cache memory grows linearly with episode length, making them unsuitable for long-horizon tasks on edge hardware. AURA-Mem replaces this with a fixed-size recurrent memory that only writes when the observation would change the next action, drastically reducing memory and write operations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02775">AURA: Action - Gated Memory for Robot Policies at Constant VRAM</a></li>
<li><a href="https://grokipedia.com/page/KV_cache">KV cache</a></li>
<li><a href="https://vla-survey.github.io/">Vision - Language - Action Models for Robotics: A Review Towards...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#memory management`, `#edge AI`, `#reinforcement learning`, `#VLA`

---

<a id="item-14"></a>
## [BehaviorBench: Benchmark for Real-World User Decision Modeling](https://arxiv.org/abs/2606.02798) ⭐️ 8.0/10

Researchers introduced BehaviorBench, a benchmark for evaluating personalized decision modeling using real-world behavioral traces from prediction markets and on-chain records, comprising 141,445 Belief instances and 1,485,972 Trade instances across 2,000 wallets. This benchmark addresses the limitation of simulated data in user modeling, providing a realistic evaluation setting that can improve AI systems for personalized decision support in finance, marketing, and beyond. The benchmark includes two task layers: Belief prediction (predicting a user's final stance and confidence) and Trade prediction (predicting transaction direction and amount), with four history interfaces for evaluation.

rss · arXiv - AI · Jun 3, 04:00

**Background**: Many AI systems for user modeling rely on simulated or model-generated behavior, which can diverge from real human behavior. BehaviorBench uses real public behavioral traces from prediction markets (like Polymarket) and on-chain records, offering a more authentic testbed for personalized decision modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02798">BehaviorBench : Modeling Real-World User Decisions from Behavioral...</a></li>
<li><a href="https://polymarket.com/dashboards/fed-rates">Polymarket | The World's Largest Prediction Market</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#user modeling`, `#decision-making`, `#behavioral traces`, `#AI`

---

<a id="item-15"></a>
## [ChatHealthAI Aligns EHR with LLMs for Clinical Reasoning](https://arxiv.org/abs/2606.02802) ⭐️ 8.0/10

Researchers propose ChatHealthAI, a multimodal framework that aligns structured EHR representations from a pretrained foundation model with a frozen LLM via a task-aware resampler, enabling grounded clinical reasoning while preserving predictive accuracy. This work bridges a critical gap between predictive EHR models and interpretable LLMs, offering a path toward clinically trustworthy AI that can reason about patient data in natural language without sacrificing performance. ChatHealthAI was evaluated on three clinical predictive tasks from the EHRSHOT benchmark, showing improved reasoning quality and interpretability while maintaining competitive predictive performance. The framework uses a task-aware resampler to align longitudinal patient representations with the LLM's semantic space.

rss · arXiv - AI · Jun 3, 04:00

**Background**: Large language models (LLMs) excel at natural-language reasoning but struggle with structured longitudinal electronic health records (EHRs). Conversely, EHR foundation models learn predictive patient representations but lack interpretable language-based reasoning. ChatHealthAI combines both by aligning structured EHR representations with a frozen LLM through a task-aware resampler, enabling grounded clinical reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://som-shahlab.github.io/ehrshot-website/docs/intro/benchmark/">Benchmark | EHRSHOT</a></li>
<li><a href="https://github.com/som-shahlab/ehrshot-benchmark">GitHub - som-shahlab/ ehrshot - benchmark : A benchmark for...</a></li>

</ul>
</details>

**Tags**: `#large language models`, `#electronic health records`, `#clinical reasoning`, `#multimodal learning`, `#healthcare AI`

---

<a id="item-16"></a>
## [Traj-Evolve: Self-Evolving Multi-Agent System for Lung Cancer Detection](https://arxiv.org/abs/2606.02812) ⭐️ 8.0/10

Traj-Evolve introduces a self-evolving multi-agent system that combines an experience pool (ExPool) with multi-agent reinforcement learning (MARL) to model patient trajectories from electronic health records for lung cancer early detection. This approach outperforms nine strong baselines on lung cancer prediction, including for never-smokers, and addresses a key limitation of existing LLM-based systems by enabling agents to learn from accumulated experience of similar prior cases. The ExPool acts as a non-parametric memory storing rejection-sampled reasoning traces, while MARL via reward-ranked fine-tuning optimizes inter-agent and agent-memory collaboration. A leave-one-out cross-retrieval strategy unifies the two mechanisms.

rss · arXiv - AI · Jun 3, 04:00

**Background**: Patient trajectory modeling from longitudinal EHRs involves reasoning over sparse, noisy, and long-context multimodal sequences. Existing LLM-based multi-agent systems process patients in isolation, unlike clinicians who leverage experience from similar prior cases. Traj-Evolve addresses this by incorporating a self-evolving memory and reinforcement learning.

<details><summary>References</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/41624295/">A Multi - Agent Reinforcement Learning Framework for Public Health ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s44443-026-00825-0">ER-MedRAG: A multi - agent reinforcement learning framework for...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#healthcare AI`, `#reinforcement learning`, `#patient trajectory modeling`, `#lung cancer`

---

<a id="item-17"></a>
## [Thinking Past the Answer: Harmful Overthinking in LRMs](https://arxiv.org/abs/2606.02835) ⭐️ 8.0/10

This paper introduces a prefix-level trajectory evaluation protocol to distinguish between redundant (verbose) and harmful overthinking in large reasoning models after they have reached the correct answer. The research reveals that stopping at the first correct prefix can improve accuracy by up to 21%, challenging the assumption that more reasoning is always better and highlighting a critical reliability risk in current models. The protocol defines reasoning sufficiency as the minimum budget needed to first generate the correct answer, and finds that many reasoning-intensive benchmarks require surprisingly little reasoning. Failure analysis shows correctness deviations are mainly due to logical drift and visual reinterpretation.

rss · arXiv - AI · Jun 3, 04:00

**Background**: Large Reasoning Models (LRMs) improve performance by generating explicit intermediate reasoning traces through increased test-time compute. However, the assumption that longer reasoning is consistently beneficial has been under-examined. This paper introduces a method to evaluate the dynamics after a model has reached the correct answer, distinguishing between harmless verbose overthinking and harmful overthinking that destabilizes the trajectory.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/trajectory-level-metrics">Trajectory - Level Metrics Overview</a></li>
<li><a href="https://www.emergentmind.com/topics/sufficiency-of-reasoning-sr">Sufficiency of Reasoning (SR) - emergentmind.com</a></li>
<li><a href="https://kiankyars.github.io/machine_learning/2025/07/24/ttc.html">Test Time Compute | kiankyars</a></li>

</ul>
</details>

**Tags**: `#large reasoning models`, `#overthinking`, `#evaluation protocol`, `#test-time compute`, `#AI safety`

---

<a id="item-18"></a>
## [Human-in-the-Loop Bandits for STR Dynamic Pricing](https://arxiv.org/abs/2606.02595) ⭐️ 8.0/10

The paper introduces the Human-in-the-Loop Gated Bandit (HITL-GB) framework, which uses historical pricing data as structurally equivalent to on-policy warm-up, reducing cold-start from ~150 to ~30 episodes in short-term rental pricing. This framework addresses a critical practical challenge in dynamic pricing for short-term rentals, where pure online learning is impractical due to sparse feedback and high financial risk, and it shows that mandatory human oversight can be a statistical asset rather than a constraint. The warm-up procedure uses regularized ridge regression on historical episodes, and the framework is validated on real STR production data (2 rooms, 1,461 nightly episodes from April 2022 to April 2026). The structural equivalence result is claimed to be domain-agnostic, applicable to clinical drug dosing, credit origination, content moderation, and radiological diagnosis.

rss · arXiv - Machine Learning · Jun 3, 04:00

**Background**: Contextual bandits are a class of online learning algorithms that balance exploration and exploitation by selecting actions based on context. In dynamic pricing, a bandit algorithm recommends prices to maximize revenue, but cold-start occurs when the algorithm lacks initial data. Human-in-the-loop (HITL) systems involve human oversight of algorithmic decisions, which is common in high-stakes domains.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Contextual_bandit_algorithm">Contextual bandit algorithm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://vinija.ai/recsys/multi-armed-bandit+copy/">Vinija's Notes • Recommendation Systems • Multi-Armed Bandits</a></li>

</ul>
</details>

**Tags**: `#contextual bandits`, `#dynamic pricing`, `#human-in-the-loop`, `#online learning`, `#short-term rental`

---

<a id="item-19"></a>
## [Class-Split Anomaly Detection Benchmarks May Be Unstable](https://arxiv.org/abs/2606.02601) ⭐️ 8.0/10

A new paper reveals that class-split anomaly detection benchmarks can become ill-posed when the held-out anomaly class overlaps the normal mixture in representation space, causing score-direction instability. The authors propose a training-free diagnostic called neighborhood class leakage to detect such instability. This finding challenges the reliability of widely used class-split evaluation protocols in anomaly detection, potentially affecting how researchers interpret benchmark results. The proposed diagnostic provides a simple tool to assess benchmark validity, improving the rigor of future anomaly detection research. The study demonstrates score-direction instability across Fashion-MNIST, CIFAR-10, and Imagenette datasets, in both pixel and VAE latent spaces. The neighborhood class leakage diagnostic predicts this instability without requiring model training.

rss · arXiv - Machine Learning · Jun 3, 04:00

**Background**: Anomaly detection aims to identify data points that deviate from a normal distribution. Class-split evaluation is a common benchmark protocol where one class is held out as anomalies and the rest as normal, but this paper shows it can be unreliable when representation overlap occurs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02601">[2606.02601] Testing the Test: Score - Direction Instability in...</a></li>
<li><a href="https://arxiv.org/html/2606.02601">Testing the Test: Score - Direction Instability in Class-Split Anomaly ...</a></li>

</ul>
</details>

**Tags**: `#anomaly detection`, `#evaluation protocol`, `#representation learning`, `#benchmarking`, `#machine learning`

---

<a id="item-20"></a>
## [ReLoRA: Efficiently Restoring LoRA Adapters for Evolving LLMs](https://arxiv.org/abs/2606.02606) ⭐️ 8.0/10

ReLoRA proposes a knowledge-reusing re-adaptation framework that restores LoRA adapters for evolving LLM services without retraining from scratch, achieving up to 8.9× faster time-to-readiness and up to 4.6% accuracy improvement over baselines. This addresses a critical practical problem for LLM service providers: frequent base-model updates invalidate existing LoRA adapters, and retraining all adapters from scratch is computationally prohibitive. ReLoRA enables rapid service recovery, reducing downtime and computational costs, which is essential for scalable LLM deployment. ReLoRA consists of two steps: adaptive LoRA initialization using Bayesian optimization to fuse information from the old adapter and base model evolution, and fine-tuning with scheduled regularization that starts strong and then relaxes for task-specific refinement. Experiments show ReLoRA reduces time-to-readiness by up to 8.9× and improves accuracy by up to 4.6%.

rss · arXiv - Machine Learning · Jun 3, 04:00

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that adds small trainable matrices to a frozen base model, enabling task-specific adaptation without retraining all parameters. When the base LLM is updated (e.g., to a new version), previously trained LoRA adapters may not work well due to incompatibility with the new backbone. Retraining all adapters from scratch is expensive, and simply reusing old adapters degrades performance.

<details><summary>References</summary>
<ul>
<li><a href="https://openinnovation.ai/lora-adapters-explained-efficient-fine-tuning-for-llms-without-retraining/">LoRA Adapters Explained - openinnovation.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_optimization">Bayesian optimization - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#LoRA`, `#fine-tuning`, `#model adaptation`, `#efficiency`

---

<a id="item-21"></a>
## [Geometry-Aware Tabular Diffusion Boosts Synthesis](https://arxiv.org/abs/2606.02607) ⭐️ 8.0/10

Researchers introduce Geometry-Aware Tabular Diffusion (GATD), which augments tabular diffusion denoisers with pairwise column geometry (angles and lengths) as inputs and auxiliary targets, achieving state-of-the-art results with 3.5x fewer parameters on average. This work demonstrates that explicit relational supervision is a portable inductive bias for tabular diffusion, significantly improving synthesis quality and efficiency, which is crucial for privacy-preserving data sharing and augmentation in domains like healthcare and finance. On ten datasets, GATD wins 8/10 Shape, 7/10 Trend, and 9/10 downstream utility (F1/RMSE), reducing Shape and Trend error by 27% and 20%. The default loss weights transfer to GNN and Transformer denoisers, improving Shape on 27/30 and Trend on 25/30 architecture-dataset cells.

rss · arXiv - Machine Learning · Jun 3, 04:00

**Background**: Tabular data synthesis aims to generate realistic synthetic tables while preserving privacy. Diffusion models have been adapted for tabular data, but they typically rely on implicit mechanisms to capture inter-column relationships. GATD explicitly incorporates pairwise column geometry to provide stronger inductive bias.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02607">Geometry - Aware Tabular Diffusion</a></li>
<li><a href="https://arxiv.org/html/2606.02607v1">Geometry-Aware Tabular Diffusion - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#tabular data`, `#diffusion models`, `#data synthesis`, `#machine learning`

---

<a id="item-22"></a>
## [IdiomX: A Multilingual Benchmark for Idiom Understanding](https://arxiv.org/abs/2606.02584) ⭐️ 8.0/10

Researchers introduced IdiomX, a large-scale multilingual benchmark with over 190,000 examples covering 12,000+ idioms across English, Arabic, and French, along with a unified four-task evaluation framework for idiom detection, retrieval, and interpretation. IdiomX addresses a persistent challenge in NLP by providing a scalable, reproducible benchmark that enables systematic evaluation of idiom understanding in multilingual contexts, which is crucial for advancing language models' figurative language capabilities. The benchmark includes four tasks: idiom detection, context-to-idiom retrieval, Arabic-to-English idiom retrieval, and idiom interpretation, with experiments showing that contextual transformers improve detection and hybrid retrieval architectures strengthen cross-lingual retrieval.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: Idioms are expressions whose meanings are non-compositional and context-dependent, making them difficult for NLP models that rely on literal word meanings. Existing idiom resources are often limited in scale, language coverage, or contextual diversity, hindering progress in multilingual figurative language understanding.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02584">[2606.02584] IdiomX A Multilingual Benchmark for Idiom ...</a></li>
<li><a href="https://github.com/aymanshar/idiomx-dataset">GitHub - aymanshar/idiomx-dataset: IdiomX: A large-scale ...</a></li>
<li><a href="https://www.machinebrief.com/news/cracking-the-code-idiomx-revolutionizes-idiomatic-expression-9bdo">Cracking the Code: IdiomX Revolutionizes Idiomatic...</a></li>

</ul>
</details>

**Tags**: `#NLP`, `#multilingual`, `#idiom understanding`, `#benchmark`, `#language models`

---

<a id="item-23"></a>
## [LLMs Found Greener Than Average Humans in New Benchmark](https://arxiv.org/abs/2606.02741) ⭐️ 8.0/10

A new benchmark study evaluates environmental attitudes in 31 large language models and finds that many LLMs exhibit more environmentally progressive attitudes than the average human survey respondent from Germany. This matters because LLMs are increasingly used in sustainability decision support and public communication; if they systematically lean progressive, they could bias outputs, raising concerns about steerability and normative reliability. The study draws on questions from established environmental awareness surveys and compares LLM responses across proprietary and open-weight models, finding no systematic relationship with model origin, size, or release context.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: Large language models are AI systems trained on vast text data to generate human-like text. They are now used in areas like sustainability reporting and decision support, making their embedded values important. This study introduces a reusable benchmark to assess environmental cognition, affect, and behavioral recommendations in LLMs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02741">Greener Than Humans? Environmental Attitudes in Large Language...</a></li>
<li><a href="https://www.solarwinds.com/blog/open-source-llms-vs-open-weight-llms-vs-proprietary-llms">Open Source LLMs vs Open Weight LLMs vs Proprietary LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#environmental attitudes`, `#AI ethics`, `#sustainability`, `#benchmark`

---

<a id="item-24"></a>
## [Deep Layers May Not Need Context for Value Vectors](https://arxiv.org/abs/2606.02780) ⭐️ 8.0/10

A new paper shows that deep transformer layers can use context-free value vectors, improving performance and enabling sparse storage without recomputation. The authors propose Bank of Values (BoV), which learns a lookup table of token-specific value vectors for the last third of layers. This finding challenges the conventional assumption that value vectors always need context from the residual stream, potentially leading to more efficient LLM architectures. BoV reduces compute and memory while matching or exceeding standard attention performance. BoV was evaluated on 135M and 780M parameter models, improving validation loss and average benchmark scores across 21 tasks. The context-free value vectors can be stored as sparse model parameters, eliminating the need for recomputation or persistent caching.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: In transformer attention, query, key, and value vectors are typically computed from the residual stream, making them context-dependent. The residual stream carries token information through layers via residual connections. This paper discovers that in deep layers, value vectors benefit primarily from original token identity rather than contextual mixing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.02780">Do Value Vectors in Deep Layers Need Context from the Residual...</a></li>
<li><a href="https://arxiv.org/html/2312.12141v1">Exploring the Residual Stream of Transformers - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#transformer`, `#LLM`, `#attention`, `#efficiency`, `#architecture`

---

<a id="item-25"></a>
## [Audit Reveals ~39% Errors in NL-to-FOL Benchmarks](https://arxiv.org/abs/2606.02837) ⭐️ 8.0/10

A systematic human inspection of the FOLIO and MALLS benchmarks found that approximately 39% and 36% of entries, respectively, contain incorrect first-order logic formalizations. The authors released corrected ground truths and an LLM-assisted framework to focus human relabeling. These errors distort LLM evaluation, as shown by accuracy gains of +9 to +22 percentage points when using corrected ground truths on three state-of-the-art LLMs. The findings highlight the need for rigorous benchmark auditing in neurosymbolic AI and natural language inference. The audit covered the validation split of FOLIO and a subset of MALLS test instances, also finding 16.4% and 48% ambiguous NL sentences in FOLIO and MALLS, respectively, and 8.4% incorrect NLI labels in FOLIO. The proposed LLM-based framework achieves 90% dataset accuracy after reviewing fewer than 24% of instances, compared to over 70% for unguided review.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: First-order logic (FOL) is a formal language used to represent knowledge in a precise, machine-readable way. Translating natural language (NL) to FOL is a key task in neurosymbolic AI and natural language inference (NLI), and benchmarks like FOLIO and MALLS are used to evaluate models. However, until this work, these benchmarks had never been rigorously audited for annotation errors.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2509.22338">Advancing Natural Language Formalization to First Order Logic ...</a></li>
<li><a href="https://github.com/fvossel/NL2FOL">GitHub - fvossel/NL2FOL: Natural Language To First Order ...</a></li>

</ul>
</details>

**Tags**: `#neurosymbolic AI`, `#natural language inference`, `#benchmark auditing`, `#first-order logic`, `#LLM evaluation`

---

<a id="item-26"></a>
## [Economy of Minds: Emergent Collective Intelligence via Economic Interactions](https://arxiv.org/abs/2606.02859) ⭐️ 8.0/10

Researchers introduced a multi-agent system where agents use auctions, payments, and bankruptcy to self-organize, achieving emergent collective intelligence without centralized control. The system outperformed monolithic baselines on five agentic tasks including mathematical reasoning and scientific research. This work demonstrates a new path to multi-agent intelligence by designing decentralized incentive structures inspired by Hayek's economic theory, potentially enabling scalable and robust AI coordination without explicit communication or global orchestration. The economy initializes with weak agents and evolves via economic selection: effective agents accumulate wealth and are mutated, while bankrupt agents are replaced. The system produces emergent multi-step reasoning strategies and outperforms stronger monolithic baselines across tasks.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: Friedrich Hayek's economic theory emphasizes decentralized coordination in markets, where prices and economic signals guide behavior without central planning. This paper applies similar principles to multi-agent AI systems, using auctions and payments as signals for credit assignment and planning.

<details><summary>References</summary>
<ul>
<li><a href="https://plato.stanford.edu/entries/friedrich-hayek/">Friedrich Hayek - Stanford Encyclopedia of Philosophy</a></li>
<li><a href="https://arxiv.org/html/2602.14219v1">The Agent Economy: A Blockchain-Based Foundation for ...</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#decentralized coordination`, `#emergent intelligence`, `#AI`, `#economic theory`

---

<a id="item-27"></a>
## [ALAR: Dual-Mode Reasoning for Efficient LLM Agents](https://arxiv.org/abs/2606.02871) ⭐️ 8.0/10

Researchers propose Adaptive Latent Agentic Reasoning (ALAR), a dual-mode framework that uses compact latent reasoning for routine agent turns and only activates explicit chain-of-thought (CoT) when deeper deliberation is needed. ALAR addresses a key inefficiency in LLM agents by reducing unnecessary verbose reasoning, achieving up to 84.6% token reduction in tool-use tasks while maintaining accuracy, which could lower cost and latency in real-world deployments. ALAR learns latent reasoning by using agent actions as supervision anchors and is optimized to use latent reasoning when sufficient, reserving explicit CoT for harder decisions. Experiments on agentic search and tool-use benchmarks show token reductions of 43.6% and 84.6%, respectively, with comparable or better accuracy.

rss · arXiv - NLP · Jun 3, 04:00

**Background**: Large reasoning models often generate extended chain-of-thought (CoT) reasoning, which improves performance but becomes inefficient for LLM agents that must make many decisions in multi-turn trajectories. Current agents allocate reasoning effort nearly uniformly across turns, leading to wasted computation on routine steps. ALAR introduces a dual-mode approach that dynamically switches between efficient latent reasoning and explicit CoT based on task difficulty.

<details><summary>References</summary>
<ul>
<li><a href="https://aigentic.blog/arxiv-digest-agents-reasoning-data-organization">Arxiv digest: Agents , reasoning latency , and data — AIgentic</a></li>
<li><a href="https://www.marktechpost.com/2025/06/14/othink-r1-a-dual-mode-reasoning-framework-to-cut-redundant-computation-in-llms/">OThink-R1: A Dual - Mode Reasoning Framework to... - MarkTechPost</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#reasoning efficiency`, `#chain-of-thought`, `#latent reasoning`, `#agentic AI`

---

<a id="item-28"></a>
## [Linear Probes Detect Task Format, Not Reasoning Mode](https://arxiv.org/abs/2606.02907) ⭐️ 8.0/10

A new study shows that linear probes on LLM hidden states achieve 100% accuracy in distinguishing reasoning types, but this is entirely due to format confounds like source identity and option count, not actual reasoning differences. This challenges a common assumption in mechanistic interpretability that linear probes reveal distinct reasoning representations, urging researchers to deconfound task format in future studies. The study probed Qwen3-14B on LogiQA 2.0 (deductive), ARC-Challenge (inductive), and αNLI (abductive), finding that after residualizing format confounds, accuracy dropped to chance, and causal steering showed no functional link (p=0.286).

rss · arXiv - NLP · Jun 3, 04:00

**Background**: Linear probing trains a linear classifier on LLM hidden states to predict a property (e.g., reasoning type). It is widely used in interpretability to claim that models encode specific concepts. However, this method can be confounded by superficial features like task format, which this paper demonstrates systematically.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02907">[2606.02907] Linear Probes Detect Task Format, Not Reasoning ...</a></li>

</ul>
</details>

**Tags**: `#LLM interpretability`, `#linear probing`, `#reasoning`, `#AI safety`, `#machine learning`

---

<a id="item-29"></a>
## [VLMs Consistent Yet Wrong: Weak Geometric Grounding Revealed](https://arxiv.org/abs/2606.02742) ⭐️ 8.0/10

A new paper introduces ViewDiag, a multi-view evaluation protocol that reveals leading vision-language models (VLMs) often produce view-invariant but incorrect spatial predictions, challenging the assumption that cross-view consistency implies geometric understanding. This finding has significant implications for robotics and embodied AI, where reliable spatial reasoning is critical; it shows that current VLMs may rely on prior-driven collapse rather than evidence-sensitive reasoning, undermining their trustworthiness in real-world applications. ViewDiag is built from Hypersim, ScanNet, and KITTI360, comprising 176 object-pair tracks across 80 scenes with 2–10 views per track, and evaluates models on metric accuracy, distributional concentration, and a latent feature probe for internal collapse.

rss · arXiv - Computer Vision · Jun 3, 04:00

**Background**: Vision-language models (VLMs) are AI systems that process both images and text to answer questions about visual content. Spatial reasoning—understanding distances and positions—is crucial for tasks like robot navigation. Prior work often used cross-view consistency as a proxy for geometric grounding, but this paper shows that consistency can be misleading.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/apple/ml-hypersim">apple/ml- hypersim : Hypersim : A Photorealistic Synthetic Dataset for...</a></li>
<li><a href="http://www.scan-net.org/">ScanNet | Richly-annotated 3D Reconstructions of Indoor Scenes</a></li>
<li><a href="https://deepwiki.com/bowang-lab/EchoJEPA/6.3-multi-view-evaluation">Multi-View Evaluation | bowang-lab/EchoJEPA | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#spatial reasoning`, `#embodied AI`, `#evaluation protocol`, `#computer vision`

---

<a id="item-30"></a>
## [MetaWorld: Scaling Multi-Agent Video World Models from Single-View Data](https://arxiv.org/abs/2606.02753) ⭐️ 8.0/10

MetaWorld introduces a framework that scales multi-agent video world models from single-view videos by decomposing monocular footage into ego-motion and subject trajectory, enabling synchronized multi-agent motion data without multi-camera setups. This addresses critical data scarcity and world state alignment challenges in multi-agent video world modeling, with high potential impact on embodied AI and Metaverse applications where consistent multi-view simulation is essential. MetaWorld uses Monocular World-State Unrolling (MWSU) for camera-trajectory decomposition, a Subject-Aware World Generator for appearance-driven simulation, and World-State Alignment (WSA) with per-frame inter-branch cross-attention to enforce geometric and motion consistency across views.

rss · arXiv - Computer Vision · Jun 3, 04:00

**Background**: Video world models are generative models that predict future video frames conditioned on actions, used for embodied AI and Metaverse. Existing models are limited to single-agent single-view, and extending to multi-agent requires expensive multi-camera data and consistent world state alignment across views.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion">Awesome Video World Models with AR Diffusion - GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ego-motion">Ego-motion</a></li>

</ul>
</details>

**Tags**: `#multi-agent`, `#video world model`, `#embodied AI`, `#monocular decomposition`, `#Metaverse`

---

<a id="item-31"></a>
## [GeoDrive-Bench: Benchmarking Region-Specific Driving VLMs](https://arxiv.org/abs/2606.02774) ⭐️ 8.0/10

Researchers introduced GeoDrive-Bench, a benchmark with 5,053 human-validated multiple-choice QA pairs across six countries to evaluate vision-language models on region-specific driving rules, and proposed a distillation method to inject such knowledge into models. This work addresses a critical gap in VLM evaluation for autonomous driving, as region-specific traffic rules are essential for safe global deployment, and the distillation method offers a practical path to improve model adaptability. The benchmark covers four driving tasks: perception, prediction, planning, and region reasoning, without providing explicit country labels. Experiments on nine state-of-the-art VLMs revealed substantial performance variations across regions.

rss · arXiv - Computer Vision · Jun 3, 04:00

**Background**: Vision-language models (VLMs) combine visual and textual understanding, and are increasingly used in autonomous driving for tasks like scene understanding and decision-making. However, traffic rules vary by country (e.g., left-hand vs. right-hand driving), and most VLMs are not explicitly trained on such regional nuances, posing risks for deployment in diverse global settings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.02774">[2606.02774] GeoDrive-Bench: Benchmarking Region-Specific ...</a></li>
<li><a href="https://github.com/GeoDriveBench/GeoDrive-Bench">GitHub - GeoDriveBench/GeoDrive-Bench: An anonymized code ...</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#vision-language models`, `#benchmark`, `#region-specific reasoning`, `#distillation`

---

<a id="item-32"></a>
## [Automated Pipeline for Oncology VQA Benchmark from Private Reports](https://arxiv.org/abs/2606.02809) ⭐️ 8.0/10

Researchers developed an automated agent-driven pipeline that generates contamination-controlled multiple-choice VQA benchmarks from private radiology reports and 3D oncology imaging, applied to four in-house cancer cohorts. This work addresses critical gaps in evaluating vision-language models on medical images by providing scalable, clinically grounded benchmarks without manual annotation, revealing that no current VLM dominates and that visual reliance varies by dataset. The pipeline produces two question types: RADS-style questions from clinician-defined schemas and LLM-generated questions verified against source reports. A blind ablation showed that for Lung CT, the leading closed model achieved higher accuracy when blinded than when sighted.

rss · arXiv - Computer Vision · Jun 3, 04:00

**Background**: Vision-language models (VLMs) are increasingly used in medical imaging, but evaluating them requires benchmarks that are clinically relevant and free from data contamination. Existing public benchmarks are often small, manually annotated, or may have leaked into VLM training data. RADS (Reporting and Data Systems) are standardized schemas used by radiologists to report findings consistently.

<details><summary>References</summary>
<ul>
<li><a href="https://www.acr.org/Clinical-Resources/Clinical-Tools-and-Reference/Reporting-and-Data-Systems">Reporting and Data Systems (RADS) - American College of Radiology</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#medical imaging`, `#benchmark`, `#VQA`, `#oncology`

---

<a id="item-33"></a>
## [Prioritize Identifying Structure Over Complex Models for Science](https://arxiv.org/abs/2606.02632) ⭐️ 8.0/10

A new position paper argues that mechanistic learning from observational data is generically underdetermined, especially when using LLMs, and proposes concrete standards for mechanistic ML to ensure genuine scientific discovery. This paper highlights a fundamental flaw in using LLMs for scientific discovery: predictive success does not guarantee correct mechanistic understanding. If adopted, its proposed standards could reshape how AI is used in science, preventing misleading conclusions. The paper argues that in high-dimensional proxy regimes, many incompatible mechanisms can produce the same observational relationships, and LLMs exacerbate this by collapsing diverse explanations into a single narrative. It calls for norms like explicit causal assumptions and out-of-distribution validation.

rss · arXiv - Data Science & Statistics · Jun 3, 04:00

**Background**: Mechanistic learning combines mechanistic mathematical modeling with data-driven machine learning to infer causal mechanisms from data. Underdetermination occurs when multiple mechanisms fit the data equally well. LLMs are increasingly used to generate scientific hypotheses, but their tendency to produce coherent narratives can mask the existence of alternative explanations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/why-mechanistic-learning-needs-an-overhaul-in-ai-2ne4">Why Mechanistic Learning Needs an Overhaul in AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2505.04651">[2505.04651] Scientific Hypothesis Generation and Validation ... GitHub - ChicagoHAI/hypothesis-generation: This is the ... Exploring the role of large language models in the scientific ... AgenticHypothesis: A Survey on Hypothesis Generation Using ... Toward Reliable Scientific Hypothesis Generation: Evaluating ... Multi agent large language models for biomedical hypothesis ... ICLR AgenticHypothesis: A Survey on Hypothesis Generation ...</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#large language models`, `#scientific discovery`, `#mechanistic models`, `#underdetermination`

---

<a id="item-34"></a>
## [Periodic and Soft Target Updates Stabilize Linear Q-Learning](https://arxiv.org/abs/2606.02645) ⭐️ 8.0/10

This paper provides a rigorous theoretical analysis proving that periodic hard target updates and soft target updates guarantee convergence of linear Q-learning to the exact projected Q-Bellman solution under explicit spectral and step-size conditions. This work fills a critical gap in understanding why target updates stabilize Q-learning, a widely used reinforcement learning algorithm, and provides theoretical foundations for designing more reliable RL algorithms. The analysis uses switched linear system dynamics and joint spectral radius (JSR) to model the effect of target updates, and extends from deterministic to stochastic settings by adding noise analysis.

rss · arXiv - Data Science & Statistics · Jun 3, 04:00

**Background**: Q-learning is a model-free reinforcement learning algorithm that learns action values. Linear Q-learning uses linear function approximation to handle large state spaces, but it can diverge. Target updates, where a separate target network is periodically or softly updated, are empirically known to stabilize training, but their theoretical justification was incomplete.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Q-learning">Q-learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Joint_Spectral_Radius">Joint spectral radius - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#Q-learning`, `#target updates`, `#convergence analysis`, `#linear function approximation`

---

<a id="item-35"></a>
## [TERA: Scalable Derivative Gaussian Processes via Exact Gradient Reduction](https://arxiv.org/abs/2606.02909) ⭐️ 8.0/10

Researchers introduced TERA, a method that reduces the computational cost of derivative Gaussian processes from O(n^3 d^3) to O(d m^2 + m^6) using exact gradient reduction and Vecchia approximation. This breakthrough enables efficient high-dimensional surrogate modeling, where derivative observations are crucial but previously computationally prohibitive, potentially accelerating applications in engineering design, Bayesian optimization, and scientific computing. TERA proves that for stationary kernels, gradient components orthogonal to the direction between target and conditioning points are conditionally independent, allowing the exact conditional density to be characterized by at most m^2 directional derivatives. The method keeps the underlying derivative GP model mathematically unchanged while achieving flat computation time and memory usage with respect to dimension d.

rss · arXiv - Data Science & Statistics · Jun 3, 04:00

**Background**: Gaussian processes (GPs) are a popular nonparametric regression method, but standard GP inference scales cubically with the number of data points. Derivative observations can improve GP surrogates in high dimensions, but exact inference with n function values and n full gradients in d dimensions costs O(n^3 d^3). The Vecchia approximation is a technique that approximates the joint distribution by a product of low-dimensional conditional distributions, inducing sparsity. TERA combines these ideas with a novel exact gradient reduction to achieve scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vecchia_approximation">Vecchia approximation</a></li>
<li><a href="https://arxiv.org/pdf/1708.06302">A general framework for Vecchia approximations of</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_process">Gaussian process - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Gaussian Processes`, `#Scalable Inference`, `#Derivative Observations`, `#Vecchia Approximation`, `#High-Dimensional Modeling`

---

<a id="item-36"></a>
## [Exact Formula for CoT Generalization Error Revealed](https://arxiv.org/abs/2606.03217) ⭐️ 8.0/10

Researchers derived an exact formula for the generalization error of chain-of-thought reasoning in in-context learning, using random matrix theory under high-dimensional asymptotics. This provides a theoretical foundation for understanding how CoT depth affects performance, revealing phase transitions and optimal scaling, which can guide the design of more efficient reasoning models. The analysis identifies sharp phase transitions separating exponential and polynomial improvement, saturation, and overthinking, and shows that deeper reasoning is most effective with rich pretraining and in-context information.

rss · arXiv - Data Science & Statistics · Jun 3, 04:00

**Background**: Chain-of-thought reasoning involves generating intermediate steps before producing a final answer, improving performance on complex tasks. In-context learning allows models to adapt to tasks using examples provided in the prompt without parameter updates. Random matrix theory is a mathematical tool used to analyze high-dimensional systems, often applied to study generalization in neural networks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.03217">An Asymptotic Theory of Chain-of-Thought in In - Context Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generalization_error">Generalization error - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#chain-of-thought`, `#in-context learning`, `#theoretical analysis`, `#random matrix theory`, `#large language models`

---

<a id="item-37"></a>
## [Unifying Calibration Concepts Across Classification and Regression](https://arxiv.org/abs/2606.03245) ⭐️ 8.0/10

This paper reviews and extends calibration notions for classification and regression, introducing modal calibration for nominal outcomes and clarifying hierarchical relations among various calibration concepts. This work provides a unified theoretical framework that bridges calibration in classification and regression, which is crucial for improving the reliability and interpretability of probabilistic forecasts in machine learning. The paper introduces modal calibration for nominal outcomes, distinguishes full, partial, and average calibration, and shows that double probability integral transform (PIT) calibration is logically independent of previous discrete calibration concepts.

rss · arXiv - Data Science & Statistics · Jun 3, 04:00

**Background**: Calibration in probabilistic forecasting ensures that predicted probabilities match observed frequencies. For classification, common notions include confidence calibration, while for regression, calibration often involves the probability integral transform (PIT). This paper bridges these areas by introducing hierarchical relations and new concepts like modal calibration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Calibration_(statistics)">Calibration (statistics) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Probability_integral_transform">Probability integral transform - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#calibration`, `#probabilistic forecasting`, `#classification`, `#regression`, `#machine learning`

---

<a id="item-38"></a>
## [GLP-1 drugs linked to lower addiction and overdose risks](https://www.sciencedaily.com/releases/2026/06/260603023919.htm) ⭐️ 8.0/10

A large study of over 600,000 U.S. veterans found that GLP-1 drugs like semaglutide are associated with reduced risks of developing substance use disorders and fewer overdoses, hospitalizations, and drug-related deaths among those already addicted. This finding suggests GLP-1 drugs could have a novel application in treating addiction, a major public health issue, potentially offering a new tool to combat the opioid crisis and other substance use disorders. The study analyzed electronic health records of over 600,000 veterans, comparing those prescribed GLP-1 drugs to those not, and found lower rates of alcohol, nicotine, cannabis, cocaine, and opioid use disorders, as well as reduced adverse outcomes.

rss · ScienceDaily Health · Jun 3, 14:04

**Background**: GLP-1 receptor agonists, such as semaglutide (Ozempic, Wegovy), are medications originally developed for type 2 diabetes and later approved for weight loss. They work by activating GLP-1 receptors in the pancreas and brain, which regulate insulin release and appetite. Recent research has suggested these drugs may also affect reward pathways in the brain, potentially reducing cravings for addictive substances.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GLP-1_receptor_agonist">GLP-1 receptor agonist - Wikipedia</a></li>
<li><a href="https://med.stanford.edu/news/insights/2025/04/ozempic-addiction-glp-1s-mounjaro-lembke.html">Five things to know about GLP-1s and addiction</a></li>

</ul>
</details>

**Tags**: `#GLP-1`, `#addiction`, `#pharmacology`, `#public health`, `#clinical research`

---

<a id="item-39"></a>
## [Scientists Reverse Anxiety by Fixing a Tiny Brain Circuit](https://www.sciencedaily.com/releases/2026/06/260603015356.htm) ⭐️ 8.0/10

Researchers identified a specific group of neurons in the amygdala that, when restored to normal activity, reversed anxiety and social deficits in mice. This discovery pinpoints a precise neural circuit underlying anxiety, offering a promising target for developing new treatments for anxiety disorders in humans. The study focused on a tiny circuit within the basolateral amygdala, and restoring excitability balance in these neurons reversed pathological behaviors in mice with intrinsic anxiety.

rss · ScienceDaily Health · Jun 3, 12:16

**Background**: The amygdala is a brain region known for processing emotions like fear and anxiety. Dysfunction in amygdala circuits has been linked to various psychiatric conditions, including anxiety disorders. This study builds on prior work showing that distinct amygdala circuits regulate different behaviors.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nature.com/articles/nature14188">From circuits to behaviour in the amygdala - Nature</a></li>
<li><a href="https://medicalxpress.com/news/2025-07-key-group-cerebral-amygdala-neurons.html">Key group of cerebral amygdala neurons identified in anxiety and...</a></li>
<li><a href="https://www.simplypsychology.org/amygdala.html">What Is The Amygdala : Function & Brain Location</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#anxiety`, `#brain circuit`, `#amygdala`, `#translational research`

---

<a id="item-40"></a>
## [Brain scans reveal two distinct autism subtypes](https://www.sciencedaily.com/releases/2026/06/260602021634.htm) ⭐️ 8.0/10

A study combining brain scans from nearly 1,000 people with autism and 20 genetically engineered mouse models identified two biologically distinct autism subtypes: one with hyperconnectivity and one with hypoconnectivity in brain regions. This discovery could lead to more personalized diagnosis and treatment for autism, as the subtypes may respond differently to therapies and have distinct underlying biological mechanisms. The hyperconnectivity subtype was associated with immune-related pathways, while the hypoconnectivity subtype was linked to synaptic pathways; the subtypes showed modest differences on standardized autism assessments.

rss · ScienceDaily Health · Jun 3, 04:46

**Background**: Autism spectrum disorder is highly heterogeneous, with varied symptoms and genetic causes. Previous research has struggled to identify consistent biological subtypes. This study used cross-species fMRI to link human brain connectivity patterns with specific genetic mouse models, providing a more robust classification.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/06/260602021634.htm">Brain scans reveal two distinct types of autism | ScienceDaily</a></li>
<li><a href="https://medicalxpress.com/news/2026-05-brain-scans-reveal-distinct-autism.html">Brain scans reveal two distinct autism subtypes with different...</a></li>
<li><a href="https://www.nature.com/articles/s41593-026-02287-z">Autism subtypes identified using cross-species functional ...</a></li>

</ul>
</details>

**Tags**: `#autism`, `#neuroscience`, `#brain imaging`, `#genetics`, `#biomarkers`

---