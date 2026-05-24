---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 52 items, 13 important content pieces were selected

---

1. [16 字节 Windows 可执行文件生成全屏演示](#item-1) ⭐️ 9.0/10
2. [内存成本占 AI 芯片近三分之二](#item-2) ⭐️ 8.0/10
3. [约束衰减：LLM 智能体在架构规则下表现脆弱](#item-3) ⭐️ 8.0/10
4. [微软开源已知最早的 DOS 源代码](#item-4) ⭐️ 8.0/10
5. [AMD 取消 Vivado 免费版 Linux 支持](#item-5) ⭐️ 8.0/10
6. [Armin Ronacher 批评 AI 生成的错误报告](#item-6) ⭐️ 8.0/10
7. [CodeGraph：预索引知识图谱大幅降低 AI 代理成本](#item-7) ⭐️ 8.0/10
8. [Chrome DevTools MCP：AI 代理控制实时浏览器](#item-8) ⭐️ 8.0/10
9. [面向 AI 代理的开源网络安全技能库（754 项技能）](#item-9) ⭐️ 8.0/10
10. [《秘密知识之书》：精选开发者资源合集](#item-10) ⭐️ 8.0/10
11. [NVlabs 发布 LongLive 2.0，用于长视频生成](#item-11) ⭐️ 8.0/10
12. [yt-dlp：功能丰富的命令行媒体下载工具](#item-12) ⭐️ 8.0/10
13. [下丘脑 Menin 蛋白下降驱动衰老，D-丝氨酸可逆转](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [16 字节 Windows 可执行文件生成全屏演示](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 9.0/10

一个名为“Wake up! 16b”的 16 字节 Windows 可执行文件生成了全屏图形和音频演示，将代码大小优化推向了极限。 这一成就展示了极致的代码压缩技术，激励了演示场景和代码高尔夫社区的进一步创新，并展示了极简编程的潜力。 该可执行文件使用可移植可执行文件（PE）格式，并利用 Windows 自动加载某些 DLL 的特性，使得代码无需显式导入即可直接调用 API 函数。

hackernews · MaximilianEmel · May 24, 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: 演示场景是一个计算机艺术亚文化，专注于创建自包含的视听程序（称为演示），通常有严格的大小限制，如 64KB 或 4KB。代码高尔夫是一种竞赛，旨在为给定任务编写尽可能短的源代码。可执行文件压缩通过将压缩数据与解压代码合并到单个可执行文件中来减小文件大小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene</a></li>
<li><a href="https://en.wikipedia.org/wiki/Code_golf">Code golf - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Executable_compression">Executable compression</a></li>

</ul>
</details>

**社区讨论**: 社区表达了敬畏和钦佩，一位评论者指出此前认为 32 字节无声音演示已是极限，称此作品为“值得退休的杰作”。另一位用户分享了前身演示的相关分析链接，突显了对代码密度的持续兴趣。

**标签**: `#demoscene`, `#code golf`, `#executable compression`, `#low-level programming`, `#x86`

---

<a id="item-2"></a>
## [内存成本占 AI 芯片近三分之二](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

一项新分析显示，由于 AI 工作负载对 DRAM 和 HBM 的需求激增，内存组件现在占 AI 芯片组件总成本的近三分之二。 这一转变凸显了内存是 AI 硬件的主要成本驱动因素，除非内存供应赶上需求，否则可能限制未来的成本降低。它还会影响消费电子产品和推理服务的定价。 该分析基于 AI 加速器的组件成本分解，显示内存占比近年来从约 40%增长到近 66%。这一趋势与 2024 年至今的全球内存供应短缺以及 HBM 晶圆分配增加有关。

hackernews · intelkishan · May 24, 16:31 · [社区讨论](https://news.ycombinator.com/item?id=48258684)

**背景**: AI 芯片（如 GPU 和定制加速器）需要大量高带宽内存（HBM）和 DRAM 来处理海量数据集和模型参数。内存制造是资本密集型产业，且前置时间长，导致 AI 需求激增时出现供应限制。成本份额的转变凸显了内存对 AI 系统经济性的重要性日益增加。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2024–present_global_memory_supply_shortage">2024–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://tech-insider.org/memory-chip-shortage-2026-ai-consumer-electronics/">Memory Chip Shortage 2026: HBM Takes 23% of DRAM Wafers</a></li>
<li><a href="https://intuitionlabs.ai/pdfs/ram-shortage-2025-how-ai-demand-is-raising-dram-prices.pdf">RAM Shortage 2025: How AI Demand is Raising DRAM Prices</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，无需创新，仅等待 DRAM 供应满足需求，就可能实现约 3 倍的硬件成本降低。其他人则强调 RAM 价格大幅上涨（例如 96GB 从 250 美元涨到 1200 美元），并对消费市场的可负担性表示担忧，一些人计划坚持使用旧的 DDR4 平台。

**标签**: `#AI hardware`, `#memory pricing`, `#chip costs`, `#DRAM supply`, `#inference costs`

---

<a id="item-3"></a>
## [约束衰减：LLM 智能体在架构规则下表现脆弱](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

一项系统性研究发现，LLM 智能体存在“约束衰减”现象——在严格的架构、ORM 和框架约束下生成多文件后端代码时，其性能显著下降，断言通过率下降约 30 个百分点。 这一发现凸显了关键可靠性差距：虽然 LLM 智能体在无约束原型设计中表现出色，但在需要严格遵守结构规则的生产级后端开发中仍不可靠。这强调了在智能体编码工作流中更好整合约束的必要性。 由于成本限制，该研究未全面测试前沿模型，因此最新模型的具体性能数据可能有所不同。该现象在 ORM 和架构模式等约定密集型框架中尤为明显。

hackernews · wek · May 24, 12:55 · [社区讨论](https://news.ycombinator.com/item?id=48256912)

**背景**: LLM 智能体是利用大型语言模型自主生成代码的 AI 系统。在生产级后端开发中，代码必须遵循特定的架构规则、ORM 约定和框架约束，这与自由形式的原型设计不同。“约束衰减”指的是随着这些约束累积，性能逐渐下降，使得智能体在复杂、规则密集的任务中不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/overview/2605.06445v1">Constraint Decay : The Fragility of LLM Agents in Backend... | alphaXiv</a></li>
<li><a href="https://agentpatterns.ai/verification/constraint-decay-backend-agents/">Constraint Decay in Backend Code Generation - AgentPatterns.ai</a></li>
<li><a href="https://arxiv.org/abs/2605.06445">[2605.06445] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，行业已通过技能、规则、测试和智能体循环等方式缓解这一问题，但一致认为随着代码库增长，LLM 的困难会加剧。有人将其类比为“钙化”现象，即模式变得僵化，并建议逐步引入约束而非一次性全部添加。

**标签**: `#LLM agents`, `#code generation`, `#software engineering`, `#AI reliability`, `#backend development`

---

<a id="item-4"></a>
## [微软开源已知最早的 DOS 源代码](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

微软开源了已知最早的 DOS 源代码，即“帕特森清单”，由 DOS 反汇编小组通过 OCR 从纸质打印件中恢复。此次发布恰逢 86-DOS 1.00 发布 45 周年。 此次发布让人们前所未有地深入了解 PC 操作系统的起源，因为该代码早于所有先前发布的 DOS 源代码。这是一件重要的历史文物，有助于研究人员和爱好者理解微软基础软件的早期开发过程。 该源代码是通过 OCR 从纸质打印件中费力转录而来，OCR 软件在处理数十年历史的纸张质量时遇到了困难。由 Yufeng Gao 和 Rich Cini 领导的 DOS 反汇编小组完成了恢复工作。

hackernews · DamnInteresting · May 24, 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: DOS（磁盘操作系统）是早期 IBM PC 及其兼容机的基础操作系统。微软最初从西雅图计算机产品公司收购了 86-DOS，并将其授权给 IBM，即 MS-DOS。“帕特森清单”以 86-DOS 的原作者蒂姆·帕特森命名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.microsoft.com/blog/2026/04/28/continuing-the-story-of-early-dos-development/">Continuing the story of early DOS development | Microsoft ...</a></li>
<li><a href="https://www.techspot.com/news/112256-microsoft-releases-earliest-dos-source-code-ever-discovered.html">Microsoft releases the earliest DOS source code ever ...</a></li>
<li><a href="https://onehack.st/t/microsoft-just-open-sourced-45-year-old-dos-code-found-on-paper-printouts-in-a-garage/322059">Microsoft Just Open-Sourced 45-Year-Old DOS Code Found on Paper ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软开源这一历史代码表示感谢，一些人指出随附的 BASIC 源代码同样重要。其他人则惊叹于几千行汇编代码就能创办一家成功的软件公司，并强调了 OCR 恢复过程中的挑战。

**标签**: `#open source`, `#history`, `#Microsoft`, `#DOS`, `#retrocomputing`

---

<a id="item-5"></a>
## [AMD 取消 Vivado 免费版 Linux 支持](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

AMD 的 Vivado 2026.1 将不再为其免费（标准）版提供 Linux 支持，而 Windows 支持保持不变。这一变化引发了 FPGA 社区的强烈反对。 这一举措疏远了依赖 Linux 进行 FPGA 开发的学生、爱好者和开发者，可能将他们推向 Lattice 或开源工具等竞争对手。这可能损害 AMD 的生态系统增长和开发者好感度。 免费版（Vivado 标准版）此前同时支持 Windows 和 Linux；付费的企业版仍支持 Linux。社区成员指出，Windows 无法为交叉编译工作负载提供功能对等。

hackernews · zdw · May 24, 04:14 · [社区讨论](https://news.ycombinator.com/item?id=48254309)

**背景**: Vivado 是 AMD（原 Xilinx）的 FPGA 设计套件。免费的标准版为较小器件提供核心功能，而付费的企业版面向高端 FPGA。Linux 在 FPGA 开发中广泛用于自动化、CI/CD 和交叉编译。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techtrendtrove.com/science-technology/why-is-vivado-2026-1-dropping-linux-support-for-free-tier/">Why is Vivado 2026.1 dropping Linux support for free tier ?</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado ™ Design Suite: Standard & Enterprise Edition</a></li>

</ul>
</details>

**社区讨论**: 社区评论几乎全是负面，用户批评 AMD 的决定损害了生态系统。一些人建议转向 Lattice 或 F4PGA 等开源替代方案，另一些人则感叹 Xilinx 自被 AMD 收购后的衰落。

**标签**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#hardware`

---

<a id="item-6"></a>
## [Armin Ronacher 批评 AI 生成的错误报告](https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything) ⭐️ 8.0/10

Flask 和 Jinja2 的创建者 Armin Ronacher 发表了一篇博客文章，批评 AI 生成的错误报告不准确但充满自信，并倡导由人类观察、结构化的错误报告。 这一批评凸显了开源维护中日益严重的问题：低质量的 AI 生成问题浪费维护者的时间并损害项目健康。它呼吁回归以人为中心的报告方式，以维护开源社区的效率和信任。 Ronacher 提出了一个最小化的错误报告模板：运行了什么命令、期望什么结果、实际发生了什么、以及确切的错误或日志。他指出 AI 生成的报告通常包含虚假的最小复现、错误的根因猜测和不相关的错误列表。

rss · Simon Willison · May 24, 18:46

**背景**: Armin Ronacher 是知名的开源开发者，以创建 Flask Web 框架和 Jinja2 模板引擎而闻名。这篇文章是针对他项目 Pi 收到的“垃圾问题”而写的，反映了 AI 生成内容泛滥开源仓库的广泛趋势。

**标签**: `#open-source`, `#AI`, `#bug reports`, `#software maintenance`, `#developer experience`

---

<a id="item-7"></a>
## [CodeGraph：预索引知识图谱大幅降低 AI 代理成本](https://github.com/colbymchenry/codegraph) ⭐️ 8.0/10

CodeGraph 是一款新的开源工具，可为 Claude Code 和 Cursor 等 AI 编码代理创建预索引的代码知识图谱，将令牌使用量减少约 35%，工具调用减少约 70%，且完全在本地运行。 这显著降低了 AI 辅助开发的成本和延迟，使使用流行编码代理的开发者和团队能够更轻松地获得高级代码智能。 CodeGraph 捆绑了自己的运行时，无需安装 Node.js，并支持 Windows、macOS 和 Linux。它与 Claude Code、Cursor、Codex CLI、opencode 和 Hermes Agent 兼容。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: AI 编码代理通常需要反复读取文件和调用工具来理解代码库，这会消耗令牌并增加延迟。代码知识图谱预先索引文件、函数和类之间的关系，使代理能够更高效地检索相关上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Lum1104/Understand-Anything">GitHub - Lum1104/Understand-Anything: Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more. · GitHub</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling">Programmatic tool calling - Claude API Docs</a></li>
<li><a href="https://github.com/nousresearch/hermes-agent">GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#code knowledge graph`, `#developer tools`, `#LLM optimization`

---

<a id="item-8"></a>
## [Chrome DevTools MCP：AI 代理控制实时浏览器](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了官方 MCP 服务器，使 AI 编码代理能够控制和检查实时 Chrome 浏览器，提供可靠的自动化、调试和性能分析。 这桥接了 AI 编码助手与真实浏览器环境，使代理能够直接通过提示进行自动调试和性能优化，可能显著改善开发者工作流程。 该服务器使用 Puppeteer 进行自动化，使用 Chrome DevTools 进行跟踪；默认收集使用统计信息，但可通过 --no-usage-statistics 标志选择退出。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: 模型上下文协议 (MCP) 是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 LLM 连接到外部工具。MCP 服务器通过标准化接口向 AI 应用程序公开特定功能。Chrome DevTools MCP 是一个官方实现，使 AI 代理能够直接访问浏览器 DevTools 功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/chrome-devtools-mcp: Chrome DevTools for coding agents · GitHub</a></li>
<li><a href="https://developer.chrome.com/blog/chrome-devtools-mcp">Chrome DevTools (MCP) for your AI agent | Blog | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#debugging`, `#automation`

---

<a id="item-9"></a>
## [面向 AI 代理的开源网络安全技能库（754 项技能）](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975 发布了 Anthropic Cybersecurity Skills，这是一个包含 754 项结构化网络安全技能的开源库，这些技能映射到五个主要框架（MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF），并兼容 26 个以上 AI 平台。 该库弥合了网络安全专业知识与 AI 代理之间的鸿沟，使开发者能够为 AI 编码工具配备跨多个框架和平台的标准化安全知识，有望加速安全 AI 开发。 这些技能涵盖 26 个安全领域，并遵循 agentskills.io 开放标准，确保在 Claude Code、GitHub Copilot、Codex CLI、Cursor 和 Gemini CLI 等平台之间可移植。该库采用 Apache 2.0 许可证。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: AI 代理越来越多地协助编码任务，但缺乏结构化的网络安全知识。agentskills.io 标准提供了一种为 AI 代理定义可复用能力的方法。MITRE ATT&CK 和 NIST CSF 等框架广泛用于对网络威胁和防御进行分类，而 MITRE ATLAS 和 D3FEND 分别针对 AI 特定威胁和防御技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/agentskills/agentskills">GitHub - agentskills/agentskills: Specification and documentation for Agent Skills · GitHub</a></li>
<li><a href="https://inference.sh/blog/skills/agent-skills-overview">Agent Skills: The Open Standard for AI Capabilities | blog | inference.sh</a></li>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-10"></a>
## [《秘密知识之书》：精选开发者资源合集](https://github.com/trimstray/the-book-of-secret-knowledge) ⭐️ 8.0/10

仓库 'trimstray/the-book-of-secret-knowledge' 持续维护和扩展，为开发者和系统管理员提供手册、速查表、CLI 工具和安全资源等全面合集。 这份精选列表为 DevOps、系统管理员和安全研究人员提供了一站式参考，节省了搜索时间，并提供了高质量、经过验证的资源。其在 GitHub 上的高人气反映了它对技术社区的价值。 该仓库采用 MIT 许可证，欢迎通过拉取请求贡献内容，注重质量而非数量。它提供 RSS 订阅更新，并有代码贡献者和财务支持者。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: GitHub 上的精选列表（常称为“awesome lists”）是社区驱动的特定主题资源合集。该仓库因其广度而脱颖而出，涵盖从命令行单行命令到渗透测试工具的各种内容，并被专业人士频繁引用。

**标签**: `#curated-list`, `#devops`, `#sysadmin`, `#resources`, `#cli`

---

<a id="item-11"></a>
## [NVlabs 发布 LongLive 2.0，用于长视频生成](https://github.com/NVlabs/LongLive) ⭐️ 8.0/10

NVlabs 发布了 LongLive 2.0，这是一个基于 NVFP4 的并行基础设施，用于长视频生成，并提供了论文、代码和模型。它在 Blackwell GPU 上实现了 45.7 FPS 的推理速度，并带来了 2.15 倍的训练加速。 该版本解决了长视频生成中的速度和内存瓶颈，使其适用于实时交互应用。它将焦点从模型技巧转向全栈基础设施，可能加速该领域的研究和部署。 LongLive 2.0 引入了 Balanced SP，一种序列并行自回归训练方法，将教师强制与并行执行协同设计。它还支持 NVFP4 量化以实现高效推理，并支持多镜头视频训练。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: 长视频生成需要处理长帧序列，计算量大且内存密集。以往的方法通常依赖模型层面的技巧，而 LongLive 2.0 提供了全面的基础设施解决方案。NVFP4 是 NVIDIA 的 4 位浮点格式，可在保持质量的同时减少内存并加速计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.18739">[2605.18739] LongLive-2.0: An NVFP4 Parallel Infrastructure for Long Video Generation</a></li>
<li><a href="https://nvlabs.github.io/LongLive/LongLive2/">LongLive - 2 . 0</a></li>
<li><a href="https://www.buildfastwithai.com/blogs/longlive-2-nvidia-nvfp4-video-2026">LongLive - 2 . 0 : NVIDIA's NVFP4 Long Video Infra | Build Fast with AI</a></li>

</ul>
</details>

**标签**: `#video generation`, `#deep learning`, `#infrastructure`, `#NVIDIA`, `#research`

---

<a id="item-12"></a>
## [yt-dlp：功能丰富的命令行媒体下载工具](https://github.com/yt-dlp/yt-dlp) ⭐️ 8.0/10

yt-dlp 是一个功能丰富的命令行音视频下载器，支持数千个网站，作为 youtube-dl 的一个分支正在积极维护。 它为开发缓慢的 youtube-dl 提供了一个可靠且持续更新的替代方案，确保用户能够从众多平台下载媒体，并享受现代功能和修复。 yt-dlp 基于已停止维护的 youtube-dlc 分支，包含赞助商块集成、缩略图嵌入等功能，并支持 YouTube 之外的许多其他网站。

rss · GitHub Trending - Daily (All) · May 24, 22:52

**背景**: youtube-dl 是一个流行的开源命令行工具，用于从 YouTube 及超过 1000 个其他网站下载视频。然而，其开发速度放缓，因此社区创建了 yt-dlp 作为分支，提供更快的更新和更多功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/yt-dlp">yt-dlp</a></li>
<li><a href="https://en.wikipedia.org/wiki/Youtube-dl">youtube-dl - Wikipedia</a></li>
<li><a href="https://yt-dlp-docs.netlify.app/docs/basic-usage/getting-started/">Getting Started | Unofficial yt - dlp Documentation</a></li>

</ul>
</details>

**标签**: `#video-downloader`, `#command-line`, `#open-source`, `#youtube-dl`, `#media`

---

<a id="item-13"></a>
## [下丘脑 Menin 蛋白下降驱动衰老，D-丝氨酸可逆转](https://www.sciencedaily.com/releases/2026/05/260524012959.htm) ⭐️ 8.0/10

研究人员发现，下丘脑中 Menin 蛋白水平下降会引发小鼠的炎症、记忆丧失和骨骼退化，而恢复 Menin 或补充 D-丝氨酸可逆转这些衰老效应。 这项研究确定了大脑中一个新的衰老分子驱动因素，并表明一种简单的氨基酸补充剂可能对抗与年龄相关的认知衰退，为抗衰老疗法开辟了新途径。 该研究在小鼠中进行，因此对人类是否适用尚未证实；D-丝氨酸已作为补充剂上市，但其长期效果和针对衰老的最佳剂量尚不清楚。

rss · ScienceDaily Health · May 24, 05:40

**背景**: 下丘脑是控制激素释放和新陈代谢的大脑区域，其功能失调与衰老有关。Menin 是一种支架蛋白，调节基因转录和细胞信号传导。D-丝氨酸是一种调节 NMDA 受体的氨基酸，参与学习和记忆过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MEN1">MEN1 - Wikipedia</a></li>
<li><a href="https://examine.com/supplements/d-serine/">D - Serine benefits, dosage, and side effects</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9671837/">Understanding the aging hypothalamus, one cell at a time - PMC</a></li>

</ul>
</details>

**标签**: `#aging`, `#neuroscience`, `#protein`, `#supplement`, `#brain health`

---