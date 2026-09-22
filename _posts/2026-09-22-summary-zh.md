---
layout: default
title: "Horizon Summary: 2026-09-22 (ZH)"
date: 2026-09-22
lang: zh
---

> From 111 items, 12 important content pieces were selected

---

1. [小米发布 MiMo v2.6 开放权重大模型系列](#item-1) ⭐️ 8.0/10
2. [NASA 火星采样返回任务实际上已被取消](#item-2) ⭐️ 8.0/10
3. [博客文章认为 AI 生成写作损害真实沟通](#item-3) ⭐️ 8.0/10
4. [xAI 发布 Grok 4.7：权重增加 40%，价格保持不变](#item-4) ⭐️ 8.0/10
5. [Cloudflare Python Workers 结束两年预览正式发布](#item-5) ⭐️ 8.0/10
6. [TypeSafe AI 发布 Jev：一种输出类型化概率决策的“System One”模型](#item-6) ⭐️ 8.0/10
7. [Anthropic 的 Claude Code 将智能体式 AI 编程带入终端](#item-7) ⭐️ 8.0/10
8. [哈佛发布开源四卷本《机器学习系统》教材](#item-8) ⭐️ 8.0/10
9. [Cactus Compute 发布 Needle：面向微型设备的 2-bit 基础模型](#item-9) ⭐️ 8.0/10
10. [AI 评审训练 AI 审稿人，引发科学判断崩塌](#item-10) ⭐️ 8.0/10
11. [TAPe+ML v3 以不到 10 万参数在 COCO 上取得强劲结果](#item-11) ⭐️ 8.0/10
12. [斯坦福发现人脑或由两套古老神经系统融合而成](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [小米发布 MiMo v2.6 开放权重大模型系列](https://mimo.xiaomi.com/mimo-v2-6) ⭐️ 8.0/10

小米发布了 MiMo v2.6 开放权重大模型系列，包含 Flash 和 Pro 两个版本，并罕见地公开了训练细节，包括实时强化学习仪表盘和详尽的技术报告。模型已在 Hugging Face、小米 MiMo 开放平台、AI Studio 和 OpenRouter 上线，API 价格与 v2.5 保持一致。 此次发布加剧了开放权重大模型竞赛，尤其是中美模型系列之间的竞争，并为训练透明度树立了新标杆，可能影响社区预期和监管讨论。同时，它为开发者提供了经济实惠、高性能的自托管和 API 使用选择。 Flash 版本总参数量为 309B，激活参数 15B；Pro 版本总参数量为 1.02T，激活参数 42B。Pro 支持 UltraSpeed 模式，输出速度最高可达 20 倍，并提供 Token 套餐以满足可预测的高并发使用需求。

hackernews · volf_ · Sep 21, 20:12 · [社区讨论](https://news.ycombinator.com/item?id=49792730)

**背景**: 开放权重大模型是指训练后的参数公开可下载、可运行和微调的模型，但训练数据和代码可能仍为专有。MiMo 是小米在这一领域的尝试，与 DeepSeek、Qwen、Llama 和 Mistral 等系列并列。透明训练实践（如分享实时仪表盘和详细报告）较为罕见，有助于研究人员理解和复现模型行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/XiaomiMiMo/MiMo-V2.6-Flash-RL">XiaomiMiMo/ MiMo - V 2 . 6 -Flash-RL · Hugging Face</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-6">MiMo - V 2 . 6 | Xiaomi</a></li>
<li><a href="https://www.xiaomi-mimo-ai.com/blog/open-llm-comparison-2026.html">Open - Weight LLM Landscape 2026 — MiMo vs DeepSeek vs Qwen...</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬小米的透明度，有人称实时强化学习仪表盘是极好的学习工具。其他人对价格实惠的中国模型表示兴奋，就中美 AI 竞争展开辩论，认为能源是关键瓶颈，并分享了 Flash 和 Pro 版本的基准测试链接。

**标签**: `#LLM`, `#open-weights`, `#Xiaomi`, `#AI-competition`, `#model-release`

---

<a id="item-2"></a>
## [NASA 火星采样返回任务实际上已被取消](https://www.science.org/content/article/nasa-s-mars-sample-return-mission-dead) ⭐️ 8.0/10

NASA 与欧洲航天局于 2022 年批准的旗舰级联合项目——火星采样返回任务（MSR），在成本飙升至约 110 亿美元、样本返回时间推迟至 2040 年之后，已于 2026 年实际上被取消。该任务原计划取回由“毅力号”火星车采集的 43 管钛制火星岩石和土壤样本，并在 2033 年左右带回地球。 此次取消使 NASA 失去了将火星样本带回地球进行详细实验室分析的主要途径，而这类分析本可回答火星是否曾经存在生命的问题；同时也让中国天问三号任务在近期火星采样返回领域占据领先地位，后者计划于 2028 年发射、约 2031 年带回样本。这还引发了关于 NASA 旗舰行星科学项目在成本超支和预算优先事项变化下能否持续的更广泛质疑。 NASA 与欧空局的方案依赖三次任务：由“毅力号”负责样本采集、一个样本取回着陆器，以及一个地球返回轨道器，样本将搭乘小型火箭从火星表面发射升空。批评者指出，该架构是围绕阿丽亚娜 64 等传统火箭设计的，而非 SpaceX 的星舰或蓝色起源的新格伦等更新、成本更低的运载工具；此外，MSR 仅能带回约 1.1 磅（0.5 公斤）物质，而阿波罗登月任务带回了 842 磅样本。

hackernews · Muhammad523 · Sep 21, 19:14 · [社区讨论](https://news.ycombinator.com/item?id=49791939)

**背景**: 火星采样返回是一个讨论已久的构想：将火星上采集的岩石和尘土带回地球，用远比任何火星车搭载传感器更强大的实验室仪器进行分析，尤其是寻找过去生命存在的迹象。NASA 的“毅力号”火星车于 2021 年着陆，一直将样本密封在小钛管中并留在火星表面，等待未来任务取回。NASA 与欧空局的 MSR 项目于 2022 年 9 月正式获批，但成本不断攀升和进度一再推迟，最终导致其在 2026 年被取消。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/NASA-ESA_Mars_Sample_Return">NASA-ESA Mars Sample Return - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tianwen-3">Tianwen-3 - Wikipedia</a></li>
<li><a href="https://www.nytimes.com/2025/01/07/science/trump-nasa-mars-sample-return.html">NASA Will Let Trump Decide How to Bring Mars Rocks to Earth - The...</a></li>

</ul>
</details>

**社区讨论**: 评论者强调了中国并行的天问三号任务——该任务近期带回了月球样本，并计划于 2028 年发射火星采样返回任务——以此作为地缘政治上的对照。其他人批评 JPL 领导层让成本升至 110 亿美元，并围绕传统火箭而非星舰等更便宜的方案进行设计；也有人认为，与其花费 200 亿美元执行一次性取回少量岩石的任务，不如投资于可重复使用运载能力。还有一位评论者指出，这篇文章的日期是 2026 年 1 月 6 日，并质疑为何现在才被翻出来。

**标签**: `#NASA`, `#Mars Sample Return`, `#space exploration`, `#space policy`, `#Tianwen-3`

---

<a id="item-3"></a>
## [博客文章认为 AI 生成写作损害真实沟通](https://blog.colinbreck.com/i-dont-want-to-read-what-you-didnt-write/) ⭐️ 8.0/10

Colin Breck 的博客文章《我不想读你没写的东西》认为，AI 生成的文档和写作缺乏作者真实的理解和意图，因此无法有效传达信息。该文章在 Hacker News 上引发热烈讨论，获得 163 个赞和 49 条评论，许多人用信息论类比和实际代码审查中的难题来延伸这一论点。 随着 AI 写作工具在软件工程中日益普及，这一批评凸显了一个日益严重的矛盾：生成的文档可能掩盖而非阐明意图，给审查者带来负担并降低团队沟通效率。社区的强烈共鸣表明，许多工程师已经在日常工作中感受到了这些负面影响。 评论者指出，AI 生成的拉取请求描述可能过于冗长——一个 20 行的改动却附上数页的合理化解释——迫使审查者要么花费大量时间阅读，要么冒着未完全理解就批准的风险。一位评论者用信息论类比：如果你有 1000 比特的语义信息，你不能只给 LLM 300 比特并期望它填补剩下的 700 比特，因为它无法知道那些比特是什么。

hackernews · mooreds · Sep 21, 22:30 · [社区讨论](https://news.ycombinator.com/item?id=49794330)

**背景**: 文章针对软件开发中的一种常见做法：使用 AI 将代码变更事后总结为设计文档或拉取请求描述。随着 GPT-4 等大型语言模型（LLM）的兴起，这种做法日益普遍，这些模型能生成流畅的文本，但缺乏对底层代码或作者意图的真正理解。这场辩论触及技术写作和代码审查的基本原则，即清晰度和共识至关重要。

**社区讨论**: 社区基本赞同文章的前提，评论者分享了对于 AI 生成的拉取请求描述过长且过于防御性的不满，还有人指出文章自己的第一句话读起来就像 AI 生成的写作，颇具讽刺意味。其他人指出了元讽刺和检测 AI 生成文本的困难，而有些人则质疑批评本身是否由 LLM 撰写。

**标签**: `#AI`, `#writing`, `#software engineering`, `#code review`, `#communication`

---

<a id="item-4"></a>
## [xAI 发布 Grok 4.7：权重增加 40%，价格保持不变](https://x.ai/news/grok-4-7) ⭐️ 8.0/10

xAI 发布了新一代前沿模型 Grok 4.7，面向编程、智能体任务和知识工作，其权重比 Grok 4.6 增加了 40%，但价格保持不变，仍为每百万输入 token 2 美元、每百万输出 token 6 美元。该模型已在 GitHub Copilot 中上线，并可通过 xAI API 使用。 此次发布加剧了前沿 AI 实验室之间的竞争，xAI 将 Grok 4.7 定位为对标 Anthropic 传闻中的 Opus 5.5 和 OpenAI 模型的竞品。在模型规模扩大的情况下仍维持原价，表明 xAI 更看重市场份额而非利润率，这可能对竞争对手的定价策略形成压力。 Grok 4.7 在 GDPval 和 AA Briefcase 等测试专业任务（如法律、护理和财务分析）的基准上优于 Grok 4.6，但其输出速度仅为每秒 39.3 个 token，远低于同价位推理模型每秒 72.5 个 token 的中位数。社区成员还指出，该版本比原计划推迟了近两周发布，且在实际使用中感觉更慢、更贵。

hackernews · meetpateltech · Sep 21, 15:50 · [社区讨论](https://news.ycombinator.com/item?id=49788838)

**背景**: Grok 是埃隆·马斯克的 AI 公司 xAI 开发的一系列大语言模型。这些模型以混合专家（MoE）架构著称，xAI 此前曾开源过 Grok-1 等版本。Grok 4.7 是一款推理模型，能够投入额外算力逐步解决复杂问题，这对编程和智能体工作流尤为有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.ai/news/grok-4-7">Introducing Grok 4.7 | SpaceXAI</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-7">Grok 4.7 | SpaceXAI Docs</a></li>
<li><a href="https://artificialanalysis.ai/models/grok-4-7">Grok 4.7 (xhigh) - Intelligence, Performance & Price Analysis | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一：一些用户认为 Grok 4.7 比 Sol 和 Opus 等竞品更慢、更贵，并质疑它是否达到了他们用于编程和智能体工作流的“智能门槛”。另一些人对 xAI 加快的发布节奏表示乐观，期待今年晚些时候 Grok 5 带来更大提升；还有人对比基准测试结果持怀疑态度，并指出不同推理级别下 token 数量存在异常。

**标签**: `#AI`, `#LLM`, `#xAI`, `#Grok`, `#model release`

---

<a id="item-5"></a>
## [Cloudflare Python Workers 结束两年预览正式发布](https://blog.cloudflare.com/python-workers-ga/) ⭐️ 8.0/10

Cloudflare 宣布 Python Workers 正式全面可用，经过约两年的预览期后，Python 成为其无服务器 Workers 平台上的一等公民、完全受支持的语言。该实现通过 Pyodide 将 Python 编译为 WebAssembly 并在 V8 isolate 中运行，同时向上游项目贡献代码，使 HTTP 客户端能够通过 JavaScript 的 fetch API 发起请求。 这一里程碑让 Python 开发者无需离开自己熟悉的语言，就能将无服务器函数部署到 Cloudflare 的全球边缘网络，有望将 Workers 生态从 JavaScript 和 TypeScript 进一步扩展。这也标志着基于 WebAssembly 的无服务器边缘计算运行时日趋成熟，这一趋势可能改变云工作负载的打包与执行方式。 Python Workers 依赖 Pyodide（CPython 移植到 WebAssembly/Emscripten 的版本）以及 pywrangler CLI 工具，包支持通过 PEP 783（PyEmscripten）实现标准化。社区成员指出，与原生运行时相比，冷启动性能和部分架构取舍仍是待解的问题。

hackernews · torutofu · Sep 21, 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49787142)

**背景**: Cloudflare Workers 是一个无服务器平台，代码运行在 Cloudflare 边缘网络的 V8 isolate 中，而非传统容器里。Pyodide 是基于 WebAssembly 的 Python 发行版，可在浏览器和 Node.js 中运行，支持大量纯 Python 包以及部分带 C、C++、Rust 扩展的包。WebAssembly 最初为浏览器设计的紧凑二进制格式，因其体积小、启动快，正越来越多地用于无服务器和边缘计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.cloudflare.com/workers/languages/python/how-python-workers-work/">How Python Workers Work · Cloudflare Workers docs</a></li>
<li><a href="https://pyodide.org/en/stable/index.html">Pyodide — Version 314.0.7</a></li>
<li><a href="https://github.com/cloudflare/python-workers-examples">GitHub - cloudflare / python - workers -examples · GitHub</a></li>

</ul>
</details>

**社区讨论**: 一位 urllib3 维护者提供了上游背景，指出 urllib3 曾合并大量 Pyodide/Emscripten 支持以及后来的 JSPI 支持，且相关资金流向了外部贡献者而非维护者本人。Wasmer 的 CEO 称赞了 Cloudflare 的进展，尤其是 PEP 783 标准化，但也提出了架构方面的担忧；其他评论者则询问冷启动性能，并对标题措辞开了玩笑。

**标签**: `#cloudflare`, `#python`, `#webassembly`, `#serverless`, `#edge-computing`

---

<a id="item-6"></a>
## [TypeSafe AI 发布 Jev：一种输出类型化概率决策的“System One”模型](https://simonwillison.net/2026/Sep/21/jev/) ⭐️ 8.0/10

TypeSafe AI 发布了 Jev，这是其称为“System One 模型”的新模型类别的首个实例（Simon Willison 和 Maggie Appleton 更倾向于称之为“决策模型”）。Jev 接受文本或半结构化的“state”输入，但不生成文本，而是返回浮点数——包括是/否（伯努利，即“Noul”）问题的置信度、选项上的概率分布以及数值评分。 对于垃圾邮件检测、打标签、优先级排序、排名和搜索重排等分类式任务，Jev 提供了一种比标准 LLM 更快、极其便宜的替代方案：输出免费，输入仅为每百万 token 0.042 美元。它可能预示着 AI 技术栈将分化为生成式模型与专用决策模型两类，后者可被软件直接消费而无需解析自然语言文本。 Jev 仅对输入 token 收费（输出免费），价格低于 OpenAI GPT-5 Nano 的每百万输入 token 0.05 美元，并可针对单个 state 并行评估多个问题。但它是彻底的黑箱：只返回一个浮点数，不提供任何解释，这引发了严重的偏见与可解释性担忧；此外问题文本在每次调用中都计入输入，因此大型评分规则会带来实际的单次请求成本。

rss · Simon Willison · Sep 21, 23:09

**背景**: 标准 LLM 按输入和输出 token 计费，输出通常单价更高，且返回自由文本，需要下游代码解析、校验并重试。由 ChatGPT 共同发明人创立的 TypeSafe AI 将 Jev 定位为“前沿智能函数调用”：输入非结构化 state，输出类型化概率决策。“System One”这一名称源自心理学中的双过程理论，用以对比快速直觉式决策与较慢的审慎推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.langchain.com/blog/building-a-harness-with-jev">What Is Jev? A Guide to TypeSafe AI ’s System One Model</a></li>
<li><a href="https://docs.typesafe.ai/introduction">Introduction - TypeSafe AI</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎“决策模型”这一提法，Maggie Appleton 建议的名称比 TypeSafe 的“System One”更受认可。Simon Willison 等人则担忧 Jev 代表着向黑箱机器学习的倒退，因为它不为评分提供任何依据，可能掩盖偏见——他特别警告不要用它来给求职者排名。

**标签**: `#LLM`, `#AI models`, `#decision models`, `#TypeSafe AI`, `#inference`

---

<a id="item-7"></a>
## [Anthropic 的 Claude Code 将智能体式 AI 编程带入终端](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 发布了 Claude Code，这是一款在终端中运行的智能体式编程工具，能够理解代码库，并通过自然语言命令执行日常任务、解释复杂代码以及处理 git 工作流。它可以在终端、IDE 中使用，也可以在 GitHub 上通过 @claude 调用；目前 npm 安装方式已被弃用，推荐使用 curl 脚本、Homebrew 和 WinGet 安装。 Claude Code 是 AI 辅助软件工程的重要一步，将 AI 编程助手从 IDE 自动补全推向能够对代码库采取行动的自主终端智能体。它主要影响开发者和 AI/ML 社区，并使 Anthropic 在快速增长的智能体编程市场中与 Cursor、Tabnine、CodeGPT 等工具展开竞争。 Claude Code 需要 Node.js 18 或更高版本，并提供多种安装方式，包括适用于 macOS/Linux 的 curl 脚本、Homebrew、适用于 Windows 的 PowerShell 脚本以及 WinGet，而 npm 包 @anthropic-ai/claude-code 已被弃用。该仓库还包含通过自定义命令和智能体扩展功能的插件，并且 Anthropic 会收集使用数据，例如代码接受或拒绝情况、相关对话数据以及通过 /bug 命令提交的反馈。

rss · GitHub Trending - Daily (All) · Sep 22, 00:28

**背景**: 智能体式编程工具是一类不仅能补全代码，还能自主阅读代码库、编辑文件、运行命令并完成多步骤开发任务的 AI 系统。Claude Code 是 Anthropic 进入这一领域的产物，基于其 Claude 系列大语言模型构建，设计上直接运行在开发者的终端中，而不仅仅局限于编辑器内。这种终端优先的方式与 Cursor、Tabnine 等以 IDE 为中心的助手形成对比，也反映了整个行业向能够代表开发者行动的 AI 智能体转变的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://code.claude.com/docs/en/terminal-guide">Terminal guide for new users - Claude Code Docs</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code">Claude Code Tutorial: Setup and Refactoring in Practice | DataCamp</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#developer tools`, `#Anthropic`, `#terminal`, `#agentic AI`

---

<a id="item-8"></a>
## [哈佛发布开源四卷本《机器学习系统》教材](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

哈佛 CS249r 课程发布了开源教材《机器学习系统：构建人工智能系统的原理与实践》，分为四卷，分别涵盖基础、扩展、智能体 AI 和物理 AI，托管在 mlsysbook.ai 和 GitHub 上。该仓库还提供配套生态，包括 TinyTorch、MLSys·im、Jupyter 实验、硬件套件和幻灯片，并提供中文、日文和韩文翻译。 这为机器学习系统社区提供了一套免费的大学级课程，内容从核心系统基础一直延伸到智能体 AI 和物理 AI 等新兴领域，而这些内容很少在同一份资料中同时出现。它降低了全球学生和从业者学习如何工程化构建 AI 系统（而不仅仅是训练模型）的门槛。 该书被组织为经过验证的四卷系列，每卷都有自动化构建检查，此外还有针对 TinyTorch、MLSys·im、实验、套件和幻灯片的独立验证流水线。TinyTorch 是一个基于 Python 的教学框架，MLSys·im 是一个 Python 模拟器，实验使用 Jupyter notebook，体现出动手实践、代码优先的教学理念。

rss · GitHub Trending - Python · Sep 22, 00:28

**背景**: 机器学习系统（MLSys）是一个跨学科领域，专注于设计、优化和实现高效训练与部署机器学习模型所需的软硬件基础设施。智能体 AI 指的是能够追求目标、使用工具并以一定自主性采取行动的 AI 程序，通常由大语言模型驱动。物理 AI 指的是能够在物理世界中感知、推理并行动的 AI 系统，将模型与传感器、执行器和机器人相结合。哈佛 CS249r 是一门专门教授这些工程原理的课程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Machine_learning_systems">Machine learning systems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_AI">Agentic AI</a></li>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>

</ul>
</details>

**标签**: `#machine-learning-systems`, `#education`, `#textbook`, `#harvard`, `#mlsys`

---

<a id="item-9"></a>
## [Cactus Compute 发布 Needle：面向微型设备的 2-bit 基础模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus Compute 发布了 Needle，这是一个 2-bit 基础模型，以单个 8-29 MB 的二进制文件形式发布，专为手机、可穿戴设备、智能家居、机器人、汽车和微控制器设计。该模型基于 Laddered Simple Attention Network 架构，牺牲通用聊天能力，以在移动端工具调用上超越其 10 倍大小的模型，并在结构化提取上匹配 2-3 倍大的模型。 此次发布推动了端侧 AI 的前沿，表明一个有用的自动化基础模型可以塞进几兆字节中，完全在本地实现工具调用、结构化提取和嵌入，无需云端往返。这可能大幅降低将智能自动化嵌入微控制器和可穿戴设备等资源受限硬件的门槛。 Needle 3 使用 Monarch Hadamard MLP 替代 FFN，采用带因果卷积抽头的 GQA 注意力、通过 gather 读取的 engram n-gram 记忆以及多通道超连接，从 2 层到 20 层的每个深度都是可部署模型。由用户模式编译的字节级语法约束每个 token，每个响应都包含来自学习头的校准置信度分数；据报道，121M 模型能完成 50M 模型的计算量，因为大部分参数位于 engram 中。

rss · GitHub Trending - Python · Sep 22, 00:28

**背景**: 基础模型通常是在广泛数据上训练的大型神经网络，可适应许多下游任务，但其规模通常使其不适用于边缘设备。量化会降低模型权重的数值精度——此处降至 2 bit——以缩小内存和计算需求，但往往会降低准确性。Needle 的引人注目之处在于，它应用了激进的 2-bit 量化和自定义注意力架构，创建了一个小到足以在微控制器上运行的模型，同时仍能执行工具调用和结构化数据提取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/cactus-compute/needle">GitHub - cactus-compute/needle: Automation foundation model for tiny devices: 2-bit, 8-29 MB, tool calls, structured extraction and embeddings on phones, wearables, smart homes, robots, cars and microcontrollers. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>
<li><a href="https://leimao.github.io/article/Neural-Networks-Quantization/">Quantization for Neural Networks - Lei Mao's Log Book</a></li>

</ul>
</details>

**标签**: `#edge-ai`, `#foundation-models`, `#quantization`, `#mobile-ml`, `#embedded-systems`

---

<a id="item-10"></a>
## [AI 评审训练 AI 审稿人，引发科学判断崩塌](https://arxiv.org/abs/2609.20942) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.20942）显示，以 Llama 3.1 8B 为基础，先在 ICLR 2018—2023 官方评审数据上微调出一个审稿模型，再用官方评审与模型生成评审的混合数据在 ICLR 2024 数据上训练后继模型，会导致评分分布被压缩，并降低同一论文层面和语料库层面的语义多样性——作者将这一失效模式称为“科学判断崩塌”。为缓解该问题，他们提出了 TrustReviewer，一个开源的、基于 LLM 的同行评审系统，结合训练时数据筛选与测试时成对激活引导。 随着 LLM 生成的评审越来越多地进入公开数据和未来的训练语料，AI 同行评审可能形成递归循环，因此这项工作揭示了一个具体风险：AI 辅助的科学评估会逐渐丧失判断多样性，并趋向同质化、压缩化的推荐结果。该发现对机器学习研究社区、会议评审流程以及任何使用 AI 生成文本训练模型的人都具有重要意义，因为它表明这种反馈循环即使不出现彻底的模型崩塌，也会降低评估质量。 该研究是对反馈循环的一步受控模拟：在 ICLR 2024 数据上，用官方评审与模型生成评审按系统性变化比例混合，训练四个后继模型，并以评分分布压缩、同一论文层面和语料库层面语义多样性下降来衡量崩塌程度。TrustReviewer 在两个阶段进行干预——训练时预防：在精心筛选的语料上进行单阶段训练，以减少低质量和语义退化的监督信号；测试时纠正：通过成对激活引导，在不进一步训练、也不增加专家标注的情况下缓解残留的崩塌判断。

rss · arXiv - Machine Learning · Sep 21, 04:00

**背景**: 模型崩塌是一个已知现象：生成模型若用自身输出进行训练，会逐渐丧失多样性和保真度，这一现象在基于 AI 生成文本训练 LLM 的讨论中已被广泛关注。ICLR 等会议的同行评审依赖人类审稿人，但 LLM 正越来越多地被用作自动审稿人或审稿助手，其输出可能流入公开数据和未来的训练集。Llama 3.1 8B 是 Meta 开放权重的 80 亿参数指令微调模型，常被用作微调研究的基座。本文将这些线索联系起来，研究当 AI 生成的评审成为下一代 AI 审稿人的训练数据时会发生什么。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.20942">When AI Reviews Train AI Reviewers: Scientific-Judgment Collapse and Mitigation</a></li>
<li><a href="https://github.com/hosytuyen/TrustReviewer">GitHub - hosytuyen/TrustReviewer · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Llama_3.1">Llama 3.1</a></li>

</ul>
</details>

**标签**: `#AI peer review`, `#LLM feedback loops`, `#scientific judgment`, `#model collapse`, `#TrustReviewer`

---

<a id="item-11"></a>
## [TAPe+ML v3 以不到 10 万参数在 COCO 上取得强劲结果](https://arxiv.org/abs/2609.20869) ⭐️ 8.0/10

TAPe+ML v3 提出了一种名为 TAPe（主动感知理论）的紧凑结构化表示，在识别之前先编码感知元素之间的关系，而不是直接处理像素张量。该系统使用不到 10 万个参数，在 COCO 目标检测上报告了 84.7 mAP50 和 65.3 mAP50-95，在 COCO 实例分割上报告了 80.7 mask mAP50 和 58.4 mask mAP50-95，并在 ImageNet-Real 上达到 89.9% 的 Top-1 准确率。 这项工作表明，将部分建模负担从网络参数转移到结构化输入表示上，可以支持数据、内存和计算需求更低的紧凑多任务视觉系统，这对边缘部署和资源受限应用具有重要意义。如果结果成立，它可能挑战当前普遍认为在 COCO 检测和分割上取得竞争力需要大型深度网络的假设。 该系统结合了背景与轮廓处理、局部目标定位、基于原型的分类以及用于协调专用子模型的协调器，并在工业试点中评估了视频场景检测的紧凑性以及分布偏移下的适应能力。然而，arXiv 编号（2609.20869）看起来异常，且没有提供社区讨论或独立复现，因此所报告的数字应谨慎对待。

rss · arXiv - Computer Vision · Sep 21, 04:00

**背景**: TAPe 代表主动感知理论，是一种在识别之前编码感知元素之间关系的结构化表示，其灵感来自人脑通过现实、感知、信息、处理这一链条来感知信息的方式。COCO 是广泛用于目标检测和实例分割的基准，其中 mAP50 衡量 IoU 阈值为 0.50 时的平均精度均值，而 mAP50-95 则在 0.50 到 0.95 的 IoU 阈值上取平均。基于原型的分类将图像与一组学习到的原型进行比较，具有可解释性，且通常比基于 Transformer 的模型计算成本更低。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.20869">[2609.20869] TAPe +ML: A Compact Structured Representation for...</a></li>
<li><a href="https://docs.ultralytics.com/guides/yolo-performance-metrics">YOLO Performance Metrics | Ultralytics</a></li>
<li><a href="https://arxiv.org/abs/2410.20722">[2410.20722] Interpretable Image Classification with Adaptive Prototype-based Vision Transformers</a></li>

</ul>
</details>

**标签**: `#computer-vision`, `#multi-task-learning`, `#efficient-models`, `#object-detection`, `#instance-segmentation`

---

<a id="item-12"></a>
## [斯坦福发现人脑或由两套古老神经系统融合而成](https://www.sciencedaily.com/releases/2026/09/260920222352.htm) ⭐️ 8.0/10

斯坦福大学的研究人员发现，人脑由两套不同的细胞系统发育而来，提示进化过程中融合了两套功能各异的古老神经系统。同一项研究还首次在实验室中培育出人类后脑神经元，为研究 ALS、脊髓性肌萎缩症及其他脑干疾病提供了新平台。 如果大脑确实由两条独立的发育谱系构建而成，这将重塑人们对大脑进化、发育和疾病的基本认识。能够在体外培育人类后脑神经元，为研究 ALS 和脊髓性肌萎缩症提供了急需的模型，这两类疾病专门攻击脑干和运动神经元，目前尚无治愈方法。 后脑（包括脑干）控制呼吸、吞咽和运动协调等生命功能，也是延髓起病型 ALS 受影响最严重的区域。实验室培育的是人类后脑神经元，这意味着它们可能比动物模型更好地再现人类特有的疾病机制，但该研究仍处于发现阶段，尚未成为疗法。

rss · ScienceDaily Health · Sep 21, 10:12

**背景**: 传统上，人脑被视为一个单一器官，分为前脑、中脑和后脑等区域，其中后脑在进化上最为古老。ALS（又称渐冻症）是一种罕见的致命性神经退行性疾病，会逐步破坏运动神经元，大多数病例病因不明且无法治愈。脊髓性肌萎缩症是一种由 SMN1 基因突变引起的遗传性神经肌肉疾病，会导致运动神经元丧失和肌肉萎缩，常在婴儿期发病。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ALS_(disease)">ALS (disease)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Spinal_muscular_atrophy">Spinal muscular atrophy</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC4862653/">Hindbrain Neurons as an Essential Hub in the Neuroanatomically...</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#brain development`, `#ALS`, `#stem cells`, `#evolution`

---