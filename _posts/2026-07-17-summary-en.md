---
layout: default
title: "Horizon Summary: 2026-07-17 (EN)"
date: 2026-07-17
lang: en
---

> From 106 items, 23 important content pieces were selected

---

1. [Firefox Compiled to WebAssembly Runs Inside a Browser](#item-1) ⭐️ 9.0/10
2. [GitHub Releases Official Copilot Agent SDKs](#item-2) ⭐️ 9.0/10
3. [First Atmosphere Found on Rocky Exoplanet in Habitable Zone](#item-3) ⭐️ 8.0/10
4. [Kimi K3 and the Pelican Benchmark: A Critical Look](#item-4) ⭐️ 8.0/10
5. [Open Source AI Surge Threatens Closed Models](#item-5) ⭐️ 8.0/10
6. [Apache Ossie: Standardizing Semantic Metadata Exchange](#item-6) ⭐️ 8.0/10
7. [Open Interpreter: Coding Agent Optimized for Low-Cost Models](#item-7) ⭐️ 8.0/10
8. [LLM-T1D: Interpretable Insulin Pump Controller](#item-8) ⭐️ 8.0/10
9. [Capability from Access Structure, Not Scale](#item-9) ⭐️ 8.0/10
10. [XAI Must Prioritize Foundations Over Ad-hoc Methods](#item-10) ⭐️ 8.0/10
11. [Branching Policy Optimization for Sandbox-Native RL](#item-11) ⭐️ 8.0/10
12. [RENEW: Repairing World Model Exploitation via Human Preferences](#item-12) ⭐️ 8.0/10
13. [JKP Framework Reveals VLM Instability Under Repeated Prompting](#item-13) ⭐️ 8.0/10
14. [First Quantum NLP System for Arabic](#item-14) ⭐️ 8.0/10
15. [LLM Agents Lose Info in Text; Latent Channel Proposed](#item-15) ⭐️ 8.0/10
16. [TTCD: Continuous Diffusion with Per-Token Times for Language Modeling](#item-16) ⭐️ 8.0/10
17. [Polestar: Drift-Aware Cache and Token Commitment for dLLMs](#item-17) ⭐️ 8.0/10
18. [SeeSE3: Probing 3D Euclidean Space in Vision Features](#item-18) ⭐️ 8.0/10
19. [DCVC-MB: Neural B-Frame Codec with State-Space Models](#item-19) ⭐️ 8.0/10
20. [Optimal Self-Distillation for Rectified Flow via Linear Probing](#item-20) ⭐️ 8.0/10
21. [Subjective Risk Decomposition Unifies UQ Measures](#item-21) ⭐️ 8.0/10
22. [PiVoT: Real-Time Multi-Object Tracking from Radar Point Clouds](#item-22) ⭐️ 8.0/10
23. [Weather Data Sabotage Risk Rising](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox Compiled to WebAssembly Runs Inside a Browser](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter has compiled the full Firefox browser (Gecko engine) to WebAssembly, allowing it to run inside another browser like Chrome. The project used LLMs (Claude Opus and Fable) for code translation, costing an estimated $25,000 in tokens. This demonstrates a paradigm shift where entire applications, even complex browsers, can be sandboxed and run within another browser, potentially enabling new forms of web-based computing and legacy software preservation. It also showcases the power of LLMs in automating large-scale code translation tasks. The demo uses the Wisp protocol to proxy all network traffic through Puter's server, as WebAssembly code cannot open arbitrary network connections. The project chose Firefox/Gecko for its strong single-process support, which simplifies the WebAssembly compilation.

rss · Simon Willison · Jul 16, 23:34

**Background**: WebAssembly (Wasm) is a low-level binary instruction format that runs in modern web browsers at near-native speed, enabling high-performance applications like games and video editing. Compiling a full browser engine like Gecko to Wasm is extremely challenging due to its size and complexity; prior attempts have compiled smaller engines like WebKit but without a public demo.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://firefox-source-docs.mozilla.org/overview/gecko.html">Gecko — Firefox Source Docs documentation</a></li>
<li><a href="https://github.com/fable-compiler/fable">GitHub - fable-compiler/Fable: F# to JavaScript, TypeScript, Python, Rust, Erlang and Dart Compiler · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion was highly enthusiastic, with many praising the technical achievement. Some commenters noted the high server costs for proxying traffic and questioned the practicality, but overall sentiment was positive.

**Tags**: `#WebAssembly`, `#Firefox`, `#Browser`, `#LLM`, `#Wasm`

---

<a id="item-2"></a>
## [GitHub Releases Official Copilot Agent SDKs](https://github.com/github/copilot-sdk) ⭐️ 9.0/10

GitHub has released the official Copilot SDK, a multi-platform toolkit that allows developers to embed the same agentic engine powering Copilot CLI into their own applications. The SDK is available in Python, TypeScript, Go, .NET, Java, and Rust, with packages on npm, PyPI, NuGet, Go, Crates.io, and Maven Central. This SDK democratizes agentic AI capabilities, enabling any developer to build Copilot-powered features into their tools without building orchestration from scratch. It significantly lowers the barrier for integrating advanced AI agents into custom developer workflows and third-party services. The SDK exposes the same production-tested agent runtime behind Copilot CLI, handling planning, tool invocation, and multi-turn execution. It is currently in technical preview, and GitHub provides cookbooks for Node.js, Python, Go, .NET, and Java to help developers get started quickly.

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**Background**: GitHub Copilot Agent is an AI-powered coding assistant that can autonomously analyze projects, create plans, and make code changes. Copilot CLI already provided agentic capabilities via the command line, but integrating it into other applications required custom work. The new SDK packages that engine into reusable libraries for popular programming languages.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub</a></li>
<li><a href="https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/">Build an agent into any app with the GitHub Copilot SDK - The GitHub Blog</a></li>
<li><a href="https://www.infoq.com/news/2026/02/github-copilot-sdk/">GitHub Copilot SDK Lets Developers Integrate Copilot CLI's Engine into Apps - InfoQ</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#API`

---

<a id="item-3"></a>
## [First Atmosphere Found on Rocky Exoplanet in Habitable Zone](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

The James Webb Space Telescope has confirmed the presence of an atmosphere on LHS 1140b, a rocky super-Earth in the habitable zone of a red dwarf star 48 light-years away. This marks the first confirmed atmosphere on a relatively rocky exoplanet within its star's habitable zone. This discovery challenges previous assumptions that rocky planets around red dwarfs cannot retain atmospheres due to intense stellar stripping. It opens new possibilities for studying potentially habitable worlds and searching for biosignatures. LHS 1140b is about 5.6 times Earth's mass and 70% larger in radius, with a density suggesting it may be an ocean world containing 9-19% water by mass. The detected gas is helium, indicating a high escape velocity capable of retaining such a light gas.

hackernews · neversaydie · Jul 17, 14:06 · [Discussion](https://news.ycombinator.com/item?id=48947560)

**Background**: Red dwarfs are cooler and smaller than the Sun, placing their habitable zones much closer, which exposes planets to intense stellar flares and radiation. Atmospheric retention on such planets has been a major uncertainty in exoplanet science. LHS 1140b was discovered in 2017 by the MEarth Project and has been a prime target for atmospheric characterization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b</a></li>
<li><a href="https://www.bbc.com/news/articles/cy4kdd1e0ejo">First atmosphere found around Earth-like planet LHS 1140 b</a></li>

</ul>
</details>

**Discussion**: Commenters expressed surprise that a rocky planet in a red dwarf's habitable zone could retain an atmosphere, with some initially suspecting it might be a mini-Neptune being boiled off. However, JWST emission spectroscopy ruled out that scenario. Others discussed future propulsion concepts for sending probes to nearby exoplanets.

**Tags**: `#exoplanets`, `#JWST`, `#atmosphere`, `#habitable zone`, `#red dwarf`

---

<a id="item-4"></a>
## [Kimi K3 and the Pelican Benchmark: A Critical Look](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison critiques the 'pelican on a bike' benchmark for LLMs, highlighting its limitations for agentic tool use and sparking debate about benchmark contamination and hidden prompts. This analysis underscores the need for more relevant benchmarks that evaluate agentic capabilities, and reveals how hidden system prompts and training data contamination can distort model comparisons. The pelican benchmark asks models to generate an SVG of a pelican riding a bicycle, but it does not test tool calling or long-context reliability. Community comments reveal tokenizer quirks and suspected hidden prompts inflating token counts.

hackernews · droidjj · Jul 17, 14:21 · [Discussion](https://news.ycombinator.com/item?id=48947717)

**Background**: The 'pelican on a bicycle' benchmark is an informal test created by Simon Willison in late 2024 to evaluate LLMs' ability to follow instructions and generate SVG code. Benchmark contamination occurs when test data leaks into training data, inflating scores. Hidden prompts are system-level instructions injected by model providers that can affect model behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/simonw/pelican-bicycle">GitHub - simonw/pelican-bicycle: LLM benchmark: Generate an SVG of a pelican riding a bicycle · GitHub</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) — Grokipedia</a></li>
<li><a href="https://gigazine.net/gsc_news/en/20250609-llms-pelicans-on-bicycles/">Here's what happens when you run the AI benchmark 'Draw a Pelican on a Bicycle' on LLama 3.3 70B or GPT 4.1 - GIGAZINE</a></li>

</ul>
</details>

**Discussion**: Community members debate whether the pelican prompt is in training data, with one noting that even Simon's own blog content appears in models. Another commenter highlights tokenizer inconsistencies suggesting a hidden 85-token system prompt in Kimi K3.

**Tags**: `#LLM`, `#benchmark`, `#AI evaluation`, `#tokenization`, `#agentic AI`

---

<a id="item-5"></a>
## [Open Source AI Surge Threatens Closed Models](https://stateofopensource.ai/) ⭐️ 8.0/10

A new analysis from Mozilla reveals that open source AI models have overtaken closed models in usage, with open models now processing 63% of tokens on OpenRouter, up from 40% four months ago. This shift could disrupt the business models of closed AI companies like OpenAI and Anthropic, as hyperscalers and device makers can deploy open models without licensing fees, potentially rendering frontier models a liability due to their high training costs. Open models processed 4.19 trillion tokens on March 19, nearly 5x the 888 billion tokens processed four months earlier, according to OpenRouter data. The analysis is presented as a CTO-style slide deck, but critics note it appears to be LLM-generated.

hackernews · rellem · Jul 17, 14:31 · [Discussion](https://news.ycombinator.com/item?id=48947825)

**Background**: Open source AI models are models with publicly available weights and code, allowing anyone to use, modify, and deploy them freely. Closed models, like OpenAI's GPT-4, are proprietary and require licensing fees or API access. The debate between open and closed AI has intensified as open models improve rapidly.

**Discussion**: Commenters are divided: some see open models as an existential threat to closed AI companies, citing rapid growth in usage, while others criticize the analysis as poorly presented and likely LLM-generated, questioning its credibility. A user built a dashboard tracking the shift in real-time.

**Tags**: `#open source AI`, `#AI models`, `#market analysis`, `#LLM`

---

<a id="item-6"></a>
## [Apache Ossie: Standardizing Semantic Metadata Exchange](https://github.com/apache/ossie) ⭐️ 8.0/10

Apache Ossie, an industry-wide specification effort under Apache incubation, aims to standardize semantic metadata exchange across analytics, AI, and BI platforms using a vendor-neutral JSON/YAML specification. This initiative addresses semantic fragmentation, where the same KPI is defined differently across tools, reducing manual reconciliation and enabling AI agents to produce reliable outputs grounded in consistent business logic. The specification is JSON- and YAML-based, and the repository includes core specs, reference converters (e.g., dbt, GoodData), examples, and validation tooling.

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**Background**: Semantic metadata provides machine-interpretable representations of data elements, enabling shared meaning across systems. Currently, tools like BI platforms and AI agents often use incompatible semantic definitions, causing inconsistencies. Apache Ossie (formerly Open Semantic Interchange) aims to create a common, vendor-agnostic standard to solve this.

<details><summary>References</summary>
<ul>
<li><a href="https://ossie.apache.org/">Home - Apache Ossie (incubating)</a></li>
<li><a href="https://github.com/apache/ossie">GitHub - apache / ossie : Apache Ossie , industry wide specification...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_interoperability">Semantic interoperability - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#semantic metadata`, `#standardization`, `#interoperability`, `#AI`, `#BI`

---

<a id="item-7"></a>
## [Open Interpreter: Coding Agent Optimized for Low-Cost Models](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter, an open-source coding agent, has been updated to support the Kimi K3 model with a Rust-based harness emulation, providing maximum performance and a Codex-like interface. This project democratizes AI-assisted coding by enabling natural language code execution on low-cost open models, making advanced coding agents accessible to a broader audience and reducing dependency on expensive proprietary APIs. Open Interpreter is a fork of OpenAI's Codex, focusing on emulating agent harnesses for low-cost models. It supports multiple harnesses including kimi-code, claude-code, and qwen-code, and is compatible with ACP (Agent Client Protocol) and Codex interfaces.

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**Background**: Open Interpreter is an open-source coding agent that allows users to interact with their computer using natural language, executing code in real time. It is designed to work with low-cost open-weight models like Kimi K3, which has 2.8 trillion parameters and is one of the largest open models available. The project aims to provide a free and accessible alternative to proprietary coding agents like GitHub Copilot.

<details><summary>References</summary>
<ul>
<li><a href="https://www.openinterpreter.com/">Open Interpreter | Coding agent for open models</a></li>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open ...</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Tags**: `#AI`, `#open-source`, `#coding agent`, `#natural language`, `#LLM`

---

<a id="item-8"></a>
## [LLM-T1D: Interpretable Insulin Pump Controller](https://arxiv.org/abs/2607.14126) ⭐️ 8.0/10

Researchers introduced LLM-T1D, a novel insulin pump controller that combines reinforcement learning with large language models to achieve 73.5% Time in Range on the FDA-approved UVA/Padova T1D simulator, while providing human-readable explanations for its decisions. This work addresses the critical trust barrier in AI-driven diabetes management by making the controller's reasoning transparent, potentially improving patient and clinician adoption. It also demonstrates that LLM-based controllers can outperform traditional black-box RL systems in a safety-critical healthcare application. The system distills knowledge from a trained expert RL policy into fine-tuned LLaMA 3.1 8B and Qwen3 8B models, and includes formal safety verification to guard against hallucinations. The 73.5% Time in Range exceeds typical RL baselines, and the controller outputs plain-language explanations for each insulin dose decision.

rss · arXiv - AI · Jul 17, 04:00

**Background**: Type 1 Diabetes (T1D) is a chronic condition where the pancreas produces little or no insulin, requiring external insulin delivery. Artificial Pancreas Systems (APS) use algorithms to automate insulin delivery, but traditional reinforcement learning controllers are often black-box, making it hard for patients and doctors to trust them. Large Language Models (LLMs) like LLaMA and Qwen can generate human-like text, and when fine-tuned, can explain their reasoning in natural language.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/meta-llama/Llama-3.1-8B/tree/main">meta- llama / Llama - 3 . 1 - 8 B at main</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5851236/">The UVA / Padova Type 1 Diabetes Simulator Goes From Single Meal...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#type 1 diabetes`, `#interpretable AI`, `#healthcare`

---

<a id="item-9"></a>
## [Capability from Access Structure, Not Scale](https://arxiv.org/abs/2607.14144) ⭐️ 8.0/10

A new paper proposes the Capability Convergence Hypothesis (CCH), arguing that under a fixed inference budget, model capability converges to a hybrid architecture class rather than improving with scale alone, and identifies three resource walls. This challenges the Platonic Representation Hypothesis and suggests that architecture design, not just scaling, is crucial for capability, potentially reshaping how researchers approach model development and resource allocation. The paper introduces three resource walls: a Shannon wall barring o(Nb)-state architectures, a horizon wall barring fixed windows, and a circuit wall barring fixed-depth attention-only composition, and shows that a hybrid architecture can cross all three.

rss · arXiv - AI · Jul 17, 04:00

**Background**: The Platonic Representation Hypothesis (PRH) suggests that as models scale, their representations converge to a shared reality model. The Capability Convergence Hypothesis (CCH) extends this by arguing that capability does not automatically follow representation convergence; instead, it depends on the access structure of the architecture, specifically having both a compressive O(1)-state channel and a scalable verbatim-index channel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Instrumental_convergence">Instrumental convergence - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2405.07987">[2405.07987] The Platonic Representation Hypothesis</a></li>

</ul>
</details>

**Tags**: `#representation learning`, `#scaling laws`, `#hybrid models`, `#theoretical computer science`, `#deep learning theory`

---

<a id="item-10"></a>
## [XAI Must Prioritize Foundations Over Ad-hoc Methods](https://arxiv.org/abs/2607.14123) ⭐️ 8.0/10

A new position paper argues that explainable AI (XAI) research should shift focus from developing ad-hoc methods to addressing foundational challenges like problem formulation, evaluation, and building explanation-driven feedback pipelines. This matters because despite many XAI techniques, explanations rarely impact real-world workflows; the paper calls for a human-centered, action-oriented paradigm that could make AI more trustworthy and practically useful. The paper supports its claim with an analysis of recent ICML, NeurIPS, and ICLR papers and a survey of XAI practitioners, revealing recurring issues that limit cumulative progress. It concludes with a practical checklist to guide future research.

rss · arXiv - Machine Learning · Jul 17, 04:00

**Background**: Explainable AI (XAI) aims to make machine learning models interpretable, but many methods like feature attributions and sparse autoencoders are often used without clear problem definitions or evaluation. Human-in-the-loop systems integrate human feedback to improve model behavior, but current XAI research lacks pipelines for explanation-driven feedback. This paper argues that foundational clarity is needed to move from ad-hoc methods to actionable, feedback-driven AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.02081">Explainability in JupyterLab and Beyond: Interactive XAI Systems for...</a></li>

</ul>
</details>

**Tags**: `#Explainable AI`, `#XAI`, `#Machine Learning`, `#Research Methodology`, `#Human-in-the-loop`

---

<a id="item-11"></a>
## [Branching Policy Optimization for Sandbox-Native RL](https://arxiv.org/abs/2607.14171) ⭐️ 8.0/10

Researchers propose Branching Policy Optimization (BPO), a reinforcement learning algorithm that constructs a tree of rollouts sharing prefixes to reduce variance in deterministic, snapshottable sandbox environments. BPO improves success rates by 3.6–6.1 absolute points over GRPO and RLOO on WebShop, ALFWorld, and SWE-bench Verified. BPO leverages the unique properties of sandbox environments—determinism and snapshotability—to share variance across rollouts, potentially improving sample efficiency for LLM agent training. This could advance the field of LLM alignment and agent reinforcement learning by reducing the number of policy updates needed. BPO adaptively snapshots the sandbox at high-entropy decision points, forks K alternative actions per branch, and computes advantages from sibling returns rather than independent prompts. The variance reduction equals the prefix-explained portion of return variance, and BPO matches the best baseline using 38% fewer policy updates.

rss · arXiv - Machine Learning · Jul 17, 04:00

**Background**: Reinforcement learning for LLM agents often uses algorithms like PPO, RLOO, and GRPO, which sample N independent trajectories per prompt and compute advantages using a group baseline. However, these methods ignore that sandbox environments are deterministic, snapshottable, and resumable from any state. BPO exploits this property to construct a tree of rollouts with shared prefixes, reducing variance more efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14171v1">[2607.14171v1] Branching Policy Optimization : Sandbox-Native...</a></li>
<li><a href="https://arxiv.org/pdf/2607.14171">Branching Policy Optimization: Sandbox - Native Language Agent...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#LLM agents`, `#policy optimization`, `#sandbox`

---

<a id="item-12"></a>
## [RENEW: Repairing World Model Exploitation via Human Preferences](https://arxiv.org/abs/2607.14180) ⭐️ 8.0/10

The paper introduces RENEW, a method that uses human preferences over imagined rollouts to repair world model exploitation in offline reinforcement learning, formalized as Dynamics Learning from Human Feedback (DLHF). This work addresses a critical problem in offline model-based RL—model exploitation in low-coverage regions—by leveraging human intuition to detect unrealistic dynamics, offering a new paradigm that avoids expensive expert demonstrations or overly conservative algorithms. RENEW uses epistemic uncertainty to focus preference-based finetuning on exploitable regions, improving sample efficiency and limiting catastrophic forgetting compared to naive DLHF. It is evaluated on Jumanji and classic control environments.

rss · arXiv - Machine Learning · Jul 17, 04:00

**Background**: World models in offline RL can generate synthetic experience but often produce unrealistic rollouts in data-sparse regions, a phenomenon known as model exploitation. Prior solutions either require costly expert data or use conservative policies that limit generalization. Human preferences have been used in RLHF for policy alignment but not directly for dynamics model repair.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.14180">RENEW: Towards Learning World Models and Repairing Model ...</a></li>
<li><a href="https://mbrenndoerfer.com/writing/reward-modeling-rlhf-architecture-training">Reward Modeling: Building Preference Predictors for RLHF - Interactive</a></li>
<li><a href="https://openreview.net/forum?id=w4JFRTD0_R4">E-MCTS: Deep Exploration in Model-Based Reinforcement Learning ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#world models`, `#human feedback`, `#model exploitation`, `#offline RL`

---

<a id="item-13"></a>
## [JKP Framework Reveals VLM Instability Under Repeated Prompting](https://arxiv.org/abs/2607.14099) ⭐️ 8.0/10

Researchers introduced Just Keep Prompting (JKP), a multi-turn evaluation framework that tests vision-language models (VLMs) by repeatedly challenging their answers over up to 10 follow-up turns using three adversarial strategies. This work exposes significant epistemic instability in state-of-the-art VLMs like GPT-4o, Gemini 2.5 Pro, and Qwen3-VL-30B, highlighting a critical gap in robustness testing that has direct implications for safe real-world deployment of conversational AI systems. The JKP framework uses three strategies: Adversarial Negation, Pure Socratic Interrogation, and Context-Aware Socratic Summarization, evaluated on 720 multi-turn runs from the STAR benchmark. Results show that repeated prompting often destabilizes models rather than improving reasoning, with GPT-4o being the most brittle and oscillatory.

rss · arXiv - NLP · Jul 17, 04:00

**Background**: Vision-language models (VLMs) combine visual and textual understanding to answer questions about images. Epistemic stability refers to a model's ability to maintain correct beliefs under pressure or repeated questioning. The Socratic method, a dialogue technique of asking questions to stimulate critical thinking, inspired the prompting strategies used in JKP.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14099">[2607.14099] Just Keep Prompting : Evaluating Repetitive Socratic...</a></li>
<li><a href="https://arxiv.org/html/2607.14099">Just Keep Prompting : Evaluating Repetitive Socratic Prompting in...</a></li>
<li><a href="https://github.com/desenyon/pressbench">desenyon/pressbench: Pushback Resistance & Epistemic Stability ...</a></li>

</ul>
</details>

**Tags**: `#Vision-Language Models`, `#Robustness`, `#Evaluation`, `#AI Safety`, `#Conversational AI`

---

<a id="item-14"></a>
## [First Quantum NLP System for Arabic](https://arxiv.org/abs/2607.14100) ⭐️ 8.0/10

Researchers have developed the first quantum compositional NLP system for Arabic, using pregroup grammar to map sentences to quantum circuits and evaluating on word order, morphology, and sense disambiguation. This work demonstrates that quantum NLP can handle morphologically rich languages like Arabic, potentially opening new avenues for quantum computing applications in linguistics and expanding the reach of QNLP beyond English. The system converts Arabic sentences into quantum circuits where subjects, verbs, and objects become quantum gates, with wiring determined by pregroup grammar dependencies. It was compared against classical baselines AraVec and AraBERT.

rss · arXiv - NLP · Jul 17, 04:00

**Background**: Quantum natural language processing (QNLP) applies quantum computing to NLP by representing words as parameterized quantum circuits. Pregroup grammar is an algebraic formalism for syntax that assigns types to words and uses a monoidal structure to compose meanings. Arabic is a morphologically rich language with free word order, making it a challenging test for compositional semantics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pregroup_grammar">Pregroup grammar</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_natural_language_processing">Quantum natural language processing - Wikipedia</a></li>
<li><a href="https://github.com/bakrianoo/aravec">GitHub - bakrianoo/ aravec : AraVec is a pre-trained distributed word ...</a></li>

</ul>
</details>

**Tags**: `#quantum NLP`, `#Arabic`, `#pregroup grammar`, `#quantum circuits`, `#compositional semantics`

---

<a id="item-15"></a>
## [LLM Agents Lose Info in Text; Latent Channel Proposed](https://arxiv.org/abs/2607.14103) ⭐️ 8.0/10

A new paper demonstrates that LLM agents lose information when communicating via text, and proposes a sparse latent communication channel using Sparse Autoencoder (SAE) features that retains 99.4% probe accuracy at 28-fold compression, compared to 80.4% for text. This work challenges the assumption that text is sufficient for inter-agent communication in multi-agent systems, and could lead to more efficient and information-preserving communication protocols for LLM agents. The study constructs three communication channels (dense latent, sparse latent, and text) and uses SAE feature analysis to quantify information loss. Cross-architecture alignment between Llama and Mistral achieves 92% top-1 retrieval with Procrustes alignment, but text round-trip destroys 88% of SAE features.

rss · arXiv - NLP · Jul 17, 04:00

**Background**: Multi-agent systems (MAS) often rely on LLM agents communicating via natural language text. However, text may not capture the full richness of internal representations. Sparse autoencoders (SAEs) are used to extract interpretable features from LLM activations, enabling analysis of information content in different communication channels.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.14103">Latent Communication Between Language Model Agents: Channels...</a></li>
<li><a href="https://www.emergentmind.com/topics/latent-communication">Latent Communication in AI Systems</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#large language models`, `#sparse autoencoders`, `#latent communication`, `#information theory`

---

<a id="item-16"></a>
## [TTCD: Continuous Diffusion with Per-Token Times for Language Modeling](https://arxiv.org/abs/2607.14106) ⭐️ 8.0/10

Researchers introduced Token Time Continuous Diffusion (TTCD), a diffusion language model that operates in continuous space and assigns per-token times, allowing tokens to denoise at different rates. A 160M parameter TTCD model trained on OpenWebText and self-distilled outperforms discrete diffusion models at high speedups in both unconditional and conditional generation. TTCD addresses key limitations of discrete diffusion models, such as inaccuracy at high speedups due to parallel token sampling, by using continuous space and per-token times. This could enable faster and more accurate text generation, benefiting applications like conditional generation and structured output tasks (e.g., Sudoku solving). TTCD deterministically maps Gaussian noise to a final token canvas without further sampling, avoiding parallel token sampling errors. The per-token times allow more certain tokens to proceed faster and enable differentiated inter-token influences during refinement.

rss · arXiv - NLP · Jul 17, 04:00

**Background**: Diffusion language models generate text by iteratively denoising a sequence of tokens, typically operating in discrete space where multiple tokens are sampled in parallel, causing inaccuracies at high speedups. Continuous diffusion models, originally developed for images, map noise to data in a continuous space, but adapting them to discrete text has been challenging. TTCD introduces per-token times, a novel concept that allows each token to have its own denoising schedule, improving conditional generation and refinement.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14106">Token Time Continuous Diffusion for Language Modeling</a></li>
<li><a href="https://www.emergentmind.com/topics/continuous-diffusion-for-discrete-text">Continuous Diffusion for Discrete Text</a></li>
<li><a href="https://medium.com/@deblinab101/bridging-two-worlds-how-diffusion-models-are-catching-up-with-large-language-models-0310c9b1815e">Bridging Two Worlds: How Diffusion Models Are Catching... | Medium</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#language modeling`, `#continuous space`, `#generative AI`, `#machine learning`

---

<a id="item-17"></a>
## [Polestar: Drift-Aware Cache and Token Commitment for dLLMs](https://arxiv.org/abs/2607.14107) ⭐️ 8.0/10

Polestar is a training-free inference framework that uses token representation drift as a unified signal to jointly optimize KV-cache reuse and token commitment in diffusion large language models (dLLMs). It achieves up to 10.73% accuracy improvement, up to 3.7x higher throughput, and high decoding parallelism of 3.67 tokens per forward pass. This work addresses two key inefficiencies in dLLM inference—inefficient KV-cache reuse and suboptimal token commitment—that have hindered practical deployment. By setting a new state-of-the-art on the accuracy-throughput Pareto frontier, Polestar could enable faster and more cost-effective inference for diffusion-based language models. Polestar consists of two components: Polestar-Cache identifies stale KV-cache positions via drift and performs sparse refreshes, and Polestar-Commit detects sharp drift events to identify commit-ready tokens. The framework is evaluated on mathematics and coding benchmarks across several dLLM families, outperforming existing baselines.

rss · arXiv - NLP · Jul 17, 04:00

**Background**: Diffusion large language models (dLLMs) generate text by iteratively denoising a sequence of tokens in parallel, unlike autoregressive models that generate tokens one by one. However, bidirectional attention in dLLMs prevents efficient reuse of the key-value (KV) cache, and static confidence thresholds for parallel decoding can degrade quality. Polestar leverages the observation that token representations drift across decoding steps to address both issues jointly.

<details><summary>References</summary>
<ul>
<li><a href="https://piirz.medium.com/diffusion-based-llms-how-they-work-and-why-theyre-a-big-deal-a4a1de7636b4">Diffusion -Based LLMs : How They Work (and Why They’re...) | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/diffusion-llms-rewriting-rules-language-generation-neil-sahota-t82le">Diffusion LLMs : Rewriting the Rules of Language Generation</a></li>

</ul>
</details>

**Tags**: `#diffusion LLMs`, `#inference efficiency`, `#KV-cache`, `#token commitment`, `#machine learning systems`

---

<a id="item-18"></a>
## [SeeSE3: Probing 3D Euclidean Space in Vision Features](https://arxiv.org/abs/2607.14228) ⭐️ 8.0/10

The paper proposes novel probes to evaluate how well vision foundation models' features reflect 3D Euclidean space structure, finding strong correlations in self-supervised models. This work reveals that self-supervised vision models inherently encode 3D spatial structure without explicit supervision, which could lead to new latent-space navigation techniques for visual odometry and localization. The probes include a mutual neighborhood metric for topological alignment and a Poincaré Adapter to test linear accessibility of camera motion geometry from latent displacements.

rss · arXiv - Computer Vision · Jul 17, 04:00

**Background**: Vision foundation models are large neural networks trained on vast image data, often via self-supervised learning. The SE(3) group represents rigid transformations (rotation and translation) in 3D space. Previous work probed 3D awareness by regressing depth or normals, but this paper investigates the structure of feature space itself.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rigid_transformation">Rigid transformation - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.14228">SeeSE3: Emergence of 3D Space in Vision Features</a></li>

</ul>
</details>

**Tags**: `#3D vision`, `#representation learning`, `#self-supervised learning`, `#foundation models`, `#Euclidean space`

---

<a id="item-19"></a>
## [DCVC-MB: Neural B-Frame Codec with State-Space Models](https://arxiv.org/abs/2607.14305) ⭐️ 8.0/10

DCVC-MB introduces a neural video codec that uses state-space models for B-frame coding, achieving up to 30.45% BD-rate reduction over VTM-19.0-LDP and 8.98% over prior neural codecs. This work significantly advances neural video compression by improving B-frame efficiency, which is critical for streaming and storage applications. It demonstrates that state-space models can outperform traditional transformers and RNNs in video coding tasks. The codec incorporates an IBP frame strategy, a spatio-temporal fusion model based on state-space models, and an entropy-aware skipping mechanism to reduce coding time. It also includes two inference-time strategies to boost compression performance.

rss · arXiv - Computer Vision · Jul 17, 04:00

**Background**: Video codecs compress video by exploiting spatial and temporal redundancies. B-frames use both past and future frames for prediction, offering higher compression than P-frames but requiring more complex bidirectional processing. Traditional codecs like VTM are handcrafted, while neural video codecs (NVCs) use deep learning to learn compression. State-space models (SSMs) are a recent alternative to transformers for efficient long-range sequence modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/DCVC">GitHub - microsoft/DCVC: Deep Contextual Video Compression · GitHub</a></li>
<li><a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Pourreza_Extending_Neural_P-Frame_Codecs_for_B-Frame_Coding_ICCV_2021_paper.pdf">Extending Neural P-Frame Codecs for B - Frame Coding</a></li>

</ul>
</details>

**Tags**: `#neural video compression`, `#state-space models`, `#B-frame coding`, `#video codec`, `#deep learning`

---

<a id="item-20"></a>
## [Optimal Self-Distillation for Rectified Flow via Linear Probing](https://arxiv.org/abs/2607.14947) ⭐️ 8.0/10

This paper proves an exact affine path identity for optimal self-distillation in linear rectified flow, deriving the optimal mixing coefficient and a sign rule for correcting teacher velocity fields. This provides a theoretical framework for optimal self-distillation in rectified flow, offering closed-form solutions and practical tuning procedures that can improve generative model training and prevent collapse. The optimal mixing coefficient obeys a sign rule: positive mixing corrects under-regularized teachers, while negative mixing corrects over-regularized teachers. The paper also provides one-shot generalized cross-validation (GCV) and validation tuning procedures that avoid grid search.

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**Background**: Rectified flow is a generative model that learns a velocity field to transform noise into data via an ordinary differential equation. Self-distillation involves training a student model on a mixture of true and teacher-generated signals, which can lead to improvement or collapse. This paper studies optimal self-distillation for rectified flow with ridge regularization.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model - Wikipedia</a></li>
<li><a href="https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2412.01169/">OmniFlow: Any-to-Any Generation with Multi-Modal Rectified Flows</a></li>
<li><a href="https://labelyourdata.com/articles/machine-learning/model-distillation">Model Distillation : Teacher-Student Training Guide... | Label Your Data</a></li>

</ul>
</details>

**Tags**: `#self-distillation`, `#rectified flow`, `#generative models`, `#regularization`, `#theory`

---

<a id="item-21"></a>
## [Subjective Risk Decomposition Unifies UQ Measures](https://arxiv.org/abs/2607.15196) ⭐️ 8.0/10

A new arXiv paper proposes deriving epistemic and aleatoric uncertainty measures via decomposition of subjective risk using strictly proper losses, unifying many existing UQ measures under a common theoretical foundation. This work provides a principled framework that connects uncertainty quantification to learning theory, potentially enabling more systematic design of UQ methods in machine learning and statistics. The decomposition using reverse cross-entropy recovers classic information-theoretic uncertainty terms, and the framework extends to learning theory by introducing subjective risk analogues of excess risk, approximation error, and estimation error.

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**Background**: Uncertainty quantification (UQ) typically distinguishes epistemic uncertainty (due to lack of knowledge) and aleatoric uncertainty (due to inherent randomness). Existing UQ measures often rely on ad-hoc axioms or specific loss functions, lacking a unified derivation. This paper proposes that UQ measures should be consequences of higher-level modeling decisions, specifically the decomposition of subjective risk based on a strictly proper loss.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15196">[2607.15196] Subjective Risk Decomposition : A New View for...</a></li>
<li><a href="https://arxiv.org/html/2607.15196v1">Subjective Risk Decomposition : A New View for Uncertainty...</a></li>

</ul>
</details>

**Tags**: `#uncertainty quantification`, `#subjective risk`, `#epistemic uncertainty`, `#aleatoric uncertainty`, `#learning theory`

---

<a id="item-22"></a>
## [PiVoT: Real-Time Multi-Object Tracking from Radar Point Clouds](https://arxiv.org/abs/2607.13891) ⭐️ 8.0/10

PiVoT introduces a variational inference framework for end-to-end detection and tracking of a large, time-varying number of objects directly from noisy radar point clouds, without requiring external clustering or detectors. This work addresses key challenges in radar-based multi-object tracking, such as heavy clutter and large object populations, achieving real-time performance comparable to deep learning methods while being training-free, which is significant for autonomous driving and radar applications. PiVoT incorporates innovations like theoretically justified birth pruning, quadratic-to-linear complexity reductions for exact updates, and a computationally efficient Doppler Poisson model, enabling scalability to a thousand objects and robustness to clutter.

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**Background**: Multi-object tracking from radar point clouds is challenging due to heavy clutter and varying object counts. Traditional Bayesian trackers use Poisson measurement models but struggle with accuracy and efficiency. PiVoT leverages variational inference to jointly infer object states, shapes, existence probabilities, data association, and measurement rates.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13891">PiVoT: A Variational Solution for Real-time Large-scale Multi - object ...</a></li>
<li><a href="https://runzegan.github.io/projects/pivot/">Poisson Measurements -based Variational Multi-object Detection and...</a></li>

</ul>
</details>

**Tags**: `#multi-object tracking`, `#radar`, `#variational inference`, `#point clouds`, `#Bayesian tracking`

---

<a id="item-23"></a>
## [Weather Data Sabotage Risk Rising](https://www.technologyreview.com/2026/07/17/1140622/weather-data-sabotage/) ⭐️ 8.0/10

A new MIT Technology Review article warns that weather data sabotage is becoming a growing threat to industries like aviation, energy, and agriculture, driven by prediction markets and AI forecasting. Weather forecasts underpin critical decisions in multiple industries, and sabotage could lead to economic losses, safety risks, and even loss of life. Historically, weather data sabotage was physical (e.g., cutting cables), but new risks arise from prediction markets and AI-based forecasting that can be manipulated.

rss · MIT Technology Review · Jul 17, 08:57

**Background**: Weather data is collected from sensors, satellites, and weather stations worldwide, then processed into forecasts used by airlines, grid operators, and farmers. Sabotage can involve tampering with data collection or manipulation of AI models.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/17/1140622/weather-data-sabotage/">The risk of weather data sabotage is rising | MIT Technology Review</a></li>
<li><a href="https://asibiont.com/en/blog/risk-sabotazha-dannykh-o-pogode-rastet-chto-nuzhno-znat-biznesu-v-2026-godu">The Hidden Threat: Why the Risk of Weather Data Sabotage Is Rising...</a></li>

</ul>
</details>

**Tags**: `#weather data`, `#cybersecurity`, `#critical infrastructure`, `#risk assessment`

---