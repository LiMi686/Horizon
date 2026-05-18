---
layout: default
title: "Horizon Summary: 2026-05-18 (ZH)"
date: 2026-05-18
lang: zh
---

> From 83 items, 35 important content pieces were selected

---

1. [Bun：一体化 JavaScript 运行时与工具链](#item-1) ⭐️ 9.0/10
2. [NOVA 框架揭示 AI 知识发现的基本极限](#item-2) ⭐️ 9.0/10
3. [罗韦利主张放弃意识的困难问题](#item-3) ⭐️ 8.0/10
4. [16 字节 x86 程序同时生成矩阵雨和音乐](#item-4) ⭐️ 8.0/10
5. [GDS 建议 NHS 保持开源仓库开放](#item-5) ⭐️ 8.0/10
6. [CLI-Anything：让所有软件原生支持 AI 代理](#item-6) ⭐️ 8.0/10
7. [生产级 GenAI 代理的开源手册](#item-7) ⭐️ 8.0/10
8. [港大数据科学团队发布 ViMax：全能智能体视频生成框架](#item-8) ⭐️ 8.0/10
9. [心智理论基准无法预测真实人机交互](#item-9) ⭐️ 8.0/10
10. [LLM 输出公平但内部存在偏见](#item-10) ⭐️ 8.0/10
11. [ICRL：通过强化学习内化自我批评](#item-11) ⭐️ 8.0/10
12. [可验证代理授权的分布式信任框架](#item-12) ⭐️ 8.0/10
13. [AgentStop：提前终止本地 LLM 代理以节省能源](#item-13) ⭐️ 8.0/10
14. [TeamTR：多智能体大语言模型协调的信任域微调](#item-14) ⭐️ 8.0/10
15. [量化可能重新引入 LLM 中的偏见](#item-15) ⭐️ 8.0/10
16. [MuteBench：传感器故障下多模态融合鲁棒性基准测试](#item-16) ⭐️ 8.0/10
17. [在线策略自蒸馏降低 LLM 安全税](#item-17) ⭐️ 8.0/10
18. [转录组引导的扩散模型用于药物设计](#item-18) ⭐️ 8.0/10
19. [生成式轨迹模型隐私评估的空白](#item-19) ⭐️ 8.0/10
20. [GQLA：通过双路径注意力实现硬件自适应的大模型解码](#item-20) ⭐️ 8.0/10
21. [OP-Mix：大模型训练全生命周期的统一数据混合算法](#item-21) ⭐️ 8.0/10
22. [从 1 亿份乌克兰法院判决构建大规模法律引用图](#item-22) ⭐️ 8.0/10
23. [Eskwai：基于 RAG 的加纳法律教育 AI 助手](#item-23) ⭐️ 8.0/10
24. [LLM 架构的神经激活模式分析](#item-24) ⭐️ 8.0/10
25. [语言模型为何比人类更不惊讶？解析多重性假设测试](#item-25) ⭐️ 8.0/10
26. [深度预对齐提升视觉语言模型性能](#item-26) ⭐️ 8.0/10
27. [递归潜在细化提升生成模型多样性](#item-27) ⭐️ 8.0/10
28. [Minerva-Ego：自我中心视频推理新基准](#item-28) ⭐️ 8.0/10
29. [特征空间采样降低 3D 群卷积神经网络计算成本](#item-29) ⭐️ 8.0/10
30. [MorphoHELM：细胞绘画综合基准测试](#item-30) ⭐️ 8.0/10
31. [MaxSketch：通过随机投影实现鲁棒的不同元素计数](#item-31) ⭐️ 8.0/10
32. [α-TCAV：修复概念激活向量的统计不稳定性](#item-32) ⭐️ 8.0/10
33. [通过子空间归因实现可解释的域偏移检测](#item-33) ⭐️ 8.0/10
34. [可解释 AI 还不够：重新思考算法可争议性](#item-34) ⭐️ 8.0/10
35. [偏态自适应共形预测提升区间效率](#item-35) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Bun：一体化 JavaScript 运行时与工具链](https://github.com/oven-sh/bun) ⭐️ 9.0/10

Bun 是一个一体化的 JavaScript 运行时、打包器、测试运行器和包管理器，旨在用一个可执行文件替代 Node.js 和多个工具。它于 2021 年 9 月首次发布，并因其速度和集成度而获得了广泛关注。 Bun 通过将运行时、打包器、测试运行器和包管理器整合到一个工具中，极大地简化了 JavaScript 开发，降低了复杂性并提高了性能。它使用 JavaScriptCore 而非 V8，并基于 Zig 实现，相比 Node.js 提供了更快的启动速度和更低的内存使用。 Bun 支持 Linux、macOS 和 Windows，可通过 curl、npm、Homebrew 或 Docker 安装。它被设计为 Node.js 的直接替代品，现有 Node.js 项目只需很少改动即可使用 Bun。

rss · GitHub Trending - Daily (All) · May 18, 15:38

**背景**: 传统上，JavaScript 开发者使用 Node.js 作为运行时，npm 或 yarn 进行包管理，Jest 或 Mocha 进行测试，以及 Webpack 或 esbuild 进行打包。Bun 旨在用一个命令行工具替代所有这些，通过使用 JavaScriptCore（Safari 的引擎）和 Zig 编程语言来提供显著的性能提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>

</ul>
</details>

**标签**: `#JavaScript`, `#runtime`, `#tooling`, `#performance`, `#open-source`

---

<a id="item-2"></a>
## [NOVA 框架揭示 AI 知识发现的基本极限](https://arxiv.org/abs/2605.15219) ⭐️ 9.0/10

NOVA 框架将 AI 自我改进循环建模为知识空间上的自适应采样过程，识别了真正发现的条件以及包括污染陷阱在内的多种失败模式。它还证明了一个缩放定律：累积生成成本随不同发现数量 D 的增长呈Θ(c_gen D^α)关系。 这项工作为理解 AI 系统何时能真正发现新知识而非仅仅利用现有数据提供了理论基础，对设计可靠的自我改进 AI 至关重要。所识别的污染陷阱警告：随着容易发现的耗尽，即使很小的假阳性率也可能使无效产物淹没真正发现。 该框架识别了四种失败模式：污染、遗忘、探索失败和接受失败。它澄清了 Good-Turing 估计是局部批次多样性诊断工具，而非历史未发现有效质量的估计器，并表明专家人类输入在自主探索障碍附近最有价值。

rss · arXiv - AI · May 18, 04:00

**背景**: AI 自我改进循环包括生成候选、验证、积累有效候选并重新训练模型。NOVA 框架将其形式化为知识空间上的自适应采样，每次发现都会减少剩余未发现的质量。推导出的缩放定律假设发现难度服从指数α>1 的 Zipf 分布。

**标签**: `#AI`, `#knowledge discovery`, `#theoretical framework`, `#machine learning`, `#self-improvement`

---

<a id="item-3"></a>
## [罗韦利主张放弃意识的困难问题](https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/) ⭐️ 8.0/10

理论物理学家卡洛·罗韦利发表文章，认为意识的困难问题是一个哲学死胡同，应将意识视为自然现象进行经验研究。 这挑战了心灵哲学和认知科学中的一个基础性辩论，可能将研究焦点从形而上学难题转向对意识的经验研究。 罗韦利类比了历史上的科学重新定义，如热的概念，并主张当我们把意识视为自然现象而非独立实体时，困难问题就消解了。

hackernews · ahalbert4 · May 18, 02:59 · [社区讨论](https://news.ycombinator.com/item?id=48175140)

**背景**: 意识的困难问题由哲学家大卫·查尔默斯于 1994 年提出，询问大脑中的物理过程为何以及如何产生主观体验（感受质）。它与可进行功能解释的“简单问题”形成对比。困难问题的存在性存在争议；一些哲学家和科学家拒绝它，而另一些人则认为它是一个真正的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hard_problem_of_consciousness">Hard problem of consciousness</a></li>
<li><a href="https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/">There Is No ‘Hard Problem Of Consciousness’ | NOEMA</a></li>

</ul>
</details>

**社区讨论**: 评论显示了实质性的辩论：一些人同意意识应像热一样被重新定义，而另一些人则认为文章缺乏证据，我们遗漏了某些基本的东西，类似于前电磁学时代的理解。

**标签**: `#consciousness`, `#philosophy`, `#cognitive science`, `#AI`, `#neuroscience`

---

<a id="item-4"></a>
## [16 字节 x86 程序同时生成矩阵雨和音乐](https://hellmood.111mb.de//wake_up_16b_writeup.html) ⭐️ 8.0/10

一篇详细文章介绍了一个 16 字节的 x86 实模式程序，它能同时显示类似《黑客帝国》的字符雨视觉效果，并通过 PC 扬声器生成音乐。 这展示了演示场景中极致的尺寸编码，将仅 16 字节所能实现的效果推向极限，激励其他开发者探索底层优化。 该程序在 x86 实模式下运行，利用 PC 扬声器的可编程间隔定时器生成音频，同时通过直接写入视频内存来创建视觉效果。

hackernews · HellMood · May 17, 23:10 · [社区讨论](https://news.ycombinator.com/item?id=48173962)

**背景**: 尺寸编码是演示场景中的一个分支，旨在将程序压缩到极小（例如 64 字节或更少），同时仍能产生令人印象深刻的图形和声音。PC 扬声器是一种早期的计算机音频设备，通过定时器芯片生成简单音调。实模式是 x86 处理器上的一种 16 位操作模式，允许直接访问硬件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.youtube.com/watch?v=f-VQfigEoO0">The Art of Code Wrestling in the Demoscene – Size ... - YouTube</a></li>
<li><a href="https://en.wikipedia.org/wiki/PC_speaker">PC speaker - Wikipedia</a></li>
<li><a href="https://wiki.osdev.org/Protected_Mode">Protected Mode - OSDev Wiki</a></li>

</ul>
</details>

**社区讨论**: 评论者将该演示与其他微型演示（如“Freespin”和“A Mind Is Born”）进行比较，称赞其在 16 字节内结合音频和视觉的惊人成就。一位用户评论说，他们的评论本身都比这个程序大。

**标签**: `#demoscene`, `#x86`, `#low-level programming`, `#audio-visual`, `#size coding`

---

<a id="item-5"></a>
## [GDS 建议 NHS 保持开源仓库开放](https://simonwillison.net/2026/May/17/gds-weighs-in/#atom-everything) ⭐️ 8.0/10

英国政府数字服务（GDS）于 2026 年 5 月 14 日发布指南，建议公共部门组织默认保持开源仓库开放，这反驳了 NHS 在通过 Project Glasswing 报告漏洞后关闭其仓库的决定。 这一干预标志着英国政府内部出现重大政策分歧，GDS 公开反驳 NHS 以安全为由退出开源的做法，可能为整个公共部门使用开源树立先例。 GDS 的指南题为《AI、开放代码与公共部门漏洞风险》，强调将仓库设为私有会增加成本并降低复用和审查，建议仅在有意例外时关闭。Terence Eden 将此解读为罕见的内部公务员分歧公开化。

rss · Simon Willison · May 17, 15:59

**背景**: Project Glasswing 是 Anthropic 于 2026 年 4 月发起的网络安全计划，利用先进 AI 查找关键开源软件中的漏洞。NHS 对此项目报告的漏洞作出回应，关闭了其开源仓库，此举受到开源倡导者的批评。GDS 是英国政府的数字转型部门，负责制定整个公共部门的数字标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Government_Digital_Service">Government Digital Service - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/glasswing">Project Glasswing: Securing critical software for the AI era</a></li>

</ul>
</details>

**标签**: `#open source`, `#government policy`, `#security`, `#NHS`, `#GDS`

---

<a id="item-6"></a>
## [CLI-Anything：让所有软件原生支持 AI 代理](https://github.com/HKUDS/CLI-Anything) ⭐️ 8.0/10

HKUDS 发布了 CLI-Anything，这是一个开源框架和中心，能为任何软件生成 CLI 封装器，让 AI 代理能够无缝与之交互。该项目还包括 CLI-Hub，一个用于共享和安装这些 CLI 的社区仓库。 该项目弥合了现有软件与 AI 代理之间的鸿沟，使得几乎任何应用都能被代理控制，而无需原生 API 支持。它通过提供通用集成层，可能加速 AI 代理在实际工作流中的采用。 CLI-Anything 使用 Click 生成标准的 Python CLI 包，输出 JSON 格式供代理使用，同时提供人类可读的输出。CLI-Hub 允许用户通过简单的命令行界面浏览、安装和管理社区贡献的 CLI。

rss · GitHub Trending - Daily (All) · May 18, 15:38

**背景**: AI 代理通常需要程序化接口（API）才能与软件交互，但许多应用缺乏此类接口。CLI-Anything 通过创建命令行封装器，以结构化方式暴露软件功能，使其成为代理原生软件。代理原生软件的概念是指设计为由 AI 代理自主操作的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HKUDS/CLI-Anything">GitHub - HKUDS/CLI-Anything: "CLI-Anything: Making ALL Software Agent ...</a></li>
<li><a href="https://clianything.org/">CLI Anything</a></li>
<li><a href="https://sourceforge.net/projects/cli-anything.mirror/">CLI-Anything download | SourceForge.net</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#CLI`, `#Software Integration`, `#Open Source`, `#Tooling`

---

<a id="item-7"></a>
## [生产级 GenAI 代理的开源手册](https://github.com/NirDiamant/agents-towards-production) ⭐️ 8.0/10

NirDiamant 发布了'Agents Towards Production'，这是一个包含 28 个代码优先教程的开源仓库，用于构建和部署生产级生成式 AI 代理。 该资源弥合了原型与企业部署之间的差距，涵盖了安全、多代理协调和 GPU 扩展等关键主题，这些对于实际 GenAI 应用至关重要。 教程包括有状态工作流、向量记忆、Docker 部署、FastAPI 端点、安全护栏、可观测性和评估，使用 LangGraph 和 LangChain 等框架。

rss · GitHub Trending - Daily (All) · May 18, 15:38

**背景**: GenAI 代理是构建在大语言模型（LLM）上的自主系统，能以最少的人工输入完成任务。LangGraph 是一个用于构建可靠、有状态代理的编排框架，而 LangChain 则简化了 LLM 与应用程序的集成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NirDiamant/GenAI_Agents">GitHub - NirDiamant/ GenAI _ Agents : 50+ tutorials and implementations...</a></li>
<li><a href="https://www.langchain.com/langgraph">LangGraph : Agent Orchestration Framework for Reliable AI Agents</a></li>
<li><a href="https://en.wikipedia.org/wiki/LangChain">LangChain - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GenAI`, `#agents`, `#production`, `#tutorials`, `#open-source`

---

<a id="item-8"></a>
## [港大数据科学团队发布 ViMax：全能智能体视频生成框架](https://github.com/HKUDS/ViMax) ⭐️ 8.0/10

ViMax 是香港大学数据科学实验室推出的开源多智能体视频生成框架，将导演、编剧、制片人和视频生成器角色整合到一个系统中，实现自动化多镜头视频生成，并保持角色和场景的一致性。 ViMax 通过提供端到端的解决方案，自动化剧本编写、分镜、角色创建和视频生成，解决了当前 AI 视频工具的关键限制——短片、不一致性和缺乏叙事结构，有望为内容创作者减少 40-60%的制作时间。 ViMax 声称比传统模型连贯性提升 35%，支持 Python 3.12 和 uv 包管理器。该框架采用 MIT 许可证，并包含快速入门指南以便部署。

rss · GitHub Trending - Python · May 18, 15:38

**背景**: 当前的 AI 视频生成工具通常只能生成短片，角色和场景不一致，且缺乏叙事深度。ViMax 采用多智能体方法，由专门的 AI 智能体处理视频制作的不同方面，类似于人类电影摄制组，从简单的概念输入创建连贯的多镜头视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/HKUDS/ViMax">GitHub - HKUDS / ViMax : " ViMax : Agentic Video Generation (Director...)</a></li>
<li><a href="https://pixel4it.com/vimax-agentic-video-generation-guide/">ViMax Agentic Video Generation: A Designer's Complete Guide</a></li>
<li><a href="https://sutopo.com/vimax-ai-agentic-video-generation-review/">ViMax AI Agentic Video Generation Review - sutopo.com</a></li>

</ul>
</details>

**标签**: `#video generation`, `#AI agents`, `#machine learning`, `#computer vision`, `#generative AI`

---

<a id="item-9"></a>
## [心智理论基准无法预测真实人机交互](https://arxiv.org/abs/2605.15205) ⭐️ 8.0/10

一项新研究提出了 LLM 心智理论的交互式评估范式，发现静态基准上的改进并不能转化为更好的人机交互。 这挑战了现有心智理论基准的有效性，并强调了基于交互的评估对于开发面向真实世界应用的社交感知 LLM 的必要性。 该研究系统评估了四种心智理论增强技术，涉及四个数据集和一项用户研究，涵盖目标导向和体验导向任务。

rss · arXiv - AI · May 18, 04:00

**背景**: 心智理论（ToM）是将心理状态归因于自己和他人的能力，对社会互动至关重要。现有的 LLM 心智理论基准通常使用静态的第三人称选择题，可能无法捕捉人机交互的动态性和第一人称特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Theory_of_mind_in_animals">Theory of mind in animals</a></li>
<li><a href="https://link.springer.com/rwe/10.1007/978-981-97-8440-0_6-1">Theory of Mind in Human-AI Interaction and AI - Springer</a></li>

</ul>
</details>

**标签**: `#Theory of Mind`, `#Large Language Models`, `#Human-AI Interaction`, `#Evaluation Benchmark`

---

<a id="item-10"></a>
## [LLM 输出公平但内部存在偏见](https://arxiv.org/abs/2605.15217) ⭐️ 8.0/10

一篇新论文揭示，指令微调的大语言模型可以抑制输出层面的偏见，但在内部表示中仍保留不对称的潜在偏见，当这些偏见被重新注入时，能够因果性地逆转决策。 这一发现对于抵押贷款审批等高 stakes 领域至关重要，因为它表明仅关注输出的行为审计是不够的，可被利用的内部偏见可能未被察觉地持续存在。 通过激活引导和新型跨层干预方法，作者证明在关键层重新注入被抑制的人口统计表示可导致近乎完全的决策逆转，且该效应在不同人口群体间是不对称的。

rss · arXiv - AI · May 18, 04:00

**背景**: 指令微调的大语言模型经过训练以遵循指令，通常表现出公平的输出。然而，它们内部可能仍编码了有偏见的关联。激活引导是一种推理时技术，通过调整内部激活来控制输出。本文使用因果干预方法来探究这些内部偏见是否能因果性地影响决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15217v1">Fair outputs, Biased Internals: Causal Potency and Asymmetry of Latent ...</a></li>
<li><a href="https://www.emergentmind.com/topics/activation-steering-method">Activation Steering in LLMs</a></li>
<li><a href="https://raktimsingh.com/counterfactual-causality-neural-networks-interventions/">Counterfactual Causality Inside Neural Networks ... - Raktim Singh</a></li>

</ul>
</details>

**标签**: `#LLM fairness`, `#latent bias`, `#causal intervention`, `#high-stakes decisions`, `#AI safety`

---

<a id="item-11"></a>
## [ICRL：通过强化学习内化自我批评](https://arxiv.org/abs/2605.15224) ⭐️ 8.0/10

研究人员提出了 ICRL，一种强化学习框架，它从共享骨干网络联合训练求解器和批评者，以内化批评，使模型无需外部反馈即可纠正错误。该方法在 Qwen3-4B 和 Qwen3-8B 骨干网络上，在智能体任务上平均比 GRPO 提升 6.4 个点，在数学推理上提升 7.0 个点。 ICRL 解决了当前 LLM 自我改进方法的一个关键局限，即模型在移除批评后无法保留改进。通过内化批评，它增强了 AI 对齐和智能体能力，可能减少对外部监督的依赖。 ICRL 引入了分布校准重加权比率来处理批评条件行为和无批评行为之间的分布偏移，以及角色分组优势估计来稳定联合优化。学习到的 8B 批评者与 32B 批评者性能相当，但使用的 token 数量大幅减少。

rss · arXiv - AI · May 18, 04:00

**背景**: 大型语言模型（LLM）经常犯错，外部批评可以引导它们纠正行为。然而，当批评被移除时，模型可能再次失败，表明它没有内化指导。ICRL 使用强化学习联合训练求解器和批评者，其中批评者根据求解器的性能提升获得奖励，从而激励求解器可以内化的可操作反馈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15224v1">ICRL: Learning to Internalize Self-Critique with Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#self-improvement`, `#AI alignment`, `#critique`

---

<a id="item-12"></a>
## [可验证代理授权的分布式信任框架](https://arxiv.org/abs/2605.15228) ⭐️ 8.0/10

一篇新论文提出了分布式信任框架（DTF），这是一种验证框架，用基于证明的授权取代了主权系统中自主 AI 代理的静态身份授权。 这解决了 AI 安全中的一个关键空白：自主代理即使拥有有效凭证也可能生成不安全操作。DTF 使代理执行变得可治理、可审计且有边界，这对云基础设施、受监管数据和国家级数字服务至关重要。 DTF 引入了合理性证明来编码操作的许可依据、用于独立评估的共识模型、从已批准证明派生的临时执行身份，以及仅追加的证据链。该框架在基于 OpenKedge 的受控变异基板上实例化。

rss · arXiv - AI · May 18, 04:00

**背景**: 传统授权假设拥有有效凭证的调用者是安全的，但自主 AI 代理可能生成语法有效但语义不安全的操作。受控变异基板通过要求意图并评估上下文和策略来干预代理操作，但将信任边界转移到了授权决策本身。DTF 使该决策变得可验证、分布式且可重放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15228">[2605.15228] Verifiable Agentic Infrastructure: Proof - Derived ...</a></li>
<li><a href="https://www.openkedge.io/">OpenKedge — Governance Protocol for AI-Driven Mutation</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#authorization`, `#autonomous agents`, `#distributed systems`, `#verification`

---

<a id="item-13"></a>
## [AgentStop：提前终止本地 LLM 代理以节省能源](https://arxiv.org/abs/2605.15206) ⭐️ 8.0/10

研究人员提出了 AgentStop，这是一种轻量级的效率监督器，能够预测并提前终止本地 LLM 代理中不太可能成功的执行轨迹，从而减少 15-20%的能源浪费，同时效用损失低于 5%。 这项工作解决了本地 LLM 代理能源效率低下的关键问题，对于在消费设备上实现可持续的边缘 AI 部署和隐私保护自动化至关重要。 AgentStop 利用低成本的执行信号（如 token 级别的对数概率）来做出终止决策，并在消费级硬件上针对基于网页的问答和编程基准进行了评估。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: LLM 代理是使用大型语言模型自主执行多步骤任务（如编程或网络研究）的 AI 系统。在用户设备上本地部署可以保护隐私并避免 API 成本，但由于迭代推理、工具使用和重试，代理工作流比单次 LLM 推理消耗更多能源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.15075v1">Atropos: Improving Cost-Benefit Trade-off of LLM-based Agents under Self-Consistency with Early Termination and Model Hotswap - arXiv</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#energy efficiency`, `#edge AI`, `#sustainable computing`

---

<a id="item-14"></a>
## [TeamTR：多智能体大语言模型协调的信任域微调](https://arxiv.org/abs/2605.15207) ⭐️ 8.0/10

TeamTR 提出了一种信任域微调框架，解决了多智能体大语言模型团队中的累积占用偏移问题，相比基线平均提升 7.1%。 该工作识别并形式化了多智能体大语言模型微调中的一个关键失败模式，并提供了具有理论保证的解决方案，对推进可靠的多智能体大语言模型系统至关重要。 论文证明，陈旧占用评估的惩罚随智能体数量呈二次方增长，而中间占用评估将其降低为线性增长。TeamTR 在每个组件更新后重新采样轨迹，并对每个智能体实施散度控制。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: 多智能体大语言模型系统涉及多个语言模型协作完成任务，但顺序微调可能导致分布偏移在智能体间累积。信任域方法在强化学习中常见，通过约束策略更新来确保稳定改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.05216">[2605.05216] SAT: Sequential Agent Tuning for Coordinator Free Plug and Play Multi-LLM Training with Monotonic Improvement Guarantees - arXiv</a></li>
<li><a href="https://arxiv.org/abs/2508.10340">[2508.10340] Multi-Agent Trust Region Policy Optimisation: A Joint Constraint Approach</a></li>

</ul>
</details>

**标签**: `#multi-agent LLM`, `#fine-tuning`, `#trust-region`, `#coordination`, `#reinforcement learning`

---

<a id="item-15"></a>
## [量化可能重新引入 LLM 中的偏见](https://arxiv.org/abs/2605.15208) ⭐️ 8.0/10

一项新研究揭示，LLM 的训练后量化可能导致刻板偏见的出现，尤其是在低精度下，呈现剂量-反应模式。该论文在 BBQ 偏见基准上测试了三个模型在五种精度水平下的表现。 这一发现对于压缩 LLM 的安全部署至关重要，因为困惑度等标准质量指标无法检测到偏见的出现。它强调了在部署前需要明确测试公平性的质量感知压缩协议。 在 3 位量化下，6-21%先前无偏见的项目出现了新的刻板行为，而模型选择“未知”答案的意愿下降了 17.4%。即使在 4 位量化下，尽管困惑度增加不到 3%，已有 2.5-5.6%的项目显示出新的偏见。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: 大型语言模型（LLM）通常通过训练后量化进行压缩以降低成本，但对偏见的影响尚不清楚。BBQ 基准是一个旨在测试问答中社会偏见的数据集。本研究系统地评估了多个模型和精度水平下的偏见出现情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2110.08193">BBQ : A Hand-Built Bias Benchmark for Question Answering</a></li>
<li><a href="https://ukgovernmentbeis.github.io/inspect_evals/evals/bias/bbq/">BBQ : Bias Benchmark for Question Answering</a></li>

</ul>
</details>

**标签**: `#LLM`, `#quantization`, `#bias`, `#safety`, `#compression`

---

<a id="item-16"></a>
## [MuteBench：传感器故障下多模态融合鲁棒性基准测试](https://arxiv.org/abs/2605.15235) ⭐️ 8.0/10

MuteBench 是一个新基准，在 9 个临床数据集、6 种融合架构和超过 12.5 万个样本上，评估多模态融合架构在两种传感器故障（模态缺失和模态内缺失）下的表现。 该基准通过系统评估对传感器故障的鲁棒性，填补了临床 AI 中的一个关键空白，而传感器故障在实际场景中很常见。架构族比参数数量对鲁棒性更重要的发现，为设计可靠的多模态系统提供了可操作的指导。 通道独立模型能很好地容忍模态缺失，但对模态内缺失可能敏感，尤其是在短序列上。课程模态丢弃仅在训练中使用的最大丢弃率范围内可靠地提供保护，一项 PTB-XL 案例研究表明，基于扩散的插补可以改善模态内缺失下的下游分类。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: 多模态融合结合来自多个传感器（如 ECG、EEG）的数据以提高临床 AI 性能。然而，传感器在实践中经常发生故障，导致数据缺失。现有基准通常只评估一种故障模式或有限的架构集，在理解跨不同条件的鲁棒性方面存在空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15235">[2605.15235] MuteBench: Modality Unavailability Tolerance Evaluation...</a></li>

</ul>
</details>

**标签**: `#multimodal fusion`, `#clinical AI`, `#robustness`, `#benchmark`, `#missing data`

---

<a id="item-17"></a>
## [在线策略自蒸馏降低 LLM 安全税](https://arxiv.org/abs/2605.15239) ⭐️ 8.0/10

研究人员提出 OPSA（用于安全对齐的在线策略自蒸馏）方法，该方法利用模型自身的生成轨迹和教师翻转率指标来降低 LLM 对齐中的安全税。 这项工作解决了 LLM 安全对齐中的一个关键权衡问题，即提高安全性往往会降低推理能力。OPSA 实现了更强的安全-推理权衡，特别是在较小模型上，这可能使安全对齐在资源受限的部署中更加实用。 OPSA 使用冻结的教师模型副本，该副本以特权安全上下文为条件，提供密集的逐 token KL 监督。教师翻转率指标衡量特权上下文将不安全响应转换为安全响应的频率，指导搜索有效的安全上下文。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: LLM 的安全对齐通常涉及在安全演示上进行微调，但这可能导致训练数据与模型自身输出之间的分布不匹配，从而产生“安全税”——推理能力下降。离线策略训练加剧了这一问题。OPSA 通过使用在线策略自蒸馏来缓解这一问题，即模型从自身生成中学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2507.17075">LoRA is All You Need for Safety Alignment of Reasoning LLMs</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#alignment`, `#self-distillation`, `#safety tax`, `#on-policy`

---

<a id="item-18"></a>
## [转录组引导的扩散模型用于药物设计](https://arxiv.org/abs/2605.15243) ⭐️ 8.0/10

研究人员提出了 CURE，一个多分辨率转录组引导的扩散框架，能够根据期望的细胞状态转变设计药物分子，将基于转录组的药物设计形式化为生成逆问题。 这项工作弥合了转录组扰动与分子生成之间的鸿沟，实现了无需靶标结构的表型驱动药物发现，可能加速针对通路失调的复杂疾病的药物开发。 CURE 包含一个转录组扰动功能特征提取器（TFE），可提取扰动嵌入，将其与双化学视图对齐，并执行异质性感知聚合以处理噪声转录组数据。在结构质量和功能一致性上优于基线，并通过零样本基因抑制剂设计得到验证。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: 扩散模型是一类生成式 AI，通过学习逆转加噪过程来创建新数据。在药物设计中，它们已被用于生成具有所需性质的分子。转录组扰动测量药物引起的基因表达变化，提供其效应的功能读数。然而，由于生物学与化学之间的领域差距以及信号的稀疏性，直接从转录组数据设计分子具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.09511v1">Diffusion Models for Molecules : A Survey of Methods and Tasks</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10994218/">Diffusion models in bioinformatics and computational biology - PMC</a></li>

</ul>
</details>

**标签**: `#drug design`, `#diffusion models`, `#transcriptomics`, `#generative AI`, `#computational biology`

---

<a id="item-19"></a>
## [生成式轨迹模型隐私评估的空白](https://arxiv.org/abs/2605.15246) ⭐️ 8.0/10

该论文识别出生成式轨迹模型在隐私评估方面的重大空白，并针对 GAN、VAE 和扩散模型实施了成员推断攻击，表明其生成性质并不能消除隐私风险。 这项工作表明，广泛应用于城市智能的生成式轨迹模型可能泄露敏感的训练数据，挑战了生成模型天生保护隐私的普遍假设。 作者对代表性轨迹数据生成模型实施了成员推断攻击，展示了实证隐私评估的可行性，并揭示了尽管模型具有生成性质，隐私风险依然存在。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: GAN、VAE 和扩散模型等生成模型被用于创建城市智能的合成轨迹数据，但其隐私属性常被假定而非严格评估。成员推断攻击是一种标准方法，通过判断特定数据点是否属于训练集来评估隐私泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1610.05820">[1610.05820] Membership Inference Attacks against Machine Learning Models - arXiv</a></li>
<li><a href="https://grokipedia.com/page/Membership_Inference_Attack">Membership Inference Attack</a></li>
<li><a href="https://www.ibm.com/docs/en/watsonx/saas?topic=atlas-membership-inference-attack">Membership inference attack risk for AI - IBM</a></li>

</ul>
</details>

**标签**: `#privacy`, `#generative models`, `#trajectory data`, `#membership inference attack`, `#AI security`

---

<a id="item-20"></a>
## [GQLA：通过双路径注意力实现硬件自适应的大模型解码](https://arxiv.org/abs/2605.15250) ⭐️ 8.0/10

GQLA 修改了多头潜在注意力（MLA），使其从同一组权重中支持 MQA 和 GQA 两种解码路径，从而无需重新训练即可在高端和普通 GPU 上实现高效推理。 这使得单个模型能够适应不同的硬件，降低部署成本，并能在 H20 等普通 GPU 上实现多 token 预测，而这在之前的 MLA 中是不可能的。 GQLA 暴露了一条与 MLA 相同的 MQA 吸收路径和一条具有每组扩展缓存的 GQA 路径；运行时根据硬件选择最优路径。TransGQLA 将预训练的 GQA 检查点（如 LLaMA-3-8B）转换为 GQLA，在 MQA 路径上将 KV 缓存压缩至 28.125%。

rss · arXiv - Machine Learning · May 18, 04:00

**背景**: DeepSeek-V2/V3 中使用的多头潜在注意力（MLA）将键和值压缩为低秩潜在表示，在 H100 GPU 上实现了高效率，但仅支持单一的 MQA 解码路径。分组查询注意力（GQA）是多头注意力（MHA）和多查询注意力（MQA）之间的折中方案，通过分组查询来共享键值投影。GQLA 桥接了这些方法以实现硬件适应性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://liorsinai.github.io/machine-learning/2025/02/22/mla.html">DeepSeek 's Multi - Head Latent Attention - Lior Sinai</a></li>
<li><a href="https://medium.com/data-science/deepseek-v3-explained-1-multi-head-latent-attention-ed6bee2a67c4">DeepSeek -V3 Explained 1: Multi - head Latent Attention | Medium</a></li>
<li><a href="https://cyk1337.github.io/notes/2024/05/10/Memory-Efficient-Attention/">Memory-Efficient Attention : MHA vs . MQA vs . GQA vs . MLA</a></li>

</ul>
</details>

**标签**: `#attention mechanisms`, `#LLM inference`, `#hardware adaptation`, `#DeepSeek`, `#efficient decoding`

---

<a id="item-21"></a>
## [OP-Mix：大模型训练全生命周期的统一数据混合算法](https://arxiv.org/abs/2605.15220) ⭐️ 8.0/10

研究人员提出了 OP-Mix（On-Policy Mix），这是一种将数据混合视为整个语言模型训练生命周期中的在线决策问题的算法，利用低秩适配器低成本地模拟候选混合方案。 OP-Mix 统一了预训练、持续中训练和持续指令微调阶段的数据混合，无需单独的代理模型，计算量最多减少 95%，同时性能持平或提升。 在预训练中，OP-Mix 相比无混合平均困惑度提升 6.3%；在持续学习中，它匹配了重训练和在线蒸馏的性能，同时计算量分别减少 66% 和 95%。

rss · arXiv - NLP · May 18, 04:00

**背景**: 数据混合决定了语言模型训练中如何组合不同数据源，对模型质量影响显著。现有方法通常依赖较小的代理模型或固定领域集，且仅针对单一训练阶段。低秩适配（LoRA）是一种通过添加轻量可训练参数来适配大模型的技术，能够高效模拟不同的数据混合方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">[2106.09685] LoRA: Low - Rank Adaptation of Large Language Models</a></li>

</ul>
</details>

**标签**: `#data mixing`, `#language model training`, `#continual learning`, `#pretraining`, `#low-rank adaptation`

---

<a id="item-22"></a>
## [从 1 亿份乌克兰法院判决构建大规模法律引用图](https://arxiv.org/abs/2605.15362) ⭐️ 8.0/10

研究人员从 1.007 亿份乌克兰法院判决中构建了首个大规模引用图，提取了 5.02 亿条引用链接，在验证样本上达到了完美的精确度。 这项工作表明，司法引用结构可以自动恢复法律领域边界，并以接近完美的准确度预测立法重要性，为法律信息学和 AI 辅助法律分析提供了强大工具。 该引用图基于完整的 EDRSR 登记册（9950 万份全文，1.1 TB），在普通硬件上使用正则表达式约 5 小时构建完成，精确度为 1.00（95% Wilson 置信区间：[0.982, 1.000]）。

rss · arXiv - NLP · May 18, 04:00

**背景**: 法律中的引用图映射了法院判决之间的相互引用关系，揭示了影响力和结构。Louvain 方法是一种通过优化模块度来检测大型网络中社区的流行算法。Wilson 置信区间为验证样本中的精确度提供了稳健的估计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Louvain_method">Louvain method - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binomial_proportion_confidence_interval">Binomial proportion confidence interval - Wikipedia</a></li>
<li><a href="https://7aac.gov.ua/en/edrsr/">edrsr | Seventh Administrative Court of Appeal</a></li>

</ul>
</details>

**标签**: `#legal informatics`, `#citation graph`, `#network analysis`, `#natural language processing`, `#machine learning`

---

<a id="item-23"></a>
## [Eskwai：基于 RAG 的加纳法律教育 AI 助手](https://arxiv.org/abs/2605.15380) ⭐️ 8.0/10

研究人员开发了 Eskwai for Students，这是一个基于检索增强生成（RAG）的 AI 助手，用于加纳的法律教育，并在 30 个月内部署，有 3100 名法学院学生提出了 32000 个查询。 这项工作填补了生成式 AI 在发展中国家法律教育应用的关键空白，提供了查询模式和伦理问题的见解，并展示了一种适用于资源匮乏地区的可扩展方法。 该系统基于一个包含超过 12000 条判例法和 1400 项加纳立法的精选数据库，研究评估了有用性，并分析了引发伦理问题的查询类型。

rss · arXiv - NLP · May 18, 04:00

**背景**: 检索增强生成（RAG）是一种技术，通过在生成响应前从外部来源检索相关信息来增强大型语言模型，减少幻觉并提高准确性。这在法律领域尤为重要，因为精确性和来源验证至关重要。发展中国家通常缺乏针对本地法律系统的先进 AI 工具，因此此次部署具有重要意义。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation</a></li>
<li><a href="https://www.pinecone.io/learn/retrieval-augmented-generation/">Retrieval - Augmented Generation (RAG) | Pinecone</a></li>

</ul>
</details>

**标签**: `#generative AI`, `#legal education`, `#retrieval augmented generation`, `#Global South`, `#AI ethics`

---

<a id="item-24"></a>
## [LLM 架构的神经激活模式分析](https://arxiv.org/abs/2605.15436) ⭐️ 8.0/10

一项新研究系统比较了六种 LLM 架构在十二项认知任务上的神经激活模式，发现数学推理产生最高的注意力熵，且解码器模型比编码器模型表现出更高的稀疏性。 该分析为基于任务需求选择 LLM 架构提供了经验指导，有望提升大数据应用的效率和性能。 该研究考察了 144 个任务-模型组合，测量了编码器和解码器架构的最终激活值、注意力熵和稀疏模式。

rss · arXiv - NLP · May 18, 04:00

**背景**: 大型语言模型（LLM）有不同的架构，主要包括仅编码器（如 BERT）、仅解码器（如 GPT）和编码器-解码器（如 T5）。注意力熵衡量注意力在 token 间的分布均匀程度，而稀疏性表示激活值接近零的程度。这些指标有助于理解模型行为和效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.03589v1">Entropy and Attention Dynamics in Small Language Models ...</a></li>
<li><a href="https://aclanthology.org/2025.acl-long.485.pdf">Attention Entropy is a Key Factor: An Analysis of Parallel Context</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/understanding-encoder-and-decoder">Understanding Encoder And Decoder LLMs</a></li>

</ul>
</details>

**标签**: `#LLM`, `#neural activation`, `#cognitive tasks`, `#attention entropy`, `#model comparison`

---

<a id="item-25"></a>
## [语言模型为何比人类更不惊讶？解析多重性假设测试](https://arxiv.org/abs/2605.15440) ⭐️ 8.0/10

一项新研究使用带束搜索的 RNNG 测试了语言模型比人类能同时维护更多解析的假设，以解释其对花园路径句困难程度的低估。结果显示减少解析数量会增加预测的花园路径效应，但不足以匹配人类数据。 这项工作解决了语言模型与人类句子处理之间的根本性不匹配问题，对于改善模型与人类认知的对齐至关重要。研究结果表明，仅凭解析多重性无法调和 LM 的惊讶度与人类阅读时间，暗示了其他因素如记忆限制或重分析成本。 该研究使用带词同步束搜索的循环神经网络文法（RNNG）来改变计算词惊讶度时的同时解析数量。即使只使用单个解析，预测的花园路径效应仍远小于人类观察到的效应，表明其他机制在起作用。

rss · arXiv - NLP · May 18, 04:00

**背景**: 惊讶度理论将单词可预测性与处理难度联系起来，语言模型的惊讶度在自然文本中通常能很好地预测人类阅读时间。然而，它们系统性地低估了花园路径句的困难程度，花园路径句是句法歧义句，会最初误导读者。解析多重性不匹配假设认为，语言模型能比人类同时考虑更多的句法解释，从而降低了惊讶度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prediction_in_language_comprehension">Prediction in language comprehension - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Garden-path_sentence">Garden-path sentence</a></li>
<li><a href="https://arxiv.org/abs/1602.07776">[1602.07776] Recurrent Neural Network Grammars</a></li>

</ul>
</details>

**标签**: `#psycholinguistics`, `#language models`, `#surprisal theory`, `#syntactic ambiguity`, `#RNNG`

---

<a id="item-26"></a>
## [深度预对齐提升视觉语言模型性能](https://arxiv.org/abs/2605.15300) ⭐️ 8.0/10

研究人员提出深度预对齐（DPA）架构，用小型视觉语言模型替换标准 ViT 编码器，使视觉特征与 LLM 文本空间深度对齐，在多模态基准上获得 1.9 至 3.0 个百分点的提升。 DPA 解决了当前视觉语言模型中的关键对齐瓶颈，使 LLM 深度更高效地用于推理而非模态对齐，并以最小开销提供无缝升级路径。 在 4B 参数规模下，DPA 在 8 个基准上平均领先基线 1.9 个百分点，在 32B 规模下扩大至 3.0 个百分点，并在 3 个文本基准上将语言能力遗忘降低 32.9%。该增益在 Qwen3 和 LLaMA 3.2 系列上保持一致。

rss · arXiv - Computer Vision · May 18, 04:00

**背景**: 大多数视觉语言模型使用轻量级投影器将 ViT 编码器输出映射到 LLM，但视觉特征在 LLM 早期层仍与文本空间距离较远，浪费深度在对齐上。DPA 用小型视觉语言模型作为感知器替换 ViT，在输入 LLM 前预先对齐特征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision_transformer">Vision transformer - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Vision Language Models`, `#Multimodal Learning`, `#Architecture`, `#Alignment`, `#arXiv`

---

<a id="item-27"></a>
## [递归潜在细化提升生成模型多样性](https://arxiv.org/abs/2605.15309) ⭐️ 8.0/10

该论文提出递归潜在细化（RTM），将基于风格的生成器中的单次潜在映射替换为迭代细化过程，在多个基准测试中持续提升质量和多样性。 这项工作解决了 FID 指标饱和以及生成模型中长期存在的模式崩溃问题，提供了一种在不牺牲质量的前提下提升多样性的实用方法，这对需要广泛覆盖的真实世界应用至关重要。 RTM 与隐式最大似然估计（IMLE）集成后，在保持有竞争力的 FID 的同时，实现了当前最先进方法中最高的精确度和召回率，在 CIFAR-10、CelebA-HQ 256x256 以及九个少样本基准测试上均有改进。

rss · arXiv - Computer Vision · May 18, 04:00

**背景**: FID（Fréchet Inception Distance）是评估生成模型的常用指标，但它混淆了样本保真度和模式覆盖，且已接近饱和，意味着模型可能获得低 FID 值但仍存在模式崩溃。模式崩溃指生成模型仅产生有限种类的输出，未能覆盖完整的数据分布。递归潜在细化（RTM）通过迭代细化潜在编码来解决此问题，鼓励模型探索多样化的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.15309v1">One Pass Is Not Enough: Recursive Latent Refinement for Generative Models - arXiv</a></li>

</ul>
</details>

**标签**: `#generative models`, `#image generation`, `#FID`, `#mode coverage`, `#IMLE`

---

<a id="item-28"></a>
## [Minerva-Ego：自我中心视频推理新基准](https://arxiv.org/abs/2605.15342) ⭐️ 8.0/10

研究人员推出了 Minerva-Ego 基准，用于评估复杂的自我中心视觉推理，并带有时空掩码标注，揭示了当前最先进模型与人类表现之间存在巨大差距。 该基准填补了视频理解中缺乏中间推理步骤评估的空白，对推动具身 AI 和自我中心智能体的发展至关重要。 Minerva-Ego 在现有自我中心视频数据集基础上增加了多步多模态问题和人工标注的时空推理轨迹，实验表明提供“在哪里”和“何时”的提示能显著提升模型性能。

rss · arXiv - Computer Vision · May 18, 04:00

**背景**: 自我中心视频理解涉及从第一人称视角进行推理，对增强现实和机器人等应用至关重要。现有基准通常只评估最终答案，而非推理过程，限制了对模型能力的深入理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.15342">Minerva - Ego : Spatiotemporal Hints for Egocentric Video Understanding</a></li>

</ul>
</details>

**标签**: `#egocentric video understanding`, `#benchmark`, `#visual reasoning`, `#embodied AI`, `#spatiotemporal reasoning`

---

<a id="item-29"></a>
## [特征空间采样降低 3D 群卷积神经网络计算成本](https://arxiv.org/abs/2605.15368) ⭐️ 8.0/10

本文提出在特征空间而非几何空间中进行采样，用于群卷积神经网络（GCNN），将几何分辨率与内存和计算成本解耦。该方法用基于特征相似性选择的代表性样本替代密集的几何样本，从而大幅加速等变 3D 分类器。 这项工作解决了 GCNN 的一个关键限制——计算成本随自由度指数增长——这阻碍了其在 3D 几何中的实际应用。通过实现高效的训练和推理，它可能使等变深度学习更易于应用于现实世界的 3D 任务，如物体识别和场景理解。 主要实验发现表明，粗粒度的特征空间采样已经能很好地保持分类精度。这允许基于几何相似性进行预计算，从而进一步加速等变 3D 分类器的训练。

rss · arXiv - Computer Vision · May 18, 04:00

**背景**: 群卷积神经网络（GCNN）通过密集采样变换组并在不同姿态下关联数据和滤波器来引入对称性作为归纳偏置，从而保持等变性。然而，这种密集采样导致高计算成本，特别是对于涉及平移和旋转的 3D 数据，成本随自由度指数增长。所提出的方法通过在特征空间而非几何空间中进行采样，将几何分辨率与计算开销解耦。

**标签**: `#group-convolutional neural networks`, `#3D geometry`, `#equivariance`, `#deep learning`, `#computational efficiency`

---

<a id="item-30"></a>
## [MorphoHELM：细胞绘画综合基准测试](https://arxiv.org/abs/2605.15383) ⭐️ 8.0/10

研究人员推出了 MorphoHELM，这是一个开放基准测试，标准化并扩展了细胞绘画实验中特征提取方法的评估协议，评估了迄今为止最广泛的方法。 该基准测试解决了形态学分析中评估碎片化的问题，实现了方法间的公平比较并揭示了权衡关系，这对推进药物筛选和生物学研究至关重要。 一个关键特点是每个任务在不同程度的批次效应下进行评估，直接量化了生物信号检测随噪声增加而退化的情况；目前没有模型在所有设置上优于经典计算机视觉策略。

rss · arXiv - Computer Vision · May 18, 04:00

**背景**: 细胞绘画是一种高内涵成像实验，使用荧光染料可视化细胞区室，实现形态学分析。包括深度学习在内的表示提取方法用于量化这些图像，但不同研究之间的评估一直不一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/cell_painting">Cell painting</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#microscopy`, `#representation learning`, `#cell painting`, `#deep learning`

---

<a id="item-31"></a>
## [MaxSketch：通过随机投影实现鲁棒的不同元素计数](https://arxiv.org/abs/2605.15571) ⭐️ 8.0/10

研究人员提出了 MaxSketch，一种使用随机高斯投影的最大线性草图，用于在高维噪声流中估计不同元素，在几何结构下实现了改进的内存保证。 这项工作连接了经典流算法和现代表示学习，表明几何结构可以从根本上降低不同元素计数的复杂性，这对于学习嵌入中的重复检测等应用至关重要。 MaxSketch 仅需 O(log n / ε²)个随机投影即可实现(1+ε)因子近似，显著优于一般度量空间中Θ(√n)的最坏情况内存界限。

rss · arXiv - Data Science & Statistics · May 18, 04:00

**背景**: 像 HyperLogLog 这样的经典不同元素计数草图依赖于相同元素的一致哈希值，但在观测数据有噪声且高维时失效。随机投影是一种降维技术，能近似保持距离，此处用于处理近似相似性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_random_projection">Gaussian random projection</a></li>

</ul>
</details>

**标签**: `#data streams`, `#distinct counting`, `#random projections`, `#robust estimation`, `#machine learning`

---

<a id="item-32"></a>
## [α-TCAV：修复概念激活向量的统计不稳定性](https://arxiv.org/abs/2605.15688) ⭐️ 8.0/10

该论文提出了α-TCAV，一个统一框架，用参数化平滑函数替换了标准 TCAV 评分中的不连续指示函数，解决了导致方差不衰减的根本缺陷。它还提供了 CAV 分布的理论分析以及调整α参数的实用指南。 这项工作修复了广泛使用的可解释性方法 TCAV 中的关键不稳定性，可能提高深度学习中基于概念的可解释性的可靠性。统一框架还涵盖了 Multi-TCAV 并节省了计算成本，影响 AI 可解释性领域的研究者和实践者。 分析表明，标准 TCAV 评分依赖不连续指示函数，导致关键区域方差不衰减。α-TCAV 用平滑函数替代，产生概率公式，能以较低成本模仿 Multi-TCAV 或提供校准的贝叶斯最优度量。

rss · arXiv - Data Science & Statistics · May 18, 04:00

**背景**: 概念激活向量（CAV）用于表示神经网络潜在空间中的高级概念（例如“条纹”）。TCAV 通过计算 CAV 与模型输出梯度之间的余弦相似度来量化概念对模型预测的影响。然而，标准 TCAV 评分使用不连续指示函数来统计正相似度，这引入了统计不稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2404.03713v1">Explaining Explainability: Understanding Concept Activation Vectors - arXiv</a></li>
<li><a href="https://christophm.github.io/interpretable-ml-book/detecting-concepts.html">29 Detecting Concepts – Interpretable Machine Learning</a></li>
<li><a href="https://www.emergentmind.com/topics/concept-activation-vector-cav">Concept Activation Vector (CAV) - Emergent Mind</a></li>

</ul>
</details>

**标签**: `#explainability`, `#deep learning`, `#concept activation vectors`, `#interpretability`, `#machine learning theory`

---

<a id="item-33"></a>
## [通过子空间归因实现可解释的域偏移检测](https://arxiv.org/abs/2605.15920) ⭐️ 8.0/10

研究人员开发了一种方法，通过识别局部密度异常及其支持的特征子空间，来检测和解释高维数据中的域偏移，并在基准测试和真实心电图数据上进行了验证。 这项工作通过使域偏移可解释，增强了机器学习模型的鲁棒性，对于在医疗 AI 等安全关键应用中部署模型至关重要，因为隐藏的偏差可能导致失败。 该方法首先使用自定义算法检测局部密度异常，然后识别异常最明显的特征子空间，从而可追溯到少量特征。它还提供了一种协议，从两个未标记数据集中提取没有残余分布差异的子集。

rss · arXiv - Data Science & Statistics · May 18, 04:00

**背景**: 域偏移指训练数据和部署数据之间的分布差异，可能导致模型性能下降。传统检测方法通常缺乏可解释性，难以理解偏移发生的原因。这项工作通过将偏移归因于特定特征子空间来弥补这一不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.16261">[2505.16261] Interpretable Anomaly Detection in Encrypted Traffic Using SHAP with Machine Learning Models - arXiv</a></li>

</ul>
</details>

**标签**: `#domain shift`, `#interpretability`, `#anomaly detection`, `#machine learning`, `#ECG`

---

<a id="item-34"></a>
## [可解释 AI 还不够：重新思考算法可争议性](https://arxiv.org/abs/2605.16041) ⭐️ 8.0/10

一篇新论文指出，可解释 AI（XAI）忽视了算法可争议性——即审查和纠正错误决策的能力，并提出了正式定义以及三种可以推翻决策的证据类型。 这项工作填补了 XAI 研究中具有高度伦理和法律重要性的关键空白，可能使个人能够挑战贷款、招聘和作弊检测等领域的自动化决策。 论文区分了可争议性与补救措施：可争议性假设决策可能错误并寻找推翻它的证据，而补救措施假设决策有效并提供改变途径。三种值得推翻的证据类型是预测多重性、错误特征值和被忽略的推翻性证据。

rss · arXiv - Data Science & Statistics · May 18, 04:00

**背景**: 可解释 AI（XAI）旨在让机器学习决策对人类可理解。然而，大多数 XAI 方法侧重于解释决策原因或如何改变它（补救措施），而不是让个人质疑可能错误的决策。算法可争议性是审查和纠正错误算法决策的能力，这对公平性和问责制至关重要。

**标签**: `#explainable AI`, `#algorithmic contestability`, `#fairness`, `#machine learning ethics`, `#XAI`

---

<a id="item-35"></a>
## [偏态自适应共形预测提升区间效率](https://arxiv.org/abs/2605.16145) ⭐️ 8.0/10

提出了一种新的偏态自适应分裂共形预测回归扩展方法，通过额外预测模型学习局部偏态，生成更高效的预测区间，同时保持有限样本边际有效性。 该方法解决了现有共形预测方法假设残差对称的实际局限性，在偏态区域生成更紧的区间，提升了实际回归任务中的不确定性量化效果。 该方法使用带符号缩放残差的反双曲正弦变换作为额外模型的训练目标，并包含一个基于校准样本的估计器，用于与经典缩放分数区间比较预期的未来相对宽度。

rss · arXiv - Data Science & Statistics · May 18, 04:00

**背景**: 共形预测是一种无分布假设的不确定性量化框架，在可交换性条件下生成有效的预测区间。标准分裂共形预测通常使用对称区间，当残差偏态时效率较低。该工作通过自适应局部偏态来提高区间效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#uncertainty quantification`, `#regression`, `#machine learning`, `#statistics`

---