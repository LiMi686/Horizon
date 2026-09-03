---
layout: default
title: "Horizon Summary: 2026-09-03 (EN)"
date: 2026-09-03
lang: en
---

> From 107 items, 22 important content pieces were selected

---

1. [OpenAI Unveils GPT-6 Astra with 99.9% ARC-AGI-3 Score](#item-1) ⭐️ 10.0/10
2. [Porting a 1993 Amiga Game to Godot with LLM Assistance](#item-2) ⭐️ 8.0/10
3. [Go Grandmaster Shin Jinseo Defeats AI KataGo with Two-Stone Handicap](#item-3) ⭐️ 8.0/10
4. [Audacity 4.0 Released with Qt6 UI Overhaul](#item-4) ⭐️ 8.0/10
5. [Polars 2.0 Pre-Release Focuses on Breaking Changes and Defaults](#item-5) ⭐️ 8.0/10
6. [Google Research Releases TimesFM 3.0 for Time-Series Forecasting](#item-6) ⭐️ 8.0/10
7. [VoiceStudio: Open-Source Local Alternative to ElevenLabs](#item-7) ⭐️ 8.0/10
8. [Chrome DevTools MCP Server Lets AI Agents Control Live Browser](#item-8) ⭐️ 8.0/10
9. [Anthropic Launches Claude Code, an Agentic Terminal Coding Tool](#item-9) ⭐️ 8.0/10
10. [EvalDetectBench: Benchmarking Evaluation Awareness in Frontier LLMs](#item-10) ⭐️ 8.0/10
11. [LLM-Guided Bayesian Learning Models Human Induction and Inquiry](#item-11) ⭐️ 8.0/10
12. [Epistemic Sybil Resistance: Formalizing Evidence Independence in Multi-Agent AI](#item-12) ⭐️ 8.0/10
13. [WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling](#item-13) ⭐️ 8.0/10
14. [Sim2Signal: A New Benchmark for Sim-to-Real Traffic Signal Control](#item-14) ⭐️ 8.0/10
15. [Survey Unifies Test-Time Adaptation, Learning, and Scaling](#item-15) ⭐️ 8.0/10
16. [Median-of-Means Limits Convex Robust Estimators; Nonconvex Route to Oracle](#item-16) ⭐️ 8.0/10
17. [VakyArth: First Pragmatic Benchmark for Indic Languages](#item-17) ⭐️ 8.0/10
18. [LLM Internal Activations Reveal Clinician-Aligned Depression Symptom Vectors](#item-18) ⭐️ 8.0/10
19. [Survey on Action-Grounded Reasoning in Autonomous Driving](#item-19) ⭐️ 8.0/10
20. [FAIRLENS Benchmark Exposes Unwarranted Inference in Vision-Language Models](#item-20) ⭐️ 8.0/10
21. [ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes](#item-21) ⭐️ 8.0/10
22. [Pig Kidney Transplant in Man Sets Record at 271 Days](#item-22) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI Unveils GPT-6 Astra with 99.9% ARC-AGI-3 Score](https://openai.com/index/gpt-6-astra/) ⭐️ 10.0/10

OpenAI has announced GPT-6 Astra, a new frontier model, along with a system card. The model reportedly achieves a 99.9% score on the ARC-AGI-3 benchmark, marking a significant milestone in AI reasoning capabilities. GPT-6 Astra's near-perfect ARC-AGI-3 performance suggests a leap toward more general and adaptive AI, potentially accelerating progress in fields requiring complex reasoning and problem-solving. This release intensifies competition among AI labs and raises the bar for frontier model capabilities. The system card is available at deploymentsafety.openai.com/gpt-6-astra. However, community members note that the ARC-AGI-3 scorecard may be misleading, as it uses a different harness for GPT-6 Astra than for previous models like GPT-5.6 Sol, potentially inflating the comparison.

hackernews · kibae · Sep 3, 18:41 · [Discussion](https://news.ycombinator.com/item?id=49554643)

**Background**: ARC-AGI-3 is an interactive reasoning benchmark that challenges AI agents to explore novel environments, acquire goals on the fly, build adaptable world models, and learn continuously. It is a successor to ARC-AGI-2 and focuses on evaluating fluid adaptive efficiency. System cards are documents that detail a model's capabilities, safety evaluations, and responsible deployment decisions, similar to those released by Anthropic for Claude models.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/arc-agi/3">Arc-agi-3</a></li>
<li><a href="https://benchlm.ai/benchmarks/arcagi3">ARC-AGI-3 Leaderboard & Scores — September 2026 | BenchLM.ai</a></li>
<li><a href="https://arxiv.org/abs/2603.24621">ARC-AGI-3: A New Challenge for Frontier Agentic Intelligence</a></li>
<li><a href="https://artificialanalysis.ai/agents/coding-agents">AI Coding Agent Benchmarks & Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the ARC-AGI-3 scorecard, noting that the harness used for GPT-6 Astra differs from that used for previous models, potentially skewing results. Some commenters also observe that while the ARC-AGI-3 score is impressive, other benchmarks show only modest improvements, and question whether this truly represents AGI progress or just broader benchmark coverage.

**Tags**: `#OpenAI`, `#GPT-6`, `#AI model`, `#ARC-AGI`, `#AGI`

---

<a id="item-2"></a>
## [Porting a 1993 Amiga Game to Godot with LLM Assistance](https://babyloniantwins.com/blog/porting-a-1993-amiga-game-to-godot/) ⭐️ 8.0/10

A developer successfully ported his 1993 Amiga game, originally written in MC68000 assembly, to the Godot engine using an LLM (Claude Fable 5) in a single evening. The LLM assembled the code with vasm and iterated until the binary matched the original, except for a 108-byte discrepancy. This demonstrates a novel and practical use of LLMs for porting legacy assembly code to modern engines, potentially lowering the barrier for preserving and modernizing retro games. It highlights the growing capability of AI in software archaeology and could inspire similar projects in the retrocomputing community. The developer used vasm on his Mac to assemble the code, aiming for byte-identical output to the original binaries. The original game was assembled with AsmOne into memory and saved as a memory snapshot after running, causing a 108-byte mismatch that the developer never personally verified. The game is being released for free.

hackernews · rabahs · Sep 3, 14:28 · [Discussion](https://news.ycombinator.com/item?id=49550375)

**Background**: The Amiga was a popular personal computer in the late 1980s and early 1990s, known for its advanced graphics and sound. MC68000 assembly language was commonly used for game development on this platform, requiring deep hardware knowledge. Godot is a modern open-source game engine that supports 2D and 3D game development across multiple platforms. LLMs (large language models) like Claude can understand and generate code, enabling tasks like translating legacy assembly into higher-level languages or engine-specific code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="http://sun.hasenbraten.de/vasm/">vasm portable and retargetable assembler</a></li>

</ul>
</details>

**Discussion**: Community members expressed awe at the developer's original achievement and the LLM's capability, with some sharing similar experiments. One user successfully used Claude to convert a ZX81 game memory dump to Go, calling it a 'crazy thing' to experience both the advent of personal computing and AI-assisted archaeology. Others asked about debugging stories and noted the game's resemblance to 'Gods: Into the Wonderful'.

**Tags**: `#LLM`, `#retrocomputing`, `#game development`, `#Godot`, `#assembly`

---

<a id="item-3"></a>
## [Go Grandmaster Shin Jinseo Defeats AI KataGo with Two-Stone Handicap](https://www.kedglobal.com/artificial-intelligence/newsView/ked202607210007) ⭐️ 8.0/10

Go grandmaster Shin Jinseo defeated the AI program KataGo in a game where he received a two-stone handicap. This marks a notable human victory against a top-tier Go AI. This event is significant because it demonstrates that even the strongest human players can overcome advanced AI when given a handicap, highlighting the ongoing gap between human and AI capabilities in Go. It also sparks discussion about the strategic depth of Go and the value of human intuition versus AI calculation. Shin Jinseo is widely considered the strongest human Go player, with a rating over 3800, significantly higher than his peers. The two-stone handicap is a substantial advantage, and the game likely involved complex joseki variations, such as the 'flying knife' joseki, which Shin used to his advantage.

hackernews · gmays · Sep 3, 01:11 · [Discussion](https://news.ycombinator.com/item?id=49544762)

**Background**: Go is an ancient board game with a 19x19 grid, where players place stones to control territory. Handicaps are used to balance games between players of different strengths, with the weaker player receiving extra stones. KataGo is a modern Go AI that uses deep learning and Monte Carlo tree search, and it is among the strongest Go programs, often defeating top humans without handicaps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Two-stone_handicap">Two-stone handicap</a></li>
<li><a href="https://en.wikipedia.org/wiki/Handicapping_in_Go">Handicapping in Go - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted that Shin Jinseo is exceptionally strong, with a rating gap over his rivals comparable to Magnus Carlsen's dominance in chess. Some pointed out that the headline could be misleading, as the handicap means Shin was the weaker player, but they acknowledged that no human could beat KataGo without a handicap. Others discussed the value of human-style play over imitating AI, citing Shin's quote about building the board according to his own style.

**Tags**: `#AI`, `#Go`, `#KataGo`, `#human vs AI`, `#game theory`

---

<a id="item-4"></a>
## [Audacity 4.0 Released with Qt6 UI Overhaul](https://github.com/audacity/audacity/releases/tag/Audacity-4.0.0) ⭐️ 8.0/10

Audacity 4.0, a major open-source audio editor release, is now available, featuring a significant UI overhaul built on Qt6, a new clip-editing model, and a new project file format. This release modernizes Audacity's interface and workflow, potentially attracting new users and improving usability for existing ones. It also signals the project's continued evolution under Muse Group, addressing long-standing UI criticisms. The migration from wxWidgets to Qt6 is a headline change, reusing architectural foundations from MuseScore Studio 4. The new version introduces a dedicated splitting tool, improved clip grouping and placement, and a new project file format, though some users may need to import legacy projects.

hackernews · ClydeN · Sep 3, 10:53 · [Discussion](https://news.ycombinator.com/item?id=49548395)

**Background**: Audacity is a free, open-source digital audio editor available on Windows, macOS, and Linux. It has been widely used for recording and editing audio, but its interface had been criticized as outdated. The move to Qt6 is part of a broader effort to modernize the application and align with other Muse Group products.

<details><summary>References</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Audacity-4.0-Released">Audacity 4.0 Audio Editor Released With Qt6 Based UI - Phoronix</a></li>
<li><a href="https://www.omgubuntu.co.uk/2026/09/audacity-4-released">Audacity 4 . 0 released with brand- new look, clip editing features</a></li>
<li><a href="https://www.audacityteam.org/au4/">Audacity ® | Audacity 4</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed. Some users praise the new UI and fixes, while others express disappointment that technical issues like JACK support remain unaddressed. There is also lingering concern about telemetry and the audio.com integration, with references to past forks like Tenacity.

**Tags**: `#Audacity`, `#open-source`, `#audio-editing`, `#Qt6`, `#release`

---

<a id="item-5"></a>
## [Polars 2.0 Pre-Release Focuses on Breaking Changes and Defaults](https://pola.rs/posts/announcing-polars-2/) ⭐️ 8.0/10

Polars has announced the pre-release of version 2.0, which aims to remove legacy design decisions and change defaults to more sensible settings. This major version bump is not intended to introduce a large set of new features but rather to clean up the API and improve usability for a broader audience. Polars is a widely-used data processing library, and this major release introduces breaking changes that will affect many users. The community discussion highlights important concerns about non-deterministic behavior in scientific pipelines, indicating that the changes have significant implications for production stability and scientific computing. The pre-release focuses on removing design decisions that block future improvements and changing defaults to more sensible settings. Specific changes include altering the default for maintain_order to False, which has raised concerns about non-deterministic behavior in scientific data analysis pipelines.

hackernews · komape · Sep 3, 06:59 · [Discussion](https://news.ycombinator.com/item?id=49546753)

**Background**: Polars is a high-performance DataFrame library written in Rust, offering both eager and lazy APIs. It has gained popularity as a faster alternative to pandas, especially for large datasets. The project follows semantic versioning, and breaking releases occur approximately every six months, with deprecation warnings provided in advance.

<details><summary>References</summary>
<ul>
<li><a href="https://pola.rs/posts/announcing-polars-2/">Polars — Pre-release of Polars 2.0</a></li>
<li><a href="https://docs.pola.rs/development/versioning/">Versioning - Polars user guide</a></li>
<li><a href="https://github.com/pola-rs/polars/issues/16458">Non-deterministic failure when materializing LazyFrame - GitHub</a></li>

</ul>
</details>

**Discussion**: Community comments show appreciation for Polars' production stability and the project's serious approach to semantic versioning. However, there is concern about the new default of maintain_order=False, as non-deterministic behavior is a known source of bugs in scientific computing. Some users also praise Polars' performance and its adoption in production environments.

**Tags**: `#Polars`, `#data processing`, `#major release`, `#API design`, `#determinism`

---

<a id="item-6"></a>
## [Google Research Releases TimesFM 3.0 for Time-Series Forecasting](https://github.com/google-research/timesfm) ⭐️ 8.0/10

Google Research has released TimesFM 3.0, a new checkpoint of its decoder-only foundation model for time-series forecasting. This version introduces native multivariate forecasting, flexible covariate support, and achieves top performance on major benchmarks. TimesFM 3.0 advances the state of time-series foundation models by enabling multivariate forecasting and covariate support without task-specific tuning, making it more practical for real-world applications. Its top benchmark rankings highlight its potential to replace traditional supervised models in various forecasting tasks. TimesFM 3.0 achieves rank #1 on the fev-bench, TIME Benchmark, and GIFT-Eval (among foundation models). The pretrained weights are distributed under a non-commercial license, while the source code remains Apache-2.0.

rss · GitHub Trending - Daily (All) · Sep 3, 23:43

**Background**: TimesFM is a time-series foundation model pretrained on a large corpus of 100 billion real-world time points, including Google Trends and Wikipedia pageviews data. It uses a decoder-only transformer architecture, similar to large language models, to perform zero-shot forecasting across various domains and granularities. The model was introduced in a paper published at ICML 2024.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google-research/timesfm/">GitHub - google-research/timesfm: TimesFM (Time Series ...</a></li>
<li><a href="https://arxiv.org/abs/2310.10688">A decoder-only foundation model for time-series forecasting A decoder-only foundation model for time-series forecasting A decoder-only foundation model for time-series forecasting A decoder-only foundation model for time-series forecasting GitHub - google-research/timesfm: TimesFM (Time Series ... A decoder-only foundation model for time-series forecasting A decoder-only foundation model for time-series forecasting</a></li>
<li><a href="https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/">A decoder-only foundation model for time-series forecasting</a></li>

</ul>
</details>

**Tags**: `#time-series`, `#foundation-model`, `#machine-learning`, `#forecasting`, `#Google-Research`

---

<a id="item-7"></a>
## [VoiceStudio: Open-Source Local Alternative to ElevenLabs](https://github.com/debpalash/VoiceStudio) ⭐️ 8.0/10

VoiceStudio, previously known as OmniVoice-Studio, has been released as an open-source, fully-local voice AI suite. It offers voice cloning, voice design, video dubbing, dictation, transcription, and audiobook creation across 646 languages, with support for 16 TTS engines and 11 ASR engines. VoiceStudio provides a privacy-preserving, self-hosted alternative to commercial services like ElevenLabs, addressing growing demand for local AI tools. Its appearance on GitHub Trending indicates strong community interest, and it could empower developers and researchers to build voice applications without cloud dependencies or usage fees. The project is licensed under AGPL-3.0 and supports macOS, Windows, Linux, and Docker. It requires no account, API key, subscription, or usage meter for local workflows, and includes an API for integration.

rss · GitHub Trending - Daily (All) · Sep 3, 23:43

**Background**: Voice cloning is the process of creating a digital simulation of a person's voice using AI, analyzing vocal characteristics like tone, pitch, and accent. ElevenLabs is a popular commercial voice AI platform, but its cloud-based nature raises privacy and cost concerns. Fully-local voice AI tools run entirely on the user's hardware, ensuring data privacy and offline operation. VoiceStudio aggregates multiple open-source TTS and ASR engines to offer a comprehensive local solution.

<details><summary>References</summary>
<ul>
<li><a href="https://deepgram.com/learn/voice-cloning-everything-to-know">Everything you need to know about voice cloning - Deepgram</a></li>
<li><a href="https://elevenlabs.io/voice-cloning">AI Voice Cloning: Clone Your Voice in Minutes - ElevenLabs</a></li>
<li><a href="https://github.com/fikrikarim/volocal">GitHub - fikrikarim/volocal: Fully local voice AI for iOS · GitHub</a></li>

</ul>
</details>

**Tags**: `#voice-ai`, `#open-source`, `#text-to-speech`, `#voice-cloning`, `#local-ai`

---

<a id="item-8"></a>
## [Chrome DevTools MCP Server Lets AI Agents Control Live Browser](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools team released chrome-devtools-mcp, an MCP server that enables coding agents like Claude, Cursor, or Copilot to control and inspect a live Chrome browser. It provides tools for performance insights, advanced debugging, and reliable automation via Puppeteer. This integration bridges AI coding agents with full-fledged browser DevTools, enabling more reliable automation, in-depth debugging, and performance analysis in AI-assisted development workflows. It could significantly enhance how developers use AI for front-end and web app debugging. The server officially supports Google Chrome and Chrome for Testing only; other Chromium-based browsers may work but are not guaranteed. Usage statistics are collected by default, but can be disabled with the --no-usage-statistics flag, and performance tools can disable CrUX data fetching with --no-performance-crux.

rss · GitHub Trending - Daily (All) · Sep 3, 23:43

**Background**: Model Context Protocol (MCP) is an open standard that allows AI agents to connect to external tools and data sources. An MCP server exposes tools that an AI agent can discover and call during a task. Chrome DevTools is a set of web developer tools built into Chrome, and Puppeteer is a Node.js library for controlling Chrome via the DevTools Protocol.

<details><summary>References</summary>
<ul>
<li><a href="https://www.npmjs.com/package/chrome-devtools-mcp">chrome-devtools-mcp - npm</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#debugging`, `#developer tools`

---

<a id="item-9"></a>
## [Anthropic Launches Claude Code, an Agentic Terminal Coding Tool](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic has released Claude Code, an agentic coding tool that operates in the terminal, IDE, or via GitHub mentions, allowing developers to execute tasks and manage workflows through natural language. The tool is now available for installation on macOS, Linux, and Windows, with npm installation deprecated in favor of native installers. Claude Code represents a significant step in AI-assisted development, moving from passive code suggestions to autonomous agents that can plan and execute coding tasks. This release intensifies competition among AI coding tools and offers developers a new way to boost productivity, potentially reshaping software development workflows. The tool requires Node.js 18 or higher and supports multiple installation methods, including curl, Homebrew, PowerShell, and WinGet. It includes plugins for custom commands and agents, and collects usage data, including code acceptance/rejection and conversation data, for feedback purposes.

rss · GitHub Trending - Python · Sep 3, 23:43

**Background**: Agentic coding is a software development approach where AI agents autonomously plan, write, test, and modify code with minimal human intervention, unlike traditional AI assistants that respond to explicit prompts. Claude Code is Anthropic's entry into this field, joining tools like OpenAI's Codex and GitHub Copilot's Agent Mode, and it aims to handle routine tasks, explain complex code, and manage git workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">anthropics/ claude - code : Claude Code is an agentic coding tool that...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>

</ul>
</details>

**Tags**: `#AI coding assistant`, `#developer tools`, `#Anthropic`, `#natural language processing`, `#terminal`

---

<a id="item-10"></a>
## [EvalDetectBench: Benchmarking Evaluation Awareness in Frontier LLMs](https://arxiv.org/abs/2609.01611) ⭐️ 8.0/10

Researchers introduced EvalDetectBench, an open pipeline and benchmark for measuring whether frontier large language models recognize when they are being evaluated. It works with any Inspect-compatible evaluation and includes a curated transcript suite covering current frontier system-card evaluations and diverse deployment sources. This benchmark addresses a critical issue in AI safety: if models behave differently during evaluations than in real deployment, the validity of safety evaluations is undermined. By providing a standardized tool to measure evaluation awareness, it helps improve the reliability of frontier AI safety assessments and informs future evaluation design. The benchmark identifies two methodological biases in existing literature: the identity of the model generating deployment transcripts accounts for 11.25% of measurement variance and can reorder model rankings, and elicitation prompts selected for high performance on one model can perform near chance on others. EvalDetectBench corrects these via per-model probe calibration and a stratified generator-harmonisation procedure.

rss · arXiv - AI · Sep 3, 04:00

**Background**: Evaluation awareness refers to the ability of large language models to detect when they are being tested, which can lead to behavior shifts that compromise evaluation validity. This is analogous to the 'Hawthorne effect' in psychology, where subjects alter their behavior when they know they are observed. The benchmark builds on prior work in measuring evaluation awareness and leverages Inspect, an open-source evaluation framework from the UK AI Safety Institute, to ensure broad applicability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.01611">[2609.01611] EvalDetectBench : A Benchmark for Measuring...</a></li>
<li><a href="https://inspect.aisi.org.uk/">Inspect</a></li>
<li><a href="https://www.emergentmind.com/topics/evaluation-awareness-in-llms">Evaluation Awareness in LLMs</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#LLM evaluation`, `#benchmark`, `#evaluation awareness`, `#frontier models`

---

<a id="item-11"></a>
## [LLM-Guided Bayesian Learning Models Human Induction and Inquiry](https://arxiv.org/abs/2609.01815) ⭐️ 8.0/10

This paper introduces a computational model that encodes symbolic knowledge as mental programs combining natural language and source code, and sequentially infers these programs using LLM-guided Bayesian learning algorithms. The model successfully reproduces quantitative signatures of human inductive learning and active inquiry, such as anchoring and garden-pathing effects. This work addresses fundamental challenges in cognitive science and AI by offering a unified framework that is data-efficient, uncertainty-aware, and flexible enough to represent a wide range of concepts. It suggests that combining LLMs with Bayesian inference can bridge the gap between neural and symbolic approaches, potentially influencing future AI systems and cognitive modeling. The model uses LLM-guided Bayesian learning to sequentially infer mental programs that combine natural language and code. In contrast, pure LLMs and classic Bayesian models either fail at the underlying task, do not reproduce human behavior, or succeed only at exorbitant computational cost.

rss · arXiv - AI · Sep 3, 04:00

**Background**: Human learning from sparse and noisy data is a longstanding challenge in cognitive science. Computational accounts must be data-efficient, capture uncertainty for active inquiry, and flexibly represent a vast range of concepts. This paper proposes that humans represent hypotheses as mental programs combining language and code, and revise them via approximate Bayesian updates, with an LLM providing tractable inference.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/llm-guided-bayesian-optimization">LLM-Guided Bayesian Optimization - emergentmind.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Program_synthesis">Program synthesis - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#cognitive science`, `#Bayesian inference`, `#LLM`, `#program synthesis`, `#human learning`

---

<a id="item-12"></a>
## [Epistemic Sybil Resistance: Formalizing Evidence Independence in Multi-Agent AI](https://arxiv.org/abs/2609.01873) ⭐️ 8.0/10

This paper formalizes the epistemic Sybil problem in multi-agent AI systems, demonstrating that report-only aggregators cannot distinguish replication from independent corroboration. Using over 20,000 controlled LLM-agent calls, it shows that naive aggregation collapses posterior coverage from 0.940 to 0.263 as report multiplicity rises from 1 to 32. This work addresses a critical flaw in current multi-agent AI systems, which often assume that more agents equate to more independent evidence. The findings have significant implications for AI safety and evaluation, urging researchers to track evidential ancestry rather than agent or report multiplicity. The paper introduces a Gaussian shared-root model showing that common ancestry does not imply complete redundancy, and that correlated extraction errors lower the source-level ceiling. A controlled manipulation shows that representation similarity changes a deduplication mechanism's inferred cluster count by 1.425, while a fourfold change in true ancestry changes it by only 0.040.

rss · arXiv - AI · Sep 3, 04:00

**Background**: Multi-agent AI systems improve inference by spawning multiple agents and synthesizing their reports, but this approach assumes that each agent provides independent evidence. The epistemic Sybil problem arises when agents share a common evidence root, making their reports non-independent. The paper formalizes this with information theory, defining a report as an epistemic Sybil extension when it provides no additional information given existing reports.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.01873">[2609.01873] Epistemic Sybil Resistance: Multiplying AI ...</a></li>
<li><a href="https://beyond-desk.com/signal/g-1903">Epistemic Sybil Resistance: Multiplying AI Agents Without ...</a></li>
<li><a href="https://github.com/marcbara/epistemic-sybil-resistance/blob/master/EXPERIMENT.md">epistemic-sybil-resistance/EXPERIMENT.md at master - GitHub</a></li>

</ul>
</details>

**Tags**: `#multi-agent AI`, `#epistemic Sybil`, `#LLM agents`, `#evidence aggregation`, `#AI safety`

---

<a id="item-13"></a>
## [WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act World Modeling](https://arxiv.org/abs/2609.01608) ⭐️ 8.0/10

WMLLM introduces a self-evolving optimization-agent framework that integrates predict-then-act world modeling with LLM-based candidate generation, achieving state-of-the-art results on multi-objective molecular optimization under limited evaluation budgets. This work addresses the sample efficiency bottleneck in black-box optimization, which is crucial for expensive real-world tasks like drug discovery and materials design. By leveraging LLMs' implicit knowledge for prediction, it opens new avenues for integrating world modeling with agentic search, potentially improving performance across various optimization domains. WMLLM uses a single LLM for both outcome prediction and candidate generation, combined with agentic multi-turn refinement, population-based search, and reinforcement learning to refine its world model and strategy. Experiments focus on multi-objective molecular optimization, where it achieves state-of-the-art results under a limited evaluation budget.

rss · arXiv - Machine Learning · Sep 3, 04:00

**Background**: Black-box optimization problems involve searching large, weakly structured, and high-dimensional spaces without explicit gradients, often requiring costly evaluations. Traditional methods like Bayesian optimization or evolutionary algorithms can suffer from poor sample efficiency. World modeling aims to predict promising directions before evaluation, and LLMs can provide nontrivial predictive accuracy due to their implicit knowledge. WMLLM builds on these ideas to create a self-evolving agent that improves its search strategy over time.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.01608v1">WMLLM: Self-Evolving Optimization Agents via Predict-Then-Act ...</a></li>
<li><a href="https://arxiv.org/pdf/1710.08005">Smart “Predict, then Optimize” - arXiv.org</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2772586322000181">Integrating prediction with optimization: Models and ...</a></li>

</ul>
</details>

**Tags**: `#black-box optimization`, `#large language models`, `#world modeling`, `#reinforcement learning`, `#agentic search`

---

<a id="item-14"></a>
## [Sim2Signal: A New Benchmark for Sim-to-Real Traffic Signal Control](https://arxiv.org/abs/2609.01676) ⭐️ 8.0/10

Sim2Signal introduces a benchmark that decomposes the sim-to-real gap in traffic signal control into observation, action, transition, and reward gaps, and evaluates 18 mitigation methods across 33 settings. This benchmark addresses a critical gap in applying reinforcement learning to real-world traffic signal control, providing a standardized way to measure and mitigate the sim-to-real gap. It could significantly improve the reliability of RL-based traffic systems and guide future research in both RL and intelligent transportation. The benchmark uses 2 base controllers, 33 gap settings, and 10 calibrated networks built from 5 real-world locations. It finds that direct transfer consistently degrades performance, but mitigation effectiveness is highly dependent on the network and gap setting, with estimation-based methods generally outperforming domain randomization or invariant representations.

rss · arXiv - Machine Learning · Sep 3, 04:00

**Background**: Reinforcement learning (RL) often performs well in simulation but fails when deployed in the real world, a problem known as the sim-to-real gap. In traffic signal control, this gap arises from mismatches in the Markov Decision Process (MDP) components: observation, action, transition, and reward. Sim2Signal provides a systematic benchmark to isolate and evaluate these gaps, helping researchers understand and mitigate them.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2502.13187">A Survey of Sim - to - Real Methods in RL: Progress, Prospects and...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10846-026-02437-2">Addressing the Sim - to - Real Gap in Reinforcement Learning for...</a></li>
<li><a href="https://deeplearn.org/arxiv/789809/measure-the-sim-to-real-gap:-designing-an-affordable-real-world-benchmark-platform-for-reinforcement-learning-in-aiot-systems">Measure the Sim - to - Real Gap : Designing an Affordable Real-World...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#sim-to-real`, `#traffic signal control`, `#benchmark`

---

<a id="item-15"></a>
## [Survey Unifies Test-Time Adaptation, Learning, and Scaling](https://arxiv.org/abs/2609.01679) ⭐️ 8.0/10

This survey introduces a unified feedback-driven framework called Test-Time Intelligence (TTI) to connect test-time adaptation, learning, and scaling. It reviews major methods, applications, and open challenges across various domains. This unified perspective helps bridge fragmented research communities and provides a clearer foundation for studying self-improving AI systems at deployment time. It could guide future research and accelerate progress in making AI models more adaptive and efficient during inference. The survey covers test-time adaptation, learning, and scaling, highlighting their distinctions and growing overlap in hybrid systems. It spans vision, language, multimodal learning, generative models, robotics, and healthcare, aiming to provide a research roadmap.

rss · arXiv - Machine Learning · Sep 3, 04:00

**Background**: Test-time adaptation (TTA) modifies a model's state using test-time signals, while test-time scaling allocates extra computation during inference, such as more sampling or tool use. These approaches are often studied separately, but this survey proposes a unified feedback-driven view to relate them.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.01679">[2609.01679] A Survey on Self-Improving Test - Time Intelligence ...</a></li>
<li><a href="https://arxiv.org/abs/2303.15361">[2303.15361] A Comprehensive Survey on Test-Time Adaptation ...</a></li>
<li><a href="https://huggingface.co/blog/Kseniase/testtimecompute">What is test-time compute and how to scale it? - Hugging Face</a></li>

</ul>
</details>

**Tags**: `#test-time adaptation`, `#test-time learning`, `#test-time scaling`, `#survey`, `#AI/ML`

---

<a id="item-16"></a>
## [Median-of-Means Limits Convex Robust Estimators; Nonconvex Route to Oracle](https://arxiv.org/abs/2609.01689) ⭐️ 8.0/10

This paper proves that all convex block M-estimators have a worst-case robustness constant of at least 1/(1-2ε), matching the median-of-means bound, and introduces a nonconvex block-Lp family (0<p<1) whose global minimizers approach the trimmed-block oracle constant 1/(1-ε) as p decreases. This establishes a fundamental limitation of convex estimators in robust statistics, guiding algorithm design toward nonconvex approaches for heavy-tailed and adversarially corrupted data. It impacts researchers in robust learning and high-dimensional statistics, potentially leading to estimators with better robustness guarantees. The block-Lp objectives have a benign landscape with no bad basins, and for sufficiently small p, global minimizers coincide with the oracle under a mild separation condition. Combined with block-level concentration, this yields sub-Gaussian deviation bounds under finite 2+δ moments and extends to high-dimensional robust mean estimation and sparse regression.

rss · arXiv - Machine Learning · Sep 3, 04:00

**Background**: Median-of-means (MoM) estimation partitions data into blocks, computes the mean of each block, and takes the median of these block means to robustly estimate the mean under heavy-tailed or corrupted data. The trimmed-block oracle is an ideal estimator that discards the worst ε fraction of blocks, achieving a robustness constant of 1/(1-ε). Convex M-estimators, which minimize convex loss functions, are widely used but this paper shows they cannot reach the oracle's robustness.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/median-of-means-estimators">Median - of - Means Estimators</a></li>
<li><a href="https://www.math.uci.edu/~rvershyn/teaching/2023-2024/hdp-knu/Lugosi-median-of-means.pdf">Mean estimation : median - of - means tournaments</a></li>
<li><a href="https://faculty.washington.edu/yenchic/short_note/note_MoM.pdf">A short note on the median - of - means estimator</a></li>

</ul>
</details>

**Tags**: `#robust statistics`, `#median-of-means`, `#nonconvex optimization`, `#heavy-tailed data`, `#adversarial robustness`

---

<a id="item-17"></a>
## [VakyArth: First Pragmatic Benchmark for Indic Languages](https://arxiv.org/abs/2609.01788) ⭐️ 8.0/10

VakyArth is introduced as the first pragmatic benchmark for Indic languages, covering Hindi, Punjabi, Tamil, and Malayalam. It evaluates LLMs across five pragmatic phenomena using multiple-choice questions, natural language inference, and translation tasks authored by native speakers. This benchmark fills a critical gap in LLM evaluation, which has largely ignored Indic languages despite their linguistic and cultural diversity. The findings reveal systematic failures in pragmatics, highlighting the need for culturally aware multilingual NLP development. The benchmark covers five phenomena: deixis, speech acts, implicature, social pragmatics, and coherence. Results show MCQ accuracy consistently exceeds NLI accuracy, translation performance does not reliably track pragmatic understanding, and Indo-Aryan languages have a translation advantage over Dravidian languages.

rss · arXiv - NLP · Sep 3, 04:00

**Background**: Pragmatics is the study of how context and cultural conventions shape meaning beyond literal words. Existing pragmatic benchmarks are mostly in English, leaving Indic languages unexplored. VakyArth addresses this by providing a diagnostic tool for four major Indic languages, spanning different language families.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.01788">VakyArth : Evaluating Pragmatic Competence in LLMs across Indic ...</a></li>
<li><a href="https://arxiv.org/html/2609.01788v1">VakyArth: Evaluating Pragmatic Competence in LLMs across</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#pragmatics`, `#Indic languages`, `#multilingual NLP`, `#benchmark`

---

<a id="item-18"></a>
## [LLM Internal Activations Reveal Clinician-Aligned Depression Symptom Vectors](https://arxiv.org/abs/2609.01832) ⭐️ 8.0/10

Researchers analyzed the residual stream of Gemma-3-27B-PT using mechanistic interpretability and found that symptom groups separate most at layer 21. They constructed Symptom Vectors via Semantic Projection, which preserved clinician-annotated rank ordering across mood, somatic, and suicidality axes, and a single depression vector achieved AUC = 0.789 in separating depressive from non-depressive text. This work bridges mechanistic interpretability and mental health, offering a novel approach to understand how LLMs represent depressive symptoms. It could lead to more transparent and trustworthy AI-based depression assessment tools, potentially improving clinical decision-making and patient care. The study used Gemma-3-27B-PT and recorded activations across symptom descriptions from validated clinical instruments. The depression vector in Layer 21 acts as an emotional valence gate, restricting symptom projection to depressive speech, indicating a decorrelated, clinician-aligned symptom signal readable from internal activations.

rss · arXiv - NLP · Sep 3, 04:00

**Background**: Mechanistic interpretability aims to reverse-engineer the internal workings of LLMs to understand how they make decisions. The residual stream in transformer models is a key component where information is accumulated across layers, and techniques like Semantic Projection can extract meaningful directions from activations. This study applies these methods to a clinical problem, exploring whether LLMs internalize psychiatric constructs in a way that aligns with clinician judgment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2602.11180v1">Mechanistic Interpretability for Large Language Model ...</a></li>
<li><a href="https://arxiv.org/abs/2602.11180">[2602.11180] Mechanistic Interpretability for Large Language ... Locate, steer, and improve: A practical survey of actionable ... Exploring Mechanistic Interpretability in Large Language ... Mechanistic indicators of understanding in large language models How Do Large Language Models Understand Relevance? A ... Interpretability in the Era of Large Language Models ...</a></li>
<li><a href="https://arxiv.org/html/2312.12141v1">Exploring the Residual Stream of Transformers - arXiv.org</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#large language models`, `#mental health`, `#depression`, `#clinical NLP`

---

<a id="item-19"></a>
## [Survey on Action-Grounded Reasoning in Autonomous Driving](https://arxiv.org/abs/2609.01659) ⭐️ 8.0/10

This survey reviews 171 papers, including 130 method papers, and proposes a representation-centered taxonomy categorizing action-grounded reasoning methods into four types: language-based, visual-spatial, latent-dynamic, and externalized reasoning, further divided into 13 subtypes. This survey addresses a frontier topic in autonomous driving, highlighting the shift from textual chain-of-thought to action-grounded reasoning. It provides a structured overview that can guide future research and development of more reliable, real-time reasoning systems for driving agents. The survey identifies that the open frontier lies in intermediate representations that are grounded in the real world, coupled to real-time action, and verifiable under safety-critical systems. The project page is available at https://github.com/tangzhengxu/awesome-av-cot.

rss · arXiv - Computer Vision · Sep 3, 04:00

**Background**: Chain-of-thought (CoT) reasoning elicits intermediate reasoning steps in generative models, improving complex reasoning. In autonomous driving, the final output is a continuous action, so reasoning must align with the physical world's spatiotemporal structure. This survey explores how CoT is adapted to action-grounded reasoning, where intermediate states are represented in forms other than text, such as visual, latent, or externalized representations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain - of - Thought Prompting Elicits Reasoning in Large...</a></li>
<li><a href="https://towardsdatascience.com/latentvla-latent-reasoning-models-for-autonomous-driving/">LatentVLA: Latent Reasoning Models for Autonomous Driving</a></li>
<li><a href="https://arxiv.org/abs/2512.10226">[2512.10226] Latent Chain-of-Thought World Modeling for End ... [2608.09333] DH-VLM: Dual-Horizon Cooperative Latent ... LatentVLA: Latent Reasoning Models for Autonomous Driving Latent Chain-of-Thought World Modeling for End-to-End Driving LatentVLA: Latent Reasoning Models for Self-Driving AI GitHub - pqh22/ColaVLA: [CVPR2026] ColaVLA: Leveraging ...</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#chain-of-thought`, `#reasoning`, `#survey`, `#AI/ML`

---

<a id="item-20"></a>
## [FAIRLENS Benchmark Exposes Unwarranted Inference in Vision-Language Models](https://arxiv.org/abs/2609.01691) ⭐️ 8.0/10

FAIRLENS, a new benchmark and evaluation framework, assesses fairness and validity of vision-language models (VLMs) in hiring, legal, and healthcare contexts. It evaluates eight VLMs across over 100K image-question pairs per model, revealing that the primary failure mode is unwarranted inference rather than unequal treatment. This work addresses a critical gap in AI ethics by highlighting that standard fairness metrics like demographic parity can miss severe validity issues in high-stakes domains. It underscores the need for VLMs to abstain from making unsupported inferences, which is crucial for safe deployment in hiring, legal, and healthcare decisions. The benchmark uses real face images with demographic annotations and closed- and open-ended questions, evaluating responses from four views: demographic parity, soundness, demographic association, and free-text bias. The weakest model made unwarranted inferences on 99% of unanswerable questions, with failures most severe in legal and healthcare contexts.

rss · arXiv - Computer Vision · Sep 3, 04:00

**Background**: Vision-language models (VLMs) are AI systems that process both images and text, extending large language models to multimodal tasks. They are increasingly used in high-stakes decision-making, but their fairness and validity are not well understood. Demographic parity is a common fairness metric that requires equal outcomes across groups, but it does not capture whether a model's inferences are supported by evidence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision_Language_Models_(VLM)">Vision Language Models (VLM)</a></li>
<li><a href="https://aiwiki.ai/wiki/demographic_parity">Demographic Parity | AI Wiki</a></li>

</ul>
</details>

**Tags**: `#fairness`, `#vision-language models`, `#benchmark`, `#AI ethics`, `#high-stakes decision-making`

---

<a id="item-21"></a>
## [ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes](https://arxiv.org/abs/2609.01740) ⭐️ 8.0/10

ZipTok3D introduces a novel 3D tokenizer that organizes object geometry into progressively informative global-token prefixes and uses iterative decoding to achieve high-fidelity reconstruction from extremely short token sequences. It achieves reconstruction quality comparable to the 32-token COD-VAE baseline using only one token on ShapeNet and four on TRELLIS, yielding 32x and 8x shorter token sequences respectively. This work addresses a key challenge in 3D generation: maintaining high-fidelity reconstruction when compressing token sequences to extremely low budgets. By enabling much shorter token sequences without quality loss, ZipTok3D could significantly improve the efficiency and scalability of 3D generative models, impacting applications in gaming, VR/AR, and digital content creation. The method employs nested dropout, which randomly truncates the latent sequence after encoding during training, requiring each retained prefix to reconstruct the complete object, thus prioritizing essential geometric information in leading tokens. The decoder repeatedly applies a parameter-shared Transformer block to recover fine-grained geometry from each prefix without a separate generative sampling stage.

rss · arXiv - Computer Vision · Sep 3, 04:00

**Background**: 3D tokenization converts 3D shapes into discrete tokens that can be processed by generative models, similar to how text or image tokenizers work. Existing tokenizers often organize latent representations over spatial regions or as fixed-size sets of global tokens, which suffer sharp reconstruction degradation when compressed to very low token budgets. Nested dropout is a regularization technique that imposes a strict order on hidden units, and here it is used to create ordered prefixes of tokens that capture progressively more detail.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ziplab/ZipTok3D">ZipTok3D: High-Fidelity 3D Tokenization with Compact Token ...</a></li>
<li><a href="https://huggingface.co/papers/2609.01740">Paper page - ZipTok3D: High-Fidelity 3D Tokenization with Compact...</a></li>
<li><a href="https://arxiv.org/abs/1402.0915">[1402.0915] Learning Ordered Representations with Nested Dropout</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#tokenization`, `#deep learning`, `#computer vision`, `#efficient representation`

---

<a id="item-22"></a>
## [Pig Kidney Transplant in Man Sets Record at 271 Days](https://www.bbc.co.uk/news/articles/c305qn2jeggo?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

A man with a transplanted pig kidney has survived a record 271 days while awaiting a human transplant, marking a major milestone in xenotransplantation. This breakthrough demonstrates prolonged survival of a pig kidney in a human, potentially addressing the critical shortage of human donor organs. It could pave the way for broader clinical use of xenotransplantation, offering hope to thousands of patients on transplant waiting lists. The patient took 52 pills daily to manage his immune system and named his pig kidney 'Wilma'. Over nine months, the kidney showed signs of gradual rejection, but the case still represents the longest successful pig-to-human kidney transplant to date.

rss · BBC Health · Sep 3, 22:31

**Background**: Xenotransplantation involves transplanting living cells, tissues, or organs from one species to another, such as from pigs to humans. Pigs are often used because their organs are similar in size and function to human organs, but genetic modifications are needed to reduce rejection risks. Previous attempts have faced challenges, including organ rejection and concerns about disease transmission.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Xenotransplantation">Xenotransplantation</a></li>
<li><a href="https://www.cnn.com/2026/01/16/health/pig-kidney-human-organ-transplant">Man who received experimental pig kidney transplant now has a ...</a></li>
<li><a href="https://www.npr.org/sections/shots-health-news/2025/04/11/g-s1-59637/pig-kidney-transplant-rejection">Pig kidney transplant fails after patient rejection - NPR</a></li>

</ul>
</details>

**Tags**: `#xenotransplantation`, `#medical research`, `#organ transplant`, `#health`

---