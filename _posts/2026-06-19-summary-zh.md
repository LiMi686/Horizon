---
layout: default
title: "Horizon Summary: 2026-06-19 (ZH)"
date: 2026-06-19
lang: zh
---

> From 105 items, 40 important content pieces were selected

---

1. [Roboflow 的 RF-DETR 实现实时检测 SOTA](#item-1) ⭐️ 9.0/10
2. [ITNet 统一 CNN、RNN 和 Transformer](#item-2) ⭐️ 9.0/10
3. [DeepSeek-V4 预览版：1.6T 参数 MoE 模型，支持百万 token 上下文](#item-3) ⭐️ 9.0/10
4. [ATProto 没有实例：一个协议类比](#item-4) ⭐️ 8.0/10
5. [Project Valhalla 历经十年终入 JDK 28](#item-5) ⭐️ 8.0/10
6. [EFF 呼吁免费公开法院记录](#item-6) ⭐️ 8.0/10
7. [业余研究者借助 AI 提出线形文字 A 破译方案](#item-7) ⭐️ 8.0/10
8. [谷歌发布 TimesFM 2.5 用于时间序列预测](#item-8) ⭐️ 8.0/10
9. [智谱 AI 发布 GLM-5 系列，支持百万上下文](#item-9) ⭐️ 8.0/10
10. [Codebase-Memory-MCP：毫秒级代码智能与知识图谱](#item-10) ⭐️ 8.0/10
11. [Lightricks 发布 LTX-2：开源音频-视频模型](#item-11) ⭐️ 8.0/10
12. [OpenMontage：首个开源智能视频制作系统](#item-12) ⭐️ 8.0/10
13. [面向自主 AI 系统的道义策略治理](#item-13) ⭐️ 8.0/10
14. [扩散语言模型的系统分析](#item-14) ⭐️ 8.0/10
15. [隐藏锚点解释多智能体 LLM 协商](#item-15) ⭐️ 8.0/10
16. [DeXposure-Claw：用于 DeFi 风险监管的智能体系统](#item-16) ⭐️ 8.0/10
17. [LLM 在临床数据上无法识别自身知识局限](#item-17) ⭐️ 8.0/10
18. [涌现对齐：LLM 通过内省实现伦理自我纠正](#item-18) ⭐️ 8.0/10
19. [计算可识别性：连接理论与实践](#item-19) ⭐️ 8.0/10
20. [Guard：多教师蒸馏实现鲁棒时间序列预测](#item-20) ⭐️ 8.0/10
21. [自对弈强化学习仅需 30 分钟人类数据即可超越模仿学习](#item-21) ⭐️ 8.0/10
22. [TreeTracer 通过随机路径可视化隐藏的 LLM 偏见](#item-22) ⭐️ 8.0/10
23. [LLM 微调收益源于任务对齐而非语言迁移](#item-23) ⭐️ 8.0/10
24. [新错误分类法揭示 LLM 在硬件设计中的局限](#item-24) ⭐️ 8.0/10
25. [扩散大语言模型中的位置偏差：分析与缓解](#item-25) ⭐️ 8.0/10
26. [因果归因剪枝在低稀疏度下提升大模型推理能力](#item-26) ⭐️ 8.0/10
27. [综述索引了涵盖 35 种语言的 120 个手语数据集](#item-27) ⭐️ 8.0/10
28. [自函数向量量化上下文学习中的偶然不确定性](#item-28) ⭐️ 8.0/10
29. [13 亿参数的胸部 X 光生成模型](#item-29) ⭐️ 8.0/10
30. [LooseControlVideo：用 3D 框实现直观视频控制](#item-30) ⭐️ 8.0/10
31. [ImageWAM：用图像编辑替代视频生成的世界动作模型](#item-31) ⭐️ 8.0/10
32. [LIVE：语言引导的可控视觉嵌入方法](#item-32) ⭐️ 8.0/10
33. [学习异步调度以加速扩散模型训练](#item-33) ⭐️ 8.0/10
34. [Stochastic Hi-Fi 将标量交互分解为独特性、冗余性和协同性](#item-34) ⭐️ 8.0/10
35. [无求解器训练方法用于预测后优化](#item-35) ⭐️ 8.0/10
36. [AURA：面向 LLM 评判的自适应不确定性感知精炼框架](#item-36) ⭐️ 8.0/10
37. [MDP 中 MNAR 奖励的缺失感知策略离线评估](#item-37) ⭐️ 8.0/10
38. [初创公司声称突破大语言模型瓶颈](#item-38) ⭐️ 8.0/10
39. [渐冻症患者成为首位长期脑机接口重度用户](#item-39) ⭐️ 8.0/10
40. [阿尔茨海默病触发机制或为淀粉样蛋白干扰 tau 蛋白](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Roboflow 的 RF-DETR 实现实时检测 SOTA](https://github.com/roboflow/rf-detr) ⭐️ 9.0/10

Roboflow 发布了 RF-DETR，这是一个实时目标检测与分割模型，在 COCO 基准上取得了最先进的结果，并被 ICLR 2026 接收。 RF-DETR 为实时检测设定了新的精度-延迟帕累托前沿，使其非常适合部署在自动驾驶和机器人等对延迟敏感的应用中。 RF-DETR 使用 DINOv2 视觉 Transformer 骨干网络，并在单一 API 中支持目标检测、实例分割和关键点检测；基础模型采用 Apache 2.0 许可证，而更大规模的变体需要商业许可证。

rss · GitHub Trending - Python · Jun 19, 22:49

**背景**: 目标检测模型传统上依赖卷积神经网络（如 YOLO），但 DETR 引入了基于 Transformer 的端到端方法。RF-DETR 在 DETR 基础上通过神经架构搜索优化精度和速度，面向实时应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/roboflow/rf-detr">GitHub - roboflow/rf-detr: RF-DETR is a real-time object detection and segmentation model architecture developed by Roboflow, SOTA on COCO, designed for fine-tuning. [ICLR 2026] · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2511.09554">[2511.09554] RF-DETR: Neural Architecture Search for Real-Time Detection Transformers</a></li>
<li><a href="https://learnopencv.com/rf-detr-object-detection/">RF-DETR by Roboflow: Fast Real-time Object Detection</a></li>

</ul>
</details>

**标签**: `#object detection`, `#computer vision`, `#deep learning`, `#real-time`, `#ICLR`

---

<a id="item-2"></a>
## [ITNet 统一 CNN、RNN 和 Transformer](https://arxiv.org/abs/2606.19538) ⭐️ 9.0/10

研究人员提出 ITNet，一种可学习的积分变换架构，将卷积、注意力和递归作为特例包含在内，在 ImageNet-1K、GLUE、ModelNet40、VQA v2 和 NLVR2 上取得了有竞争力的性能。 这项工作表明，CNN、RNN 和 Transformer 之间长期存在的分离并非根本性的，可能带来更简单、更通用的神经架构，能够从数据中自适应其归纳偏置。 ITNet 使用一个由 MLP 实现的可学习核来建模成对交互，并通过分块核融合、重要性加权蒙特卡洛积分和学习到的低秩分解来提高效率。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 卷积网络、递归网络和 Transformer 在数学上一直是具有不同归纳偏置的独立架构。积分变换是一种通过核将一个函数映射到另一个函数的数学操作，而可学习的积分变换允许从数据中学习核。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Integral_transform">Integral transform - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Inductive_bias">Inductive bias - Wikipedia</a></li>

</ul>
</details>

**标签**: `#deep learning`, `#neural architecture`, `#integral transform`, `#unified model`, `#arXiv`

---

<a id="item-3"></a>
## [DeepSeek-V4 预览版：1.6T 参数 MoE 模型，支持百万 token 上下文](https://arxiv.org/abs/2606.19348) ⭐️ 9.0/10

DeepSeek AI 发布了 DeepSeek-V4 预览版，包含两个 MoE 模型：DeepSeek-V4-Pro（总参数 1.6T，激活参数 49B）和 DeepSeek-V4-Flash（总参数 284B，激活参数 13B），均支持百万 token 上下文长度。该系列引入了压缩稀疏注意力（CSA）、重度压缩注意力（HCA）、流形约束超连接（mHC）和 Muon 优化器。 此次发布推动了开源大语言模型的前沿，在显著降低长上下文任务推理成本的同时实现了最先进的性能。百万 token 上下文能力使文档分析、多轮推理等长周期应用更加实用。 在百万 token 上下文设置下，DeepSeek-V4-Pro 的推理 FLOPs 仅为 DeepSeek-V3.2 的 27%，KV 缓存仅为 10%。模型在超过 32 万亿 token 上进行了预训练，并已在 Hugging Face 上发布。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 混合专家（MoE）模型每个 token 仅激活部分参数，从而在可控计算量下实现大总参数量。长上下文注意力传统上因二次复杂度而代价高昂；CSA 和 HCA 通过压缩键值条目并对压缩表示使用稀疏或密集注意力来降低开销。超连接增强了残差流的表达能力，Muon 优化器加速了训练收敛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dasroot.net/posts/2026/04/deepseek-v4-hybrid-attention-massive-contexts/">Inside DeepSeek V4: Hybrid Attention for Massive Contexts · Technical news about AI, coding and all</a></li>
<li><a href="https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/">DeepSeek AI Releases DeepSeek-V4: Compressed Sparse Attention and Heavily Compressed Attention Enable One-Million-Token Contexts - MarkTechPost</a></li>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections</a></li>

</ul>
</details>

**标签**: `#large language models`, `#mixture-of-experts`, `#long-context`, `#deep learning`, `#AI research`

---

<a id="item-4"></a>
## [ATProto 没有实例：一个协议类比](https://overreacted.io/there-are-no-instances-in-atproto/) ⭐️ 8.0/10

Dan Abramov 发表了一篇文章，解释 ATProto（Bluesky 背后的协议）没有像 Mastodon 那样的“实例”概念，并用 RSS 和电子邮件类比来阐明其架构。 这一澄清解决了去中心化社交媒体领域的一个常见误解，帮助开发者和用户理解 ATProto 与 ActivityPub 之间的根本架构差异，这会影响审核、托管和联邦机制的工作方式。 在 ATProto 中，个人数据服务器（PDS）、中继（Relay）和应用视图（AppView）是独立的服务，而 Mastodon 中每个实例捆绑了所有功能。这种分离允许独立扩展，并避免了 Mastodon 中出现的“去联邦”问题。

hackernews · danabramov · Jun 19, 15:10 · [社区讨论](https://news.ycombinator.com/item?id=48599515)

**背景**: ATProto（认证传输协议）是一种用于社交网络的去中心化协议，被 Bluesky 使用。ActivityPub 是 Mastodon 和 Fediverse 背后的协议。在 Mastodon 中，每个服务器（实例）托管用户数据、处理联邦并提供用户界面，导致服务器锁定和去联邦等问题。ATProto 将这些关注点分离为不同的服务：PDS 用于用户数据，Relay 用于数据流，AppView 用于应用逻辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://atproto.com/guides/overview">Protocol Overview - AT Protocol</a></li>
<li><a href="https://en.wikipedia.org/wiki/AT_Protocol">AT Protocol - Wikipedia</a></li>
<li><a href="https://atproto.com/guides/understanding-atproto">Understanding Atproto - AT Protocol Docs - AT Protocol</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论讨论了 RSS 类比的准确性，一些人认为 RSS 对中心化服务的依赖程度低于 ATProto 的 Relay。其他人则欣赏对架构差异的清晰解释，但认为文章淡化了实例解决的审核挑战。

**标签**: `#ATProto`, `#ActivityPub`, `#decentralization`, `#Bluesky`, `#protocol design`

---

<a id="item-5"></a>
## [Project Valhalla 历经十年终入 JDK 28](https://www.jvm-weekly.com/p/project-valhalla-explained-how-a) ⭐️ 8.0/10

Project Valhalla 在 JDK 28 中为 JVM 引入了值类型和堆扁平化，使 JVM 能够将值对象直接存储在数组中，无需对象头或指针，从而提升内存密度和性能。 这是一项重大的 JVM 增强，弥合了面向对象表达性与底层性能之间的差距，使 Java 应用受益于更小的内存占用和更快的访问模式，尤其在数据密集型领域。 值类型（内联类）是无标识的对象，可以在数组和字段中被扁平化，但堆扁平化仅限于表示不超过 64 位的对象；更大的值类型仍需间接访问。

hackernews · philonoist · Jun 19, 06:35 · [社区讨论](https://news.ycombinator.com/item?id=48595511)

**背景**: Project Valhalla 是 2014 年 7 月宣布的实验性 OpenJDK 项目，由 Brian Goetz 领导，旨在为 Java 引入值类型。传统上，所有 Java 对象都有标识并通过引用访问，导致内存开销和间接性。值类型移除标识，使 JVM 能够像基本类型一样内联存储它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Project_Valhalla_(Java_language)">Project Valhalla (Java language) - Wikipedia</a></li>
<li><a href="https://medium.com/@vishalpriyadarshi/project-valhalla-bringing-value-types-and-performance-efficiency-to-java-83b85e00b791">Project Valhalla : Bringing Value Types and Performance... | Medium</a></li>
<li><a href="https://inside.java/2025/10/31/jvmls-jep-401/">Value Classes Heap Flattening - What to expect from JEP 401 #JVMLS</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些人赞赏性能提升，但批评复杂性和可读性成本，例如值类型破坏了统一性原则（如赋值语义在值类和引用类之间不同）。另一些人则捍卫 JVM 的演进，指出许多批评者持有对 Java 的过时看法。

**标签**: `#Java`, `#JVM`, `#Project Valhalla`, `#performance`, `#language design`

---

<a id="item-6"></a>
## [EFF 呼吁免费公开法院记录](https://www.eff.org/deeplinks/2026/06/court-records-should-be-free) ⭐️ 8.0/10

电子前哨基金会（EFF）主张公共法院记录应免费，批评当前按页收费的 PACER 系统，并支持立法创建现代化的免费访问平台。 这很重要，因为公众获取法院记录是透明度和正义的基础；当前的费用对个人和组织造成了障碍，破坏了法律应免费获取的原则。 PACER 每页收费 0.10 美元（每份文件上限 3 美元），但州系统可能更贵，例如爱达荷州每页收费 10 美元。拟议法案将用现代化的统一平台取代 PACER 和 CM/ECF。

hackernews · hn_acker · Jun 19, 17:34 · [社区讨论](https://news.ycombinator.com/item?id=48600946)

**背景**: PACER（公共法院电子记录访问系统）是一个提供联邦法院电子记录访问的系统，但用户需按页付费。EFF 是一个倡导在线公民自由的数字权利组织。CourtListener 和 RECAP 是众包 PACER 文档的免费工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Electronic_Frontier_Foundation">Electronic Frontier Foundation - Wikipedia</a></li>
<li><a href="https://pacer.uscourts.gov/register-account">Register for an Account | PACER : Federal Court Records</a></li>

</ul>
</details>

**社区讨论**: 评论者对高昂的费用表示不满，尤其是在州法院（例如爱达荷州每页 10 美元）。他们称赞 CourtListener 和 RECAP 是重要的临时解决方案，并希望拟议的立法能使其过时。

**标签**: `#legal tech`, `#public access`, `#government transparency`, `#PACER`, `#EFF`

---

<a id="item-7"></a>
## [业余研究者借助 AI 提出线形文字 A 破译方案](https://aiclambake.com/clamtakes/linear-a/) ⭐️ 8.0/10

业余研究者 Tom Di Mino 使用 Anthropic 的 Claude Code AI 工具构建 Python 脚本分析线形文字 A 语料库，提出破译方案，将该文字与一种已灭绝的闪米特语联系起来。据报道他已翻译了 300 多个单词，这是前所未有的成就。 如果得到验证，这将是线形文字 A 首次成功破译，该文字一个多世纪以来一直未被解读，可能改写我们对米诺斯文明及其语言的理解。这也展示了 AI 工具在历史语言学和铭文学中的新颖应用。 破译工作依赖于线形文字 A 中研究最多的重复短语“奠酒公式”，并使用 Claude Code 大规模系统测试假设。该研究目前正在接受罗格斯大学和剑桥大学语言学专家的评审。

hackernews · Kosturdistan · Jun 19, 16:04 · [社区讨论](https://news.ycombinator.com/item?id=48600107)

**背景**: 线形文字 A 是米诺斯人在公元前 1800 年至 1450 年间在克里特岛使用的文字系统，自 1900 年重新发现以来一直未被破译。它与线形文字 B 共享许多字形，后者于 20 世纪 50 年代被破译，发现代表迈锡尼希腊语。线形文字 A 的语料库极其零碎，只有少量较长的文本，使得破译极具挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Linear_A_script">Linear A script</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>

</ul>
</details>

**社区讨论**: 社区持谨慎乐观态度，许多人注意到该方法的合理性和所达到的翻译规模。一些评论者强调该工作正在接受专家评审，增加了可信度，而另一些人则因过去关于线形文字 A 的未经证实的说法而表示怀疑。Claude Code 被用于构建工具而非黑箱求解的做法受到赞扬。

**标签**: `#Linear A`, `#AI`, `#decipherment`, `#archaeology`, `#Claude Code`

---

<a id="item-8"></a>
## [谷歌发布 TimesFM 2.5 用于时间序列预测](https://github.com/google-research/timesfm) ⭐️ 8.0/10

谷歌研究发布了 TimesFM 2.5，这是一个用于时间序列预测的预训练基础模型，其检查点可在 Hugging Face 上获取，并与 BigQuery ML、Google Sheets 和 Vertex Model Garden 集成。 TimesFM 提供了一个单一的预训练模型，能够以零样本性能预测多样化的时间序列数据，减少了对定制模型的需求，并推动了 AI 驱动预测在企业及生产力工具中的广泛应用。 TimesFM 2.5 使用 2 亿参数（从 5 亿减少），支持高达 16k 的上下文长度，并通过可选的 3000 万分位数头提供长达 1k 范围的连续分位数预测。它还移除了频率指示器并增加了新的预测标志。

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**背景**: 时间序列预测基于历史数据预测未来值，用于金融、天气和库存管理。基础模型是大型预训练模型，可通过少量微调适应多种任务。TimesFM 是一个仅解码器的 Transformer 模型，在 1000 亿个真实世界时间点上训练而成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google-research/timesfm">GitHub - google-research/timesfm: TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting. · GitHub</a></li>
<li><a href="https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/">A decoder - only foundation model for time - series forecasting</a></li>
<li><a href="https://arxiv.org/abs/2310.10688">A decoder - only foundation model for time - series forecasting</a></li>

</ul>
</details>

**社区讨论**: 社区积极为 TimesFM 做出贡献，特别感谢@kashif 和@darkpowerxo 提供了微调示例和单元测试，以及@borealBytes 添加了代理支持。GitHub 仓库显示了持续的参与和协作改进。

**标签**: `#time-series`, `#foundation model`, `#forecasting`, `#Google Research`, `#ICML 2024`

---

<a id="item-9"></a>
## [智谱 AI 发布 GLM-5 系列，支持百万上下文](https://github.com/zai-org/GLM-5) ⭐️ 8.0/10

智谱 AI（通过 zai-org）发布了 GLM-5 模型系列，包括 GLM-5.2、GLM-5.1 和 GLM-5，其中 GLM-5.2 支持稳定的百万 token 上下文，并在编码基准测试上取得显著提升。 此次发布提升了长周期任务能力，使 AI 智能体能够在扩展上下文中处理复杂的多步骤工作流，这对实际软件工程和自主系统至关重要。 GLM-5.2 采用 IndexShare 技术，在百万上下文下将每 token 的 FLOPs 降低 2.9 倍，并在 Terminal-Bench 2.1 上达到 81.0 分，接近 Claude Opus 4.8 的 85.0 分。该模型系列参数规模从 355B 扩展到 744B，采用 MoE 架构。

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**背景**: 长周期任务要求 AI 在多步骤中规划和执行，通常需要长上下文窗口。GLM-5 系列基于智谱之前的 GLM 模型，面向智能体工程和复杂编码任务。这些模型是开源的，可在 Hugging Face 上获取。

**标签**: `#AI`, `#LLM`, `#GLM`, `#machine learning`, `#model release`

---

<a id="item-10"></a>
## [Codebase-Memory-MCP：毫秒级代码智能与知识图谱](https://github.com/DeusData/codebase-memory-mcp) ⭐️ 8.0/10

DeusData 发布了 codebase-memory-mcp，一个高性能 MCP 服务器，可将整个代码库索引为持久化知识图谱，实现亚毫秒级查询，并通过 tree-sitter AST 分析支持 158 种语言。 该工具大幅减少了 AI 编码助手的 token 使用量和工具调用次数，实现更快、更准确的代码理解，有望显著提升开发者生产力和 AI 辅助代码导航。 它能在 3 分钟内索引 Linux 内核（2800 万行代码，7.5 万个文件），在 1 毫秒内回答结构查询，并以零依赖的单一静态二进制文件形式发布，支持 macOS、Linux 和 Windows。

rss · GitHub Trending - Daily (All) · Jun 19, 22:49

**背景**: MCP（模型上下文协议）是一种允许 AI 模型与外部工具和数据源交互的协议。知识图谱表示代码实体（函数、类）及其关系，无需扫描文件即可高效查询。Tree-sitter 是一个解析器生成工具，可为多种语言提供快速增量解析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/DeusData/codebase-memory-mcp">GitHub - DeusData/ codebase -memory-mcp: High-performance code ...</a></li>
<li><a href="https://codegraph.codes/">CodeGraph — Code Knowledge Graph for Claude Code & Cursor</a></li>
<li><a href="https://lobehub.com/mcp/eviking-codekg">codeKG — Codebase Knowledge Graph | ... · LobeHub</a></li>

</ul>
</details>

**标签**: `#code intelligence`, `#MCP server`, `#knowledge graph`, `#developer tools`, `#open source`

---

<a id="item-11"></a>
## [Lightricks 发布 LTX-2：开源音频-视频模型](https://github.com/Lightricks/LTX-2) ⭐️ 8.0/10

Lightricks 发布了 LTX-2 的官方 Python 包，支持推理和 LoRA 训练，并在 HuggingFace 上提供了模型检查点。 LTX-2 是首个基于 DiT 的音频-视频基础模型，将同步音频与视频、高保真度和多种性能模式集成于一个开源包中，有望推动高级视频生成的普及。 该模型拥有 220 亿参数，并包含用于两阶段管道的空间上采样器；支持文本到视频、图像到视频和音频到视频生成。

rss · GitHub Trending - Python · Jun 19, 22:49

**背景**: DiT（扩散变换器）是一类将扩散过程与变换器架构相结合的生成模型，能够生成高质量视频。LoRA（低秩适应）是一种轻量级微调技术，可减少可训练参数，便于将大型模型适配到特定任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Lightricks/LTX-2">GitHub - Lightricks/ LTX - 2 : Official Python inference and LoRA trainer...</a></li>
<li><a href="https://www.ynetnews.com/tech-and-digital/article/hklbzavrgx">Lightricks unveils powerful AI video model challenging OpenAI and...</a></li>
<li><a href="https://huggingface.co/docs/diffusers/training/lora">LoRA · Hugging Face</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#video generation`, `#audio-video model`, `#LoRA`, `#open source`

---

<a id="item-12"></a>
## [OpenMontage：首个开源智能视频制作系统](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage 作为全球首个开源智能视频制作系统正式发布，包含 12 条流水线、52 个工具和 500 多项智能体技能，让 AI 编程助手能够根据自然语言描述制作完整视频。 该项目通过提供免费开源方案，打破了专有系统的垄断，有望为个人和小团队的内容创作带来革命性变化。 OpenMontage 能够利用免费素材库和开放档案制作真正的视频，而不仅仅是基于图片的动画。它支持多种 AI 提供商，制作一部 60 秒动画短片成本低至 1.33 美元。

rss · GitHub Trending - Python · Jun 19, 22:49

**背景**: 智能视频制作系统利用 AI 智能体自主处理脚本编写、素材生成、剪辑和合成等任务。OpenMontage 是首个此类开源系统，与闭源商业工具形成对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/ OpenMontage : World's first open -source, agentic...</a></li>
<li><a href="https://openalt.pro/en/tools/openmontage-6d3bd03b">OpenMontage — Video AI Tool | OpenAlt</a></li>
<li><a href="https://www.scriptbyai.com/open-ai-video-production-agent/">Free AI Video Production Agent with Real-Footage Pipelines ...</a></li>

</ul>
</details>

**标签**: `#open-source`, `#video production`, `#AI agents`, `#tooling`, `#generative AI`

---

<a id="item-13"></a>
## [面向自主 AI 系统的道义策略治理](https://arxiv.org/abs/2606.19464) ⭐️ 8.0/10

一篇新论文提出了 AgenticRei，这是一个道义策略框架，超越了传统的访问控制，用于治理 LLM 驱动的自主 AI 系统，包含了义务、禁止、豁免和冲突解决。 这填补了 AI 治理中的一个关键空白，因为当前的策略引擎如 XACML、Rego 和 Cedar 无法处理义务生命周期管理或元策略冲突，而这些对于自主系统中的企业安全、隐私和合规至关重要。 AgenticRei 使用基于 Rei 框架构建的道义策略语言，以 OWL（Web 本体语言）表达，并由 LLM 外部的高性能逻辑引擎在运行时评估。它同时管理工具调用和智能体间消息，并与 A2AS 等行业框架兼容。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 道义逻辑是逻辑学的一个分支，涉及义务、许可和禁止。当前 AI 系统的策略引擎主要关注授权（允许/拒绝），缺乏对随时间管理义务或解决策略冲突的支持。自主 AI 系统能够自主调用工具并与其他智能体协调，需要更全面的治理来确保安全和合规。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2501.05765v1">Deontic Temporal Logic for Formal Verification of AI Ethics - arXiv</a></li>
<li><a href="https://ebiquity.umbc.edu/paper/html/id/1221/Deontic-Policies-for-Runtime-Governance-of-Agentic-AI-Systems">Deontic Policies for Runtime Governance of Agentic AI Systems</a></li>
<li><a href="https://github.com/XMPro/Multi-Agent/blob/main/docs/concepts/deontic-principles.md">Deontic Principles: Rules of Engagement for Agents - GitHub</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#LLM agents`, `#deontic logic`, `#policy engines`, `#security`

---

<a id="item-14"></a>
## [扩散语言模型的系统分析](https://arxiv.org/abs/2606.19475) ⭐️ 8.0/10

一篇新论文对八种最先进的扩散语言模型（DLM）在涵盖推理、编程、翻译等任务的八个基准上进行了系统实验评估，分析了生成质量和计算效率。 这项研究提供了亟需的 DLM 标准化比较，帮助研究人员和从业者理解这一新兴范式的性能-效率权衡，可能影响未来模型设计和部署决策。 分析包括八种 DLM，并考察了去噪步数、上下文长度、块大小和并行解掩策略等推理时因素的影响，还对在相同条件下训练的较小模型进行了受控比较。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 像 GPT-4 这样的大型语言模型通常以自回归方式生成文本，一次预测一个 token。扩散语言模型（DLM）提供了一种替代方案，通过迭代去噪生成文本，从随机噪声开始并行逐步优化整个序列。这种方法可能提高效率并实现双向上下文，但一直缺乏系统比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://breynald.github.io/2025/03/10/dllm/">Diffusion Language Model : The Rise of a New... - Breynald Shelter</a></li>
<li><a href="https://arxiv.org/pdf/2508.10875">A Survey on Diffusion Language Models</a></li>

</ul>
</details>

**标签**: `#diffusion language models`, `#LLMs`, `#experimental analysis`, `#natural language processing`, `#machine learning`

---

<a id="item-15"></a>
## [隐藏锚点解释多智能体 LLM 协商](https://arxiv.org/abs/2606.19494) ⭐️ 8.0/10

一篇新论文将多智能体 LLM 协商建模为一个动力系统，其中每个智能体都有一个隐藏的内部信念（锚点）牵引其观点，解释了信心如何超越初始信念——这是 DeGroot 或 Friedkin-Johnsen 等经典模型未能捕捉的现象。 这项工作为理解和改进多智能体 LLM 推理系统提供了理论基础，揭示了协商可以产生超出初始观点凸包的结果，这对设计更有效的 AI 协作协议具有重要意义。 作者表明，仅从协商数据中即可恢复隐藏锚点，并且通过检验恢复的锚点是否能预测未参与运行的协商结果，可以简单判断行为是否由锚点驱动。在三个开放权重模型系列中，锚点影响力同样强，但锚点位置不同，只有当锚点远离初始观点时，协商才会逃出凸包。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 经典观点动力学模型如 DeGroot 和 Friedkin-Johnsen 描述了智能体如何通过社会影响收敛观点，但假设观点保持在初始信念的凸包内。凸包是包含所有初始观点点的最小凸多边形。本文引入了隐藏锚点——一种持久的内部信念——使观点能够逃出该凸包，这与多智能体 LLM 系统中观察到的行为一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2603.10756">A Survey on Algorithmic Interventions in Opinion Dynamics</a></li>
<li><a href="https://arxiv.org/abs/2407.10680">Friedkin - Johnsen Model for Opinion Dynamics on Signed Graphs</a></li>
<li><a href="https://www.researchgate.net/publication/321752941_Steering_opinion_dynamics_via_containment_control">(PDF) Steering opinion dynamics via containment control</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#LLM deliberation`, `#opinion dynamics`, `#AI reasoning`, `#mathematical modeling`

---

<a id="item-16"></a>
## [DeXposure-Claw：用于 DeFi 风险监管的智能体系统](https://arxiv.org/abs/2606.19501) ⭐️ 8.0/10

研究人员推出了 DeXposure-Claw，这是一个结合图时间序列预测与基于 LLM 的推理的智能体系统，为去中心化金融（DeFi）提供可审计的风险监管。他们还发布了 DeXposure-Bench，一个与监管标准对齐的六轴评估基准。 这项工作通过提供一个结构化、可审计的框架，减少了 LLM 智能体的误报，填补了 DeFi 风险监管的关键空白。它可能为可靠的 AI 驱动金融监管树立新标准，使监管机构和 DeFi 平台都受益。 该系统使用 DeXposure-FM（一个图时间序列基础模型）来预测风险敞口网络，然后应用确定性监控和置信度门控，最后生成监管票据。在五年真实数据上的实验证明了其有效性。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 去中心化金融（DeFi）涉及跨互联网络的复杂、快速变化的信用风险。通用 LLM 智能体常常过度解读微弱证据并推荐高风险干预措施，而现有评估缺乏与监管对齐的指标。DeXposure-Claw 通过将 LLM 决策路由到结构化证据和显式误报率约束来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.19501">DeXposure-Claw: An Agentic System for DeFi Risk Supervision</a></li>

</ul>
</details>

**标签**: `#DeFi`, `#LLM Agents`, `#Risk Supervision`, `#Graph Neural Networks`, `#Financial AI`

---

<a id="item-17"></a>
## [LLM 在临床数据上无法识别自身知识局限](https://arxiv.org/abs/2606.19509) ⭐️ 8.0/10

一项新研究发现，LLM 在临床表格数据上表现出认知空洞的置信度，无论准确率如何都输出近乎恒定的置信度，并提出了跨模型归因分歧来检测此类盲点。 这项工作揭示了 LLM 在医疗等高风险领域中置信度校准的关键缺陷，而可靠的 uncertainty 估计对于安全部署至关重要。 该研究在临床预测任务上比较了 Qwen 2.5 7B 和 XGBoost，发现 LLM 的置信度跟随提示格式而非准确率，并且将少样本示例与 SHAP 特征证据结合可将归因分歧从 1.54 降至 0.38，准确率从 49% 提升至 75.3%。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 认知不确定性（epistemic uncertainty）指因知识缺乏而产生的不确定性，区别于来自固有随机性的偶然不确定性（aleatoric uncertainty）。SHAP 是一种通过为每个特征分配重要性来解释模型预测的方法。跨模型归因分歧衡量模型间特征归因的不一致程度，可指示认知盲点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ethanlazuk.com/blog/hamsterdam-research-epistemic-aleatoric-uncertainty/">Epistemic vs. Aleatoric Uncertainty in LLMs & Why... - Ethan Lazuk</a></li>
<li><a href="https://www.emergentmind.com/papers/2406.02543">LLM Uncertainty : Quantifying and Preventing Hallucinations</a></li>

</ul>
</details>

**标签**: `#LLM`, `#epistemic uncertainty`, `#clinical data`, `#attribution divergence`, `#confidence calibration`

---

<a id="item-18"></a>
## [涌现对齐：LLM 通过内省实现伦理自我纠正](https://arxiv.org/abs/2606.19527) ⭐️ 8.0/10

该论文提出了涌现对齐方法，通过添加内省良知步骤并结合直接偏好优化（DPO）训练，使 LLM 能够自我纠正伦理偏差，无需外部评判器。 这解决了微调可能导致广泛不道德行为的涌现失调问题，提供了一种可扩展的自我对齐技术，无需依赖更弱或更强的模型即可增强 AI 安全性。 该方法使用 LLM 自身的冻结副本作为评判器，并通过基于 DPO 的对齐组件扩展训练损失，在训练、微调、对抗性提示和零样本学习场景中均有效。

rss · arXiv - AI · Jun 19, 04:00

**背景**: 大型语言模型（LLM）可能表现出涌现失调——即通过窄域微调产生的不道德行为，这在先前工作中已有展示。直接偏好优化（DPO）是一种通过在偏好对上进行训练来对齐模型与人类偏好、无需独立奖励模型的技术。涌现对齐利用 DPO 和一个内省步骤引导模型远离不道德输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.17424">[2502.17424] Emergent Misalignment: Narrow finetuning can produce...</a></li>
<li><a href="https://huggingface.co/learn/smol-course/unit2/3">Hands-On Exercise: Direct Preference Optimization with...</a></li>

</ul>
</details>

**标签**: `#LLM alignment`, `#AI safety`, `#Direct Preference Optimization`, `#emergent behavior`, `#self-correction`

---

<a id="item-19"></a>
## [计算可识别性：连接理论与实践](https://arxiv.org/abs/2606.19361) ⭐️ 8.0/10

本文提出了“计算可识别性”这一新框架，用有限计算搜索过程替代理论可识别性的渐近假设，在指定误差容限内寻找经验估计量。 该框架将可识别性定义为存在一个有限搜索过程，能在误差容限内找到经验估计量，且依赖于先验分布和搜索过程本身。实验展示了其在小样本、模糊图结构、混合观测-干预数据以及反事实估计量上的有效性。

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**背景**: 因果识别确定是否可以从观测数据和假设中唯一计算因果效应。传统的理论可识别性假设无限数据和渐近性质，在实践中常常不成立。本文提出了一种受计算约束的替代方案，适用于有限样本和计算限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19361">Computational Identifiability</a></li>
<li><a href="https://lmyint.github.io/causal_fall_2024/02-identification.html">Causal identification : building intuition – STAT 451</a></li>
<li><a href="https://stats.stackexchange.com/questions/552882/why-do-we-need-identification-in-causal-inference">causality - Why do we need identification in causal inference ?</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#identifiability`, `#computational complexity`, `#machine learning`, `#statistics`

---

<a id="item-20"></a>
## [Guard：多教师蒸馏实现鲁棒时间序列预测](https://arxiv.org/abs/2606.19363) ⭐️ 8.0/10

研究人员提出 Guard 框架，这是一种多教师蒸馏方法，能动态选择并适配基础模型，训练出轻量且鲁棒的科学时间序列预测器，相比固定权重基线显著降低 RMSE。 该工作解决了大型时间序列基础模型丰富知识与计算成本及领域错位之间的关键矛盾，使得在资源受限的边缘设备上实现高精度科学预测成为可能。 Guard 使用上下文路由器为每个实例选择最佳教师，并采用不确定性门控温度机制，在教师置信度与领域现实不符时减弱蒸馏强度。在最难的实例中，有 28.5%优于全局最优的基础模型。

rss · arXiv - Machine Learning · Jun 19, 04:00

**背景**: 时间序列基础模型（TSFM）是预训练模型，能捕捉通用时间动态，但在零样本应用于特定科学领域时经常出现分布错位。知识蒸馏将知识从大型教师模型转移到小型学生模型，但多教师蒸馏通常使用固定权重，忽略了实例级别的教师质量。Guard 引入了自适应路由和不确定性感知门控来克服这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19363">[2606.19363] When to Trust, How to Distill : Multi -Foundation Model...</a></li>

</ul>
</details>

**标签**: `#time-series forecasting`, `#foundation models`, `#knowledge distillation`, `#scientific computing`, `#edge AI`

---

<a id="item-21"></a>
## [自对弈强化学习仅需 30 分钟人类数据即可超越模仿学习](https://arxiv.org/abs/2606.19370) ⭐️ 8.0/10

研究人员开发了一种方法，将自对弈强化学习与仅 30 分钟的人类驾驶演示作为正则化目标相结合，生成的驾驶策略能够与人类驾驶员有效协调，所用人类数据仅为模仿学习的 1/2500。 该方法大幅减少了自动驾驶中对昂贵人类数据的需求，解决了扩展自动驾驶技术的关键瓶颈。同时解决了纯自对弈策略的行为不对齐问题，使其与人类驾驶员兼容。 该方法使用最小安全目标到达奖励加上人类演示的正则化项，训练在单个消费级 GPU 上 15 小时完成。生成的策略在保留的人类轨迹上评估，显示出有效的协调能力。

rss · arXiv - Machine Learning · Jun 19, 04:00

**背景**: 自对弈强化学习通过让智能体在模拟中与自己博弈来训练，实现无需人类数据的廉价大规模训练。然而，纯自对弈常导致与人类不兼容的怪异驾驶习惯。模仿学习则需要大量人类演示（例如 1250 小时）才能达到类似性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-driving_car">Self- driving car - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#autonomous driving`, `#self-play`, `#human-in-the-loop`, `#behavioral alignment`

---

<a id="item-22"></a>
## [TreeTracer 通过随机路径可视化隐藏的 LLM 偏见](https://arxiv.org/abs/2606.19344) ⭐️ 8.0/10

研究人员推出了 TreeTracer，一种可视化分析工具，它将数百次随机 LLM 生成聚合成语法对齐的层次结构，并通过自定义 Sankey 图进行可视化，以揭示隐藏的偏见。该工具通过比较 GPT-2 XL 与符合宪法对齐的 Apertus 模型进行了验证，揭示了诸如反事实代词抑制等偏见。 这项工作通过聚合比较使隐藏的偏见变得可见，减少了分析人员的认知负担，并支持系统性偏见检测，从而解决了 LLM 审计中的一个关键空白。它对 AI 公平性研究和更公平语言模型的开发具有很高的潜在影响。 TreeTracer 使用扰动分析流程，替换提示中本体定义的术语，将随机生成聚合成语法对齐的树，并通过辅助语言模型进行分类感知的节点合并。该系统还应用对比推理来计算和显示反事实令牌概率，降低误解风险。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 大型语言模型（LLM）随机生成文本，这使得检测可能仅出现在低概率输出中的偏见变得困难。标准审计方法依赖于单一输出或静态指标，会遗漏隐藏的偏见。TreeTracer 通过聚合多次生成来通过视觉比较揭示这些偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19344">Visualizing Hidden LLM Bias through Stochastic Path Aggregation - arXiv</a></li>
<li><a href="https://arxiv.org/html/2606.19344v1">Visualizing Hidden LLM Bias through Stochastic Path Aggregation - arXiv</a></li>

</ul>
</details>

**标签**: `#LLM bias`, `#visual analytics`, `#AI fairness`, `#natural language processing`, `#explainability`

---

<a id="item-23"></a>
## [LLM 微调收益源于任务对齐而非语言迁移](https://arxiv.org/abs/2606.19346) ⭐️ 8.0/10

一项新研究在阿拉伯语上微调了七个大语言模型（4B–671B 参数），未发现闪语族特有的零样本迁移证据；所有语言的改进表明收益来自任务对齐而非跨语言语言关联性。 这挑战了 LLM 跨语言迁移依赖于语言相似性的常见假设，对多语言 NLP 训练策略和资源分配具有启示意义。 该研究测试了密集和混合专家架构，思维链消融实验表明，从微调中受益最大的模型也从推理时推理中同等受益，强化了任务对齐的解释。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 零样本跨语言迁移指模型在一种语言上训练后无需额外微调即可在另一种语言上表现良好。混合专家（MoE）架构使用路由器仅为每个 token 激活相关子网络，实现大容量低计算。思维链提示通过生成中间步骤来改进推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/aimstack/aim-and-mlflow-choosing-experiment-tracker-for-zero-shot-cross-lingual-transfer-4bad0a199fc7">Aim and MLflow — Choosing Experiment Tracker for Zero - Shot ...</a></li>
<li><a href="https://www.linkedin.com/posts/amjad-amireh-99822032_mixture-of-experts-moe-mixture-of-experts-activity-7456401344376176640-hXBj">Mixture of Experts AI Architecture for Efficient Language ... | LinkedIn</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**标签**: `#cross-lingual transfer`, `#large language models`, `#NLP`, `#fine-tuning`, `#multilingual`

---

<a id="item-24"></a>
## [新错误分类法揭示 LLM 在硬件设计中的局限](https://arxiv.org/abs/2606.19347) ⭐️ 8.0/10

一篇新论文提出了针对 LLM 生成的硬件设计代码的错误分类法，将失败分为语法、语义、可解功能和不可解功能类型，并揭示前沿模型在 VerilogEval 基准测试中因不可解功能错误而停滞在 90.8%的通过率。 这项工作指出了将 LLM 应用于硬件设计的关键瓶颈，表明对齐技术仅教会模型编译而非推理，这对 AI 辅助工程和更强大模型的开发具有重要意义。 论文揭示了“表面收敛差距”，即优化修复语法错误实际上会加剧更深层的功能失败，并发现重复采样可以修补可解错误，但 RTL 编码能力仍受预训练知识限制。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: RTL（寄存器传输级）编码是使用 Verilog 等硬件描述语言描述数字电路的方法。LLM 在生成代码方面显示出潜力，但在硬件设计所需的并行时序逻辑上存在困难。VerilogEval 基准测试是评估 LLM 在 Verilog 代码补全任务上性能的标准框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2408.11053v2">Revisiting VerilogEval : A Year of Improvements in Large-Language...</a></li>
<li><a href="https://github.com/NVlabs/verilog-eval">GitHub - NVlabs/ verilog - eval : Verilog evaluation benchmark for large...</a></li>
<li><a href="https://www.linkedin.com/pulse/accelerating-rtl-design-agentic-ai-multi-agent-llm-driven-y80uc">Accelerating RTL Design with Agentic AI: A Multi-Agent LLM-Driven...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#hardware design`, `#error taxonomy`, `#Verilog`, `#AI generalization`

---

<a id="item-25"></a>
## [扩散大语言模型中的位置偏差：分析与缓解](https://arxiv.org/abs/2606.19349) ⭐️ 8.0/10

该论文揭示了查询位置因空间近因效应显著影响扩散大语言模型中的上下文学习，并提出了一种名为 Auto-ICL 的无标签缓解方法。 这一发现挑战了从自回归模型继承的传统尾部查询模板，提出的 Auto-ICL 方法无需真实标签即可提升生成质量，将影响未来 dLLM 的设计与部署。 作者通过实验将位置方差与示例语义质量解耦，表明两者影响相当。他们引入平均置信度（C̄）来跟踪迭代解码动态，该指标在 dLLM 中优于传统的单步置信度。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 扩散大语言模型（dLLMs）是一种非自回归范式，通过迭代去噪生成文本，提供双向上下文和并行解码。与具有因果掩码的自回归 LLM 不同，dLLM 允许灵活的查询放置，但当前实践常使用尾部查询模板，未考虑这一灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://koshurai.medium.com/diffusion-large-language-models-dllms-a-paradigm-shift-in-ai-e4aa3b71f298">Diffusion Large Language Models ( dLLMs ): A Paradigm... | Medium</a></li>
<li><a href="https://intuitionlabs.ai/articles/llm-position-bias-primacy-recency-effects">LLM Position Bias: Primacy and Recency Effects in ... | IntuitionLabs</a></li>
<li><a href="https://www.researchgate.net/publication/395034818_Diffusion_Language_Models_Know_the_Answer_Before_Decoding">(PDF) Diffusion Language Models Know the Answer Before Decoding</a></li>

</ul>
</details>

**标签**: `#Diffusion LLMs`, `#In-Context Learning`, `#Positional Bias`, `#Decoding Dynamics`, `#Attention Mechanism`

---

<a id="item-26"></a>
## [因果归因剪枝在低稀疏度下提升大模型推理能力](https://arxiv.org/abs/2606.19350) ⭐️ 8.0/10

研究人员提出因果归因剪枝（CAP），这是一种无需训练的方法，通过测量注意力头对推理任务的因果影响来识别关键头，在 20%稀疏度下，ARC-Challenge 上相比 Wanda 获得了高达 61%的相对准确率提升。 这项工作通过实现更有效的剪枝来保留推理性能，解决了大语言模型推理成本高的问题，对于在资源受限环境中部署大模型至关重要。 CAP 使用一小部分推理问题的校准集，估计每个注意力头被掩码时的预期性能下降，然后将这些因果分数转换为权重级重要性用于剪枝。在 Llama-3-8B-Instruct 和 Mistral-7B-Instruct 上以 10%、20%和 50%稀疏度进行的评估表明，在中等稀疏度下 CAP 始终优于 Wanda。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 大语言模型（LLM）依赖注意力头来处理信息，剪枝通过移除不重要的权重来减小模型大小和推理成本。现有的剪枝方法如 Wanda 使用权重幅度或基于激活的标准，可能无法捕捉注意力头对推理任务的功能重要性。CAP 引入了一种因果干预方法，直接测量每个头的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19350">Pruning via Causal Attribution Preserves Reasoning Performance in...</a></li>
<li><a href="https://eric-mingjie.github.io/wanda/home.html">A Simple and Effective Pruning Approach for Large Language Models</a></li>
<li><a href="https://arxiv.org/html/2601.04398">Interpreting Transformers Through Attention Head Intervention</a></li>

</ul>
</details>

**标签**: `#LLM`, `#pruning`, `#causal attribution`, `#reasoning`, `#efficiency`

---

<a id="item-27"></a>
## [综述索引了涵盖 35 种语言的 120 个手语数据集](https://arxiv.org/abs/2606.19352) ⭐️ 8.0/10

一项全面综述索引了涵盖 35 种语言的 120 个手语数据集，分析了模态不平衡、标注粒度和手语者偏差等挑战，并提出了标准化的 24 字段数据表和一个公开的 GitHub 仓库。 这项工作为开发包容且可扩展的手语技术提供了统一基础，解决了阻碍识别、翻译和生成系统发展的碎片化和不一致性问题。 该综述引入了一个 24 字段的手语数据表以标准化文档，并发布了一个公开的 GitHub 仓库（https://github.com/Ginqwerty/Open-Sign-Language）用于可复现评估。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 手语是聋人和听障人士使用的视觉语言。尽管基于 AI 的手语识别和翻译取得了进展，但数据集碎片化、标注不一致以及语言覆盖不足限制了发展。本综述系统地解决了这些差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19352">Sign - Language Datasets at Scale: A Comprehensive Survey on...</a></li>
<li><a href="https://arxiv.org/html/2403.02563v1">Systemic Biases in Sign Language AI Research: A Deaf-Led Call to...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s11227-025-07119-8">Data augmentation and debiasing for signers in signer -independent...</a></li>

</ul>
</details>

**标签**: `#sign language`, `#datasets`, `#survey`, `#annotation`, `#benchmarks`

---

<a id="item-28"></a>
## [自函数向量量化上下文学习中的偶然不确定性](https://arxiv.org/abs/2606.19353) ⭐️ 8.0/10

该论文引入了自函数向量，利用模型内部表示来分解上下文学习中的偶然不确定性，从而更可靠地估计 LLM 预测置信度。它还提出了首个针对 ICL 中偶然不确定性的严格评估协议，并在合成和真实任务上进行了验证。 这项工作通过区分上下文学习中的偶然不确定性（数据噪声）和认知不确定性（模型无知），填补了 LLM 可靠性的关键空白。该方法可应用于幻觉检测等实际任务，提升 LLM 输出的可信度。 自函数向量基于贝叶斯观点和 ICL 的机制可解释性，对提示过程中学到的潜在概念进行建模，无需依赖输入或解码操作。评估协议通过控制数据属性，精确地将偶然不确定性与认知不确定性分开量化。

rss · arXiv - NLP · Jun 19, 04:00

**背景**: 上下文学习（ICL）允许 LLM 从少量示例中适应新任务而无需微调，但预测对提示设计敏感。偶然不确定性源于数据固有噪声，认知不确定性源于模型局限性；分解它们对于可靠预测至关重要。现有的 LLM 不确定性量化方法针对标准生成任务设计，无法捕捉 ICL 的动态特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://learnmechinterp.com/topics/function-vectors/">Function Vectors | Learn Mechanistic Interpretability</a></li>
<li><a href="https://link.springer.com/article/10.1007/s10994-021-05946-3">Aleatoric and epistemic uncertainty in machine learning : an...</a></li>
<li><a href="https://arxiv.org/pdf/2604.12434">A Bayesian Perspective on the Role of Epistemic Uncertainty for...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#uncertainty quantification`, `#in-context learning`, `#mechanistic interpretability`, `#Bayesian methods`

---

<a id="item-29"></a>
## [13 亿参数的胸部 X 光生成模型](https://arxiv.org/abs/2606.19460) ⭐️ 8.0/10

研究人员推出了首个十亿参数级别的胸部 X 光生成基础模型，该模型拥有超过 13 亿参数，基于 120 万张 X 光片并使用整流流变换器进行训练。 该模型解决了放射学 AI 在不同患者群体和机构间泛化能力差的问题，通过可控生成和编辑来丰富临床数据集，提升诊断模型的鲁棒性。 该模型支持跨人口统计亚组、采集视图和十多种病理的可控生成，其生成图像的逼真度在临床专家看来与真实 X 光片无异。

rss · arXiv - Computer Vision · Jun 19, 04:00

**背景**: 整流流变换器结合了整流流（一种基于常微分方程的生成方法）的高效性和变换器的强大表征能力。医学影像生成基础模型旨在合成高保真图像，以扩充训练数据并评估模型的鲁棒性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.03206">[2403.03206] Scaling Rectified Flow Transformers for...</a></li>
<li><a href="https://radit-project.github.io/">Scaling Generative Foundation Models for Chest Radiography with...</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#medical imaging`, `#foundation model`, `#chest radiography`, `#rectified flow`

---

<a id="item-30"></a>
## [LooseControlVideo：用 3D 框实现直观视频控制](https://arxiv.org/abs/2606.19495) ⭐️ 8.0/10

LooseControlVideo 提出了一种框架，利用稀疏、有方向的 3D 框作为遮挡代理，在文本到视频生成中实现直观的 3D 空间控制，并在 Wan 2.2 骨干网络上通过新颖的 DNOCS 编码进行微调。 这项工作解决了文本到视频生成中多对象场景编排的关键挑战，使用户能够设计高级布局和轨迹，同时模型处理真实的遮挡和动态，显著优于现有的 2D 框和基于流的基线方法。 该方法在 nuScenes、HO-3D 和 BEHAVE 基准测试上，与最先进的布局条件模型相比，轨迹误差降低了 1.2 到 3 倍，刚体运动一致性提升了 2 倍，遮挡精度提高了 1.5 到 2 倍。

rss · arXiv - Computer Vision · Jun 19, 04:00

**背景**: 文本到视频生成旨在根据文本描述创建视频。现有的深度条件模型需要密集、逐帧精确的指导，对于动态场景来说劳动强度大。LooseControlVideo 使用稀疏的 3D 框作为高级控制信号，允许用户指定对象位置和轨迹，而无需密集标注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19495">LooseControlVideo : Directorial Video Control using Spatial Blocking</a></li>
<li><a href="https://shariqfarooq123.github.io/LooseControlVideo/">LooseControlVideo Project Page</a></li>
<li><a href="https://huggingface.co/papers/2606.19495">Paper page - LooseControlVideo : Directorial Video Control using...</a></li>

</ul>
</details>

**标签**: `#text-to-video`, `#3D control`, `#video generation`, `#spatial layout`, `#deep learning`

---

<a id="item-31"></a>
## [ImageWAM：用图像编辑替代视频生成的世界动作模型](https://arxiv.org/abs/2606.19531) ⭐️ 8.0/10

ImageWAM 提出了一种新框架，将预训练的图像编辑模型用于机器人动作预测，挑战了世界动作模型中主流的视频生成方法。 这项工作大幅降低了计算成本和延迟——FLOPs 降至视频 WAM 的 1/6，延迟降至 1/4——同时保持或提升了性能，使世界动作模型在真实机器人应用中更加实用。 ImageWAM 在推理时不解码目标帧，而是将流匹配动作专家条件化于图像编辑去噪产生的 KV 缓存，将其作为紧凑的世界动作上下文。它在无需额外策略预训练的情况下，超越了标准 VLA 基线和有竞争力的 WAM。

rss · arXiv - Computer Vision · Jun 19, 04:00

**背景**: 世界动作模型（WAM）是统一预测性世界建模与动作生成的具身 AI 系统，通常依赖视频生成来预测未来帧。然而，视频生成计算成本高，且容易因无关细节产生错误。图像编辑通过仅关注当前状态与目标状态之间与动作相关的变换，提供了一种更高效的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/yuyangalin/ImageWAM">GitHub - yuyangalin/ ImageWAM : ImageWAM : Do World Action Models...</a></li>
<li><a href="https://huggingface.co/papers/2606.19531">Paper page - ImageWAM: Do World Action Models Really Need Video...</a></li>

</ul>
</details>

**标签**: `#world action models`, `#image editing`, `#robot control`, `#video generation`, `#AI`

---

<a id="item-32"></a>
## [LIVE：语言引导的可控视觉嵌入方法](https://arxiv.org/abs/2606.19584) ⭐️ 8.0/10

研究人员提出 LIVE（语言引导视觉嵌入）框架，在推理时利用语言指令动态引导视觉编码器，生成任务中心化的嵌入，无需针对特定任务重新训练。 LIVE 在 MMVP 基准上将视觉幻觉降低 34 个百分点，在视觉问答上超越参数量大数个量级的视觉语言模型，并能泛化到未见任务，为自适应、指令驱动的视觉智能提供了一条轻量级路径。 LIVE 仅涉及视觉编码器，因此轻量高效，可在设备端运行。它通过训练编码器遵循文本指令，实现了对编码器的动态细粒度控制。

rss · arXiv - Computer Vision · Jun 19, 04:00

**背景**: 传统视觉基础模型是静态特征提取器，任务适应需要大型下游模型或微调。LIVE 则利用语言作为高层引导来操控视觉编码器，在推理时生成可控且可泛化的嵌入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.19584">[2606.19584] Language - Instructed Vision Embeddings for...</a></li>
<li><a href="https://live-embedding.github.io/">LIVE : Language - Instructed Vision Embeddings for Controllable and...</a></li>

</ul>
</details>

**标签**: `#computer vision`, `#vision-language models`, `#foundation models`, `#instruction-driven perception`, `#hallucination reduction`

---

<a id="item-33"></a>
## [学习异步调度以加速扩散模型训练](https://arxiv.org/abs/2606.19662) ⭐️ 8.0/10

研究人员提出了一种为多表示扩散模型学习异步调度的方法，在 ImageNet 256x256 上实现了 4 倍的训练缩减，同时匹配或超越了最先进的 FID 分数。 这项工作显著降低了训练高质量扩散模型的计算成本，使其更易于研究和部署，并可能加速图像生成及其他生成任务的进展。 该方法使用调度校正目标和一种灵活的参数化调度类（通过构造保证凸性和单调性），学习开销不到额外计算的 1%。在 AutoGuidance 下，200 个 epoch 的模型达到 FID 1.05，匹配 800 个 epoch 的 SFD-XL 基线。

rss · arXiv - Computer Vision · Jun 19, 04:00

**背景**: 扩散模型通过逐步去噪随机噪声样本来生成图像。多表示扩散模型对图像的互补视图（例如不同频带）进行去噪，其性能取决于决定每个视图何时去噪的异步调度。先前的工作使用固定调度；本文从数据中学习调度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19662">Learning When to Denoise: Optimizing Asynchronous Schedules for...</a></li>
<li><a href="https://www.emergentmind.com/topics/asynchronous-diffusion-models">Asynchronous Diffusion Models</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#asynchronous scheduling`, `#image generation`, `#flow matching`, `#efficient training`

---

<a id="item-34"></a>
## [Stochastic Hi-Fi 将标量交互分解为独特性、冗余性和协同性](https://arxiv.org/abs/2606.19410) ⭐️ 8.0/10

该论文提出了 Stochastic Hi-Fi，一种无需重新训练的事后方法，可将成对交互得分分解为独特性、冗余性和协同性分量，并提供了理论证明以及在结构因果模型和 GPT-2 上的应用。 这项工作通过解耦混淆的机制，解决了标量交互指数的基本局限性，显著提高了机器学习模型（尤其是大型语言模型）的可解释性，并实现了对特征交互的更精确分析。 Stochastic Hi-Fi 使用干预掩码推理和耦合菱形采样来降低方差，提供有限样本蒙特卡洛界，并在表格 SCM 上相比标量基线实现了高达 411 倍的交互幅度恢复比。

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**背景**: 有符号成对交互得分（如 Shapley-Taylor 和 Shapley Interaction 指数）常用于衡量机器学习模型中的特征交互。然而，这些标量得分混淆了三种不同的机制：独特性、冗余性和协同性，导致解释模糊。Stochastic Hi-Fi 通过干预推理提供了一种分解方法，将这些机制分离开来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1902.05622">[1902.05622] The Shapley Taylor Interaction Index</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#causal inference`, `#machine learning`, `#feature interaction`, `#LLM`

---

<a id="item-35"></a>
## [无求解器训练方法用于预测后优化](https://arxiv.org/abs/2606.19587) ⭐️ 8.0/10

研究人员提出了一种新的预测后优化训练方法，通过测度变换原理创建无求解器的替代损失，从而在梯度评估期间无需调用求解器。 该方法在保持竞争性决策质量的同时，将训练时间减少了几个数量级，使得决策聚焦学习能够扩展到求解器调用成为瓶颈的更大规模问题。 该方法提供了包括 Fisher 一致性和超额风险界在内的理论保证，并在实证上以显著更低的计算成本达到了与最先进方法相当的决策质量。

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**背景**: 在预测后优化范式中，机器学习预测被用作下游优化问题的系数。直接最小化决策遗憾具有挑战性，因为决策映射是分段常数且梯度几乎处处为零。现有方法通过平滑微分来解决，但每个梯度步骤都需要昂贵的求解器调用，限制了可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/predict-then-optimize-paradigm-9d829742-aae1-4663-9a7f-ac6606541a6b">Predict - Then - Optimize Paradigm</a></li>
<li><a href="https://arxiv.org/html/2601.04062">Smart Predict – then – Optimize Paradigm for Portfolio Optimization in...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#optimization`, `#decision-focused learning`, `#predict-then-optimize`

---

<a id="item-36"></a>
## [AURA：面向 LLM 评判的自适应不确定性感知精炼框架](https://arxiv.org/abs/2606.19714) ⭐️ 8.0/10

AURA 是一种新颖的自适应不确定性感知框架，它迭代地学习人类一致性信号，并优先将不确定的成对比较提交给人工审核，从而实现更可靠的 LLM 评判审计。 这解决了 LLM 评估中的一个关键限制：评判偏见和人工标注的稀缺性。通过选择性地将人力集中在不确定的案例上，AURA 可以在不需要全面人工评估的情况下显著提高 LLM 评判系统的可靠性。 AURA 将对评判者的信任视为一个潜在量，随着证据的积累逐步精炼。它提供了紧凑的公式、稳定的精炼过程，并在合成和真实的成对 LLM 答案数据上进行了全面评估。

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**背景**: LLM 评判是一种让大型语言模型根据定义的标准评估 AI 输出的方法，但这些模型常常表现出偏见，可能无法与人类判断完全对齐。传统审计假设存在可靠的示例子集或干净的监督信号，这在实践中很脆弱。AURA 通过自适应地从有限的人工验证中学习来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.19714">AURA: Adaptive Uncertainty - aware Refinement for LLM-as-a-Judge...</a></li>
<li><a href="https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge">LLM - as - a - Judge - Langfuse</a></li>
<li><a href="https://arxiv.org/pdf/2411.15594">A Survey on LLM - as - a - Judge</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#auditing`, `#uncertainty`, `#human-in-the-loop`, `#NLP`

---

<a id="item-37"></a>
## [MDP 中 MNAR 奖励的缺失感知策略离线评估](https://arxiv.org/abs/2606.20206) ⭐️ 8.0/10

本文提出了在有限时域马尔可夫决策过程中，当奖励非随机缺失（MNAR）时进行离线策略评估的新方法，利用影子变量和桥函数来纠正选择偏差。 这项工作通过处理医疗和营销等领域常见的 MNAR 奖励，填补了离线强化学习中的一个关键空白，使得从真实世界日志数据中进行更可靠的策略评估成为可能。 该方法形式化了奖励依赖的倾向模型，使用未来状态作为影子变量，并引入通过最小-最大过程估计的桥函数，无需显式建模 MNAR 机制即可恢复条件均值奖励。

rss · arXiv - Data Science & Statistics · Jun 19, 04:00

**背景**: 离线策略评估（OPE）利用从不同行为策略收集的数据来估计目标策略的价值。在许多实际应用中，奖励常常是非随机缺失（MNAR）的，即缺失与否取决于未观测到的奖励本身，这引入了选择偏差。现有的 OPE 方法通常假设奖励完全观测或随机缺失，限制了其适用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.16061">Partial Identification under Missing Data Using Weak Shadow ... - arXiv</a></li>
<li><a href="https://arxiv.org/abs/2202.04970">[2202.04970] Off-Policy Fitted Q - Evaluation with Differentiable...</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1002/sam.70045">Neural Estimation of Treatment Bridge Functions for Proximal Causal Inference - Zhang - 2025 - Statistical Analysis and Data Mining: An ASA Data Science Journal - Wiley Online Library</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#off-policy evaluation`, `#missing data`, `#causal inference`

---

<a id="item-38"></a>
## [初创公司声称突破大语言模型瓶颈](https://www.technologyreview.com/2026/06/19/1139313/a-startup-claims-it-broke-through-a-bottleneck-thats-holding-back-llms/) ⭐️ 8.0/10

总部位于迈阿密的 AI 初创公司 Subquadratic 走出隐身模式，声称解决了近十年来限制大语言模型的二次注意力瓶颈。该公司已分享独立评估结果以支持其说法。 如果属实，这一突破可大幅降低大语言模型的计算成本和功耗，实现更长的上下文窗口和更广泛的部署。该声明针对的是 Transformer 架构中制约 AI 进展的根本性限制。 Subquadratic 的技术名为 SubQ，声称是首个基于次二次注意力的商业大语言模型，拥有 1200 万 token 的上下文窗口，成本仅为前沿模型的一小部分。然而，细节仍然稀少，这些说法遭到了 AI 社区的怀疑。

rss · MIT Technology Review · Jun 19, 10:40

**背景**: 像 GPT-4 这样的大语言模型依赖于 Transformer 架构，其注意力机制的计算复杂度随输入长度呈二次方增长。这种二次复杂度使得处理长序列在内存和计算上极其昂贵，将上下文窗口限制在数千 token 以内。次二次注意力旨在降低这种复杂度，从而在不按比例增加成本的情况下实现更长的上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/19/1139313/a-startup-claims-it-broke-through-a-bottleneck-thats-holding-back-llms/">A startup claims it broke through a bottleneck that’s holding back LLMs</a></li>
<li><a href="https://thenextweb.com/news/subquadratic-subq-sparse-attention-llm-bottleneck">A startup says it cracked the bottleneck holding back AI</a></li>
<li><a href="https://www.peremptory.ai/posts/subquadratic-subq-llm-attention-architecture">A Startup Claims to Have Broken the Transformer's Core Bottleneck</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#startup`, `#AI research`, `#bottleneck`

---

<a id="item-39"></a>
## [渐冻症患者成为首位长期脑机接口重度用户](https://www.technologyreview.com/2026/06/19/1139270/brain-computer-interface-trials-are-taking-off/) ⭐️ 8.0/10

患有渐冻症（ALS）的凯西·哈雷尔成为首位长期使用脑机接口的重度用户，尽管瘫痪，他借助植入设备已近三年进行交流。 这一里程碑表明，脑机接口技术能够为严重瘫痪患者提供持续、实际的益处，为更广泛的临床应用和生活质量改善铺平道路。 哈雷尔在没有该设备的情况下无法连贯说话，该设备解读其运动皮层的神经信号以实现交流。该植入物已使用近三年，创下脑机接口用于交流的最长连续使用记录。

rss · MIT Technology Review · Jun 19, 09:00

**背景**: 脑机接口（BCI）是大脑与外部设备之间的直接通信通路，绕过肌肉和神经。对于渐冻症或瘫痪患者，BCI 可以解码神经活动来控制光标、拼写字母或操作辅助设备。以往的试验多为短期，而哈雷尔的案例展示了长期可行性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alzforum.org/news/research-news/mind-machine-meld-brain-computer-interfaces-als-paralysis">Mind-machine Meld: Brain-computer Interfaces for ALS , Paralysis</a></li>
<li><a href="https://neurosciencenews.com/als-paralysis-computer-control-implant-5512/">Implant Allows Locked In ALS Patient to Operate... - Neuroscience News</a></li>
<li><a href="https://alsnewstoday.com/news/nih-grants-10-million-launch-us-trial-stentrode-severe-paralysis/">NIH Grants $10M to US Trial of Stentrode Brain Implant for ALS ...</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neurotechnology`, `#ALS`, `#medical technology`, `#human augmentation`

---

<a id="item-40"></a>
## [阿尔茨海默病触发机制或为淀粉样蛋白干扰 tau 蛋白](https://www.sciencedaily.com/releases/2026/06/260617032209.htm) ⭐️ 8.0/10

科学家提出，阿尔茨海默病的触发机制是β-淀粉样蛋白干扰 tau 蛋白功能，而非仅由淀粉样斑块引起。 这一范式转变可能将药物研发方向转向针对淀粉样蛋白与 tau 蛋白的相互作用，从而有望开发出更有效的阿尔茨海默病治疗方法。 研究指出，β-淀粉样蛋白破坏了 tau 蛋白稳定微管的功能，而微管对神经元结构和物质运输至关重要。这种破坏可能引发导致阿尔茨海默病病理变化的神经元损伤。

rss · ScienceDaily Health · Jun 19, 02:49

**背景**: 阿尔茨海默病以两种标志性脑部异常为特征：淀粉样斑块（β-淀粉样蛋白团块）和 tau 蛋白缠结（tau 蛋白扭曲纤维）。几十年来，主流假说认为淀粉样斑块直接导致疾病。然而，针对斑块的疗法效果有限，促使研究人员探索其他机制。tau 蛋白通常通过结合微管来维持神经元的结构稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pubmed.ncbi.nlm.nih.gov/35443153/">Regional Aβ- tau interactions promote onset and acceleration of...</a></li>
<li><a href="https://link.springer.com/article/10.1186/s40035-025-00479-4">Dual modulation of amyloid beta and tau aggregation and dissociation...</a></li>
<li><a href="https://int.livhospital.com/neurofibrillary-tangles-tau-protein-guide/">Neurofibrillary Tangles Tau Protein : Guide - Liv Hospital</a></li>

</ul>
</details>

**标签**: `#Alzheimer's`, `#neuroscience`, `#amyloid beta`, `#tau protein`

---