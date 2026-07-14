---
layout: default
title: "Horizon Summary: 2026-07-14 (EN)"
date: 2026-07-14
lang: en
---

> From 106 items, 33 important content pieces were selected

---

1. [Bonsai 27B: 27B-Parameter Model Runs on Phones](#item-1) ⭐️ 8.0/10
2. [AI-Assisted Programming May Worsen Software Complexity](#item-2) ⭐️ 8.0/10
3. [Cursor 0day: Full Disclosure After 6 Months Unpatched](#item-3) ⭐️ 8.0/10
4. [Are we offloading too much thinking to AI?](#item-4) ⭐️ 8.0/10
5. [Linux Input Latency Measured: X11 vs Wayland, VRR, DXVK](#item-5) ⭐️ 8.0/10
6. [Lobste.rs Migrates from MariaDB to SQLite](#item-6) ⭐️ 8.0/10
7. [OpenManus: Open-Source AI Agent Framework Launches on GitHub](#item-7) ⭐️ 8.0/10
8. [Heretic: Automatic Censorship Removal for LLMs](#item-8) ⭐️ 8.0/10
9. [New Metrics Quantify LLM Sensitivity to Prompt Formatting](#item-9) ⭐️ 8.0/10
10. [Message Format Effects in Multi-Hop LLM Relays Are Tier-Dependent](#item-10) ⭐️ 8.0/10
11. [Latent CoT Reasoning as Dynamical Systems](#item-11) ⭐️ 8.0/10
12. [YUKTI: Robust Decision-Making from Natural Language](#item-12) ⭐️ 8.0/10
13. [Verifier as Curriculum: Self-Distillation Boosts Game Code Generation](#item-13) ⭐️ 8.0/10
14. [SLM + Multi-Agent Self-Correction for Closed-Loop Control](#item-14) ⭐️ 8.0/10
15. [Feedback-Coupled Memory Systems in Continuous Time](#item-15) ⭐️ 8.0/10
16. [GNNs Across the KG Lifecycle: A Comprehensive Survey](#item-16) ⭐️ 8.0/10
17. [Ground Truth Datasets Are Human Constructions, Not Objective](#item-17) ⭐️ 8.0/10
18. [Systematic Comparison of KV-Cache Compression Methods](#item-18) ⭐️ 8.0/10
19. [Coding Agents Need Minimal Context to Act](#item-19) ⭐️ 8.0/10
20. [Detecting LLM Distillation via Reference-Based Method](#item-20) ⭐️ 8.0/10
21. [DEGS: Training-Free LLM Reasoning via Entropy Collapse](#item-21) ⭐️ 8.0/10
22. [LLM System Outperforms Market in Merger Arbitrage Forecasting](#item-22) ⭐️ 8.0/10
23. [Benchmarking LLM Faithfulness in Clinical Trial Summaries](#item-23) ⭐️ 8.0/10
24. [Quantization Silently Degrades LLM Reasoning Quality](#item-24) ⭐️ 8.0/10
25. [WiCAT: Zero-shot behavior decoding via atlas-aligned tokenization](#item-25) ⭐️ 8.0/10
26. [RSLoRA: Training-Free Rank Allocation for LoRA](#item-26) ⭐️ 8.0/10
27. [ReflectWorld-MM: Entity-Oriented Memory for Open-Ended Video](#item-27) ⭐️ 8.0/10
28. [Wearable Motion Reconstruction from Arbitrary Sensors](#item-28) ⭐️ 8.0/10
29. [Conformal Prediction for Spatial Events with Manifold Constraints](#item-29) ⭐️ 8.0/10
30. [New SO(2) Theory Advances ML Interatomic Potentials](#item-30) ⭐️ 8.0/10
31. [Diversified Multinomial Logit Contextual Bandits](#item-31) ⭐️ 8.0/10
32. [PsiQuantum Plans Large-Scale Quantum Computer Using Light](#item-32) ⭐️ 8.0/10
33. [Yale Discovers Hidden Retinal Network with 'Commander' Cell](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bonsai 27B: 27B-Parameter Model Runs on Phones](https://prismml.com/news/bonsai-27b) ⭐️ 8.0/10

PrismML released Bonsai 27B, a 27-billion-parameter language model compressed via advanced quantization to fit on mobile devices, with ternary and 1-bit variants achieving 95% and 90% of full-precision performance respectively. This breakthrough enables running a 27B-class model locally on a phone, democratizing access to powerful AI without cloud dependency, and could accelerate edge AI adoption across consumer and enterprise applications. Bonsai 27B supports a 262K-token context and speculative decoding, with the ternary variant occupying only 5.9 GB and the 1-bit variant using 1.125 effective bits per weight (14.2x reduction vs FP16). It is released under the Apache 2.0 license.

hackernews · xenova · Jul 14, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48910545)

**Background**: Large language models typically require significant GPU memory, making local deployment on phones impractical. Quantization reduces numerical precision of model weights, shrinking memory footprint while preserving most capabilities. Bonsai 27B uses ternary (values -1, 0, +1) and 1-bit representations to achieve extreme compression.

<details><summary>References</summary>
<ul>
<li><a href="https://prismml.com/news/bonsai-27b">PrismML — Announcing Bonsai 27B: The First 27B-Class Model to Run on a Phone</a></li>
<li><a href="https://huggingface.co/prism-ml/Bonsai-27B-gguf">prism-ml/Bonsai-27B-gguf · Hugging Face</a></li>
<li><a href="https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf">prism-ml/Ternary-Bonsai-27B-gguf · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Commenters expressed excitement about scaling ternary models and compared Bonsai 27B to Gemma 4 12B QAT, noting trade-offs in tool-calling performance. Some questioned the quality of generated recipes and macronutrient accuracy, while others highlighted Apple's reported interest in PrismML.

**Tags**: `#AI`, `#model compression`, `#quantization`, `#edge AI`, `#mobile`

---

<a id="item-2"></a>
## [AI-Assisted Programming May Worsen Software Complexity](https://lucumr.pocoo.org/2026/7/13/the-tower-keeps-rising/) ⭐️ 8.0/10

An essay argues that AI-assisted programming, while boosting individual productivity, may exacerbate software complexity by enabling faster code production without improving team coordination, echoing the Lisp Curse. This matters because large software projects are limited by coordination, not individual coding speed; AI tools could lead to a 'tower that keeps rising' without shared understanding, increasing maintenance costs and failure risks. The essay draws a parallel to the Lisp Curse, where Lisp's power led to isolated development; similarly, AI agents may let developers build more alone, reducing the need for collaboration and shared architectural understanding.

hackernews · cdrnsf · Jul 14, 16:57 · [Discussion](https://news.ycombinator.com/item?id=48909785)

**Background**: The Lisp Curse describes how Lisp's expressiveness allows individual programmers to achieve much alone, discouraging collaboration and leading to fragmented, poorly documented software. In large projects, coordination and shared understanding are critical for managing complexity. AI-assisted programming tools like code generators and agents are becoming more capable, raising concerns about their impact on software engineering practices.

<details><summary>References</summary>
<ul>
<li><a href="https://www.freshcodeit.com/blog/myths-of-lisp-curse">What is the Curse of Lisp: Challenges and Opportunities - Freshcode</a></li>
<li><a href="https://www.reddit.com/r/programming/comments/s09b5/til_about_the_lisp_curse/">r/programming on Reddit: TIL about the Lisp Curse</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the thesis, noting that composability is like Tetris—lines must clear—and that naive use of agents violates architectural principles. Some reference the Lisp Curse and Bipolar Lisp Programmer, highlighting that AI may accelerate the same problem of isolated development.

**Tags**: `#software engineering`, `#AI-assisted programming`, `#complexity`, `#coordination`, `#Lisp Curse`

---

<a id="item-3"></a>
## [Cursor 0day: Full Disclosure After 6 Months Unpatched](https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left) ⭐️ 8.0/10

Mindgard disclosed a 0day vulnerability in Cursor IDE that allows arbitrary executables from the project folder to run without user prompt, remaining unpatched for over six months despite multiple reports to Cursor and HackerOne. This vulnerability poses a serious security risk to developers using Cursor, as it can be exploited by malicious repositories to execute arbitrary code on the user's machine. The prolonged unpatched period and vendor inaction undermine trust in AI coding tools and highlight the need for responsible disclosure. The vulnerability involves Cursor searching the current working directory for executables like git.exe before the system PATH, allowing a malicious .exe placed in the project folder to be executed. Cursor's trust dialog for opening projects does not prevent this, and the issue persists in the latest tested version.

hackernews · Synthetic7346 · Jul 14, 17:58 · [Discussion](https://news.ycombinator.com/item?id=48910676)

**Background**: Cursor is an AI-powered code editor based on VS Code that integrates AI agents to assist with coding tasks. The vulnerability exploits a Windows behavior where the current directory is searched for executables before the PATH environment variable, combined with Cursor's lack of prompting before running such executables.

<details><summary>References</summary>
<ul>
<li><a href="https://mindgard.ai/blog/cursor-0day-when-full-disclosure-becomes-the-only-protection-left">Cursor 0day: When Full Disclosure Becomes the Only Protection Left</a></li>
<li><a href="https://www.darkreading.com/application-security/cursor-ide-malicious-code-poisoned-repos">Cursor IDE Auto-Executes Malicious Code in Poisoned Repos</a></li>
<li><a href="https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/">CVE-2026-26268: How an AI Coding Agent Can Run Exploits in Cursor IDE</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some argue the vulnerability requires an attacker to already have placed a malicious executable in the project folder, reducing its severity, while others find it alarming that Cursor runs executables without prompting and that the vendor failed to respond for months. There is also debate about whether this is primarily a Windows quirk rather than a Cursor bug.

**Tags**: `#security`, `#vulnerability`, `#AI tools`, `#0day`, `#Cursor`

---

<a id="item-4"></a>
## [Are we offloading too much thinking to AI?](https://www.artfish.ai/p/offloading-thinking-to-ai) ⭐️ 8.0/10

A high-scoring article on Artfish.ai sparks debate about whether heavy reliance on AI for cognitive tasks is eroding human critical thinking and understanding, drawing parallels to calculator use but highlighting unique risks. This discussion is critical because as AI becomes ubiquitous in work and education, the risk of diminished human reasoning and over-reliance could have long-term consequences for productivity, innovation, and personal agency. The article scores 8.0/10 with 343 points and 333 comments, indicating strong community engagement. It compares AI offloading to calculator use but argues that AI, unlike calculators, can replace entire thought processes, not just arithmetic.

hackernews · yenniejun111 · Jul 14, 15:18 · [Discussion](https://news.ycombinator.com/item?id=48908178)

**Background**: The debate centers on the concept of 'cognitive offloading'—using tools to reduce mental effort. While calculators offload computation, AI language models can generate entire arguments, decisions, and creative outputs, potentially bypassing human understanding. This raises concerns about skill atrophy and loss of deep knowledge.

**Discussion**: Commenters express mixed views: some argue that heavy AI users still retain agency, while others share anecdotes of junior developers blindly trusting AI-generated code without understanding it. A few fear a future where AI dictates decisions, forcing compliance and stifling independent thought.

**Tags**: `#AI ethics`, `#critical thinking`, `#productivity`, `#AI over-reliance`, `#education`

---

<a id="item-5"></a>
## [Linux Input Latency Measured: X11 vs Wayland, VRR, DXVK](https://marco-nett.de/blog/measuring-input-latency-on-linux-x11-vs-wayland-vrr-dxvk/) ⭐️ 8.0/10

A detailed measurement study compared input latency on Linux across X11 and Wayland display servers, with and without VRR and DXVK, using a 500Hz display and high-precision tools. This analysis provides empirical data to settle debates about Linux desktop responsiveness and gaming performance, helping users choose the best configuration and guiding developers to optimize the graphics stack. The test used a 500Hz display, which may mask larger latency differences visible at lower refresh rates like 60Hz or 120Hz; XWayland showed about 3ms extra latency compared to native Wayland.

hackernews · hoechst · Jul 14, 16:36 · [Discussion](https://news.ycombinator.com/item?id=48909424)

**Background**: Input latency is the delay between a user action (e.g., mouse click) and the corresponding visual update on screen. X11 and Wayland are competing display servers on Linux; Wayland is newer and aims for better security and performance. VRR (Variable Refresh Rate) synchronizes the display's refresh rate with the game's frame rate to reduce tearing and stutter. DXVK translates Direct3D calls to Vulkan, enabling Windows games to run on Linux via Wine/Proton.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Variable_refresh_rate">Variable refresh rate - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/DXVK">DXVK - Wikipedia</a></li>
<li><a href="https://github.com/doitsujin/dxvk">GitHub - doitsujin/dxvk: Vulkan-based implementation of D3D8, 9, 10 and ...</a></li>

</ul>
</details>

**Discussion**: Commenters praised the rigorous methodology and noted that results at 60Hz would be more revealing for typical users. Some pointed out that XWayland's extra latency might explain why some perceive Wayland as slow when running X11 games. The discussion also highlighted the value of such open analysis for improving the Linux ecosystem.

**Tags**: `#Linux`, `#input latency`, `#Wayland`, `#X11`, `#gaming`

---

<a id="item-6"></a>
## [Lobste.rs Migrates from MariaDB to SQLite](https://simonwillison.net/2026/Jul/14/lobsters-sqlite/#atom-everything) ⭐️ 8.0/10

Lobste.rs, a popular community link-aggregator, successfully migrated its production database from MariaDB to SQLite, completing a long-planned transition that began in 2018. The site now runs entirely on a single VPS with reduced CPU and memory usage. This migration demonstrates that SQLite can serve as a viable production database for moderately-trafficked web applications, challenging the conventional wisdom that a client-server database is always necessary. It provides a real-world case study for developers considering simplifying their architecture and reducing operational costs. The primary SQLite database file is approximately 3.8 GB, with additional files for cache (1.1 GB), queue (218 MB), and Rack::Attack (555 MB). The migration pull request added 735 lines and removed 593 lines across 30 commits and 188 files.

rss · Simon Willison · Jul 14, 19:44

**Background**: Lobste.rs is a Ruby on Rails application that originally used MariaDB. The team had considered migrating to PostgreSQL since 2018, but later decided to investigate SQLite. SQLite is an embedded, serverless database engine that stores data in a single file, making it simpler to manage than client-server databases like MariaDB or PostgreSQL.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/lobsters/lobsters/pull/1927">Migrate to SQLite (after the great Chicago fire of 1871) by thomasdziedzic · Pull Request #1927 · lobsters/lobsters</a></li>
<li><a href="https://github.com/lobsters/lobsters/pull/1705">Migrate to SQLite by thomasdziedzic · Pull Request #1705 · lobsters/lobsters</a></li>
<li><a href="https://lobste.rs/s/oz7ebk/lobste_rs_migrates_from_mariadb_sqlite">lobste.rs migrates from MariaDB to SQLite | Lobsters</a></li>

</ul>
</details>

**Discussion**: The Lobsters community discussion (implied by the source) likely includes positive reactions to the performance improvements and cost savings, with some debate about SQLite's suitability for write-heavy workloads and concurrency. The thread also contains technical details about the migration process and lessons learned.

**Tags**: `#SQLite`, `#database migration`, `#web performance`, `#Rails`, `#production deployment`

---

<a id="item-7"></a>
## [OpenManus: Open-Source AI Agent Framework Launches on GitHub](https://github.com/FoundationAgents/OpenManus) ⭐️ 8.0/10

FoundationAgents has released OpenManus, an open-source AI agent framework that provides a modular architecture for building general-purpose agents without requiring invitation codes. The prototype was built within three hours by the team behind MetaGPT. OpenManus democratizes access to advanced AI agent technology by removing the invite-code barrier, enabling developers worldwide to experiment and build autonomous agents. Its rapid development and open-source nature could accelerate innovation in the AI agent ecosystem. The framework supports modular agent architecture with specialized components for planning, tool usage, and task execution. It also introduces OpenManus-RL, a companion project for reinforcement learning-based tuning of LLM agents, developed with researchers from UIUC.

rss · GitHub Trending - Python · Jul 14, 22:51

**Background**: AI agents are software systems that can autonomously perform tasks by planning, using tools, and executing actions. Manus is a popular but invite-only AI agent platform, which limited access. OpenManus aims to provide an open alternative, built by the same team behind MetaGPT, a well-known open-source project for multi-agent collaboration.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/FoundationAgents/OpenManus">OpenManus - GitHub</a></li>
<li><a href="https://openmanus.github.io/">OpenManus - Open-source Framework for Building AI Agents</a></li>
<li><a href="https://foundationagents.org/projects/openmanus/">OpenManus - Foundation Agents</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Open Source`, `#Python`, `#FoundationAgents`

---

<a id="item-8"></a>
## [Heretic: Automatic Censorship Removal for LLMs](https://github.com/p-e-w/heretic) ⭐️ 8.0/10

Heretic is a new open-source tool that automatically removes censorship (safety alignment) from transformer-based language models using directional ablation and a TPE-based optimizer, without requiring expensive post-training. This tool democratizes the ability to decensor LLMs, potentially impacting AI safety debates and freedom of expression, while raising concerns about misuse for generating harmful content. Heretic combines directional ablation (abliteration) with an Optuna-powered TPE optimizer to minimize refusals and KL divergence, achieving results comparable to manual abliteration. It supports most dense models, multimodal models, and some MoE architectures.

rss · GitHub Trending - Python · Jul 14, 22:51

**Background**: Many language models are fine-tuned with safety alignment to refuse harmful requests, but this can also suppress legitimate uses. Directional ablation is a technique that removes refusal behavior by modifying model activations. Heretic automates this process, making it accessible to non-experts.

**Tags**: `#LLM`, `#AI safety`, `#censorship`, `#open source`

---

<a id="item-9"></a>
## [New Metrics Quantify LLM Sensitivity to Prompt Formatting](https://arxiv.org/abs/2607.09665) ⭐️ 8.0/10

A new paper introduces the Format Sensitivity Index (FSI) and Parseability Sensitivity Index (PSI) to measure how prompt wrapper formatting affects LLM benchmark scores, based on 140,000 generations across 7 tasks and 4 models. This work reveals that prompt wrapper variance can flip leaderboard conclusions, highlighting a critical flaw in current LLM evaluation practices. It provides practical recommendations for more robust benchmarking and structured-output deployments. The study found that mean FSI varies by over 30x across models, and parseability failures largely explain accuracy variance. A fixed-effects regression showed parseability remains a strong predictor of accuracy even after controlling for task, model, and wrapper.

rss · arXiv - AI · Jul 14, 04:00

**Background**: LLM benchmarks often use prompt wrappers—templates that format questions and answers—which can differ only in formatting but still affect model scores. The paper argues that reporting accuracy without considering wrapper variance and compliance is statistically fragile.

**Tags**: `#LLM benchmarking`, `#prompt engineering`, `#evaluation robustness`, `#structured output`, `#format sensitivity`

---

<a id="item-10"></a>
## [Message Format Effects in Multi-Hop LLM Relays Are Tier-Dependent](https://arxiv.org/abs/2607.09678) ⭐️ 8.0/10

This paper introduces a controlled relay testbed to study how message format affects information fidelity in multi-hop LLM agent relays, finding that effects are tier-dependent and strong relays can be nearly lossless under faithful instructions. This research challenges assumptions about message format effects in multi-hop agent relays, providing practical guidance for designing reliable multi-agent systems where information must be passed accurately across multiple hops. The testbed uses five formats (free NL, precision-instructed NL, JSON, triples, key-value) over six hops, with two relay-capability tiers and a cognitive-load condition, finding that structure buys a faithful, error-localizing channel but not error correction.

rss · arXiv - AI · Jul 14, 04:00

**Background**: LLM agents often need to pass information in multi-hop relays, where copy fidelity matters more than one-shot generation. Previous work disagreed on whether structured messages help or hurt accuracy, but did not study multi-hop scenarios. This paper fills that gap.

**Tags**: `#LLM agents`, `#multi-hop relay`, `#message format`, `#information fidelity`, `#NLP`

---

<a id="item-11"></a>
## [Latent CoT Reasoning as Dynamical Systems](https://arxiv.org/abs/2607.09698) ⭐️ 8.0/10

This paper models latent chain-of-thought reasoning as dynamical systems, revealing structured dynamics and two distinct stability classes in methods like CODI and COCONUT. This work addresses a critical interpretability gap in latent reasoning methods, providing a quantitative framework that could guide improvements in model transparency and performance. The study uses measures like step-to-step change, direction consistency, and Lyapunov sensitivity, alongside UMAP and DMD/PHATE projections, to characterize reasoning dynamics.

rss · arXiv - AI · Jul 14, 04:00

**Background**: Latent reasoning methods like CODI and COCONUT maintain multiple candidate traces in hidden space, unlike explicit chain-of-thought which follows a single transparent trace. This makes them powerful but hard to interpret. Dynamical systems analysis offers a way to study how these hidden states evolve over reasoning steps.

**Tags**: `#mechanistic interpretability`, `#latent reasoning`, `#dynamical systems`, `#chain-of-thought`, `#representation learning`

---

<a id="item-12"></a>
## [YUKTI: Robust Decision-Making from Natural Language](https://arxiv.org/abs/2607.09706) ⭐️ 8.0/10

YUKTI introduces a novel autoformulation framework that uses typed-proposition graphs with uncertainty and provenance to produce robust, verifiable decisions from natural language, overcoming the fragility of single-objective point-estimate pipelines. This framework significantly reduces decision regret (by over 90% in controlled tests) and addresses the optimizer's curse, making it highly relevant for high-stakes domains like healthcare, finance, and operations research where robust decisions are critical. YUKTI introduces Assumption-Robust Pareto Frontiers (ARPF) that resample assumptions to score action survival rates (rho), and proves a bound making rho an exact factor of decision regret. It also includes a data generation system (SRJANA) for benchmark creation.

rss · arXiv - AI · Jul 14, 04:00

**Background**: Current natural language to optimization pipelines (e.g., NL4Opt, OptiMUS) commit to a single objective and point-valued coefficients, then solve once, which is fragile because every number is an assumption. YUKTI changes this by representing uncertainty and provenance in a typed-proposition graph, routing to multiple solvers, and using distributional Pareto hand-offs.

**Tags**: `#natural language processing`, `#decision-making`, `#uncertainty quantification`, `#operations research`, `#robust optimization`

---

<a id="item-13"></a>
## [Verifier as Curriculum: Self-Distillation Boosts Game Code Generation](https://arxiv.org/abs/2607.09709) ⭐️ 8.0/10

Researchers propose a deterministic, judge-free 'strict-launch' filter for rejection-sampling self-distillation, which significantly improves cross-family game code generation without proxy optimization. On GameCraft-Bench, a 14B model distilled under this gate raised clean generation from 8.8% to 42.2% per-candidate and achieved perfect best-of-K coverage (25/25) over three rounds. This work addresses a fundamental issue in learned judges—proxy optimization—by using an ungameable signal, demonstrating that the verifier itself can serve as the curriculum for self-distillation. The approach has strong potential to improve code generation and self-distillation methods across various domains. The strict-launch filter checks whether a generated Godot project launches cleanly under a headless engine, providing a deterministic and ungameable signal. A gold-duplication control regressed below the base model (5.6% vs. 8.8%), while a lenient BUILD check erased all gains, isolating verifier precision as the key factor.

rss · arXiv - AI · Jul 14, 04:00

**Background**: Self-distillation involves training a model on its own outputs, often using a learned judge to filter high-quality samples. However, learned judges can be gamed, leading to proxy optimization where the model learns to increase scores without improving actual quality. This paper introduces a deterministic filter that cannot be gamed, ensuring that only truly functional code is used for training.

**Tags**: `#code generation`, `#self-distillation`, `#game development`, `#machine learning`, `#LLM`

---

<a id="item-14"></a>
## [SLM + Multi-Agent Self-Correction for Closed-Loop Control](https://arxiv.org/abs/2607.09713) ⭐️ 8.0/10

Researchers propose using a compact Qwen2.5-1.5B small language model aligned via GRPO in a validator-guided correction loop for autonomous control policy generation from natural language, achieving 91.5% action-alignment accuracy at 3.84s mean inference latency. This work demonstrates that small language models can be practically deployed for edge closed-loop control, addressing latency and compute constraints that hinder large cloud-based models, and enabling reconfigurable autonomous industrial automation. The framework combines an action agent, a symbolic/digital-twin validation layer, and a reprompting agent that iteratively steers outputs toward valid actions. In 30 randomized thermal-control simulations with 500 steps each, it achieved 86.3%–100% accuracy across cases and maintained a 95% in-range rate under symbolic re-mapping.

rss · arXiv - AI · Jul 14, 04:00

**Background**: Closed-loop control in industrial automation requires generating control policies from natural language specifications. Large language models are often too slow or data-sensitive for edge deployment. Small language models offer lower latency and compute footprint but may lack reasoning capability. This work uses GRPO alignment and multi-agent self-correction to bridge that gap.

**Tags**: `#small language models`, `#closed-loop control`, `#multi-agent systems`, `#industrial automation`, `#reinforcement learning`

---

<a id="item-15"></a>
## [Feedback-Coupled Memory Systems in Continuous Time](https://arxiv.org/abs/2607.09714) ⭐️ 8.0/10

This paper formalizes feedback-coupled memory systems in continuous time by defining the agent update operator via Mechanism-Based Intelligence and the environmental update operator via Coupled Memory Graph Process, achieving Lyapunov global dissipativity with a computable stability threshold. This framework bridges agent-based modeling and non-Markovian dynamics, providing a universal organizing principle that memory dissipation must outpace feedback gain, which has potential impact on distributed systems and AI coordination. The stability condition is given by the inequality 4β² < 2ημγ², generalizing previous discrete-time results, and numerical simulations with N=2 and mean-field validation at N=10⁶ confirm the threshold and the emergence of a self-reinforcing coordination cascade when violated.

rss · arXiv - AI · Jul 14, 04:00

**Background**: Feedback-coupled memory systems (FCMS) are architectures where agents and environment interact through closed-loop feedback with memory. The original FCMS framework left two key operators axiomatically undefined; this paper provides concrete definitions using MBI and CMGP, enabling rigorous stability analysis in continuous time.

**Tags**: `#feedback systems`, `#memory systems`, `#agent-based modeling`, `#non-Markovian`, `#stability analysis`

---

<a id="item-16"></a>
## [GNNs Across the KG Lifecycle: A Comprehensive Survey](https://arxiv.org/abs/2607.09666) ⭐️ 8.0/10

This paper proposes a novel two-level taxonomy for GNN-based knowledge graph technologies, covering the entire pipeline from construction to applications. It fills a gap in systematic reviews of GNN methods for knowledge graphs, providing a unified framework that can guide future research and development. The taxonomy includes two dimensions: the KG technologies pipeline (construction, embedding, reasoning, applications) and GNN-based perspective (GCN, GAT, HGNN). The review analyzes advantages, strengths, and limitations of various models.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: Graph Neural Networks (GNNs) are deep learning models designed for graph-structured data, while Knowledge Graphs (KGs) represent entities and their relationships. Integrating GNNs into KG tasks has shown promise, but a systematic overview was lacking.

**Tags**: `#Graph Neural Networks`, `#Knowledge Graphs`, `#Survey`, `#Knowledge Graph Embedding`, `#Knowledge Reasoning`

---

<a id="item-17"></a>
## [Ground Truth Datasets Are Human Constructions, Not Objective](https://arxiv.org/abs/2607.09668) ⭐️ 8.0/10

A new position paper argues that ground truth datasets in machine learning are human constructions shaped by social and technical choices, not objective truths, and proposes the concept of 'situated reliability' to improve model evaluation. This challenges a fundamental assumption in ML that ground truth is neutral, potentially leading to more transparent, accountable, and reliable models by acknowledging the contingent nature of reference datasets. The paper introduces 'situated reliability' as a framework to articulate the limits and strengths of models and their truth claims, emphasizing that ground truths are context-dependent and not universal.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: Ground truth datasets are used to train and evaluate machine learning models, serving as reference standards. However, these datasets are often created through human annotation or measurement processes that involve subjective decisions, biases, and contextual factors, yet they are typically treated as objective benchmarks.

**Tags**: `#machine learning`, `#ground truth`, `#dataset bias`, `#AI ethics`, `#reproducibility`

---

<a id="item-18"></a>
## [Systematic Comparison of KV-Cache Compression Methods](https://arxiv.org/abs/2607.09683) ⭐️ 8.0/10

This study systematically compares Turbo-Quant and SpectralQuant KV-cache compression methods, revealing that eigenbasis-based methods fail on heavy-tailed data but excel in structured regimes, with effective semantic dimension adapting to calibration budgets. This work provides statistically validated insights into KV-cache compression, which is critical for reducing memory and latency in large language model inference, potentially guiding future optimization strategies. The study evaluates non-dominated schemes including WHT rotation with Beta Lloyd-Max and QJL, using a statistical validation methodology that separates systematic codec differences from implementation variance.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: KV-cache compression reduces memory usage in transformer-based LLMs by storing fewer key-value pairs. Turbo-Quant and SpectralQuant are two recent methods that use quantization and eigenbasis transformations, respectively. This study compares their effectiveness under different data regimes.

**Tags**: `#KV-cache compression`, `#LLM optimization`, `#quantization`, `#statistical validation`, `#eigenbasis methods`

---

<a id="item-19"></a>
## [Coding Agents Need Minimal Context to Act](https://arxiv.org/abs/2607.09691) ⭐️ 8.0/10

A new study on SWE-bench Verified reveals that coding agents require only the code being edited, not the full repository context, to effectively resolve issues. This challenges the prevailing assumption that larger context windows improve agent performance, with implications for reducing computational costs and improving efficiency in AI-assisted software engineering. The study found that natural-language summaries of the code answer only 4 out of 45 behavioral questions, compared to 27 out of 45 for the source code itself, and that surrounding context (e.g., UML skeletons) did not improve issue resolution rates.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: SWE-bench Verified is a benchmark for evaluating coding agents on real-world software engineering tasks. Coding agents are AI systems that can autonomously edit code to fix bugs or implement features. This study separates the tasks of finding where to edit from actually editing, focusing on the latter.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/SWE-bench_Verified">SWE-bench Verified</a></li>

</ul>
</details>

**Tags**: `#coding agents`, `#AI-assisted programming`, `#context window`, `#software engineering`, `#empirical study`

---

<a id="item-20"></a>
## [Detecting LLM Distillation via Reference-Based Method](https://arxiv.org/abs/2607.09692) ⭐️ 8.0/10

A new paper proposes a reference-based membership inference method to detect whether a later-generation LLM checkpoint was distilled from a specific teacher model, achieving near-perfect accuracy in single-teacher scenarios. This addresses a critical gap in LLM security and ethics, as model distillation is widely used but can involve policy violations or unfair advantages; the method enables auditing of distillation relationships in real-world models. The method compares alignment of student outputs with candidate teachers relative to a reference checkpoint, and handles unknown pipelines by inferring proxy prompt templates; it also identifies a glyph-level signal specific to o1/o3 models.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: Model distillation involves training a student model on outputs from a stronger teacher model to improve performance. Detecting which teacher was used is challenging because the student only sees outputs, not the teacher's weights. This paper introduces a reference-based approach that leverages an earlier checkpoint from the same lineage to make detection tractable.

**Tags**: `#LLM`, `#model distillation`, `#membership inference`, `#security`, `#ethics`

---

<a id="item-21"></a>
## [DEGS: Training-Free LLM Reasoning via Entropy Collapse](https://arxiv.org/abs/2607.09693) ⭐️ 8.0/10

Researchers propose Depth-Entropy Guided Sampling (DEGS), a training-free method that uses layer-wise entropy collapse as an intrinsic quality signal to guide test-time sampling for LLM reasoning. DEGS achieves reinforcement-learning-like reasoning gains without expensive training, reward models, or labeled data, offering a practical alternative to RL fine-tuning for improving LLM reasoning. DEGS defines a per-sequence collapse depth and combines it with sequence likelihood in an MCMC power-sampling framework, achieving state-of-the-art training-free accuracy across three models and four benchmarks with minimal overhead.

rss · arXiv - Machine Learning · Jul 14, 04:00

**Background**: Reinforcement learning (RL) is commonly used to improve LLM reasoning but requires expensive training and curated data. Recent work shows that test-time sampling from sharpened base-model distributions can recover much of the RL gain, but existing methods only use output-layer likelihoods. DEGS exploits internal layer-wise entropy dynamics, specifically entropy collapse in deeper layers, as a signal for better sampling.

**Tags**: `#LLM reasoning`, `#test-time sampling`, `#entropy collapse`, `#training-free`, `#reinforcement learning`

---

<a id="item-22"></a>
## [LLM System Outperforms Market in Merger Arbitrage Forecasting](https://arxiv.org/abs/2607.09921) ⭐️ 8.0/10

Researchers developed a language-model forecasting system for merger arbitrage that achieves state-of-the-art performance by combining expert-guided context engineering with finetuning on hindsight-guided reasoning traces. This work demonstrates that LLMs can succeed in specialized, long-context financial forecasting tasks, outperforming market-implied probabilities and traditional machine learning models, which could transform how merger arbitrage and similar high-stakes financial decisions are made. On an out-of-sample set of over 400 large deals across 42 countries, the system achieved a class-balanced Brier score of 0.151, which is 24% lower than calibrated market-implied probabilities and 19% lower than XGBoost.

rss · arXiv - NLP · Jul 14, 04:00

**Background**: Merger arbitrage is an investment strategy that speculates on the successful completion of mergers and acquisitions. The Brier score measures the accuracy of probabilistic predictions, with lower scores indicating better calibration. This paper applies LLMs to a long-context reasoning task involving hundreds of pages of technical documents.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Merger_arbitrage">Merger arbitrage</a></li>
<li><a href="https://en.wikipedia.org/wiki/Brier_score">Brier score</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#financial forecasting`, `#merger arbitrage`, `#long-context reasoning`, `#finetuning`

---

<a id="item-23"></a>
## [Benchmarking LLM Faithfulness in Clinical Trial Summaries](https://arxiv.org/abs/2607.09932) ⭐️ 8.0/10

This paper introduces a benchmark to evaluate the faithfulness of LLM-generated clinical trial summaries for three stakeholder audiences, identifying unsupported claims as the primary failure mode. A knowledge-graph-augmented retrieval system improved faithfulness scores significantly. Hallucinations in LLMs pose serious risks in high-stakes domains like healthcare; this work provides a rigorous framework to measure and improve faithfulness, which is critical for AI safety and clinical decision-making. The benchmark uses 200 stratified trials from ClinicalTrials.gov, evaluated with audience-specific prompts and a six-dimension annotation schema. Baseline measurements for GPT-4o, Claude Sonnet 4.6, and Gemini 2.5 Flash showed unsupported claims scored 1.55/3 on average.

rss · arXiv - NLP · Jul 14, 04:00

**Background**: Large language models (LLMs) are increasingly used to summarize clinical trial results for healthcare providers, patients, and payers. However, LLMs can generate plausible-sounding but incorrect information (hallucinations), which is especially dangerous in medical contexts. Faithfulness measures how accurately a summary reflects the source data without adding unsupported claims.

**Tags**: `#LLM`, `#clinical trials`, `#faithfulness`, `#benchmark`, `#AI safety`

---

<a id="item-24"></a>
## [Quantization Silently Degrades LLM Reasoning Quality](https://arxiv.org/abs/2607.09999) ⭐️ 8.0/10

A new study reveals that post-training quantization can cause silent failures in LLM reasoning, such as hollow convergence and shortcut collapse, even when task accuracy remains high. This matters because quantized LLMs are widely deployed for efficiency, but standard accuracy metrics fail to detect these reasoning failures, posing reliability risks in critical applications. The study analyzed 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B–14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks, with a validated six-category failure taxonomy.

rss · arXiv - NLP · Jul 14, 04:00

**Background**: Post-training quantization reduces model size and inference cost by using lower-precision numerical formats (e.g., NF4). However, this study shows that quantization can alter reasoning processes without affecting final accuracy, a phenomenon invisible to standard evaluation.

**Tags**: `#LLM`, `#quantization`, `#reasoning`, `#reliability`, `#taxonomy`

---

<a id="item-25"></a>
## [WiCAT: Zero-shot behavior decoding via atlas-aligned tokenization](https://arxiv.org/abs/2607.09754) ⭐️ 8.0/10

WiCAT introduces a self-supervised, atlas-aligned spatiotemporal tokenization method for multi-subject widefield calcium imaging, achieving zero-shot behavior decoding on unseen subjects. This is a significant step toward foundation models in neuroscience, enabling scalable and generalizable analysis of brain-wide dynamics across subjects and tasks. WiCAT uses an atlas-grounded tokenization scheme without session-specific components and learns globally shared spatiotemporal representations, outperforming single-session models on multiple datasets.

rss · arXiv - Computer Vision · Jul 14, 04:00

**Background**: Widefield calcium imaging captures brain-wide cortical dynamics at high resolution, but its high dimensionality and task-irrelevant activity have limited modeling to single sessions. Multi-subject models for this modality have not been demonstrated before, and zero-shot behavior decoding across subjects remains challenging for neural modalities in general.

**Tags**: `#neuroscience`, `#calcium imaging`, `#self-supervised learning`, `#foundation model`, `#brain-wide dynamics`

---

<a id="item-26"></a>
## [RSLoRA: Training-Free Rank Allocation for LoRA](https://arxiv.org/abs/2607.09757) ⭐️ 8.0/10

RSLoRA introduces a training-free and gradient-free rank allocator for LoRA that uses activation-space geometry to assign ranks based on representational sensitivity, outperforming existing methods like AdaLoRA and GoRA. This addresses a key limitation of uniform rank assignment in LoRA, enabling more efficient and effective fine-tuning of large models without additional training overhead. RSLoRA uses a virtual representational probing mechanism that simulates adaptation via structured low-rank noise and measures manifold displacement using Effective Rank and Fréchet Distance to identify high-sensitivity modules.

rss · arXiv - Computer Vision · Jul 14, 04:00

**Background**: Low-Rank Adaptation (LoRA) is a popular parameter-efficient fine-tuning method that adds trainable low-rank matrices to pre-trained weights. Typically, all layers use the same rank, which is suboptimal because layers have different functional importance. Existing rank allocation methods either require expensive training or rely on heuristics that ignore task-specific representations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sensitivity_analysis">Sensitivity analysis - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2508.11277">[2508.11277] Probing the Representational Power of Sparse Autoencoders in Vision Models</a></li>

</ul>
</details>

**Tags**: `#LoRA`, `#parameter-efficient fine-tuning`, `#rank allocation`, `#representation learning`, `#fine-tuning`

---

<a id="item-27"></a>
## [ReflectWorld-MM: Entity-Oriented Memory for Open-Ended Video](https://arxiv.org/abs/2607.09759) ⭐️ 8.0/10

ReflectWorld-MM introduces an entity-oriented multi-media memory system for open-ended video streams, using hierarchical long-term memory grounded in human memory theory to track persistent entities over time. This work addresses a key limitation of existing frame-based memory systems by organizing memory around persistent entities, enabling better tracking of who and what reappears over time, which is crucial for long-term video understanding and multimodal AI agents. The system consists of a perception front-end, a hierarchical long-term memory (including episodic, semantic, and procedural memory), and a real-world implementation that plugs into off-the-shelf assistants. It achieves state-of-the-art accuracy on all six long-video and lifelong-memory benchmarks.

rss · arXiv - Computer Vision · Jul 14, 04:00

**Background**: Existing multimodal agents with long-term memory over video streams typically organize memory around frames or keep it in a flat feature store, limiting them to bounded videos and weakening entity tracking. ReflectWorld-MM instead uses an entity-oriented approach inspired by human memory theory, which separates episodic, semantic, and procedural memory to better handle open-ended streams.

**Tags**: `#multimodal AI`, `#long-term memory`, `#video understanding`, `#entity-oriented`, `#memory system`

---

<a id="item-28"></a>
## [Wearable Motion Reconstruction from Arbitrary Sensors](https://arxiv.org/abs/2607.09780) ⭐️ 8.0/10

Researchers propose WHIP, a generative model that reconstructs full-body motion from arbitrary subsets of consumer wearable sensors like smartphones, smartwatches, smart glasses, and smart insoles, along with a large-scale multi-modal dataset of 50 activities. This work addresses a key limitation in wearable motion capture by enabling robust reconstruction from any sensor configuration, which is crucial for practical applications in AR/VR, health monitoring, and human-computer interaction where users wear diverse devices. The dataset synchronizes consumer-grade sensors with ground-truth 3D motion across 50 activities, and WHIP handles missing modalities by design, producing physically plausible motions. The paper also systematically studies sensor complementarity.

rss · arXiv - Computer Vision · Jul 14, 04:00

**Background**: Traditional motion capture uses fixed sensor configurations (e.g., IMU suits or HMD-centric rigs), which limits generalization. Consumer wearables are more unobtrusive but pose challenges due to varying sensor sets. This work aims to bridge that gap.

**Tags**: `#motion capture`, `#wearable sensors`, `#generative model`, `#multi-modal dataset`, `#computer vision`

---

<a id="item-29"></a>
## [Conformal Prediction for Spatial Events with Manifold Constraints](https://arxiv.org/abs/2607.10008) ⭐️ 8.0/10

A new conformal prediction method is introduced that uses sliced Wasserstein distance and manifold constraints to produce calibrated prediction sets for spatial events like tropical cyclone genesis and earthquake locations, with theoretical coverage guarantees. 这项工作解决了自然灾害预测等高影响领域中对不确定性量化的关键需求，这些领域的准确风险评估依赖于可靠的预测区间。 The method represents spatial point clouds as empirical measures, scores them using sliced Wasserstein distance, and constrains the prediction set to lie near the training data manifold. A modified flow-based sampling procedure is introduced to make the prediction sets tractable as ensembles.

rss · arXiv - Data Science & Statistics · Jul 14, 04:00

**Background**: Conformal prediction is a distribution-free framework that produces statistically valid prediction sets under the assumption of exchangeability. It works by computing nonconformity scores on labeled data to create prediction intervals for new test points. Empirical measures are random measures derived from observed data, used to approximate the true underlying probability distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Empirical_measure">Empirical measure</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#uncertainty quantification`, `#spatial events`, `#Wasserstein distance`, `#machine learning`

---

<a id="item-30"></a>
## [New SO(2) Theory Advances ML Interatomic Potentials](https://arxiv.org/abs/2607.10664) ⭐️ 8.0/10

This paper systematically investigates SO(2) theory for machine learning interatomic potentials, proposing direct Cartesian and recursive Clebsch-Gordan constructions of Wigner D-matrices, and introduces Edge Complex Product Basis and Radial Rotary Complex Attention (RRA) to improve many-body expansion and extrapolation. These contributions address limitations of conventional SO(2) linear architectures relative to SO(3) Clebsch-Gordan tensor products, potentially advancing the accuracy and efficiency of machine learning interatomic potentials for computational chemistry and materials science. The proposed TECE-OAM-RRA-1.0 model achieves state-of-the-art performance on the Matbench Discovery benchmark, trained on OMat24, sAlex, and MPTrj datasets. The Edge Complex Product Basis uses complex-valued equivariant multiplications to directly construct higher-order interactions on edges.

rss · arXiv - Data Science & Statistics · Jul 14, 04:00

**Background**: Machine learning interatomic potentials (MLIPs) aim to predict atomic energies and forces from atomic configurations, enabling efficient molecular dynamics simulations. Equivariant neural networks, such as those based on SO(2) or SO(3) symmetry, are crucial for ensuring physical consistency. The paper builds on prior work like Atomic Cluster Expansion (ACE) and attention mechanisms.

**Tags**: `#machine learning`, `#interatomic potentials`, `#equivariant neural networks`, `#computational chemistry`, `#SO(2) theory`

---

<a id="item-31"></a>
## [Diversified Multinomial Logit Contextual Bandits](https://arxiv.org/abs/2607.11684) ⭐️ 8.0/10

This paper introduces the diversified multinomial logit (DMNL) contextual bandit model, which augments MNL choice probabilities with a submodular diversity function, and proposes a UCB-based algorithm called OFU-DMNL that achieves a (1-1/(e+1))-approximate regret bound of O~(d sqrt(T/K)). This work bridges the gap between relevance-driven MNL bandits and diversity-encoding submodular bandits, providing a principled framework for balancing relevance and diversity in assortment optimization, which is crucial for recommendation systems and online learning. The OFU-DMNL algorithm constructs assortments item-wise by maximizing optimistic marginal gains, avoiding black-box optimization oracles, and achieves an improved approximation factor over standard submodular baselines. Experiments show consistent gains and comparable regret with substantially lower runtime relative to exhaustive enumeration.

rss · arXiv - Data Science & Statistics · Jul 14, 04:00

**Background**: Multinomial logit (MNL) models are widely used to predict choice probabilities among multiple alternatives, but they focus solely on relevance and ignore diversity. Submodular functions capture diminishing returns and are used to model diversity, but they lack structured choice probabilities. This paper combines both to address the relevance-diversity trade-off in assortment optimization under uncertainty.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multinomial_logit_model">Multinomial logit model</a></li>
<li><a href="https://en.wikipedia.org/wiki/Submodular_function">Submodular function</a></li>

</ul>
</details>

**Tags**: `#contextual bandits`, `#multinomial logit`, `#diversity`, `#submodularity`, `#online learning`

---

<a id="item-32"></a>
## [PsiQuantum Plans Large-Scale Quantum Computer Using Light](https://www.technologyreview.com/2026/07/14/1140356/psiquantum-plan-massive-quantum-computer-out-of-light/) ⭐️ 8.0/10

PsiQuantum has detailed its plan to build a large-scale, fault-tolerant quantum computer using photonic qubits, housed in cryogenically cooled cabinets. If successful, this approach could overcome key challenges in quantum computing, such as scalability and error correction, potentially leading to practical quantum computers sooner than expected. The machine will consist of about 100 stainless-steel cabinets, each connected to a liquid helium supply to maintain temperatures near absolute zero.

rss · MIT Technology Review · Jul 14, 08:00

**Background**: Fault-tolerant quantum computing (FTQC) is a regime where quantum processors are large-scale and use error correction to achieve very low error rates. Current quantum computers are in the noisy intermediate-scale quantum (NISQ) era, which are prone to noise and lack full error correction. PsiQuantum's photonic approach uses particles of light as qubits, which may offer advantages in coherence and connectivity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fault_tolerant_quantum_computing">Fault tolerant quantum computing</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#photonics`, `#PsiQuantum`, `#cryogenics`, `#hardware`

---

<a id="item-33"></a>
## [Yale Discovers Hidden Retinal Network with 'Commander' Cell](https://www.sciencedaily.com/releases/2026/07/260713000804.htm) ⭐️ 8.0/10

Yale researchers have discovered a hidden communication network in the retina where a newly identified 'commander' cell coordinates separate visual pathways to enhance detection of faint details. This breakthrough challenges the traditional view that retinal pathways work independently, and could lead to new treatments for vision disorders or inspire advanced artificial vision systems. The 'commander' cell appears to coordinate cooperation between separate visual pathways, helping the eye detect faint details that might otherwise be missed. The study was published in a scientific journal and is based on experimental observations in animal models.

rss · ScienceDaily Health · Jul 14, 01:15

**Background**: The retina is a light-sensitive layer at the back of the eye that converts light into neural signals. Traditionally, it was thought that different visual features (e.g., motion, color, fine detail) are processed by separate, parallel pathways that do not interact. This discovery reveals a previously unknown layer of communication within the retina.

**Tags**: `#neuroscience`, `#vision`, `#retina`, `#biology`, `#medical research`

---