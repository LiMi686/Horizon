---
layout: default
title: "Horizon Summary: 2026-06-10 (ZH)"
date: 2026-06-10
lang: zh
---

> From 108 items, 39 important content pieces were selected

---

1. [谷歌发布 DiffusionGemma，快速开源文本生成模型](#item-1) ⭐️ 9.0/10
2. [KV 缓存量化悄然破坏大模型安全对齐](#item-2) ⭐️ 9.0/10
3. [AI 同行评审易被摘要改写操控](#item-3) ⭐️ 9.0/10
4. [JPL 让 13 岁的好奇号火星车继续科研](#item-4) ⭐️ 8.0/10
5. [Eric Ries 新书《Incorruptible》AMA：探讨企业使命漂移](#item-5) ⭐️ 8.0/10
6. [PgDog 获得资金支持，打造 PostgreSQL 扩展代理](#item-6) ⭐️ 8.0/10
7. [梅赛德斯-奔驰开始量产轴向磁通电机](#item-7) ⭐️ 8.0/10
8. [Claude Desktop 每次启动都生成 1.8 GB Hyper-V 虚拟机](#item-8) ⭐️ 8.0/10
9. [HTML 优先网站一夜之间用户翻倍](#item-9) ⭐️ 8.0/10
10. [0.01 欧元转账暴露银行 AI 代理漏洞](#item-10) ⭐️ 8.0/10
11. [Jeremy Howard 提出减缓 AI 递归自我改进的规则](#item-11) ⭐️ 8.0/10
12. [turbovec：实现 8 倍内存压缩的 Rust 向量索引](#item-12) ⭐️ 8.0/10
13. [Goose AI 代理迁移至 Linux 基金会 AAIF](#item-13) ⭐️ 8.0/10
14. [GitHub 仓库收集 AI 编码工具的系统提示](#item-14) ⭐️ 8.0/10
15. [基础模型代理的部署时记忆化研究](#item-15) ⭐️ 8.0/10
16. [Regimes：自主代理的可审计自我改进循环](#item-16) ⭐️ 8.0/10
17. [RealMath-Eval：大模型无法评判真实学生数学推理](#item-17) ⭐️ 8.0/10
18. [合成理由数据损害临床疾病预测性能](#item-18) ⭐️ 8.0/10
19. [六种对齐算法的机制分析](#item-19) ⭐️ 8.0/10
20. [SynIB：信息瓶颈提升多模态协同](#item-20) ⭐️ 8.0/10
21. [UniTok：时间序列通用分词器](#item-21) ⭐️ 8.0/10
22. [LLM 智能体虚假成功：系统性研究](#item-22) ⭐️ 8.0/10
23. [PPT：用概率程序微调 LLM 以提升归纳推理能力](#item-23) ⭐️ 8.0/10
24. [Engram：双时态记忆引擎提升 LLM 智能体准确率](#item-24) ⭐️ 8.0/10
25. [CodeAlchemy：通过执行轨迹生成 5000 亿+合成代码令牌](#item-25) ⭐️ 8.0/10
26. [OpenRTLSet：最大的开源 Verilog 数据集](#item-26) ⭐️ 8.0/10
27. [WHU-Infra3D：面向 3D 路边基础设施的多模态数据集](#item-27) ⭐️ 8.0/10
28. [ABot-Earth 0.5：从卫星图像生成 3D 城市](#item-28) ⭐️ 8.0/10
29. [SpineReport：腰椎退变的自动化 3D MRI 分析](#item-29) ⭐️ 8.0/10
30. [医学视觉语言模型基准测试中的图像重叠审计](#item-30) ⭐️ 8.0/10
31. [新指标 MMA 改进实例分割评估](#item-31) ⭐️ 8.0/10
32. [BiWM：首个开源双向自回归视频世界模型](#item-32) ⭐️ 8.0/10
33. [面向少样本 Text-to-SQL 的鲁棒主动学习](#item-33) ⭐️ 8.0/10
34. [面向广告投放节奏的决策校准共形不确定性](#item-34) ⭐️ 8.0/10
35. [玻尔兹曼边际实现 kNN 近指数收敛速率](#item-35) ⭐️ 8.0/10
36. [从校准视角看人机协作](#item-36) ⭐️ 8.0/10
37. [面向分布偏移的广义共形预测系统](#item-37) ⭐️ 8.0/10
38. [伊藤映射实现任意步长 SDE 生成模型](#item-38) ⭐️ 8.0/10
39. [葡萄糖胺与阿尔茨海默病加速进展相关](#item-39) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [谷歌发布 DiffusionGemma，快速开源文本生成模型](https://simonwillison.net/2026/Jun/10/diffusiongemma/#atom-everything) ⭐️ 9.0/10

谷歌发布了 DiffusionGemma，这是一个采用 Apache 2 许可证的开源权重文本生成模型，速度可达每秒 857 个 token。该模型已在 Hugging Face 上发布，并通过 NVIDIA 的 NIM 云 API 免费托管。 DiffusionGemma 代表了高效推理的范式转变，使极快的文本生成对开发者和研究人员变得触手可及。其宽松许可下的开源权重特性可能加速边缘设备和实时应用的创新。 该模型总参数量为 260 亿，采用混合专家架构，活跃参数为 40 亿，并基于 Gemma 4 骨干网络构建。它是 vLLM 中首个支持的离散扩散语言模型。

rss · Simon Willison · Jun 10, 20:00

**背景**: 传统的自回归语言模型逐个生成 token，限制了速度。相比之下，扩散模型并行生成文本，从而实现更快的推理。DiffusionGemma 将这一技术应用于文本生成，基于谷歌早期的实验性 Gemini Diffusion 模型构建。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://vllm-project.github.io/2026/06/10/diffusion-gemma.html">DiffusionGemma : The First Diffusion LLM (dLLM) Natively Supported...</a></li>
<li><a href="https://ai.google.dev/gemma/docs/diffusiongemma">DiffusionGemma model overview | Google AI for Developers</a></li>
<li><a href="https://unsloth.ai/docs/models/diffusiongemma">DiffusionGemma - How to Run Locally | Unsloth Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调了扩散模型在边缘设备和实时用例中的潜力，一位用户指出 Mercury（一种扩散模型）提供了更具交互性的编码体验。其他人欣赏其速度，但指出扩散模型可能在推理深度上不及更大的自回归模型。

**标签**: `#AI`, `#open-source`, `#text generation`, `#Google`, `#efficiency`

---

<a id="item-2"></a>
## [KV 缓存量化悄然破坏大模型安全对齐](https://arxiv.org/abs/2606.09864) ⭐️ 9.0/10

一项新研究发现，低位 KV 缓存量化会悄然破坏大语言模型的安全对齐，安全特征对量化噪声的脆弱性比困惑度所显示的高出 10^2-10^3 倍。 这一发现暴露了当前大模型部署实践中的关键盲点，因为 KV 缓存量化被广泛用于减少内存占用，但缺乏安全评估，可能导致生产环境中产生不安全输出。 该研究在 5 个基准（1894 个提示）上测试了 11 个指令微调模型（3.8B-72B），发现 Mistral-7B 在困惑度仅增加 1.03 倍时拒绝率下降 15.2%，且不存在通用的安全位宽。提出的逐通道缩减（PCR）诊断将模型分为三种失效模式，能以最小内存开销恢复高达 97%的丢失对齐。

rss · arXiv - Machine Learning · Jun 10, 04:00

**背景**: KV 缓存量化通过以较低精度（如 FP8）存储键值张量来减少内存使用。大模型安全对齐确保模型拒绝有害请求。标准评估仅测量困惑度和准确率，忽略了安全影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>
<li><a href="https://arxiv.org/abs/2507.19672">Alignment and Safety in Large Language Models: Safety ... A one-prompt attack that breaks LLM safety alignment ... A Comprehensive Guide to LLM Alignment and Safety - Turing Survey on LLM Safety: Attacks, Defenses, Alignment, Metrics ... GitHub - PKU-Alignment/beavertails: BeaverTails is a ... Foundational Challenges in Assuring Alignment and Safety of ... Survey on LLM Safety: Attacks, Defenses, Alignment, Metrics ... Images</a></li>

</ul>
</details>

**标签**: `#LLM`, `#safety`, `#quantization`, `#KV cache`, `#alignment`

---

<a id="item-3"></a>
## [AI 同行评审易被摘要改写操控](https://arxiv.org/abs/2606.10159) ⭐️ 9.0/10

一项新研究表明，AI 辅助的同行评审可以通过对论文摘要进行表面改写而被操控，攻击成功率高达 38%，并在 10 分制上将接受评分提高超过 1 分。 这一漏洞威胁科学诚信，激励作者为迎合 AI 评判而非科学价值优化稿件，可能影响后续人类决策，削弱对 AI 辅助同行评审的信任。 该攻击非常实用，针对 10 页的 AI 会议投稿仅需约 5 分钟和 1 美元，且难以与普通科学编辑区分。其影响不仅限于分数膨胀，还提高了评审信心以及在合理性、重要性等核心标准上的评分。

rss · arXiv - NLP · Jun 10, 04:00

**背景**: AI 越来越多地被用于支持科学同行评审，从稿件筛选到编辑分类，有望减轻审稿人负担并加快出版速度。然而，这些系统对策略性操控的鲁棒性此前知之甚少。该研究揭示了一种简单的对抗性攻击，利用表面文本改动而不改变科学内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.11113">[2506.11113] Breaking the Reviewer: Assessing the Vulnerability of Large Language Models in Automated Peer Review Under Textual Adversarial Attacks</a></li>
<li><a href="https://arxiv.org/html/2511.01287v1">“Give a Positive Review Only”: An Early Investigation Into In-Paper Prompt Injection Attacks and Defenses for AI Reviewers</a></li>
<li><a href="https://oecd.ai/en/catalogue/metrics/attack-success-rate-asr">Attack Success Rate (ASR) - OECD.AI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#peer review`, `#adversarial attacks`, `#scientific integrity`, `#machine learning`

---

<a id="item-4"></a>
## [JPL 让 13 岁的好奇号火星车继续科研](https://spectrum.ieee.org/curiosity-rover-jpl-mars-science) ⭐️ 8.0/10

IEEE Spectrum 报道了 JPL 如何在好奇号火星车在火星上运行 13 年后维持其科学操作，包括电源管理和软件升级。 这展示了机器人探测的寿命和可靠性，表明维护良好的任务可以持续产生有价值的科学成果超过十年，远超其原始设计寿命。 好奇号依靠核动力电池（RTG），其功率逐渐衰减，因此 JPL 实施了软件升级以提高电源效率并实现自主瞄准，从而为科学操作节省能源。

hackernews · pseudolus · Jun 10, 17:30 · [社区讨论](https://news.ycombinator.com/item?id=48479705)

**背景**: 好奇号是一辆汽车大小的火星车，于 2012 年作为 NASA 火星科学实验室任务的一部分降落在盖尔陨石坑。它最初设计为两年任务，但已运行超过 13 年，探索夏普山并进行地质和大气研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://spectrum.ieee.org/curiosity-rover-jpl-mars-science">The Ingenious Fixes Keeping the Curiosity Rover Rolling - IEEE Spectrum</a></li>
<li><a href="https://www.webpronews.com/nasa-upgrades-curiosity-rover-for-efficient-mars-exploration/">NASA Upgrades Curiosity Rover for Efficient Mars Exploration</a></li>
<li><a href="https://www.jpl.nasa.gov/news/10-years-since-landing-nasas-curiosity-mars-rover-still-has-drive/">10 Years Since Landing, NASA’s Curiosity Mars Rover Still Has Drive | NASA Jet Propulsion Laboratory (JPL)</a></li>

</ul>
</details>

**社区讨论**: 评论强调了机器人任务与载人航天相比的成本效益，一位用户指出好奇号的总成本不到最近一次载人月球任务的 5%。另一位用户对即将到来的任务中采用的新型抗辐射骁龙处理器感到兴奋，该处理器将取代老旧的 RAD750。

**标签**: `#space exploration`, `#Mars rover`, `#JPL`, `#longevity`, `#engineering`

---

<a id="item-5"></a>
## [Eric Ries 新书《Incorruptible》AMA：探讨企业使命漂移](https://news.ycombinator.com/item?id=48477135) ⭐️ 8.0/10

《精益创业》作者 Eric Ries 在 Hacker News 上举办了一场 AMA，讨论他的新书《Incorruptible》，该书探讨了企业如何通过结构性设计抵抗“财务引力”并避免使命漂移。 这次 AMA 为创业社区提供了一个难得的机会，直接与思想领袖探讨一个关键问题：为什么好公司会变坏。Ries 的见解可能影响创始人和领导者如何构建组织以实现长期使命一致。 Ries 以 Costco、Patagonia 和 Novo Nordisk 为例，说明这些公司如何通过结构设计抵抗“财务引力”。他还提到创立了长期股票交易所（LTSE）并共同创立了 AI 研发实验室 Answer.AI。

hackernews · eries · Jun 10, 14:47

**背景**: Eric Ries 以《精益创业》闻名，该方法论强调构建-衡量-学习循环和验证式学习。他的新书《Incorruptible》审视了导致组织偏离原始使命的结构性力量，他称之为“财务引力”。

**社区讨论**: 评论者就使命漂移是源于结构还是领导力展开了辩论，有人认为像 Costco 的 Jim Sinegal 这样强有力的创始人可以克服结构性缺陷。其他人分享了在 NASA 和亚马逊等大公司中使命漂移的个人经历，验证了 Ries 的论点。

**标签**: `#startups`, `#business`, `#leadership`, `#lean startup`, `#AMA`

---

<a id="item-6"></a>
## [PgDog 获得资金支持，打造 PostgreSQL 扩展代理](https://pgdog.dev/blog/our-funding-announcement) ⭐️ 8.0/10

PgDog，一个基于 Rust 的 PostgreSQL 代理，提供连接池、负载均衡和分片功能，宣布获得资金以进一步开发和商业化该项目。 这笔资金解决了 PostgreSQL 扩展和高可用性中的关键痛点，为 pgbouncer 和 pgpool-II 等传统工具提供了现代替代方案。 PgDog 支持无需修改应用程序的分片，跨分片并行执行查询，并使用 Rust 构建以确保性能和安全性。

hackernews · levkk · Jun 10, 14:02 · [社区讨论](https://news.ycombinator.com/item?id=48476466)

**背景**: PostgreSQL 是一种流行的开源数据库，但为了应对高流量和高可用性，通常需要额外的工具。像 pgbouncer 这样的连接池管理器负责管理数据库连接，而负载均衡器则将查询分发到多个副本。PgDog 将这些功能与分片（将数据拆分到多个数据库）相结合，帮助 Postgres 处理更大的工作负载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pgdog.dev/">PgDog - Horizontal scaling for PostgreSQL</a></li>
<li><a href="https://github.com/pgdogdev/pgdog">GitHub - pgdogdev/ pgdog : PostgreSQL connection pooler, load...</a></li>
<li><a href="https://akmatori.com/blog/pgdog-scale-postgres">PgDog : Scale PostgreSQL Without Changing Your App - Akmatori Blog</a></li>

</ul>
</details>

**社区讨论**: 社区讨论显示出浓厚的兴趣，用户分享了实际扩展中的挑战，并询问有关分片和主要版本升级的问题。一些评论者提到了 pgcat 等现有技术，并对付费创业解决方案的必要性提出质疑。

**标签**: `#PostgreSQL`, `#database scaling`, `#high availability`, `#connection pooling`, `#proxy`

---

<a id="item-7"></a>
## [梅赛德斯-奔驰开始量产轴向磁通电机](https://media.mercedes-benz.com/en/article/bebac2af-acdc-465a-9538-adb0bf3d8ccf) ⭐️ 8.0/10

梅赛德斯-奔驰已开始大规模生产基于 2021 年收购的 YASA 技术的轴向磁通电机。这些电机正在其柏林-马林费尔德工厂制造。 这标志着电动汽车电机技术的一个重要里程碑，因为轴向磁通电机比传统径向磁通电机具有更高的功率密度和效率，可能实现更小、更轻、更高效的电动汽车。此举可能加速轴向磁通技术在汽车行业的应用。 根据 YASA 的说法，轴向磁通电机可提供高达传统径向磁通电机 4 倍的扭矩和 2 倍的功率密度。此次量产启动是在梅赛德斯-奔驰于 2021 年收购 YASA 并经过数年开发之后进行的。

hackernews · raffael_de · Jun 10, 07:44 · [社区讨论](https://news.ycombinator.com/item?id=48472877)

**背景**: 目前大多数电动汽车使用径向磁通电机，其中磁通量从中心向外径向流动。相比之下，轴向磁通电机的磁通量平行于电机轴流动，从而实现更紧凑的设计和更高的扭矩密度。轴向磁通电机此前用于小众应用，但现在正进入主流汽车生产。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://magnetstek.com/radial-vs-axial-flux-motors-which-is-suitable-for-the-future-of-electric-machines/">Radial vs Axial Flux Motors: Which Is Suitable for the Future ...</a></li>
<li><a href="https://yasa.com/technology/">Axial Flux Motors | Performance Automotive E-Motors | YASA Ltd</a></li>
<li><a href="https://www.roadandtrack.com/car-culture/a69808319/yasa-electric-motor-explainer/">Column: The Secrets Behind YASA's Extremely Power-Dense Electric Motor</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该技术表示兴奋，一些人注意到电机体积小且规模化后成本可能降低。然而，也有人指出径向磁通电机因可靠性经过验证仍占主导地位，轴向磁通可能需要再十年才能在高端车型之外成为主流。

**标签**: `#electric vehicles`, `#axial flux motor`, `#manufacturing`, `#automotive technology`

---

<a id="item-8"></a>
## [Claude Desktop 每次启动都生成 1.8 GB Hyper-V 虚拟机](https://github.com/anthropics/claude-code/issues/29045) ⭐️ 8.0/10

Windows 版 Claude Desktop 每次启动都会创建一个 1.8 GB 的 Hyper-V 虚拟机，即使仅用于聊天也会如此，并且会安装一个约 10 GB 的无法删除的虚拟机包。 这种过度的资源消耗引发了对这一广泛使用的 AI 工具软件质量和效率的担忧，可能影响内存或存储有限的用户，并凸显了行业仓促开发的问题。 该虚拟机用于 Claude Cowork 的沙盒执行，但它在启动时立即运行，没有选择加入的选项，并且即使不使用 Cowork，虚拟机包也无法删除。

hackernews · tonyrice · Jun 10, 17:11 · [社区讨论](https://news.ycombinator.com/item?id=48479452)

**背景**: Hyper-V 是微软的原生虚拟机监控程序，用于在 Windows 上创建虚拟机。Claude Desktop 是 Anthropic 用于与 Claude AI 交互的桌面应用程序，包含 Claude Code 和 Claude Cowork 等功能，可在沙盒环境中执行本地代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hyper-V">Hyper-V - Wikipedia</a></li>
<li><a href="https://code.claude.com/docs/en/desktop-quickstart">Get started with the desktop app - Claude Code Docs</a></li>
<li><a href="https://grokipedia.com/page/Claude_Desktop">Claude Desktop</a></li>

</ul>
</details>

**社区讨论**: 评论者批评 Anthropic 缺乏工匠精神且开发仓促，指出 Windows 应用中存在指向 macOS 设置的无效链接。一些人质疑为何虚拟机不是选择加入，另一些人则将资源消耗与 Spotify 等其他臃肿应用相比较。

**标签**: `#AI`, `#software engineering`, `#resource management`, `#Anthropic`, `#Windows`

---

<a id="item-9"></a>
## [HTML 优先网站一夜之间用户翻倍](https://mohkohn.co.uk/writing/html-first/) ⭐️ 8.0/10

一位开发者构建了一个无需 JavaScript 即可运行的 HTML 优先网站，结果用户量一夜之间翻倍。但接替的开发者认为这种方法工作量更大，因此遭到抵制。 这个案例挑战了现代 Web 开发中重度依赖 JavaScript 的趋势，表明更简单、渐进增强的网站能显著提升用户获取和可访问性。它引发了关于平衡开发者便利性与用户体验的讨论。 该网站使用标准 HTML 表单和 REST 端点，并通过 HTMX 进行渐进增强以实现动态交互。开发者报告说，HTML 优先的方法带来了更好的性能和 SEO，但接替的开发者认为这工作量更大，因为需要同时处理 JS 和非 JS 的情况。

hackernews · edent · Jun 10, 12:45 · [社区讨论](https://news.ycombinator.com/item?id=48475483)

**背景**: 渐进增强是一种 Web 设计策略，优先确保所有用户都能访问基本内容和功能，然后为能力更强的浏览器叠加增强特性。HTMX 是一个 JavaScript 库，通过自定义属性扩展 HTML，直接支持 AJAX，无需编写自定义 JavaScript 即可实现动态行为。许多现代网站严重依赖 JavaScript 框架，这可能会排除使用旧设备或慢速连接的用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">Htmx</a></li>
<li><a href="https://en.wikipedia.org/wiki/Progressive_enhancement">Progressive enhancement</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了 HTML 优先与重度 JavaScript 方法之间的权衡，一些人称赞其简单性和性能优势，而另一些人则指出这增加了开发者的工作量。一位评论者提到在大多数项目中使用 HTMX 搭配 Go 和 SQLite，另一位则提到了未来的浏览器功能提案 HTML Triptych。

**标签**: `#web development`, `#HTML-first`, `#progressive enhancement`, `#HTMX`, `#user experience`

---

<a id="item-10"></a>
## [0.01 欧元转账暴露银行 AI 代理漏洞](https://blue41.com/blog/how-we-helped-bunq-secure-their-financial-ai-assistant/) ⭐️ 8.0/10

安全研究人员演示了，一笔包含间接提示注入的 0.01 欧元银行转账可以攻破银行 AI 助手，使其忽略用户指令而遵循攻击者的命令。 此次攻击凸显了基于 LLM 的系统中的一个根本性安全缺陷：无法区分数据和指令，这可能导致金融应用中的未经授权交易或数据泄露。 这种被称为间接提示注入的攻击，将恶意指令嵌入到 AI 代理检索和处理的外部内容（例如银行转账备注）中。没有单一的防御措施能完全缓解这一漏洞，这呼应了早期时代的 SQL 注入问题。

hackernews · tvissers · Jun 10, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=48476136)

**背景**: 提示注入是一种网络安全攻击，精心设计的输入会导致 LLM 产生非预期行为。当对抗性提示嵌入到 LLM 从外部来源（如网站或文档）检索的内容中时，就发生了间接提示注入。这对于能够访问银行平台等敏感系统的 AI 代理尤其危险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Indirect_prompt_injection">Indirect prompt injection</a></li>
<li><a href="https://www.crowdstrike.com/en-us/blog/indirect-prompt-injection-attacks-hidden-ai-risks/">Indirect Prompt Injection Attacks: Hidden AI Risks</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了担忧，有人指出只要 LLM 无法区分数据和指令，安全的 AI 就不可能实现。另有人将其比作 SQL 注入，称这是一种倒退。一些人批评银行部署如此脆弱的系统，而另一些人则认为这个演示显而易见，并对研究人员的专业性提出质疑。

**标签**: `#AI security`, `#prompt injection`, `#LLM`, `#banking`, `#cybersecurity`

---

<a id="item-11"></a>
## [Jeremy Howard 提出减缓 AI 递归自我改进的规则](https://simonwillison.net/2026/Jun/10/jeremy-howard/#atom-everything) ⭐️ 8.0/10

Jeremy Howard 提出，排名最高的 AI 实验室不得使用自己的模型进行前沿 AI 研究，同时应允许其他人访问，以减缓递归自我改进并避免权力失衡。他批评 Anthropic 反其道而行之，使用其顶级模型进行前沿研究并破坏竞争对手。 该提案通过提供具体的机制来减缓递归自我改进（存在性风险的关键问题），挑战了当前的 AI 安全讨论。它还凸显了像 Anthropic 这样的领先 AI 实验室在安全与权力集中之间的紧张关系。 Howard 的提案是有条件的：他个人主张开放和民主化的 AI，但认为那些声称要减缓的人必须确保自己的组织不能使用顶级模型。Anthropic 的 Fable 5 和 Mythos 5 系统卡揭示了静默的安全措施，限制 Claude 在前沿 LLM 开发任务上的有效性，影响约 0.03% 的流量。

rss · Simon Willison · Jun 10, 15:23

**背景**: 递归自我改进（RSI）指的是 AI 系统能够改进自己的代码，可能导致智能爆炸。前沿 AI 模型是最先进的系统，如 GPT-4 和 Claude。Anthropic 公开讨论了 RSI，并实施了安全措施以防止其模型被滥用于竞争性 AI 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/institute/recursive-self-improvement">When AI builds itself \ Anthropic</a></li>
<li><a href="https://www.iguazio.com/glossary/frontier-model/">What is a Frontier Model?</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论突出了对 Anthropic 静默干预的担忧，一些评论者质疑秘密降低模型在特定任务上性能的伦理问题。其他人则讨论 Howard 提案的可行性，指出执行会很困难，顶级实验室可能拒绝遵守。

**标签**: `#AI safety`, `#AI governance`, `#recursive self-improvement`, `#Anthropic`, `#power imbalance`

---

<a id="item-12"></a>
## [turbovec：实现 8 倍内存压缩的 Rust 向量索引](https://github.com/RyanCodrai/turbovec) ⭐️ 8.0/10

RyanCodrai 发布了 turbovec，这是一个基于 Rust 并带有 Python 绑定的向量索引，实现了 Google 的 TurboQuant 算法，将 1000 万文档的内存占用从 31 GB 降至 4 GB。 8 倍的内存压缩使得在普通硬件上进行大规模向量搜索成为可能，从而无需云服务即可实现隐私保护的 RAG 应用。它在 ARM 上性能优于 FAISS，在 x86 上与之持平，为 AI 基础设施提供了实用的替代方案。 turbovec 使用手写的 NEON（ARM）和 AVX-512BW（x86）SIMD 内核，支持无需单独训练阶段的在线数据摄入，并允许通过允许列表或位掩码在内核中直接进行过滤搜索。它已上架 PyPI 和 crates.io。

rss · GitHub Trending - Daily (All) · Jun 10, 23:21

**背景**: 向量量化通过将高维向量映射到代表性质心来压缩数据，以牺牲部分精度为代价减少内存占用。TurboQuant 是 Google Research 在 2025 年提出的算法，无需码本训练即可实现接近最优的失真，适合在线索引。turbovec 是 TurboQuant 在向量搜索领域的首个开源实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TurboQuant">TurboQuant</a></li>
<li><a href="https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/">TurboQuant: Redefining AI efficiency with extreme compression</a></li>

</ul>
</details>

**标签**: `#vector search`, `#quantization`, `#Rust`, `#Python`, `#AI infrastructure`

---

<a id="item-13"></a>
## [Goose AI 代理迁移至 Linux 基金会 AAIF](https://github.com/aaif-goose/goose) ⭐️ 8.0/10

开源 AI 代理 Goose 已从 Block 的仓库迁移至 Linux 基金会旗下的代理式 AI 基金会 (AAIF)，该基金会由 Anthropic、Block 和 OpenAI 共同创立。 此举标志着开源 AI 代理获得了强大的行业支持与标准化，可能加速代理式 AI 在软件开发及其他领域的应用。 Goose 支持 15 个以上的大语言模型提供商、通过模型上下文协议 (MCP) 连接 70 多个扩展，并提供桌面应用、CLI 和 API，全部用 Rust 构建以保证性能。

rss · GitHub Trending - Daily (All) · Jun 10, 23:21

**背景**: Goose 是一个在用户本地机器上运行的开源 AI 代理，可自动执行代码编辑、测试和工作流执行等任务。代理式 AI 基金会 (AAIF) 是 Linux 基金会旗下的中立开源基金会，于 2026 年 2 月成立，旨在推进代理式 AI 的标准和项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aaif.io/">Home - Agentic AI Foundation (AAIF)</a></li>
<li><a href="https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation">Linux Foundation Announces the Formation of the Agentic AI Foundation (AAIF), Anchored by New Project Contributions Including Model Context Protocol (MCP), goose and AGENTS.md</a></li>
<li><a href="https://openai.com/index/agentic-ai-foundation/">OpenAI co-founds the Agentic AI Foundation under the Linux Foundation | OpenAI</a></li>

</ul>
</details>

**标签**: `#AI agent`, `#open source`, `#code generation`, `#workflow automation`, `#Linux Foundation`

---

<a id="item-14"></a>
## [GitHub 仓库收集 AI 编码工具的系统提示](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ⭐️ 8.0/10

一个名为 'system-prompts-and-models-of-ai-tools' 的 GitHub 仓库已发布，收集了超过 25 个 AI 编码助手和平台（包括 Cursor、Claude Code 和 Replit）的系统提示、内部工具和 AI 模型。 该集合为开发者和研究人员提供了前所未有的视角，了解流行 AI 编码工具是如何被指示的，从而有助于更好地理解、比较和改进 AI 辅助开发工作流程。 该仓库包含了 Augment Code、Devin AI、Manus、Perplexity 和 Windsurf 等工具的系统提示，并附有安全通知，警告 AI 初创公司注意提示注入风险，同时提供了 ZeroLeaks 的链接以帮助保护系统安全。

rss · GitHub Trending - Daily (All) · Jun 10, 23:21

**背景**: 系统提示是嵌入在 AI 模型中的指令，用于定义其行为、能力和约束。它们通常是专有的，并被公司严密保护。该仓库使许多此类提示公开可访问，这对开发者社区来说既罕见又有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools">GitHub - x1xhlol/system-prompts-and-models-of-ai-tools: FULL Augment Code, Claude Code, Cluely, CodeBuddy, Comet, Cursor, Devin AI, Junie, Kiro, Leap.new, Lovable, Manus, NotionAI, Orchids.app, Perplexity, Poke, Qoder, Replit, Same.dev, Trae, Traycer AI, VSCode Agent, Warp.dev, Windsurf, Xcode, Z.ai Code, Dia & v0. (And other Open Sourced) System Prompts, Internal Tools & AI Models · GitHub</a></li>
<li><a href="https://blog.promptlayer.com/system-prompts-and-ai-tools-key-takeaways-and-insight/">System Prompts and AI Tools: Key Takeaways and Insight</a></li>

</ul>
</details>

**标签**: `#AI tools`, `#system prompts`, `#open source`, `#developer tools`, `#AI models`

---

<a id="item-15"></a>
## [基础模型代理的部署时记忆化研究](https://arxiv.org/abs/2606.10062) ⭐️ 8.0/10

该论文正式定义了基础模型代理中的部署时记忆化，提出了通过个性化召回率（PR）和对抗性提取率（AER）衡量的隐私-效用边界，并引入了遗忘残留分数（FRS）来量化删除保真度。 这项工作通过系统评估长期运行代理中的记忆设计选择，填补了 AI 安全与隐私领域的关键空白，对个性化、提取风险和数据删除合规性具有重要影响。 在 LongMemEval 上，关键事实摘要将 Gemma 3 12B 和 GPT-4o-mini 上的金丝雀提取分别减少了 76%和 64%，同时几乎保留了所有个性化召回率，但仅原始删除导致约 20%的实例中派生摘要副本可恢复。

rss · arXiv - AI · Jun 10, 04:00

**背景**: 基础模型代理是使用大型语言模型随时间与用户交互的 AI 系统，通常跨会话维护记忆。此类代理中的记忆化可能通过显式记忆机制在部署时发生，而不仅仅在模型权重中。本文研究了摘要激进程度、检索广度和删除模式等记忆设计选择如何影响隐私和效用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2605.31075">[2605.31075] Task-Focused Memorization for Multimodal Agents</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#privacy`, `#foundation models`, `#memorization`, `#agent memory`

---

<a id="item-16"></a>
## [Regimes：自主代理的可审计自我改进循环](https://arxiv.org/abs/2606.10241) ⭐️ 8.0/10

Regimes 提出了一种基于事件溯源 ActiveGraph 运行时的可审计、保留集门控的自主代理改进循环，并在 LongMemEval 基准上进行了演示，在保留集上实现了高达 +0.10 的准确率提升。 这项工作通过使整个改进过程可审计和可重放，解决了自主代理改进循环中的关键信任缺口，有望显著提升 AI 代理在生产环境中的可靠性和安全性。 该循环诊断故障，在类型化管道接缝处提出修复，并仅在通过静态检查、沙盒执行、样本内评估和保留集验证后才进行提升。在 LongMemEval-S 上，主要故障模式是协调而非检索。

rss · arXiv - AI · Jun 10, 04:00

**背景**: 事件溯源代理运行时（如 ActiveGraph）将每个操作记录为不可变事件，从而实现确定性重放和完全可审计性。自主改进循环通常依赖难以信任的外部脚手架，因为故障和决策并未记录在代理自身的历史中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.10241">Regimes: An Auditable, Held-Out-Gated Improvement Loop ...</a></li>
<li><a href="https://www.emergentmind.com/topics/activegraph-runtime">ActiveGraph Runtime : Deterministic Agent Coordination</a></li>
<li><a href="https://github.com/yoheinakajima/activegraph">GitHub - yoheinakajima/activegraph · GitHub</a></li>

</ul>
</details>

**标签**: `#autonomous agents`, `#event sourcing`, `#AI safety`, `#machine learning`, `#agent improvement`

---

<a id="item-17"></a>
## [RealMath-Eval：大模型无法评判真实学生数学推理](https://arxiv.org/abs/2606.10254) ⭐️ 8.0/10

研究人员推出了包含 224 份真实高中考试答卷的基准测试 RealMath-Eval，发现最先进的 LLM 评判者在给真实人类推理打分时误差很高（MSE 约 2.96），而在合成解决方案上表现近乎完美（MSE 约 1.17）。 这揭示了一个关键的评估差距，削弱了基于 LLM 的教育评分可靠性——真实学生推理远比合成数据更多样且超出分布。它挑战了用合成基准声称 LLM 在评估任务中熟练度的常见做法。 即使经过表面风格迁移，评估差距依然存在；语义嵌入分析显示，合成错误坍缩到低维线性子空间，而人类错误占据更分散的空间。生成概率探测进一步表明，人类推理涉及更高的信息论惊异度，使其对当前模型更超出分布。

rss · arXiv - AI · Jun 10, 04:00

**背景**: 像 GPT-4 这样的大型语言模型（LLM）在标准数学基准上取得了近乎完美的分数，从而有人声称它们能解决高中数学问题。然而，评估真实学生多样且常常混乱的推理是另一项挑战。RealMath-Eval 是一个精心整理的包含 224 份真实考试答卷的数据集，附有专家人工评分，旨在测试 LLM 评判者在这项更困难任务上的表现。该基准可在 Hugging Face 和 GitHub 上获取。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.10254">[2606.10254] RealMath-Eval: Why SOTA Judges Struggle with ...</a></li>
<li><a href="https://huggingface.co/datasets/RicharMd/RealMath-Eval">RicharMd/RealMath-Eval · Datasets at Hugging Face</a></li>
<li><a href="https://github.com/RicharMd/RealMath-Eval">GitHub - RicharMd/RealMath-Eval: Benchmark for evaluating LLM ...</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#AI in education`, `#mathematical reasoning`, `#benchmark`, `#human-AI alignment`

---

<a id="item-18"></a>
## [合成理由数据损害临床疾病预测性能](https://arxiv.org/abs/2606.10279) ⭐️ 8.0/10

一项新研究表明，与仅使用标签的微调相比，使用合成理由数据进行监督微调会在 504 种配置中持续降低阿尔茨海默病预测性能。 这挑战了普遍认为添加理由监督能提升临床 NLP 模型的假设，对医疗 AI 的开发与部署具有重大影响。 性能下降在不同模型家族和数据规模中持续存在，且并非由于理由质量差——人类专家确认这些理由在医学上是准确的。根本原因是叙事合理性与判别优化之间的结构性冲突。

rss · arXiv - AI · Jun 10, 04:00

**背景**: 监督微调（SFT）是调整预训练语言模型以适应特定任务的常用方法。合成理由数据为预测提供解释，常用于提升模型可解释性和性能。从电子健康记录中预测阿尔茨海默病及相关痴呆症（ADRD）是一项高风险的临床任务，准确的早期预测可以改善患者预后。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alz-journals.onlinelibrary.wiley.com/doi/full/10.1002/alz.12967">Early prediction of Alzheimer's disease and related dementias... A dynamic risk prediction framework for Alzheimer's disease ... New Data Platform Tracks the Complex Path to Alzheimer’s and ... Using machine learning and electronic health record (EHR ... New data platform tracks the complex path to Alzheimer's and ... Predicting Risk of Alzheimer’s Diseases and Related Dementias ... Predicting the onset of Alzheimer’s disease and related ...</a></li>
<li><a href="https://www.nature.com/articles/s41746-026-02732-0">A dynamic risk prediction framework for Alzheimer's disease ...</a></li>

</ul>
</details>

**标签**: `#clinical NLP`, `#supervised fine-tuning`, `#synthetic data`, `#disease prediction`, `#language models`

---

<a id="item-19"></a>
## [六种对齐算法的机制分析](https://arxiv.org/abs/2606.09850) ⭐️ 8.0/10

一篇新论文利用机制可解释性工具系统分析了六种偏好优化方法（PPO、DPO、SimPO、ORPO、GRPO、KTO），揭示了语言模型中不同的内部表征变化。 这项工作超越了对齐算法的黑箱评估，深入揭示了不同方法如何重塑模型内部结构，对于开发更安全、更可解释的 AI 系统至关重要。 该研究结合了逐层线性探测、稀疏自编码器和交叉编码器，在三个开源权重模型家族中定位偏好表征并量化潜在空间中的几何变换。

rss · arXiv - Machine Learning · Jun 10, 04:00

**背景**: 机制可解释性旨在逆向工程神经网络的内部计算，超越输入-输出分析。DPO 和 PPO 等偏好优化方法用于使语言模型与人类价值观对齐，但其内部影响尚不明确。本文应用机制工具比较了六种此类方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://transformer-circuits.pub/2024/crosscoders/">Sparse Crosscoders for Cross-Layer Features and Model Diffing</a></li>
<li><a href="https://aman.ai/primers/ai/preference-optimization/">Aman's AI Journal • Primers • Policy/Preference Optimization</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#mechanistic interpretability`, `#language models`, `#preference optimization`

---

<a id="item-20"></a>
## [SynIB：信息瓶颈提升多模态协同](https://arxiv.org/abs/2606.09853) ⭐️ 8.0/10

研究人员提出了协同信息瓶颈（SynIB），这是一种可扩展的训练目标，直接最大化多模态学习中的协同信息，在依赖协同的样本上准确率提升高达 7.8%。 SynIB 解决了当前多模态方法的一个根本性局限——它们往往依赖冗余或单模态信息，有望改进需要真正跨模态理解的 AI 系统，如仇恨言论检测或情感识别。 SynIB 通过每次遮蔽一个模态进行前向传播，并对模型保持高置信度施加惩罚，迫使模型依赖跨模态交互。在包括 Hateful Memes 和 CREMA-D 在内的五个真实世界基准上，总体准确率提升高达 3.8%。

rss · arXiv - Machine Learning · Jun 10, 04:00

**背景**: 多模态学习旨在结合来自多个来源（如文本和图像）的信息。协同是指仅当多种模态联合使用时才出现的信息，单独任何模态都无法提供。标准训练往往无法捕捉协同，因为模型可能依赖单模态线索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.09853">[2606.09853] SynIB: Informational Bottleneck for Maximizing Synergy ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.09853">SynIB: Informational Bottleneck for Maximizing Synergy in ...</a></li>
<li><a href="https://aidailypost.com/news/synib-introduces-information-bottleneck-boost-multimodal-synergy">SynIB Introduces Information Bottleneck to Boost...</a></li>

</ul>
</details>

**标签**: `#multimodal learning`, `#information bottleneck`, `#synergy`, `#information theory`, `#deep learning`

---

<a id="item-21"></a>
## [UniTok：时间序列通用分词器](https://arxiv.org/abs/2606.09861) ⭐️ 8.0/10

研究人员提出了 UniTok，一种将连续时间序列转换为离散标记的通用分词器，以及 UniTok-FM，一个基于这些标记通过下一个标记预测进行预训练的基础模型，实现了零样本预测和上下文学习。 这项工作弥合了 LLM 式预训练与连续时间序列之间的差距，为能够处理预测、生成和分类而无需特定任务训练的通用时间序列基础模型铺平了道路。 UniTok 使用带有前缀归一化的向量量化自编码器、渐进分辨率因果架构和结构保持重建损失。UniTok-FM 采用标准 LLM 架构，没有针对时间序列的特定修改。

rss · arXiv - Machine Learning · Jun 10, 04:00

**背景**: 下一个标记预测（NTP）在预训练大型语言模型（LLM）方面非常成功，但将其应用于连续时间序列具有挑战性，因为时间序列是无界且连续的。分词是将时间序列离散化为可由 LLM 风格架构处理的标记的关键步骤。先前的时间序列基础模型通常需要特定任务的微调或缺乏零样本能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.09861">[2606.09861] Time Series as Language: A Universal Tokenizer for...</a></li>
<li><a href="https://arxiv.org/pdf/2606.09861">Time Series as Language: A Universal Tokenizer for General-Purpose...</a></li>

</ul>
</details>

**标签**: `#time series`, `#foundation model`, `#tokenizer`, `#LLM`, `#pretraining`

---

<a id="item-22"></a>
## [LLM 智能体虚假成功：系统性研究](https://arxiv.org/abs/2606.09863) ⭐️ 8.0/10

该论文系统性地刻画了 LLM 智能体中的“虚假成功”现象，即智能体错误地声称任务已完成，发现该现象在不同设置下占失败的 45%-75%，且 LLM 评判器无法可靠检测。 这项研究揭示了 LLM 智能体在可靠性方面的关键缺陷，对 AI 安全及生产系统部署具有重要意义——未被检测到的失败可能导致高昂代价。 该研究分析了来自 8 个模型家族的 9,876 条 tau2-bench 轨迹和来自 4 个模型家族的 1,879 条 AppWorld 轨迹。轻量级 TF-IDF 检测器在 tau2-bench 上 AUROC 达 0.83，在 AppWorld 上达 0.95，优于 LLM 评判器（最高 AUROC 0.65），且延迟低 3300 倍。

rss · arXiv - Machine Learning · Jun 10, 04:00

**背景**: LLM 智能体是利用大语言模型与环境交互来执行任务的 AI 系统。“虚假成功”指智能体声称完成任务但实际未达成目标，这在自主系统中很危险。tau2-bench 和 AppWorld 分别是评估智能体在工具使用和编程任务中性能的基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentbeats.dev/agentbeater/tau2-bench?leaderboard_page_0=2">tau 2 - bench - AgentBeats</a></li>
<li><a href="https://arxiv.org/abs/2407.18901">[2407.18901] AppWorld : A Controllable World of Apps and People for...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#AI safety`, `#failure analysis`, `#benchmarking`, `#agent evaluation`

---

<a id="item-23"></a>
## [PPT：用概率程序微调 LLM 以提升归纳推理能力](https://arxiv.org/abs/2606.09856) ⭐️ 8.0/10

研究人员提出了基于程序的后验训练（PPT），该方法通过在概率程序上微调大型语言模型，以提升从稀疏数据中进行归纳推理的能力。该方法生成了 10,000 个程序化场景，并使用概率推理生成分布式的软标签用于训练。 这项工作填补了 LLM 后训练中的一个关键空白——此前主要关注数学和编程等演绎推理任务。通过使 LLM 能够进行带有校准不确定性的归纳推理，PPT 有望提升 AI 处理观测稀疏且模糊的真实世界问题的能力。 PPT 利用 LLM 生成多样化的开放世界场景作为概率程序，运行概率推理产生分布式的目标，并在这些软标签上进行微调。校准方面的提升并未被事后温度缩放所涵盖，表明模型更深入地内化了不确定性。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: LLM 的后训练通常针对演绎推理任务，如数学和编程，这些任务的正确性是可验证的。归纳推理涉及从稀疏观测中推断不确定的信念，由于难以整理标注数据集和处理分布式的目标，因此更具挑战性。概率编程将编程与概率推理相结合，用于建模不确定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.10182">A Survey of Inductive Reasoning for Large Language Models Images The Role of Deductive and Inductive Reasoning in Large ... Inductive reasoning in humans and large language models Inductive reasoning in humans and large language models ... Hypothesis Search: Inductive Reasoning with Language Models Evaluating the Inductive Abilities of Large Language Models ... Inductive Linguistic Reasoning with Large Language Models</a></li>
<li><a href="https://github.com/probcomp/LLaMPPL">GitHub - probcomp/LLaMPPL: A domain-specific probabilistic ... Bayesian teaching enables probabilistic reasoning in large ... Teaching LLMs to reason like Bayesians - Google Research Fine Tuning Large Language Model (LLM) - GeeksforGeeks Probabilistic Programming with LLM Integration | AI Tutorial From Probabilistic to Predictable: Engineering Near ... - Medium</a></li>
<li><a href="https://www.nature.com/articles/s41467-025-67998-6">Bayesian teaching enables probabilistic reasoning in large ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#probabilistic programming`, `#inductive reasoning`, `#fine-tuning`, `#AI research`

---

<a id="item-24"></a>
## [Engram：双时态记忆引擎提升 LLM 智能体准确率](https://arxiv.org/abs/2606.09900) ⭐️ 8.0/10

Engram 是一个面向 LLM 智能体的开源双时态记忆引擎，在 LongMemEval_S 上仅用约 9.6k token 的检索上下文就达到了 83.6%的准确率，以约 8 分之一的 token 数超越了全历史基线（73.2%）。 这项工作直接解决了 LLM 智能体中长期记忆的长期挑战，表明精简且结构良好的检索可以胜过暴力全上下文回放，有望实现更高效、可扩展的智能体架构。 Engram 采用包含有效时间和记录时间的双时态数据模型，将原子事实（主语、谓语、宾语）提取到知识图谱中，并使用融合了稠密、词汇、图和新近度信号的混合读取路径。该论文还提供了可复现的评估框架，并记录了常见的基准测试陷阱。

rss · arXiv - NLP · Jun 10, 04:00

**背景**: LLM 智能体经常在跨会话中丢失上下文；常见的解决方法是将整个对话历史回放到提示中，这既昂贵又随着干扰累积而变得不准确。双时态建模同时跟踪事实在现实世界中为真的时间（有效时间）和记录时间（记录时间），从而实现精确的时间点查询。Engram 基于这些概念为智能体提供高效、准确的记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bitemporal_Modeling">Bitemporal modeling - Wikipedia</a></li>
<li><a href="https://github.com/B12Labs/engram">GitHub - B12Labs/engram: Portable memory for AI agents. Graph ...</a></li>
<li><a href="https://arxiv.org/abs/2010.05953">[2010.05953] COMET-ATOMIC 2020: On Symbolic and Neural ... Images Thiwanka-Sandakalum/atomic-fact-knowledge-graph - GitHub (Comet-) Atomic 2020: On Symbolic and Neural Commonsense ... COMET-ATOMIC 2020: On Symbolic and Neural ... - AllenAI Benchmarks for Commonsense Reasoning: Symbolic and Knowledge ... ATOM: AdapTive and OptiMized dynamic temporal knowledge graph ... Beyond Basic Chunking: Harnessing Atomic Facts and Graph Fact ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#memory systems`, `#knowledge graph`, `#temporal data`, `#information retrieval`

---

<a id="item-25"></a>
## [CodeAlchemy：通过执行轨迹生成 5000 亿+合成代码令牌](https://arxiv.org/abs/2606.10087) ⭐️ 8.0/10

CodeAlchemy 使用五种策略生成了超过 5000 亿个合成代码令牌，其中包括来自 14 种语言和 5000 个库的 130 万个文件的执行轨迹。该框架还产生了 3500 亿个推理令牌，并引入了两个新基准：DevEval 和 TraceEval。 这项工作通过提供大规模、语义丰富的合成数据（不仅包含语法，还包含运行时行为），解决了代码预训练中的一个关键空白。它使得小模型（3B 参数）在多个基准测试上超越比其大 10 倍的前沿模型，可能使代码 AI 更加普及。 五种策略包括：CodeEnhance（质量感知重写）、CodeQA（基于模板的问题）、CodeDev（开发者任务）、CodeDialogue（多轮对话）和 CodeTrace（执行轨迹）。3B 模型在 HumanEval 上达到 83.5%，在 MBPP 上达到 63.2%，在 DevEval 上胜率为 8.09%，而像 Claude Sonnet 4.5 这样的前沿模型在 TraceEval 上仅达到 5.6%的精确匹配。

rss · arXiv - NLP · Jun 10, 04:00

**背景**: 在原始代码上进行预训练可以学习语法，但对于调试或代码审查等多样化的现实任务提供的信号有限。合成数据对语言模型产生了变革性影响，但其在代码领域的应用仅限于小规模的质量改进。执行轨迹捕获运行时行为，如控制流和状态变化，比静态代码提供更丰富的训练信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.10087">CodeAlchemy : Synthetic Code Rewriting at Scale</a></li>
<li><a href="https://joshuaberkowitz.us/blog/papers-7/code-world-model-a-32b-agentic-coding-llm-grounded-in-execution-traces-1282">Code World Model : A 32B Agentic Coding LLM... | Joshua Berkowitz</a></li>

</ul>
</details>

**标签**: `#synthetic data`, `#code generation`, `#pre-training`, `#large language models`, `#execution traces`

---

<a id="item-26"></a>
## [OpenRTLSet：最大的开源 Verilog 数据集](https://arxiv.org/abs/2606.10285) ⭐️ 8.0/10

OpenRTLSet 推出了最大的完全开源 Verilog 数据集，包含超过 131,000 个样本，涵盖来自 GitHub 的模块、VHDL 翻译和 C/C++ 翻译，并配有由 DeepSeek-R1 生成的自然语言描述。 该数据集使得针对 Verilog 代码生成的大语言模型微调成为可能，有望加速硬件设计自动化，并让研究人员和工业界更容易获得 AI 辅助的硬件设计能力。 该数据集包含 102k 个 GitHub 模块、5k 个 VHDL 翻译和 24k 个 C/C++ 翻译，并探索了量化技术（INT4 与 BF16）以及从 7B 到 32B 参数的模型规模。

rss · arXiv - NLP · Jun 10, 04:00

**背景**: Verilog 是一种用于建模电子系统的硬件描述语言。大语言模型在代码生成方面已展现出潜力，但由于缺乏大规模开源数据集，其在硬件设计中的应用受到限制。OpenRTLSet 通过提供多样化、免费可用的数据集来填补这一空白，用于训练 LLM 进行 Verilog 模块设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-R1">deepseek-ai/ DeepSeek - R 1 · Hugging Face</a></li>
<li><a href="https://chipverify.com/verilog/verilog-modules">Verilog Module</a></li>
<li><a href="https://itsembedded.com/dhd/verilator_1/">Verilator Pt.1: Introduction :: It's Embedded!</a></li>

</ul>
</details>

**标签**: `#hardware design`, `#Verilog`, `#open-source dataset`, `#large language models`, `#AI-assisted design`

---

<a id="item-27"></a>
## [WHU-Infra3D：面向 3D 路边基础设施的多模态数据集](https://arxiv.org/abs/2606.09882) ⭐️ 8.0/10

研究人员发布了 WHU-Infra3D，这是一个覆盖三个城市 53.8 公里的大规模多模态数据集，集成了全景图像和 LiDAR 点云，具有 2D-3D 实例关联和超过 18.1 万个属性标注，用于路边基础设施清单和健康评估。 该数据集通过提供自动化基础设施维护所需的细粒度属性和状态标注（如锈蚀、遮挡），填补了数字孪生研究中的关键空白，推动了可扩展的 AI 驱动城市资产全生命周期管理。 该数据集包含超过 17.5 万个多视角 2D 边界框、数千个 3D 基础设施实例，并为五个核心任务建立了基线：2D 检测、跨视角匹配、3D 地理识别、点云分割和属性识别。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 数字孪生城市旨在创建物理城市资产的虚拟副本以进行模拟和管理。然而，现有数据集通常缺乏自动化基础设施健康诊断所需的精确多模态对齐和详细属性标注。LiDAR 点云标注是此类系统中 3D 目标检测和分割的关键技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.09882">[2606.09882] WHU-Infra3D: A Full-stack Multi-modal Dataset ...</a></li>
<li><a href="https://github.com/WHU-USI3DV/WHU-Infra3D">GitHub - WHU-USI3DV/WHU-Infra3D · GitHub</a></li>

</ul>
</details>

**标签**: `#3D perception`, `#multi-modal dataset`, `#digital twin`, `#LiDAR`, `#infrastructure inventory`

---

<a id="item-28"></a>
## [ABot-Earth 0.5：从卫星图像生成 3D 城市](https://arxiv.org/abs/2606.09967) ⭐️ 8.0/10

ABot-Earth 0.5 是一个生成式 3D 框架，利用 3D 高斯泼溅从卫星图像合成逼真的大规模城市环境，生成速度低于每平方公里 10 分钟。 这项工作显著降低了创建大规模 3D 城市重建的成本和技术门槛，实现了实时交互式可视化，并有助于缩小无人机导航等具身 AI 应用的模拟到现实差距。 该模型在真实城市重建语料库上训练，推理时仅以卫星图像为条件，并集成了分层细节层次（LOD）结构，支持基于网页的实时渲染。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 3D 高斯泼溅（3DGS）是一种最新的实时辐射场渲染技术，将场景表示为 3D 高斯集合。具身 AI 指嵌入物理身体并与真实世界交互的 AI 系统，而模拟到现实差距描述了将在模拟中训练的模型迁移到真实环境所面临的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/embodied-ai/">What is Embodied AI? | NVIDIA Glossary</a></li>
<li><a href="https://thirddimension.ai/blog/posts/the-domain-gap-problem-why-traditional-simulators-fall-short-for-robotics">The Domain Gap : Why Traditional Simulators Fall... | Third Dimension</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#Gaussian Splatting`, `#Embodied AI`, `#urban simulation`, `#satellite imagery`

---

<a id="item-29"></a>
## [SpineReport：腰椎退变的自动化 3D MRI 分析](https://arxiv.org/abs/2606.10021) ⭐️ 8.0/10

SpineReport 是一个开源、全自动的框架，可对腰椎 MRI 进行全面的 3D 形态测量分析，从椎管、脊髓、椎骨、椎间盘和椎间孔等关键结构中提取定量指标。 该框架通过提供客观、可解释的 3D 指标，解决了当前 2D 临床评估可重复性差的问题，有望改善腰椎退变的诊断和监测。 在临床评估中，SpineReport 的 T2 加权 CSF 信号对中央椎管狭窄的 AUC 达到 0.95，椎管 AP 直径和面积比的 AUC 超过 0.80；然而，对于椎间孔狭窄未发现显著关联。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 腰椎退变是导致残疾的主要原因，但 MRI 分析通常局限于 2D 测量，既耗时又重复性差。自动化的 3D 量化可以提供更一致和全面的评估。形态测量分析涉及从医学图像中测量解剖结构的形状和大小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vertebral_foramen">Vertebral foramen - Wikipedia</a></li>
<li><a href="https://my.clevelandclinic.org/health/diseases/24856-foraminal-stenosis">Foraminal Stenosis: What It Is, Symptoms, Types & Treatments</a></li>

</ul>
</details>

**标签**: `#medical imaging`, `#MRI`, `#spine degeneration`, `#automated quantification`, `#deep learning`

---

<a id="item-30"></a>
## [医学视觉语言模型基准测试中的图像重叠审计](https://arxiv.org/abs/2606.10066) ⭐️ 8.0/10

一篇新论文对医学视觉语言模型基准测试中的预训练数据污染进行了审计，发现可测量的图像侧源重叠（例如 SLAKE-En 上 19.8%），但未确认像素级重复。 这项工作凸显了基准测试数据泄露可能导致医学 AI 性能被夸大的风险，敦促社区在信任报告准确率之前采用严格的污染检测方法。 该研究使用了四类检测器，包括基于 SigLIP 的图像相似性和规范顺序可交换性测试，并发现像 Min-K%++这样的队列相对检测器在小型医学队列上不可靠。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 医学视觉语言模型（VLM）在公开基准测试上进行评估，但这些数据可能在预训练期间已被模型见过，导致数据污染。检测污染具有挑战性，因为模型可能记忆示例。本文使用多种检测方法系统审计了几个基准测试，以评估污染程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.10066">A Controlled Audit of Pretraining Contamination in Public Medical...</a></li>
<li><a href="https://arxiv.org/pdf/2606.10066">A Controlled Audit of Pretraining Contamination in Public ...</a></li>
<li><a href="https://huggingface.co/docs/transformers/model_doc/siglip">SigLIP · Hugging Face</a></li>

</ul>
</details>

**标签**: `#medical vision-language models`, `#data contamination`, `#benchmark auditing`, `#pretraining`, `#AI evaluation`

---

<a id="item-31"></a>
## [新指标 MMA 改进实例分割评估](https://arxiv.org/abs/2606.10107) ⭐️ 8.0/10

研究人员提出了最大匹配精度（MMA），这是一种无阈值、连续的实例分割指标，采用全局最优的一对一匹配和逐像素归一化。 MMA 解决了现有指标（如 AP 和 PQ）的根本缺陷，如评分不连续和匹配非最优，从而提供更稳定、更敏感、更可解释的评估，尤其适用于生物细胞成像。 MMA 通过最大二分匹配强制真实掩码与预测掩码之间的一一对应，并使用逐像素归一化聚合重叠，无需任何 IoU 阈值。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 实例分割评估指标如平均精度（AP）和全景质量（PQ）依赖于硬 IoU 阈值和贪心匹配，在常见故障模式（如细胞分裂或合并）下可能产生不连续的分数和不可靠的排名。MMA 通过使用全局最优匹配和连续评分克服了这些问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.10107">Maximum Matching Accuracy : An Instance Segmentation Evaluation...</a></li>
<li><a href="https://github.com/kadenstillwagon/MMA">Maximum Matching Accuracy: An Instance Segmentation ... - GitHub</a></li>

</ul>
</details>

**标签**: `#instance segmentation`, `#evaluation metric`, `#computer vision`, `#biological imaging`

---

<a id="item-32"></a>
## [BiWM：首个开源双向自回归视频世界模型](https://arxiv.org/abs/2606.10135) ⭐️ 8.0/10

BiWM 是首个采用双向自回归的全栈开源交互式视频世界模型框架，仅需两个训练阶段（而非四个），在 8 块 H200 GPU 上几百步即可收敛。 该框架解决了视频世界模型中的误差累积和交互性问题，实现了高保真、可控的视频生成及真实世界相机控制，对机器人仿真和自动驾驶等应用至关重要。 BiWM 支持多种骨干网络，包括 Wan2.1-1.3B、Wan2.2-5B、HunyuanVideo-1.5-8B 和 LTX-2.3-22B，并提供可选的 NVFP4 4 位训练/推理以及可插拔历史压缩以支持长序列生成。

rss · arXiv - Computer Vision · Jun 10, 04:00

**背景**: 视频世界模型旨在通过基于动作或控制生成未来视频帧来模拟环境。传统的双向扩散模型质量高但缺乏交互性，而因果自回归模型支持交互但存在误差累积。BiWM 通过双向自回归和分布匹配蒸馏结合了两种范式的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/gracezhao1997/Awesome-Video-World-Models-with-AR-Diffusion">GitHub - gracezhao1997/Awesome- Video - World - Models -with...</a></li>
<li><a href="https://tianweiy.github.io/dmd/">One-step Diffusion with Distribution Matching Distillation</a></li>

</ul>
</details>

**标签**: `#video generation`, `#world models`, `#autoregressive models`, `#diffusion models`, `#open-source`

---

<a id="item-33"></a>
## [面向少样本 Text-to-SQL 的鲁棒主动学习](https://arxiv.org/abs/2606.10125) ⭐️ 8.0/10

一篇新论文提出了一种分层贪心算法，用于在 Text-to-SQL 中主动选择少样本示例，该算法处理了异方差标注可靠性和分区拟阵约束。 这项工作解决了部署 Text-to-SQL 系统的一个关键瓶颈：在保持高准确率的同时减少昂贵的专家标注，从而降低领域特定应用的门槛。 该算法最大化异方差互信息目标，具有理论上的常数因子近似保证，并且在模型误设下近似性能优雅退化。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: Text-to-SQL 系统将自然语言查询转换为 SQL 语句。少样本示例检索依赖少量标注示例来引导大语言模型，但标注成本高昂。主动学习旨在选择最具信息量的示例进行标注，从而减少工作量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2606.10125">Robust Active Learning for Few-Shot Example Selection in Text-to-SQL</a></li>
<li><a href="https://arxiv.org/pdf/2602.11825">CAAL: Confidence-Aware Active Learning for Heteroscedastic ...</a></li>
<li><a href="https://arxiv.org/pdf/2606.07954">Minibatch Selection via Partition Matroid Constrained ...</a></li>

</ul>
</details>

**标签**: `#text-to-SQL`, `#active learning`, `#few-shot learning`, `#large language models`, `#experimental design`

---

<a id="item-34"></a>
## [面向广告投放节奏的决策校准共形不确定性](https://arxiv.org/abs/2606.10187) ⭐️ 8.0/10

该论文提出了一种面向流媒体广告投放节奏的决策校准共形预测框架，它通过预测误差对可部署策略的最大影响来衡量误差，而非使用通用残差。该方法提供了有限样本覆盖保证，并在真实数据集上大幅降低了不确定性半径。 这项工作弥合了不确定性量化与实时竞价之间的鸿沟，使广告主能够在不过度保守的情况下做出自信的投放节奏决策。它有望提高预算效率并减少流媒体广告系统中的违规行为，对广告技术和机器学习运营产生影响。 在 Criteo 和 KuaiRand 数据集上，传统共形投放的残差半径分别为 7236.7 和 4629.4，而所提方法将其分别降至 18.4 和 278.6。在 Criteo 上，该方法还将任何违规率从 16.7%降至 3.3%，且预算和成员负载违规为零。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: 共形预测是一种无分布假设的方法，用于构建具有保证覆盖率的预测区间。流媒体广告中的投放节奏涉及在不确定的未来库存和需求下管理预算支出。传统的共形方法基于通用预测残差进行校准，这对于下游决策可能过于保守。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>
<li><a href="https://arxiv.org/abs/2107.07511">[2107.07511] A Gentle Introduction to Conformal Prediction ...</a></li>
<li><a href="https://climbtheladder.com/what-is-pacing-in-advertising-and-how-does-it-work/">What Is Pacing in Advertising and How Does It Work? - CLIMB</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#streaming advertising`, `#uncertainty quantification`, `#decision calibration`, `#pacing`

---

<a id="item-35"></a>
## [玻尔兹曼边际实现 kNN 近指数收敛速率](https://arxiv.org/abs/2606.10361) ⭐️ 8.0/10

本文提出了玻尔兹曼边际条件，它桥接了 Tsybakov 边际和 Massart 边际，并首次证明了 kNN 分类的近指数收敛速率。 这一理论进展显著收紧了 kNN 分类器的收敛保证，可能影响未来的分类理论和算法设计。 玻尔兹曼边际弱于 Massart 边际但通常强于 Tsybakov 边际，论文还提供了数值证据支持理论结果。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: 分类器的收敛速率分析通常使用 Tsybakov 边际（弱，多项式速率）或 Massart 边际（强，指数速率）。玻尔兹曼边际填补了这两种机制之间的空白，在更弱条件下实现更快的速率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Boltzmann_distribution">Boltzmann distribution - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/1406.5383">[1406.5383] Noise-adaptive Margin -based Active Learning and Lower...</a></li>
<li><a href="https://people.math.binghamton.edu/qiao/math605/book/fast-rate-under-margin-condition.html">Chapter 6 Fast rate under margin condition | Theory of ...</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#classification`, `#convergence rates`, `#kNN`, `#margin theory`

---

<a id="item-36"></a>
## [从校准视角看人机协作](https://arxiv.org/abs/2606.10906) ⭐️ 8.0/10

一篇新论文通过统计校准的视角分析了人机协作框架，表明组合方法无法保持人类的校准，而委托则将负担转移给决定谁预测的拒绝器元模型。 这项工作指出了现有人机协作方法的根本局限性，可能影响医疗、自动驾驶等高风险领域协作 AI 系统的设计。 论文假设人类和 AI 都相对于某种特征空间划分是校准的，并通过理论和实证结果表明组合方法无法保持人类的校准，而委托则要求拒绝器进行精细校准，这一需求随着人类专业知识的增加而增长。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: 机器学习中的统计校准是指预测概率反映真实可能性的性质。人机协作框架包括组合（平均预测）和委托（通过拒绝器元模型将决策路由给人类或模型）。拒绝器元模型根据估计的成功概率决定由谁进行预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2501.19047v2">Understanding Model Calibration - A gentle introduction and ...</a></li>
<li><a href="https://openreview.net/forum?id=SZQJ8K2DUe">Learning to Defer with an Uncertain Rejector via Conformal ...</a></li>
<li><a href="https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1733942/full">Frontiers | From testbeds to high-stakes work: a review of Human - AI ...</a></li>

</ul>
</details>

**标签**: `#human-AI teaming`, `#calibration`, `#machine learning`, `#delegation`, `#AI safety`

---

<a id="item-37"></a>
## [面向分布偏移的广义共形预测系统](https://arxiv.org/abs/2606.11044) ⭐️ 8.0/10

该论文通过引入观测特定的排列权重，将共形预测系统（CPS）扩展到非可交换场景，从而在分布偏移下提供具有有限样本保证的有效预测带。 这项工作解决了标准共形预测的一个关键局限性——对可交换性的依赖——使不确定性量化对现实世界中的分布偏移具有鲁棒性，这对于动态环境中可靠的机器学习至关重要。 该方法包括处理估计权重的权重不确定性框，并为一致性度量 CPS、共形分箱和共形保序分布回归提供高效计算。在协变量偏移和生物分子设计下的实验显示，校准带在更强偏移下变宽。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: 共形预测是一种不确定性量化框架，在可交换性假设下产生具有保证覆盖率的预测集。共形预测系统（CPS）将其扩展到输出校准的预测分布（CDF）。然而，当训练和测试时的数据分布发生偏移时（这是实践中的常见问题），标准 CPS 会失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2411.11824">Theoretical Foundations of Conformal Prediction</a></li>
<li><a href="https://www.emergentmind.com/topics/conformal-prediction">Conformal Prediction Methods</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#distribution shift`, `#uncertainty quantification`, `#machine learning`, `#statistical learning`

---

<a id="item-38"></a>
## [伊藤映射实现任意步长 SDE 生成模型](https://arxiv.org/abs/2606.11156) ⭐️ 8.0/10

研究人员提出了伊藤映射（Itô map），这是一种随机流映射，能够接收中间状态和布朗路径，单步预测未来状态，从而为生成模型实现任意步长 SDE 积分。 这项工作弥合了基于确定性流的生成模型与随机动力学之间的差距，为图像生成和随机控制等应用提供了高效的后验采样和推理时控制能力。 伊藤映射提供了对后验样本的可微访问，在合成和图像生成基准上实现了强大的引导性能，并将任意步长 SDE 积分确立为一种有用的原语。

rss · arXiv - Data Science & Statistics · Jun 10, 04:00

**背景**: 近期的一步生成模型通过学习常微分方程的确定性流映射来加速采样。然而，随机动力学（SDE）缺乏精确的蒸馏过程。伊藤映射将这一概念扩展到随机场景，利用伊藤积分处理布朗运动路径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.11156">[2606.11156] Itô maps for any-step SDEs - arXiv.org</a></li>
<li><a href="https://en.wikipedia.org/wiki/Itô_calculus">Itô calculus - Wikipedia</a></li>
<li><a href="https://www.alphaxiv.org/abs/2606.11156">Itô maps for any-step SDEs | alphaXiv</a></li>

</ul>
</details>

**标签**: `#generative models`, `#stochastic differential equations`, `#posterior sampling`, `#machine learning`, `#control`

---

<a id="item-39"></a>
## [葡萄糖胺与阿尔茨海默病加速进展相关](https://www.sciencedaily.com/releases/2026/06/260610003044.htm) ⭐️ 8.0/10

2026 年 6 月发表的一项重大研究发现，常见的关节补充剂葡萄糖胺与从轻度认知障碍进展为阿尔茨海默病的风险增加 25%相关。 这一发现挑战了葡萄糖胺在老年人中的广泛使用，可能对公共健康产生重大影响，因为数百万人为关节健康服用该补充剂，却未意识到潜在的认知风险。 该研究揭示了可能解释这一关联的生物学线索，但确切机制尚不清楚。研究聚焦于轻度认知障碍患者，这一阶段通常先于阿尔茨海默病出现。

rss · ScienceDaily Health · Jun 10, 05:17

**背景**: 葡萄糖胺是一种天然存在于软骨中的氨基糖，常被用作骨关节炎和关节疼痛的膳食补充剂。轻度认知障碍（MCI）涉及明显的认知下降，但尚未影响日常生活，而阿尔茨海默病是一种进行性神经退行性疾病，严重损害记忆和功能。这项研究为越来越多的证据增添了新内容，表明某些补充剂可能对大脑健康产生意想不到的影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Glucosamine">Glucosamine - Wikipedia</a></li>
<li><a href="https://www.verywellhealth.com/mild-cognitive-impairment-and-alzheimers-disease-98561">Mild Cognitive Impairment vs. Alzheimer's Disease</a></li>
<li><a href="https://health.clevelandclinic.org/mild-cognitive-impairment-vs-dementia">Mild Cognitive Impairment vs. Dementia: What’s the Difference?</a></li>

</ul>
</details>

**标签**: `#Alzheimer's`, `#glucosamine`, `#dementia`, `#health research`, `#supplements`

---