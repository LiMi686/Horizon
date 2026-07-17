---
layout: default
title: "Horizon Summary: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
---

> From 106 items, 23 important content pieces were selected

---

1. [Firefox 被编译为 WebAssembly 在浏览器中运行](#item-1) ⭐️ 9.0/10
2. [GitHub 发布官方 Copilot Agent SDK](#item-2) ⭐️ 9.0/10
3. [首次在宜居带岩质系外行星上发现大气层](#item-3) ⭐️ 8.0/10
4. [Kimi K3 与鹈鹕基准测试：一次批判性审视](#item-4) ⭐️ 8.0/10
5. [开源 AI 崛起威胁闭源模型](#item-5) ⭐️ 8.0/10
6. [Apache Ossie：标准化语义元数据交换](#item-6) ⭐️ 8.0/10
7. [Open Interpreter：为低成本模型优化的编码代理](#item-7) ⭐️ 8.0/10
8. [LLM-T1D：可解释的胰岛素泵控制器](#item-8) ⭐️ 8.0/10
9. [能力源于访问结构，而非规模](#item-9) ⭐️ 8.0/10
10. [可解释 AI 应优先基础研究而非临时方法](#item-10) ⭐️ 8.0/10
11. [面向沙盒原生强化学习的分支策略优化](#item-11) ⭐️ 8.0/10
12. [RENEW：通过人类偏好修复世界模型利用问题](#item-12) ⭐️ 8.0/10
13. [JKP 框架揭示 VLM 在重复提示下的不稳定性](#item-13) ⭐️ 8.0/10
14. [首个阿拉伯语量子自然语言处理系统](#item-14) ⭐️ 8.0/10
15. [LLM 智能体文本通信信息丢失，潜在通道被提出](#item-15) ⭐️ 8.0/10
16. [TTCD：具有逐词元时间的连续扩散语言模型](#item-16) ⭐️ 8.0/10
17. [Polestar：基于漂移的缓存与令牌提交优化扩散 LLM 推理](#item-17) ⭐️ 8.0/10
18. [SeeSE3：探索视觉特征中的三维欧几里得空间](#item-18) ⭐️ 8.0/10
19. [DCVC-MB：基于状态空间模型的神经 B 帧编码器](#item-19) ⭐️ 8.0/10
20. [通过线性探测实现整流流的最优自蒸馏](#item-20) ⭐️ 8.0/10
21. [主观风险分解统一不确定性量化度量](#item-21) ⭐️ 8.0/10
22. [PiVoT：从雷达点云实现实时多目标跟踪](#item-22) ⭐️ 8.0/10
23. [天气数据遭破坏风险上升](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Firefox 被编译为 WebAssembly 在浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 将完整的 Firefox 浏览器（Gecko 引擎）编译为 WebAssembly，使其能够在 Chrome 等另一个浏览器中运行。该项目使用 LLM（Claude Opus 和 Fable）进行代码翻译，估计花费了 25,000 美元的 token。 这展示了一种范式转变：整个应用程序，甚至复杂的浏览器，都可以在另一个浏览器中沙盒化运行，可能开启基于 Web 的计算和遗留软件保存的新形式。同时，它也展示了 LLM 在自动化大规模代码翻译任务中的强大能力。 该演示使用 Wisp 协议通过 Puter 的服务器代理所有网络流量，因为 WebAssembly 代码无法打开任意网络连接。项目选择 Firefox/Gecko 是因为其强大的单进程支持，这简化了 WebAssembly 编译。

rss · Simon Willison · Jul 16, 23:34

**背景**: WebAssembly (Wasm) 是一种低级二进制指令格式，可在现代浏览器中以接近原生的速度运行，支持游戏和视频编辑等高性能应用。将像 Gecko 这样的完整浏览器引擎编译为 Wasm 极具挑战性，因为其体积和复杂性；之前的尝试编译了较小的引擎如 WebKit，但没有公开演示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/wisp-protocol: Wisp is a low-overhead, easy to implement protocol for proxying multiple TCP/UDP sockets over a single websocket. · GitHub</a></li>
<li><a href="https://firefox-source-docs.mozilla.org/overview/gecko.html">Gecko — Firefox Source Docs documentation</a></li>
<li><a href="https://github.com/fable-compiler/fable">GitHub - fable-compiler/Fable: F# to JavaScript, TypeScript, Python, Rust, Erlang and Dart Compiler · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论非常热烈，许多人称赞这一技术成就。一些评论者指出了代理流量的高服务器成本，并质疑其实用性，但总体情绪是积极的。

**标签**: `#WebAssembly`, `#Firefox`, `#Browser`, `#LLM`, `#Wasm`

---

<a id="item-2"></a>
## [GitHub 发布官方 Copilot Agent SDK](https://github.com/github/copilot-sdk) ⭐️ 9.0/10

GitHub 发布了官方 Copilot SDK，这是一个多平台工具包，允许开发者将驱动 Copilot CLI 的同一代理引擎嵌入到自己的应用中。该 SDK 支持 Python、TypeScript、Go、.NET、Java 和 Rust，并已在 npm、PyPI、NuGet、Go、Crates.io 和 Maven Central 上提供包。 该 SDK 使代理式 AI 能力大众化，让任何开发者都能将 Copilot 驱动的功能集成到自己的工具中，而无需从头构建编排。它大大降低了将高级 AI 代理集成到自定义开发者工作流和第三方服务中的门槛。 该 SDK 公开了 Copilot CLI 背后经过生产测试的同一代理运行时，负责规划、工具调用和多轮执行。目前处于技术预览阶段，GitHub 为 Node.js、Python、Go、.NET 和 Java 提供了 cookbook 以帮助开发者快速上手。

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**背景**: GitHub Copilot Agent 是一个 AI 驱动的编码助手，可以自主分析项目、制定计划并进行代码更改。Copilot CLI 已经通过命令行提供了代理能力，但将其集成到其他应用程序中需要自定义工作。新的 SDK 将该引擎打包成流行编程语言的可重用库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub</a></li>
<li><a href="https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/">Build an agent into any app with the GitHub Copilot SDK - The GitHub Blog</a></li>
<li><a href="https://www.infoq.com/news/2026/02/github-copilot-sdk/">GitHub Copilot SDK Lets Developers Integrate Copilot CLI's Engine into Apps - InfoQ</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#API`

---

<a id="item-3"></a>
## [首次在宜居带岩质系外行星上发现大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

詹姆斯·韦伯太空望远镜确认了 LHS 1140b 上存在大气层，这是一颗位于 48 光年外红矮星宜居带内的岩质超级地球。这是首次在相对岩质的系外行星的宜居带内确认大气层。 这一发现挑战了此前认为红矮星周围的岩质行星因强烈恒星剥离而无法保留大气层的假设。它为研究潜在宜居世界和寻找生物特征开辟了新的可能性。 LHS 1140b 的质量约为地球的 5.6 倍，半径大 70%，其密度表明它可能是一个海洋世界，水质量占比 9-19%。检测到的气体是氦，表明其逃逸速度很高，足以保留这种轻气体。

hackernews · neversaydie · Jul 17, 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: 红矮星比太阳更冷更小，其宜居带更靠近恒星，使行星暴露在强烈的恒星耀斑和辐射下。此类行星的大气层保留一直是系外行星科学中的主要不确定性。LHS 1140b 于 2017 年由 MEarth 项目发现，一直是大气表征的主要目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b</a></li>
<li><a href="https://www.bbc.com/news/articles/cy4kdd1e0ejo">First atmosphere found around Earth-like planet LHS 1140 b</a></li>

</ul>
</details>

**社区讨论**: 评论者对于红矮星宜居带内的岩质行星能保留大气层表示惊讶，一些人最初怀疑它可能是一个正在被蒸发的迷你海王星。但 JWST 的发射光谱排除了这种可能性。其他人讨论了未来向附近系外行星发送探测器的推进概念。

**标签**: `#exoplanets`, `#JWST`, `#atmosphere`, `#habitable zone`, `#red dwarf`

---

<a id="item-4"></a>
## [Kimi K3 与鹈鹕基准测试：一次批判性审视](https://simonwillison.net/2026/Jul/16/kimi-k3/) ⭐️ 8.0/10

Simon Willison 批评了针对大语言模型的“骑自行车的鹈鹕”基准测试，指出其在代理工具使用方面的局限性，并引发了关于基准污染和隐藏提示的讨论。 这一分析强调了需要更相关的基准来评估代理能力，并揭示了隐藏的系统提示和训练数据污染如何扭曲模型比较。 鹈鹕基准测试要求模型生成一个骑自行车的鹈鹕的 SVG，但它不测试工具调用或长上下文可靠性。社区评论揭示了分词器的异常以及疑似隐藏提示导致 token 计数膨胀。

hackernews · droidjj · Jul 17, 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48947717)

**背景**: “骑自行车的鹈鹕”基准测试是 Simon Willison 于 2024 年底创建的非正式测试，用于评估大语言模型遵循指令和生成 SVG 代码的能力。基准污染是指测试数据泄露到训练数据中，导致分数虚高。隐藏提示是模型提供商注入的系统级指令，可能影响模型行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/simonw/pelican-bicycle">GitHub - simonw/pelican-bicycle: LLM benchmark: Generate an SVG of a pelican riding a bicycle · GitHub</a></li>
<li><a href="https://grokipedia.com/page/Pelican_on_a_bicycle_AI_benchmark">Pelican on a bicycle (AI benchmark) — Grokipedia</a></li>
<li><a href="https://gigazine.net/gsc_news/en/20250609-llms-pelicans-on-bicycles/">Here's what happens when you run the AI benchmark 'Draw a Pelican on a Bicycle' on LLama 3.3 70B or GPT 4.1 - GIGAZINE</a></li>

</ul>
</details>

**社区讨论**: 社区成员争论鹈鹕提示是否在训练数据中，有人指出即使是 Simon 自己的博客内容也会出现在模型中。另一位评论者指出分词器的不一致性，暗示 Kimi K3 中隐藏了 85 个 token 的系统提示。

**标签**: `#LLM`, `#benchmark`, `#AI evaluation`, `#tokenization`, `#agentic AI`

---

<a id="item-5"></a>
## [开源 AI 崛起威胁闭源模型](https://stateofopensource.ai/) ⭐️ 8.0/10

Mozilla 的一份新分析显示，开源 AI 模型在使用量上已超越闭源模型，在 OpenRouter 上开源模型处理的 token 占比从四个月前的 40%升至 63%。 这一转变可能颠覆 OpenAI 和 Anthropic 等闭源 AI 公司的商业模式，因为超大规模云服务商和设备制造商可以无许可费地部署开源模型，前沿模型因其高昂的训练成本可能变成负担。 根据 OpenRouter 数据，开源模型在 3 月 19 日处理了 4.19 万亿个 token，几乎是四个月前 8880 亿 token 的 5 倍。该分析以 CTO 风格的幻灯片形式呈现，但批评者指出其内容似乎是 LLM 生成的。

hackernews · rellem · Jul 17, 14:31 · [社区讨论](https://news.ycombinator.com/item?id=48947825)

**背景**: 开源 AI 模型是指权重和代码公开可用的模型，任何人都可以自由使用、修改和部署。闭源模型如 OpenAI 的 GPT-4 是专有的，需要许可费或 API 访问。随着开源模型快速改进，开源与闭源 AI 之间的争论日益激烈。

**社区讨论**: 评论者意见不一：一些人认为开源模型对闭源 AI 公司构成生存威胁，并引用使用量的快速增长；另一些人则批评该分析呈现不佳且可能是 LLM 生成的，质疑其可信度。有用户构建了实时追踪这一转变的仪表盘。

**标签**: `#open source AI`, `#AI models`, `#market analysis`, `#LLM`

---

<a id="item-6"></a>
## [Apache Ossie：标准化语义元数据交换](https://github.com/apache/ossie) ⭐️ 8.0/10

Apache Ossie 是一项在 Apache 孵化器下的行业级规范工作，旨在通过供应商中立的 JSON/YAML 规范，标准化分析、AI 和 BI 平台之间的语义元数据交换。 该计划解决了语义碎片化问题——同一 KPI 在不同工具中定义各异，从而减少人工对账，并使 AI 代理能够基于一致的业务逻辑生成可靠输出。 该规范基于 JSON 和 YAML，仓库包含核心规范、参考转换器（例如 dbt、GoodData）、示例和验证工具。

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**背景**: 语义元数据提供数据元素的机器可解释表示，使系统间能够共享含义。目前，BI 平台和 AI 代理等工具常使用不兼容的语义定义，导致不一致。Apache Ossie（前身为 Open Semantic Interchange）旨在创建一个通用的、供应商中立的标准来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ossie.apache.org/">Home - Apache Ossie (incubating)</a></li>
<li><a href="https://github.com/apache/ossie">GitHub - apache / ossie : Apache Ossie , industry wide specification...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_interoperability">Semantic interoperability - Wikipedia</a></li>

</ul>
</details>

**标签**: `#semantic metadata`, `#standardization`, `#interoperability`, `#AI`, `#BI`

---

<a id="item-7"></a>
## [Open Interpreter：为低成本模型优化的编码代理](https://github.com/openinterpreter/openinterpreter) ⭐️ 8.0/10

Open Interpreter 是一个开源编码代理，现已更新支持 Kimi K3 模型，通过基于 Rust 的 harness 仿真提供最大性能和类似 Codex 的界面。 该项目通过允许在低成本开放模型上以自然语言执行代码，使 AI 辅助编码民主化，让更广泛的用户能够使用先进的编码代理，并减少对昂贵专有 API 的依赖。 Open Interpreter 是 OpenAI Codex 的一个分支，专注于为低成本模型仿真代理 harness。它支持多种 harness，包括 kimi-code、claude-code 和 qwen-code，并与 ACP（代理客户端协议）和 Codex 接口兼容。

rss · GitHub Trending - Daily (All) · Jul 17, 22:41

**背景**: Open Interpreter 是一个开源编码代理，允许用户通过自然语言与计算机交互，实时执行代码。它专为 Kimi K3 等低成本开放权重模型设计，Kimi K3 拥有 2.8 万亿参数，是最大的开放模型之一。该项目旨在提供 GitHub Copilot 等专有编码代理的免费且可访问的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.openinterpreter.com/">Open Interpreter | Coding agent for open models</a></li>
<li><a href="https://github.com/openinterpreter/openinterpreter">GitHub - openinterpreter/openinterpreter: A coding agent for open ...</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#coding agent`, `#natural language`, `#LLM`

---

<a id="item-8"></a>
## [LLM-T1D：可解释的胰岛素泵控制器](https://arxiv.org/abs/2607.14126) ⭐️ 8.0/10

研究人员推出了 LLM-T1D，一种结合强化学习与大语言模型的新型胰岛素泵控制器，在 FDA 批准的 UVA/Padova T1D 模拟器上实现了 73.5%的血糖达标时间，同时为其决策提供人类可读的解释。 这项工作通过使控制器的推理过程透明化，解决了 AI 驱动糖尿病管理中的关键信任障碍，有望提高患者和临床医生的采用率。它还证明了基于大语言模型的控制器在安全关键的医疗应用中能够超越传统的黑盒强化学习系统。 该系统将训练好的专家强化学习策略的知识蒸馏到微调的 LLaMA 3.1 8B 和 Qwen3 8B 模型中，并包含形式化安全验证以防止幻觉。73.5%的血糖达标时间超过了典型的强化学习基线，控制器会为每次胰岛素剂量决策输出通俗易懂的解释。

rss · arXiv - AI · Jul 17, 04:00

**背景**: 1 型糖尿病（T1D）是一种胰腺几乎不产生胰岛素的慢性疾病，需要外部胰岛素输注。人工胰腺系统（APS）使用算法自动输注胰岛素，但传统的强化学习控制器通常是黑盒，使患者和医生难以信任。像 LLaMA 和 Qwen 这样的大语言模型（LLM）能够生成类似人类的文本，经过微调后可以用自然语言解释其推理过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/meta-llama/Llama-3.1-8B/tree/main">meta- llama / Llama - 3 . 1 - 8 B at main</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5851236/">The UVA / Padova Type 1 Diabetes Simulator Goes From Single Meal...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#type 1 diabetes`, `#interpretable AI`, `#healthcare`

---

<a id="item-9"></a>
## [能力源于访问结构，而非规模](https://arxiv.org/abs/2607.14144) ⭐️ 8.0/10

一篇新论文提出了能力收敛假说（CCH），认为在固定推理预算下，模型能力收敛于混合架构类别，而非仅随规模提升，并识别出三道资源墙。 这挑战了柏拉图表征假说，表明架构设计而非仅规模对能力至关重要，可能重塑研究人员对模型开发和资源分配的看法。 论文引入了三道资源墙：香农墙禁止 o(Nb)状态架构，视界墙禁止固定窗口，电路墙禁止固定深度纯注意力组合，并展示了混合架构可以跨越所有三道墙。

rss · arXiv - AI · Jul 17, 04:00

**背景**: 柏拉图表征假说（PRH）认为，随着模型规模扩大，其表征收敛于共享的现实模型。能力收敛假说（CCH）在此基础上提出，能力不会自动跟随表征收敛，而是取决于架构的访问结构，具体来说需要同时具备压缩的 O(1)状态通道和可扩展的逐字索引通道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Instrumental_convergence">Instrumental convergence - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2405.07987">[2405.07987] The Platonic Representation Hypothesis</a></li>

</ul>
</details>

**标签**: `#representation learning`, `#scaling laws`, `#hybrid models`, `#theoretical computer science`, `#deep learning theory`

---

<a id="item-10"></a>
## [可解释 AI 应优先基础研究而非临时方法](https://arxiv.org/abs/2607.14123) ⭐️ 8.0/10

一篇新的立场论文认为，可解释 AI（XAI）研究应将重点从开发临时方法转向解决基础性挑战，如问题定义、评估以及构建解释驱动的反馈管道。 这很重要，因为尽管有许多 XAI 技术，但解释很少影响实际工作流程；该论文呼吁以人为中心、面向行动的范式，这可以使 AI 更可信且实用。 该论文通过分析最近的 ICML、NeurIPS 和 ICLR 论文以及对 XAI 从业者的调查来支持其主张，揭示了限制累积进展的反复出现的问题。最后，它提出了一个实用清单来指导未来研究。

rss · arXiv - Machine Learning · Jul 17, 04:00

**背景**: 可解释 AI（XAI）旨在使机器学习模型可解释，但许多方法如特征归因和稀疏自编码器常常在没有明确问题定义或评估的情况下使用。人机回环系统整合人类反馈以改善模型行为，但当前的 XAI 研究缺乏解释驱动反馈的管道。该论文认为，需要基础性的清晰度，才能从临时方法转向可行动的、反馈驱动的 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Human-in-the-loop">Human - in - the - loop - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2404.02081">Explainability in JupyterLab and Beyond: Interactive XAI Systems for...</a></li>

</ul>
</details>

**标签**: `#Explainable AI`, `#XAI`, `#Machine Learning`, `#Research Methodology`, `#Human-in-the-loop`

---

<a id="item-11"></a>
## [面向沙盒原生强化学习的分支策略优化](https://arxiv.org/abs/2607.14171) ⭐️ 8.0/10

研究人员提出了分支策略优化（BPO），这是一种强化学习算法，通过在确定性、可快照的沙盒环境中构建共享前缀的 rollout 树来降低方差。在 WebShop、ALFWorld 和 SWE-bench Verified 上，BPO 相比 GRPO 和 RLOO 将成功率提升了 3.6–6.1 个绝对百分点。 BPO 利用了沙盒环境的独特属性——确定性和可快照性——在 rollout 之间共享方差，从而可能提高 LLM 智能体训练的样本效率。这通过减少所需的策略更新次数，有望推动 LLM 对齐和智能体强化学习领域的发展。 BPO 在高熵决策点自适应地对沙盒进行快照，每个分支分叉出 K 个备选动作，并从兄弟节点的回报而非独立提示中计算优势。方差减少量等于回报方差中由前缀解释的部分，并且 BPO 使用比最佳基线少 38% 的策略更新次数即可达到相同性能。

rss · arXiv - Machine Learning · Jul 17, 04:00

**背景**: 用于 LLM 智能体的强化学习通常使用 PPO、RLOO 和 GRPO 等算法，这些算法对每个提示采样 N 条独立轨迹，并使用组基线计算优势。然而，这些方法忽略了沙盒环境是确定性的、可快照的，并且可以从任何状态恢复。BPO 利用这一特性构建具有共享前缀的 rollout 树，从而更有效地降低方差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14171v1">[2607.14171v1] Branching Policy Optimization : Sandbox-Native...</a></li>
<li><a href="https://arxiv.org/pdf/2607.14171">Branching Policy Optimization: Sandbox - Native Language Agent...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#LLM agents`, `#policy optimization`, `#sandbox`

---

<a id="item-12"></a>
## [RENEW：通过人类偏好修复世界模型利用问题](https://arxiv.org/abs/2607.14180) ⭐️ 8.0/10

该论文提出了 RENEW 方法，通过人类对想象轨迹的偏好来修复离线强化学习中的世界模型利用问题，并将其形式化为从人类反馈中学习动力学（DLHF）。 这项工作通过利用人类直觉检测不现实的动力学，解决了离线基于模型的强化学习中的一个关键问题——低覆盖区域中的模型利用，提供了一种避免昂贵专家演示或过度保守算法的新范式。 RENEW 利用认知不确定性将基于偏好的微调集中在可被利用的区域，相比朴素 DLHF 提高了样本效率并限制了灾难性遗忘。该方法在 Jumanji 和经典控制环境中进行了评估。

rss · arXiv - Machine Learning · Jul 17, 04:00

**背景**: 离线强化学习中的世界模型可以生成合成经验，但在数据稀疏区域常产生不真实的轨迹，这种现象称为模型利用。先前的解决方案要么需要昂贵的专家数据，要么使用限制泛化的保守策略。人类偏好已用于 RLHF 中的策略对齐，但尚未直接用于动力学模型修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2607.14180">RENEW: Towards Learning World Models and Repairing Model ...</a></li>
<li><a href="https://mbrenndoerfer.com/writing/reward-modeling-rlhf-architecture-training">Reward Modeling: Building Preference Predictors for RLHF - Interactive</a></li>
<li><a href="https://openreview.net/forum?id=w4JFRTD0_R4">E-MCTS: Deep Exploration in Model-Based Reinforcement Learning ...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#world models`, `#human feedback`, `#model exploitation`, `#offline RL`

---

<a id="item-13"></a>
## [JKP 框架揭示 VLM 在重复提示下的不稳定性](https://arxiv.org/abs/2607.14099) ⭐️ 8.0/10

研究人员提出了 Just Keep Prompting（JKP），这是一个多轮评估框架，通过最多 10 轮后续对话，使用三种对抗策略反复质疑视觉语言模型（VLM）的答案，来测试其稳定性。 这项工作揭示了 GPT-4o、Gemini 2.5 Pro 和 Qwen3-VL-30B 等最先进 VLM 存在显著的认识论不稳定性，凸显了鲁棒性测试中的一个关键空白，对对话式 AI 系统的安全实际部署具有直接影响。 JKP 框架使用三种策略：对抗性否定、纯粹苏格拉底式质询和上下文感知的苏格拉底式总结，在 STAR 基准的 720 次多轮运行中进行了评估。结果表明，重复提示往往会使模型不稳定，而非改善推理，其中 GPT-4o 最为脆弱和振荡。

rss · arXiv - NLP · Jul 17, 04:00

**背景**: 视觉语言模型（VLM）结合视觉和文本理解来回答关于图像的问题。认识论稳定性指模型在压力或重复提问下保持正确信念的能力。苏格拉底方法是一种通过提问激发批判性思维的对话技巧，启发了 JKP 中使用的提示策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14099">[2607.14099] Just Keep Prompting : Evaluating Repetitive Socratic...</a></li>
<li><a href="https://arxiv.org/html/2607.14099">Just Keep Prompting : Evaluating Repetitive Socratic Prompting in...</a></li>
<li><a href="https://github.com/desenyon/pressbench">desenyon/pressbench: Pushback Resistance & Epistemic Stability ...</a></li>

</ul>
</details>

**标签**: `#Vision-Language Models`, `#Robustness`, `#Evaluation`, `#AI Safety`, `#Conversational AI`

---

<a id="item-14"></a>
## [首个阿拉伯语量子自然语言处理系统](https://arxiv.org/abs/2607.14100) ⭐️ 8.0/10

研究人员开发了首个阿拉伯语量子组合自然语言处理系统，利用预群语法将句子映射到量子电路，并在词序、形态和词义消歧上进行了评估。 这项工作表明量子自然语言处理能够处理像阿拉伯语这样形态丰富的语言，可能为量子计算在语言学中的应用开辟新途径，并将 QNLP 的应用范围扩展到英语之外。 该系统将阿拉伯语句子转换为量子电路，其中主语、动词和宾语成为量子门，连接方式由预群语法依赖关系决定。该系统与经典基线 AraVec 和 AraBERT 进行了比较。

rss · arXiv - NLP · Jul 17, 04:00

**背景**: 量子自然语言处理（QNLP）通过将单词表示为参数化量子电路，将量子计算应用于自然语言处理。预群语法是一种用于句法的代数形式，它为单词分配类型，并使用幺半群结构来组合意义。阿拉伯语是一种形态丰富、词序自由的语言，使其成为组合语义学的一个具有挑战性的测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pregroup_grammar">Pregroup grammar</a></li>
<li><a href="https://en.wikipedia.org/wiki/Quantum_natural_language_processing">Quantum natural language processing - Wikipedia</a></li>
<li><a href="https://github.com/bakrianoo/aravec">GitHub - bakrianoo/ aravec : AraVec is a pre-trained distributed word ...</a></li>

</ul>
</details>

**标签**: `#quantum NLP`, `#Arabic`, `#pregroup grammar`, `#quantum circuits`, `#compositional semantics`

---

<a id="item-15"></a>
## [LLM 智能体文本通信信息丢失，潜在通道被提出](https://arxiv.org/abs/2607.14103) ⭐️ 8.0/10

一篇新论文证明，LLM 智能体通过文本通信时会丢失信息，并提出一种使用稀疏自编码器（SAE）特征的稀疏潜在通信通道，在 28 倍压缩下保持 99.4%的探针准确率，而文本通道仅为 80.4%。 这项工作挑战了文本足以用于多智能体系统中智能体间通信的假设，并可能为 LLM 智能体带来更高效且保留信息的通信协议。 该研究构建了三种通信通道（密集潜在、稀疏潜在和文本），并使用 SAE 特征分析量化信息丢失。Llama 和 Mistral 之间的跨架构对齐通过 Procrustes 对齐实现了 92%的 top-1 检索，但文本往返过程破坏了 88%的 SAE 特征。

rss · arXiv - NLP · Jul 17, 04:00

**背景**: 多智能体系统（MAS）通常依赖 LLM 智能体通过自然语言文本进行通信。然而，文本可能无法捕捉内部表示的丰富性。稀疏自编码器（SAE）用于从 LLM 激活中提取可解释的特征，从而分析不同通信通道中的信息内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.14103">Latent Communication Between Language Model Agents: Channels...</a></li>
<li><a href="https://www.emergentmind.com/topics/latent-communication">Latent Communication in AI Systems</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#large language models`, `#sparse autoencoders`, `#latent communication`, `#information theory`

---

<a id="item-16"></a>
## [TTCD：具有逐词元时间的连续扩散语言模型](https://arxiv.org/abs/2607.14106) ⭐️ 8.0/10

研究人员提出了词元时间连续扩散（TTCD），这是一种在连续空间中运行并为每个词元分配独立时间的扩散语言模型，使得不同词元可以以不同速率去噪。在 OpenWebText 上训练并通过自蒸馏的 1.6 亿参数 TTCD 模型，在高加速比下，无论是在无条件生成还是条件生成方面，都优于离散扩散模型。 TTCD 通过使用连续空间和逐词元时间，解决了离散扩散模型在高加速比下因并行词元采样导致不准确的关键限制。这有望实现更快、更准确的文本生成，惠及条件生成和结构化输出任务（如数独求解）等应用。 TTCD 确定性地将高斯噪声映射到最终词元画布，无需进一步采样，从而避免了并行词元采样误差。逐词元时间允许更确定的词元更快推进，并在精炼过程中实现差异化的词元间影响。

rss · arXiv - NLP · Jul 17, 04:00

**背景**: 扩散语言模型通过迭代去噪词元序列来生成文本，通常操作在离散空间中，并行采样多个词元，这在高加速比下会导致不准确。最初为图像开发的连续扩散模型在连续空间中将噪声映射到数据，但将其适配到离散文本一直具有挑战性。TTCD 引入了逐词元时间这一新颖概念，允许每个词元拥有自己的去噪时间表，从而改进了条件生成和精炼过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.14106">Token Time Continuous Diffusion for Language Modeling</a></li>
<li><a href="https://www.emergentmind.com/topics/continuous-diffusion-for-discrete-text">Continuous Diffusion for Discrete Text</a></li>
<li><a href="https://medium.com/@deblinab101/bridging-two-worlds-how-diffusion-models-are-catching-up-with-large-language-models-0310c9b1815e">Bridging Two Worlds: How Diffusion Models Are Catching... | Medium</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#language modeling`, `#continuous space`, `#generative AI`, `#machine learning`

---

<a id="item-17"></a>
## [Polestar：基于漂移的缓存与令牌提交优化扩散 LLM 推理](https://arxiv.org/abs/2607.14107) ⭐️ 8.0/10

Polestar 是一个无需训练的推理框架，利用令牌表示漂移作为统一信号，联合优化扩散大语言模型（dLLM）中的 KV 缓存复用和令牌提交。它在数学和编程基准测试中实现了高达 10.73% 的准确率提升、3.7 倍的吞吐量提升以及每次前向传递 3.67 个令牌的高解码并行度。 这项工作解决了 dLLM 推理中的两个关键低效问题——KV 缓存复用效率低和令牌提交次优——这些问题阻碍了实际部署。通过在准确率-吞吐量帕累托前沿上达到新最优，Polestar 可能为基于扩散的语言模型实现更快、更具成本效益的推理。 Polestar 包含两个组件：Polestar-Cache 通过漂移识别过时的 KV 缓存位置并执行稀疏刷新，Polestar-Commit 检测剧烈漂移事件以识别可提交的令牌。该框架在多个 dLLM 系列的数学和编程基准测试中进行了评估，优于现有基线。

rss · arXiv - NLP · Jul 17, 04:00

**背景**: 扩散大语言模型（dLLM）通过并行迭代去噪令牌序列来生成文本，不同于逐个生成令牌的自回归模型。然而，dLLM 中的双向注意力机制阻碍了键值（KV）缓存的高效复用，而用于并行解码的静态置信度阈值可能降低质量。Polestar 利用令牌表示在解码步骤间漂移的观察，联合解决了这两个问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://piirz.medium.com/diffusion-based-llms-how-they-work-and-why-theyre-a-big-deal-a4a1de7636b4">Diffusion -Based LLMs : How They Work (and Why They’re...) | Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/diffusion-llms-rewriting-rules-language-generation-neil-sahota-t82le">Diffusion LLMs : Rewriting the Rules of Language Generation</a></li>

</ul>
</details>

**标签**: `#diffusion LLMs`, `#inference efficiency`, `#KV-cache`, `#token commitment`, `#machine learning systems`

---

<a id="item-18"></a>
## [SeeSE3：探索视觉特征中的三维欧几里得空间](https://arxiv.org/abs/2607.14228) ⭐️ 8.0/10

该论文提出了新的探测方法，用于评估视觉基础模型的特征在多大程度上反映了三维欧几里得空间结构，并发现自监督模型中存在强相关性。 这项工作揭示了自监督视觉模型在没有显式监督的情况下内在地编码了三维空间结构，这可能导致用于视觉里程计和定位的潜在空间导航新技术。 探测方法包括用于拓扑对齐的互邻域度量，以及用于测试从潜在位移中线性访问相机运动几何的庞加莱适配器。

rss · arXiv - Computer Vision · Jul 17, 04:00

**背景**: 视觉基础模型是在大量图像数据上训练的大型神经网络，通常通过自监督学习。SE(3)群表示三维空间中的刚体变换（旋转和平移）。先前的工作通过回归深度或法线来探测三维感知，但本文研究了特征空间本身的结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Rigid_transformation">Rigid transformation - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.14228">SeeSE3: Emergence of 3D Space in Vision Features</a></li>

</ul>
</details>

**标签**: `#3D vision`, `#representation learning`, `#self-supervised learning`, `#foundation models`, `#Euclidean space`

---

<a id="item-19"></a>
## [DCVC-MB：基于状态空间模型的神经 B 帧编码器](https://arxiv.org/abs/2607.14305) ⭐️ 8.0/10

DCVC-MB 提出了一种使用状态空间模型进行 B 帧编码的神经视频编码器，相比 VTM-19.0-LDP 实现了高达 30.45%的 BD 率降低，相比之前的神经编码器降低了 8.98%。 这项工作通过提高 B 帧效率显著推进了神经视频压缩，这对流媒体和存储应用至关重要。它证明了状态空间模型在视频编码任务中可以超越传统的 Transformer 和 RNN。 该编码器采用了 IBP 帧策略、基于状态空间模型的时空融合模型，以及一种熵感知跳过机制以减少编码时间。它还包含两种推理时策略以提升压缩性能。

rss · arXiv - Computer Vision · Jul 17, 04:00

**背景**: 视频编码器通过利用空间和时间冗余来压缩视频。B 帧同时使用过去和未来的帧进行预测，提供比 P 帧更高的压缩率，但需要更复杂的双向处理。传统编码器如 VTM 是手工设计的，而神经视频编码器（NVC）使用深度学习来学习压缩。状态空间模型（SSM）是最近出现的 Transformer 替代方案，用于高效的长序列建模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/DCVC">GitHub - microsoft/DCVC: Deep Contextual Video Compression · GitHub</a></li>
<li><a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Pourreza_Extending_Neural_P-Frame_Codecs_for_B-Frame_Coding_ICCV_2021_paper.pdf">Extending Neural P-Frame Codecs for B - Frame Coding</a></li>

</ul>
</details>

**标签**: `#neural video compression`, `#state-space models`, `#B-frame coding`, `#video codec`, `#deep learning`

---

<a id="item-20"></a>
## [通过线性探测实现整流流的最优自蒸馏](https://arxiv.org/abs/2607.14947) ⭐️ 8.0/10

该论文证明了线性整流流中最优自蒸馏的精确仿射路径恒等式，推导出最优混合系数以及用于修正教师速度场的符号规则。 这为整流流中的最优自蒸馏提供了理论框架，给出了闭式解和实用的调优程序，能够改进生成模型训练并防止崩溃。 最优混合系数遵循符号规则：正混合修正欠正则化的教师，负混合修正过正则化的教师。论文还提供了单次广义交叉验证（GCV）和验证调优程序，避免了网格搜索。

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**背景**: 整流流是一种生成模型，通过学习速度场，利用常微分方程将噪声转化为数据。自蒸馏是指在真实信号和教师生成信号的混合上训练学生模型，这可能导致改进或崩溃。本文研究了带岭正则化的整流流的最优自蒸馏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model - Wikipedia</a></li>
<li><a href="https://deep-diver.github.io/ai-paper-reviewer/paper-reviews/2412.01169/">OmniFlow: Any-to-Any Generation with Multi-Modal Rectified Flows</a></li>
<li><a href="https://labelyourdata.com/articles/machine-learning/model-distillation">Model Distillation : Teacher-Student Training Guide... | Label Your Data</a></li>

</ul>
</details>

**标签**: `#self-distillation`, `#rectified flow`, `#generative models`, `#regularization`, `#theory`

---

<a id="item-21"></a>
## [主观风险分解统一不确定性量化度量](https://arxiv.org/abs/2607.15196) ⭐️ 8.0/10

一篇新的 arXiv 论文提出通过使用严格适当损失分解主观风险来推导认知不确定性和偶然不确定性度量，将许多现有的不确定性量化度量统一在一个共同的理论基础下。 这项工作提供了一个原则性框架，将不确定性量化与学习理论联系起来，可能有助于在机器学习和统计学中更系统地设计不确定性量化方法。 使用反向交叉熵的分解恢复了经典的信息论不确定性项，并且该框架通过引入超额风险、近似误差和估计误差的主观风险类比，扩展到学习理论。

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**背景**: 不确定性量化通常区分认知不确定性（由于缺乏知识）和偶然不确定性（由于固有随机性）。现有的不确定性量化度量往往依赖于特设的公理或特定的损失函数，缺乏统一的推导。本文提出，不确定性量化度量应是更高层次建模决策的结果，特别是基于严格适当损失的主观风险分解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.15196">[2607.15196] Subjective Risk Decomposition : A New View for...</a></li>
<li><a href="https://arxiv.org/html/2607.15196v1">Subjective Risk Decomposition : A New View for Uncertainty...</a></li>

</ul>
</details>

**标签**: `#uncertainty quantification`, `#subjective risk`, `#epistemic uncertainty`, `#aleatoric uncertainty`, `#learning theory`

---

<a id="item-22"></a>
## [PiVoT：从雷达点云实现实时多目标跟踪](https://arxiv.org/abs/2607.13891) ⭐️ 8.0/10

PiVoT 提出了一种变分推理框架，可直接从含噪雷达点云中端到端检测和跟踪大量时变目标，无需外部聚类或检测器。 该工作解决了基于雷达的多目标跟踪中的关键挑战，如严重杂波和大规模目标群体，在无需训练的情况下实现了与深度学习方法相当的性能，对自动驾驶和雷达应用具有重要意义。 PiVoT 融合了理论上有依据的新生剪枝、精确更新的二次到线性复杂度降低以及计算高效的 Doppler Poisson 模型等创新，使其可扩展至上千个目标并对杂波具有鲁棒性。

rss · arXiv - Data Science & Statistics · Jul 17, 04:00

**背景**: 从雷达点云进行多目标跟踪因严重杂波和变化的目标数量而具有挑战性。传统的贝叶斯跟踪器使用 Poisson 测量模型，但在准确性和效率上存在困难。PiVoT 利用变分推理联合推断目标状态、形状、存在概率、数据关联和测量率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.13891">PiVoT: A Variational Solution for Real-time Large-scale Multi - object ...</a></li>
<li><a href="https://runzegan.github.io/projects/pivot/">Poisson Measurements -based Variational Multi-object Detection and...</a></li>

</ul>
</details>

**标签**: `#multi-object tracking`, `#radar`, `#variational inference`, `#point clouds`, `#Bayesian tracking`

---

<a id="item-23"></a>
## [天气数据遭破坏风险上升](https://www.technologyreview.com/2026/07/17/1140622/weather-data-sabotage/) ⭐️ 8.0/10

一篇新的《麻省理工科技评论》文章警告，受预测市场和 AI 天气预报推动，天气数据遭破坏正成为航空、能源和农业等行业日益严重的威胁。 天气预报支撑着多个行业的关键决策，数据遭破坏可能导致经济损失、安全风险甚至人员伤亡。 历史上，天气数据遭破坏是物理性的（如剪断电缆），但预测市场和基于 AI 的天气预报带来了可被操纵的新风险。

rss · MIT Technology Review · Jul 17, 08:57

**背景**: 天气数据来自全球的传感器、卫星和气象站，经处理后形成天气预报，供航空公司、电网运营商和农民使用。破坏行为可能涉及篡改数据收集或操纵 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/17/1140622/weather-data-sabotage/">The risk of weather data sabotage is rising | MIT Technology Review</a></li>
<li><a href="https://asibiont.com/en/blog/risk-sabotazha-dannykh-o-pogode-rastet-chto-nuzhno-znat-biznesu-v-2026-godu">The Hidden Threat: Why the Risk of Weather Data Sabotage Is Rising...</a></li>

</ul>
</details>

**标签**: `#weather data`, `#cybersecurity`, `#critical infrastructure`, `#risk assessment`

---