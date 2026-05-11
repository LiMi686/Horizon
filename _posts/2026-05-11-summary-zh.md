---
layout: default
title: "Horizon Summary: 2026-05-11 (ZH)"
date: 2026-05-11
lang: zh
---

> From 90 items, 38 important content pieces were selected

---

1. [Nvidia 发布 CUDA-Oxide：Rust 到 CUDA 编译器](#item-1) ⭐️ 9.0/10
2. [HumanNet：百万小时人类中心视频数据集](#item-2) ⭐️ 9.0/10
3. [前馈神经网络具有有限样本复杂度](#item-3) ⭐️ 9.0/10
4. [开发者回归手写代码，警示 AI 认知债务](#item-4) ⭐️ 8.0/10
5. [AI 可能终结软件工程作为终身职业](#item-5) ⭐️ 8.0/10
6. [Mythos AI 发现 curl 漏洞，炒作遭质疑](#item-6) ⭐️ 8.0/10
7. [纽约时报因发布 AI 生成引文发布编者按](#item-7) ⭐️ 8.0/10
8. [字节跳动开源多模态 AI 智能体栈](#item-8) ⭐️ 8.0/10
9. [Agent Skills：为 AI 编程代理提供生产级工作流](#item-9) ⭐️ 8.0/10
10. [CloakBrowser：隐身 Chromium 通过所有机器人检测测试](#item-10) ⭐️ 8.0/10
11. [GenericAgent：从 3000 行种子代码自我进化的智能体](#item-11) ⭐️ 8.0/10
12. [Memori：面向 LLM 的智能体原生记忆基础设施](#item-12) ⭐️ 8.0/10
13. [GraphDC：用于图推理的分治多智能体系统](#item-13) ⭐️ 8.0/10
14. [更长的推理链加剧大模型位置偏差](#item-14) ⭐️ 8.0/10
15. [谱诊断方法检测多智能体 AI 中的隐藏联盟](#item-15) ⭐️ 8.0/10
16. [CASCADE：部署期间基于案例的 LLM 持续适应框架](#item-16) ⭐️ 8.0/10
17. [LLM 智能体记忆进化：从存储到经验](#item-17) ⭐️ 8.0/10
18. [Weblica：为视觉网络代理提供可扩展的训练环境](#item-18) ⭐️ 8.0/10
19. [SCALAR：迭代批评提升大模型物理推理能力](#item-19) ⭐️ 8.0/10
20. [RateQuant：基于率失真理论的最优混合精度 KV 缓存量化](#item-20) ⭐️ 8.0/10
21. [LKV：学习型 KV 缓存淘汰方法提升 LLM 推理效率](#item-21) ⭐️ 8.0/10
22. [PND：无需训练的解码方法减少 VLM 幻觉](#item-22) ⭐️ 8.0/10
23. [流匹配中的应变与涡量误差分析](#item-23) ⭐️ 8.0/10
24. [Toeplitz MLP Mixer：高效的次二次序列模型](#item-24) ⭐️ 8.0/10
25. [种系吸收扩散改进抗体设计](#item-25) ⭐️ 8.0/10
26. [33 个 LLM 的领域级元认知监测研究](#item-26) ⭐️ 8.0/10
27. [IntentGrasp 基准揭示 LLM 意图理解差距](#item-27) ⭐️ 8.0/10
28. [提出以人为中心的大语言模型框架](#item-28) ⭐️ 8.0/10
29. [LLM 无法根据检索信息确定性调整回应](#item-29) ⭐️ 8.0/10
30. [测度传输理论解释视觉文本压缩](#item-30) ⭐️ 8.0/10
31. [LookWhen：通过令牌选择实现高效视频识别](#item-31) ⭐️ 8.0/10
32. [3D 医学影像知识迁移的缩放定律](#item-32) ⭐️ 8.0/10
33. [HSA：用于高效视频扩散 Transformer 的异构步长分配](#item-33) ⭐️ 8.0/10
34. [注意力机制：随机矩阵理论对信号恢复的洞见](#item-34) ⭐️ 8.0/10
35. [神经算子学习任意联合密度的条件分布](#item-35) ⭐️ 8.0/10
36. [将核选择视为模型选择以改进 MMD 检验](#item-36) ⭐️ 8.0/10
37. [可解释的 IRT 框架用于可扩展的大语言模型评估](#item-37) ⭐️ 8.0/10
38. [TRACE：基于扩散与流匹配的传输对齐共形预测](#item-38) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Nvidia 发布 CUDA-Oxide：Rust 到 CUDA 编译器](https://nvlabs.github.io/cuda-oxide/index.html) ⭐️ 9.0/10

Nvidia Labs 发布了 CUDA-oxide 0.1，这是一个实验性的 Rust 到 CUDA 编译器，可将标准 Rust 代码直接编译为 PTX，从而无需 DSL 或外部函数绑定即可用 Rust 开发 GPU 内核。 这标志着 Nvidia 正式支持 Rust 进行 GPU 编程，可能将 Rust 的内存安全性和性能优势引入 CUDA 开发，通过提供比 CUDA C++ 更安全的替代方案，对 GPU 计算生态产生重大影响。 CUDA-oxide 是一个自定义的 rustc 后端，支持单源编译，即主机和设备代码位于同一文件中，并通过单个 cargo oxide build 命令构建。它直接将 Rust 编译为 PTX，即 NVIDIA GPU 的中间表示。

hackernews · adamnemecek · May 11, 15:55 · [社区讨论](https://news.ycombinator.com/item?id=48096692)

**背景**: CUDA 是 Nvidia 的并行计算平台和编程模型，用于 GPU 加速，传统上使用带有扩展的 C++ 进行编程。Rust 是一种系统编程语言，以无需垃圾回收的内存安全性著称。CUDA-oxide 旨在将 Rust 的安全保证与 CUDA 的性能相结合，尽管由于硬件限制，GPU 内核编程本质上涉及不安全操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVlabs/cuda-oxide">GitHub - NVlabs/cuda-oxide: cuda-oxide is an experimental Rust-to-CUDA compiler that lets you write (SIMT) GPU kernels in safe(ish), idiomatic Rust. It compiles standard Rust code directly to PTX — no DSLs, no foreign language bindings, just Rust.</a></li>
<li><a href="https://nvlabs.github.io/cuda-oxide/index.html">The cuda-oxide Book — cuda-oxide</a></li>
<li><a href="https://www.phoronix.com/news/NVIDIA-CUDA-Oxide-0.1">NVIDIA Releases CUDA-Oxide 0.1 For Experimental Rust-To-CUDA Compiler - Phoronix</a></li>

</ul>
</details>

**社区讨论**: 社区对 CUDA-oxide 作为现有 Rust CUDA 包的潜在替代品感到兴奋，关注构建时间比较以及 Rust 内存模型的处理。有人担心 Rust 的安全特性（如边界检查）可能带来开销，增加寄存器使用并降低内核并发性，此外还关注主机和设备之间共享结构体的能力。

**标签**: `#CUDA`, `#Rust`, `#GPU Programming`, `#Compilers`, `#Nvidia`

---

<a id="item-2"></a>
## [HumanNet：百万小时人类中心视频数据集](https://arxiv.org/abs/2605.06747) ⭐️ 9.0/10

研究人员推出了 HumanNet，这是一个包含一百万小时人类中心视频的数据集，具有以交互为中心的标注，包括描述、运动描述以及手部和身体信号，旨在扩展具身智能学习。 该数据集为训练具身基础模型提供了一种可扩展且经济高效的替代方案，替代了机器人专用数据，可能加速人类活动理解、运动生成和人到机器人迁移的进展。 HumanNet 涵盖第一人称和第三人称视角，覆盖细粒度活动、人-物交互、工具使用和长期行为。一项验证实验表明，使用 HumanNet 中 1000 小时自我中心视频进行持续训练，优于使用 Magic Cobot 中 100 小时真实机器人数据进行的训练。

rss · arXiv - Computer Vision · May 11, 04:00

**背景**: 具身智能旨在创建能够感知并在物理世界中行动的人工智能系统。虽然视觉和语言模型通过互联网数据实现了规模化，但物理交互的学习一直受到缺乏大规模、多样化和丰富标注的人类活动数据集的限制。HumanNet 通过将非结构化互联网视频整理为结构化资源来弥补这一缺口，用于具身学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Embodied_intelligence">Embodied intelligence</a></li>
<li><a href="https://arxiv.org/abs/2412.00115">[2412.00115] OpenHumanVid: A Large-Scale High-Quality Dataset for Enhancing Human-Centric Video Generation</a></li>

</ul>
</details>

**标签**: `#embodied intelligence`, `#human-centric video`, `#dataset`, `#human-object interaction`, `#motion learning`

---

<a id="item-3"></a>
## [前馈神经网络具有有限样本复杂度](https://arxiv.org/abs/2605.07097) ⭐️ 9.0/10

一篇新论文证明，任何层在 o-minimal 结构中可定义的前馈神经网络，在不可知 PAC 模型下都具有有限样本复杂度，涵盖 MLP、CNN、GNN 和 Transformer。 该结果将现代前馈架构的 PAC 可学习性统一在一个理论框架下，表明有限样本可学习性是基线属性而非区分因素，从而将关注点转向归纳偏置、可扩展性和优化。 该结果即使在参数无界的情况下也成立，涵盖线性投影、残差连接、注意力、池化、归一化和可接受的位置编码等操作，但不包括循环架构。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: PAC 学习是一个分析学习算法能否在有限样本下以高概率实现低误差的框架。VC 维度衡量假设类的容量；有限 VC 维度意味着 PAC 可学习性。O-minimal 结构是模型论中的结构，其中每个可定义集都是区间和点的有限并集，确保“驯顺”行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/O-minimal_structure">O-minimal structure</a></li>
<li><a href="https://en.wikipedia.org/wiki/Probably_approximately_correct_learning">Probably approximately correct learning - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/VC_dimension">VC dimension</a></li>

</ul>
</details>

**标签**: `#PAC learning`, `#neural networks`, `#o-minimal structures`, `#VC dimension`, `#deep learning theory`

---

<a id="item-4"></a>
## [开发者回归手写代码，警示 AI 认知债务](https://blog.k10s.dev/im-going-back-to-writing-code-by-hand/) ⭐️ 8.0/10

一位开发者发表博文，在体验了 AI 生成代码的弊端后，主张回归手写代码，引发了关于认知债务和代码质量的讨论。 这一讨论凸显了软件工程界日益增长的担忧：AI 生成的代码可能增加认知债务，即开发者缺乏对所依赖代码的理解，从而导致长期维护难题。 博文和社区评论强调，AI 生成的代码可能造成虚假的生产力提升，开发者最终会面临无法理解或安全修改的代码库。术语“认知债务”用于描述在不完全理解的情况下使用代码所付出的隐性代价。

hackernews · dropbox_miner · May 11, 01:23 · [社区讨论](https://news.ycombinator.com/item?id=48090029)

**背景**: 认知债务（也称理解债务）是指开发者在处理自己不完全理解的代码（通常由 AI 生成）时所承担的心智负担。它与技术债务类似，但影响的是人类认知而非代码结构。随着 GitHub Copilot 等 AI 辅助编码工具的普及，这一概念逐渐受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.getdx.com/p/cognitive-debt-the-hidden-risk-in">Cognitive debt : The hidden risk in AI-driven software development</a></li>
<li><a href="https://productera.io/blog/cognitive-debt-ai-first-startup">Cognitive Debt Is Eating Your AI-First Startup | Productera</a></li>
<li><a href="https://www.linkedin.com/pulse/cognitive-debt-crisis-architecture-disruption-agentic-markus-eisele-98ygf">The Cognitive Debt Crisis - The Architecture of Disruption - Agentic...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍赞同博文观点，并分享了个人认知债务经历。一位评论者指出，只有不阅读生成代码的人才会认为它没问题；另一位描述了 AI 逐步接管更多编码任务，直到代码库变得无法管理的渐进过程。一些人建议安全使用 AI 的规则，例如只生成开发者自己能编写的代码。

**标签**: `#AI-assisted coding`, `#software engineering`, `#code quality`, `#cognitive debt`

---

<a id="item-5"></a>
## [AI 可能终结软件工程作为终身职业](https://www.seangoedecke.com/software-engineering-may-no-longer-be-a-lifetime-career/) ⭐️ 8.0/10

一篇文章和社区讨论认为，AI（尤其是大型语言模型）可能使软件工程不再是一个可行的终身职业，因为依赖 AI 可能导致技能退化和解决问题能力下降。 这场辩论影响着全球数百万软件工程师，因为它质疑了他们的技能在未来 AI 增强行业中的价值以及职业的可持续性。 评论者区分了使用 AI 增强推理的工程师和用 AI 替代推理的工程师，警告后者面临长期技能退化的风险。而将 AI 作为工具的资深工程师可能会变得更高产。

hackernews · movis · May 11, 14:34 · [社区讨论](https://news.ycombinator.com/item?id=48095550)

**背景**: 软件工程传统上被视为稳定且高需求的职业。然而，GPT-4 和 Copilot 等 AI 代码生成工具的快速发展引发了担忧，即初级和中级岗位可能被自动化，从而减少对人类开发者的长期需求。

**社区讨论**: 讨论观点多样：一些评论者认为，将 AI 作为工具的资深工程师仍然非常有价值，而另一些人则警告过度依赖 AI 会导致技能退化。一个关键见解是，开发者只有一小部分时间用于编写代码，大部分时间用于理解问题和制定解决方案。

**标签**: `#software engineering`, `#AI`, `#career`, `#LLM`, `#future of work`

---

<a id="item-6"></a>
## [Mythos AI 发现 curl 漏洞，炒作遭质疑](https://daniel.haxx.se/blog/2026/05/11/mythos-finds-a-curl-vulnerability/) ⭐️ 8.0/10

Daniel Stenberg 报告称，Anthropic 的 AI 模型 Mythos 在 curl 中发现了一个漏洞，但仅发现了五个问题，远低于预期。社区讨论质疑对 Mythos 的炒作是否合理，因为 curl 相对简单且结果平平。 此事重要，因为 curl 是广泛使用的工具，而 AI 驱动的漏洞检测是热门话题。平平的结果表明 AI 炒作可能超过实际能力，影响组织对安全工具的投入决策。 Mythos 在 curl 中仅发现五个问题，Daniel Stenberg 称其“并不特别危险”。社区指出 curl 是相对简单且经过良好加固的工具，因此发现少可能反映 curl 的质量而非 Mythos 的弱点。

hackernews · TangerineDream · May 11, 06:39 · [社区讨论](https://news.ycombinator.com/item?id=48091737)

**背景**: curl 是一个用于 URL 数据传输的命令行工具和库，被数十亿设备使用。Mythos 是 Anthropic 的 AI 模型，属于 Claude 系列，旨在分析代码漏洞。对 Mythos 的炒作曾暗示它会发现“海啸”般的漏洞，但在 curl 上的测试结果平平。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://curl.se/docs/vulnall.html">curl - Vulnerability Table</a></li>
<li><a href="https://www.bbc.com/news/articles/c2ev24yx4rmo">Claude Mythos : Finance ministers and top bankers raise serious...</a></li>

</ul>
</details>

**社区讨论**: 评论者如 rzmmm 和 apexalpha 认为炒作主要是营销，apexalpha 指出这帮助争取了预算。srcreigh 认为 curl 的简单性限制了测试的相关性，而 EMM_386 指出零漏洞可能意味着 curl 已充分加固。总体情绪对 Mythos 声称的有效性持怀疑态度。

**标签**: `#curl`, `#vulnerability`, `#AI`, `#security`, `#hype`

---

<a id="item-7"></a>
## [纽约时报因发布 AI 生成引文发布编者按](https://simonwillison.net/2026/May/10/new-york-times-editors-note/#atom-everything) ⭐️ 8.0/10

《纽约时报》于 2026 年 4 月 14 日发布编者按，承认一篇文章中引用加拿大保守党领袖皮埃尔·波利耶夫的话实际上是 AI 对其观点的总结，而非真实引文。 此事件凸显了 AI 幻觉在新闻业中的关键风险——AI 生成的内容可能被误认为事实，从而侵蚀媒体信任。它强调了新闻编辑室对 AI 输出进行人工验证的迫切需求。 记者未能核实 AI 工具的输出，文章后来被更正，加入了波利耶夫演讲中的真实引文，其中并未出现 AI 所建议的“叛徒”一词。

rss · Simon Willison · May 10, 23:58

**背景**: AI 幻觉是指 AI 模型生成虚假或误导性信息并呈现为事实的现象。在新闻业中，AI 工具有时被用于总结或起草内容，但若缺乏仔细的人工监督，它们可能产生听起来合理但完全虚构的引文，正如本例所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)">Hallucination (artificial intelligence) - Wikipedia</a></li>
<li><a href="https://particlenews.medium.com/3-ways-particle-detects-and-avoids-hallucinations-in-news-summaries-c1a02d06f602">3 Ways Particle Detects and Avoids Hallucinations in News... | Medium</a></li>
<li><a href="https://phoue.co.kr/en/posts/ai-hallucination-plausible-lies-and-how-to-address-them/">AI Hallucination : Plausible Lies and How to Address Them</a></li>

</ul>
</details>

**标签**: `#ai-ethics`, `#hallucinations`, `#generative-ai`, `#journalism`

---

<a id="item-8"></a>
## [字节跳动开源多模态 AI 智能体栈](https://github.com/bytedance/UI-TARS-desktop) ⭐️ 8.0/10

字节跳动发布了 UI-TARS-desktop，这是一个开源的多模态 AI 智能体栈，包含 Agent TARS（通用 CLI/Web UI 智能体）和 UI-TARS Desktop（用于桌面和浏览器控制的本地 GUI 智能体）。 此次发布降低了开发者构建和部署能够控制计算机和浏览器的多模态 AI 智能体的门槛，有望加速软件测试、工作流管理和个人生产力等领域的自动化。 Agent TARS 集成了 MCP 工具，并通过多模态大语言模型支持类人任务完成；UI-TARS Desktop 则提供本地和远程操作器，用于计算机和浏览器控制。

rss · GitHub Trending - Daily (All) · May 11, 18:37

**背景**: 多模态 AI 智能体结合视觉和语言理解能力，以类似人类的方式与图形用户界面（GUI）交互。驱动 UI-TARS Desktop 的字节跳动 UI-TARS 模型是一个视觉-语言模型，经过训练可以解释屏幕内容并执行操作。此次开源发布包含两个互补项目：Agent TARS 用于通用智能体工作流，UI-TARS Desktop 用于直接桌面自动化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bytedance/UI-TARS-desktop">bytedance/UI- TARS -desktop: The Open-Source Multimodal AI Agent ...</a></li>
<li><a href="https://agent-tars.com/">Agent TARS - Open-source Multimodal AI Agent Stack</a></li>
<li><a href="https://ui-tarsai.com/">Bytedance UI - TARS AI Desktop : AI Agent for Computer Control</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#multimodal`, `#agent`, `#desktop`

---

<a id="item-9"></a>
## [Agent Skills：为 AI 编程代理提供生产级工作流](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 发布了一个名为 'agent-skills' 的 GitHub 仓库，将高级工程师的工作流和质量门禁打包成斜杠命令，供 Claude Code、Cursor 和 Gemini CLI 等 AI 编程代理使用。 该项目弥合了随意 AI 提示与严谨软件工程之间的差距，使 AI 代理能够在整个开发生命周期中遵循一致的生产级实践。 该仓库提供七个斜杠命令（/spec、/plan、/build、/test、/review、/code-simplify、/ship），对应开发阶段，并且技能会根据上下文自动激活（例如，API 设计会触发 api-and-interface-design）。

rss · GitHub Trending - Daily (All) · May 11, 18:37

**背景**: 像 Claude Code 和 Cursor 这样的 AI 编程代理可以生成代码，但通常缺乏结构化的工程工作流。'Agent Skills' 将高级工程师的最佳实践编码为可复用的技能，指导代理完成规范、规划、构建、测试、审查和发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://addyosmani.com/blog/agent-skills/">AddyOsmani .com - Agent Skills</a></li>
<li><a href="https://pyshine.com/Agent-Skills-Production-Grade-Engineering-for-AI/">Agent Skills : Production - Grade Engineering Skills for AI ... | PyShine</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#workflows`, `#developer tools`, `#best practices`

---

<a id="item-10"></a>
## [CloakBrowser：隐身 Chromium 通过所有机器人检测测试](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser 是一款新的开源隐身 Chromium 浏览器，通过应用 49 个源码级 C++ 指纹补丁，绕过所有主流机器人检测系统，取得了 30/30 的完美测试分数。它可作为 Playwright 和 Puppeteer 的直接替代品，仅需三行代码即可集成。 该项目解决了网络自动化和爬取中的一个关键痛点，即 Cloudflare Turnstile 和 reCAPTCHA v3 等机器人检测系统经常阻止自动化浏览器。通过提供一个通过所有检测测试的免费开源解决方案，CloakBrowser 可以显著减少依赖浏览器自动化的开发者和研究人员的障碍。 该浏览器使用了 49 个源码级 C++ 补丁，涵盖 canvas、WebGL、音频、字体、GPU、屏幕、WebRTC、网络时序、自动化信号和 CDP 输入行为。它还包含一个 humanize=True 标志，可模拟类人鼠标曲线、键盘时序和滚动模式，并取得了 0.9 的 reCAPTCHA v3 分数。

rss · GitHub Trending - Daily (All) · May 11, 18:37

**背景**: 浏览器指纹是一种网站通过收集屏幕分辨率、字体和 WebGL 渲染器等独特属性来识别和阻止自动化浏览器的技术。传统的绕过检测方法包括修补 JavaScript API 或使用无头浏览器，但这些往往会被高级反机器人系统检测到。CloakBrowser 在 C++ 级别修改 Chromium 源代码，使浏览器看起来与普通用户的浏览器完全相同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zenrows.com/blog/browser-fingerprinting">What Is Browser Fingerprinting and How to Bypass It? - ZenRows</a></li>
<li><a href="https://www.browserscan.net/bot-detection">BrowserScan - Robot Detection /WebDriver | BrowserScan</a></li>
<li><a href="https://bot.incolumitas.com/">Bot / Headless Chrome Detection Tests</a></li>

</ul>
</details>

**标签**: `#web automation`, `#bot detection`, `#browser fingerprinting`, `#open source`, `#Playwright`

---

<a id="item-11"></a>
## [GenericAgent：从 3000 行种子代码自我进化的智能体](https://github.com/lsdefine/GenericAgent) ⭐️ 8.0/10

GenericAgent 是一个极简的自我进化自主智能体框架，从约 3300 行种子代码生长出技能树，相比其他智能体实现 6 倍的令牌消耗降低，并具备完整的系统控制能力。 该方法大幅降低令牌消耗和成本，同时让智能体自主扩展能力，可能使 AI 智能体在真实系统控制任务中更加实用和可扩展。 核心代码仅约 3000 行，包含约 100 行的智能体循环和 9 个原子工具，可控制浏览器、终端、文件系统、键盘/鼠标、屏幕视觉以及通过 ADB 控制移动设备。支持 Claude、Gemini、Kimi 和 MiniMax 等模型。

rss · GitHub Trending - Daily (All) · May 11, 18:37

**背景**: 传统 AI 智能体通常依赖大上下文窗口（20 万到 100 万令牌）和预定义技能库，导致成本高、适应性有限。GenericAgent 采用自我进化机制，将执行路径固化为可复用技能，将上下文控制在 3 万令牌以内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/lsdefine/GenericAgent">GitHub - lsdefine/ GenericAgent : Self - evolving agent : grows skill tree...</a></li>
<li><a href="https://www.genericagent.org/">GenericAgent - Self - Evolving Agents for Real System Work</a></li>
<li><a href="https://a-gnt.com/agents/genericagent">a-gnt // GenericAgent — AI Agent for Claude, ChatGPT & More</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Self-Evolution`, `#Token Efficiency`, `#Skill Tree`, `#GitHub Trending`

---

<a id="item-12"></a>
## [Memori：面向 LLM 的智能体原生记忆基础设施](https://github.com/MemoriLabs/Memori) ⭐️ 8.0/10

Memori Labs 发布了 Memori，这是一个开源、与 LLM 无关的记忆基础设施，能将智能体的执行和对话转化为结构化的持久化状态，适用于生产系统。 这填补了构建可靠 LLM 智能体的关键空白，通过提供跨会话和跨模型的持久记忆，使 AI 应用更加连贯且具备上下文感知能力。 Memori 与 LLM、数据存储和框架无关，提供 TypeScript 和 Python SDK，并通过云服务（Memori Cloud）或自托管选项与现有技术栈集成。

rss · GitHub Trending - Python · May 11, 18:37

**背景**: LLM 智能体通常缺乏长期记忆，会在跨会话或切换模型时丢失上下文。Memori 捕获每次对话轮次，将其分类为事实、偏好、规则和摘要，并持久化以供回忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MemoriLabs/Memori">MemoriLabs/Memori: Memori is agent-native memory infrastructure .</a></li>
<li><a href="https://memorilabs.ai/">Memori – Agent-native memory infrastructure</a></li>
<li><a href="https://www.truefoundry.com/blog/truemem-building-a-model-agnostic-memory-layer-for-ai">How to Build Persistent Memory for AI Applications</a></li>

</ul>
</details>

**标签**: `#LLM`, `#agent memory`, `#infrastructure`, `#AI`, `#open source`

---

<a id="item-13"></a>
## [GraphDC：用于图推理的分治多智能体系统](https://arxiv.org/abs/2605.06671) ⭐️ 8.0/10

研究人员提出了 GraphDC，一个分治多智能体框架，它将大图分解为较小的子图，分配给专门的智能体进行局部推理，并由主智能体整合结果，显著提升了 LLM 在图算法任务上的表现。 这项工作解决了 LLM 在处理复杂图结构时的关键局限，实现了在大图上的可扩展和鲁棒推理，对知识图谱、网络分析和科学发现等应用至关重要。 GraphDC 的分层设计减轻了单个智能体的推理负担并缓解了计算瓶颈。实验表明，它持续优于现有方法，尤其是在直接端到端推理可靠性较低的大图实例上。

rss · arXiv - AI · May 11, 04:00

**背景**: 大型语言模型（LLM）在数学推理方面展现出强大潜力，但由于图结构复杂且需要多步推理，在图算法任务上表现不佳。现有方法通常尝试直接端到端推理，随着图规模增大变得不可靠。分治是一种经典的算法设计范式，它将问题分解为较小的子问题，独立求解后合并结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.22597">Are Large-Language Models Graph Algorithmic Reasoners? - arXiv</a></li>

</ul>
</details>

**标签**: `#LLM`, `#graph algorithms`, `#multi-agent systems`, `#scalability`, `#AI reasoning`

---

<a id="item-14"></a>
## [更长的推理链加剧大模型位置偏差](https://arxiv.org/abs/2605.06672) ⭐️ 8.0/10

一项新研究发现，大语言模型中更长的思维链推理轨迹会加剧多项选择问答中的位置偏差，这与“更多思考减少偏差”的假设相反。 这挑战了推理模型更鲁棒的普遍认知，揭示了一个隐藏的脆弱性，可能影响高风险评估和应用的可靠性。 在 13 种推理模式配置中，12 种显示轨迹长度与位置偏差得分（PBS）正相关，截断实验提供了因果证据：后续续写更倾向于位置偏好的选项。

rss · arXiv - AI · May 11, 04:00

**背景**: 位置偏差指大模型倾向于偏好某些答案位置（如“A”而非“B”），而不考虑内容。思维链（CoT）推理是一种提示模型在回答前生成逐步推理的技术，常用于提高准确性并减少偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@lyx_62906/the-hidden-position-bias-in-llms-why-your-ai-might-fail-when-its-asked-to-choose-26d59516f6ee">The Hidden Position Bias in LLMs : Why Your AI Might Fail... | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_reasoning">Chain-of-thought reasoning</a></li>

</ul>
</details>

**标签**: `#chain-of-thought`, `#position bias`, `#reasoning models`, `#LLM evaluation`, `#cognitive bias`

---

<a id="item-15"></a>
## [谱诊断方法检测多智能体 AI 中的隐藏联盟](https://arxiv.org/abs/2605.06696) ⭐️ 8.0/10

研究人员提出了一种谱诊断方法，该方法从智能体的内部神经表征构建互信息图，并应用谱分割来检测行为变化之前出现的隐藏联盟。 该方法通过早期检测多智能体系统中可能导致共谋或失调的新兴联盟，解决了 AI 安全中的一个关键空白，为分布式 AI 提供了可扩展的监控工具。 该方法在多智能体强化学习环境和大型语言模型中得到了验证，成功恢复了预设的联盟结构，并排除了无信息耦合的行为协调产生的误报。

rss · arXiv - AI · May 11, 04:00

**背景**: 多智能体 AI 系统由多个相互作用的智能体组成，它们可以形成联盟，产生新兴的群体级组织。仅观察行为往往不足以区分真正的信息耦合与虚假的相似性，因为联盟可能在行为变化之前就在内部表征层面形成。谱分割是一种利用图的拉普拉斯矩阵特征值来寻找最优切分的技术，常用于社区检测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06696">Hidden Coalitions in Multi-Agent AI: A Spectral Diagnostic from Internal ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Graph_partition">Graph partition - Wikipedia</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#AI safety`, `#coalition detection`, `#spectral partitioning`, `#mutual information`

---

<a id="item-16"></a>
## [CASCADE：部署期间基于案例的 LLM 持续适应框架](https://arxiv.org/abs/2605.06702) ⭐️ 8.0/10

CASCADE 提出了一个用于 LLM 部署时学习的新框架，使智能体无需修改模型参数即可从经验中改进，利用不断演化的情景记忆和具有无遗憾保证的上下文赌博机公式。 这项工作解决了当前 LLM 的一个关键限制——部署期间无法学习——并形式化了 LLM 生命周期的第三阶段，可能使 AI 系统在多种应用中持续改进。 在 16 个多样化任务中，CASCADE 相比零样本提示将宏观平均成功率提高了 20.9%，持续优于基于梯度和基于记忆的基线方法。

rss · arXiv - AI · May 11, 04:00

**背景**: 大型语言模型（LLM）通常在训练后停止学习，这与持续适应的自然智能不同。部署时学习（DTL）是一种新范式，允许 LLM 在部署期间通过交互改进，而无需参数更新，利用情景记忆存储和重用过去的经验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2501.13121">[2501.13121] Episodic Memories Generation and Evaluation...</a></li>
<li><a href="https://github.com/miguelalcocker/episodic-memory-llm">GitHub - miguelalcocker/ episodic - memory - llm : Persistent Episodic ...</a></li>
<li><a href="https://huggingface.co/papers/2407.09450">Paper page - Human-like Episodic Memory for Infinite Context LLMs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#continual learning`, `#deployment-time learning`, `#contextual bandit`, `#episodic memory`

---

<a id="item-17"></a>
## [LLM 智能体记忆进化：从存储到经验](https://arxiv.org/abs/2605.06716) ⭐️ 8.0/10

该综述提出了 LLM 智能体记忆机制的三阶段演化框架：存储、反思和经验，弥合了操作系统工程与认知科学之间的鸿沟。 该框架为 LLM 智能体的记忆设计提供了统一视角，对于提升智能体在长程一致性、动态环境和持续学习方面的能力至关重要。 三个阶段被正式定义：存储保存轨迹，反思优化轨迹，经验抽象轨迹。该综述还探讨了经验阶段中的主动探索和跨轨迹抽象这两种变革性机制。

rss · arXiv - AI · May 11, 04:00

**背景**: 基于 LLM 的智能体集成了外部工具和规划能力，但其记忆机制在不同领域中较为分散。短期记忆处理即时上下文，而长期记忆跨任务持久化。该综述旨在将这些观点统一到一个演化框架中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.rohan-paul.com/p/augmenting-llm-agents-with-long-term">Augmenting LLM Agents with Long-Term Memory - Rohan's Bytes</a></li>
<li><a href="https://www.emergentmind.com/videos/memory-mechanisms-in-llm-agents-b4da59c4">Memory Mechanisms in LLM Agents</a></li>
<li><a href="https://gist.github.com/Moenupa/5b9b341bfb52aa1bf150d8f35de831cf">Memory Literature Review · GitHub</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#memory mechanisms`, `#survey`, `#AI`, `#cognitive science`

---

<a id="item-18"></a>
## [Weblica：为视觉网络代理提供可扩展的训练环境](https://arxiv.org/abs/2605.06761) ⭐️ 8.0/10

Weblica 提出了一种框架，利用 HTTP 级缓存和基于 LLM 的环境合成来创建可扩展、可复现的网络环境，用于训练视觉网络代理，其 Weblica-8B 模型达到了最先进的性能。 这解决了网络代理研究中的一个关键瓶颈，使得在数千个多样化环境中进行可扩展的强化学习训练成为可能，超越了开源基线模型，并与 API 模型竞争，有望加速鲁棒网络代理的开发。 Weblica 利用 HTTP 级缓存来捕获和重放稳定的视觉状态，同时保留交互行为，并使用基于真实网站的 LLM 合成来生成多样化的训练任务。Weblica-8B 模型在多个基准测试上以更少的推理步骤超越了类似规模的开源基线模型。

rss · arXiv - AI · May 11, 04:00

**背景**: 视觉网络代理是通过处理截图并执行点击或键入等操作来与网络界面交互的 AI 系统。由于网络的动态性以及对多样化、可复现环境的需求，训练此类代理具有挑战性。现有方法依赖于有限的离线轨迹或模拟环境，无法捕捉真实世界的多样性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2601.02439v3">WebGym: Scaling Training Environments for Visual Web Agents with...</a></li>
<li><a href="https://jykoh.com/vwa">VisualWebArena: Evaluating Multimodal Agents on Realistic Visual ...</a></li>

</ul>
</details>

**标签**: `#web agents`, `#reinforcement learning`, `#LLM`, `#scalable environments`, `#AI`

---

<a id="item-19"></a>
## [SCALAR：迭代批评提升大模型物理推理能力](https://arxiv.org/abs/2605.06772) ⭐️ 8.0/10

研究人员提出了 SCALAR，一个演员-评论家-裁判流水线，系统评估迭代批评如何提升大语言模型在量子场论和弦论问题上的表现，发现多轮对话始终优于单次尝试。 这项工作为理解研究人员与 AI 代理之间的哪些交互结构能促进科学发现提供了受控测试平台，对设计理论物理等领域更有效的 AI 助手具有重要意义。 研究变化了演员角色、评论家反馈策略和模型规模，发现增加模型规模（如从 DeepSeek-R1 8B 到 70B）改善了较简单的问题，但未解决最难的瓶颈，且评论家策略在非对称演员-评论家配对中最为重要。

rss · arXiv - AI · May 11, 04:00

**背景**: 大语言模型越来越多地被用于物理学研究级推理。从强化学习借鉴的演员-评论家框架包括演员提出解决方案和评论家提供反馈；SCALAR 增加了一个独立的裁判进行评估。这项工作探索了不同配对和反馈策略如何影响复杂理论物理问题的表现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">deepseek-ai/ DeepSeek - R 1 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI reasoning`, `#theoretical physics`, `#agentic AI`, `#critique`

---

<a id="item-20"></a>
## [RateQuant：基于率失真理论的最优混合精度 KV 缓存量化](https://arxiv.org/abs/2605.06675) ⭐️ 8.0/10

RateQuant 提出了一种基于率失真理论的最优混合精度 KV 缓存量化方法，识别并解决了现有方法中因失真模型不匹配而导致性能下降的故障模式。 这项工作通过实现更高效的 KV 缓存压缩，解决了 LLM 服务中的关键内存瓶颈，有望在保持模型质量的同时减少内存使用，这对于将 LLM 扩展到更长上下文至关重要。 RateQuant 从一个小型校准集中拟合每个量化器的失真模型，并通过率失真理论中的反向注水法解决比特分配问题。在 Qwen3-8B 上平均 2.5 比特时，它将 KIVI 的困惑度从 49.3 降至 14.9，并将 QuaRot 的困惑度提升 6.6，校准仅需在单个 GPU 上花费 1.6 秒。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: KV 缓存存储 LLM 生成过程中先前计算的关键值对，其大小随序列长度线性增长，成为主要的内存瓶颈。量化可以降低这些值的位宽，但现有方法对所有注意力头分配相同的位宽，忽略了头重要性的差异。混合精度量化旨在为重要头分配更多比特，但 RateQuant 揭示了不同量化器具有不同的失真曲线，使用一个量化器的模型为另一个量化器分配比特会导致失真模型不匹配，使性能比均匀量化更差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rate-distortion_theory">Rate-distortion theory</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>
<li><a href="https://grokipedia.com/page/Progressive_Mixed-Precision_KV_Cache_Quantization">Progressive Mixed-Precision KV Cache Quantization</a></li>

</ul>
</details>

**标签**: `#LLM`, `#KV cache quantization`, `#mixed-precision`, `#rate-distortion theory`, `#efficient inference`

---

<a id="item-21"></a>
## [LKV：学习型 KV 缓存淘汰方法提升 LLM 推理效率](https://arxiv.org/abs/2605.06676) ⭐️ 8.0/10

LKV 提出了一种端到端可微分的 KV 缓存淘汰框架，包含用于学习每头预算的 LKV-H 和用于令牌重要性评分的 LKV-T，在 LongBench 上仅保留 15%的 KV 缓存即可实现近乎无损的性能。 这项工作通过用学习型、任务优化的方法取代基于启发式的缓存管理，解决了长上下文 LLM 推理中的关键瓶颈，有望在内存受限环境中实现更高效的大模型部署。 LKV-H 通过可微松弛学习每个注意力头的全局预算，而 LKV-T 在不具体化注意力矩阵的情况下计算内在令牌重要性，绕过了注意力汇聚等启发式代理。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: 大型语言模型（LLM）使用键值（KV）缓存来存储中间注意力状态，其大小随序列长度线性增长，成为长上下文推理的内存瓶颈。现有的压缩方法依赖启发式规则进行预算分配和令牌选择，往往导致性能次优。

**标签**: `#LLM`, `#KV cache`, `#compression`, `#efficient inference`, `#deep learning`

---

<a id="item-22"></a>
## [PND：无需训练的解码方法减少 VLM 幻觉](https://arxiv.org/abs/2605.06679) ⭐️ 8.0/10

研究人员提出正负解码（PND），这是一种无需训练的推理框架，通过在解码过程中放大视觉证据并惩罚语言先验，减少视觉语言模型中的物体幻觉。 物体幻觉是 VLM 中的一个关键缺陷，削弱了对多模态 AI 的信任；PND 提供了一种实用的、无需重新训练的解决方案，可应用于现有模型，有望提高实际应用中的可靠性。 PND 引入了双路径对比：正路径放大视觉证据，负路径构建反事实以惩罚先验主导的生成。在 POPE、MME 和 CHAIR 基准上的实验表明，无需重新训练即可达到最先进性能。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: 视觉语言模型（VLM）如 LLaVA 基于视觉输入和语言先验生成文本，但常常过度依赖语言上下文，导致物体幻觉——描述图像中不存在的物体。现有的缓解方法通常需要额外的训练或微调，资源消耗大。PND 直接在推理时干预，调整解码过程以偏向视觉依据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.06679">Breaking the Illusion: When Positive Meets Negative in Multimodal...</a></li>
<li><a href="https://www.machinebrief.com/news/reining-in-ais-imagination-with-positive-and-negative-decodi-fgk4">Reining in AI's Imagination with Positive - and - Negative ... | Machine Brief</a></li>

</ul>
</details>

**标签**: `#Vision-Language Models`, `#Object Hallucination`, `#Decoding Strategy`, `#Multimodal AI`, `#Inference-time Intervention`

---

<a id="item-23"></a>
## [流匹配中的应变与涡量误差分析](https://arxiv.org/abs/2605.06680) ⭐️ 8.0/10

本文证明在流匹配数值积分中，应变导致误差指数放大，而涡量仅线性贡献，并提出加权雅可比正则化来减小误差。 这一理论见解可通过减少所需积分步数来提升如 Stable Diffusion 3 等生成模型的效率，在保持质量的同时降低推理成本。 分析将速度雅可比分解为应变率 S 和涡量Ω，表明应变通过对数范数控制误差。在二维数据实验中，NFE=5 时误差降低达 2.7 倍；CIFAR-10 微调在 NFE=10 时 FID 提升 14%。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: 流匹配是一种生成建模技术，通过学习速度场，利用常微分方程将噪声转化为数据。函数评估次数（NFE）决定推理成本，积分误差影响样本质量。对数范数是数值分析中用于界定 ODE 求解器误差增长的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Logarithmic_norm">Logarithmic norm - Wikipedia</a></li>

</ul>
</details>

**标签**: `#flow matching`, `#numerical integration`, `#generative modeling`, `#Jacobian regularization`

---

<a id="item-24"></a>
## [Toeplitz MLP Mixer：高效的次二次序列模型](https://arxiv.org/abs/2605.06683) ⭐️ 8.0/10

研究人员提出了 Toeplitz MLP Mixer（TMM），这是一种类似 Transformer 的架构，用三角掩码 Toeplitz 矩阵乘法替代注意力机制，在训练时实现 O(dn log n)时间和 O(dn)空间复杂度，推理预填充时为 O(dn)。 TMM 解决了 Transformer 的二次复杂度瓶颈，能够更高效地处理长序列，同时保留更多输入信息并提升复制能力，这对大型语言模型至关重要。 TMM 在序列维度上使用三角掩码 Toeplitz 矩阵，这是一种结构化矩阵，可通过 FFT 实现快速乘法。尽管缺乏输入调制或状态维护，TMM 在训练效率和信息保留方面优于同类次二次架构。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: Transformer 依赖注意力机制，其复杂度随序列长度呈二次增长，限制了长上下文的可扩展性。状态空间模型和线性注意力等次二次架构旨在降低这种复杂度。Toeplitz 矩阵沿对角线为常数，可通过 FFT 实现 O(n log n)的矩阵向量乘法，因此适合高效的序列混合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06683">[2605.06683] Toeplitz MLP Mixers are Low Complexity...</a></li>
<li><a href="https://arxiv.org/html/2605.06683">Toeplitz MLP Mixers are Low Complexity, Information-Rich Sequence...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#architecture`, `#efficiency`, `#transformers`, `#sequence models`

---

<a id="item-25"></a>
## [种系吸收扩散改进抗体设计](https://arxiv.org/abs/2605.06720) ⭐️ 8.0/10

研究人员提出了一种带有种系吸收噪声的分类器引导离散扩散模型，用于抗体序列的条件生成，将非种系残基预测准确率从 26%提升至 46%。 该方法解决了蛋白质语言模型在抗体设计中的关键局限，如种系偏差和缺乏灵活的条件生成能力，有望加速计算抗体疗法的开发。 该模型使用种系吸收扩散，其中种系序列作为吸收态，并支持基于任何现成分类器的条件生成，在疏水性和结合亲和力任务上优于 EvoProtGrad。

rss · arXiv - Machine Learning · May 11, 04:00

**背景**: 抗体设计通常依赖蛋白质语言模型（pLM），但这些模型倾向于记忆种系序列，且在条件生成方面存在困难。离散扩散模型提供了生成序列的概率框架，而分类器引导则能实现目标性质优化。

**标签**: `#antibody design`, `#discrete diffusion`, `#protein language models`, `#computational biology`, `#generative models`

---

<a id="item-26"></a>
## [33 个 LLM 的领域级元认知监测研究](https://arxiv.org/abs/2605.06673) ⭐️ 8.0/10

一项对 33 个前沿 LLM 的研究揭示了元认知监测质量在领域层面的系统性差异，其中应用/专业知识最容易监测，而形式推理和自然科学最难。 这一发现表明，聚合的元认知分数掩盖了重要的模型内差异，这对 AI 安全以及在特定应用领域的部署决策至关重要。 该研究使用了跨越六个领域的 1500 个 MMLU 题目，从口头化置信度分数中计算 Type-2 AUROC，并发现 Anthropic、Google-Gemini 和 Qwen 的族内轮廓形状聚类显著，而 DeepSeek、Google-Gemma 和 OpenAI 则不显著。

rss · arXiv - NLP · May 11, 04:00

**背景**: 元认知监测指的是 LLM 准确评估自身输出置信度的能力。MMLU 基准测试跨多个领域的知识，而 Type-2 AUROC 是评估置信度校准质量的指标。

**标签**: `#LLM`, `#metacognition`, `#AI evaluation`, `#MMLU`, `#benchmarking`

---

<a id="item-27"></a>
## [IntentGrasp 基准揭示 LLM 意图理解差距](https://arxiv.org/abs/2605.06832) ⭐️ 8.0/10

研究人员推出了 IntentGrasp，这是一个用于评估 LLM 意图理解能力的大规模基准测试，发现即使是 GPT-5.4 等前沿模型在 All Set 上得分低于 60%，在具有挑战性的 Gem Set 上得分低于 25%。 该基准测试揭示了当前 LLM 在意图理解方面的关键弱点，这对于构建可靠的 AI 助手至关重要，并提出了 Intentional Fine-Tuning (IFT)方法，显著提升了性能，为更安全、更强大的 AI 指明了方向。 IntentGrasp 包含 262,759 个训练实例和两个评估集（All Set 有 12,909 个案例，Gem Set 有 470 个案例），源自 12 个领域的 49 个语料库；20 个测试模型中有 17 个在 Gem Set 上的表现低于随机猜测（15.2%），而估计的人类表现约为 81.1%。

rss · arXiv - NLP · May 11, 04:00

**背景**: 意图理解是 LLM 从用户输入中正确推断其潜在目标或请求的能力。尽管语言模型取得了进展，但对此能力的系统性评估一直缺乏。IntentGrasp 通过提供多样化的大规模基准测试填补了这一空白。

**标签**: `#LLM`, `#benchmark`, `#intent understanding`, `#NLP`, `#evaluation`

---

<a id="item-28"></a>
## [提出以人为中心的大语言模型框架](https://arxiv.org/abs/2605.06901) ⭐️ 8.0/10

一篇新论文提出了以人为中心的大语言模型（HCLLM）框架，该框架在从设计到部署的整个开发流程中整合了伦理、经济和技术考量。 该框架通过确保在 LLM 开发的每个阶段（而不仅仅是训练后）都考虑人类价值观和优先级，回应了日益增长的对负责任 AI 的需求，可能影响行业实践和政策。 该框架结合了 NLP、人机交互和负责任 AI 的视角，为系统设计、数据采集、模型训练、评估和部署提供了具体建议，并包含一个关于未来工作的案例研究。

rss · arXiv - NLP · May 11, 04:00

**背景**: 大语言模型（如 GPT-4）是在海量文本数据上训练的神经网络，用于语言生成。尽管功能强大，但它们往往缺乏对人类价值观的明确考量，从而引发伦理问题。本文提出了一种系统方法，将“以人为中心”贯穿于 LLM 的整个生命周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.linkedin.com/top-content/artificial-intelligence/human-ai-collaboration/building-human-centered-large-language-models/">Building Human - Centered Large Language Models</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Human-Computer Interaction`, `#Responsible AI`, `#NLP`, `#Ethics`

---

<a id="item-29"></a>
## [LLM 无法根据检索信息确定性调整回应](https://arxiv.org/abs/2605.06919) ⭐️ 8.0/10

一项新研究评估了八个 LLM 在上下文确定性遵从性上的表现，发现系统性失败，但提出了一种结合提醒、重新校准和简化的交互策略，将遵从错误减少了 25%。 这项工作揭示了检索增强生成（RAG）系统中一个未被充分探索的关键局限性，对于医学和金融等高风险领域尤其令人担忧，因为这些领域常见不确定信息。 该研究测试了八个 LLM，发现它们在面对不确定上下文时难以回忆先验知识、误解确定性表述，并过度信任复杂上下文。提出的交互策略无需修改模型权重即可减少错误。

rss · arXiv - NLP · May 11, 04:00

**背景**: 检索增强生成（RAG）系统将 LLM 与外部知识检索相结合以提高事实准确性。然而，检索到的信息通常带有不同程度的确定性（例如置信度分数、模糊措辞）。本研究系统性地考察了 LLM 如何处理这种不确定性。

**标签**: `#LLM`, `#Retrieval-Augmented Generation`, `#Uncertainty`, `#Reliability`, `#Interaction Design`

---

<a id="item-30"></a>
## [测度传输理论解释视觉文本压缩](https://arxiv.org/abs/2605.06708) ⭐️ 8.0/10

一篇新论文将视觉文本压缩（VTC）形式化为测度传输问题，引入了一个原则性框架来量化将文本渲染为图像供视觉语言模型处理时与任务相关的信息损失。 这项工作解决了理解压缩比为何不能预测下游性能的关键空白，实现了无标签路由和自适应注视机制，在 24 个 NLP 数据集上提升了效率和准确性。 该框架将传输成本分解为精度成本（块内聚合）和覆盖成本（跨块碎片化），两者均无需下游标签即可估计。其无标签路由规则在 17/24 个数据集（70.8%）上与每个数据集的 oracle 匹配，平均任务得分提高+3.3%，平均令牌数减少-10.3%。

rss · arXiv - Computer Vision · May 11, 04:00

**背景**: 视觉文本压缩（VTC）将长文本渲染为图像，并用视觉语言模型重新编码，通常比子词分词产生 3-20 倍更少的解码器令牌。然而，令牌节省并不能可靠地转化为更好的任务性能，仅凭压缩比无法预测视觉编码何时有帮助或有害。测度传输是来自最优传输理论的数学框架，通过考虑将质量从一个分布移动到另一个分布的成本来比较概率分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Information_theory">Information theory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Glyph_visual-text_compression">Glyph (visual-text compression)</a></li>

</ul>
</details>

**标签**: `#visual text compression`, `#measure transport`, `#vision-language models`, `#long-context processing`, `#information theory`

---

<a id="item-31"></a>
## [LookWhen：通过令牌选择实现高效视频识别](https://arxiv.org/abs/2605.06809) ⭐️ 8.0/10

LookWhen 提出了一种选择器-提取器框架，学习何时、何处以及计算什么，使用浅层选择器对令牌进行评分，深层提取器仅处理前 K 个令牌，在近似全视频表示的同时降低计算成本。 这项工作解决了视频 transformer 中的计算冗余问题，在多个基准上实现了更好的精度-计算权衡，并可能使资源受限设备上的视频理解更加高效。 选择器预训练使用最近邻距离按唯一性对令牌排序，提取器则从视频教师和图像教师（具有归一化的逐帧表示）中蒸馏。LookWhen 在同等精度下比 InternVideo2-B 快 6.7 倍。

rss · arXiv - Computer Vision · May 11, 04:00

**背景**: 视频 transformer 通过将视频分割成时空令牌来处理，但计算成本随令牌数量超线性增长。视频包含大量冗余，因此并非所有令牌都具有相同的信息量。LookWhen 通过仅选择信息量最大的令牌进行处理来利用这一点。

**标签**: `#video recognition`, `#efficient deep learning`, `#transformer`, `#token selection`, `#distillation`

---

<a id="item-32"></a>
## [3D 医学影像知识迁移的缩放定律](https://arxiv.org/abs/2605.06859) ⭐️ 8.0/10

该论文发现 3D 医学影像领域存在非对称知识迁移和幂律缩放现象，提出了一种基于缩放定律的数据分配优化方法，其性能比数据比例采样高出 58%。 这项工作为 3D 医学影像基础模型的多模态预训练中的数据分配提供了原则性框架，有望显著提升多种临床任务的效率和性能。 推导出的分配方案揭示了枢纽-岛屿结构：高迁移性领域（枢纽）惠及众多其他领域，而孤立领域（岛屿）需要直接投入。迁移感知分配对未见预算的泛化相关性达到 r=0.989。

rss · arXiv - Computer Vision · May 11, 04:00

**背景**: 视觉基础模型正从 2D 扩展到 3D 医学影像领域，跨 CT、MRI 和 PET 等模态的统一预训练可为多种临床任务提供基础模型。当前混合异构影像领域的策略主要依赖启发式方法。该论文引入缩放定律来指导此类多模态预训练中的数据分配。

**标签**: `#scaling laws`, `#medical imaging`, `#transfer learning`, `#vision foundation models`, `#3D`

---

<a id="item-33"></a>
## [HSA：用于高效视频扩散 Transformer 的异构步长分配](https://arxiv.org/abs/2605.06892) ⭐️ 8.0/10

研究人员提出异构步长分配（HSA），这是一种无需训练即可根据速度动态为不同令牌分配不同去噪步数的推理方法，从而降低视频生成扩散 Transformer 的计算成本。 HSA 引入了 KV 缓存同步机制来处理序列长度不匹配问题，以及缓存欧拉更新来推进跳过的令牌而无需额外模型评估。在 Wan-2 和 LTX-2 模型上，HSA 优于先前的缓存方法，尤其在 50%和 25%运行时间下表现突出。

rss · arXiv - Computer Vision · May 11, 04:00

**背景**: 扩散 Transformer（DiT）在视频生成中达到最先进水平，但每个令牌需要大量去噪步骤，导致计算成本高昂。标准推理对所有令牌应用均匀步数，忽略了人类视觉可以跳过冗余运动。HSA 利用速度动态来异构分配步数。

**标签**: `#Diffusion Transformers`, `#Video Generation`, `#Efficient Inference`, `#KV-cache`, `#Deep Learning`

---

<a id="item-34"></a>
## [注意力机制：随机矩阵理论对信号恢复的洞见](https://arxiv.org/abs/2605.06826) ⭐️ 8.0/10

该论文推导了由池化序列表示构成的样本协方差矩阵的精确谱特征，揭示了由注意力权重和词汇结构控制的信号恢复中的相变。 这项工作为理解注意力机制如何帮助信号恢复提供了严格的理论基础，可能指导更高效的 Transformer 模型和基于注意力的架构的设计。 分析表明，最大化信噪比的最优注意力权重由位置相关矩阵的主特征向量给出，且具有τ/d 分数缩放的无参数因果自注意力产生确定性调和权重，当早期 token 携带更多信号时，其信号恢复优于平均池化。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: 随机矩阵理论研究大型随机矩阵的谱性质，在高维统计和机器学习中有应用。Marchenko-Pastur 定律描述了样本协方差矩阵的特征值分布，其自由乘法卷积将其推广到结构化设置。Transformer 中的注意力机制动态加权 token 贡献，理解其理论性质对模型可解释性和改进至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Marchenko–Pastur_distribution">Marchenko – Pastur distribution - Wikipedia</a></li>

</ul>
</details>

**标签**: `#attention`, `#random matrix theory`, `#deep learning theory`, `#signal recovery`, `#transformers`

---

<a id="item-35"></a>
## [神经算子学习任意联合密度的条件分布](https://arxiv.org/abs/2605.06873) ⭐️ 8.0/10

本文提出学习一个单一的神经算子，将任意联合密度映射到其条件分布，从而在联合-条件对上进行摊销，并提供了任意精度的理论保证。 这项工作为通用、摊销的概率条件化提供了理论基础，可能为贝叶斯推理的基础模型铺平道路，并推动机器学习中的不确定性量化。 作者证明了条件算子在适当密度类上的连续性，并在高斯混合模型上使用神经算子展示了该框架。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: 概率条件化是根据一个随机变量更新另一个随机变量分布的过程，是不确定性量化的基础。传统方法针对固定的联合分布学习条件分布，而本文旨在学习一个适用于任意联合密度的算子。神经算子是一种深度学习架构，用于学习函数空间之间的映射，最初是为求解偏微分方程而开发的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neural_operators">Neural operators</a></li>

</ul>
</details>

**标签**: `#probabilistic conditioning`, `#neural operators`, `#uncertainty quantification`, `#machine learning`, `#amortized inference`

---

<a id="item-36"></a>
## [将核选择视为模型选择以改进 MMD 检验](https://arxiv.org/abs/2605.06883) ⭐️ 8.0/10

本文提出了复杂度惩罚 MMD（CP-MMD），将核选择视为模型选择问题，能够在连续核类上进行无网格优化，同时防止过拟合。 CP-MMD 通过数学上考虑优化复杂度，解决了非参数两样本检验中的一个基本限制，确保无条件的第一类错误控制，并在线性、多项式和深度核场景中最大化检验功效。 CP-MMD 中的惩罚项通过两样本均匀集中不等式，用核搜索空间的复杂度来约束经验 MMD，从而允许在连续参数类（如标量带宽和深度网络参数）上进行直接最大化。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: 最大均值差异（MMD）是一种用于检验两个分布是否不同的统计量，但其功效依赖于核的选择。数据驱动的核优化违反了独立同分布假设，导致基于比率的方法出现过拟合，或聚合方法可扩展性有限。CP-MMD 通过将核选择视为带有复杂度惩罚的模型选择问题来解决这一问题。

**标签**: `#kernel methods`, `#two-sample test`, `#MMD`, `#model selection`, `#statistical learning theory`

---

<a id="item-37"></a>
## [可解释的 IRT 框架用于可扩展的大语言模型评估](https://arxiv.org/abs/2605.07046) ⭐️ 8.0/10

研究人员提出了一种新框架，将用于大语言模型评估的项目反应理论（IRT）重新表述为约束矩阵分解，利用 MM 算法实现稳定高效的参数估计。该方法在 MATH-500 和 Open LLM Leaderboard 等基准测试上比传统 IRT 方法快数个数量级。 当前大语言模型评估依赖平均准确率，忽略了项目的异质性和输出的随机性。该框架提供可解释的能力估计和项目特征，有助于更合理的基准设计和更公平的模型比较，在大语言模型广泛部署的背景下至关重要。 该框架将 IRT 重新表述为一系列约束矩阵分解子问题，具有可识别性和收敛性的理论保证。实验表明，它在保持相当或更高估计精度的同时，速度显著快于竞争方法。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: 项目反应理论（IRT）是一种心理测量学范式，将正确响应的概率建模为潜在能力和项目参数（难度、区分度）的函数。传统的 IRT 估计方法在大规模大语言模型评估中计算成本高且数值不稳定。该提出的方法通过利用 MM 算法和矩阵分解技术解决了这些限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Item_response_theory">Item response theory</a></li>

</ul>
</details>

**标签**: `#Large Language Models`, `#Evaluation`, `#Item Response Theory`, `#Matrix Factorization`, `#Scalability`

---

<a id="item-38"></a>
## [TRACE：基于扩散与流匹配的传输对齐共形预测](https://arxiv.org/abs/2605.07100) ⭐️ 8.0/10

TRACE 提出了一种新的共形预测非一致性分数，利用扩散和流匹配模型中的传输对齐，避免了限制性假设和似然评估。 这项工作为多维输出提供了有效且信息丰富的共形预测区域，对于复杂生成模型和可靠 AI 系统中的不确定性量化至关重要。 该方法沿随机传输轨迹平均去噪或速度匹配误差以产生标量分数，并使用分裂共形预测进行校准，以保证可交换性下的边际覆盖。

rss · arXiv - Data Science & Statistics · May 11, 04:00

**背景**: 共形预测是一种为预测集提供有限样本、无分布覆盖保证的框架。然而，现有的多维输出非一致性分数通常依赖于限制性几何假设或需要显式似然评估，限制了其适用性。扩散和流匹配模型是通过随机传输过程学习数据分布的生成模型。

**标签**: `#conformal prediction`, `#diffusion models`, `#flow matching`, `#uncertainty quantification`, `#machine learning`

---