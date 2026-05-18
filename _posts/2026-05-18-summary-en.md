---
layout: default
title: "Horizon Summary: 2026-05-18 (EN)"
date: 2026-05-18
lang: en
---

> From 83 items, 35 important content pieces were selected

---

1. [Bun: All-in-One JavaScript Runtime and Toolchain](#item-1) ⭐️ 9.0/10
2. [NOVA Framework Reveals Fundamental Limits of AI Knowledge Discovery](#item-2) ⭐️ 9.0/10
3. [Rovelli Argues to Abandon the Hard Problem of Consciousness](#item-3) ⭐️ 8.0/10
4. [16-Byte x86 Demo Generates Matrix Rain and Music](#item-4) ⭐️ 8.0/10
5. [GDS Advises NHS to Keep Open Source Repositories Open](#item-5) ⭐️ 8.0/10
6. [CLI-Anything: Making All Software Agent-Native](#item-6) ⭐️ 8.0/10
7. [Open-source playbook for production GenAI agents](#item-7) ⭐️ 8.0/10
8. [HKUDS Releases ViMax: All-in-One Agentic Video Generation Framework](#item-8) ⭐️ 8.0/10
9. [ToM Benchmarks Don't Predict Real Human-AI Interaction](#item-9) ⭐️ 8.0/10
10. [Fair Outputs, Biased Internals in LLMs](#item-10) ⭐️ 8.0/10
11. [ICRL: Internalizing Self-Critique via RL](#item-11) ⭐️ 8.0/10
12. [Distributed Trust Framework for Verifiable Agent Authorization](#item-12) ⭐️ 8.0/10
13. [AgentStop: Early Termination to Save Energy in Local LLM Agents](#item-13) ⭐️ 8.0/10
14. [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](#item-14) ⭐️ 8.0/10
15. [Quantization Can Reintroduce Bias in LLMs](#item-15) ⭐️ 8.0/10
16. [MuteBench: Benchmarking Multimodal Fusion Robustness Under Sensor Failure](#item-16) ⭐️ 8.0/10
17. [On-Policy Self-Distillation Reduces LLM Safety Tax](#item-17) ⭐️ 8.0/10
18. [Transcriptome-Guided Diffusion Model for Drug Design](#item-18) ⭐️ 8.0/10
19. [Privacy Evaluation Gap in Generative Trajectory Models](#item-19) ⭐️ 8.0/10
20. [GQLA: Hardware-Adaptive LLM Decoding via Dual-Path Attention](#item-20) ⭐️ 8.0/10
21. [OP-Mix: Unified Data Mixing for LLM Training Lifecycle](#item-21) ⭐️ 8.0/10
22. [Massive Legal Citation Graph Built from 100M Ukrainian Court Decisions](#item-22) ⭐️ 8.0/10
23. [Eskwai: RAG-based AI Assistant for Legal Education in Ghana](#item-23) ⭐️ 8.0/10
24. [Neural Activation Patterns Across LLM Architectures Analyzed](#item-24) ⭐️ 8.0/10
25. [Why LMs Are Less Surprised Than Humans? Parse Multiplicity Tested](#item-25) ⭐️ 8.0/10
26. [Deep Pre-Alignment Improves Vision-Language Models](#item-26) ⭐️ 8.0/10
27. [Recursive Latent Refinement Boosts Generative Model Diversity](#item-27) ⭐️ 8.0/10
28. [Minerva-Ego: New Benchmark for Egocentric Video Reasoning](#item-28) ⭐️ 8.0/10
29. [Feature-Space Sampling Reduces Cost of 3D Group-Convolutional Neural Networks](#item-29) ⭐️ 8.0/10
30. [MorphoHELM: A Comprehensive Benchmark for Cell Painting](#item-30) ⭐️ 8.0/10
31. [MaxSketch: Robust Distinct Counting via Random Projections](#item-31) ⭐️ 8.0/10
32. [α-TCAV: Fixing Statistical Instability in Concept Activation Vectors](#item-32) ⭐️ 8.0/10
33. [Interpretable Domain Shift Detection via Subspace Attribution](#item-33) ⭐️ 8.0/10
34. [Explainable AI Isn't Enough: Rethinking Algorithmic Contestability](#item-34) ⭐️ 8.0/10
35. [Skew-Adaptive Conformal Prediction Improves Interval Efficiency](#item-35) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun: All-in-One JavaScript Runtime and Toolchain](https://github.com/oven-sh/bun) ⭐️ 9.0/10

Bun is an all-in-one JavaScript runtime, bundler, test runner, and package manager that aims to replace Node.js and multiple tools with a single executable. It was first released in September 2021 and has gained significant traction for its speed and integration. Bun dramatically simplifies JavaScript development by combining runtime, bundler, test runner, and package manager into one tool, reducing complexity and improving performance. Its use of JavaScriptCore instead of V8 and its Zig-based implementation offer faster startup and lower memory usage compared to Node.js. Bun supports Linux, macOS, and Windows, and can be installed via curl, npm, Homebrew, or Docker. It is designed as a drop-in replacement for Node.js, meaning existing Node.js projects can use Bun with minimal changes.

rss · GitHub Trending - Daily (All) · May 18, 15:38

**Background**: Traditionally, JavaScript developers use Node.js as the runtime, npm or yarn for package management, Jest or Mocha for testing, and Webpack or esbuild for bundling. Bun aims to replace all these with a single command-line tool, offering significant speed improvements by using JavaScriptCore (Safari's engine) and the Zig programming language.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**Tags**: `#JavaScript`, `#runtime`, `#tooling`, `#performance`, `#open-source`

---

<a id="item-2"></a>
## [NOVA Framework Reveals Fundamental Limits of AI Knowledge Discovery](https://arxiv.org/abs/2605.15219) ⭐️ 9.0/10

The NOVA framework models AI self-improvement loops as adaptive sampling over a knowledge space, identifying conditions for genuine discovery and failure modes including a contamination trap. It also proves a scaling law showing that cumulative generation cost grows as Θ(c_gen D^α) for D distinct discoveries. This work provides a theoretical foundation for understanding when AI systems can genuinely discover new knowledge versus merely exploiting existing data, which is critical for designing reliable self-improving AI. The identified contamination trap warns that as easy discoveries are exhausted, even small false-positive rates can overwhelm genuine discoveries with invalid artifacts. The framework identifies four failure modes: contamination, forgetting, exploration failure, and acceptance failure. It clarifies that Good-Turing estimation is a local batch-diversity diagnostic, not an estimator of historically undiscovered valid mass, and shows that expert human input is most valuable near autonomous exploration barriers.

rss · arXiv - AI · May 18, 04:00

**Background**: AI self-improvement loops involve generating candidates, verifying them, accumulating valid ones, and retraining the model. The NOVA framework formalizes this as adaptive sampling over a knowledge space, where each discovery reduces the remaining undiscovered mass. The scaling law derived assumes a Zipf-like distribution of discovery difficulty with exponent α>1.

**Tags**: `#AI`, `#knowledge discovery`, `#theoretical framework`, `#machine learning`, `#self-improvement`

---

<a id="item-3"></a>
## [Rovelli Argues to Abandon the Hard Problem of Consciousness](https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/) ⭐️ 8.0/10

Carlo Rovelli, a theoretical physicist, published an article arguing that the hard problem of consciousness is a philosophical dead end and that consciousness should be treated as a natural phenomenon to be studied empirically. This challenges a foundational debate in philosophy of mind and cognitive science, potentially shifting research focus from metaphysical puzzles to empirical investigation of consciousness. Rovelli draws parallels to historical scientific redefinitions, such as the concept of heat, and argues that the hard problem dissolves when we view consciousness as a natural phenomenon rather than a separate entity.

hackernews · ahalbert4 · May 18, 02:59 · [Discussion](https://news.ycombinator.com/item?id=48175140)

**Background**: The hard problem of consciousness, coined by philosopher David Chalmers in 1994, asks why and how physical processes in the brain give rise to subjective experience (qualia). It is contrasted with 'easy problems' that are amenable to functional explanation. The existence of the hard problem is disputed; some philosophers and scientists reject it, while others consider it a genuine challenge.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hard_problem_of_consciousness">Hard problem of consciousness</a></li>
<li><a href="https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/">There Is No ‘Hard Problem Of Consciousness’ | NOEMA</a></li>

</ul>
</details>

**Discussion**: Comments show substantive debate: some agree that consciousness should be redefined like heat, while others argue the article lacks proof and that we are missing something fundamental, akin to pre-electromagnetism understanding.

**Tags**: `#consciousness`, `#philosophy`, `#cognitive science`, `#AI`, `#neuroscience`

---

<a id="item-4"></a>
## [16-Byte x86 Demo Generates Matrix Rain and Music](https://hellmood.111mb.de//wake_up_16b_writeup.html) ⭐️ 8.0/10

A 16-byte x86 real-mode program, detailed in a writeup, simultaneously displays a Matrix-like falling-characters visual and generates music via the PC speaker. This demonstrates extreme size coding in the demoscene, pushing the limits of what can be achieved in just 16 bytes, inspiring other developers to explore low-level optimization. The program runs in x86 real mode and uses the PC speaker's programmable interval timer to generate audio, while the visual is created by directly writing to video memory.

hackernews · HellMood · May 17, 23:10 · [Discussion](https://news.ycombinator.com/item?id=48173962)

**Background**: Size coding is a demoscene discipline where programs are compressed to extremely small sizes (e.g., 64 bytes or less) while still producing impressive graphics and sound. The PC speaker, an early computer audio device, generates simple tones via a timer chip. Real mode is a 16-bit operating mode on x86 processors that allows direct hardware access.

<details><summary>References</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=f-VQfigEoO0">The Art of Code Wrestling in the Demoscene – Size ... - YouTube</a></li>
<li><a href="https://en.wikipedia.org/wiki/PC_speaker">PC speaker - Wikipedia</a></li>
<li><a href="https://wiki.osdev.org/Protected_Mode">Protected Mode - OSDev Wiki</a></li>

</ul>
</details>

**Discussion**: Commenters compared the demo to other tiny demos like 'Freespin' and 'A Mind Is Born', noting the impressive feat of combining audio and visual in 16 bytes. One user remarked that their comment itself is larger than the program.

**Tags**: `#demoscene`, `#x86`, `#low-level programming`, `#audio-visual`, `#size coding`

---

<a id="item-5"></a>
## [GDS Advises NHS to Keep Open Source Repositories Open](https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything) ⭐️ 8.0/10

The UK Government Digital Service (GDS) published guidance on May 14, 2026, recommending that public sector organizations keep open source repositories open by default, countering the NHS's decision to close its repositories after vulnerabilities were reported via Project Glasswing. This intervention signals a major policy rift within the UK government, as GDS publicly contradicts the NHS's security-driven retreat from open source, potentially setting a precedent for open source use across the entire public sector. GDS's guidance, titled 'AI, open code and vulnerability risk in the public sector,' emphasizes that making repositories private adds costs and reduces reuse and scrutiny, advising closure only as a deliberate exception. Terence Eden interprets this as a rare public escalation of internal civil service disagreement.

rss · Simon Willison · May 17, 15:59

**Background**: Project Glasswing is Anthropic's cybersecurity initiative launched in April 2026, using advanced AI to find vulnerabilities in critical open source software. The NHS responded to vulnerabilities reported through this project by closing its open source repositories, a move criticized by open source advocates. GDS is the UK government's digital transformation unit, responsible for setting digital standards across the public sector.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Government_Digital_Service">Government Digital Service - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>

</ul>
</details>

**Tags**: `#open source`, `#government policy`, `#security`, `#NHS`, `#GDS`

---

<a id="item-6"></a>
## [CLI-Anything: Making All Software Agent-Native](https://github.com/HKUDS/CLI-Anything) ⭐️ 8.0/10

HKUDS released CLI-Anything, an open-source framework and hub that generates CLI wrappers for any software, enabling AI agents to interact with them seamlessly. The project includes CLI-Hub, a community repository for sharing and installing these CLIs. This project bridges the gap between existing software and AI agents, making virtually any application controllable by agents without requiring native API support. It could accelerate the adoption of AI agents in real-world workflows by providing a universal integration layer. CLI-Anything generates standard Python CLI packages using Click, with JSON output for agent consumption and human-readable output. The CLI-Hub allows users to browse, install, and manage community-contributed CLIs via a simple command-line interface.

rss · GitHub Trending - Daily (All) · May 18, 15:38

**Background**: AI agents typically require programmatic interfaces (APIs) to interact with software, but many applications lack such interfaces. CLI-Anything addresses this by creating command-line wrappers that expose software functionality in a structured way, making it agent-native. The concept of agent-native software refers to systems designed to be operated by AI agents autonomously.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HKUDS/CLI-Anything">GitHub - HKUDS/CLI-Anything: "CLI-Anything: Making ALL Software Agent ...</a></li>
<li><a href="https://clianything.org/">CLI Anything</a></li>
<li><a href="https://sourceforge.net/projects/cli-anything.mirror/">CLI-Anything download | SourceForge.net</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#CLI`, `#Software Integration`, `#Open Source`, `#Tooling`

---

<a id="item-7"></a>
## [Open-source playbook for production GenAI agents](https://github.com/NirDiamant/agents-towards-production) ⭐️ 8.0/10

NirDiamant released 'Agents Towards Production', an open-source repository with 28 code-first tutorials for building and deploying production-grade generative AI agents. This resource bridges the gap between prototype and enterprise deployment, covering critical topics like security, multi-agent coordination, and GPU scaling, which are essential for real-world GenAI applications. Tutorials include stateful workflows, vector memory, Docker deployment, FastAPI endpoints, security guardrails, observability, and evaluation, using frameworks like LangGraph and LangChain.

rss · GitHub Trending - Daily (All) · May 18, 15:38

**Background**: GenAI agents are autonomous systems built on large language models (LLMs) that can complete tasks with minimal human input. LangGraph is an orchestration framework for building reliable, stateful agents, while LangChain simplifies LLM integration into applications.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/NirDiamant/GenAI_Agents">GitHub - NirDiamant/ GenAI _ Agents : 50+ tutorials and implementations...</a></li>
<li><a href="https://www.langchain.com/langgraph">LangGraph : Agent Orchestration Framework for Reliable AI Agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/LangChain">LangChain - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#GenAI`, `#agents`, `#production`, `#tutorials`, `#open-source`

---

<a id="item-8"></a>
## [HKUDS Releases ViMax: All-in-One Agentic Video Generation Framework](https://github.com/HKUDS/ViMax) ⭐️ 8.0/10

ViMax is an open-source, multi-agent video generation framework from HKU Data Science Lab that integrates director, screenwriter, producer, and video generator roles into a single system, enabling automated multi-shot video generation with character and scene consistency. ViMax addresses key limitations of current AI video tools—short clips, inconsistency, and lack of narrative structure—by providing an end-to-end solution that automates scriptwriting, storyboarding, character creation, and video generation, potentially reducing production time by 40-60% for content creators. ViMax claims 35% better coherence than traditional models and supports Python 3.12 with the uv package manager. The framework is licensed under MIT and includes a quick start guide for easy deployment.

rss · GitHub Trending - Python · May 18, 15:38

**Background**: Current AI video generation tools often produce only short clips with inconsistent characters and scenes, and lack narrative depth. ViMax uses a multi-agent approach where specialized AI agents handle different aspects of video production, similar to a human film crew, to create coherent multi-shot videos from a simple concept input.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HKUDS/ViMax">GitHub - HKUDS / ViMax : " ViMax : Agentic Video Generation (Director...)</a></li>
<li><a href="https://pixel4it.com/vimax-agentic-video-generation-guide/">ViMax Agentic Video Generation: A Designer's Complete Guide</a></li>
<li><a href="https://sutopo.com/vimax-ai-agentic-video-generation-review/">ViMax AI Agentic Video Generation Review - sutopo.com</a></li>

</ul>
</details>

**Tags**: `#video generation`, `#AI agents`, `#machine learning`, `#computer vision`, `#generative AI`

---

<a id="item-9"></a>
## [ToM Benchmarks Don't Predict Real Human-AI Interaction](https://arxiv.org/abs/2605.15205) ⭐️ 8.0/10

A new study proposes an interactive evaluation paradigm for Theory of Mind in LLMs, finding that improvements on static benchmarks do not translate to better human-AI interactions. This challenges the validity of existing ToM benchmarks and highlights the need for interaction-based assessments to develop socially aware LLMs for real-world applications. The study systematically evaluated four ToM enhancement techniques across four datasets and a user study, covering goal-oriented and experience-oriented tasks.

rss · arXiv - AI · May 18, 04:00

**Background**: Theory of Mind (ToM) is the ability to attribute mental states to oneself and others, crucial for social interactions. Existing LLM ToM benchmarks typically use static, third-person multiple-choice questions, which may not capture the dynamic, first-person nature of human-AI interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Theory_of_mind_in_animals">Theory of mind in animals</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/978-981-97-8440-0_6-1">Theory of Mind in Human-AI Interaction and AI - Springer</a></li>

</ul>
</details>

**Tags**: `#Theory of Mind`, `#Large Language Models`, `#Human-AI Interaction`, `#Evaluation Benchmark`

---

<a id="item-10"></a>
## [Fair Outputs, Biased Internals in LLMs](https://arxiv.org/abs/2605.15217) ⭐️ 8.0/10

A new paper reveals that instruction-tuned LLMs can suppress output bias while retaining asymmetric latent biases in internal representations that can causally reverse decisions when reinjected. This finding is critical for high-stakes domains like mortgage underwriting, as it shows that behavioral audits focusing only on outputs are insufficient and that exploitable internal biases may persist undetected. Using activation steering and novel cross-layer interventions, the authors demonstrate that reinjecting suppressed demographic representations at critical layers can cause near-complete decision reversals, and the effect is asymmetric across demographic groups.

rss · arXiv - AI · May 18, 04:00

**Background**: Instruction-tuned LLMs are trained to follow instructions and often exhibit fair outputs. However, they may still encode biased associations internally. Activation steering is an inference-time technique that adjusts internal activations to control outputs. This paper uses causal intervention methods to probe whether these internal biases can causally affect decisions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15217v1">Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent ...</a></li>
<li><a href="https://www.emergentmind.com/topics/activation-steering-method">Activation Steering in LLMs</a></li>
<li><a href="https://raktimsingh.com/counterfactual-causality-neural-networks-interventions/">Counterfactual Causality Inside Neural Networks ... - Raktim Singh</a></li>

</ul>
</details>

**Tags**: `#LLM fairness`, `#latent bias`, `#causal intervention`, `#high-stakes decisions`, `#AI safety`

---

<a id="item-11"></a>
## [ICRL: Internalizing Self-Critique via RL](https://arxiv.org/abs/2605.15224) ⭐️ 8.0/10

Researchers propose ICRL, a reinforcement learning framework that jointly trains a solver and a critic from a shared backbone to internalize critique, enabling the model to correct errors without external feedback. The method achieves average gains of 6.4 points on agentic tasks and 7.0 points on mathematical reasoning over GRPO using Qwen3-4B and Qwen3-8B backbones. ICRL addresses a key limitation in current self-improvement methods for LLMs, where models fail to retain improvements after critique is removed. By internalizing critique, it enhances AI alignment and agent capabilities, potentially reducing reliance on external supervision. ICRL introduces a distribution-calibration re-weighting ratio to handle the distribution shift between critique-conditioned and critique-free behavior, and a role-wise group advantage estimation to stabilize joint optimization. The learned 8B critic is comparable to 32B critics while using substantially fewer tokens.

rss · arXiv - AI · May 18, 04:00

**Background**: Large language models (LLMs) often make mistakes, and external critique can guide them to correct behavior. However, when the critique is removed, the model may fail again, indicating it has not internalized the guidance. ICRL uses reinforcement learning to jointly train a solver and a critic, where the critic is rewarded based on the solver's performance gain, incentivizing actionable feedback that the solver can internalize.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15224v1">ICRL: Learning to Internalize Self-Critique with Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#large language models`, `#self-improvement`, `#AI alignment`, `#critique`

---

<a id="item-12"></a>
## [Distributed Trust Framework for Verifiable Agent Authorization](https://arxiv.org/abs/2605.15228) ⭐️ 8.0/10

A new paper introduces the Distributed Trust Framework (DTF), a verification framework that replaces standing identity-based authorization with proof-derived authority for autonomous AI agents in sovereign systems. This addresses a critical gap in AI safety: autonomous agents can generate unsafe actions even with valid credentials. DTF makes agentic execution governable, auditable, and bounded, which is essential for cloud infrastructure, regulated data, and national-scale digital services. DTF introduces a Justification Proof to encode the admissibility basis of an action, a consensus model for independent evaluation, an ephemeral Execution Identity derived from the approved proof, and an append-only Evidence Chain. The framework is instantiated over an OpenKedge-based governed mutation substrate.

rss · arXiv - AI · May 18, 04:00

**Background**: Traditional authorization assumes that callers with valid credentials are safe, but autonomous AI agents can generate syntactically valid yet semantically unsafe actions. Governed mutation substrates interpose on agent actions by requiring intents and evaluating context and policy, but they shift the trust boundary to the authorization decision itself. DTF makes that decision verifiable, distributed, and replayable.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15228">[2605.15228] Verifiable Agentic Infrastructure: Proof - Derived ...</a></li>
<li><a href="https://www.openkedge.io/">OpenKedge — Governance Protocol for AI-Driven Mutation</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#authorization`, `#autonomous agents`, `#distributed systems`, `#verification`

---

<a id="item-13"></a>
## [AgentStop: Early Termination to Save Energy in Local LLM Agents](https://arxiv.org/abs/2605.15206) ⭐️ 8.0/10

Researchers introduced AgentStop, a lightweight efficiency supervisor that predicts and preemptively terminates unlikely-to-succeed trajectories in local LLM-based agents, reducing wasted energy by 15-20% with less than 5% utility drop. This work addresses the critical issue of energy inefficiency in local LLM agents, which is essential for sustainable edge AI deployment and privacy-preserving automation on consumer devices. AgentStop uses low-cost execution signals like token-level log probabilities to make termination decisions, and was evaluated on web-based question answering and coding benchmarks on consumer hardware.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: LLM agents are AI systems that use large language models to autonomously perform multi-step tasks like coding or web research. Deploying them locally on user devices preserves privacy and avoids API costs, but agentic workflows consume significantly more energy than single LLM inferences due to iterative reasoning, tool use, and retries.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.15075v1">Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap - arXiv</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#energy efficiency`, `#edge AI`, `#sustainable computing`

---

<a id="item-14"></a>
## [TeamTR: Trust-Region Fine-Tuning for Multi-Agent LLM Coordination](https://arxiv.org/abs/2605.15207) ⭐️ 8.0/10

TeamTR introduces a trust-region fine-tuning framework that addresses compounding occupancy shift in multi-agent LLM teams, achieving 7.1% average improvement over baselines. This work identifies and formalizes a key failure mode in multi-agent LLM fine-tuning, providing a principled solution with theoretical guarantees, which is crucial for advancing reliable multi-agent LLM systems. The paper proves that stale-occupancy evaluation incurs a penalty scaling quadratically with the number of agents, while intermediate-occupancy evaluation reduces it to linear scaling. TeamTR resamples trajectories after each component update and enforces per-agent divergence control.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Multi-agent LLM systems involve multiple language models collaborating on tasks, but sequential fine-tuning can cause distribution shifts that compound across agents. Trust-region methods, common in reinforcement learning, constrain policy updates to ensure stable improvement.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05216">[2605.05216] SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM Training with Monotonic Improvement Guarantees - arXiv</a></li>
<li><a href="https://arxiv.org/abs/2508.10340">[2508.10340] Multi-Agent Trust Region Policy Optimisation: A Joint Constraint Approach</a></li>

</ul>
</details>

**Tags**: `#multi-agent LLM`, `#fine-tuning`, `#trust-region`, `#coordination`, `#reinforcement learning`

---

<a id="item-15"></a>
## [Quantization Can Reintroduce Bias in LLMs](https://arxiv.org/abs/2605.15208) ⭐️ 8.0/10

A new study reveals that post-training quantization of LLMs can cause stereotypical biases to emerge, especially at low precision, following a dose-response pattern. The paper tests three models at five precision levels on the BBQ bias benchmark. This finding is critical for safe deployment of compressed LLMs, as standard quality metrics like perplexity fail to detect bias emergence. It underscores the need for quality-aware compression protocols that explicitly test for fairness before deployment. At 3-bit quantization, 6-21% of previously unbiased items develop new stereotypical behaviors, while models' willingness to select 'unknown' answers declines by 17.4%. Even at 4-bit, 2.5-5.6% of items already show new biases, despite perplexity increasing by less than 3%.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Large language models (LLMs) are often compressed via post-training quantization to reduce costs, but the impact on bias is poorly understood. The BBQ benchmark is a dataset designed to test social biases in question answering. This study systematically evaluates bias emergence across multiple models and precision levels.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2110.08193">BBQ : A Hand-Built Bias Benchmark for Question Answering</a></li>
<li><a href="https://ukgovernmentbeis.github.io/inspect_evals/evals/bias/bbq/">BBQ : Bias Benchmark for Question Answering</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#quantization`, `#bias`, `#safety`, `#compression`

---

<a id="item-16"></a>
## [MuteBench: Benchmarking Multimodal Fusion Robustness Under Sensor Failure](https://arxiv.org/abs/2605.15235) ⭐️ 8.0/10

MuteBench is a new benchmark that evaluates multimodal fusion architectures under two types of sensor failure—modality missing and within-modality missing—across 9 clinical datasets, 6 fusion architectures, and over 125,000 samples. This benchmark addresses a critical gap in clinical AI by systematically evaluating robustness to sensor failures, which are common in real-world settings. The finding that architecture family matters more than parameter count for robustness provides actionable guidance for designing reliable multimodal systems. Channel-independent models tolerate modality missing well but can be sensitive to within-modality missing, especially on short sequences. Curriculum modality dropout protects reliably only up to the maximum dropout rate used in training, and a PTB-XL case study suggests diffusion-based imputation can improve downstream classification under within-modality missing.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Multimodal fusion combines data from multiple sensors (e.g., ECG, EEG) to improve clinical AI performance. However, sensors often fail in practice, leading to missing data. Existing benchmarks typically evaluate only one failure mode or a limited set of architectures, leaving a gap in understanding robustness across diverse conditions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15235">[2605.15235] MuteBench: Modality Unavailability Tolerance Evaluation...</a></li>

</ul>
</details>

**Tags**: `#multimodal fusion`, `#clinical AI`, `#robustness`, `#benchmark`, `#missing data`

---

<a id="item-17"></a>
## [On-Policy Self-Distillation Reduces LLM Safety Tax](https://arxiv.org/abs/2605.15239) ⭐️ 8.0/10

Researchers propose OPSA (On-Policy Self-Distillation for Safety Alignment), a method that uses the model's own rollouts and a teacher flip rate metric to reduce the safety tax in LLM alignment. This work addresses a critical trade-off in LLM safety alignment, where improving safety often degrades reasoning ability. OPSA achieves a stronger safety-reasoning trade-off, especially on smaller models, which could make safety alignment more practical for resource-constrained deployments. OPSA uses a frozen teacher copy of the model conditioned on a privileged safety context, providing dense per-token KL supervision. The teacher flip rate metric measures how often the privileged context converts unsafe responses into safe ones, guiding the search for effective safety contexts.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Safety alignment in LLMs often involves fine-tuning on safety demonstrations, but this can cause a distributional mismatch between training data and the model's own outputs, leading to a 'safety tax' — a drop in reasoning ability. Off-policy training exacerbates this issue. OPSA mitigates it by using on-policy self-distillation, where the model learns from its own generations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.17075">LoRA is All You Need for Safety Alignment of Reasoning LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#alignment`, `#self-distillation`, `#safety tax`, `#on-policy`

---

<a id="item-18"></a>
## [Transcriptome-Guided Diffusion Model for Drug Design](https://arxiv.org/abs/2605.15243) ⭐️ 8.0/10

Researchers propose CURE, a multi-resolution transcriptome-guided diffusion framework that designs drug molecules conditioned on desired cellular state transitions, formalizing transcriptome-based drug design as a generative inverse problem. This work bridges the gap between transcriptomic perturbations and molecular generation, enabling phenotype-driven drug discovery without requiring target structures, which could accelerate the development of drugs for complex diseases with dysregulated pathways. CURE features a Transcriptome Perturbation Functional Feature Extractor (TFE) that distills perturbation embeddings, aligns them to dual chemical views, and performs heterogeneity-aware aggregation to handle noisy transcriptomic data. It outperforms baselines in structural quality and functional consistency, validated via zero-shot gene-inhibitor design.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Diffusion models are a class of generative AI that learn to reverse a noising process to create new data. In drug design, they have been applied to generate molecules with desired properties. Transcriptomic perturbations measure changes in gene expression caused by a drug, providing a functional readout of its effect. However, designing molecules directly from transcriptomic data is challenging due to the domain gap between biology and chemistry and the sparsity of signals.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.09511v1">Diffusion Models for Molecules : A Survey of Methods and Tasks</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10994218/">Diffusion models in bioinformatics and computational biology - PMC</a></li>

</ul>
</details>

**Tags**: `#drug design`, `#diffusion models`, `#transcriptomics`, `#generative AI`, `#computational biology`

---

<a id="item-19"></a>
## [Privacy Evaluation Gap in Generative Trajectory Models](https://arxiv.org/abs/2605.15246) ⭐️ 8.0/10

This paper identifies a significant gap in privacy evaluation for generative trajectory models and demonstrates Membership Inference Attacks against GANs, VAEs, and Diffusion Models, showing that their generative nature does not eliminate privacy risks. This work highlights that generative trajectory models, widely used in urban intelligence, may leak sensitive training data, challenging the common assumption that generative models inherently preserve privacy. The authors implement Membership Inference Attacks (MIAs) on representative generative models for trajectory data, demonstrating the feasibility of empirical privacy evaluation and revealing that privacy risks persist despite the models' generative nature.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Generative models like GANs, VAEs, and Diffusion Models are used to create synthetic trajectory data for urban intelligence, but their privacy properties are often assumed rather than rigorously evaluated. Membership Inference Attacks (MIAs) are a standard method to assess privacy leakage by determining whether a specific data point was part of the training set.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1610.05820">[1610.05820] Membership Inference Attacks against Machine Learning Models - arXiv</a></li>
<li><a href="https://grokipedia.com/page/Membership_Inference_Attack">Membership Inference Attack</a></li>
<li><a href="https://www.ibm.com/docs/en/watsonx/saas?topic=atlas-membership-inference-attack">Membership inference attack risk for AI - IBM</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#generative models`, `#trajectory data`, `#membership inference attack`, `#AI security`

---

<a id="item-20"></a>
## [GQLA: Hardware-Adaptive LLM Decoding via Dual-Path Attention](https://arxiv.org/abs/2605.15250) ⭐️ 8.0/10

GQLA modifies Multi-head Latent Attention (MLA) to support both MQA and GQA decoding paths from the same weights, enabling efficient inference on both high-end and commodity GPUs without retraining. This allows a single model to adapt to diverse hardware, reducing deployment costs and enabling multi-token prediction on commodity GPUs like the H20, which was previously impossible with MLA. GQLA exposes an MQA-absorb path identical to MLA's and a GQA path with per-group expanded cache; the runtime selects the optimal path per hardware. TransGQLA converts pretrained GQA checkpoints (e.g., LLaMA-3-8B) to GQLA, compressing KV cache to 28.125% on the MQA path.

rss · arXiv - Machine Learning · May 18, 04:00

**Background**: Multi-head Latent Attention (MLA) used in DeepSeek-V2/V3 compresses keys and values into a low-rank latent, achieving high efficiency on H100 GPUs but only supporting a single MQA decoding path. Group-Query Attention (GQA) is a middle ground between Multi-Head Attention (MHA) and Multi-Query Attention (MQA), grouping queries to share key-value projections. GQLA bridges these approaches for hardware adaptability.

<details><summary>References</summary>
<ul>
<li><a href="https://liorsinai.github.io/machine-learning/2025/02/22/mla.html">DeepSeek 's Multi - Head Latent Attention - Lior Sinai</a></li>
<li><a href="https://medium.com/data-science/deepseek-v3-explained-1-multi-head-latent-attention-ed6bee2a67c4">DeepSeek -V3 Explained 1: Multi - head Latent Attention | Medium</a></li>
<li><a href="https://cyk1337.github.io/notes/2024/05/10/Memory-Efficient-Attention/">Memory-Efficient Attention : MHA vs . MQA vs . GQA vs . MLA</a></li>

</ul>
</details>

**Tags**: `#attention mechanisms`, `#LLM inference`, `#hardware adaptation`, `#DeepSeek`, `#efficient decoding`

---

<a id="item-21"></a>
## [OP-Mix: Unified Data Mixing for LLM Training Lifecycle](https://arxiv.org/abs/2605.15220) ⭐️ 8.0/10

Researchers propose OP-Mix (On-Policy Mix), a data mixing algorithm that treats data mixing as an online decision problem across the entire language model training lifecycle, using low-rank adapters to cheaply simulate candidate mixtures. OP-Mix unifies data mixing across pretraining, continual midtraining, and continual instruction tuning, eliminating the need for separate proxy models and reducing compute by up to 95% while matching or improving performance. In pretraining, OP-Mix improves average perplexity by 6.3% over no mixing; for continual learning, it matches retraining and on-policy distillation while using 66% and 95% less compute, respectively.

rss · arXiv - NLP · May 18, 04:00

**Background**: Data mixing determines how to combine different data sources during language model training, significantly affecting model quality. Existing methods often rely on smaller proxy models or fixed domain sets and address only one training phase. Low-rank adaptation (LoRA) is a technique that adapts large models by adding lightweight trainable parameters, enabling efficient simulation of different data mixtures.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">[2106.09685] LoRA: Low - Rank Adaptation of Large Language Models</a></li>

</ul>
</details>

**Tags**: `#data mixing`, `#language model training`, `#continual learning`, `#pretraining`, `#low-rank adaptation`

---

<a id="item-22"></a>
## [Massive Legal Citation Graph Built from 100M Ukrainian Court Decisions](https://arxiv.org/abs/2605.15362) ⭐️ 8.0/10

Researchers constructed the first large-scale citation graph from 100.7 million Ukrainian court decisions, extracting 502 million citation links with perfect precision on a validation sample. This work demonstrates that judicial citation structure can automatically recover legal domain boundaries and predict legislative importance with near-perfect accuracy, offering a powerful tool for legal informatics and AI-assisted legal analysis. The citation graph was built from the complete EDRSR registry (99.5 million full texts, 1.1 TB) using regex on commodity hardware in about 5 hours, with precision of 1.00 (95% Wilson CI: [0.982, 1.000]).

rss · arXiv - NLP · May 18, 04:00

**Background**: Citation graphs in law map how court decisions reference each other, revealing influence and structure. The Louvain method is a popular algorithm for detecting communities in large networks by optimizing modularity. The Wilson confidence interval provides a robust estimate for precision in validation samples.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Louvain_method">Louvain method - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval">Binomial proportion confidence interval - Wikipedia</a></li>
<li><a href="https://7aac.gov.ua/en/edrsr/">edrsr | Seventh Administrative Court of Appeal</a></li>

</ul>
</details>

**Tags**: `#legal informatics`, `#citation graph`, `#network analysis`, `#natural language processing`, `#machine learning`

---

<a id="item-23"></a>
## [Eskwai: RAG-based AI Assistant for Legal Education in Ghana](https://arxiv.org/abs/2605.15380) ⭐️ 8.0/10

Researchers developed Eskwai for Students, a retrieval-augmented generation (RAG) AI assistant for legal education in Ghana, and deployed it over 30 months with 3,100 law students generating 32,000 queries. This work addresses a critical gap in applying generative AI to legal education in the Global South, providing insights into query patterns and ethical concerns, and demonstrating a scalable approach for under-resourced regions. The system is grounded in a curated database of over 12,000 case laws and 1,400 pieces of Ghanaian legislation, and the study evaluated helpfulness while analyzing query types that raise ethical concerns.

rss · arXiv - NLP · May 18, 04:00

**Background**: Retrieval-augmented generation (RAG) is a technique that enhances large language models by retrieving relevant information from external sources before generating responses, reducing hallucinations and improving accuracy. This is particularly important in legal contexts where precision and source verification are critical. The Global South often lacks access to advanced AI tools tailored to local legal systems, making this deployment significant.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.pinecone.io/learn/retrieval-augmented-generation/">Retrieval - Augmented Generation (RAG) | Pinecone</a></li>

</ul>
</details>

**Tags**: `#generative AI`, `#legal education`, `#retrieval augmented generation`, `#Global South`, `#AI ethics`

---

<a id="item-24"></a>
## [Neural Activation Patterns Across LLM Architectures Analyzed](https://arxiv.org/abs/2605.15436) ⭐️ 8.0/10

A new study systematically compares neural activation patterns across six LLM architectures on twelve cognitive tasks, revealing that mathematical reasoning yields the highest attention entropy and decoder models exhibit higher sparsity than encoder models. This analysis provides empirical guidance for selecting LLM architectures based on task requirements, potentially improving efficiency and performance in big data applications. The study examined 144 task-model combinations, measuring final activation values, attention entropy, and sparsity patterns across encoder and decoder architectures.

rss · arXiv - NLP · May 18, 04:00

**Background**: Large language models (LLMs) come in different architectures, primarily encoder-only (e.g., BERT), decoder-only (e.g., GPT), and encoder-decoder (e.g., T5). Attention entropy measures how evenly attention is distributed across tokens, while sparsity indicates how many activations are near zero. These metrics help understand model behavior and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.03589v1">Entropy and Attention Dynamics in Small Language Models ...</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.485.pdf">Attention Entropy is a Key Factor: An Analysis of Parallel Context</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder">Understanding Encoder And Decoder LLMs</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#neural activation`, `#cognitive tasks`, `#attention entropy`, `#model comparison`

---

<a id="item-25"></a>
## [Why LMs Are Less Surprised Than Humans? Parse Multiplicity Tested](https://arxiv.org/abs/2605.15440) ⭐️ 8.0/10

A new study tests the hypothesis that language models' ability to maintain more simultaneous parses than humans explains their underprediction of difficulty in garden path sentences, using RNNGs with beam search. The results show that reducing the number of parses increases predicted garden path effects, but not enough to match human data. This work addresses a fundamental mismatch between language models and human sentence processing, which is crucial for improving model alignment with human cognition. The findings suggest that parse multiplicity alone cannot reconcile LM surprisal with human reading times, pointing to other factors like memory constraints or reanalysis costs. The study used Recurrent Neural Network Grammars (RNNGs) with word-synchronous beam search to vary the number of simultaneous parses when computing word surprisal. Even with a single parse, the predicted garden path effects were still much smaller than those observed in humans, indicating that other mechanisms are at play.

rss · arXiv - NLP · May 18, 04:00

**Background**: Surprisal theory links word predictability to processing difficulty, and language model surprisals often predict human reading times well in naturalistic text. However, they systematically underpredict difficulty in garden path sentences, which are syntactically ambiguous sentences that initially mislead readers. The parse multiplicity mismatch hypothesis suggests that LMs can consider more syntactic interpretations simultaneously than humans, reducing surprisal.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prediction_in_language_comprehension">Prediction in language comprehension - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Garden-path_sentence">Garden-path sentence</a></li>
<li><a href="https://arxiv.org/abs/1602.07776">[1602.07776] Recurrent Neural Network Grammars</a></li>

</ul>
</details>

**Tags**: `#psycholinguistics`, `#language models`, `#surprisal theory`, `#syntactic ambiguity`, `#RNNG`

---

<a id="item-26"></a>
## [Deep Pre-Alignment Improves Vision-Language Models](https://arxiv.org/abs/2605.15300) ⭐️ 8.0/10

Researchers propose Deep Pre-Alignment (DPA), a novel architecture that replaces the standard ViT encoder with a small VLM to deeply align visual features with the LLM's text space, achieving 1.9–3.0 point gains across multimodal benchmarks. DPA addresses a critical alignment bottleneck in current VLMs, enabling more efficient use of LLM depth for reasoning rather than modality alignment, and offers a seamless upgrade path with minimal overhead. At the 4B scale, DPA outperforms baselines by 1.9 points across 8 benchmarks, widening to 3.0 points at 32B scale, and reduces language capability forgetting by 32.9% on 3 text benchmarks. The gains are consistent across Qwen3 and LLaMA 3.2 families.

rss · arXiv - Computer Vision · May 18, 04:00

**Background**: Most VLMs use a lightweight projector to map ViT encoder outputs to the LLM, but visual features remain distant from the text space in early LLM layers, wasting depth on alignment. DPA replaces the ViT with a small VLM as a perceiver that pre-aligns features before feeding into the LLM.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Vision Language Models`, `#Multimodal Learning`, `#Architecture`, `#Alignment`, `#arXiv`

---

<a id="item-27"></a>
## [Recursive Latent Refinement Boosts Generative Model Diversity](https://arxiv.org/abs/2605.15309) ⭐️ 8.0/10

The paper introduces Recursive Latent Refinement (RTM), which replaces the single-pass latent mapping in style-based generators with iterative refinement, consistently improving both quality and diversity across multiple benchmarks. This work addresses the saturation of the FID metric and the persistent problem of mode collapse in generative models, offering a practical method that improves diversity without sacrificing quality, which is crucial for real-world applications requiring broad coverage. RTM integrated with Implicit Maximum Likelihood Estimation (IMLE) achieves the highest precision and recall among current state-of-the-art approaches while maintaining competitive FID, with improvements on CIFAR-10, CelebA-HQ 256x256, and nine few-shot benchmarks.

rss · arXiv - Computer Vision · May 18, 04:00

**Background**: FID (Fréchet Inception Distance) is a widely used metric for evaluating generative models, but it conflates sample fidelity with mode coverage and is near saturation, meaning models can achieve low FID while still suffering from mode collapse. Mode collapse occurs when a generative model produces only a limited variety of outputs, failing to cover the full data distribution. Recursive Latent Refinement (RTM) addresses this by iteratively refining the latent code, encouraging the model to explore diverse modes.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15309v1">One Pass Is Not Enough: Recursive Latent Refinement for Generative Models - arXiv</a></li>

</ul>
</details>

**Tags**: `#generative models`, `#image generation`, `#FID`, `#mode coverage`, `#IMLE`

---

<a id="item-28"></a>
## [Minerva-Ego: New Benchmark for Egocentric Video Reasoning](https://arxiv.org/abs/2605.15342) ⭐️ 8.0/10

Researchers introduced Minerva-Ego, a benchmark for evaluating complex egocentric visual reasoning with spatiotemporal mask annotations, revealing a large gap between state-of-the-art models and human performance. This benchmark addresses the lack of intermediate reasoning step evaluation in video understanding, which is crucial for advancing embodied AI and egocentric agents. Minerva-Ego extends existing egocentric video datasets with multi-step multimodal questions and human-annotated spatiotemporal reasoning traces, and experiments show that providing 'where' and 'when' hints significantly improves model performance.

rss · arXiv - Computer Vision · May 18, 04:00

**Background**: Egocentric video understanding involves reasoning from a first-person perspective, which is essential for applications like augmented reality and robotics. Existing benchmarks often only evaluate final answers, not the reasoning process, limiting insight into model capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15342">Minerva - Ego : Spatiotemporal Hints for Egocentric Video Understanding</a></li>

</ul>
</details>

**Tags**: `#egocentric video understanding`, `#benchmark`, `#visual reasoning`, `#embodied AI`, `#spatiotemporal reasoning`

---

<a id="item-29"></a>
## [Feature-Space Sampling Reduces Cost of 3D Group-Convolutional Neural Networks](https://arxiv.org/abs/2605.15368) ⭐️ 8.0/10

This paper proposes sampling in feature space rather than geometric space for group-convolutional neural networks (GCNNs), decoupling geometric resolution from memory and computational cost. The method replaces dense geometric samples with representative samples selected by feature similarity, enabling substantial acceleration of equivariant 3D classifiers. This work addresses a key limitation of GCNNs—exponential growth of computational cost with degrees of freedom—which has hindered practical applications in 3D geometry. By enabling efficient training and inference, it could make equivariant deep learning more accessible for real-world 3D tasks such as object recognition and scene understanding. The main empirical finding shows that a coarse feature-space sampling already preserves classification accuracy remarkably well. This permits precomputation based on geometric similarity, which further accelerates training of equivariant 3D classifiers.

rss · arXiv - Computer Vision · May 18, 04:00

**Background**: Group-convolutional neural networks (GCNNs) incorporate symmetry as an inductive bias by sampling a transformation group densely and correlating data and filters in different poses to maintain equivariance. However, this dense sampling leads to high computational costs, especially for 3D data involving translations and rotations, where costs grow exponentially with degrees of freedom. The proposed method decouples geometric resolution from computational effort by sampling in feature space instead of geometric space.

**Tags**: `#group-convolutional neural networks`, `#3D geometry`, `#equivariance`, `#deep learning`, `#computational efficiency`

---

<a id="item-30"></a>
## [MorphoHELM: A Comprehensive Benchmark for Cell Painting](https://arxiv.org/abs/2605.15383) ⭐️ 8.0/10

Researchers introduced MorphoHELM, an open benchmark that standardizes and extends evaluation protocols for feature extraction methods in Cell Painting assays, evaluating the widest range of methods to date. This benchmark addresses the fragmented evaluation landscape in morphological profiling, enabling fair comparisons across methods and revealing trade-offs, which is critical for advancing drug screening and biological research. A defining feature is that each task is evaluated at different degrees of batch effects, directly quantifying how biological signal detection degrades with noise; no existing model outperforms classic computer vision strategies across all settings.

rss · arXiv - Computer Vision · May 18, 04:00

**Background**: Cell Painting is a high-content imaging assay that uses fluorescent dyes to visualize cellular compartments, enabling morphological profiling. Representation extraction methods, including deep learning, are used to quantify these images, but evaluation has been inconsistent across studies.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/cell_painting">Cell painting</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#microscopy`, `#representation learning`, `#cell painting`, `#deep learning`

---

<a id="item-31"></a>
## [MaxSketch: Robust Distinct Counting via Random Projections](https://arxiv.org/abs/2605.15571) ⭐️ 8.0/10

Researchers introduced MaxSketch, a max-linear sketch using random Gaussian projections, to estimate distinct elements in high-dimensional noisy streams with improved memory guarantees under geometric structure. This work bridges classical streaming algorithms and modern representation learning, showing that geometric structure can fundamentally reduce the complexity of distinct counting, which is crucial for applications like duplicate detection in learned embeddings. MaxSketch requires only O(log n / ε²) random projections to achieve a (1+ε)-factor approximation, significantly improving over the Θ(√n) worst-case memory bound for general metric spaces.

rss · arXiv - Data Science & Statistics · May 18, 04:00

**Background**: Classical distinct counting sketches like HyperLogLog rely on consistent hash values for identical elements, but fail when observations are noisy and high-dimensional. Random projection is a dimensionality reduction technique that approximately preserves distances, and is used here to handle approximate similarity.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_random_projection">Gaussian random projection</a></li>

</ul>
</details>

**Tags**: `#data streams`, `#distinct counting`, `#random projections`, `#robust estimation`, `#machine learning`

---

<a id="item-32"></a>
## [α-TCAV: Fixing Statistical Instability in Concept Activation Vectors](https://arxiv.org/abs/2605.15688) ⭐️ 8.0/10

The paper introduces α-TCAV, a unified framework that replaces the discontinuous indicator function in the standard TCAV score with a parameterized smooth function, addressing a fundamental flaw that caused non-decaying variance. It also provides theoretical analysis of CAV distributions and practical guidance for tuning the α parameter. This work fixes a critical instability in TCAV, a widely used explainability method, potentially improving the reliability of concept-based interpretability in deep learning. The unified framework also subsumes Multi-TCAV and offers computational savings, impacting both researchers and practitioners in AI interpretability. The analysis shows that the standard TCAV score's reliance on a discontinuous indicator function leads to non-decaying variance in critical regimes. α-TCAV replaces this with a smooth function, yielding a probabilistic formulation that can imitate Multi-TCAV at lower cost or provide a calibrated Bayes-optimal measure.

rss · arXiv - Data Science & Statistics · May 18, 04:00

**Background**: Concept Activation Vectors (CAVs) are used to represent high-level concepts (e.g., 'striped') in the latent space of neural networks. Testing with CAVs (TCAV) quantifies a concept's influence on model predictions by computing a sensitivity score based on the cosine similarity between the CAV and the gradient of the model's output. However, the standard TCAV score uses a discontinuous indicator function to count positive similarities, which introduces statistical instability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2404.03713v1">Explaining Explainability: Understanding Concept Activation Vectors - arXiv</a></li>
<li><a href="https://christophm.github.io/interpretable-ml-book/detecting-concepts.html">29 Detecting Concepts – Interpretable Machine Learning</a></li>
<li><a href="https://www.emergentmind.com/topics/concept-activation-vector-cav">Concept Activation Vector (CAV) - Emergent Mind</a></li>

</ul>
</details>

**Tags**: `#explainability`, `#deep learning`, `#concept activation vectors`, `#interpretability`, `#machine learning theory`

---

<a id="item-33"></a>
## [Interpretable Domain Shift Detection via Subspace Attribution](https://arxiv.org/abs/2605.15920) ⭐️ 8.0/10

Researchers developed a method to detect and interpret domain shifts in high-dimensional data by identifying localized density anomalies and their supporting feature subspaces, validated on benchmarks and real ECG data. This work enhances machine learning robustness by making domain shifts interpretable, which is crucial for deploying models in safety-critical applications like medical AI where hidden biases can lead to failures. The method first detects localized density anomalies using a custom algorithm, then identifies the feature subspace where the anomaly is most pronounced, enabling traceability to a small set of features. It also provides a protocol to extract subsets with no residual distributional difference from two unlabeled datasets.

rss · arXiv - Data Science & Statistics · May 18, 04:00

**Background**: Domain shift refers to differences in data distributions between training and deployment, which can degrade model performance. Traditional detection methods often lack interpretability, making it hard to understand why a shift occurred. This work addresses that gap by attributing shifts to specific feature subspaces.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.16261">[2505.16261] Interpretable Anomaly Detection in Encrypted Traffic Using SHAP with Machine Learning Models - arXiv</a></li>

</ul>
</details>

**Tags**: `#domain shift`, `#interpretability`, `#anomaly detection`, `#machine learning`, `#ECG`

---

<a id="item-34"></a>
## [Explainable AI Isn't Enough: Rethinking Algorithmic Contestability](https://arxiv.org/abs/2605.16041) ⭐️ 8.0/10

A new paper argues that explainable AI (XAI) has neglected algorithmic contestability—the ability to review and correct erroneous decisions—and proposes formal definitions and three types of evidence that can overturn decisions. This work addresses a critical gap in XAI research with high ethical and legal importance, potentially empowering individuals to challenge automated decisions in areas like loans, hiring, and cheating detection. The paper distinguishes contestability from recourse: contestability presumes a decision may be incorrect and seeks evidence to overturn it, while recourse assumes the decision is valid and provides pathways to change it. Three types of evidence warranting reversal are predictive multiplicity, incorrect feature values, and neglected overruling evidence.

rss · arXiv - Data Science & Statistics · May 18, 04:00

**Background**: Explainable AI (XAI) aims to make machine learning decisions understandable to humans. However, most XAI methods focus on explaining why a decision was made or how to change it (recourse), rather than enabling individuals to contest potentially incorrect decisions. Algorithmic contestability is the ability to review and correct erroneous algorithmic decisions, which is crucial for fairness and accountability.

**Tags**: `#explainable AI`, `#algorithmic contestability`, `#fairness`, `#machine learning ethics`, `#XAI`

---

<a id="item-35"></a>
## [Skew-Adaptive Conformal Prediction Improves Interval Efficiency](https://arxiv.org/abs/2605.16145) ⭐️ 8.0/10

A new skew-adaptive extension of split conformal prediction for regression is proposed, which learns local skewness via an additional predictive model to produce more efficient prediction intervals while maintaining finite-sample marginal validity. This method addresses a practical limitation of existing conformal prediction methods that assume symmetric residuals, enabling tighter intervals in skewed regions and improving uncertainty quantification in real-world regression tasks. The method uses the inverse hyperbolic sine transform of signed scaled residuals as the training target for an additional model, and includes a calibration-sample-based estimator to compare expected relative future width against classical scaled-score intervals.

rss · arXiv - Data Science & Statistics · May 18, 04:00

**Background**: Conformal prediction is a distribution-free framework for uncertainty quantification that produces valid prediction intervals under exchangeability. Standard split conformal prediction often uses symmetric intervals, which can be inefficient when residuals are skewed. This work adapts intervals to local skewness for improved efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#uncertainty quantification`, `#regression`, `#machine learning`, `#statistics`

---