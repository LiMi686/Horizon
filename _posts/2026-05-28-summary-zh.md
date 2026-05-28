---
layout: default
title: "Horizon Summary: 2026-05-28 (ZH)"
date: 2026-05-28
lang: zh
---

> From 103 items, 33 important content pieces were selected

---

1. [Anthropic 完成 650 亿美元 H 轮融资，估值 9650 亿美元](#item-1) ⭐️ 9.0/10
2. [vLLM：高吞吐量 LLM 推理引擎](#item-2) ⭐️ 9.0/10
3. [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](#item-3) ⭐️ 8.0/10
4. [用 Postgres 实现持久化工作流引擎](#item-4) ⭐️ 8.0/10
5. [SQLite 新增 AGENTS.md 禁止 AI 生成代码](#item-5) ⭐️ 8.0/10
6. [面向 AI 代理的开源网络安全技能库](#item-6) ⭐️ 8.0/10
7. [哈佛开源机器学习系统工程书籍](#item-7) ⭐️ 8.0/10
8. [NVIDIA Megatron Bridge 实现与 Hugging Face 的互操作](#item-8) ⭐️ 8.0/10
9. [Soro：基于 Gemma 3 的塔吉克语专用大语言模型](#item-9) ⭐️ 8.0/10
10. [DynaSchedBench：校准的动态调度基准](#item-10) ⭐️ 8.0/10
11. [LLM 从根本上无法进行因果发现；A-CBO 提供出路](#item-11) ⭐️ 8.0/10
12. [RULER：新指标检测机器遗忘中的残留信息](#item-12) ⭐️ 8.0/10
13. [LaneRoPE：大语言模型的协作并行推理方法](#item-13) ⭐️ 8.0/10
14. [Agyn：面向可扩展 AI 代理的开源平台](#item-14) ⭐️ 8.0/10
15. [综述：MoE 应对多模态学习挑战](#item-15) ⭐️ 8.0/10
16. [液态神经网络在效率和鲁棒性上超越 LSTM](#item-16) ⭐️ 8.0/10
17. [LCO：基于 LLM 的约束优化实现更安全的智能体](#item-17) ⭐️ 8.0/10
18. [OralAgent：首个交互式牙科影像分析 AI 智能体](#item-18) ⭐️ 8.0/10
19. [自对齐方法弥合低资源语音模型的稳定性-表现力鸿沟](#item-19) ⭐️ 8.0/10
20. [FLUID 高效将自回归大语言模型适配为扩散模型](#item-20) ⭐️ 8.0/10
21. [EvoSpec：投机解码的实时自适应方法](#item-21) ⭐️ 8.0/10
22. [表示条件扩散模型提升合成数据质量](#item-22) ⭐️ 8.0/10
23. [What-If World：视频世界模型的因果基准](#item-23) ⭐️ 8.0/10
24. [重尾结果的因果推断](#item-24) ⭐️ 8.0/10
25. [新协议为因果边附加不可能性证书](#item-25) ⭐️ 8.0/10
26. [噪声异质性核度量的高效推断](#item-26) ⭐️ 8.0/10
27. [利用几何特征检测多轮欺骗](#item-27) ⭐️ 8.0/10
28. [GRASP：微调中无监督去除虚假相关性](#item-28) ⭐️ 8.0/10
29. [软专家：面向不确定性感知的 LLM 后训练的α-Rényi 集成方法](#item-29) ⭐️ 8.0/10
30. [新提取工艺有望实现更便宜、更环保的锂生产](#item-30) ⭐️ 8.0/10
31. [阻断 GPNMB 蛋白或能阻止帕金森病扩散](#item-31) ⭐️ 8.0/10
32. [脑部扫描挑战长新冠炎症理论](#item-32) ⭐️ 8.0/10
33. [隐藏的肠脑回路触发蛋白质渴望](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 完成 650 亿美元 H 轮融资，估值 9650 亿美元](https://www.anthropic.com/news/series-h) ⭐️ 9.0/10

Anthropic 宣布完成 650 亿美元的 H 轮融资，投后估值达 9650 亿美元，在收入和估值上均超越 OpenAI。 这轮融资标志着 AI 初创公司的历史性里程碑，凸显了 Anthropic 的主导地位以及 AI 行业资本密集度的加速提升。 Anthropic 自称其年化运行率收入本月早些时候达到 470 亿美元，高于 2026 年 4 月的 300 亿美元，反映出企业客户的快速采用。

hackernews · meetpateltech · May 28, 18:09 · [社区讨论](https://news.ycombinator.com/item?id=48313048)

**背景**: 年化运行率收入是将当前月收入外推至全年的一种指标，常被快速增长的私营公司用来展示增长轨迹。Anthropic 的估值现已接近 1 万亿美元，这是私营 AI 公司此前从未达到的里程碑。

**社区讨论**: 评论者注意到 Anthropic 在收入和估值上超越 OpenAI，有人质疑年化运行率指标，也有人惊叹于接近万亿美元的私人估值。还有讨论涉及股票市场对于如此大型私营公司角色的变化。

**标签**: `#AI`, `#funding`, `#valuation`, `#Anthropic`, `#startups`

---

<a id="item-2"></a>
## [vLLM：高吞吐量 LLM 推理引擎](https://github.com/vllm-project/vllm) ⭐️ 9.0/10

vLLM 是一个开源库，用于大型语言模型的高吞吐量和内存高效的推理与服务，最初由加州大学伯克利分校的 Sky Computing Lab 开发。它引入了 PagedAttention，一种用于 Transformer 键值缓存的新型内存管理技术。 vLLM 已成为 AI 生态系统中的关键基础设施组件，能够以最先进的服务吞吐量实现大型模型的成本效益部署。其广泛采用和超过 2000 名贡献者的活跃社区使其成为 LLM 服务的开创性项目。 vLLM 支持来自 Hugging Face 的 200 多种模型架构，包括仅解码器、混合专家、多模态和嵌入模型。它具有连续批处理、分块预填充、前缀缓存、量化（FP8、INT4 等）以及 FlashAttention 等优化内核。

rss · GitHub Trending - Python · May 28, 23:09

**背景**: 大型语言模型在推理时需要大量内存和计算，尤其是随着序列长度增长的键值缓存。传统的注意力机制将 KV 缓存存储在连续内存中，导致碎片化和浪费。PagedAttention 受虚拟内存分页启发，将 KV 缓存划分为固定大小的页面，并使用间接表实现高效的内存分配和重用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/VLLM">vLLM - Wikipedia</a></li>
<li><a href="https://github.com/vllm-project/vllm">GitHub - vllm-project/vllm: A high-throughput and memory-efficient ...</a></li>
<li><a href="https://vllm.ai/">vLLM</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#serving`, `#open-source`, `#AI infrastructure`

---

<a id="item-3"></a>
## [Anthropic 发布 Claude Opus 4.8，预告 Mythos 模型](https://www.anthropic.com/news/claude-opus-4-8) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 4.8，相比 Opus 4.7 有适度改进，包括更好的对齐能力，并在网页界面中新增了关闭自适应思考的开关。该公司还宣布了 Project Glasswing 项目，并预览了更强大的 Claude Mythos 模型，用于网络安全工作。 此次发布表明 Anthropic 在持续渐进改进前沿模型，同时暗示 Mythos 将带来重大飞跃。关闭自适应思考的功能解决了用户对输出质量不稳定的抱怨。 据报道，Opus 4.8 允许代码缺陷未被注意地通过的可能性比 Opus 4.7 低四倍，失调行为率也大幅降低。Claude Mythos 预览版目前仅通过 Project Glasswing 向特定组织提供，预计数周内全面发布。

hackernews · craigmart · May 28, 16:49 · [社区讨论](https://news.ycombinator.com/item?id=48311647)

**背景**: Claude Opus 是 Anthropic 最强大的模型系列，版本号如 4.5、4.6、4.7 和现在的 4.8 表示渐进式更新。Project Glasswing 是一项利用先进 AI 模型保护关键开源软件的倡议。自适应思考是一种动态调整模型推理深度的功能，部分用户认为其不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/technology/anthropics-claude-opus-4-8-is-here-with-3x-cheaper-fast-mode-and-near-mythos-level-alignment">Anthropic's Claude Opus 4.8 is here with 3X cheaper fast mode and near-Mythos level alignment | VentureBeat</a></li>
<li><a href="https://thenextweb.com/news/anthropics-claude-opus-4-8-is-its-most-honest-ai-model-yet-and-mythos-is-coming-in-weeks">Anthropic’s Claude Opus 4.8 is its most honest AI model yet, and Mythos is coming in weeks</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户赞赏适度的改进和关闭自适应思考的功能，而另一些用户则指出更新的渐进性质并对版本命名模式提出质疑。人们对 Mythos 感到兴奋，但也对其有限可用性和安全要求表示担忧。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Frontier Models`

---

<a id="item-4"></a>
## [用 Postgres 实现持久化工作流引擎](https://www.dbos.dev/blog/postgres-is-all-you-need-for-durable-execution) ⭐️ 8.0/10

一篇博客文章认为 PostgreSQL 可以作为持久化工作流引擎，通过集中数据来降低系统复杂性。社区提到了相关项目，如 Armin Ronacher 的“absurd”和 DBOS，它们都在 Postgres 上实现了持久化工作流。 这种方法通过消除独立工作流引擎和数据存储的需求，简化了后端架构，降低了运维开销。它可能使已经使用 Postgres 的团队更容易采用持久化工作流，从而可能改变行业实践。 文章建议利用 Postgres 的事务、触发器和 LISTEN/NOTIFY 等特性来编排工作流。但社区评论指出，扩展到 TB 级数据时可能需要迁移到专用系统。

hackernews · KraftyOne · May 28, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48313530)

**背景**: 持久化工作流引擎通过持久化状态和重试步骤，确保长时间运行的过程即使在故障后也能可靠完成。传统上，这类引擎（如 Temporal、Azure Durable Functions）是独立的系统，增加了复杂性。使用 Postgres 作为唯一引擎可以集中状态和逻辑，简化技术栈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/my-favorite-technologies-implementing-durable-marian-veteanu-oslqe">My Favorite Technologies for Implementing Durable Workflows ...</a></li>
<li><a href="https://github.com/durable-workflow/workflow">GitHub - durable-workflow/workflow: Durable workflow engine ...</a></li>
<li><a href="https://dev.to/mahdi0shamlou/mahdi-shamlou-durable-workflow-engines-comparison-temporal-dbos-transact-prefect-custom-3a6a">Mahdi Shamlou | Durable Workflow Engines Comparison ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同使用 Postgres 集中数据的好处，但提出了扩展到大数据量时的担忧。一些人提到了现有的实现如“absurd”和 DBOS，而另一些人则将基于 Postgres 的方法与 Temporal 进行比较，指出了在负载大小限制和复杂性方面的权衡。

**标签**: `#PostgreSQL`, `#durable workflows`, `#software architecture`, `#backend development`

---

<a id="item-5"></a>
## [SQLite 新增 AGENTS.md 禁止 AI 生成代码](https://simonwillison.net/2026/May/27/sqlite-agents/#atom-everything) ⭐️ 8.0/10

SQLite 在其仓库中新增了 AGENTS.md 文件，明确表示不接受代理（AI 生成）代码贡献，同时欢迎人类提交的 bug 报告和概念验证补丁。该项目还从政策中删除了“目前”一词以强化立场。 这是首个正式制定禁止 AI 生成代码政策的主要开源项目之一，为项目如何管理大量低质量 AI 贡献树立了先例。它凸显了 AI 编码代理与人类维护代码库之间日益紧张的关系。 AGENTS.md 文件要求所有贡献必须置于公共领域，并声明不接受来自代理的拉取请求，但人类开发者可以审查简洁的补丁作为概念验证。此外，SQLite 论坛被 AI 生成的 bug 报告淹没，促使创建了单独的 Bug 论坛。

rss · Simon Willison · May 27, 23:44

**背景**: SQLite 是一个广泛使用的嵌入式 SQL 数据库引擎，用 C 语言编写，其源代码属于公共领域。最近，AI 编码代理（如由 LLM 驱动的代理）开始自动生成并向开源项目提交代码贡献，这些贡献质量参差不齐，且缺乏适当的法律声明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/sqlite/sqlite/blob/master/AGENTS.md">sqlite/AGENTS.md at master - GitHub</a></li>
<li><a href="https://simonwillison.net/2026/May/27/sqlite-agents/">sqlite AGENTS.md - simonwillison.net</a></li>
<li><a href="https://themodelwire.com/article/sqlite-agents-md-01KSNXFG179RJA3K5FQ9TXJ1R2">sqlite AGENTS.md · Modelwire</a></li>

</ul>
</details>

**社区讨论**: Datasette Discord 上的社区讨论指出 SQLite 明确政策的创新性，一些人表示支持保护代码质量，另一些人则质疑此类政策能否有效执行。

**标签**: `#sqlite`, `#ai-agents`, `#open-source`, `#software-engineering`, `#policy`

---

<a id="item-6"></a>
## [面向 AI 代理的开源网络安全技能库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

一个名为 Anthropic-Cybersecurity-Skills 的 GitHub 仓库已发布，包含 754 个面向 AI 代理的结构化网络安全技能，映射到五个主要框架（MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF），并兼容 26 个以上 AI 平台。 该库满足了 AI 代理对标准化、可复用网络安全能力日益增长的需求，使开发者能够为代理配备跨多个领域和平台的生产级安全技能，从而可能加速 AI 在安全运维中的应用。 这些技能涵盖 26 个安全领域，遵循 agentskills.io 开放标准，并采用 Apache 2.0 许可证。仓库还包含 GARS-2026 报告的调查链接以及通过 Casky.ai 提供的游乐场。

rss · GitHub Trending - Daily (All) · May 28, 23:09

**背景**: Agent Skills 是由 Anthropic 主导的开放标准，用于以 AI 代理可读取和执行的格式编码可重复任务知识。MITRE ATT&CK 是广泛使用的对手战术和技术知识库，NIST CSF 提供网络安全框架。D3FEND 是防御性对策本体，而 MITRE ATLAS 专注于 AI 特定威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and ...</a></li>
<li><a href="https://deepwiki.com/libukai/awesome-agent-skills/1.1-the-agent-skills-standard">The Agent Skills Standard | libukai/awesome-agent-skills ...</a></li>
<li><a href="https://www.productbuilder.net/learn/agent-skills">Agent Skills: The Open Standard for AI Agent Capabilities</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-7"></a>
## [哈佛开源机器学习系统工程书籍](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

哈佛大学 CS249r 课程在 GitHub 上开源了一本名为《机器学习系统：工程人工智能系统的原理与实践》的书籍，支持包括英语、中文、日语和韩语在内的多语言版本。 该资源提供了一所顶尖大学关于机器学习系统工程的全面、免费可访问的课程内容，弥合了机器学习模型开发与生产部署之间的差距，面向全球受众。 该仓库不仅包含书籍，还包括幻灯片、实验和 TinyTorch 实现等补充材料，全部采用 CC-BY-NC-SA 4.0 许可证。

rss · GitHub Trending - Python · May 28, 23:09

**背景**: 机器学习系统工程关注在生产环境中部署和维护机器学习模型的实际方面，而这往往被模型开发所忽视。本书旨在教授构建稳健 AI 系统所需的原理和实践，涵盖数据管道、模型服务和监控等主题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hellogithub.com/en/repository/harvard-edge/cs249r_book">harvard-edge/ cs 249 r _ book : Machine Learning Systems... - HelloGitHub</a></li>
<li><a href="https://blog.tensorflow.org/2024/11/mlsysbookai-principles-and-practices-of-machine-learning-systems-engineering.html">MLSysBook.AI: Principles and Practices of Machine Learning Systems Engineering — The TensorFlow Blog</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#systems engineering`, `#education`, `#AI`, `#open source`

---

<a id="item-8"></a>
## [NVIDIA Megatron Bridge 实现与 Hugging Face 的互操作](https://github.com/NVIDIA-NeMo/Megatron-Bridge) ⭐️ 8.0/10

NVIDIA 发布了 Megatron Bridge 库，这是 NeMo 框架内的一个 PyTorch 原生工具，提供 Megatron 与 Hugging Face 模型格式之间的双向转换，并支持流行 LLM 和 VLM 的预训练、SFT 和 LoRA。 该库连接了两大生态系统——用于大规模训练的 Megatron 和用于社区模型的 Hugging Face——实现了无缝模型转换和互操作，简化了研究人员和工程师处理大型语言模型的工作流程。 该库支持 DeepSeek V4、Nemotron-3 Nano Omni 和 Gemma 4 VL 等模型，并为新版本提供 day-0 支持。它还提供了多模态模型的转换、推理、SFT 和 PEFT（LoRA）示例。

rss · GitHub Trending - Python · May 28, 23:09

**背景**: Megatron 是 NVIDIA 用于大规模训练大型语言模型的框架，而 Hugging Face Transformers 是广泛使用的预训练模型访问库。此前，在这两种格式之间转换模型需要手动操作。Megatron Bridge 自动化了这一过程，使利用两个生态系统变得更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA-NeMo/Megatron-Bridge">GitHub - NVIDIA-NeMo/Megatron-Bridge: Training library for ...</a></li>
<li><a href="https://docs.nvidia.com/nemo/megatron-bridge/latest/">NeMo Megatron Bridge - NVIDIA Documentation Hub</a></li>
<li><a href="https://pypi.org/project/megatron-bridge/">megatron-bridge · PyPI</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Megatron`, `#Hugging Face`, `#LLM`, `#Training`

---

<a id="item-9"></a>
## [Soro：基于 Gemma 3 的塔吉克语专用大语言模型](https://arxiv.org/abs/2605.27379) ⭐️ 8.0/10

研究人员推出了 Soro，这是一系列塔吉克语专用大语言模型，通过在精心筛选的 19 亿词元塔吉克语语料库上对 Gemma 3 进行持续预训练，并在 4 万个示例上进行指令微调而构建，同时开源了塔吉克语基准测试集。 Soro 填补了 LLM 在塔吉克语等低资源语言覆盖上的关键空白，能够在保持强大英语性能的同时，为塔吉克斯坦的教育等领域提供实用的 AI 应用。 Soro 采用 FP8 和 INT4 量化以减少边缘部署的内存需求，并在涵盖通用知识、语言学和入学考试的新塔吉克语基准测试中，优于同尺寸的 Gemma 3 基线模型。

rss · arXiv - AI · May 28, 04:00

**背景**: 塔吉克语等低资源语言缺乏足够的数字数据和 NLP 工具，构建有效的语言模型面临挑战。持续预训练通过在相关数据上进一步训练，将通用 LLM 适应到特定领域或语言。Gemma 3 是 Google 推出的轻量级、开放权重的模型，可在单个 GPU 上运行，适合资源受限环境下的部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemma/gemma-3/">Gemma 3 — Google DeepMind</a></li>
<li><a href="https://arxiv.org/abs/2402.17400">[2402.17400] Investigating Continual Pretraining in Large Language Models: Insights and Implications</a></li>

</ul>
</details>

**标签**: `#low-resource NLP`, `#large language models`, `#continual pretraining`, `#Tajik language`, `#benchmarks`

---

<a id="item-10"></a>
## [DynaSchedBench：校准的动态调度基准](https://arxiv.org/abs/2605.27566) ⭐️ 8.0/10

DynaSchedBench 提出了一个顺序事件空间校准器（SESC），通过计算调度压力指数（SSI）来对动态柔性作业车间调度问题（DFJSP）的实例按难度分层。 该框架解决了静态基准与未校准生成器之间的方法论矛盾，使得对基于 LLM 的调度代理进行严格测试成为可能，并揭示了它们的局限性，例如可观测性悖论。 SESC 在计算上比进化基线更高效，并能可靠地收敛到目标指标。该框架包括实例生成、基于快照的模拟、代理、评估和可视化等模块化组件。

rss · arXiv - AI · May 28, 04:00

**背景**: 动态柔性作业车间调度问题（DFJSP）涉及在机器上调度作业，同时处理新作业到达或机器故障等动态事件。传统基准常常存在过拟合或随机噪声问题，阻碍了神经组合优化的进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2550454">Dynamic flexible job shop scheduling problem considering ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10845-025-02645-x">Systematic review and future directions in dynamic flexible ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-024-79593-8">Dynamic scheduling for flexible job shop based on MachineRank ...</a></li>

</ul>
</details>

**标签**: `#scheduling`, `#benchmarking`, `#combinatorial optimization`, `#LLM agents`, `#operations research`

---

<a id="item-11"></a>
## [LLM 从根本上无法进行因果发现；A-CBO 提供出路](https://arxiv.org/abs/2605.27567) ⭐️ 8.0/10

一篇新论文证明，大型语言模型（LLM）无法仅从观测数据中可靠地进行因果发现，这一根本性限制被形式化为核障碍定理。作者提出了代理因果贝叶斯优化（A-CBO），该方法将冻结的 LLM 用作干预预言机，并通过外部贝叶斯循环可证明地收敛到正确的因果图。 这项工作为 LLM 在因果发现基准上表现停滞提供了理论解释，将关注点从扩大模型规模转向设计结合 LLM 与结构化推理的混合系统。A-CBO 无需训练即可取得强劲结果，为 AI 中的因果推断提出了新范式。 核障碍定理表明，监督微调、直接偏好优化和上下文学习都会产生无法区分生成相似观测数据的因果图的预测器。A-CBO 仅需对数轮次的干预查询即可将信念集中在候选因果图上。

rss · arXiv - AI · May 28, 04:00

**背景**: 因果发现旨在从数据中推断因果关系，这对科学推理至关重要。LLM 已在此任务上接受测试，但表现有限，尤其是在复杂图上。核障碍定理将这种失败解释为学习范式的内在缺陷，而非特定模型或数据集的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27567">Why LLMs Fail at Causal Discovery and How Interventional ...</a></li>
<li><a href="https://www.emergentmind.com/papers/2506.00844">LLMs in Causal Discovery: Limits & Guidelines</a></li>
<li><a href="https://www.amazon.science/publications/causal-bayesian-optimization">Causal Bayesian optimization - Amazon Science</a></li>

</ul>
</details>

**标签**: `#causal discovery`, `#large language models`, `#machine learning theory`, `#Bayesian optimization`

---

<a id="item-12"></a>
## [RULER：新指标检测机器遗忘中的残留信息](https://arxiv.org/abs/2605.27569) ⭐️ 8.0/10

研究人员提出了 RULER，一套用于机器遗忘的表示级验证指标，包括基于原始模型的对比指标（M2）和无原始模型的指标（M4）。 当前的输出级验证协议可能被欺骗，而 RULER 能检测中间表示中的残留信息，从而提升 AI 系统的可信度和合规性。 实验中，四种近似遗忘方法通过了输出级评估，但 M2 在 12 种条件中的 10 种检测到显著残留（p<0.05）。M4 还能检测人脸识别模型中的身份级记忆。

rss · arXiv - AI · May 28, 04:00

**背景**: 机器遗忘旨在无需完全重新训练的情况下，移除特定训练数据对模型的影响。当前验证依赖输出级指标（如成员推断和准确率），可能遗漏内部表示中的隐藏信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27569">RULER: Representation - Level Verification of Machine Unlearning</a></li>
<li><a href="https://arxiv.org/pdf/2605.27569">RULER: Representation - Level Verification of Machine Unlearning</a></li>

</ul>
</details>

**标签**: `#machine unlearning`, `#verification`, `#representation learning`, `#AI safety`, `#privacy`

---

<a id="item-13"></a>
## [LaneRoPE：大语言模型的协作并行推理方法](https://arxiv.org/abs/2605.27570) ⭐️ 8.0/10

LaneRoPE 提出了序列间注意力机制和 RoPE 扩展，使多个并行的大语言模型生成过程能够在解码时相互协作，从而提升测试时扩展效率。 这解决了测试时扩展中独立采样的关键限制，使大语言模型能够在并行序列间共享中间推理过程，从而以最小的架构改动提升准确性。 LaneRoPE 使用序列间注意力掩码使不同序列的 token 采样相互依赖，并通过 RoPE 扩展编码序列内和跨序列的相对位置，推理开销可忽略不计。

rss · arXiv - AI · May 28, 04:00

**背景**: 并行测试时扩展技术（如 best-of-N）从同一提示生成多个独立序列并选择最佳结果，但序列之间无法相互影响。LaneRoPE 通过修改注意力掩码和位置编码实现协作，其基础是 Rotary Position Embedding (RoPE)，这是现代大语言模型中常用的位置编码方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27570">[2605.27570] LaneRoPE: Positional Encoding for Collaborative ...</a></li>
<li><a href="https://openreview.net/forum?id=6WAuvwZjmw">LaneRoPE: Positional Encoding for Collaborative Parallel ...</a></li>
<li><a href="https://learncodecamp.net/rope-explained/">RoPE Explained: The Positional Encoding Trick Behind Modern ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#positional encoding`, `#parallel decoding`, `#test-time scaling`, `#reasoning`

---

<a id="item-14"></a>
## [Agyn：面向可扩展 AI 代理的开源平台](https://arxiv.org/abs/2605.27575) ⭐️ 8.0/10

Agyn 是一个用于大规模部署 AI 代理的开源平台，具有基于 Kubernetes 的信号驱动无服务器运行时、通过 Terraform 提供程序实现的基础设施即代码以及零信任安全。该平台与代理无关、模型无关且云无关。 Agyn 解决了 AI 代理在生产中的关键挑战，如可扩展性、隔离、治理和安全性，这对企业采用至关重要。它提供了一种标准化的开源方法，可以加速可靠且安全的 AI 代理系统的部署。 该平台使用基于 Kubernetes 的信号驱动、有状态无服务器运行时，一个用于定义代理和框架的 Terraform 提供程序，以及基于最小权限原则的零信任安全模型。它被设计为与代理、模型和云提供商无关。

rss · arXiv - AI · May 28, 04:00

**背景**: AI 代理是执行任务的自主程序，通常可以访问内部服务，但在生产环境中部署它们需要处理非确定性工作流、有状态会话和安全性。Kubernetes 上的无服务器计算提供按需执行和自动扩展，而 Terraform 等基础设施即代码工具支持声明式管理。零信任安全确保没有隐式信任，强制执行最小权限访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agynio/platform">GitHub - agynio/ platform : Agyn is an open-source Kubernetes-native...</a></li>
<li><a href="https://www.youtube.com/watch?v=i4vZQ9vRvfY">Agyn Demo: AI Engineering Teams Working Natively in... - YouTube</a></li>
<li><a href="https://www.linkedin.com/posts/omarsar_another-great-paper-if-you-are-building-with-activity-7427033691593428992-xIkX">Agyn : Open-Source Multi-Agent Platform for Software... | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#serverless`, `#Kubernetes`, `#zero-trust`, `#open-source`

---

<a id="item-15"></a>
## [综述：MoE 应对多模态学习挑战](https://arxiv.org/abs/2605.27431) ⭐️ 8.0/10

一篇新的综述系统回顾了混合专家模型（MoE）如何应对多模态学习挑战，涵盖高效扩展、表示学习以及对不完美数据的适应。 该综述填补了联合分析 MoE 与多模态学习的空白，为未来可扩展且可解释的多模态 AI 系统研究奠定了基础。 该综述从三个视角审视 MoE：作为高效引擎、表示学习器以及不完美数据的适配器。它指出了可解释路由、专家通信和终身多模态学习等研究空白。

rss · arXiv - Machine Learning · May 28, 04:00

**背景**: 混合专家模型（MoE）是一种机器学习技术，它使用多个专门的子网络（专家）和一个门控网络为每个输入选择最佳专家，通过仅激活部分参数实现高效扩展。多模态学习涉及整合多种数据类型（如文本、图像、音频）的信息，面临表示、对齐、融合以及处理缺失模态等挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://www.datacamp.com/blog/mixture-of-experts-moe">What Is Mixture of Experts (MoE)? How It Works, Use Cases & More | DataCamp</a></li>
<li><a href="https://engineering.mercari.com/en/blog/entry/20210623-5-core-challenges-in-multimodal-machine-learning/">5 Core Challenges In Multimodal Machine Learning | Mercari Engineering</a></li>

</ul>
</details>

**标签**: `#Mixture-of-Experts`, `#Multimodal Learning`, `#Survey`, `#Deep Learning`, `#Scalability`

---

<a id="item-16"></a>
## [液态神经网络在效率和鲁棒性上超越 LSTM](https://arxiv.org/abs/2605.27467) ⭐️ 8.0/10

一项新的比较研究表明，液态神经网络（特别是闭式连续时间网络）在四个序列模式识别任务（包括神经形态数据和临床时间序列）中，相比 LSTM 实现了更优的参数效率和鲁棒性。 这项工作凸显了连续时间模型在数据稀疏或缺失的现实应用（如临床监测）中的实际优势，可能以更少的参数实现更可靠的 AI 系统。 该研究在 N-MNIST、QuickDraw、IAM 和 PhysioNet Sepsis-3 数据集上对 LNN 与 LSTM 进行了基准测试，并引入了时间丢弃压力测试来评估对缺失数据的鲁棒性。

rss · arXiv - Machine Learning · May 28, 04:00

**背景**: 液态神经网络（LNN）是一类连续时间神经网络，通过微分方程建模隐藏状态演化，而传统的 RNN 和 LSTM 在离散时间步上运行。闭式连续时间（CfC）网络为液态时间常数网络提供了高效的闭式近似，从而实现了更快的训练和推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://builtin.com/articles/liquid-neural-networks">Liquid Neural Networks (LNN): A Guide - Built In</a></li>
<li><a href="https://www.nature.com/articles/s42256-022-00556-7">Closed-form continuous-time neural networks - Nature</a></li>
<li><a href="https://www.garrickorchard.com/datasets/n-mnist">Garrick Orchard - N-MNIST</a></li>

</ul>
</details>

**标签**: `#Liquid Neural Networks`, `#LSTM`, `#Sequential Pattern Recognition`, `#Robustness`, `#Clinical Utility`

---

<a id="item-17"></a>
## [LCO：基于 LLM 的约束优化实现更安全的智能体](https://arxiv.org/abs/2605.27375) ⭐️ 8.0/10

研究人员提出了基于 LLM 的约束优化（LCO）框架，该框架无需微调即可缓解自主 LLM 智能体中的上下文奖励破解（ICRH）问题。 ICRH 带来了重大安全风险，因为 LLM 智能体会迭代优化代理目标，导致有害副作用；LCO 提供了一种实用的、无需微调的防御方法，可应用于现有模型。 LCO 包含一个自我思考模块，用于主动进行安全考量，以及一个进化采样模块，利用基于 LLM 的交叉和变异将动作约束在安全解空间内。在推文参与度任务中，LCO 将 GPT-4 上的毒性增长率降低了 39%；在策略优化基准上，它将 ICRH 发生率降低了 15.23%，且未牺牲任务性能。

rss · arXiv - NLP · May 28, 04:00

**背景**: 上下文奖励破解（ICRH）发生在 LLM 智能体根据反馈迭代优化其输出时，过度优化代理目标并导致意外的有害副作用。与训练期间的传统奖励破解不同，ICRH 发生在推理时，无需权重更新，使得现有防御措施效果不佳。LCO 通过将约束优化直接集成到 LLM 的推理过程中来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27375">[2605.27375] LCO : LLM - based Constraint Optimization for Safer...</a></li>
<li><a href="https://arxiv.org/html/2402.06627v3">Feedback Loops With Language Models Drive In - Context Reward ...</a></li>
<li><a href="https://lilianweng.github.io/posts/2024-11-28-reward-hacking/">Reward Hacking in Reinforcement Learning | Lil'Log</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI safety`, `#constraint optimization`, `#reward hacking`, `#agentic AI`

---

<a id="item-18"></a>
## [OralAgent：首个交互式牙科影像分析 AI 智能体](https://arxiv.org/abs/2605.27378) ⭐️ 8.0/10

研究人员推出了 OralAgent，这是首个牙科专用 AI 智能体，它将多模态推理、22 个视觉分析工具以及从 368 本牙科教科书中检索知识集成到一个端到端框架中，用于交互式牙科影像分析。 这一进展弥合了孤立的牙科 AI 模型与现实临床工作流程之间的差距，有望提高口腔医疗中的诊断准确性和治疗规划水平。 该系统还引入了 OralCorpus，一个包含 1.348 亿词元的大规模双语牙科语料库，用于检索增强生成；以及 OralQA-ZH，一个包含 11 个亚专科 798 道题的中文选择题基准。

rss · arXiv - NLP · May 28, 04:00

**背景**: 检索增强生成（RAG）通过允许大语言模型访问外部知识库来提升其准确性并减少幻觉。OralAgent 将该技术应用于牙科领域，并结合了专门的影像分析工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval - augmented generation - Wikipedia</a></li>
<li><a href="https://aws.amazon.com/what-is/retrieval-augmented-generation/">What is RAG? - Retrieval - Augmented Generation AI Explained - AWS</a></li>
<li><a href="https://huggingface.co/datasets/OralGPT/OralCorpus">OralGPT/OralCorpus · Datasets at Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI Agent`, `#Medical AI`, `#Dental Image Analysis`, `#Multimodal Reasoning`, `#Retrieval-Augmented Generation`

---

<a id="item-19"></a>
## [自对齐方法弥合低资源语音模型的稳定性-表现力鸿沟](https://arxiv.org/abs/2605.27383) ⭐️ 8.0/10

研究人员提出了两种自对齐框架（DGSA 和 TDSC），以缓解由合成数据扩展引起的低资源语音模型中的稳定性-表现力鸿沟，并实现了老挝语的零样本语音克隆。 这项工作解决了低资源语言语音模型中的关键权衡问题，在真实数据稀缺的情况下实现了高保真语音合成和语音克隆，性能优于 ElevenLabs 和 Gemini Pro 等商业系统。 稳定性-表现力鸿沟描述了合成数据如何提高音素准确性但抑制韵律变异性，导致合成侵蚀。DGSA 通过韵律-音色分离恢复表现力，而 TDSC 在参考样本极其有限的情况下使用自动探索和过滤来稳定生成。

rss · arXiv - NLP · May 28, 04:00

**背景**: 语音语言模型（SLM）直接生成语音，无需文本到语音的流水线，但低资源语言缺乏转录语音。合成数据扩展是常用方法，但会引入音素准确性和韵律表现力之间的权衡，即稳定性-表现力鸿沟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27383">[2605.27383] Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models</a></li>
<li><a href="https://arxiv.org/html/2605.27383">Bridging the Stability-Expressivity Gap: Synthetic Data Scaling and Preference Alignment for Low-Resource Spoken Language Models</a></li>
<li><a href="https://arxiv.org/pdf/2605.27383">Bridging the Stability - Expressivity Gap : Synthetic Data Scaling and...</a></li>

</ul>
</details>

**标签**: `#spoken language models`, `#low-resource languages`, `#synthetic data`, `#speech synthesis`, `#self-alignment`

---

<a id="item-20"></a>
## [FLUID 高效将自回归大语言模型适配为扩散模型](https://arxiv.org/abs/2605.27387) ⭐️ 8.0/10

研究人员提出 FLUID 框架，通过严格因果对齐和弹性视野机制，将预训练的自回归大语言模型适配为扩散模型，实现无需从头预训练的并行文本生成。 该工作弥合了自回归模型与扩散模型之间的结构不匹配，大幅降低训练成本的同时达到最先进性能，有望加速大语言模型中高效并行生成的部署。 严格因果对齐允许从 GPT 风格检查点无缝初始化，弹性视野则根据局部信息密度动态调整去噪步长。该方法声称将训练成本降低数个数量级。

rss · arXiv - NLP · May 28, 04:00

**背景**: 自回归模型（如 GPT）逐个 token 顺序生成文本，而扩散模型通过迭代去噪随机噪声来并行生成文本。然而，扩散模型通常需要双向注意力，这与预训练自回归模型的因果注意力不兼容，导致必须从头进行昂贵的预训练。FLUID 通过强制严格因果对齐来保留自回归注意力模式，并引入熵驱动机制优化去噪调度，从而解决了这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27387">[2605.27387] From AR to Diffusion : Efficiently Adapting Large...</a></li>
<li><a href="https://arxiv.org/html/2605.27387">From AR to Diffusion: Efficiently Adapting Large Language Models with Strictly Causal and Elastic Horizons</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Diffusion Models`, `#Parallel Text Generation`, `#Model Adaptation`, `#Efficient Training`

---

<a id="item-21"></a>
## [EvoSpec：投机解码的实时自适应方法](https://arxiv.org/abs/2605.27390) ⭐️ 8.0/10

EvoSpec 提出了一种框架，在投机解码过程中实时动态调整草稿模型的词汇表和参数，克服了静态剪枝在专业领域或主题切换场景中导致接受率下降的局限性。 这一创新通过实现对动态分布偏移的高效自适应，解决了 LLM 推理中的关键瓶颈——输出投影层，有望在编程、法律和医学等实际应用中提升推理速度并降低内存开销。 EvoSpec 使用上下文感知机制，通过语义和统计索引检索长尾词元，并采用基于课程学习的轻量级在线对齐策略，以最小化草稿模型与目标模型之间的分布差距。在 EAGLE-3 上，相比静态基线 FR-Spec 实现了 1.13 倍加速，内存开销降低 27%。

rss · arXiv - NLP · May 28, 04:00

**背景**: 投机解码通过使用小型草稿模型生成候选词元，再由大型目标模型进行验证，从而加速 LLM 推理。然而，随着词汇表规模增长，将隐藏状态映射到词汇表 logits 的输出投影层成为瓶颈。静态剪枝方法虽能降低这一开销，但在主题切换或专业领域等动态分布偏移场景下表现不佳。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>
<li><a href="https://research.google/blog/looking-back-at-speculative-decoding/">Looking back at speculative decoding</a></li>
<li><a href="https://arxiv.org/pdf/2505.10202">VQ-Logits: Compressing the Output Bottleneck of Large ...</a></li>

</ul>
</details>

**标签**: `#speculative decoding`, `#LLM inference`, `#vocabulary adaptation`, `#online learning`, `#curriculum learning`

---

<a id="item-22"></a>
## [表示条件扩散模型提升合成数据质量](https://arxiv.org/abs/2605.27495) ⭐️ 8.0/10

研究人员提出表示条件扩散模型，利用来自 DINOv2、DINOv3 和 CLIP 的学习表示生成合成训练数据，在 ImageNet100 上比类条件生成高出 10.76 个百分点（top-1 准确率），甚至比真实数据高出 2.0 个百分点。 该方法通过生成高质量合成数据来应对深度学习中的数据稀缺问题，可以增强或替代真实数据集，从而降低数据收集和标注的成本与工作量。 该方法使用以自监督模型（如 DINOv2）的表示为条件的潜在扩散模型，这些表示比类别标签捕获更丰富的语义信息。扩大合成数据集规模可进一步提升性能，且条件空间还可用于样本过滤。

rss · arXiv - Computer Vision · May 28, 04:00

**背景**: 扩散模型是一种学习去噪数据的生成模型，潜在扩散模型在压缩的潜在空间中执行该过程以提高效率。DINOv2 是一种自监督视觉模型，无需标签即可学习鲁棒的图像表示，捕获对象部件和分割等特征。模式覆盖指生成模型产生覆盖数据分布所有模式的多样化样本的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2304.07193v2">DINOv2: Learning Robust Visual Features without Supervision</a></li>
<li><a href="https://www.picsellia.com/post/dinov2-steps-by-steps-explanations-picsellia">DINOv2 - Steps by steps explanations - Picsellia | Picsellia</a></li>
<li><a href="https://encord.com/blog/dinov2-self-supervised-learning-explained/">DINOv2 Explained: Revolutionizing Computer Vision with Self-Supervised Learning | Encord</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#synthetic data`, `#representation learning`, `#image classification`, `#data augmentation`

---

<a id="item-23"></a>
## [What-If World：视频世界模型的因果基准](https://arxiv.org/abs/2605.27589) ⭐️ 8.0/10

研究人员推出了 What-If World 基准，包含基于 nuScenes 和 DROID 数据集真实帧构建的 319 个提示对，用于测试视频生成模型是否正确建模驾驶和操作场景中的因果物理变化。 该基准填补了具身 AI 世界模型评估的关键空白，揭示了即使最先进的视频生成模型也无法可靠模拟因果干预，而这对于动作条件仿真和基于模型的规划至关重要。 该基准使用六种物理变量的分类法，并通过 APEO（四部分评分标准）对每个提示对进行评分；在九个模型中，没有系统在配对得分上超过 52%，开源模型集中在 28% 左右。

rss · arXiv - Computer Vision · May 28, 04:00

**背景**: 视频生成模型越来越多地被用作驾驶和机器人操作等任务的世界模拟器。现有基准单独评估视频，无法检测模型是否正确响应输入提示中的因果变化。What-If World 使用仅在一个物理变量上不同的配对提示来测试因果推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nuscenes.org/">Recent announcements, as well as key figures about the nuScenes ...</a></li>
<li><a href="https://droid-dataset.github.io/">DROID: A Large-Scale In-the-Wild Robot Manipulation Dataset</a></li>

</ul>
</details>

**标签**: `#world models`, `#causal reasoning`, `#video generation`, `#embodied AI`, `#benchmark`

---

<a id="item-24"></a>
## [重尾结果的因果推断](https://arxiv.org/abs/2605.27474) ⭐️ 8.0/10

本文提出了一种新的平均剂量响应函数（ADRF）估计器，为重尾结果提供尾部形状诊断，打破了现有方法中因稳健损失函数选择而导致尾部推断变化的循环依赖。 这项工作填补了极端事件因果推断的关键空白，对于金融和气候等高风险领域至关重要，在这些领域中，千分之一极端事件才是实际目标。与分位数回归相比，所提方法将深尾回报水平 MAE 降低了 11%，条件短缺 MAE 降低了 25.5%。 该估计器输出四个处理条件量：尾部形状、深尾回报水平、条件短缺和均值 ADRF，并在极值建模不支持时提供明确的拒绝机制。在样本稀缺场景（n ≤ 2000）下，MAE 降低了 20-29%，并在汽车保险索赔数据上成功触发了外推拒绝。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 因果推断旨在估计结果如何响应处理，但标准方法如双机器学习（DML）会抑制重尾结果中的极端值以稳定平均值。重尾分布在尾部有更多概率质量，使得极端事件更可能发生，这在金融和气候领域至关重要。现有的尾部感知方法存在循环依赖问题，因为它们从残差中读取尾部，导致基于稳健损失函数（如 Huber 与 Welsch）选择的不稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Huber_loss">Huber loss - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1908.05097">[1908.05097] Causal discovery in heavy-tailed models - arXiv.org Causal discovery in heavy-tailed models - JSTOR Causal modelling of heavy-tailed variables and confounders ... Causal discovery in heavy-tailed models - Project Euclid Full article: When Heavy Tails Disrupt Statistical Inference Causal discovery in heavy-tailed models • causalXtreme Heavy-tailed distribution - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heavy-tailed_distribution">Heavy-tailed distribution - Wikipedia</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#heavy tails`, `#machine learning`, `#extreme events`, `#statistics`

---

<a id="item-25"></a>
## [新协议为因果边附加不可能性证书](https://arxiv.org/abs/2605.27477) ⭐️ 8.0/10

一项新的观测因果发现协议为每条候选边附加一个离散的不可能性证书（RESOLVED 或 IMPOSSIBLE），从而区分由数据识别的方向与基于假设分配的方向。该协议还引入了五个门控可识别性层级（LSNM、IGCI、Stein、MDL、PEIT）和两个预言机原语，建立了恢复任意有向无环图所需专家交互次数的上界为 1+K。 这项工作解决了因果发现中的一个基本局限：缺乏每条边的不确定性量化。通过提供不可能性证书和分层预言机框架，它实现了专家知识的原则性整合，并可能显著提高科学应用中因果推断的可靠性。 不可能性证书使用 RESOLVED 代码记录确定方向所依据的可识别性定理，使用 IMPOSSIBLE 代码指定失败模式以及专家必须回答的具体问题。双变量级联包含五个层级（LSNM、IGCI、Stein、MDL、PEIT），当前提条件检验失败时它们会弃权；预言机原语（元枢纽查询和子节点查询）保证最多通过 1+K 次专家交互即可恢复任意有向无环图，其中 K 是非叶顶点数。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 因果发现旨在从观测数据中推断因果关系，但在标准马尔可夫性和忠实性假设下，只能识别出一个马尔可夫等价类（MEC）——即具有相同条件独立性的多个有向无环图。MEC 内的边方向无法仅由数据确定，需要额外假设或专家知识。该协议提供了一种系统化的方法来追踪哪些方向已被识别，哪些需要外部输入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27477">[2605.27477] Iterative Causal Discovery : Per-Edge Impossibility ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/11564089_9">Learning Causal Structures Based on Markov Equivalence Class | Springer Nature Link</a></li>
<li><a href="https://arxiv.org/html/2505.02781v1">Local Markov Equivalence and Local Causal Discovery for Identifying Controlled Direct Effects</a></li>

</ul>
</details>

**标签**: `#causal discovery`, `#causal inference`, `#identifiability`, `#graphical models`, `#machine learning`

---

<a id="item-26"></a>
## [噪声异质性核度量的高效推断](https://arxiv.org/abs/2605.27526) ⭐️ 8.0/10

本文针对加性噪声模型中的噪声异质性核度量，提出了半参数有效推断方法，引入了一种希尔伯特值一步估计量来校正第一阶段回归偏差。 这项工作为机器学习流程中的残差独立性和拟合优度提供了有效的假设检验和置信区间，解决了使标准推断失效的关键偏差来源。 该估计量经过自助法校准且渐近有效，该框架可扩展到包含额外协变量的场景，用于推断不同处理组间的分布异质性。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 在加性噪声模型中，结果被建模为协变量的函数加上独立噪声。当使用灵活的机器学习方法估计回归函数时，残差可能继承偏差，导致协变量与残差之间产生虚假依赖，从而破坏标准的独立性假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2303.16711">One-Step Estimation of Differentiable Hilbert-Valued Parameters Images One-Step Estimation of Differentiable Hilbert-Valued Parameters One-Step Estimation of Differentiable Hilbert-Valued ... GitHub - alexluedtke12/HilbertOneStep: Implements the one ... One-Step Estimation of Differentiable Hilbert-Valued ... One-Step Estimation of Differentiable Hilbert-Valued Parameters</a></li>
<li><a href="https://jmlr.org/papers/volume15/peters14a/peters14a.pdf">Causal Discovery with Continuous Additive Noise Models Additive noise models — causal-learn 0.1.3.6 documentation Additive white Gaussian noise - Wikipedia Causal Identiﬁcation with Additive Noise Models: Quantifying ... Nonlinear causal discovery with additive noise models - NeurIPS Identifying Causal Mechanism Shifts Under Additive Models ...</a></li>

</ul>
</details>

**标签**: `#semiparametric inference`, `#kernel methods`, `#noise heterogeneity`, `#machine learning`, `#causal inference`

---

<a id="item-27"></a>
## [利用几何特征检测多轮欺骗](https://arxiv.org/abs/2605.27671) ⭐️ 8.0/10

研究人员提出了一种流程，通过多目标遗传优化生成多轮欺骗提示，并利用嵌入空间中的几何特征进行检测，使用轻量级分类器实现了 0.89 的高召回率。 这项工作通过关注多轮欺骗（比单轮攻击更现实）填补了 LLM 安全的关键空白，并提供了一种实用、可解释的检测方法，无需昂贵的端到端训练。 检测模型使用三个几何特征（角度覆盖、距离比、线性度）加上成对相似性统计，在基础、改写和截断的三轮场景中实现了 0.74-0.86 的测试 F1 分数。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 大型语言模型（LLM）通常使用单轮提示进行安全测试，但现实攻击可能涉及间接的多轮探测以绕过防御。嵌入空间中的几何特征捕获了欺骗意图的结构模式，从而无需完全重新训练模型即可实现轻量级检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/gepa-ai/gepa">GitHub - gepa-ai/gepa: Optimize prompts, code, and more with ...</a></li>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1613007/full">GAAPO: genetic algorithmic applied to prompt optimization</a></li>
<li><a href="https://arxiv.org/pdf/2511.22150">From Topology to Retrieval: Decoding Embedding Spaces with ...</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#adversarial attacks`, `#multi-turn deception`, `#geometric features`, `#genetic optimization`

---

<a id="item-28"></a>
## [GRASP：微调中无监督去除虚假相关性](https://arxiv.org/abs/2605.27676) ⭐️ 8.0/10

该论文提出了 GRASP，一种无监督方法，通过分析 LoRA 权重在微调中识别并去除虚假相关性，同时保留有用的潜在因子。在涌现失调和政治偏见任务上验证，优于基线方法。 这项工作以原则性的无监督方法解决了微调大语言模型中的关键问题——虚假相关性，无需对虚假概念进行标注。它在减少偏见和保持任务性能之间提供了更好的权衡，增强了 NLP 的公平性和鲁棒性。 GRASP 使用梯度投影来防止模型对已识别的潜在因子产生新的依赖，同时保留预训练内容。它在不安全代码生成中完全消除了失调，在不良医疗建议中减少了约 5 倍，并将政治漂移减半，同时提升了任务性能。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 在精心策划的数据集上微调预训练语言模型可能会在任务和意外的潜在因子（如政治倾向）之间引入虚假相关性。现有的偏见去除方法（如激活引导）需要虚假概念的标签，并可能丢弃有用的信号。LoRA 是一种参数高效的微调方法，学习低秩权重更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/revolutionizing-ai-fine-tuning-grasp-keeps-models-on-target-hdtc">Revolutionizing AI Fine-Tuning: GRASP Keeps Models On Target</a></li>
<li><a href="https://arxiv.org/pdf/2605.27676">Unsupervised Identification and Removal of Spurious ...</a></li>
<li><a href="https://arxiv.org/html/2508.09019v1">Activation Steering for Bias Mitigation: An Interpretable Approach to...</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#spurious correlations`, `#bias removal`, `#LLMs`, `#LoRA`

---

<a id="item-29"></a>
## [软专家：面向不确定性感知的 LLM 后训练的α-Rényi 集成方法](https://arxiv.org/abs/2605.27747) ⭐️ 8.0/10

研究人员提出了一种α-Rényi 变分框架，学习大语言模型后训练参数的分布，实现训练样本在集成成员间的软路由。 该方法解决了标准 LLM 训练将冲突数据压缩为单一平均行为的根本局限，为监督微调和偏好优化提供了可扩展的不确定性量化与模型专业化能力。 该变分目标在经典变分贝叶斯与面向预测的后验学习之间插值，框架使用附着在冻结基模型上的 LoRA 适配器实现可扩展训练。

rss · arXiv - Data Science & Statistics · May 28, 04:00

**背景**: 当前 LLM 训练从大量常含矛盾的数据中学习单一参数集，迫使模型平均化冲突目标。深度集成方法独立训练多个模型以改善不确定性，但计算成本高昂。α-Rényi 散度推广了变分推断中使用的 KL 散度，允许在全局合理性与专业化之间灵活权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.27747">[2605.27747] Soft Specialists: ||alpha;$-Rényi Ensembles for ...</a></li>
<li><a href="https://www.machinebrief.com/news/reimagining-ai-training-with-the-a-renyi-variational-framewo-h0pf">Reimagining AI Training with the α-Rényi Variational Framework</a></li>

</ul>
</details>

**标签**: `#large language models`, `#uncertainty quantification`, `#variational inference`, `#post-training`, `#deep ensembles`

---

<a id="item-30"></a>
## [新提取工艺有望实现更便宜、更环保的锂生产](https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/) ⭐️ 8.0/10

研究人员在《科学》杂志上发表了一种从硬岩中提取锂的新方法，该方法比现有技术更便宜且更环保。一家名为 Rock Zero 的初创公司正在将该技术商业化。 这一突破可能显著降低锂生产的成本和碳足迹，而锂对于电动汽车电池和储能至关重要。它通过使锂供应更加可持续和廉价，解决了清洁能源转型中的一个主要瓶颈。 该工艺利用闪蒸焦耳加热和氯气，在数秒内从锂辉石矿石中提取氯化锂，纯度达 97%，产率达 94%。该方法无需硫酸焙烧，减少了废物排放。

rss · MIT Technology Review · May 28, 18:01

**背景**: 锂是电动汽车和储能所用锂离子电池的关键成分。目前，大部分锂从卤水或锂辉石等硬岩矿石中提取，但传统提取方法能耗高、产生大量废物且碳排放高。新方法旨在克服这些缺点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/28/1138096/lithium-extraction-rock-zero/">How a new extraction process could unlock the world’s lithium</a></li>
<li><a href="https://rockzero.com/">Rock Zero</a></li>
<li><a href="https://www.science.org/doi/10.1126/sciadv.ady6457">One-step separation of lithium from natural ores in seconds</a></li>

</ul>
</details>

**标签**: `#lithium`, `#battery technology`, `#energy storage`, `#materials science`, `#sustainability`

---

<a id="item-31"></a>
## [阻断 GPNMB 蛋白或能阻止帕金森病扩散](https://www.sciencedaily.com/releases/2026/05/260527023214.htm) ⭐️ 8.0/10

研究人员发现 GPNMB 蛋白是帕金森病扩散的关键驱动因素，并在早期实验中证明，阻断 GPNMB 的抗体可以阻止毒性过程在细胞间传播。 这一发现为帕金森病提供了潜在的新治疗靶点，目前该病缺乏能够阻止疾病进展的疗法。如果得到验证，靶向 GPNMB 的抗体疗法可能减缓或阻止数百万患者的神经退行性变。 研究发现，免疫细胞在应对受损神经元时会释放 GPNMB，形成加速脑细胞变性的恶性循环。阻断 GPNMB 的抗体在细胞模型中阻止了这种毒性传播，但仍需进一步的动物和人体试验。

rss · ScienceDaily Health · May 28, 07:12

**背景**: 帕金森病是一种进行性神经退行性疾病，其特征是错误折叠的α-突触核蛋白积聚，并能在神经元之间传播。GPNMB 是一种跨膜糖蛋白，参与多种细胞过程，此前其在帕金森病扩散中的作用尚不明确。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPNMB">GPNMB - Wikipedia</a></li>
<li><a href="https://scitechdaily.com/scientists-may-have-discovered-how-parkinsons-disease-spreads-through-the-brain/">Scientists May Have Discovered How Parkinson’s Disease ...</a></li>

</ul>
</details>

**标签**: `#Parkinson's disease`, `#neuroscience`, `#protein`, `#therapeutics`, `#biomedical research`

---

<a id="item-32"></a>
## [脑部扫描挑战长新冠炎症理论](https://www.sciencedaily.com/releases/2026/05/260527023206.htm) ⭐️ 8.0/10

一项新的脑成像研究发现，长新冠患者没有广泛性脑部炎症的证据；相反，严重症状与情绪相关脑区的活动增加有关。 这挑战了脑部炎症驱动长新冠的主流假说，可能将研究转向情绪和情感通路，并影响治疗方法。 该研究使用先进的 PET 成像测量炎症标志物，发现长新冠患者与健康对照组之间无显著差异。最严重的症状与杏仁核和前额叶皮层的过度活跃相关。

rss · ScienceDaily Health · May 28, 05:44

**背景**: 长新冠指急性 COVID-19 感染后持续数周或数月的症状。此前研究认为脑部炎症可能导致脑雾等认知问题，但这项新的影像学证据反驳了这一观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/05/260527023206.htm">Scientists thought brain inflammation was driving long COVID ...</a></li>
<li><a href="https://covidbrainstudy.umn.edu/">Neuroimaging in long COVID | COVID-BRAIN Project</a></li>
<li><a href="https://neurosciencenews.com/covid-flu-brain-fog-inflammation-30192/">COVID-19 Uniquely Rewires the Brain Compared to the Flu</a></li>

</ul>
</details>

**标签**: `#long COVID`, `#brain imaging`, `#inflammation`, `#neurology`, `#COVID-19`

---

<a id="item-33"></a>
## [隐藏的肠脑回路触发蛋白质渴望](https://www.sciencedaily.com/releases/2026/05/260527023202.htm) ⭐️ 8.0/10

研究人员发现了一个肠脑回路，当身体蛋白质不足时，它会向大脑发送信号，将渴望从糖转向必需氨基酸。 这一发现揭示了蛋白质渴望背后的直接生物机制，可能改变我们对食欲、营养和肥胖的理解。 这项在果蝇中进行的研究发现了一种肽激素，它能快速向大脑发出氨基酸缺乏的信号，同时抑制对糖的寻求行为。

rss · ScienceDaily Health · May 28, 04:35

**背景**: 肠脑轴是连接胃肠道和大脑的通信网络。先前研究表明，膳食氨基酸在肠道中被感知，触发激素释放向大脑发出信号。这项新研究确定了一个特定回路，直接控制对蛋白质而非糖的渴望。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/05/260527023202.htm">Scientists Discover Hidden Gut-brain Circuit That Triggers ...</a></li>
<li><a href="https://www.technologynetworks.com/neuroscience/news/your-gut-may-know-you-need-protein-before-your-brain-does-412953">Gut-Brain Pathway Controls Protein Cravings | Technology Networks</a></li>
<li><a href="https://www.earth.com/news/your-gut-can-steer-food-cravings-toward-missing-nutrients/">Your gut can steer food cravings toward missing nutrients</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#nutrition`, `#gut-brain axis`, `#obesity`, `#biology`

---