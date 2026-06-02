---
layout: default
title: "Horizon Summary: 2026-06-02 (EN)"
date: 2026-06-02
lang: en
---

> From 103 items, 25 important content pieces were selected

---

1. [Microsoft unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs](#item-1) ⭐️ 8.0/10
2. [Godot Engine: Open-Source Game Engine Trending on GitHub](#item-2) ⭐️ 8.0/10
3. [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](#item-3) ⭐️ 8.0/10
4. [Post-Solve Robustness Layer Proposed for MILP Decision Engines](#item-4) ⭐️ 8.0/10
5. [Consilium Protocol: BFT-Based Multi-Model AI Deliberation](#item-5) ⭐️ 8.0/10
6. [Deliberative Curation Protocol for Multi-Agent Knowledge Bases](#item-6) ⭐️ 8.0/10
7. [Delayed Reward Attribution Boosts Multi-Agent RL for LLMs](#item-7) ⭐️ 8.0/10
8. [Universal Quantum Transformer Achieves Exact Reasoning](#item-8) ⭐️ 8.0/10
9. [Grokers: Write-Time Intelligence for Knowledge Graphs](#item-9) ⭐️ 8.0/10
10. [BitsMoE: Spectral-Energy-Guided Bit Allocation for MoE LLMs](#item-10) ⭐️ 8.0/10
11. [LLM Valence Axis Aligns with Human EEG](#item-11) ⭐️ 8.0/10
12. [ADNTNs: Exponential Compression of DNNs via Differentiable Tensor Networks](#item-12) ⭐️ 8.0/10
13. [World Models Survey: Taxonomy, Methods, and Applications](#item-13) ⭐️ 8.0/10
14. [LLM Agent Tool-calling: Evaluation Sensitivity & RL Waste](#item-14) ⭐️ 8.0/10
15. [Proactive Lifecycle-Based Survey for GenAI Threat Detection](#item-15) ⭐️ 8.0/10
16. [SENSE: Semantic Embedding for Robust Speculative Decoding](#item-16) ⭐️ 8.0/10
17. [TrustLDM: Benchmarking Trustworthiness in Language Diffusion Models](#item-17) ⭐️ 8.0/10
18. [ART: Run-Time KV Cache Pruning Boosts LLM Throughput 20%](#item-18) ⭐️ 8.0/10
19. [Multi-Domain Red Teaming Framework for Medical LLMs](#item-19) ⭐️ 8.0/10
20. [Planktonzilla-17M: Largest Plankton Image Dataset Released](#item-20) ⭐️ 8.0/10
21. [MIND: Diffusion Model with Explicit Manifold Geometry](#item-21) ⭐️ 8.0/10
22. [Zero-Shot Super-Resolution in Operator Learning: Theory](#item-22) ⭐️ 8.0/10
23. [Parameter-Free Group-Conditional Online Conformal Prediction](#item-23) ⭐️ 8.0/10
24. [FK-PINNs: Preconditioning Loss Landscape with Feynman-Kac Supervision](#item-24) ⭐️ 8.0/10
25. [NFIL3 Protein Identified as Key Barrier in CAR T Therapy](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft unveils MAI-Thinking-1 and MAI-Code-1-Flash LLMs](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

Microsoft announced two new large language models: MAI-Thinking-1, a 35B active parameter reasoning model with a 128K context window, and MAI-Code-1-Flash, a 5B parameter code model built for GitHub Copilot. Both models are trained on clean, commercially licensed data without distillation from third-party models. These models achieve high performance with low parameter counts, potentially reducing inference costs and enabling local deployment. MAI-Thinking-1 claims to be preferred over Sonnet 4.6 in blind evaluations, challenging the notion that larger models are always necessary. MAI-Thinking-1 is a sparse Mixture of Experts model with ~1T total parameters but only 35B active, and is currently available to select early partners. MAI-Code-1-Flash is rolling out to GitHub Copilot individual users in Visual Studio Code, and both models emphasize training on appropriately licensed data.

rss · Simon Willison · Jun 2, 22:21

**Background**: Large language models (LLMs) are AI systems trained on vast text data to generate human-like text. Parameter count often correlates with capability, but larger models are expensive to run. Microsoft's new models aim to deliver competitive performance at lower cost, using clean data to address copyright concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI-Thinking-1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI - Code - 1 - Flash | Microsoft AI</a></li>
<li><a href="https://mashable.com/tech/microsoft-launches-new-mai-family-of-models-at-build">Microsoft launches new MAI family of AI models at Microsoft Build | Mashable</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Microsoft`, `#AI models`, `#reasoning`, `#code generation`

---

<a id="item-2"></a>
## [Godot Engine: Open-Source Game Engine Trending on GitHub](https://github.com/godotengine/godot) ⭐️ 8.0/10

Godot Engine, a free and open-source 2D and 3D game engine, is trending on GitHub due to high community engagement, though no new version or major announcement has been made. This highlights the growing interest in open-source game development tools, as Godot offers a viable alternative to proprietary engines like Unity and Unreal Engine, empowering indie developers and studios. Godot uses the permissive MIT license, supports one-click export to desktop, mobile, web, and console platforms, and is community-driven with support from the Godot Foundation.

rss · GitHub Trending - Daily (All) · Jun 2, 23:29

**Background**: Godot Engine was originally developed in-house by Juan Linietsky and Ariel Manzur before being open-sourced in February 2014. It provides a unified interface for 2D and 3D game development, with a built-in scripting language (GDScript) and a node-based scene system.

**Tags**: `#game engine`, `#open source`, `#2D`, `#3D`, `#cross-platform`

---

<a id="item-3"></a>
## [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](https://github.com/OpenBMB/VoxCPM) ⭐️ 8.0/10

OpenBMB has released VoxCPM2, a 2-billion-parameter tokenizer-free text-to-speech model trained on over 2 million hours of multilingual speech data, supporting 30 languages, voice design, controllable voice cloning, and 48kHz audio output. VoxCPM2 advances open-source TTS by eliminating tokenization, enabling more natural and expressive speech synthesis, and offering creative voice design from text descriptions alone, which lowers the barrier for voice content creation. The model uses a diffusion autoregressive architecture operating in continuous latent space, built on a MiniCPM-4 backbone, and is available on Hugging Face and ModelScope with a live demo and documentation.

rss · GitHub Trending - Daily (All) · Jun 2, 23:29

**Background**: Traditional TTS systems convert text to speech using discrete audio tokens, which can lose subtle nuances. Tokenizer-free models like VoxCPM2 directly generate continuous speech representations, preserving more naturalness and expressiveness. OpenBMB is known for open-source large language models like MiniCPM.

<details><summary>References</summary>
<ul>
<li><a href="https://voxcpm.net/">VoxCPM: Tokenizer - Free TTS & Zero-Shot Voice Cloning</a></li>
<li><a href="https://voxcpm.readthedocs.io/en/latest/models/architecture.html">Architecture - VoxCPM 2 .0 documentation</a></li>
<li><a href="https://explainx.ai/blog/voxcpm2-tokenizer-free-tts-multilingual-voice-cloning-2026">VoxCPM 2 : The 2B Parameter Tokenizer-Free TTS Model ... | explainx.ai</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#speech generation`, `#voice cloning`, `#multilingual`, `#open-source`

---

<a id="item-4"></a>
## [Post-Solve Robustness Layer Proposed for MILP Decision Engines](https://arxiv.org/abs/2606.00002) ⭐️ 8.0/10

A position paper on arXiv (2606.00002) introduces the concept of a post-solve robustness layer for MILP decision engines, formalizing epsilon-near-optimal feasible neighborhoods and solution smoothness under perturbations. This addresses a critical gap in optimization pipelines for high-stakes systems, where small perturbations can invalidate solutions or cause discontinuous shifts, and proposes making robustness a first-class output of decision engines. The paper synthesizes insights from sensitivity analysis, robust optimization, neighborhood search, adversarial testing, and learning-based enhancements, and calls for certified inner approximations, probabilistic robustness estimation, and adversarial robustness margins.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Mixed-Integer Linear Programming (MILP) is a mathematical optimization method used to find the best solution from a set of discrete and continuous variables. Decision engines that solve MILP problems are widely used in industrial systems, but they typically assume that input parameters are fixed, ignoring real-world perturbations. Robust optimization and stochastic programming address uncertainty at solve time, but do not audit the robustness of a given solution after it is computed.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00002">[2606.00002] Position Paper: Post - Solve Robustness in Decision...</a></li>
<li><a href="https://artificialintelligenceherald.com/posts/post-solve-robustness-gap-milp-2026">Post - Solve Robustness Gap in MILP Decision Engines - AI Herald</a></li>

</ul>
</details>

**Tags**: `#MILP`, `#robust optimization`, `#decision engines`, `#perturbation analysis`

---

<a id="item-5"></a>
## [Consilium Protocol: BFT-Based Multi-Model AI Deliberation](https://arxiv.org/abs/2606.00005) ⭐️ 8.0/10

The Consilium Protocol introduces a Byzantine Fault Tolerance-derived architecture for structured multi-model AI deliberation, treating inter-model disagreement as epistemic signal rather than error. Across 1,478 sessions, it shows that cognitive persona, not model, determines epistemic behavior, and that RLHF creates domain-specific blind spots. This work demonstrates that inexpensive models with proper personas can match frontier model output, potentially reducing AI system costs dramatically. It also reveals systematic biases from RLHF alignment, which has significant implications for AI safety and alignment research. The protocol uses an In-Sample/Out-of-Sample validation framework from quantitative finance to distinguish training-data consensus from empirically grounded conclusions. Total cost for the complete battery was only 217 USD, and run-to-run reproducibility averaged ±2.2% standard deviation.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Byzantine Fault Tolerance (BFT) is a consensus mechanism from distributed computing that ensures system reliability despite faulty or malicious nodes. The Consilium Protocol adapts BFT to multi-model AI systems, where each model acts as a node with a cognitive persona that dictates its reasoning style, separate from the underlying model weights.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00005">[2606.00005] Emergent Collaborative Deliberation in Multi - Model AI...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Byzantine_fault">Byzantine fault - Wikipedia</a></li>
<li><a href="https://pypi.org/project/consilium/">Multi - model deliberation CLI. 4 frontier LLMs debate with rotating...</a></li>

</ul>
</details>

**Tags**: `#multi-model AI`, `#Byzantine Fault Tolerance`, `#epistemic synthesis`, `#RLHF`, `#alignment`

---

<a id="item-6"></a>
## [Deliberative Curation Protocol for Multi-Agent Knowledge Bases](https://arxiv.org/abs/2606.00007) ⭐️ 8.0/10

A new deliberative curation protocol for multi-agent knowledge bases is proposed, combining reputation-weighted voting, EigenTrust amplification, and graduated sanctions, evaluated via agent-based simulation with 100 agents. This protocol addresses the critical challenge of governing collective knowledge curation in multi-agent AI systems, showing improved resilience under adversarial conditions compared to majority voting, which is vital for trustworthy AI collaboration. The protocol degrades roughly three times more slowly than majority vote under stress, and ablation analysis identifies commit-reveal vote concealment as the most impactful component (8.2-8.6pp precision improvement). Graduated sanctions were not exercised in simulation and remain unvalidated.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Multi-agent systems involve multiple AI agents collaborating in shared knowledge ecosystems. Reputation systems like Beta Reputation and EigenTrust help assess agent trustworthiness, while graduated sanctions deter misbehavior. This protocol adapts these concepts for stateless agents, addressing challenges like model homogeneity and sycophancy.

<details><summary>References</summary>
<ul>
<li><a href="https://people.cs.vt.edu/~irchen/6204b/paper/Josang-BECC02-slide.pptx">The Beta Reputation System Jøsang and R. Ismail 15th Bled...</a></li>
<li><a href="https://en.wikipedia.org/wiki/EigenTrust">EigenTrust - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10458-020-09465-8">Runtime revision of sanctions in normative multi-agent systems | Autonomous Agents and Multi-Agent Systems | Springer Nature Link</a></li>

</ul>
</details>

**Tags**: `#multi-agent systems`, `#knowledge curation`, `#AI governance`, `#reputation systems`, `#agent-based simulation`

---

<a id="item-7"></a>
## [Delayed Reward Attribution Boosts Multi-Agent RL for LLMs](https://arxiv.org/abs/2606.00017) ⭐️ 8.0/10

Researchers introduce delayed per-step reward attribution with eligibility gating, a pipeline that computes rewards only at episode end and propagates them back to originating steps, enabling stable RL training for language model agents in multi-agent games. A single 8B-parameter open-source model trained with this method matched or surpassed GPT-5 in the MindGames Arena benchmark at NeurIPS 2025. This work addresses a fundamental challenge in multi-agent reinforcement learning with language models: entangled outcomes across time and agents. By enabling sample-efficient training with smaller open-source models to compete with much larger proprietary systems, it democratizes access to advanced AI strategic interaction capabilities. The pipeline uses vLLM's continuous batching for asynchronous rollout generation, curriculum-based opponent sampling, and multi-level stratified batch construction. Eligibility gating excludes steps without valid dependent information from training, ensuring only relevant steps contribute to learning.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Reinforcement learning typically requires per-step rewards, but in multi-agent games, an action's quality may depend on future events or other players' moves that are unknown at the time. Delayed per-step reward attribution computes rewards only at episode end and propagates them back, while eligibility gating filters out steps that lack valid dependent information. vLLM's continuous batching improves inference throughput for generating multiple rollouts asynchronously.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.00017">MindGames Arena Generalization Track: In2AI Solution with Delayed ...</a></li>
<li><a href="https://papers.cool/arxiv/2606.00017">MindGames Arena Generalization Track: In2AI Solution with Delayed ...</a></li>
<li><a href="https://insujang.github.io/2024-01-07/llm-inference-continuous-batching-and-pagedattention/">LLM Inference: Continuous Batching and PagedAttention</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#multi-agent systems`, `#language models`, `#reward attribution`, `#strategic interaction`

---

<a id="item-8"></a>
## [Universal Quantum Transformer Achieves Exact Reasoning](https://arxiv.org/abs/2606.00045) ⭐️ 8.0/10

Researchers introduced the Universal Quantum Transformer (UQT), a quantum-native architecture that uses geometric phase embedding and SU(2) wave-interference to perform exact mathematical reasoning on a 5-qubit system, perfectly learning modular arithmetic and non-Abelian algebra. This work demonstrates that quantum architectures can achieve deterministic generalization without the stochastic instability and massive over-parameterization required by classical neural networks, potentially revolutionizing quantum machine learning and enabling exact AI on near-term quantum hardware. The UQT bypasses the quadratic bottleneck of classical self-attention and logarithmically compresses representation dimensions, and has been deployed on IBM Quantum computers, proving viability on NISQ hardware.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Classical neural networks struggle with exact mathematical symmetries like modular arithmetic, often requiring massive parameter scaling and exhibiting delayed generalization (grokking). The UQT leverages quantum properties such as superposition and interference to naturally encode discrete logical rules, achieving a phenomenon called crystallization that goes beyond grokking.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00045">[2606.00045] Universal Quantum Transformer</a></li>
<li><a href="https://medium.com/@quantaeon.ai/why-classical-ai-struggles-with-exact-logic-and-how-quantum-physics-fixes-it-28740a1c0986">Why Classical AI Struggles with Exact Logic (And How Quantum ...)</a></li>

</ul>
</details>

**Tags**: `#quantum computing`, `#machine learning`, `#transformers`, `#algebraic reasoning`, `#arXiv`

---

<a id="item-9"></a>
## [Grokers: Write-Time Intelligence for Knowledge Graphs](https://arxiv.org/abs/2606.00050) ⭐️ 8.0/10

Grokers introduces a bottom-up inductive architecture for typed knowledge graphs that shifts comprehension work to write time, achieving near-100% KV-cache hit rates and eliminating LM calls at query time. This architecture could significantly reduce computational costs for knowledge-intensive applications by avoiding repeated comprehension at query time, contrasting with RAG systems that incur full cost per query. The paper proves three formal theorems: Byte-Identity Theorem for KV-cache reuse, Accumulation Monotonicity Theorem for growing wisdom library, and Dual-Traversal Ordering Theorem for correct traversal. A reference implementation is provided in the open-source Qbix/Safebox/Safebots stack.

rss · arXiv - AI · Jun 2, 04:00

**Background**: Knowledge graphs represent entities and their relationships as typed nodes and edges. Traditional RAG systems retrieve relevant information and feed it to a language model at query time, incurring comprehension cost per query. Grokers inverts this by performing comprehension once at write time, storing enriched attributes for future queries.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00050">[2606.00050] Grokers: Bottom-Up Inductive Comprehension and Write-Time Intelligence over Typed Knowledge Graphs</a></li>
<li><a href="https://arxiv.org/html/2606.00050">Grokers: Bottom-Up Inductive Comprehension and Write-Time...</a></li>

</ul>
</details>

**Tags**: `#knowledge graphs`, `#AI architecture`, `#RAG`, `#KV-cache`, `#formal proofs`

---

<a id="item-10"></a>
## [BitsMoE: Spectral-Energy-Guided Bit Allocation for MoE LLMs](https://arxiv.org/abs/2606.00079) ⭐️ 8.0/10

BitsMoE proposes a novel spectral-energy-guided framework for mixed-precision quantization of Mixture-of-Experts (MoE) large language models, using SVD decomposition and activation-aware bit allocation to achieve efficient memory compression. Under 2-bit quantization on Qwen3-30B-A3B-Base, BitsMoE accelerates quantization by 12.3×, improves average accuracy by 27.83 percentage points, and increases decoding speed by 1.76× over GPTQ. This work addresses the critical memory bottleneck in deploying MoE LLMs, which require all expert weights to be resident in memory despite sparse activation. By enabling ultra-low-bit quantization with minimal accuracy loss, BitsMoE can significantly reduce the hardware requirements for running large MoE models, making them more accessible for edge and resource-constrained environments. BitsMoE decomposes each MoE layer via SVD into a shared basis (kept unquantized) and expert-specific spectral factors (quantized with varying bit-widths). The bit-width for each unit is determined by solving an integer linear program that minimizes estimated reconstruction loss under a fixed bit budget, guided by an activation-aware reconstruction surrogate.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: Mixture-of-Experts (MoE) is a neural network architecture that uses multiple specialized sub-networks (experts) and a gating mechanism to activate only a subset of experts per input, reducing computation. However, all expert weights must be loaded in memory, creating a memory bottleneck. Quantization reduces model precision (e.g., from 16-bit to 2-bit) to compress memory, but uniform quantization fails to account for varying importance across experts and weights. Mixed-precision quantization allocates different bit-widths to different parts of the model, but existing methods lack a principled way to determine bit allocation for MoE structures.

<details><summary>References</summary>
<ul>
<li><a href="https://tokenmix.ai/blog/moe-architecture-explained">MoE Architecture : Why Every AI Model Got... - TokenMix Blog</a></li>
<li><a href="https://jacobgil.github.io/deeplearning/tensor-decompositions-deep-learning">Accelerating Deep Neural Networks with Tensor Decompositions</a></li>

</ul>
</details>

**Tags**: `#LLM quantization`, `#Mixture-of-Experts`, `#model compression`, `#efficient inference`, `#spectral analysis`

---

<a id="item-11"></a>
## [LLM Valence Axis Aligns with Human EEG](https://arxiv.org/abs/2606.00129) ⭐️ 8.0/10

Researchers constructed a one-dimensional valence direction (V-axis) from LLMs using only nine emotion-evoking sentences and showed it aligns with human EEG neural activity across 123 subjects watching affective videos. This work bridges LLMs and human neural representations, suggesting shared emotional valence structures across models and brains, which could advance brain-computer interfaces and AI alignment research. The V-axis was validated via zero-shot transfer to sentiment benchmarks and cross-model consistency across 14 LLMs; 36 EEG classifiers spontaneously rediscovered the same direction without exposure to the V-axis.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: Emotional valence refers to the intrinsic attractiveness (positive) or averseness (negative) of an event or stimulus. EEG (electroencephalography) measures electrical activity in the brain. Large language models (LLMs) like GPT-4 learn rich representations from text, and recent research explores their alignment with human neural activity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00129">[2606.00129] A Shared Valence Axis Across Modern LLMs and...</a></li>
<li><a href="https://arxiv.org/html/2606.00129">A Shared Valence Axis Across Modern LLMs and Human EEG: The...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#neural representation`, `#EEG`, `#emotional valence`, `#cognitive science`

---

<a id="item-12"></a>
## [ADNTNs: Exponential Compression of DNNs via Differentiable Tensor Networks](https://arxiv.org/abs/2606.00130) ⭐️ 8.0/10

This paper introduces Automatically Differentiable Nonlinear Tensor Networks (ADNTNs), a family of structured weight generators that train compact core tensors end-to-end via reverse-mode automatic differentiation, achieving per-layer compression ratios from 2000× to 77000× on AlexNet and VGG-16 while maintaining or improving accuracy. ADNTNs offer a mathematically structured and hardware-aware approach to drastically reduce neural network size, potentially enabling deployment of large models on resource-constrained devices without significant accuracy loss. The paper focuses on three architectures: Tree Tensor Networks (TTNs), augmented TTNs (aTTNs) with boundary disentanglers, and Multi-scale Entanglement Renormalisation Ansatze (MERA); it also supports nonlinear activations, batching, and hardware-aware execution schedules.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: Tensor networks are mathematical structures originally developed in quantum physics to efficiently represent high-dimensional states. In deep learning, they have been used for model compression by factorizing weight matrices into smaller tensors. ADNTNs extend this idea by making the entire tensor network trainable via automatic differentiation, allowing end-to-end optimization of the compressed representation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.00130">Automatically Differentiable Nonlinear Tensor Networks ( ADNTNs )...</a></li>
<li><a href="https://www.emergentmind.com/topics/tree-tensor-networks-ttns">Tree Tensor Networks ( TTNs ): A Concise Overview</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-scale-entanglement-renormalization-ansatz-mera">MERA : Multi - scale Entanglement Renormalization Ansatz</a></li>

</ul>
</details>

**Tags**: `#tensor networks`, `#deep learning`, `#model compression`, `#automatic differentiation`

---

<a id="item-13"></a>
## [World Models Survey: Taxonomy, Methods, and Applications](https://arxiv.org/abs/2606.00133) ⭐️ 8.0/10

A new comprehensive survey introduces a multi-axis taxonomy for world models, covering architectures, methodologies, reasoning paradigms, and applications across reinforcement learning, robotics, and video generation. This survey unifies a fragmented field, providing a structured framework that can guide future research and accelerate progress toward artificial general intelligence. The taxonomy organizes world models along four dimensions: architecture, methodological family, reasoning strategy, and application domain, tracing evolution from PlaNet to Sora and Genie.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: World models are internal simulators that learn environment dynamics, enabling agents to predict, plan, and reason. They are central to AI research but have lacked a unified framework, making this survey a timely contribution.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00133">[2606.00133] World Models : A Comprehensive Survey of...</a></li>
<li><a href="https://github.com/GigaAI-research/General-World-Models-Survey">GitHub - GigaAI-research/General- World - Models - Survey · GitHub</a></li>

</ul>
</details>

**Tags**: `#world models`, `#survey`, `#reinforcement learning`, `#deep learning`, `#AI`

---

<a id="item-14"></a>
## [LLM Agent Tool-calling: Evaluation Sensitivity & RL Waste](https://arxiv.org/abs/2606.00135) ⭐️ 8.0/10

This paper systematically analyzes tool-calling in LLM agents, revealing that evaluation results are highly sensitive to minor implementation choices like random seed and system prompt, and identifies two sources of computational waste in RL training. These findings challenge the reliability of leaderboard rankings and offer practical techniques to accelerate RL-based tool-calling training, which is crucial for building efficient and reproducible LLM agents. The paper introduces two techniques that achieve substantial wall-clock speedup in RL-based tool-calling training without degrading performance, addressing waste from uninformative rollouts and costly policy updates.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: Tool-calling allows LLM agents to interact with external tools (e.g., APIs, databases) to extend their capabilities beyond parametric knowledge. Reinforcement learning (RL) is commonly used to train agents to use tools effectively, but the evaluation and training processes have been understudied.

<details><summary>References</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/infinite-tool-calling-trap-how-your-llm-agent-can-get-rajveer-gangwar-zketc">The Infinite Tool - Calling Trap: How Your LLM Agent Can Get Stuck in...</a></li>
<li><a href="https://www.ibm.com/think/tutorials/local-tool-calling-ollama-granite">Ollama tool calling | IBM</a></li>
<li><a href="https://blog.sentry.security/exploiting-tool-and-function-calling-in-llm-agents/">Exploiting Tool and Function Calling in LLM Agents</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#tool-calling`, `#reinforcement learning`, `#evaluation`, `#efficiency`

---

<a id="item-15"></a>
## [Proactive Lifecycle-Based Survey for GenAI Threat Detection](https://arxiv.org/abs/2606.00136) ⭐️ 8.0/10

This survey proposes a proactive lifecycle-based taxonomy for detecting emerging inauthentic narratives generated by AI, integrating machine learning and social science models. It addresses the critical challenge of adversarial synthetic content detection, shifting from reactive to proactive methods to enhance digital ecosystem resilience. The survey structures analysis around the C5 Interaction Model (Context, Causes, Content, Cycle of Amplification, Consequences) and reviews techniques like coordinated inauthentic behavior detection, epidemiological modeling, and agentic AI systems.

rss · arXiv - Machine Learning · Jun 2, 04:00

**Background**: Generative AI can produce convincing fake content at scale, making traditional reactive detection methods insufficient. Proactive detection aims to identify emerging threats before they cause harm, using lifecycle models to understand how narratives are created, seeded, and amplified.

**Tags**: `#Generative AI`, `#Adversarial Content Detection`, `#Digital Ecosystem Resilience`, `#Survey`, `#AI Safety`

---

<a id="item-16"></a>
## [SENSE: Semantic Embedding for Robust Speculative Decoding](https://arxiv.org/abs/2606.00021) ⭐️ 8.0/10

Researchers propose SENSE, a novel retrieval-based speculative decoding method that uses semantic embeddings and a soft-gated evaluation module to validate semantic equivalence, achieving up to 4.09 mean acceptance length and 3.26x speedup on LLaMA and Qwen models. This work addresses a key limitation of lexical dependencies in retrieval-based speculative decoding, making LLM inference more robust to surface-level variations and potentially accelerating deployment in latency-sensitive applications. SENSE anchors retrieval on the hidden states of the target model for robust semantic alignment, and introduces a soft-gated evaluation module that validates semantic equivalence rather than exact token matches. The paper also provides a unified benchmarking framework for component-level comparison.

rss · arXiv - NLP · Jun 2, 04:00

**Background**: Speculative decoding accelerates LLM inference by using a lightweight draft model to propose tokens that are verified in parallel by the target model. Retrieval-based speculative decoding (RSD) is a plug-and-play variant, but its performance suffers from rigid lexical dependencies in retrieval and verification. SENSE overcomes this by leveraging semantic embeddings from the target model's hidden states.

**Tags**: `#LLM inference`, `#speculative decoding`, `#retrieval`, `#semantic embedding`, `#NLP`

---

<a id="item-17"></a>
## [TrustLDM: Benchmarking Trustworthiness in Language Diffusion Models](https://arxiv.org/abs/2606.00023) ⭐️ 8.0/10

Researchers introduce TrustLDM, a comprehensive benchmark evaluating safety, privacy, and fairness of Language Diffusion Models (LDMs), revealing that their trustworthiness degrades when malicious post contexts are attached to masked responses. As LDMs gain prominence as alternatives to autoregressive models, understanding their trustworthiness is critical for safe deployment; this benchmark provides systematic evaluation and identifies vulnerabilities, guiding the development of more reliable LDMs. The benchmark covers multiple LDM architectures and static post contexts, and includes TrustLDM-Auto, an automatic evaluation framework that leverages decoding flexibility to identify vulnerable configurations. Results show that longer contexts do not necessarily induce stronger effects, and decoding order and generation length affect outcomes.

rss · arXiv - NLP · Jun 2, 04:00

**Background**: Language Diffusion Models (LDMs) are a new paradigm in language modeling inspired by image diffusion models, using any-order decoding strategies that enable fast generation but may introduce trustworthiness challenges. Unlike autoregressive models that generate tokens left-to-right, LDMs can fill in masked tokens in any order, which can be exploited by malicious post contexts.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@vickythevgn/large-language-diffusion-models-b4d0e6826057">Large Language Diffusion Models . Welcome to a new... | Medium</a></li>
<li><a href="https://arxiv.org/pdf/2508.10875">A Survey on Diffusion Language Models</a></li>
<li><a href="https://www.linkedin.com/pulse/dawn-large-language-diffusion-models-new-era-ai-driven-xy2le">The Dawn of Large Language Diffusion Models : A New Era in...</a></li>

</ul>
</details>

**Tags**: `#trustworthiness`, `#language diffusion models`, `#benchmark`, `#AI safety`, `#fairness`

---

<a id="item-18"></a>
## [ART: Run-Time KV Cache Pruning Boosts LLM Throughput 20%](https://arxiv.org/abs/2606.00024) ⭐️ 8.0/10

Researchers propose Attention Run-time Termination (ART), a lightweight mechanism that terminates unnecessary KV block accesses during LLM decoding, achieving 20% higher generation throughput in large batch sizes without sacrificing accuracy. ART directly addresses the memory bandwidth bottleneck in LLM inference, which is the primary constraint on throughput. Its orthogonality to existing methods means it can be easily combined with other optimizations, making it highly practical for real-world deployments. ART tracks accumulated attention outputs during kernel execution and stops fetching KV blocks once further contributions become negligible. It is orthogonal to key-based KV cache management methods and was validated on LongBench benchmarks.

rss · arXiv - NLP · Jun 2, 04:00

**Background**: LLM decoding is memory bandwidth-bound because the GPU must repeatedly read the entire KV cache from memory for each generated token, while compute units remain idle. Existing KV management methods typically prune keys before decoding but cannot efficiently incorporate values due to overhead. ART operates at run-time, dynamically skipping KV blocks that contribute little to the final attention output.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/plasmon_imp/if-memory-could-compute-would-we-still-need-gpus-4ccb">If Memory Could Compute, Would We Still Need... - DEV Community</a></li>
<li><a href="https://www.linkedin.com/pulse/memory-bandwidth-engineering-true-bottleneck-llm-gpu-benavides-85rhf">#29 Memory Bandwidth Engineering: The True Bottleneck in LLM ...</a></li>
<li><a href="https://medium.com/learnwithnk/decoding-real-time-llm-inference-a-guide-to-the-latency-vs-throughput-bottleneck-c1ad96442d50">Decoding Real-Time LLM Inference: A Guide to the Latency... | Medium</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#KV cache`, `#inference optimization`, `#attention mechanism`, `#memory bandwidth`

---

<a id="item-19"></a>
## [Multi-Domain Red Teaming Framework for Medical LLMs](https://arxiv.org/abs/2606.00027) ⭐️ 8.0/10

Researchers developed a multi-domain red teaming framework that evaluated 11 medical LLMs across 690 clinically grounded scenarios, revealing performance variance and safety-critical failures masked by aggregate accuracy. This framework addresses a critical gap in safety and fairness assessment for medical LLMs, with potential impact on clinical AI deployment by highlighting that worst-case failures are more clinically meaningful than mean accuracy. The evaluation covered nine domains and over 150 subcategories, using a seven-dimension rubric with LLM-assisted scoring and human-in-the-loop validation; equity-related tasks showed 10-20% error amplification with demographic modifications.

rss · arXiv - NLP · Jun 2, 04:00

**Background**: Large language models are increasingly used in healthcare, but existing benchmarks often fail to capture adversarial or ethically complex scenarios common in clinical practice. Red teaming is a structured approach to probe model vulnerabilities, and this work extends it to medical LLMs with a focus on safety, robustness, and fairness.

**Tags**: `#LLM safety`, `#medical AI`, `#red teaming`, `#fairness`, `#benchmarking`

---

<a id="item-20"></a>
## [Planktonzilla-17M: Largest Plankton Image Dataset Released](https://arxiv.org/abs/2606.00080) ⭐️ 8.0/10

Researchers introduced Planktonzilla-17M, a unified dataset of 17.4 million plankton images from 13 imaging systems, with standardized taxonomy and geo-environmental metadata, enabling robust species identification across instruments. This dataset addresses a key generalization problem in marine ecology, where existing models fail across different instruments and environments, and could significantly improve ocean health monitoring and climate change research. The dataset includes 3.74 million plankton images spanning 602 taxonomic classes, with 201 identified at species level. Supervised training on this dataset outperformed CLIP-style methods, and existing biological foundation models like BioCLIP performed poorly on plankton.

rss · arXiv - Computer Vision · Jun 2, 04:00

**Background**: Marine plankton are critical for aquatic food webs and global CO2 sequestration, but species identification is challenging due to diverse imaging systems and inconsistent labels. Previous datasets were isolated, limiting model generalization. Planktonzilla-17M consolidates public collections to overcome this.

**Tags**: `#multimodal learning`, `#marine ecology`, `#dataset`, `#computer vision`, `#climate science`

---

<a id="item-21"></a>
## [MIND: Diffusion Model with Explicit Manifold Geometry](https://arxiv.org/abs/2606.00094) ⭐️ 8.0/10

Researchers propose MIND, a diffusion model that explicitly models data manifold geometry by integrating discrete patch tokenization into continuous score functions, achieving state-of-the-art FID scores on ImageNet 256×256. This work bridges discrete tokenization and continuous diffusion, offering a fresh perspective on generative modeling that could improve image quality and efficiency, potentially influencing future research in generative AI. MIND introduces soft top-k aggregation for end-to-end differentiable training and dual-branch high-frequency embedding to address spectral bias. The base model achieves FID 22.73 without guidance, nearly halving the DiT-B/2 baseline's 43.47 FID.

rss · arXiv - Computer Vision · Jun 2, 04:00

**Background**: Diffusion models generate images by gradually denoising random noise, learning the score function of the data distribution. Data manifold refers to the low-dimensional structure underlying high-dimensional data; explicit modeling of its geometry is challenging. Discrete tokenization (e.g., VQ-VAE) quantizes patches into discrete codes, while continuous diffusion operates in continuous space.

**Tags**: `#diffusion models`, `#image generation`, `#manifold learning`, `#generative AI`, `#deep learning`

---

<a id="item-22"></a>
## [Zero-Shot Super-Resolution in Operator Learning: Theory](https://arxiv.org/abs/2606.00296) ⭐️ 8.0/10

This paper provides a systematic theoretical study of zero-shot super-resolution in operator learning, proving that it can be information-theoretically impossible even in simple settings and identifying Hölder smoothness as a sufficient condition. This work bridges the gap between empirical observations and theoretical understanding of zero-shot super-resolution, which is crucial for reliable deployment of neural operators in scientific computing and engineering applications. The paper shows impossibility even when input functions are available over the entire continuum and the ground truth is a simple rank-one linear operator, and derives generalization bounds under Hölder smoothness.

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**Background**: Neural operators learn mappings between function spaces and are used in physics simulations. Zero-shot super-resolution refers to the ability of a model trained on coarse grids to make accurate predictions on finer grids without retraining. This phenomenon has been observed empirically but lacked theoretical justification.

**Tags**: `#operator learning`, `#zero-shot super-resolution`, `#neural operators`, `#theoretical analysis`, `#generalization bounds`

---

<a id="item-23"></a>
## [Parameter-Free Group-Conditional Online Conformal Prediction](https://arxiv.org/abs/2606.00419) ⭐️ 8.0/10

A new parameter-free algorithm for group-conditional online conformal prediction is proposed, achieving the best group-conditional coverage guarantees under distribution shift without requiring manual tuning of learning rates. This work addresses a critical gap in online conformal prediction by simultaneously ensuring group-conditional coverage (important for fairness) and parameter-free operation (robust to unknown shifts), making uncertainty quantification more reliable and fair in dynamic environments. The algorithm unifies group-conditional coverage with parameter-free online learning, providing theoretical guarantees and empirical validation on synthetic and real-world data, with prediction intervals comparable to well-tuned group-conditional methods.

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**Background**: Online conformal prediction (OCP) provides uncertainty quantification for streaming data under distribution shift, but existing methods often sacrifice either group-conditional coverage (needed for fairness) or parameter-free implementation (needed for robustness). Parameter-free optimization adapts automatically without manual learning rate tuning, which is crucial when shifts are adversarial or unknown.

**Tags**: `#conformal prediction`, `#uncertainty quantification`, `#online learning`, `#fairness`, `#distribution shift`

---

<a id="item-24"></a>
## [FK-PINNs: Preconditioning Loss Landscape with Feynman-Kac Supervision](https://arxiv.org/abs/2606.00643) ⭐️ 8.0/10

This paper introduces FK-PINNs, which augment Physics-Informed Neural Networks (PINNs) with pointwise data-fidelity terms generated via Monte Carlo averages of the Feynman-Kac functional, acting as an operator-level preconditioner to improve the condition number of the loss landscape. The authors also provide non-asymptotic L^2 error bounds for FK-PINNs trained with gradient descent, and establish new pseudo-dimension bounds for derivatives of tanh networks. This work addresses a fundamental ill-conditioning issue in PINNs that often leads to slow convergence or failure, providing both theoretical guarantees and practical improvements. It is highly relevant for scientific computing and machine learning for PDEs, potentially enabling more reliable neural solvers for challenging problems like Schrödinger and committor equations. The preconditioning effect is shown to be independent of how the pointwise labels are obtained, and the Feynman-Kac representation is used to generate labels for a broad class of PDEs. Numerical experiments on Poisson, Schrödinger, mean exit time, and committor problems demonstrate that FK-PINNs succeed where standard PINNs fail.

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**Background**: Physics-Informed Neural Networks (PINNs) embed PDE residuals into the loss function to solve PDEs, but often suffer from ill-conditioned loss landscapes due to the differential operator. The Feynman-Kac formula provides a probabilistic representation of PDE solutions via stochastic processes, which can be used to generate supervised labels. Operator preconditioning is a technique to improve the conditioning of optimization problems by transforming the operator.

**Tags**: `#PINNs`, `#PDEs`, `#operator preconditioning`, `#Feynman-Kac`, `#scientific computing`

---

<a id="item-25"></a>
## [NFIL3 Protein Identified as Key Barrier in CAR T Therapy](https://www.sciencedaily.com/releases/2026/06/260602021641.htm) ⭐️ 8.0/10

Researchers have identified the NFIL3 protein as a primary cause of CAR T-cell exhaustion, and disabling it significantly improved the cells' durability and tumor control in animal models. This finding directly addresses a major limitation of CAR T-cell therapy—cell exhaustion—potentially leading to more effective and durable cancer treatments. The study was conducted in animal models, and disabling NFIL3 allowed CAR T cells to remain stronger for longer and control tumors more effectively.

rss · ScienceDaily Health · Jun 2, 14:54

**Background**: CAR T-cell therapy is a cancer immunotherapy where a patient's T cells are engineered to recognize and kill cancer cells. However, these cells often become exhausted over time, losing their effectiveness. NFIL3 is a transcription factor that regulates immune cell function.

**Tags**: `#cancer immunotherapy`, `#CAR T-cell therapy`, `#NFIL3`, `#immunology`, `#biomedical research`

---