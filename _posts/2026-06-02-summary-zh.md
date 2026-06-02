---
layout: default
title: "Horizon Summary: 2026-06-02 (ZH)"
date: 2026-06-02
lang: zh
---

> From 103 items, 25 important content pieces were selected

---

1. [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](#item-1) ⭐️ 8.0/10
2. [Godot 引擎：开源游戏引擎在 GitHub 上流行](#item-2) ⭐️ 8.0/10
3. [OpenBMB 发布 VoxCPM2：无分词器 TTS 模型](#item-3) ⭐️ 8.0/10
4. [为 MILP 决策引擎提出求解后鲁棒性层](#item-4) ⭐️ 8.0/10
5. [Consilium 协议：基于拜占庭容错的多模型 AI 协商](#item-5) ⭐️ 8.0/10
6. [多智能体知识库的审议策展协议](#item-6) ⭐️ 8.0/10
7. [延迟奖励归因提升多智能体强化学习在语言模型中的应用](#item-7) ⭐️ 8.0/10
8. [通用量子变压器实现精确推理](#item-8) ⭐️ 8.0/10
9. [Grokers：知识图谱的写入时智能架构](#item-9) ⭐️ 8.0/10
10. [BitsMoE：基于谱能量引导的 MoE 大模型比特分配方法](#item-10) ⭐️ 8.0/10
11. [LLM 情感效价轴与人类脑电对齐](#item-11) ⭐️ 8.0/10
12. [ADNTNs：通过可微张量网络实现深度神经网络指数级压缩](#item-12) ⭐️ 8.0/10
13. [世界模型综述：分类、方法与应用的统一框架](#item-13) ⭐️ 8.0/10
14. [LLM 智能体工具调用：评估敏感性与 RL 浪费](#item-14) ⭐️ 8.0/10
15. [生成式 AI 威胁检测的主动生命周期综述](#item-15) ⭐️ 8.0/10
16. [SENSE：基于语义嵌入的鲁棒推测解码](#item-16) ⭐️ 8.0/10
17. [TrustLDM：语言扩散模型可信度基准测试](#item-17) ⭐️ 8.0/10
18. [ART：运行时 KV 缓存剪枝将 LLM 吞吐量提升 20%](#item-18) ⭐️ 8.0/10
19. [医疗大语言模型的多领域红队测试框架](#item-19) ⭐️ 8.0/10
20. [Planktonzilla-17M：最大浮游生物图像数据集发布](#item-20) ⭐️ 8.0/10
21. [MIND：显式建模数据流形几何的扩散模型](#item-21) ⭐️ 8.0/10
22. [算子学习中的零样本超分辨率：理论基础](#item-22) ⭐️ 8.0/10
23. [无参数组条件在线共形预测](#item-23) ⭐️ 8.0/10
24. [FK-PINNs：用 Feynman-Kac 监督预条件损失景观](#item-24) ⭐️ 8.0/10
25. [NFIL3 蛋白被确定为 CAR T 疗法的主要障碍](#item-25) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软发布 MAI-Thinking-1 和 MAI-Code-1-Flash 大语言模型](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything) ⭐️ 8.0/10

微软宣布了两款新的大语言模型：MAI-Thinking-1，一个拥有 35B 活跃参数和 128K 上下文窗口的推理模型；以及 MAI-Code-1-Flash，一个专为 GitHub Copilot 构建的 5B 参数代码模型。这两个模型均使用干净、商业许可的数据从头训练，未从第三方模型进行蒸馏。 这些模型以较低的参数数量实现了高性能，可能降低推理成本并支持本地部署。MAI-Thinking-1 声称在盲测中优于 Sonnet 4.6，挑战了“更大模型总是更好”的观念。 MAI-Thinking-1 是一个稀疏混合专家模型，总参数约 1T，但仅 35B 活跃，目前仅对选定的早期合作伙伴开放。MAI-Code-1-Flash 正在向 Visual Studio Code 中的 GitHub Copilot 个人用户推出，两个模型都强调使用适当许可的数据进行训练。

rss · Simon Willison · Jun 2, 22:21

**背景**: 大语言模型（LLM）是在海量文本数据上训练的人工智能系统，能够生成类似人类的文本。参数数量通常与能力相关，但更大的模型运行成本高昂。微软的新模型旨在以更低成本提供有竞争力的性能，并使用干净数据来解决版权问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://microsoft.ai/news/introducing-mai-thinking-1/">Introducing MAI-Thinking-1 | Microsoft AI</a></li>
<li><a href="https://microsoft.ai/news/introducingmai-code-1-flash/">Introducing MAI - Code - 1 - Flash | Microsoft AI</a></li>
<li><a href="https://mashable.com/tech/microsoft-launches-new-mai-family-of-models-at-build">Microsoft launches new MAI family of AI models at Microsoft Build | Mashable</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Microsoft`, `#AI models`, `#reasoning`, `#code generation`

---

<a id="item-2"></a>
## [Godot 引擎：开源游戏引擎在 GitHub 上流行](https://github.com/godotengine/godot) ⭐️ 8.0/10

Godot 引擎，一款免费开源的 2D 和 3D 游戏引擎，因社区高度活跃而在 GitHub 上流行，但并未发布新版本或重大公告。 这凸显了开源游戏开发工具日益增长的兴趣，Godot 为独立开发者和工作室提供了 Unity 和 Unreal Engine 等专有引擎的可行替代方案。 Godot 采用宽松的 MIT 许可证，支持一键导出到桌面、移动、网页和主机平台，由社区驱动并得到 Godot 基金会的支持。

rss · GitHub Trending - Daily (All) · Jun 2, 23:29

**背景**: Godot 引擎最初由 Juan Linietsky 和 Ariel Manzur 内部开发，于 2014 年 2 月开源。它提供统一的 2D 和 3D 游戏开发界面，内置脚本语言（GDScript）和基于节点的场景系统。

**标签**: `#game engine`, `#open source`, `#2D`, `#3D`, `#cross-platform`

---

<a id="item-3"></a>
## [OpenBMB 发布 VoxCPM2：无分词器 TTS 模型](https://github.com/OpenBMB/VoxCPM) ⭐️ 8.0/10

OpenBMB 发布了 VoxCPM2，这是一个 20 亿参数的无分词器文本转语音模型，在超过 200 万小时的多语言语音数据上训练，支持 30 种语言、语音设计、可控语音克隆和 48kHz 音频输出。 VoxCPM2 通过消除分词器推进了开源 TTS，实现了更自然、更具表现力的语音合成，并支持仅凭文本描述进行创意语音设计，从而降低了语音内容创作的门槛。 该模型采用在连续潜在空间中运行的扩散自回归架构，基于 MiniCPM-4 骨干网络，可在 Hugging Face 和 ModelScope 上获取，并配有在线演示和文档。

rss · GitHub Trending - Daily (All) · Jun 2, 23:29

**背景**: 传统 TTS 系统使用离散音频令牌将文本转换为语音，这可能会丢失细微差别。像 VoxCPM2 这样的无分词器模型直接生成连续语音表示，保留了更多的自然度和表现力。OpenBMB 以开源大语言模型（如 MiniCPM）而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://voxcpm.net/">VoxCPM: Tokenizer - Free TTS & Zero-Shot Voice Cloning</a></li>
<li><a href="https://voxcpm.readthedocs.io/en/latest/models/architecture.html">Architecture - VoxCPM 2 .0 documentation</a></li>
<li><a href="https://explainx.ai/blog/voxcpm2-tokenizer-free-tts-multilingual-voice-cloning-2026">VoxCPM 2 : The 2B Parameter Tokenizer-Free TTS Model ... | explainx.ai</a></li>

</ul>
</details>

**标签**: `#TTS`, `#speech generation`, `#voice cloning`, `#multilingual`, `#open-source`

---

<a id="item-4"></a>
## [为 MILP 决策引擎提出求解后鲁棒性层](https://arxiv.org/abs/2606.00002) ⭐️ 8.0/10

arXiv 上的一篇立场论文（编号 2606.00002）提出了 MILP 决策引擎的求解后鲁棒性层概念，形式化了参数空间中的ε-近优可行邻域和决策空间中的解平滑性。 这解决了高风险系统优化流程中的一个关键空白——微小扰动可能使解失效或导致不连续跳变，并提议将鲁棒性作为决策引擎的一等输出。 该论文综合了敏感性分析、鲁棒优化、邻域搜索、对抗性测试和基于学习的增强等领域的见解，并呼吁建立认证内逼近、概率鲁棒性估计和对抗性鲁棒性边界。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 混合整数线性规划（MILP）是一种数学优化方法，用于从离散和连续变量集合中寻找最优解。求解 MILP 问题的决策引擎广泛应用于工业系统，但它们通常假设输入参数固定，忽略了现实世界中的扰动。鲁棒优化和随机规划在求解时处理不确定性，但不会在解计算后审计其鲁棒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00002">[2606.00002] Position Paper: Post - Solve Robustness in Decision...</a></li>
<li><a href="https://artificialintelligenceherald.com/posts/post-solve-robustness-gap-milp-2026">Post - Solve Robustness Gap in MILP Decision Engines - AI Herald</a></li>

</ul>
</details>

**标签**: `#MILP`, `#robust optimization`, `#decision engines`, `#perturbation analysis`

---

<a id="item-5"></a>
## [Consilium 协议：基于拜占庭容错的多模型 AI 协商](https://arxiv.org/abs/2606.00005) ⭐️ 8.0/10

Consilium 协议提出了一种基于拜占庭容错的多模型 AI 协商架构，将模型间的分歧视为认知信号而非错误。在 1478 次会话中，它表明认知角色（而非模型本身）决定了认知行为，并且 RLHF 训练会引入领域特定的盲点。 该工作表明，配备适当角色的廉价模型可以媲美前沿模型的输出，有望大幅降低 AI 系统成本。同时，它揭示了 RLHF 对齐训练带来的系统性偏见，对 AI 安全和对齐研究具有重要意义。 该协议采用了来自量化金融的样本内/样本外验证框架，以区分训练数据共识与经验性结论。完整实验的总成本仅为 217 美元，运行间可重复性平均标准差为±2.2%。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 拜占庭容错（BFT）是分布式计算中的一种共识机制，确保系统在存在故障或恶意节点时仍能可靠运行。Consilium 协议将 BFT 适配到多模型 AI 系统，其中每个模型作为一个节点，并拥有独立于底层模型权重的认知角色，该角色决定了其推理风格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00005">[2606.00005] Emergent Collaborative Deliberation in Multi - Model AI...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Byzantine_fault">Byzantine fault - Wikipedia</a></li>
<li><a href="https://pypi.org/project/consilium/">Multi - model deliberation CLI. 4 frontier LLMs debate with rotating...</a></li>

</ul>
</details>

**标签**: `#multi-model AI`, `#Byzantine Fault Tolerance`, `#epistemic synthesis`, `#RLHF`, `#alignment`

---

<a id="item-6"></a>
## [多智能体知识库的审议策展协议](https://arxiv.org/abs/2606.00007) ⭐️ 8.0/10

提出了一种新的多智能体知识库审议策展协议，结合了声誉加权投票、EigenTrust 放大和渐进式制裁，并通过 100 个智能体的基于智能体的模拟进行了评估。 该协议解决了多智能体 AI 系统中集体知识策展治理的关键挑战，在对抗条件下相比多数投票表现出更强的韧性，这对可信的 AI 协作至关重要。 该协议在压力下退化速度比多数投票慢约三倍，消融分析发现提交-揭示投票隐藏是最有影响力的组件（精度提升 8.2-8.6 个百分点）。渐进式制裁在模拟中未被使用，仍未经实证验证。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 多智能体系统涉及多个 AI 代理在共享知识生态中协作。像 Beta 声誉系统和 EigenTrust 这样的声誉系统有助于评估代理的可信度，而渐进式制裁则用于阻止不当行为。该协议将这些概念适配到无状态代理，解决了模型同质性和谄媚等挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://people.cs.vt.edu/~irchen/6204b/paper/Josang-BECC02-slide.pptx">The Beta Reputation System Jøsang and R. Ismail 15th Bled...</a></li>
<li><a href="https://en.wikipedia.org/wiki/EigenTrust">EigenTrust - Wikipedia</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10458-020-09465-8">Runtime revision of sanctions in normative multi-agent systems | Autonomous Agents and Multi-Agent Systems | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#knowledge curation`, `#AI governance`, `#reputation systems`, `#agent-based simulation`

---

<a id="item-7"></a>
## [延迟奖励归因提升多智能体强化学习在语言模型中的应用](https://arxiv.org/abs/2606.00017) ⭐️ 8.0/10

研究人员提出了一种带有资格门控的延迟逐步骤奖励归因方法，该管道仅在回合结束时计算奖励并将其回溯到原始步骤，从而实现了语言模型智能体在多智能体游戏中的稳定强化学习训练。在 NeurIPS 2025 的 MindGames Arena 基准测试中，一个使用该方法训练的 80 亿参数开源模型在正面交锋中匹配甚至超越了 GPT-5。 这项工作解决了语言模型在多智能体强化学习中的一个基本挑战：跨时间和智能体的结果纠缠。通过使较小的开源模型能够进行样本高效的训练，并与更大的专有系统竞争，它使先进的人工智能战略交互能力更加普及。 该管道使用 vLLM 的连续批处理进行异步轨迹生成、基于课程的对手采样和多层分层批次构建。资格门控将没有有效依赖信息的步骤排除在训练之外，确保只有相关步骤对学习有贡献。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 强化学习通常需要每步奖励，但在多智能体游戏中，动作的质量可能取决于未来的事件或其他玩家的动作，而这些在动作发生时是未知的。延迟逐步骤奖励归因仅在回合结束时计算奖励并将其回溯，而资格门控则过滤掉缺乏有效依赖信息的步骤。vLLM 的连续批处理提高了异步生成多个轨迹的推理吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.00017">MindGames Arena Generalization Track: In2AI Solution with Delayed ...</a></li>
<li><a href="https://papers.cool/arxiv/2606.00017">MindGames Arena Generalization Track: In2AI Solution with Delayed ...</a></li>
<li><a href="https://insujang.github.io/2024-01-07/llm-inference-continuous-batching-and-pagedattention/">LLM Inference: Continuous Batching and PagedAttention</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#multi-agent systems`, `#language models`, `#reward attribution`, `#strategic interaction`

---

<a id="item-8"></a>
## [通用量子变压器实现精确推理](https://arxiv.org/abs/2606.00045) ⭐️ 8.0/10

研究人员提出了通用量子变压器（UQT），这是一种量子原生架构，利用几何相位嵌入和 SU(2)波干涉在 5 量子比特系统上执行精确数学推理，完美学习了模运算和非阿贝尔代数。 这项工作表明，量子架构可以实现确定性泛化，无需经典神经网络所需的随机不稳定性和大量过参数化，可能彻底改变量子机器学习，并在近期量子硬件上实现精确人工智能。 UQT 绕过了经典自注意力的二次瓶颈，并对表示维度进行对数压缩，且已在 IBM 量子计算机上部署，证明了在 NISQ 硬件上的可行性。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 经典神经网络难以处理模运算等精确数学对称性，通常需要大量参数缩放并表现出延迟泛化（grokking）。UQT 利用叠加和干涉等量子特性自然编码离散逻辑规则，实现了超越 grokking 的所谓结晶化现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00045">[2606.00045] Universal Quantum Transformer</a></li>
<li><a href="https://medium.com/@quantaeon.ai/why-classical-ai-struggles-with-exact-logic-and-how-quantum-physics-fixes-it-28740a1c0986">Why Classical AI Struggles with Exact Logic (And How Quantum ...)</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#machine learning`, `#transformers`, `#algebraic reasoning`, `#arXiv`

---

<a id="item-9"></a>
## [Grokers：知识图谱的写入时智能架构](https://arxiv.org/abs/2606.00050) ⭐️ 8.0/10

Grokers 提出了一种面向类型化知识图谱的自底向上归纳架构，将理解工作转移到写入时，实现了接近 100% 的 KV-cache 命中率，并在查询时消除了语言模型调用。 该架构通过避免在查询时重复理解，可大幅降低知识密集型应用的计算成本，与每次查询都产生全部成本的 RAG 系统形成对比。 论文证明了三个形式化定理：用于 KV-cache 重用的字节恒等定理、用于知识库增长的累积单调性定理，以及用于正确遍历顺序的双遍历排序定理。参考实现已在开源 Qbix/Safebox/Safebots 栈中提供。

rss · arXiv - AI · Jun 2, 04:00

**背景**: 知识图谱将实体及其关系表示为类型化的节点和边。传统的 RAG 系统在查询时检索相关信息并输入语言模型，每次查询都产生理解成本。Grokers 反转了这一设计，在写入时一次性完成理解，并存储增强后的属性以供未来查询使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00050">[2606.00050] Grokers: Bottom-Up Inductive Comprehension and Write-Time Intelligence over Typed Knowledge Graphs</a></li>
<li><a href="https://arxiv.org/html/2606.00050">Grokers: Bottom-Up Inductive Comprehension and Write-Time...</a></li>

</ul>
</details>

**标签**: `#knowledge graphs`, `#AI architecture`, `#RAG`, `#KV-cache`, `#formal proofs`

---

<a id="item-10"></a>
## [BitsMoE：基于谱能量引导的 MoE 大模型比特分配方法](https://arxiv.org/abs/2606.00079) ⭐️ 8.0/10

BitsMoE 提出了一种新颖的基于谱能量引导的混合精度量化框架，用于混合专家（MoE）大语言模型，通过 SVD 分解和激活感知的比特分配实现高效内存压缩。在 Qwen3-30B-A3B-Base 上进行 2 比特量化时，BitsMoE 相比 GPTQ 将量化速度提升 12.3 倍，平均准确率提高 27.83 个百分点，解码速度提升 1.76 倍。 这项工作解决了 MoE 大模型部署中的关键内存瓶颈问题——尽管专家激活是稀疏的，但所有专家权重都必须常驻内存。通过实现极低比特量化且精度损失极小，BitsMoE 可以显著降低运行大型 MoE 模型的硬件需求，使其更易于在边缘和资源受限环境中部署。 BitsMoE 通过 SVD 将每个 MoE 层分解为共享基（不量化）和专家特定的谱因子（以不同比特宽度量化）。每个单元的比特宽度通过求解整数线性规划来确定，该规划在固定比特预算下最小化估计的重建损失，并由激活感知的重建代理引导。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 混合专家（MoE）是一种神经网络架构，使用多个专门的子网络（专家）和一个门控机制，每个输入只激活部分专家，从而减少计算量。然而，所有专家权重都必须加载到内存中，造成内存瓶颈。量化通过降低模型精度（例如从 16 比特降到 2 比特）来压缩内存，但均匀量化无法考虑不同专家和权重的重要性差异。混合精度量化为模型的不同部分分配不同的比特宽度，但现有方法缺乏为 MoE 结构确定比特分配的原则性方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tokenmix.ai/blog/moe-architecture-explained">MoE Architecture : Why Every AI Model Got... - TokenMix Blog</a></li>
<li><a href="https://jacobgil.github.io/deeplearning/tensor-decompositions-deep-learning">Accelerating Deep Neural Networks with Tensor Decompositions</a></li>

</ul>
</details>

**标签**: `#LLM quantization`, `#Mixture-of-Experts`, `#model compression`, `#efficient inference`, `#spectral analysis`

---

<a id="item-11"></a>
## [LLM 情感效价轴与人类脑电对齐](https://arxiv.org/abs/2606.00129) ⭐️ 8.0/10

研究人员仅用九个情感诱发句子从 LLM 中构建了一维效价方向（V 轴），并证明其与 123 名受试者观看情感视频时的人类脑电神经活动对齐。 这项工作连接了 LLM 与人类神经表征，表明模型和大脑共享情感效价结构，可能推动脑机接口和 AI 对齐研究。 V 轴通过零样本迁移到情感基准测试和跨 14 个 LLM 的模型一致性得到验证；36 个脑电解码器在未接触 V 轴的情况下自发发现了相同方向。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 情感效价指事件或刺激的内在吸引力（正性）或厌恶感（负性）。脑电图（EEG）测量大脑电活动。大型语言模型（LLM）如 GPT-4 从文本中学习丰富表征，近期研究探索其与人类神经活动的对齐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00129">[2606.00129] A Shared Valence Axis Across Modern LLMs and...</a></li>
<li><a href="https://arxiv.org/html/2606.00129">A Shared Valence Axis Across Modern LLMs and Human EEG: The...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#neural representation`, `#EEG`, `#emotional valence`, `#cognitive science`

---

<a id="item-12"></a>
## [ADNTNs：通过可微张量网络实现深度神经网络指数级压缩](https://arxiv.org/abs/2606.00130) ⭐️ 8.0/10

本文提出了自动可微非线性张量网络（ADNTNs），这是一类通过反向模式自动微分端到端训练紧凑核心张量的结构化权重生成器，在 AlexNet 和 VGG-16 上实现了每层 2000 倍到 77000 倍的压缩比，同时保持或提升了准确率。 ADNTNs 提供了一种数学结构清晰且硬件感知的方法，可大幅减小神经网络规模，有望在资源受限设备上部署大型模型而不会显著损失准确率。 本文重点研究了三种架构：树张量网络（TTNs）、带边界解缠器的增强 TTN（aTTNs）以及多尺度纠缠重整化拟设（MERA）；该方法还支持非线性激活、批处理和硬件感知执行调度。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 张量网络最初是在量子物理学中发展起来的数学结构，用于高效表示高维状态。在深度学习中，它们通过将权重矩阵分解为更小的张量来用于模型压缩。ADNTNs 通过使整个张量网络可通过自动微分训练，扩展了这一思想，从而实现了压缩表示的端到端优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.00130">Automatically Differentiable Nonlinear Tensor Networks ( ADNTNs )...</a></li>
<li><a href="https://www.emergentmind.com/topics/tree-tensor-networks-ttns">Tree Tensor Networks ( TTNs ): A Concise Overview</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-scale-entanglement-renormalization-ansatz-mera">MERA : Multi - scale Entanglement Renormalization Ansatz</a></li>

</ul>
</details>

**标签**: `#tensor networks`, `#deep learning`, `#model compression`, `#automatic differentiation`

---

<a id="item-13"></a>
## [世界模型综述：分类、方法与应用的统一框架](https://arxiv.org/abs/2606.00133) ⭐️ 8.0/10

一项新的全面综述提出了世界模型的多轴分类法，涵盖架构、方法论、推理范式以及在强化学习、机器人和视频生成等领域的应用。 该综述统一了碎片化的研究领域，提供了一个结构化框架，可指导未来研究并加速迈向通用人工智能的进程。 该分类法从架构、方法论家族、推理策略和应用领域四个维度组织世界模型，追溯了从 PlaNet 到 Sora 和 Genie 的演变过程。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 世界模型是学习环境动态的内部模拟器，使智能体能够预测、规划和推理。它们是 AI 研究的核心，但一直缺乏统一框架，因此本综述是一项及时的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.00133">[2606.00133] World Models : A Comprehensive Survey of...</a></li>
<li><a href="https://github.com/GigaAI-research/General-World-Models-Survey">GitHub - GigaAI-research/General- World - Models - Survey · GitHub</a></li>

</ul>
</details>

**标签**: `#world models`, `#survey`, `#reinforcement learning`, `#deep learning`, `#AI`

---

<a id="item-14"></a>
## [LLM 智能体工具调用：评估敏感性与 RL 浪费](https://arxiv.org/abs/2606.00135) ⭐️ 8.0/10

本文系统分析了 LLM 智能体中的工具调用，揭示评估结果对随机种子、系统提示等微小实现选择高度敏感，并识别出 RL 训练中两个计算浪费来源。 这些发现挑战了排行榜排名的可靠性，并提供了加速基于 RL 的工具调用训练的实用技术，对构建高效且可复现的 LLM 智能体至关重要。 本文引入了两种技术，在不降低性能的情况下显著加速基于 RL 的工具调用训练，解决了无信息 rollout 和高成本策略更新的浪费问题。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 工具调用允许 LLM 智能体与外部工具（如 API、数据库）交互，扩展其超越参数知识的能力。强化学习（RL）常用于训练智能体有效使用工具，但评估和训练过程此前研究不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/infinite-tool-calling-trap-how-your-llm-agent-can-get-rajveer-gangwar-zketc">The Infinite Tool - Calling Trap: How Your LLM Agent Can Get Stuck in...</a></li>
<li><a href="https://www.ibm.com/think/tutorials/local-tool-calling-ollama-granite">Ollama tool calling | IBM</a></li>
<li><a href="https://blog.sentry.security/exploiting-tool-and-function-calling-in-llm-agents/">Exploiting Tool and Function Calling in LLM Agents</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#tool-calling`, `#reinforcement learning`, `#evaluation`, `#efficiency`

---

<a id="item-15"></a>
## [生成式 AI 威胁检测的主动生命周期综述](https://arxiv.org/abs/2606.00136) ⭐️ 8.0/10

该综述提出了一种基于生命周期的主动分类法，用于检测由 AI 生成的新兴虚假叙事，整合了机器学习和社会科学模型。 它解决了对抗性合成内容检测的关键挑战，从被动方法转向主动方法，以增强数字生态系统的韧性。 该综述围绕 C5 交互模型（背景、原因、内容、放大循环、后果）构建分析，并回顾了协调不真实行为检测、流行病学建模和自主 AI 系统等技术。

rss · arXiv - Machine Learning · Jun 2, 04:00

**背景**: 生成式 AI 可以大规模生成令人信服的虚假内容，使得传统的被动检测方法不足。主动检测旨在在威胁造成危害之前识别它们，利用生命周期模型理解叙事如何被创建、播种和放大。

**标签**: `#Generative AI`, `#Adversarial Content Detection`, `#Digital Ecosystem Resilience`, `#Survey`, `#AI Safety`

---

<a id="item-16"></a>
## [SENSE：基于语义嵌入的鲁棒推测解码](https://arxiv.org/abs/2606.00021) ⭐️ 8.0/10

研究人员提出 SENSE，一种新颖的基于检索的推测解码方法，利用语义嵌入和软门控评估模块验证语义等价性，在 LLaMA 和 Qwen 模型上实现了高达 4.09 的平均接受长度和 3.26 倍加速。 这项工作解决了基于检索的推测解码中词汇依赖的关键限制，使 LLM 推理对表面变化更加鲁棒，并可能加速在延迟敏感应用中的部署。 SENSE 将检索锚定在目标模型的隐藏状态上以实现鲁棒的语义对齐，并引入软门控评估模块来验证语义等价性而非精确令牌匹配。论文还提供了一个统一的基准测试框架，用于组件级比较。

rss · arXiv - NLP · Jun 2, 04:00

**背景**: 推测解码通过使用轻量级草稿模型提出令牌，并由目标模型并行验证，从而加速 LLM 推理。基于检索的推测解码（RSD）是一种即插即用的变体，但其性能因检索和验证中的刚性词汇依赖而受损。SENSE 通过利用目标模型隐藏状态的语义嵌入来克服这一问题。

**标签**: `#LLM inference`, `#speculative decoding`, `#retrieval`, `#semantic embedding`, `#NLP`

---

<a id="item-17"></a>
## [TrustLDM：语言扩散模型可信度基准测试](https://arxiv.org/abs/2606.00023) ⭐️ 8.0/10

研究人员提出了 TrustLDM，这是一个全面评估语言扩散模型（LDM）安全性、隐私性和公平性的基准，揭示了当恶意后上下文附加到掩码响应时，其可信度会下降。 随着 LDM 作为自回归模型替代方案日益突出，理解其可信度对于安全部署至关重要；该基准提供了系统评估并识别了漏洞，指导更可靠的 LDM 的开发。 该基准涵盖多种 LDM 架构和静态后上下文，并包含 TrustLDM-Auto，这是一个利用解码灵活性自动识别易受攻击配置的评估框架。结果表明，更长的上下文不一定产生更强的影响，解码顺序和生成长度会影响结果。

rss · arXiv - NLP · Jun 2, 04:00

**背景**: 语言扩散模型（LDM）是受图像扩散模型启发的一种新的语言建模范式，采用任意顺序解码策略，能够实现快速生成，但可能带来可信度挑战。与从左到右生成 token 的自回归模型不同，LDM 可以按任意顺序填充掩码 token，这可能会被恶意后上下文利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@vickythevgn/large-language-diffusion-models-b4d0e6826057">Large Language Diffusion Models . Welcome to a new... | Medium</a></li>
<li><a href="https://arxiv.org/pdf/2508.10875">A Survey on Diffusion Language Models</a></li>
<li><a href="https://www.linkedin.com/pulse/dawn-large-language-diffusion-models-new-era-ai-driven-xy2le">The Dawn of Large Language Diffusion Models : A New Era in...</a></li>

</ul>
</details>

**标签**: `#trustworthiness`, `#language diffusion models`, `#benchmark`, `#AI safety`, `#fairness`

---

<a id="item-18"></a>
## [ART：运行时 KV 缓存剪枝将 LLM 吞吐量提升 20%](https://arxiv.org/abs/2606.00024) ⭐️ 8.0/10

研究人员提出注意力运行时终止（ART）机制，在 LLM 解码过程中终止不必要的 KV 块访问，在大批量下实现 20%的生成吞吐量提升，且不牺牲准确性。 ART 直接解决了 LLM 推理中的内存带宽瓶颈，这是吞吐量的主要限制因素。它与现有方法的正交性意味着可以轻松与其他优化结合，使其在实际部署中非常实用。 ART 在内核执行期间跟踪累积的注意力输出，一旦后续贡献可忽略就停止获取 KV 块。它与基于键的 KV 缓存管理方法正交，并在 LongBench 基准上得到验证。

rss · arXiv - NLP · Jun 2, 04:00

**背景**: LLM 解码受限于内存带宽，因为 GPU 必须为每个生成的令牌重复从内存中读取整个 KV 缓存，而计算单元处于空闲状态。现有的 KV 管理方法通常在解码前剪枝键，但由于开销无法有效纳入值。ART 在运行时操作，动态跳过对最终注意力输出贡献很小的 KV 块。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/plasmon_imp/if-memory-could-compute-would-we-still-need-gpus-4ccb">If Memory Could Compute, Would We Still Need... - DEV Community</a></li>
<li><a href="https://www.linkedin.com/pulse/memory-bandwidth-engineering-true-bottleneck-llm-gpu-benavides-85rhf">#29 Memory Bandwidth Engineering: The True Bottleneck in LLM ...</a></li>
<li><a href="https://medium.com/learnwithnk/decoding-real-time-llm-inference-a-guide-to-the-latency-vs-throughput-bottleneck-c1ad96442d50">Decoding Real-Time LLM Inference: A Guide to the Latency... | Medium</a></li>

</ul>
</details>

**标签**: `#LLM`, `#KV cache`, `#inference optimization`, `#attention mechanism`, `#memory bandwidth`

---

<a id="item-19"></a>
## [医疗大语言模型的多领域红队测试框架](https://arxiv.org/abs/2606.00027) ⭐️ 8.0/10

研究人员开发了一个多领域红队测试框架，在 690 个临床场景中评估了 11 个医疗大语言模型，揭示了被平均准确率掩盖的性能差异和安全关键性失败。 该框架填补了医疗大语言模型安全性和公平性评估的关键空白，通过强调最坏情况失败比平均准确率更具临床意义，可能影响临床 AI 部署。 评估涵盖九个领域和 150 多个子类别，使用七维度评分标准，结合大语言模型辅助评分和人工验证；公平性相关任务在人口统计信息修改后错误率放大 10-20%。

rss · arXiv - NLP · Jun 2, 04:00

**背景**: 大语言模型在医疗领域的应用日益增多，但现有基准测试往往无法捕捉临床实践中常见的对抗性或伦理复杂场景。红队测试是一种系统探测模型漏洞的方法，本研究将其扩展到医疗大语言模型，重点关注安全性、鲁棒性和公平性。

**标签**: `#LLM safety`, `#medical AI`, `#red teaming`, `#fairness`, `#benchmarking`

---

<a id="item-20"></a>
## [Planktonzilla-17M：最大浮游生物图像数据集发布](https://arxiv.org/abs/2606.00080) ⭐️ 8.0/10

研究人员发布了 Planktonzilla-17M，这是一个统一的数据集，包含来自 13 个成像系统的 1740 万张浮游生物图像，具有标准化的分类学和地理环境元数据，能够跨仪器进行稳健的物种识别。 该数据集解决了海洋生态学中的一个关键泛化问题，即现有模型在不同仪器和环境中的失效，可能显著改善海洋健康监测和气候变化研究。 该数据集包含 374 万张浮游生物图像，涵盖 602 个分类类别，其中 201 个已鉴定到物种级别。在该数据集上的监督训练优于 CLIP 风格方法，而现有的生物基础模型如 BioCLIP 在浮游生物上表现不佳。

rss · arXiv - Computer Vision · Jun 2, 04:00

**背景**: 海洋浮游生物对水生食物网和全球二氧化碳封存至关重要，但由于成像系统多样和标签不一致，物种识别具有挑战性。以往的数据集相互孤立，限制了模型的泛化能力。Planktonzilla-17M 整合了公开数据集以克服这一问题。

**标签**: `#multimodal learning`, `#marine ecology`, `#dataset`, `#computer vision`, `#climate science`

---

<a id="item-21"></a>
## [MIND：显式建模数据流形几何的扩散模型](https://arxiv.org/abs/2606.00094) ⭐️ 8.0/10

研究人员提出 MIND，一种通过将离散补丁标记化集成到连续得分函数中来显式建模数据流形几何的扩散模型，在 ImageNet 256×256 上实现了最先进的 FID 分数。 这项工作弥合了离散标记化和连续扩散之间的鸿沟，为生成建模提供了新视角，可能提升图像质量和效率，并影响生成式 AI 的未来研究。 MIND 引入了软 top-k 聚合以实现端到端可微训练，以及双分支高频嵌入来解决频谱偏差。基础模型在无引导下达到 FID 22.73，几乎将 DiT-B/2 基线的 43.47 FID 减半。

rss · arXiv - Computer Vision · Jun 2, 04:00

**背景**: 扩散模型通过逐步去噪随机噪声来生成图像，学习数据分布的得分函数。数据流形是指高维数据背后的低维结构；显式建模其几何形状具有挑战性。离散标记化（如 VQ-VAE）将补丁量化为离散码，而连续扩散在连续空间中运行。

**标签**: `#diffusion models`, `#image generation`, `#manifold learning`, `#generative AI`, `#deep learning`

---

<a id="item-22"></a>
## [算子学习中的零样本超分辨率：理论基础](https://arxiv.org/abs/2606.00296) ⭐️ 8.0/10

本文对算子学习中的零样本超分辨率进行了系统的理论研究，证明了即使在简单设置下，零样本超分辨率在信息论上也可能是不可能的，并确定了 Hölder 光滑性是一个充分条件。 这项工作弥合了零样本超分辨率经验观察与理论理解之间的差距，对于在科学计算和工程应用中可靠部署神经算子至关重要。 论文表明，即使输入函数在整个连续域上可用且真实函数是简单的秩一线性算子，零样本超分辨率也不可能，并在 Hölder 光滑性下推导了泛化界。

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**背景**: 神经算子学习函数空间之间的映射，用于物理模拟。零样本超分辨率是指模型在粗网格上训练后，无需重新训练就能在更细网格上做出准确预测的能力。这一现象已被经验观察到，但缺乏理论依据。

**标签**: `#operator learning`, `#zero-shot super-resolution`, `#neural operators`, `#theoretical analysis`, `#generalization bounds`

---

<a id="item-23"></a>
## [无参数组条件在线共形预测](https://arxiv.org/abs/2606.00419) ⭐️ 8.0/10

提出了一种新的无参数组条件在线共形预测算法，在分布漂移下无需手动调整学习率即可实现最佳组条件覆盖保证。 该工作填补了在线共形预测中的一个关键空白，同时保证了组条件覆盖（对公平性重要）和无参数操作（对未知漂移鲁棒），使动态环境中的不确定性量化更加可靠和公平。 该算法将组条件覆盖与无参数在线学习统一起来，在合成和真实数据上提供了理论保证和实证验证，预测区间大小与精心调优的组条件方法相当。

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**背景**: 在线共形预测（OCP）为分布漂移下的流式数据提供不确定性量化，但现有方法常常牺牲组条件覆盖（公平性所需）或无参数实现（鲁棒性所需）。无参数优化无需手动调整学习率即可自动适应，这在漂移具有对抗性或未知时至关重要。

**标签**: `#conformal prediction`, `#uncertainty quantification`, `#online learning`, `#fairness`, `#distribution shift`

---

<a id="item-24"></a>
## [FK-PINNs：用 Feynman-Kac 监督预条件损失景观](https://arxiv.org/abs/2606.00643) ⭐️ 8.0/10

本文提出了 FK-PINNs，通过蒙特卡洛平均 Feynman-Kac 泛函生成逐点数据保真项，作为算子级预条件子改善损失景观的条件数。作者还给出了梯度下降训练的 FK-PINNs 的非渐近 L^2 误差界，并建立了 tanh 网络导数的新伪维数界。 这项工作解决了 PINNs 中导致收敛缓慢或失败的基本病态问题，提供了理论保证和实际改进。它对科学计算和偏微分方程的机器学习具有重要意义，可能为薛定谔方程和 committor 问题等挑战性任务提供更可靠的神经求解器。 预条件效果与逐点标签的获取方式无关，Feynman-Kac 表示用于为一大类 PDE 生成标签。在泊松方程、薛定谔方程、平均退出时间和 committor 问题上的数值实验表明，FK-PINNs 在标准 PINNs 失败的情况下仍能成功。

rss · arXiv - Data Science & Statistics · Jun 2, 04:00

**背景**: 物理信息神经网络（PINNs）将 PDE 残差嵌入损失函数以求解 PDE，但常因微分算子导致损失景观病态。Feynman-Kac 公式通过随机过程提供 PDE 解的概率表示，可用于生成监督标签。算子预条件是一种通过变换算子改善优化问题条件数的技术。

**标签**: `#PINNs`, `#PDEs`, `#operator preconditioning`, `#Feynman-Kac`, `#scientific computing`

---

<a id="item-25"></a>
## [NFIL3 蛋白被确定为 CAR T 疗法的主要障碍](https://www.sciencedaily.com/releases/2026/06/260602021641.htm) ⭐️ 8.0/10

研究人员发现 NFIL3 蛋白是 CAR T 细胞耗竭的主要原因，禁用该蛋白后，细胞在动物模型中的持久性和肿瘤控制能力显著提高。 这一发现直接解决了 CAR T 细胞疗法的主要限制——细胞耗竭，有望带来更有效、更持久的癌症治疗方法。 该研究在动物模型中进行，禁用 NFIL3 后，CAR T 细胞能保持更长时间的功能，并更有效地控制肿瘤。

rss · ScienceDaily Health · Jun 2, 14:54

**背景**: CAR T 细胞疗法是一种癌症免疫疗法，通过改造患者自身的 T 细胞来识别并杀死癌细胞。然而，这些细胞往往会随时间耗竭，失去效力。NFIL3 是一种调节免疫细胞功能的转录因子。

**标签**: `#cancer immunotherapy`, `#CAR T-cell therapy`, `#NFIL3`, `#immunology`, `#biomedical research`

---