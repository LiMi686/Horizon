---
layout: default
title: "Horizon Summary: 2026-05-21 (ZH)"
date: 2026-05-21
lang: zh
---

> From 118 items, 37 important content pieces were selected

---

1. [通过扩散模型对几乎任何条件进行高斯过程推断](#item-1) ⭐️ 9.0/10
2. [谷歌在搜索中测试 AI 生成广告](#item-2) ⭐️ 8.0/10
3. [在 2021 款 MacBook 上本地索引视频，使用 Gemma 4 31B](#item-3) ⭐️ 8.0/10
4. [340 多家地方新闻媒体限制互联网档案馆访问](#item-4) ⭐️ 8.0/10
5. [Google Antigravity IDE 更新引发用户强烈不满](#item-5) ⭐️ 8.0/10
6. [Datasette Agent：数据探索的 AI 助手](#item-6) ⭐️ 8.0/10
7. [CodeGraph 将代码预索引为知识图谱以赋能 AI 助手](#item-7) ⭐️ 8.0/10
8. [Anthropic 推出官方 Claude Code 插件目录](#item-8) ⭐️ 8.0/10
9. [NVlabs/Sana：高效高分辨率图像合成](#item-9) ⭐️ 8.0/10
10. [数据探针：理解数据对 LLM 影响的新方法](#item-10) ⭐️ 8.0/10
11. [面向生产环境文档 AI 的微服务架构](#item-11) ⭐️ 8.0/10
12. [个人健康记录上下文提升大模型健康回答质量](#item-12) ⭐️ 8.0/10
13. [代理网络中的信任必须内建，而非外挂](#item-13) ⭐️ 8.0/10
14. [ReElicit：系统提示的贝叶斯优化方法](#item-14) ⭐️ 8.0/10
15. [DecisionBench：评估 AI 工作流中的涌现委托基准](#item-15) ⭐️ 8.0/10
16. [掩码扩散模型的神经互信息估计](#item-16) ⭐️ 8.0/10
17. [TabPFN-MT：面向表格数据的多任务上下文学习器](#item-17) ⭐️ 8.0/10
18. [理论解释扩散模型在流形上的高效性](#item-18) ⭐️ 8.0/10
19. [MagBridge-Battery：用于锂离子磁测量的合成数据集](#item-19) ⭐️ 8.0/10
20. [LEAP：基于大语言模型的钙钛矿添加剂主动学习框架](#item-20) ⭐️ 8.0/10
21. [GROW：将 GRPO 与状态-动作建模对齐用于 VLM 智能体](#item-21) ⭐️ 8.0/10
22. [CP-MoE：保持一致性的混合专家持续学习框架](#item-22) ⭐️ 8.0/10
23. [数据缩放：预测贡献谱的渐进覆盖](#item-23) ⭐️ 8.0/10
24. [FlowLM：通过流匹配实现少步文本生成](#item-24) ⭐️ 8.0/10
25. [ProxyCoT：通过代理思维链提升长上下文推理](#item-25) ⭐️ 8.0/10
26. [Artifact-Bench：评估多模态大模型对 AI 视频伪影的检测能力](#item-26) ⭐️ 8.0/10
27. [EgoTraj：用于人体轨迹预测的自我中心多模态数据集](#item-27) ⭐️ 8.0/10
28. [多头注意力作为集成核回归](#item-28) ⭐️ 8.0/10
29. [潜高斯模型的拉普拉斯近似修正](#item-29) ⭐️ 8.0/10
30. [矛盾图确定 VC 维数](#item-30) ⭐️ 8.0/10
31. [通过最优传输分析迁移学习的样本复杂度](#item-31) ⭐️ 8.0/10
32. [GAME：一种处理重叠子组矩阵补全的凸方法](#item-32) ⭐️ 8.0/10
33. [基于梯度相似性的新型可计算模型复杂度度量](#item-33) ⭐️ 8.0/10
34. [CLAIR：一种感知污染的联邦 LoRA 微调框架](#item-34) ⭐️ 8.0/10
35. [Anthropic 的 Code with Claude 活动展示 AI 编程未来](#item-35) ⭐️ 8.0/10
36. [研究人员起诉特朗普政府，事关在线安全](#item-36) ⭐️ 8.0/10
37. [PerturbFate 工具揭示癌症突变的隐藏弱点](#item-37) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [通过扩散模型对几乎任何条件进行高斯过程推断](https://arxiv.org/abs/2605.21041) ⭐️ 9.0/10

该论文建立了高斯过程与线性扩散模型之间的显式等价关系，通过简单的蒙特卡洛近似，实现了对任意似然（如非线性物理和自然语言）的精确高斯过程条件推断。 这一突破将高斯过程推断扩展到传统的线性高斯框架之外，使实践者无需专门推导即可将复杂的现实世界知识（包括大语言模型的输出）作为条件信息纳入模型。 该方法在线性高斯情况下精确恢复标准 GP 条件推断，并通过白化隔离非高斯动力学，最小化 Wasserstein-2 传输代价并消除数值刚性。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: 高斯过程是一种强大的贝叶斯函数建模工具，但精确推断仅限于共轭（线性高斯）设置。扩散模型是一类通过逆转加噪过程进行生成的模型。该工作将两者桥接，为任意似然条件下的 GP 推断提供了通用方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_process">Gaussian process - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2605.21041">Conditioning Gaussian Processes on Almost Anything</a></li>
<li><a href="https://en.wikipedia.org/wiki/Whitening_transformation">Whitening transformation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Gaussian Processes`, `#Diffusion Models`, `#Probabilistic Inference`, `#Machine Learning`, `#Bayesian Methods`

---

<a id="item-2"></a>
## [谷歌在搜索中测试 AI 生成广告](https://blog.google/products/ads-commerce/google-marketing-live-search-ads/) ⭐️ 8.0/10

谷歌宣布正在搜索中测试新的 AI 驱动广告格式，包括对话式发现广告和 AI 生成的购物广告，这些广告利用 Gemini 撰写定制产品说明。该公司还在扩展其 Direct Offers 试点项目，允许广告商在 AI 模式中直接呈现独家优惠。 将 AI 生成的广告直接整合到搜索结果中，引发了关于用户操纵和搜索实用性下降的担忧，因为广告变得与自然内容难以区分。这也标志着在线广告的重大转变，AI 个性化可能显著影响用户体验和信任。 新的广告格式包括对话式发现广告，通过突出产品特点来回答用户具体问题，以及由 Gemini 生成定制说明的 AI 购物广告。Direct Offers 试点项目仍处于 alpha 阶段，允许广告商在 AI 模式中直接提供如 20%折扣的独家优惠。

hackernews · sofumel · May 21, 09:49 · [社区讨论](https://news.ycombinator.com/item?id=48220105)

**背景**: 谷歌的搜索结果长期以来一直包含付费广告，但这些广告通常有标注且与自然结果分开。随着 AI 驱动搜索的兴起，谷歌正在将 Gemini 整合到广告中，以创建个性化的对话体验。Direct Offers 试点是谷歌向代理型商务（AI 充当销售人员）更广泛推进的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/products/ads-commerce/google-marketing-live-search-ads/">New ad formats built with Gemini coming to Google Search</a></li>
<li><a href="https://www.engadget.com/2178075/google-is-bringing-new-ai-powered-ad-formats-to-search/">Google is bringing new AI-powered ad formats to search - Engadget</a></li>
<li><a href="https://www.accelerateddigitalmedia.com/insights/agentic-commerce-googles-direct-offers-pilot-is-bringing-paid-ads-to-ai-mode/">Agentic Commerce: Google’s “Direct Offers” Pilot is Bringing Paid Ads to AI Mode - Accelerated Digital Media</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈担忧，用户称 AI 生成的广告是“AI 广告邪恶本质的浓缩”，并担心谷歌收集如何有效影响人们的训练数据。一些用户计划屏蔽谷歌的爬虫，而另一些用户则建议像维基百科这样的公共机构应提供替代搜索 API。

**标签**: `#AI`, `#advertising`, `#Google`, `#search`, `#ethics`

---

<a id="item-3"></a>
## [在 2021 款 MacBook 上本地索引视频，使用 Gemma 4 31B](https://blog.simbastack.com/indexed-a-year-of-video-locally/) ⭐️ 8.0/10

一位开发者使用 Gemma 4 31B 模型和 50GB 交换空间，在 2021 款 MacBook 上本地索引了一年的个人视频素材，并发布了名为 Framedex 的开源工具，采用 MIT 许可证。 这表明大型语言模型可以在消费级硬件上运行，用于视频索引等实际任务，有望实现保护隐私的本地 AI 辅助视频编辑和归档工作流。 使用的模型是 Google 的 Gemma 4 31B，一个稠密的 310 亿参数模型，在 2021 款 MacBook 上使用 50GB 交换内存运行。作者计划将该索引与 DaVinci Resolve 集成，实现 AI 辅助视频编辑。

hackernews · asenna · May 21, 14:01 · [社区讨论](https://news.ycombinator.com/item?id=48222733)

**背景**: Gemma 4 是 Google DeepMind 推出的开放模型系列，专为高级推理、编码和智能体工作流设计。交换内存允许系统在物理 RAM 耗尽时使用磁盘空间作为虚拟 RAM，但速度较慢且可能加速 SSD 磨损。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://build.nvidia.com/google/gemma-4-31b-it">gemma - 4 - 31 b -it Model by Google | NVIDIA NIM</a></li>
<li><a href="https://deepmind.google/models/gemma/gemma-4/">Gemma 4 is a family of open models , purpose-built for advanced...</a></li>
<li><a href="https://itsfoss.com/swap-size/">How Much Swap Should You Use in Linux?</a></li>

</ul>
</details>

**社区讨论**: 评论者担心大量交换会加速 SSD 磨损，并指出 4 位量化的 Gemma 4 31B 仅需约 19 GiB，而非 28.4 GiB。作者回应称已在 GitHub 上发布工具，并分享了 AI 辅助视频编辑的计划。

**标签**: `#local AI`, `#video indexing`, `#Gemma`, `#open source`, `#machine learning`

---

<a id="item-4"></a>
## [340 多家地方新闻媒体限制互联网档案馆访问](https://www.niemanlab.org/2026/05/more-than-340-local-news-outlets-are-limiting-the-internet-archives-access-to-their-journalism/) ⭐️ 8.0/10

据尼曼实验室 2026 年 5 月报道，超过 340 家地方新闻媒体已实施限制措施，阻止互联网档案馆的 Wayback Machine 抓取和保存其新闻报道。 这威胁到地方新闻的长期保存，并减少了 AI 模型可用的多样化训练数据，可能加剧信息垄断，削弱公众获取历史新闻的能力。 这些限制可能涉及 robots.txt 指令或技术封锁，阻止 Wayback Machine 存档内容。此举反映了出版商保护收入与互联网档案馆普及知识使命之间日益加剧的紧张关系。

hackernews · jaredwiener · May 21, 16:59 · [社区讨论](https://news.ycombinator.com/item?id=48225838)

**背景**: 互联网档案馆的 Wayback Machine 于 2001 年启动，已存档超过 1 万亿个网页以保存数字历史。新闻媒体因担心 AI 公司无偿使用其内容进行训练而日益加强访问限制，引发了关于 AI 时代知识产权和合理使用的广泛讨论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive_Wayback_Machine">Internet Archive Wayback Machine</a></li>
<li><a href="https://guides.library.yale.edu/c.php?g=870243&p=7146684">Intellectual Property Rights and Web Archiving - Web Archiving @ Yale - Yale University Library Research Guides at Yale University</a></li>

</ul>
</details>

**社区讨论**: 评论者观点不一：有人建议采取临时封锁（如一周）作为折衷方案，也有人对历史保存的损失表示惋惜。少数人认为限制是保护知识产权的必要步骤，还有人提议为 AI 训练数据访问建立微支付系统。

**标签**: `#Internet Archive`, `#digital preservation`, `#journalism`, `#AI training data`, `#web archiving`

---

<a id="item-5"></a>
## [Google Antigravity IDE 更新引发用户强烈不满](https://www.0xsid.com/blog/antigravity-bait-n-switch) ⭐️ 8.0/10

Google 将 Antigravity IDE 更新至 2.0 版本，用智能体优先的聊天界面取代了传统代码编辑器，实质上移除了核心 IDE 功能，严重干扰了现有用户的工作流程。 这种“诱饵调包”行为损害了用户对 Google 开发者工具的信任，并凸显其产品策略的不一致性，可能促使开发者转向 Cursor 或 Claude Code 等竞争对手。 该更新未经用户同意自动替换了原有 IDE，破坏了 Remote-WSL 连接，并以需要借助社区脚本手动恢复的方式合并了用户设置。

hackernews · ssiddharth · May 21, 13:50 · [社区讨论](https://news.ycombinator.com/item?id=48222529)

**背景**: Antigravity 是 Google 推出的 AI 驱动 IDE，最初提供带有 AI 辅助的熟悉编辑器。2.0 版本转向智能体优先范式，与 Claude Code 和 OpenAI Codex 等工具竞争，但代价是放弃了传统编辑界面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Antigravity">Google Antigravity - Wikipedia</a></li>
<li><a href="https://timesofindia.indiatimes.com/technology/tech-news/google-antigravity-2-0-goes-after-claude-code-and-openai-codex-with-a-full-agent-first-rebuild/articleshow/131209670.cms">Google Antigravity 2.0 goes after Claude Code and OpenAI Codex with a full agent-first rebuild</a></li>
<li><a href="https://piunikaweb.com/2026/05/20/fix-google-antigravity-2-0-missing-ide-error/">Google Antigravity 2.0 broken? Missing IDE and folder fixes explained</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了沮丧和不信任，用户 ctippett 称之为“诱饵调包”，postalcoder 批评 Google 缺乏专注。部分用户分享了技术解决方案，例如 antimirov 提供的用于恢复旧设置的 Python 脚本。

**标签**: `#Google`, `#IDE`, `#product strategy`, `#developer tools`, `#AI`

---

<a id="item-6"></a>
## [Datasette Agent：数据探索的 AI 助手](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything) ⭐️ 8.0/10

Simon Willison 宣布了 Datasette Agent 的首个版本，这是一个可扩展的 AI 助手，为 Datasette 提供对话式数据查询和图表生成功能（通过插件实现）。 LLM 与 Datasette 的集成使非技术用户也能轻松进行数据探索，支持自然语言查询和自动图表生成，有望大幅降低数据分析的门槛。 实时演示运行在 Gemini 3.1 Flash-Lite 上，成本低且速度快；助手能生成 SQL 查询并使用 Observable Plot 绘制图表。目前已发布三个插件，包括 datasette-agent-charts 和 datasette-agent-openai-imagegen。

rss · Simon Willison · May 21, 19:52

**背景**: Datasette 是一个用于探索和发布数据的开源工具，常与 SQLite 数据库配合使用。Simon Willison 开发的 LLM Python 库提供了与大型语言模型交互的 CLI 和 Python 接口。Datasette Agent 将这两个项目结合起来，允许用户用自然语言提问并从数据中获取答案。

**标签**: `#Datasette`, `#AI assistant`, `#data exploration`, `#LLM`, `#open source`

---

<a id="item-7"></a>
## [CodeGraph 将代码预索引为知识图谱以赋能 AI 助手](https://github.com/colbymchenry/codegraph) ⭐️ 8.0/10

CodeGraph 是一个新的开源工具，它将代码库预索引为本地知识图谱，从而减少 Claude Code、Cursor、Codex CLI 和 OpenCode 等 AI 编码助手的 token 消耗和工具调用次数。 通过提供对符号关系和调用图的即时访问，CodeGraph 可将成本降低约 35%，工具调用减少约 70%，使 AI 辅助编码对开发者来说更高效、更经济。 在 7 个真实代码库（包括约 1 万文件的 VS Code）上的基准测试显示，中位数节省为成本降低 35%、token 减少 59%、速度提升 49%、工具调用减少 70%。该工具 100% 本地运行，支持 Windows、macOS 和 Linux。

rss · GitHub Trending - Daily (All) · May 21, 22:59

**背景**: 像 Claude Code 这样的 AI 编码助手会生成代理，通过 grep、glob 和 Read 操作扫描文件来探索代码库，每次工具调用都会消耗 token。CodeGraph 将代码预索引为包含符号关系、调用图和代码结构的知识图谱，使代理可以直接查询图谱，而无需扫描文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/colbymchenry/codegraph">colbymchenry/codegraph: Pre - indexed code knowledge graph for...</a></li>

</ul>
</details>

**标签**: `#code intelligence`, `#AI coding assistants`, `#knowledge graph`, `#developer tools`

---

<a id="item-8"></a>
## [Anthropic 推出官方 Claude Code 插件目录](https://github.com/anthropics/claude-plugins-official) ⭐️ 8.0/10

Anthropic 在 GitHub 上发布了官方精选的 Claude Code 高质量插件目录（anthropics/claude-plugins-official），包含 Anthropic 内部开发的插件以及来自合作伙伴和社区的第三方插件。 这个官方插件目录标志着 Claude Code 生态系统的成熟，使开发者更容易发现和安装可信的扩展。它还建立了标准化的插件结构和提交流程，鼓励社区贡献和第三方集成。 插件可以通过命令 '/plugin install {plugin-name}@claude-plugins-official' 或通过 Claude Code 中的“发现”选项卡安装。目录分为两个文件夹：'/plugins' 用于内部插件，'/external_plugins' 用于第三方插件，每个插件都遵循包含必需 'plugin.json' 元数据的标准结构。

rss · GitHub Trending - Daily (All) · May 21, 22:59

**背景**: Claude Code 是 Anthropic 的 AI 编程助手，帮助开发者编写、审查和调试代码。插件通过添加自定义工具、命令和集成来扩展其功能。模型上下文协议（MCP）是一种标准，使这些插件能够与外部服务和数据源通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/plugins">Plugins for Claude Code and Cowork | Anthropic</a></li>
<li><a href="https://www.firecrawl.dev/blog/best-claude-code-plugins">Top 10 Claude Code Plugins to Try in 2026</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#plugins`, `#Anthropic`, `#developer tools`, `#AI`

---

<a id="item-9"></a>
## [NVlabs/Sana：高效高分辨率图像合成](https://github.com/NVlabs/Sana) ⭐️ 8.0/10

NVIDIA 发布了 Sana，这是一个基于线性扩散 Transformer 的高效高分辨率图像合成模型，并提供了多个变体，包括 SANA-1.5、SANA-Sprint、SANA-Video、SANA-WM 和 Sol-RL，以及完整的训练和推理流程。 Sana 将传统扩散 Transformer 的二次复杂度降低到近线性，实现了更快、更省内存的高分辨率图像生成，这可能使生成式 AI 更广泛地应用于更多场景。 该模型支持高达 4K 的分辨率，包含一个 4 位量化版本用于单 GPU 推理，并与 ComfyUI、SGLang 和 Cosmos-RL 集成。SANA-WM 是一个 26 亿参数的世界模型，支持 720p 视频生成和六自由度相机控制。

rss · GitHub Trending - Python · May 21, 22:59

**背景**: 扩散 Transformer（DiT）是一类将扩散过程与 Transformer 架构相结合的生成模型。传统的 DiT 使用二次复杂度的注意力机制，在高分辨率下计算成本高昂。线性注意力将其降低到近线性复杂度，使高分辨率合成更加实用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techmonsterwang.github.io/LiT_page/">LiT: Delving into a Simple Linear Diffusion Transformer for Image...</a></li>
<li><a href="https://arxiv.org/html/2501.12976v1">LiT: Delving into a Simplified Linear Diffusion Transformer for Image...</a></li>
<li><a href="https://www.emergentmind.com/topics/linear-diffusion-transformer-dit">Linear Diffusion Transformer (LiT)</a></li>

</ul>
</details>

**标签**: `#image synthesis`, `#diffusion transformer`, `#generative AI`, `#deep learning`, `#NVIDIA`

---

<a id="item-10"></a>
## [数据探针：理解数据对 LLM 影响的新方法](https://arxiv.org/abs/2605.18801) ⭐️ 8.0/10

一篇立场论文提出开发系统性的数据探针——来自随机过程的合成序列——以从根本上理解数据特征如何影响 LLM 在训练、微调和推理阶段的行为。 这种方法可以减少对计算密集型经验启发式方法进行数据过滤和数据集构建的依赖，为揭示数据在 LLM 性能中的作用提供原则性途径。 探针序列表现出统计特性，可以使用典型集等理论概念进行分析，并推广到描述 LLM 行为。该方法旨在通过系统研究数据特征，超越经验启发式方法。

rss · arXiv - AI · May 21, 04:00

**背景**: 数据对 LLM 至关重要，但理解哪些数据特征对训练、微调、对齐、上下文学习等不同阶段有用仍是一个开放问题。当前方法依赖对大型公共数据集的大量实验来获得经验启发式方法，这计算密集且缺乏原则性理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.18801">[2605.18801] Position: Let's Develop Data Probes to Fundamentally...</a></li>
<li><a href="https://arxiv.org/pdf/2605.18801">Position: Let's Develop Data Probes to Fundamentally Understand...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#data quality`, `#synthetic data`, `#machine learning research`, `#data-centric AI`

---

<a id="item-11"></a>
## [面向生产环境文档 AI 的微服务架构](https://arxiv.org/abs/2605.18818) ⭐️ 8.0/10

一篇新论文提出了一种面向生产规模文档 AI 管道的微服务架构，该架构结合了分类、OCR 和基于 LLM 的字段提取，并提供了每小时处理数千份多页文档的批量分析结果。 这项工作弥合了学术模型研究与生产部署之间的差距，为文档理解提供了具体的架构模式和令人惊讶的发现（例如 OCR 主导延迟），可指导从业者构建高效的实际系统。 关键设计决策包括混合分类、将 GPU 密集型推理与 CPU 密集型编排分离、对 IO 密集型操作采用异步处理以及独立水平扩展；批量分析显示 OCR 主导端到端延迟，系统饱和由共享 GPU 推理容量而非工作进程数量决定。

rss · arXiv - AI · May 21, 04:00

**背景**: 文档 AI 管道通常涉及多个步骤：对文档类型进行分类、执行光学字符识别（OCR）以提取文本，以及使用大型语言模型（LLM）提取结构化字段。在生产规模上部署此类管道需要仔细的架构选择，以管理延迟、资源利用率和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@shahriddhi717/ai-design-patterns-engineering-modular-ml-pipelines-and-agentic-systems-c5f9f7ca29db">AI Design Patterns: Engineering Modular ML Pipelines and... | Medium</a></li>
<li><a href="https://www.lido.app/blog/automatic-document-classification">Automatic Document Classification : How AI Sorts Your Documents</a></li>

</ul>
</details>

**标签**: `#document AI`, `#microservice architecture`, `#production ML`, `#OCR`, `#LLM`

---

<a id="item-12"></a>
## [个人健康记录上下文提升大模型健康回答质量](https://arxiv.org/abs/2605.18937) ⭐️ 8.0/10

一项研究评估了 Gemini 3.0 Flash 在 2257 个患者健康查询上的表现，使用了不同级别的个人健康记录上下文，发现完整的临床记录能显著提升回答的有用性。 这项工作表明，将个人健康记录与大语言模型集成可以增强个性化健康 AI，可能帮助患者更好地理解自身健康状况，并改善临床决策支持。 该研究使用了 1945 份去标识化的个人健康记录和三种查询分布（网络搜索、聊天机器人模板、患者电话），通过 SHARP 框架和临床医生对 95 个查询子集的评分进行评估。

rss · arXiv - AI · May 21, 04:00

**背景**: 个人健康记录（PHR）是由患者管理的健康数据，可包含人口统计信息、疾病、用药和临床记录。像 Gemini 这样的大语言模型（LLM）是经过海量文本数据训练的人工智能系统，能生成类似人类的回答。论文中提到的 SHARP 框架是一个用于评估回答质量的评级系统，尽管该缩写也用于摩托车头盔安全评级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SHARP_(helmet_ratings)">SHARP (helmet ratings ) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_2.5_Flash_Image">Gemini 2.5 Flash Image</a></li>

</ul>
</details>

**标签**: `#large language models`, `#personal health records`, `#health AI`, `#clinical NLP`, `#patient empowerment`

---

<a id="item-13"></a>
## [代理网络中的信任必须内建，而非外挂](https://arxiv.org/abs/2605.19035) ⭐️ 8.0/10

一篇新的愿景论文指出，由于对抗性组合和级联故障等系统性漏洞，代理到代理（A2A）网络中的可信性必须从一开始就进行架构设计，而非事后修补。 该论文指出了新兴 A2A 网络中可信性的关键缺口，这类网络越来越多地用于多步骤任务。所提出的设计理念转变可能影响未来的代理协调框架和 AI 安全标准。 该论文提出了一个包含四个设计支柱的概念框架，用于 A2A 系统中的信任，并指出现有的代理对齐技术无法解决对抗性组合、语义错位和级联操作故障等漏洞。

rss · arXiv - AI · May 21, 04:00

**背景**: 基于大语言模型（LLM）的代理正从独立运行演变为称为代理到代理（A2A）网络的协作生态系统。在这些网络中，异构代理自主协调以解决多步骤任务，但这引入了新的系统性漏洞，现有的针对单个代理的安全技术无法解决。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.19035">Trustworthy Agent Network: Trust in Agent Networks Must Be Baked...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multi-agent_system">Multi - agent system - Wikipedia</a></li>
<li><a href="https://dev.to/willvelida/preventing-cascading-failures-in-ai-agents-p3c">Preventing Cascading Failures in AI Agents - DEV Community</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#agent-to-agent networks`, `#trustworthiness`, `#AI safety`, `#multi-agent systems`

---

<a id="item-14"></a>
## [ReElicit：系统提示的贝叶斯优化方法](https://arxiv.org/abs/2605.19093) ⭐️ 8.0/10

研究人员提出了 ReElicit，一个利用大语言模型（LLM）引发的特征空间进行贝叶斯优化的框架，用于在聚合反馈约束下优化系统提示。 这解决了 AI 系统中仅能获得聚合指标的实际挑战，无需逐示例标签即可高效调整系统提示，这在现实部署中很常见。 ReElicit 在新评估到来时动态重新引发特征空间，使表示适应观察到的提示-分数历史，并在 30 次评估预算下取得了基线中最强的聚合性能。

rss · arXiv - AI · May 21, 04:00

**背景**: 贝叶斯优化是一种无需假设函数形式的序贯策略，用于优化昂贵的黑盒函数。系统提示是控制 AI 行为的文本指令，但当反馈仅为聚合指标（如平均用户满意度）时，调整它们很困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.19093">[2605.19093] Embedding by Elicitation : Dynamic Representations for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_optimization">Bayesian optimization - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Bayesian optimization`, `#prompt engineering`, `#LLM`, `#system prompts`, `#AI alignment`

---

<a id="item-15"></a>
## [DecisionBench：评估 AI 工作流中的涌现委托基准](https://arxiv.org/abs/2605.19099) ⭐️ 8.0/10

研究人员推出了 DecisionBench，这是一个用于评估长期代理工作流中涌现委托的标准化基准，涵盖 7 个供应商家族的 11 个模型和 23,375 个任务实例。 该基准填补了多智能体编排评估的关键空白，揭示了仅凭质量指标会遗漏委托信号，并且未来方法还有 15-31 个百分点的未实现提升空间。 该基座包括任务套件（GAIA、tau-bench、BFCL 多轮）、带有 call_model 和 read_profile 的委托接口、确定性技能注释层，以及涵盖质量、成本、延迟、委托率、路由保真度、供应商自偏好和反事实上限的多轴指标。

rss · arXiv - AI · May 21, 04:00

**背景**: 涌现委托是指 AI 智能体在多智能体系统中自主决定何时以及如何将子任务委托给其他智能体的能力。现有基准通常关注单智能体性能或简单协调，缺乏对复杂长期委托场景的标准化评估。DecisionBench 提供了一个受控基座，以在不同感知条件和传递通道下隔离和测量委托行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2311.12983">[2311.12983] GAIA : a benchmark for General AI Assistants</a></li>
<li><a href="https://ukgovernmentbeis.github.io/inspect_evals/evals/assistants/gaia/">GAIA : A Benchmark for General AI Assistants</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#multi-agent systems`, `#AI`, `#delegation`, `#agentic workflows`

---

<a id="item-16"></a>
## [掩码扩散模型的神经互信息估计](https://arxiv.org/abs/2605.20187) ⭐️ 8.0/10

提出了一种神经估计器，可从掩码扩散模型的隐藏状态中计算成对互信息，实现互信息引导的并行解码，将推理步骤减少 3-5 倍。 这项工作弥合了掩码扩散模型在可解释性和效率之间的差距，提供了一种实用方法，在保持生成质量的同时加速生成，适用于蛋白质序列设计和结构化输出生成。 该估计器使用模型自身条件分布的真实互信息进行训练，并在单次前向传播中预测完整的互信息矩阵。在数独和 ESM-C 蛋白质生成任务上验证，优于基于熵的并行化方法。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 掩码扩散模型通过迭代去噪掩码标记来生成数据，但仅提供边际条件分布，不提供显式的变量间依赖关系。互信息量化了变量之间的依赖程度，可用于识别条件独立子集以指导并行解码。本文引入了一种神经估计器，从模型的隐藏状态中提取该信息。

**标签**: `#mutual information`, `#masked diffusion models`, `#generative modeling`, `#protein sequence generation`, `#parallel decoding`

---

<a id="item-17"></a>
## [TabPFN-MT：面向表格数据的多任务上下文学习器](https://arxiv.org/abs/2605.20234) ⭐️ 8.0/10

TabPFN-MT 将先验数据拟合网络（PFN）扩展到表格数据的多任务上下文学习，能够通过单次前向传播同时预测多个目标，并在中小型数据集上取得了最先进的结果。 这项工作解决了 PFN 的关键局限——单任务推理——通过实现任务间信息共享并将推理成本从 O(T) 次前向传播降低到 O(1) 次，这对于资源受限环境下的多目标表格应用至关重要。 TabPFN-MT 使用扩展的 y 编码器和共享解码器头来捕获任务间依赖关系，并在多目标合成先验上进行训练。在 344 个数据集上，它取得了 4.89 的整体准确率排名，是所有测试模型中平均排名最高的。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 先验数据拟合网络（PFN）是基于 Transformer 的模型，用于表格数据的上下文学习，但最初设计为单任务推理，需要多次前向传播来处理多个目标。TabPFN-MT 在此基础上通过支持单个上下文内的多任务学习，使其特别适用于传统基于梯度的方法难以处理的中小型数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TabPFN">TabPFN</a></li>

</ul>
</details>

**标签**: `#tabular data`, `#in-context learning`, `#multitask learning`, `#deep learning`, `#prior-data fitted networks`

---

<a id="item-18"></a>
## [理论解释扩散模型在流形上的高效性](https://arxiv.org/abs/2605.20235) ⭐️ 8.0/10

本文识别出扩散模型中的一种“坍塌与精炼”机制，解释了当数据位于低维流形上时模型如何绕过维度灾难，并提出了 Score 诱导的潜在扩散（SiLD），这是一个新的两阶段框架，在单一分数匹配目标下统一了流形学习和密度估计。 这项工作为扩散模型在高维数据上的经验成功提供了严格的理论基础，可能指导设计更高效的生成模型，其样本复杂度取决于内在维度而非环境维度。 坍塌与精炼机制在不同噪声尺度下运作：在小噪声下，分数的奇异性驱动维度坍塌到数据流形上；在中等噪声下，训练精炼学习到的流形上的密度。SiLD 用原则性的分数匹配目标取代了基于 VAE 的潜在扩散模型中的启发式 KL 正则化。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 扩散模型通过逆转噪声过程生成数据，但其在低维流形支撑的高维数据上的理论效率此前未被很好理解。流形假设认为现实世界的高维数据集中在低维流形附近。分数匹配是一种学习数据对数密度梯度（分数）的技术。

**标签**: `#diffusion models`, `#manifold hypothesis`, `#score matching`, `#generative models`, `#theory`

---

<a id="item-19"></a>
## [MagBridge-Battery：用于锂离子磁测量的合成数据集](https://arxiv.org/abs/2605.20240) ⭐️ 8.0/10

作者发布了 MagBridge-Battery v1.0，这是一个包含 6,760 个磁场信号的合成数据集，用于锂离子电池健康状态诊断，将真实磁形态与退化标签联系起来。 该数据集填补了关键空白，提供了首个与退化标签配对的公开合成磁测量数据集，使得利用磁测量进行非侵入式电池健康估计的研究成为可能。 该数据集包含 5,600 个基础样本、600 个传感器异常样本和 560 个低电压外推样本，并经过验证的电池无关基准划分。受控标签洗牌消融实验证实，该桥梁非平凡地编码了 SOH 信息。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 电池健康诊断传统上依赖于在电池端子处测量的电化学信号。磁测量可以提供额外信息，但由于缺乏将磁测量与退化标签配对的公开数据集，相关开发受到阻碍。

**标签**: `#battery health`, `#magnetometry`, `#dataset`, `#state-of-health`, `#Li-ion`

---

<a id="item-20"></a>
## [LEAP：基于大语言模型的钙钛矿添加剂主动学习框架](https://arxiv.org/abs/2605.20242) ⭐️ 8.0/10

研究人员开发了 LEAP，一个将领域专用大语言模型与主动学习相结合的闭环框架，用于高效发现钙钛矿前驱体添加剂，实现了 21.32%的冠军器件效率。 这项工作展示了将大语言模型与主动学习相结合用于材料发现的新方法，有望通过取代低效的试错筛选来加速高性能钙钛矿太阳能电池的开发。 领域专用大语言模型从文献中提取机制相关知识，并通过可解释的描述符表示分子，随后在贝叶斯优化中用于低数据条件下的不确定性感知优先级排序。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 钙钛矿太阳能电池是一种有前景的光伏技术，但其性能在很大程度上取决于前驱体添加剂，而这类添加剂通常通过缓慢的试错法发现。大语言模型可以处理科学文献，而主动学习通过优先考虑有希望的候选物来高效探索化学空间。

**标签**: `#perovskite solar cells`, `#large language models`, `#active learning`, `#materials discovery`, `#Bayesian optimization`

---

<a id="item-21"></a>
## [GROW：将 GRPO 与状态-动作建模对齐用于 VLM 智能体](https://arxiv.org/abs/2605.20246) ⭐️ 8.0/10

这解决了标准 GRPO 在多轮开放世界任务中的关键限制（完整轨迹导致长上下文和噪声），可能推动 VLM 智能体研究，并为复杂环境提供更有效的训练方法。 该方法计算状态-动作样本之间的优势，而不是将完整轨迹视为单个实体，并包含一个替代分析，表明在简化假设下目标保留了核心相对策略优化信号。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 视觉语言模型（VLM）智能体结合视觉感知和语言理解，在 Minecraft 等开放世界环境中执行任务。标准 GRPO 对单轮强化学习有效，但难以处理多轮任务，因为它需要完整轨迹作为训练样本，导致长上下文和噪声。

**标签**: `#reinforcement learning`, `#vision-language models`, `#multi-turn agents`, `#GRPO`, `#open-world tasks`

---

<a id="item-22"></a>
## [CP-MoE：保持一致性的混合专家持续学习框架](https://arxiv.org/abs/2605.20247) ⭐️ 8.0/10

CP-MoE 引入了一个瞬态专家和保持一致性的路由偏置，以减轻 LLM 和 VLM 持续学习中的灾难性遗忘。 这项工作解决了基于 MoE 的持续学习中知识迁移与遗忘之间的基本权衡，在 SuperNI 和 VQA v2 等基准上取得了最先进的性能。 CP-MoE 使用瞬态专家捕获早期任务特定更新并引导其集成到稳定专家中，同时通过正则化机制在合并过程中保护重要的历史参数。

rss · arXiv - Machine Learning · May 21, 04:00

**背景**: 持续学习旨在按任务序列训练模型而不遗忘先前任务。灾难性遗忘是指新更新覆盖重要参数。混合专家（MoE）架构使用多个专用子网络（专家）处理不同任务，但现有基于 LoRA 的 MoE 方法难以平衡知识迁移与遗忘。

**标签**: `#continual learning`, `#mixture-of-experts`, `#catastrophic forgetting`, `#LLM`, `#VLM`

---

<a id="item-23"></a>
## [数据缩放：预测贡献谱的渐进覆盖](https://arxiv.org/abs/2605.20196) ⭐️ 8.0/10

该论文引入了一个预测贡献谱来解释数据缩放定律，表明在 12 个语料库中，有效截断秩与训练规模的对数呈线性关系。 该框架为理解更大数据集为何能提升模型性能提供了新颖的理论基础，可能指导 AI 中更高效的数据选择和缩放策略。 有效截断秩 K(N)通过将观测到的额外损失与全局 KL 谱的残差尾部质量匹配来定义，原始谱的合并 R²为 0.96，平滑谱为 0.90。

rss · arXiv - NLP · May 21, 04:00

**背景**: 数据缩放定律描述了模型性能如何随训练数据规模提升，但其潜在机制尚未完全理解。该工作提出缩放对应于逐步覆盖不同数据模式的预测贡献谱。

**标签**: `#scaling laws`, `#language models`, `#data efficiency`, `#theoretical ML`

---

<a id="item-24"></a>
## [FlowLM：通过流匹配实现少步文本生成](https://arxiv.org/abs/2605.20199) ⭐️ 8.0/10

FlowLM 通过高效微调将预训练的扩散语言模型适配到流匹配，实现了高质量少步文本生成，其效果可与甚至超过 2000 步扩散采样。 该方法在保持或提升质量的同时大幅减少语言模型的推理步数，有望在生产系统中实现更快、更高效的文本生成。 微调后的 FlowLM 仅需从头训练一半的轮数即可达到性能饱和，并且它采用预测干净数据的目标进行流匹配，从而持续引导采样过程朝向真实数据分布。

rss · arXiv - NLP · May 21, 04:00

**背景**: 扩散语言模型通过逐步去噪随机噪声来生成文本，但通常需要大量步骤（例如 2000 步）才能达到高质量。流匹配是一种替代生成框架，学习直线轨迹，从而能用更少的步骤生成。FlowLM 通过将预训练的扩散语言模型转换为流匹配模型，桥接了这两种方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/diffusion-language-model">Diffusion language model</a></li>

</ul>
</details>

**标签**: `#flow matching`, `#diffusion models`, `#language modeling`, `#few-step generation`, `#fine-tuning`

---

<a id="item-25"></a>
## [ProxyCoT：通过代理思维链提升长上下文推理](https://arxiv.org/abs/2605.20201) ⭐️ 8.0/10

研究人员提出 ProxyCoT 训练框架，通过强化学习和监督微调，将思维链推理能力从短代理上下文迁移到完整长上下文中，显著提升了大语言模型的长上下文推理性能。 这解决了长上下文大语言模型的一个关键局限——尽管支持数百万 token，但在复杂推理任务上表现不佳——有望使 LLM 在文档分析、多轮对话等任务中更可靠。 ProxyCoT 首先通过强化学习或教师蒸馏在代理上下文中生成高质量思维链轨迹，然后通过监督微调将其锚定到完整上下文中，在降低计算成本的同时持续优于基线。

rss · arXiv - NLP · May 21, 04:00

**背景**: 像 GPT-4 这样的大语言模型可以处理非常长的输入（多达数百万 token），但在需要在整个上下文中进行复杂推理的任务上表现不佳。思维链（CoT）提示帮助模型逐步推理，但为长上下文生成 CoT 计算成本高且往往效果不佳。ProxyCoT 利用了一个洞察：许多长上下文任务只需使用相关子集（代理上下文）即可解决，并将从短上下文学到的推理迁移到完整上下文。

**标签**: `#long-context reasoning`, `#chain-of-thought`, `#large language models`, `#training framework`, `#NLP`

---

<a id="item-26"></a>
## [Artifact-Bench：评估多模态大模型对 AI 视频伪影的检测能力](https://arxiv.org/abs/2605.18984) ⭐️ 8.0/10

研究人员推出了 Artifact-Bench，这是一个全面基准测试，用于评估多模态大语言模型（MLLMs）在检测和评估 AI 生成视频中伪影的能力，涵盖逼真、动画和 CG 风格领域。 该基准填补了评估 MLLMs 对 AI 生成视频中细粒度伪影感知能力的关键空白，这对于提升视频生成质量和确保 AI 安全至关重要。 Artifact-Bench 定义了三个互补任务：真实与 AI 生成视频分类、成对真实感比较和细粒度伪影识别，并对 19 个主流 MLLMs 进行了测试，结果显示许多模型性能接近随机，存在显著局限性。

rss · arXiv - Computer Vision · May 21, 04:00

**背景**: 最近的视频生成模型能产生高度逼真的输出，但常包含时间不一致和结构扭曲等伪影。多模态大语言模型（MLLMs）具有强大的视觉理解能力，但此前缺乏对其检测此类伪影能力的系统评估。现有基准缺乏针对逼真内容之外多种视频领域的分类体系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.immersivecomputinglab.org/publication/geneva/">A Dataset of Human Annotations for Generative Text to Video Artifacts</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3706598.3713962">Characterizing Photorealism and Artifacts in Diffusion Model ...</a></li>
<li><a href="https://openaccess.thecvf.com/content/ICCV2025W/APAI/papers/Sharma_Explainable_AI-Generated_Image_Forensics_A_Low-Resolution_Perspective_with_Novel_Artifact_ICCVW_2025_paper.pdf">[PDF] Explainable AI-Generated Image Forensics: A Low-Resolution ...</a></li>

</ul>
</details>

**标签**: `#AI-generated video`, `#benchmark`, `#multimodal LLM`, `#artifact detection`, `#video generation`

---

<a id="item-27"></a>
## [EgoTraj：用于人体轨迹预测的自我中心多模态数据集](https://arxiv.org/abs/2605.19004) ⭐️ 8.0/10

研究人员发布了 EgoTraj，这是一个用于人体轨迹预测的新型自我中心多模态数据集，包含 75 段使用 Meta Quest Pro 录制的真实城市导航序列，包括同步的 RGB 视频、头部姿态、眼动注视和场景标注。 该数据集通过提供真实世界的多模态数据，填补了自我中心轨迹预测的关键空白，对于推动人形机器人、可穿戴传感和辅助导航系统的发展至关重要。 EgoTraj 具有跨多样城市路线的长时程、自导式导航，参与者多样性广泛，并包含对最先进方法的基准测试以及关于注视、场景和运动线索的消融研究。

rss · arXiv - Computer Vision · May 21, 04:00

**背景**: 自我中心轨迹预测旨在从个人视角预测其未来路径，这对增强现实和辅助机器人等应用至关重要。现有数据集通常缺乏带有同步传感器的真实世界多模态数据，限制了该领域的进展。

**标签**: `#egocentric trajectory`, `#multimodal dataset`, `#humanoid robotics`, `#assistive navigation`, `#computer vision`

---

<a id="item-28"></a>
## [多头注意力作为集成核回归](https://arxiv.org/abs/2605.20271) ⭐️ 8.0/10

本文提供了一个严格的统计理论，证明 Transformer 中的多头注意力等价于一组 Nadaraya-Watson 核回归估计器的集成，并引入了头多样性指数（HDI）来衡量头之间的去相关性。 这项工作首次从理论上解释了注意力头为何会特化以及方差减少如何依赖于头去相关性，可能指导更高效 Transformer 架构的设计。 作者推导了多头注意力的偏差-方差-协方差分解，并表明正交投影子空间能最大程度减少方差。他们还解决了在固定总维度预算下的最优头维度分配问题，得出了新的缩放定律。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: Nadaraya-Watson 估计器是一种非参数核回归方法，用于估计随机变量的条件期望。在 Transformer 中，单头 softmax 注意力已被证明在代数上等价于 Nadaraya-Watson 估计器。本文将这种等价性扩展到多头注意力，将每个头视为在学习的子空间中的独立核回归估计器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nadaraya-Watson_estimator">Nadaraya-Watson estimator</a></li>

</ul>
</details>

**标签**: `#attention mechanisms`, `#transformers`, `#statistical learning theory`, `#variance reduction`, `#kernel regression`

---

<a id="item-29"></a>
## [潜高斯模型的拉普拉斯近似修正](https://arxiv.org/abs/2605.20345) ⭐️ 8.0/10

本文提出了一种重要性采样方案，用于修正潜高斯模型中贝叶斯推断的积分拉普拉斯近似误差。 潜高斯模型广泛应用于空间统计、高斯过程和混合模型，该修正提高了后验精度，对这些领域的从业者具有重要影响。 该方法将重要性采样与伪边缘化、拟蒙特卡洛和随机拟蒙特卡洛相结合，并在自动微分框架中实现，以支持超参数推断的哈密顿蒙特卡洛方法。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: 潜高斯模型（LGM）是潜变量服从高斯先验的贝叶斯层次模型。对于非高斯似然，精确边缘化难以处理，因此使用积分拉普拉斯近似（ILA）等近似方法，但 ILA 可能引入显著误差。本研究利用重要性采样修正这些误差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Latent_Gaussian_model">Latent Gaussian model</a></li>
<li><a href="https://grokipedia.com/page/integrated_nested_laplace_approximations">Integrated nested Laplace approximations</a></li>

</ul>
</details>

**标签**: `#Bayesian inference`, `#latent Gaussian models`, `#importance sampling`, `#Laplace approximation`, `#Monte Carlo methods`

---

<a id="item-30"></a>
## [矛盾图确定 VC 维数](https://arxiv.org/abs/2605.20434) ⭐️ 8.0/10

一篇新论文证明，与二元概念类相关的矛盾图序列决定了其 VC 维数，解决了 Alon 等人于 2024 年提出的一个开放问题。 这一结果为学习理论中的基本概念 VC 维提供了新的图论刻画，可能为分析概念类的复杂性带来新工具。 m 阶矛盾图 G_m(H)的顶点表示长度为 m 的可实现标记序列，边连接那些对某个公共域点赋予相反标签的序列。论文表明，仅凭 G_m(H)即可确定 VCdim(H) ≥ m 是否成立。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: VC 维衡量二元概念类打散点的能力，是 PAC 学习理论的核心概念。矛盾图由 Alon 等人引入，用于捕捉标记序列之间的成对不一致性。该工作将这两个概念联系起来。

**标签**: `#VC dimension`, `#learning theory`, `#contradiction graphs`, `#combinatorial geometry`, `#binary concept classes`

---

<a id="item-31"></a>
## [通过最优传输分析迁移学习的样本复杂度](https://arxiv.org/abs/2605.20545) ⭐️ 8.0/10

本文利用最优传输框架从理论上证明，在高维情况下迁移学习比直接学习具有更好的样本效率。 该结果为迁移学习在大语言模型和生成式 AI 中的成功提供了严格的理论支持，尤其在目标任务数据稀缺时。 当数据维度 d > 3 时，迁移学习的样本复杂度为 O(m^{-(α+1)/d})，而直接学习为 O(m^{-p/d})，其中 α 和 p 是平滑度参数。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: 迁移学习利用源任务的知识来改进在数据有限的目标任务上的学习。样本复杂度衡量达到给定性能所需的训练样本数量。最优传输提供了一种比较概率分布的几何方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Optimal_Transport_in_Machine_Learning">Optimal Transport in Machine Learning</a></li>

</ul>
</details>

**标签**: `#transfer learning`, `#sample complexity`, `#optimal transport`, `#theoretical machine learning`

---

<a id="item-32"></a>
## [GAME：一种处理重叠子组矩阵补全的凸方法](https://arxiv.org/abs/2605.20559) ⭐️ 8.0/10

研究人员提出了组感知矩阵估计（GAME），这是一种用于处理重叠子组低秩矩阵补全的凸估计器，通过重叠核范数惩罚在组间共享信息同时保留局部结构。 该方法填补了异质矩阵补全中的一个关键空白，在推荐系统和神经科学等数据自然属于多个重叠组的应用中，提高了重构精度和潜在子空间保真度。 GAME 提供了重构误差和子组特定子空间恢复的有限样本保证，实验表明它在结构化缺失模式下最为有效，优于全局低秩和侧信息基线方法。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: 矩阵补全旨在填充部分观测矩阵中的缺失条目，通常假设低秩结构。标准方法假设单一的全局潜在空间，当数据行属于多个具有不同模式的重叠子组（例如推荐系统中不同人口统计和年龄组的用户）时，这种方法可能失效。

**标签**: `#matrix completion`, `#low-rank estimation`, `#convex optimization`, `#subgroup recovery`, `#machine learning`

---

<a id="item-33"></a>
## [基于梯度相似性的新型可计算模型复杂度度量](https://arxiv.org/abs/2605.21167) ⭐️ 8.0/10

提出了一种基于模型梯度在输入间相似性的新复杂度度量，该度量在数学上严谨且计算可行。它被证明可以推广多种现有的模型特定复杂度度量，并为双重下降现象提供了新见解。 该度量提供了一种统一且原则性的方法来评估不同模型家族的复杂度，有望改进模型选择、解释以及对泛化能力的理解。它还揭示了双重下降现象，这是现代机器学习中的一个关键谜题。 该度量适用于任何参数化模型以及基于核的非参数化模型。它推广了多项式次数、核长度尺度、邻居数量、分裂次数和树数量等度量，并应用于随机傅里叶特征、随机森林、神经网络和梯度提升。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: 模型复杂度度量对于理解泛化和模型选择至关重要，但许多现有度量要么基于启发式假设，要么计算成本高昂。双重下降是指随着模型复杂度增加，测试误差先下降、再上升、再下降的现象，挑战了传统的偏差-方差权衡观点。随机傅里叶特征是一种使用随机投影近似核方法的技术，可实现可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Random_Fourier_feature">Random Fourier feature</a></li>

</ul>
</details>

**标签**: `#model complexity`, `#machine learning`, `#theory`, `#double descent`

---

<a id="item-34"></a>
## [CLAIR：一种感知污染的联邦 LoRA 微调框架](https://arxiv.org/abs/2605.21217) ⭐️ 8.0/10

研究人员提出了 CLAIR，这是一种感知污染的联邦 LoRA 微调框架，通过低秩加块稀疏分解来恢复共享子空间并检测被污染的客户端。 这解决了在协作微调大型语言模型时保持参数效率和抵御恶意客户端的关键挑战，对于隐私保护和去中心化 AI 应用具有重要意义。 CLAIR 在无噪声情况下提供了共享 LoRA 子空间精确恢复的理论保证，并在估计误差下实现了稳定恢复；在文本复制任务上的实验表明，它能准确检测污染并提升良性客户端的性能。

rss · arXiv - Data Science & Statistics · May 21, 04:00

**背景**: LoRA（低秩适应）是一种参数高效的微调方法，仅更新低秩矩阵而非完整模型权重。联邦学习允许多个客户端在不共享原始数据的情况下协作训练模型。然而，当客户端数据异构或存在恶意（被污染）客户端时，使用 LoRA 进行联邦微调面临挑战。

**标签**: `#federated learning`, `#LoRA`, `#LLM fine-tuning`, `#robustness`, `#parameter-efficient`

---

<a id="item-35"></a>
## [Anthropic 的 Code with Claude 活动展示 AI 编程未来](https://www.technologyreview.com/2026/05/21/1137735/anthropics-code-with-claude-showed-off-codings-future-whether-you-like-it-or-not/) ⭐️ 8.0/10

Anthropic 于 2026 年 5 月 19 日在伦敦举办了为期两天的 Code with Claude 活动，展示了使用其 Claude 模型进行 AI 辅助软件开发。 该活动凸显了 AI 与软件工程的加速融合，标志着代码编写和审查方式的转变，可能重塑开发者角色和生产力。 该活动与 Google I/O 同期举行，但 Anthropic 员工表示纯属巧合。开发者展示了完全由 AI 编写的拉取请求，引发了兴奋与担忧。

rss · MIT Technology Review · May 21, 14:30

**背景**: 像 GitHub Copilot 和 Claude 这样的 AI 辅助编程工具已获得关注，使开发者能够通过自然语言提示生成代码。Anthropic 的 Claude 是一个大型语言模型，与 OpenAI 的 GPT-4 和 Google 的 Gemini 竞争。

**标签**: `#AI-assisted coding`, `#Anthropic`, `#software development`, `#Claude`

---

<a id="item-36"></a>
## [研究人员起诉特朗普政府，事关在线安全](https://www.technologyreview.com/2026/05/21/1137632/lawsuit-trump-administration-online-safety-coalition-for-independent-technology-research/) ⭐️ 8.0/10

一群技术研究人员对特朗普政府提起诉讼，挑战其针对在线安全研究的行动。该案上周首次出庭，可能产生全球影响。 这起诉讼可能为在线安全研究和言论自由的未来树立先例，影响全球研究人员如何研究仇恨言论、骚扰和虚假信息。其结果可能影响全球科技政策和学术自由。 该诉讼由独立技术研究联盟提起，代表那些研究对抗在线危害而受到政府针对的研究人员。案件处于早期阶段，上周首次出庭。

rss · MIT Technology Review · May 21, 09:00

**背景**: 自重返白宫以来，特朗普政府一直针对研究在线仇恨言论、骚扰、宣传和虚假信息的研究人员。这些行动引发了对学术自由和独立开展在线安全研究能力的担忧。该诉讼旨在保护研究人员不受政府干预地研究和对抗在线危害的权利。

**标签**: `#online safety`, `#free speech`, `#tech policy`, `#lawsuit`, `#Trump administration`

---

<a id="item-37"></a>
## [PerturbFate 工具揭示癌症突变的隐藏弱点](https://www.sciencedaily.com/releases/2026/05/260520093726.htm) ⭐️ 8.0/10

科学家开发了一种名为 PerturbFate 的新工具，该工具追踪基因突变如何随时间重塑细胞，从而识别突变通路汇聚的隐藏控制枢纽。 这种方法通过靶向控制枢纽而非单个缺陷基因，可能彻底改变对癌症和阿尔茨海默病等具有大量基因突变的疾病的治疗。 PerturbFate 分析突变随时间推移的动态效应，而非静态快照，从而精确定位可用药物靶向的汇聚点。

rss · ScienceDaily Health · May 21, 11:52

**背景**: 许多疾病如癌症涉及数百种不同的基因突变，使得针对每种突变单独开发治疗变得困难。PerturbFate 通过识别多个突变共同影响的共同通路或“控制枢纽”，提供单一治疗靶点来解决这一问题。

**标签**: `#cancer`, `#genetic mutations`, `#PerturbFate`, `#Alzheimer's`, `#systems biology`

---