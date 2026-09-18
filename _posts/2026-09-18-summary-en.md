---
layout: default
title: "Horizon Summary: 2026-09-18 (EN)"
date: 2026-09-18
lang: en
---

> From 110 items, 16 important content pieces were selected

---

1. [Android 17 adds Pixel-exclusive APIs without AOSP release](#item-1) ⭐️ 8.0/10
2. [Cactus Needle 3: 8-29MB Models Match DeepSeek V4 Flash](#item-2) ⭐️ 8.0/10
3. [ZCode silently uploads users' full Git history to the cloud](#item-3) ⭐️ 8.0/10
4. [Dan Abramov uses AI to 'vibe' a proof of Conway's conjecture](#item-4) ⭐️ 8.0/10
5. [South Korea Raises Data Breach Fines to 10% of Revenue](#item-5) ⭐️ 8.0/10
6. [Rust Team Warns of Targeted Social-Engineering Attacks on Maintainers](#item-6) ⭐️ 8.0/10
7. [Anthropic's Claude Code Hits GitHub Trending as Agentic Terminal Coding Tool](#item-7) ⭐️ 8.0/10
8. [NSA's Ghidra: Open-Source Reverse Engineering Framework](#item-8) ⭐️ 8.0/10
9. [Colibri: Pure C engine streams frontier MoE models from disk](#item-9) ⭐️ 8.0/10
10. [Google Research Releases TimesFM 3.0 Time-Series Foundation Model](#item-10) ⭐️ 8.0/10
11. [First End-to-End Study of Web Search by Conversational LLM Agents](#item-11) ⭐️ 8.0/10
12. [AutoTuring Tests Whether AI Agents Truly Understand Computer Architecture](#item-12) ⭐️ 8.0/10
13. [MAGS: Multi-Agent Framework Adds Formal Safety Guarantees to LLM Code](#item-13) ⭐️ 8.0/10
14. [RF-CNNs Repurpose Wireless Hardware for Edge AI Inference](#item-14) ⭐️ 8.0/10
15. [SonoBase: Open Ultrasound Foundation Model Trained on 456k Images](#item-15) ⭐️ 8.0/10
16. [Cells That Survive Programmed Death Rebuild Damaged Tissue](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Android 17 adds Pixel-exclusive APIs without AOSP release](https://grapheneos.social/@GrapheneOS/117282080803799576) ⭐️ 8.0/10

GrapheneOS reports that Android 17 QPR1 introduces new app developer APIs that are available only on Pixel devices and have not been released to the Android Open Source Project (AOSP). This marks the first time since Android 3.x that new APIs have been added without a corresponding AOSP release. This change undermines the openness of Android and could fragment the ecosystem, making it harder for alternative operating systems like GrapheneOS to stay compatible and secure. It also raises questions about Google's long-term commitment to AOSP and could affect other OEMs and developers who rely on timely source releases. According to community discussion, the issue may not be that the new API is Pixel-exclusive per se, but that the first and third quarterly release patches each year are Pixel-exclusive, delaying AOSP updates. Google still provides monthly security backports to trusted OEMs, but the public AOSP source lags behind.

hackernews · theanonymousone · Sep 18, 19:03 · [Discussion](https://news.ycombinator.com/item?id=49758736)

**Background**: AOSP is the open-source codebase that Google maintains and releases for Android; device makers and custom ROM projects like GrapheneOS build on it. Historically, Google has released new Android versions and their APIs to AOSP, allowing the community to adapt. GrapheneOS is a security- and privacy-focused Android fork that relies on timely AOSP releases to integrate patches and maintain compatibility with Pixel devices.

<details><summary>References</summary>
<ul>
<li><a href="https://alternativeto.net/news/2026/9/grapheneos-claims-android-17-qpr1-apis-remain-exclusive-to-pixel-devices/">GrapheneOS claims Android 17 QPR1 APIs remain exclusive to Pixel devices | AlternativeTo</a></li>
<li><a href="https://source.android.com/">Android Open Source Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely critical of Google, with users expressing frustration over roadblocks for GrapheneOS and accusing Google of regretting Android's open-source nature. Some clarify that the real issue is the Pixel-exclusive quarterly patches, not just the new API, while others praise GrapheneOS and hope it survives.

**Tags**: `#Android`, `#AOSP`, `#GrapheneOS`, `#Open Source`, `#Google`

---

<a id="item-2"></a>
## [Cactus Needle 3: 8-29MB Models Match DeepSeek V4 Flash](https://cactuscompute.com/needle) ⭐️ 8.0/10

Cactus released Needle 3, a family of ultra-small automation models (8-29MB, 25-121M parameters at 2-bit) that handle tool calls and structured JSON output, matching or surpassing DeepSeek V4 Flash on narrow tasks. The models use a novel Monarch Hadamard MLP architecture and intelligence laddering, and run on platforms from Raspberry Pi 5 to WebAssembly. This demonstrates that extremely small, compressed models can handle automation tasks previously requiring much larger models, enabling powerful edge AI on low-power devices like phones, cars, and industrial controllers. It could significantly reduce cost and latency for tool-calling applications while keeping data local. The 20-layer model achieves 86.0 on Mobile Actions at 2-bit, beating LFM2.5 1.2B (82.4) and Qwen3.5 0.8B (76.0); it supports 7 languages, finetuning, regex triggers, and calibrated confidence scores. However, it does not chat by design and may fail on indirect or ambiguous commands, as community tests showed.

hackernews · HenryNdubuaku · Sep 18, 00:11 · [Discussion](https://news.ycombinator.com/item?id=49748553)

**Background**: Small language models aim to run on edge devices by drastically reducing size through quantization (e.g., 2-bit) and efficient architectures. Tool calls and structured JSON output are critical for automation, allowing models to trigger actions like turning on lights. Cactus Needle 3 builds on prior Needle 2 feedback to improve performance and usability.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49748553">Show HN: Cactus Needle 3: 8-29MB automation models... | Hacker News</a></li>
<li><a href="https://kerneldigest.dev/glosario/dsa/hadamard-mlp">Hadamard MLP — KernelDigest</a></li>
<li><a href="https://github.com/HarryR/z80ai">GitHub - HarryR/z80ai: Z80-μLM is a 2 - bit quantized language model ...</a></li>

</ul>
</details>

**Discussion**: Community members tested the demo and found it works for direct commands like 'turn all the lights on/off' but struggles with indirect phrasing such as 'I need a wee' or 'it's too cold', sometimes producing incorrect actions. Some noted low confidence scores on bad responses and suggested adding a threshold, while others praised its potential for low-power real-world use cases when paired with voice models.

**Tags**: `#small language models`, `#tool calls`, `#structured output`, `#edge AI`, `#model compression`

---

<a id="item-3"></a>
## [ZCode silently uploads users' full Git history to the cloud](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

A forensic investigation published on blog.ferstar.org reveals that ZCode, the AI coding tool from z.ai, silently packages a user's entire workspace — including full .git history, LFS asset cache, reflogs, and global app configs — encrypts it, and uploads the archive to Aliyun OSS whenever the user is logged in. The post reconstructs the upload pipeline and encryption scheme via local forensics and reverse engineering, and notes that the decryption keys are held exclusively by the server, meaning users cannot decrypt or audit what was sent. This is a serious privacy and security issue for developers, because Git history often contains secrets, credentials, proprietary code, and internal commit messages that were never meant to leave the local machine. It also raises broader questions about trust in AI coding agents, which increasingly run with broad filesystem permissions and are hard for users to audit. According to the investigation, the upload happens silently whenever the app is logged in and targets Aliyun OSS (Alibaba Cloud object storage), with server-exclusive decryption keys; the article ties the behavior to ZCode's 'codebase indexing' feature, which z.ai later apologized for in an official statement. Community members also noted that the same class of risk applies to other agents, with one commenter observing that GLM and DeepSeek models are 'fond of trying to read dotfiles and anything listed in your .gitignore files.'

hackernews · csmantle · Sep 18, 06:11 · [Discussion](https://news.ycombinator.com/item?id=49750694)

**Background**: ZCode is a free AI coding tool launched by Chinese startup z.ai in July 2026, powered by its GLM model family and positioned as a lower-cost challenger to Cursor, Claude Code, and GitHub Copilot. AI coding agents typically need to read project files to provide useful suggestions, and many offer a 'codebase indexing' feature that builds a searchable representation of the repository — usually locally, but sometimes involving cloud services. Git history is the complete record of every commit ever made in a repository, so uploading it can expose deleted files, old credentials, and sensitive commit messages that are no longer visible in the current working tree.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/">Inside ZCode: Silently Uploading Your Entire Git History to the Cloud</a></li>
<li><a href="https://tokenstead.ai/guides/zcode-silent-git-history-upload">ZCode uploads your git history ; Z.ai holds the only key</a></li>
<li><a href="https://venturebeat.com/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding">Z.ai launches ZCode to challenge Cursor, Claude Code and GitHub Copilot in AI coding | VentureBeat</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (243 points, 89 comments) is largely critical and skeptical: commenters question whether it is naive to assume an agent will not access anything on disk, note that permission classifiers in auto mode are just models guessing, and point out that sandboxing is undermined when agents route around it. Several users say incidents like this are why they stick with alternatives such as OpenCode, and one commenter reports that Windows Defender repeatedly asks to upload Codex work files for analysis, which they block.

**Tags**: `#privacy`, `#security`, `#AI coding tools`, `#Git`, `#cloud upload`

---

<a id="item-4"></a>
## [Dan Abramov uses AI to 'vibe' a proof of Conway's conjecture](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 8.0/10

Dan Abramov published a blog post and GitHub repository (gaearon/conway-refinement) describing how he used large language models to assist in producing a proof of Conway's conjecture, the last of John Conway's own conjectures about his 'look-and-say' numbers still standing. The writeup includes a section titled 'Why I think it's correct' explaining the reasoning behind the AI-assisted proof. If the proof holds up, it would be a striking demonstration that LLMs can contribute to original mathematical research, potentially reshaping how mathematicians approach open problems and how credit is assigned in academia. It also fuels the broader debate about 'vibe coding'—accepting AI-generated output without full verification—extended into the domain of formal proof. The proof is presented in a GitHub repository with an explicit section justifying its correctness, but it has not been formally verified or peer-reviewed. The author is a software engineer (creator of Redux) rather than a trained mathematician, and the approach relies on iterative prompting and simplification of AI-generated arguments.

hackernews · m-hodges · Sep 18, 14:36 · [Discussion](https://news.ycombinator.com/item?id=49755024)

**Background**: Conway's conjecture concerns the 'look-and-say' sequence, in which each term describes the previous term (e.g., '1, 11, 21, 1211...'). John Conway proved that the ratio between successive terms converges to a constant now called Conway's constant, and conjectured that certain other properties of the sequence hold; this conjecture remained open. 'Vibe coding' is a term coined by Andrej Karpathy in February 2025 for AI-assisted programming where developers accept generated code based on results rather than line-by-line review.

<details><summary>References</summary>
<ul>
<li><a href="https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/">How I Vibed a Proof of Conway ’ s Conjecture — overreacted</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dan_Abramov">Dan Abramov</a></li>

</ul>
</details>

**Discussion**: Commenters were largely impressed but cautious: a trained mathematician praised the direction while recommending further simplification and checking whether parts of the proof exist elsewhere, and another commenter compared AI to the monkey in the infinite monkey theorem, suggesting a finite number of LLM agents could eventually find all theorems given enough tokens. A more skeptical commenter argued that if the proof is valid, it would be shocking to academia and would break existing intellectual hierarchies and reward systems.

**Tags**: `#AI`, `#mathematics`, `#proof`, `#LLM`, `#Conway's conjecture`

---

<a id="item-5"></a>
## [South Korea Raises Data Breach Fines to 10% of Revenue](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899) ⭐️ 8.0/10

South Korea has amended its Personal Information Protection Act (PIPA) to raise the maximum fine for data breaches from 3% to 10% of a company's total revenue, with the amendment promulgated on March 10, 2026, and taking effect on September 11, 2026. The change also introduces personal accountability for CEOs for data protection failures. This move could set a global precedent for stricter data protection enforcement, pushing companies worldwide to prioritize security investments over cost-cutting. It may influence other countries to adopt similar revenue-based fines, potentially reshaping corporate incentives around data privacy. Fines apply only in cases of intent or gross negligence, which some observers consider a high bar that may limit actual enforcement. The law also holds CEOs personally accountable, but critics worry about enforcement against large conglomerates like Samsung and potential evasion through shell companies.

hackernews · throw7 · Sep 18, 20:02 · [Discussion](https://news.ycombinator.com/item?id=49759466)

**Background**: South Korea's PIPA is the country's main data protection law, previously capping fines at 3% of revenue. The amendment significantly increases penalties to deter data breaches, aligning with global trends like the EU's GDPR. The law takes effect in September 2026, giving companies time to comply.

<details><summary>References</summary>
<ul>
<li><a href="https://databreaches.net/2026/09/10/korea-raises-data-breach-fines-to-10-of-revenue/">Korea raises data breach fines to 10 % of revenue - DataBreaches .Net</a></li>
<li><a href="https://www.techtimes.com/articles/321115/20260720/south-koreas-diplomatic-roster-exposed-zero-day-nearly-ten-months.htm">South Korea 's Diplomatic Roster Exposed by Zero-Day for Nearly Ten...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49759466">Korea raises data breach fines to 10 % of revenue | Hacker News</a></li>

</ul>
</details>

**Discussion**: Commenters largely welcomed the move as a necessary step to make corporations care about security, but some expressed skepticism about enforcement, citing the high bar of 'intent or gross negligence' and government hypocrisy (e.g., Berlin's breach). Others noted corporate evasion tactics like using shell companies to avoid liability.

**Tags**: `#data-privacy`, `#regulation`, `#security`, `#policy`, `#korea`

---

<a id="item-6"></a>
## [Rust Team Warns of Targeted Social-Engineering Attacks on Maintainers](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

On September 17, 2026, Adam Harvey and the crates security team published a warning that an ongoing campaign is targeting rust-lang members and owners of popular crates, using fake video-call job or contract offers to trick victims into installing malware or executing clipboard commands. The warning follows a confirmed supply chain attack in August 2026 that poisoned the arrayref crate and two related crates. This is an active, targeted threat against the human layer of the Rust supply chain, and because almost all software depends on open source, a single compromised maintainer can push malware to millions of downstream users. The August attack already reached crates with roughly 245 million downloads, showing the real-world blast radius of such campaigns. The attackers set up video calls framed as positive opportunities and then use them to get targets to install something (such as a purportedly missing audio codec) or run a command, for example by placing it on the clipboard. In the August incident, malicious versions arrayref 0.3.10, internment 0.8.7, and append-only-vec 0.1.9 added a typosquatted build-time dependency, proc-macro1, whose build script downloaded and ran a remote binary during cargo build; the crates were removed and the account locked, and researchers noted significant overlap with DPRK campaigns.

rss · Simon Willison · Sep 17, 23:59

**Background**: Rust's package registry, crates.io, hosts reusable libraries called crates, and a crate's maintainer holds publishing rights that let them release new versions to everyone who depends on it. A supply chain attack abuses that trust by compromising a maintainer's account or machine and publishing malicious code, which then runs in downstream projects. Social engineering is the use of psychological manipulation, rather than technical exploits, to persuade someone to perform an action or reveal information.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref: Significant Overlap with DPRK Campaigns | Wiz Blog</a></li>

</ul>
</details>

**Discussion**: The post's author, Simon Willison, argues that any software depending on open source has a network of humans who are potential attack vectors, and suggests dependency cooldowns — waiting a few days before upgrading to new releases — as the best current defense, hoping someone else spots the attack first.

**Tags**: `#security`, `#supply-chain`, `#rust`, `#open-source`, `#social-engineering`

---

<a id="item-7"></a>
## [Anthropic's Claude Code Hits GitHub Trending as Agentic Terminal Coding Tool](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic's Claude Code, an agentic coding tool that runs in the terminal, is trending on GitHub. It understands codebases and automates routine tasks, explains complex code, and handles git workflows through natural language commands, and can also be used in an IDE or by tagging @claude on GitHub. Claude Code represents a significant push into agentic coding, where AI agents autonomously handle multi-step development tasks rather than just autocompleting lines. Its terminal-first design and GitHub Trending presence signal strong developer interest that could reshape everyday workflows for engineers. Installation via npm is now deprecated; Anthropic recommends a curl install script for macOS/Linux, Homebrew cask, PowerShell script or WinGet for Windows. The repository also ships plugins that extend functionality with custom commands and agents, and Claude Code collects usage data such as code acceptance or rejection and conversation data.

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**Background**: Agentic coding refers to using AI agents powered by large language models to autonomously carry out software development tasks across the lifecycle, from code generation to debugging and testing. Claude Code is Anthropic's implementation of this idea, placing an AI agent directly in the developer's terminal so it can read the project, run commands, and edit files. Natural language codebase understanding means developers can ask questions about unfamiliar code in plain language instead of manually tracing files.

<details><summary>References</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code">Claude Code Tutorial: Setup and Refactoring in Practice | DataCamp</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer-tools`, `#agentic-coding`, `#terminal`, `#Anthropic`

---

<a id="item-8"></a>
## [NSA's Ghidra: Open-Source Reverse Engineering Framework](https://github.com/NationalSecurityAgency/ghidra) ⭐️ 8.0/10

Ghidra is a free, open-source software reverse engineering (SRE) framework developed by the NSA's Research Directorate, offering disassembly, decompilation, graphing, and scripting for Windows, macOS, and Linux. It supports many processor instruction sets and executable formats, and can be extended with Java or Python scripts. Ghidra provides a powerful, no-cost alternative to proprietary tools like IDA Pro, significantly lowering the barrier for security researchers, malware analysts, and students. Its open-source nature and NSA backing have made it a widely adopted standard in the reverse engineering community. Ghidra requires JDK 25 64-bit to run, and its decompiler component is written in C++ while the rest is Java-based. The project warns of known security vulnerabilities in certain versions, so users should check the security advisories before use.

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**Background**: Software reverse engineering is the process of analyzing compiled binaries to understand their structure and behavior, often used for security research, malware analysis, and vulnerability discovery. Ghidra was released by the NSA at the RSA Conference in March 2019, with source code published on GitHub a month later. It is written primarily in Java and includes a decompiler that can convert machine code back into a readable high-level representation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NationalSecurityAgency/ghidra">GitHub - NationalSecurityAgency/ ghidra : Ghidra is a software reverse...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ghidra_(software)">Ghidra (software)</a></li>

</ul>
</details>

**Tags**: `#reverse-engineering`, `#security`, `#NSA`, `#open-source`, `#disassembly`

---

<a id="item-9"></a>
## [Colibri: Pure C engine streams frontier MoE models from disk](https://github.com/JustVugg/colibri) ⭐️ 8.0/10

JustVugg released Colibri v1.11.0, a pure C, zero-dependency inference engine that runs frontier Mixture-of-Experts models ranging from 744B to 2.8T parameters on consumer hardware by streaming routed experts from disk. It currently supports nine model families, including GLM-5.2/5.3 (744B), Kimi K3 (2.8T), DeepSeek V4 Flash (284B), and Qwen3.6 (35B-A3B), each implemented as a single C file behind a unified `coli chat` / `coli serve` / `coli web` front end. This approach dramatically lowers the hardware barrier to running frontier-scale MoE models, potentially democratizing large-model inference for researchers and developers who lack datacenter GPUs. By treating storage, RAM, and VRAM as a single inference hierarchy, it points toward a future where model capability depends less on scarce, expensive hardware. Colibri keeps dense components like attention, shared experts, and embeddings resident in memory (about 17B parameters, 9.9 GB), while storing 21,504 routed experts (roughly 370 GB) entirely on disk and streaming them on demand. The project explicitly offers no SLA on speed but a hard guarantee on semantics: the default policy never silently changes model precision or router semantics, and a demo shows a 744B model running at 4 tok/s with 1.6s TTFT on 6× RTX 5090.

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**Background**: Mixture-of-Experts (MoE) models divide a large network into many specialized 'expert' sub-networks, activating only a small subset for each input token, which lets them scale to enormous parameter counts with far less compute per token than dense models. Because only a few experts are needed at any moment, the inactive experts can be stored on slower, cheaper storage and loaded on demand — a technique known as disk streaming. Colibri builds on this sparsity by treating VRAM, RAM, and disk as one memory hierarchy, similar in spirit to how llama.cpp popularized zero-dependency quantized inference.

<details><summary>References</summary>
<ul>
<li><a href="https://pasqualepillitteri.it/en/news/15985/disk-streaming-moe-models-laptop">Run 744B MoE models on a laptop with disk streaming, no GPU ...</a></li>
<li><a href="https://ai-beat.github.io/news/2026/07/colibri-moe-disk-streaming/">Streaming 744 Billion Parameters from Disk · AI Beat</a></li>
<li><a href="https://www.aitoolnet.com/JustVugg-colibri">Colibri - Tiny C Engine Runs 744B MoE Model on... - Aitoolnet</a></li>

</ul>
</details>

**Tags**: `#MoE`, `#inference`, `#C`, `#edge-computing`, `#LLM`

---

<a id="item-10"></a>
## [Google Research Releases TimesFM 3.0 Time-Series Foundation Model](https://github.com/google-research/timesfm) ⭐️ 8.0/10

Google Research has released TimesFM 3.0, a new checkpoint of its pretrained decoder-only foundation model for time-series forecasting, available as google/timesfm-3.0-pytorch on Hugging Face. The 3.0 release adds native multivariate forecasting, flexible past-only and past-and-future covariate support, and claims the top rank on fev-bench, TIME Benchmark, and GIFT-Eval. TimesFM 3.0 brings foundation-model-style zero-shot forecasting to multivariate and covariate-rich real-world problems, potentially reducing the need to train bespoke models for each forecasting task. Its integration into BigQuery ML, Google Sheets, and Vertex Model Garden signals that Google is pushing time-series foundation models into mainstream enterprise analytics. The source code remains Apache-2.0 and weights up to version 2.5 stay Apache-2.0, but the TimesFM 3.0 pretrained weights are released under a separate timesfm-non-commercial-license-v1.0 restricted to non-commercial, non-production use. Older 1.0 and 2.0 checkpoints are archived under the v1 subdirectory and can be loaded via pip install timesfm==1.3.0.

rss · GitHub Trending - Python · Sep 18, 23:47

**Background**: TimesFM (Time Series Foundation Model) is a pretrained model from Google Research, published at ICML 2024, that forecasts time series it has never seen before without task-specific training, similar to how large language models predict the next word. It is built as a decoder-only attention model with input patching, pretrained on a large corpus of roughly 100 billion real-world time points. Time-series forecasting is widely used in business for predicting inventory needs, energy demand, and similar quantities.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/timesfm">GitHub - google-research/ timesfm : TimesFM ( Time Series Foundation...</a></li>
<li><a href="https://arxiv.org/abs/2310.10688">[2310.10688] A decoder-only foundation model for time-series forecasting</a></li>
<li><a href="https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/">A decoder-only foundation model for time-series forecasting</a></li>

</ul>
</details>

**Tags**: `#time-series`, `#foundation-model`, `#forecasting`, `#google-research`, `#machine-learning`

---

<a id="item-11"></a>
## [First End-to-End Study of Web Search by Conversational LLM Agents](https://arxiv.org/abs/2609.19244) ⭐️ 8.0/10

A new arXiv paper (2609.19244) presents the first end-to-end characterization of web search behavior across four major conversational platforms: ChatGPT, Claude, Grok, and DeepSeek. Combining real-world user interactions (in vivo) with controlled API-based experiments (in vitro), it analyzes when agents decide to search, how they formulate queries, which domains their search engines favor, and how they ground responses in results. As conversational agents increasingly rely on web search to answer questions, understanding their search decisions and grounding behavior is critical for reliability and attribution. The finding that more frequent search does not necessarily improve response quality, and that some claims rely on uncited results, has direct implications for the design of future AI agents and search tools. The study finds that web-search invocation decisions vary substantially across platforms and models, and that agents employ different complex querying strategies. Platform-specific search engines tend to return results from their preferred domains, and although responses are largely grounded in search results, some claims rely on uncited results, raising concerns about attribution and reliability.

rss · arXiv - AI · Sep 18, 04:00

**Background**: Conversational LLM agents are AI systems that can autonomously decide to call tools such as web search to answer user questions, a pattern often called agentic search or retrieval-augmented generation (RAG). In vivo experiments observe real user interactions, while in vitro experiments use controlled API calls to isolate model behavior. This paper is the first to combine both approaches to characterize the full search lifecycle across multiple commercial platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.14253">[2510.14253] Towards Agentic Self-Learning LLMs in Search ... Agentic Retrieval Overview - Azure AI Search | Microsoft Learn Agentic search | OpenSearch Documentation GitHub - YunjiaXi/Awesome-Search-Agent-Papers LLM Agent Benchmarks (September 2026): 26 Agentic Evals ... Best LLMs for Agentic — September 2026 Leaderboard Awesome RL-based Agentic Search Papers - GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview">Agentic Retrieval Overview - Azure AI Search | Microsoft Learn</a></li>
<li><a href="https://www.firecrawl.dev/glossary/web-search-apis/reduce-hallucinations-search-grounded-llm-responses">How do I reduce hallucinations when using search - grounded LLM ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#web search`, `#conversational AI`, `#agentic search`, `#empirical study`

---

<a id="item-12"></a>
## [AutoTuring Tests Whether AI Agents Truly Understand Computer Architecture](https://arxiv.org/abs/2609.19387) ⭐️ 8.0/10

AutoTuring presents a controlled experiment in which the same AI agent optimizes the same 15-dimensional accelerator design space twice: once as named architectural knobs with simulator counters, and once as anonymous variables on [0,1], with the evaluator, legal space, and reachable optima held identical. On a nine-kernel FP16 GEMM basket, the architect agent beats a modeled H200 by 5.4% and its blind counterpart by 12.3% on average while using 70.1% fewer simulator calls. This methodology isolates whether AI agents genuinely reason about computer architecture or merely search over anonymous variables, a distinction that determines whether their skills transfer to the next architecture. It offers a clean measurement of 'meaning' in agent reasoning that could reshape how AI-for-systems and hardware design agents are evaluated. The paper reports preliminary findings based on only five to six runs per condition on a single modeled accelerator, and notes that a critic loop recovers most of the gap for the blind agent while buying the architect nothing, suggesting architectural knowledge and structured critique act as substitutes rather than complements. The authors explicitly frame the comparison itself, not the accelerator, as the contribution.

rss · arXiv - AI · Sep 18, 04:00

**Background**: AI agents are increasingly used to design hardware accelerators, and reports of improved designs cannot explain why the improvement occurred. An agent may be reasoning about the machine, or it may simply be searching competently over knobs whose meaning it never recovers, and only the first case transfers to a new architecture. Existing evaluations cannot distinguish these cases because they vary the agent while holding the problem framing fixed; AutoTuring does the opposite by varying only the semantic framing.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.19387v1">Do AI Agents Understand Computer Architecture? - arXiv.org</a></li>
<li><a href="https://arxiv.org/pdf/2510.19577">gem5 Co-Pilot: AI Assistant Agent for Architectural Design ...</a></li>
<li><a href="https://arxiv.org/html/2601.01743v1">AI Agent Systems: Architectures, Applications, and Evaluation</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#computer architecture`, `#hardware design`, `#evaluation methodology`, `#AutoML`

---

<a id="item-13"></a>
## [MAGS: Multi-Agent Framework Adds Formal Safety Guarantees to LLM Code](https://arxiv.org/abs/2609.19391) ⭐️ 8.0/10

Researchers introduced MAGS, a unified multi-agent framework that generates executable programs with formal safety guarantees by using Dafny as a verification-aware intermediate representation. MAGS freezes human-audited APIs and safety requirements, translates LLM-generated code into Dafny, repairs violations using verifier feedback, and compiles verified programs back into executable code, achieving a 100% success rate across 220 examples spanning 100 CUDA kernels, 100 terminal scripts, and 20 robotic-arm tasks. As LLM coding agents generate increasingly complex programs at a scale that makes thorough human review impractical, MAGS addresses a critical safety gap by providing machine-checkable guarantees rather than relying on probabilistic detection methods like fuzz testing or LLM-as-a-Verifier. This approach could significantly impact AI safety and software engineering by enabling trustworthy deployment of agentic code generation in safety-critical domains. The framework achieves non-trivial safety guarantees against frozen specifications across all 220 examples, but independent evaluations reveal failures when the auto-formalized semantics do not fully capture the target behavior. This limitation highlights the ongoing challenge of ensuring that formal specifications accurately reflect real-world requirements.

rss · arXiv - AI · Sep 18, 04:00

**Background**: Dafny is a verification-aware programming language with native support for specifications and a static program verifier that continuously checks code against its specifications. Formal verification provides machine-checkable guarantees over specified properties but traditionally demands substantial manual specification and proof engineering. Recent work has proposed using Dafny as a verification-aware intermediate language for LLM code generation, where the LLM first generates Dafny code that can be automatically validated before compilation to a target language.

<details><summary>References</summary>
<ul>
<li><a href="https://dafny.org/">Dafny</a></li>
<li><a href="https://arxiv.org/abs/2501.06283">[2501.06283] Dafny as Verification-Aware Intermediate ...</a></li>
<li><a href="https://arxiv.org/abs/2607.05391">[2607.05391] LLM-as-a-Verifier: A General-Purpose ...</a></li>

</ul>
</details>

**Tags**: `#formal-verification`, `#multi-agent-systems`, `#LLM-code-generation`, `#AI-safety`, `#Dafny`

---

<a id="item-14"></a>
## [RF-CNNs Repurpose Wireless Hardware for Edge AI Inference](https://arxiv.org/abs/2609.19279) ⭐️ 8.0/10

Researchers introduced radio-frequency convolutional neural networks (RF-CNNs), which repurpose the frequency mixer already present in every wireless radio to perform CNN inference. They experimentally demonstrated deep CNNs up to 26.4 million parameters and nine layers, achieving near full-precision performance for wireless signal classification, image classification, and controllable image generation. This approach could eliminate the need for dedicated edge AI accelerators, which add size, weight, power, and cost (SWaP-C) to already constrained devices like smartphones, wearables, and drones. By leveraging deployed wireless infrastructure, it may bring efficient, state-of-the-art AI inference to billions of connected devices. The system maps multi-channel convolutions onto frequency tones for a passive mixer to execute in a single pass, with weights arriving over the air and analog hardware shared with communication. Energy consumption drops to 0.72 femtojoules per multiply-accumulate, two orders of magnitude less than an added digital processor, with the edge device spending energy only on data preparation and readout.

rss · arXiv - Machine Learning · Sep 18, 04:00

**Background**: Edge devices often lack the computing power for modern neural networks, and adding accelerators increases SWaP-C constraints. A frequency mixer, a standard component in wireless radios, multiplies signals in time, which mathematically performs convolution in the frequency domain. RF-CNNs exploit this property to run CNN inference directly on existing communication hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.19279">[2609.19279] Radio-Frequency Convolutional Neural Networks</a></li>
<li><a href="https://arxiv.org/html/2609.19279">Radio-Frequency Convolutional Neural Networks</a></li>

</ul>
</details>

**Tags**: `#edge-ai`, `#hardware-acceleration`, `#rf-computing`, `#neural-networks`, `#signal-processing`

---

<a id="item-15"></a>
## [SonoBase: Open Ultrasound Foundation Model Trained on 456k Images](https://arxiv.org/abs/2609.19230) ⭐️ 8.0/10

Researchers released SonoCorpus, an open ultrasound dataset of 456,963 images and 1,626,085 expert masks drawn from 53 public datasets across 24 clinical applications and 17 countries, along with SonoBase, an interactive segmentation foundation model pretrained on it. SonoBase outperformed SAM2, MedSAM2, and MedSAM3 on all fifteen evaluation datasets covering new organs, devices, operators, and geographies, and matched per-dataset specialist models trained on the same data. Ultrasound is the most widely deployed imaging modality worldwide, yet clinical AI has remained fragmented into narrow single-task models that break down when devices, operators, or anatomies change. A robust open foundation model could enable reliable clinical measurements such as ejection fraction and fetal head circumference even on handheld probes operated by minimally trained users in low- and middle-income countries. Ejection fraction derived from SonoBase segmentations fell within inter-observer variability (6.63% error) with fewer misclassifications at the defibrillator-candidacy threshold than promptable baselines (13% versus 18–42%), and fetal head-circumference (1.81 mm) and gestational-age (1.2 days) errors also fell below inter-observer variability. Where a baseline failed outright (one in four test cases), SonoBase recovered a usable segmentation in 81% of them, and just five labeled examples helped it adapt to a new setting; all checkpoints, optimizer states, data-split indices, deduplication hashes, and starter code were released.

rss · arXiv - Computer Vision · Sep 18, 04:00

**Background**: Foundation models are large neural networks pretrained on broad data that can be adapted to many downstream tasks, and in medical imaging they are typically built by adapting segmentation architectures such as SAM2 (Segment Anything Model 2) to clinical data. Ultrasound is notoriously difficult for such models because images vary greatly with probe type, operator technique, and patient anatomy, causing domain shift that degrades performance. Prior medical variants like MedSAM2 and MedSAM3 add medical data but still struggle on fully external ultrasound data, which is the gap SonoBase targets.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/AlfredQin/sonobase">GitHub - AlfredQin/sonobase: SonoBase: interactive ultrasound segmentation foundation model, pretrained on SonoCorpus · GitHub</a></li>
<li><a href="https://arxiv.org/html/2509.11752">A Fully Open and Generalizable Foundation Model for Ultrasound ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-658-51100-5_8">Foundation Models in Medical Image Segmentation | Springer Nature...</a></li>

</ul>
</details>

**Tags**: `#medical-imaging`, `#foundation-models`, `#ultrasound`, `#segmentation`, `#domain-adaptation`

---

<a id="item-16"></a>
## [Cells That Survive Programmed Death Rebuild Damaged Tissue](https://www.sciencedaily.com/releases/2026/09/260917003722.htm) ⭐️ 8.0/10

Scientists have identified a population of cells that can initiate programmed cell death (apoptosis), survive the process, and then rapidly rebuild damaged tissue. Their descendants show markedly increased resistance to future damage, revealing a mechanism with dual implications for healing and cancer relapse. The finding could reshape regenerative medicine by showing how the body might be coaxed to heal faster, while also offering a new explanation for why tumors can return after therapy. It suggests that the same survival-and-resistance program that aids repair may be hijacked by cancer cells to evade treatment. The cells survive a process normally considered irreversible cell suicide, and their descendants inherit heightened resistance to subsequent damage. This dual nature means any therapy targeting these cells must balance promoting tissue repair against the risk of fostering treatment-resistant cancer.

rss · ScienceDaily Health · Sep 18, 12:30

**Background**: Apoptosis, or programmed cell death, is a tightly regulated self-destruct mechanism that removes damaged or unwanted cells and is generally thought to be irreversible once triggered. Cancer relapse after treatment often involves a small subpopulation of cells that survive therapy and develop resistance, a phenomenon linked to tumor heterogeneity and markers such as YAP1. This discovery connects those two areas by showing that survival of apoptosis can produce a repair-capable, damage-resistant cell lineage.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencealert.com/APOPTOSIS-PROGRAMMED-CELL-DEATH-MECHANISM-TRIGGER-WAVE">Scientists Have Just Measured The 'Speed of Death ' of a Cell And...</a></li>
<li><a href="https://medicalxpress.com/news/2026-05-biomarker-chemotherapy-resistance-relapsed-lung.html">Researchers find biomarker of chemotherapy resistance in relapsed ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9558974/">Current Landscape of Therapeutic Resistance in Lung Cancer and...</a></li>

</ul>
</details>

**Tags**: `#cell biology`, `#regenerative medicine`, `#cancer research`, `#apoptosis`, `#tissue repair`

---