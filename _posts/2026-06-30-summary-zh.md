---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> From 106 items, 28 important content pieces were selected

---

1. [ATHENA-R1：通过强化学习进行治疗推理的 AI 智能体](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Sonnet 5，增强自主能力](#item-2) ⭐️ 8.0/10
3. [Claude Code 隐写标记请求](#item-3) ⭐️ 8.0/10
4. [Anthropic 推出 Claude Science，面向安全环境的数据科学工具](#item-4) ⭐️ 8.0/10
5. [shot-scraper video：让 AI 代理录制 Web 应用演示视频](#item-5) ⭐️ 8.0/10
6. [CuPy：面向 GPU 加速的 NumPy/SciPy 替代库](#item-6) ⭐️ 8.0/10
7. [openpilot：开源机器人操作系统，升级驾驶辅助系统](#item-7) ⭐️ 8.0/10
8. [Free-for-Dev：免费云服务精选列表](#item-8) ⭐️ 8.0/10
9. [VeraCrypt：基于 TrueCrypt 的磁盘加密软件](#item-9) ⭐️ 8.0/10
10. [谷歌发布 TimesFM 2.5 用于时间序列预测](#item-10) ⭐️ 8.0/10
11. [RSEA：通过留出选择实现递归自进化智能体](#item-11) ⭐️ 8.0/10
12. [能力切片闭环大模型预训练数据与评估](#item-12) ⭐️ 8.0/10
13. [GPTNT：实时多模态智能体协作基准测试](#item-13) ⭐️ 8.0/10
14. [IMCBench：多模态大语言模型在医疗对话中的基准测试](#item-14) ⭐️ 8.0/10
15. [COMPASS：面向构图意图的统一多模态框架](#item-15) ⭐️ 8.0/10
16. [BV-Blend 稳定了基于可验证奖励的无评论家强化学习](#item-16) ⭐️ 8.0/10
17. [SciDraw-Bench：科学图形生成基准](#item-17) ⭐️ 8.0/10
18. [网格智能需要液态基底](#item-18) ⭐️ 8.0/10
19. [强化学习研究者需区分求解模拟器与将其作为代理使用](#item-19) ⭐️ 8.0/10
20. [深度单项式网络：数学解释简单模型偏好](#item-20) ⭐️ 8.0/10
21. [LLM 心智理论出现晚且脆弱](#item-21) ⭐️ 8.0/10
22. [面向长上下文的轮次平均稀疏自编码器](#item-22) ⭐️ 8.0/10
23. [静态斐波那契间隔在稀疏注意力中优于学习膨胀](#item-23) ⭐️ 8.0/10
24. [SEAD：熵引导的在线策略蒸馏提升大模型训练效率](#item-24) ⭐️ 8.0/10
25. [用粒度校准验证 LLM 的构念测量](#item-25) ⭐️ 8.0/10
26. [探究手语模型的音系感知能力](#item-26) ⭐️ 8.0/10
27. [RADIANT-PET：大语言模型与强化学习提升 PET/CT 病灶分割](#item-27) ⭐️ 8.0/10
28. [双向自回归潜扩散模型用于磁流体动力学](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [ATHENA-R1：通过强化学习进行治疗推理的 AI 智能体](https://arxiv.org/abs/2606.28692) ⭐️ 9.0/10

研究人员推出了 ATHENA-R1，这是一个通过强化学习在 212 个生物医学工具上训练的 AI 智能体，能够对自 1939 年以来所有 FDA 批准的药物进行治疗推理，且无需人工标注轨迹。 ATHENA-R1 在药物和治疗推理基准上显著优于现有模型（包括 GPT-5），其自学习框架无需昂贵的人工标注，有望加速临床决策支持。 ATHENA-R1 在开放式药物推理上达到 94.7%的准确率，在治疗推理上达到 82.9%，分别比 GPT-5 高出 17.8 和 10.7 个百分点。它生成的不良事件假设在 540 万患者的电子健康记录数据中得到了验证。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 治疗推理是一个复杂的迭代过程，需要整合疾病背景、合并症和药物信息。强化学习（RL）是一种机器学习范式，智能体通过试错学习最优行动，并越来越多地应用于个性化医学中的序贯决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12096033/">Reinforcement Learning in Personalized Medicine: A Comprehensive Review of Treatment Optimization Strategies - PMC</a></li>
<li><a href="https://www.nature.com/articles/s41746-024-01316-0">A Primer on Reinforcement Learning in Medicine for Clinicians | npj Digital Medicine</a></li>

</ul>
</details>

**标签**: `#AI`, `#biomedical`, `#reinforcement learning`, `#clinical decision support`, `#treatment reasoning`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Sonnet 5，增强自主能力](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Sonnet 5，该模型速度更快、能力更强，改进了自主能力和指令遵循能力，但在常识问答和工具调用任务上存在弱点。 此次发布意义重大，因为 Sonnet 5 在价格、质量和速度之间取得了更好的平衡，适用于辅助开发场景，可能使自主 AI 智能体更易获取且更实用。 社区基准测试显示，Sonnet 5 性能达到 GLM-5.2 水平，成本翻倍但速度也翻倍；在常识问答中得 0/3，组合工具调用得 45/100，谜题解决得 77。每任务成本图表建议，在较高努力水平下应使用 Opus 而非 Sonnet 5。

hackernews · marinesebastian · Jun 30, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: 自主 AI 指能够感知、推理并自主行动以在有限监督下完成目标的系统。工具调用允许大语言模型通过生成结构化请求来调用外部函数或 API，从而执行超越文本生成的实际任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/agentic-ai/">What is Agentic AI? - Agentic AI Explained - AWS</a></li>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>

</ul>
</details>

**社区讨论**: 社区反馈褒贬不一：部分用户称赞 Sonnet 5 改进了指令遵循能力并能一次性完成复杂任务，而另一些用户指出其在常识问答和工具调用方面的弱点，并质疑其在较高努力水平下相比 Opus 的成本效益。

**标签**: `#AI`, `#LLM`, `#Claude`, `#Anthropic`, `#agentic`

---

<a id="item-3"></a>
## [Claude Code 隐写标记请求](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

Anthropic 的 AI 编程助手 Claude Code 被发现通过在系统提示中嵌入不可见的 Unicode 标记，以隐写方式标记发出的请求。这一做法由安全研究人员发现并报告，揭示了该工具行为缺乏透明度。 这引发了关于用户同意和软件透明度的严重担忧，因为该工具在用户机器上运行代码而未明确告知。它还可能触犯 CFAA 等法律，并削弱对 AI 开发工具的信任。 隐写标记隐藏在用户不可见的 Unicode 字符中，其可能意图是检测 API 转售商、未经授权的网关或模型蒸馏攻击。该实现被批评为粗糙，本可以做得更隐蔽。

hackernews · kirushik · Jun 30, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是将信息隐藏在其他数据（如图像或文本）中以避免检测的做法。在本例中，Claude Code 使用不可见的 Unicode 字符在系统提示中嵌入标记，然后发送到 Anthropic 的服务器。该技术不同于加密，因为它隐藏了隐藏数据的存在本身。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thereallo.dev/blog/claude-code-prompt-steganography">Claude Code Is Steganographically Marking Requests</a></li>
<li><a href="https://spawn-queue.acm.org/doi/10.1145/3806226">In Code They Think; In Proof We Trust | Queue</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些人认为隐写术是防止中国公司滥用的合理措施，而另一些人则谴责它侵犯了用户信任，并可能违反 CFAA。批评者还指出实现粗糙，呼吁提高透明度并对开发工具进行沙盒化。

**标签**: `#AI`, `#security`, `#ethics`, `#steganography`, `#transparency`

---

<a id="item-4"></a>
## [Anthropic 推出 Claude Science，面向安全环境的数据科学工具](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 推出了 Claude Science，这是一个运行本地服务器和基于 Web 的 UI 的新工具，通过集成数据库和 HPC 集群，在严格受限的环境中实现数据科学任务。 该产品解决了制药等安全环境中研究人员的关键痛点——使用云端工具通常无法连接敏感数据，有望加速受监管行业的科学发现。 Claude Science 与 Claude Code 和 Cowork 不同，它运行本地服务器并采用基于浏览器的 UI，从而能在隔离或严格控制的网络中运行。它支持与机构集群及多种数据库的集成。

hackernews · lebovic · Jun 30, 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: 在高度监管的行业中，数据科学通常需要处理不能离开本地网络的敏感数据。传统的云端 AI 工具不适合此类环境，因此需要结合 AI 能力与本地数据访问的本地解决方案。

**社区讨论**: 社区评论强调了该产品在安全环境中的价值，一位相关 HPC 工具的构建者指出其与机构集群的集成。一位领域专家将其用于 RNAi 生物农药设计测试，认为其能力合格但不突出，并指出了使用哺乳动物设计规则等局限。

**标签**: `#AI`, `#data science`, `#Anthropic`, `#research tools`, `#HPC`

---

<a id="item-5"></a>
## [shot-scraper video：让 AI 代理录制 Web 应用演示视频](https://simonwillison.net/2026/Jun/30/shot-scraper-video/#atom-everything) ⭐️ 8.0/10

Simon Willison 发布了 shot-scraper 1.10，新增了 'video' 命令，该命令接受一个 storyboard.yml 文件，并使用 Playwright 录制 Web 应用程序操作的视频。该工具旨在让编码代理自动生成其工作成果的视频演示。 该工具解决了 AI 代理开发中的一个实际需求：通过生成可视化演示来证明代码确实有效。它使代理能够自主创建可分享的视频证据，这对调试、文档编写以及与利益相关者沟通都很有价值。 storyboard.yml 文件可以定义要启动的本地服务器、视口大小、光标可见性、等待条件、JavaScript 覆盖（例如用于模拟剪贴板），以及包含点击和暂停等操作的一系列场景。该命令支持 --auth 进行基于 cookie 的身份验证，并输出 WebM 或 MP4 格式的视频。

rss · Simon Willison · Jun 30, 16:54

**背景**: shot-scraper 是 Simon Willison 开发的一个 CLI 工具，用于使用 Playwright 截取网页截图和抓取网站数据。新的 'video' 命令将其扩展为录制完整的视频演示，这基于一个理念：AI 编码代理应生成演示来证明其工作确实能运行。Playwright 是一个浏览器自动化库，可以录制页面交互的视频。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper-video/">Have your agent record video demos of its work with shot-scraper video</a></li>
<li><a href="https://simonwillison.net/2026/Jun/30/shot-scraper/">Release: shot-scraper 1.10 - Simon Willison's Weblog</a></li>
<li><a href="https://github.com/simonw/shot-scraper/issues">Issues · simonw/shot-scraper - GitHub</a></li>

</ul>
</details>

**标签**: `#developer-tools`, `#AI-agents`, `#video-recording`, `#playwright`, `#automation`

---

<a id="item-6"></a>
## [CuPy：面向 GPU 加速的 NumPy/SciPy 替代库](https://github.com/cupy/cupy) ⭐️ 8.0/10

CuPy 是一个开源库，提供与 NumPy 和 SciPy 兼容的 API，用于 GPU 加速计算，支持 NVIDIA CUDA 和 AMD ROCm 平台。它允许用户以最小修改在 GPU 上运行现有的 NumPy/SciPy 代码。 CuPy 通过利用 GPU 并行性显著加速数值计算任务，对数据科学、机器学习和科学计算非常有价值。它作为 NumPy/SciPy 的即插即用替代品，降低了 GPU 采用的门槛。 CuPy 支持 CUDA 和 ROCm 后端，并为 Linux 和 Windows 提供二进制 wheel 包。它还提供低级 CUDA 功能，如 RawKernels、Streams 和直接 CUDA 运行时 API 调用。

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**背景**: NumPy 和 SciPy 是 Python 中用于数值计算的基础库，但它们在 CPU 上运行。CuPy 将其功能扩展到 GPU，GPU 擅长并行操作，从而加速大型数组和复杂数学运算的计算。

**标签**: `#GPU computing`, `#NumPy`, `#SciPy`, `#Python`, `#machine learning`

---

<a id="item-7"></a>
## [openpilot：开源机器人操作系统，升级驾驶辅助系统](https://github.com/commaai/openpilot) ⭐️ 8.0/10

openpilot 是一个开源机器人操作系统，现已支持超过 300 种车型，用于升级驾驶辅助系统。该项目在 GitHub 上以 MIT 许可证发布。 openpilot 使先进的驾驶辅助技术更加普及，让爱好者和研究人员能够实验并改进自动驾驶功能。其开源特性促进了社区创新，加速了机器人和汽车领域的发展。 使用 openpilot 需要支持的设备（如 comma four）、兼容的汽车以及汽车线束。软件可通过 URL 安装，并提供预构建分支用于稳定版本。

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**背景**: openpilot 由 comma.ai 开发，该公司专注于构建自动驾驶平台。它运行在 comma four 等定制硬件上，提供自适应巡航控制和车道保持等功能。该项目是 GitHub 上最受欢迎的开源自动驾驶系统之一。

**标签**: `#autonomous driving`, `#open source`, `#robotics`, `#driver assistance`, `#comma.ai`

---

<a id="item-8"></a>
## [Free-for-Dev：免费云服务精选列表](https://github.com/ripienaar/free-for-dev) ⭐️ 8.0/10

由 1600 多位贡献者维护的 ripienaar/free-for-dev GitHub 仓库持续更新，提供了一份全面的 SaaS、PaaS 和 IaaS 服务列表，这些服务为开发者和 DevOps 从业者提供免费层级。 该资源将免费层级服务集中在一处，为开发者节省了大量时间，帮助他们做出明智的基础设施决策，而无需进行昂贵的试用。它在开发者社区中被广泛引用，是经济高效使用云服务的首选指南。 该列表明确排除自托管软件，并要求如果按时间分桶，免费层级至少持续一年；同时要求免费层级支持 TLS。该仓库带有主观性，专注于基础设施相关服务，而非通用免费工具。

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**背景**: SaaS、PaaS 和 IaaS 是通过互联网提供软件、平台和基础设施的云服务模型。许多提供商提供有限资源的免费层级以吸引开发者，但查找和比较它们可能很耗时。这份由 R.I. Pienaar 发起的精选列表通过社区贡献成长为可信赖的参考资源。

**标签**: `#devops`, `#free-tier`, `#SaaS`, `#PaaS`, `#IaaS`

---

<a id="item-9"></a>
## [VeraCrypt：基于 TrueCrypt 的磁盘加密软件](https://github.com/veracrypt/VeraCrypt) ⭐️ 8.0/10

VeraCrypt 是一款源自 TrueCrypt 7.1a 的磁盘加密软件，集成了安全增强和持续维护。GitHub 仓库提供了 Windows、Linux、macOS、FreeBSD 和 OpenBSD 的源代码。 VeraCrypt 在保持兼容性的同时修复了 TrueCrypt 的安全漏洞，成为保护敏感数据的可信工具。其开源特性和跨平台支持确保了在注重安全的用户中的广泛采用。 仓库包含预构建的 EFI 引导加载程序二进制文件和详细的 Windows 构建指南，需要 Visual Studio 和 Windows SDK。官方二进制文件使用 IDRIX 的 GlobalSign 证书进行数字签名，文件大小增加约 10 KiB。

rss · GitHub Trending - Daily (All) · Jun 30, 23:04

**背景**: TrueCrypt 是一款流行的磁盘加密工具，于 2014 年因安全问题突然停止开发。VeraCrypt 从 TrueCrypt 7.1a 分支出来，以继续开发并修复漏洞，例如 TrueCrypt 审计中发现的问题。它使用更强的密钥派生算法（例如更高迭代次数的 PBKDF2）并解决了其他安全问题。

**标签**: `#encryption`, `#security`, `#open-source`, `#disk-encryption`, `#cryptography`

---

<a id="item-10"></a>
## [谷歌发布 TimesFM 2.5 用于时间序列预测](https://github.com/google-research/timesfm) ⭐️ 8.0/10

谷歌研究发布了 TimesFM 2.5，这是一个用于时间序列预测的预训练基础模型，其检查点可在 Hugging Face 上获取，并已集成到 BigQuery ML、Google Sheets 和 Vertex Model Garden 中。 此次发布使最先进的时间序列预测技术更加普及，企业和开发者无需大量训练即可利用强大的基础模型。与 BigQuery ML 等谷歌产品的集成简化了大规模部署。 TimesFM 2.5 使用 2 亿参数（从 5 亿减少），支持高达 16k 的上下文长度，并通过可选的 3000 万分位数头提供高达 1k 水平线的连续分位数预测。它还包含用于更快推理的 Flax 版本，并通过 LoRA 支持微调。

rss · GitHub Trending - Python · Jun 30, 23:04

**背景**: 时间序列预测基于历史数据预测未来值，用于金融、天气和库存管理。基础模型是大型预训练模型，可通过少量微调适应各种任务。TimesFM 是一个仅解码器的 Transformer 模型，发表于 ICML 2024。

**社区讨论**: 社区积极为 TimesFM 做出贡献，特别感谢@kashif 和@darkpowerxo 提供微调示例，以及@borealBytes 添加代理支持。开源版本广受好评，并持续进行改进和添加单元测试。

**标签**: `#time-series forecasting`, `#foundation model`, `#Google Research`, `#machine learning`, `#ICML 2024`

---

<a id="item-11"></a>
## [RSEA：通过留出选择实现递归自进化智能体](https://arxiv.org/abs/2606.28374) ⭐️ 8.0/10

研究人员提出了 RSEA，一种递归自进化的大语言模型智能体，通过使用留出数据的严格保持更好门控来改进其自然语言状态，在四个基准测试中优于基线方法。 这项工作为无需权重更新的 LLM 智能体递归自我改进提供了一种原则性方法，解决了上下文进化中的退化问题，这对可靠的自主智能体至关重要。 RSEA 携带三层自然语言状态（策略、技能、剧本），仅当候选版本在不相交的留出分割上不退化时才提交。它在 ALFWorld 上达到 69.3%（ReAct 为 64.6%），重试后达到 79.4%，但在工具使用任务上，具体工作流归纳（AWM）表现最佳。

rss · arXiv - AI · Jun 30, 04:00

**背景**: LLM 智能体通常通过进化自然语言工件（如提示或工作流）来改进，而不更新模型权重。然而，不加防护的进化可能导致在某些任务上性能崩溃，例如 Dynamic Cheatsheet 在 WebShop 上的得分 0.14，而 ReAct 为 0.43。RSEA 的留出选择确保了单调安全的进化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.28374">[2606.28374] Recursive Self-Evolving Agents via Held-Out Selection - arXiv</a></li>
<li><a href="https://artificialintelligenceherald.com/ai/rsea-recursive-self-evolving-agents-held-out-selection-2026">RSEA Recursive Self-Evolving Agents via Held-Out Selection - AI Herald</a></li>
<li><a href="https://www.machinebrief.com/news/rsea-a-new-direction-in-ais-evolutionary-tactics-36cc">RSEA: A New Direction in AI's Evolutionary Tactics - Machine Brief</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#self-improvement`, `#benchmarking`, `#natural-language state`, `#recursive evolution`

---

<a id="item-12"></a>
## [能力切片闭环大模型预训练数据与评估](https://arxiv.org/abs/2606.28471) ⭐️ 8.0/10

论文提出“能力切片”作为单元，在大模型预训练中连接数据与评估，通过结构化分类和映射规则实现模型弱点的系统定位。 该工作通过将直觉推断转化为常规、可审计的方法，将基准测试失败转化为有针对性的数据干预，解决了大模型优化中的实际差距，有望提升模型效率和性能。 能力切片按背景条件、任务类型、求解操作和输出约束对评估样本分组，兼顾精确性和稳定性。两个案例研究展示了该闭环正确判定数据是否有效的能力，包括通过修复被掩码的<EOS>损失恢复 BBH 性能。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 在大模型预训练中，数据前瞻性地塑造模型能力，而评估通过有噪声的分数回顾性地揭示能力。由于数据和评估使用不兼容的词汇，工程师通常依赖直觉从基准测试失败推断数据修复。能力切片提供了共同单元来闭环这个反馈回路。

**标签**: `#LLM`, `#evaluation`, `#data-centric AI`, `#pre-training`, `#model capability`

---

<a id="item-13"></a>
## [GPTNT：实时多模态智能体协作基准测试](https://arxiv.org/abs/2606.28514) ⭐️ 8.0/10

研究人员推出了 GPTNT，这是一个基于合作游戏《保持通话，无人爆炸》的基准测试，用于评估多模态智能体在时间压力和信息不对称条件下的实时协作能力。 该基准测试填补了现有评估的空白，在时间压力和不完美通信等现实条件下测试协作能力，这对于在人类-智能体团队中部署 AI 至关重要。 在 GPTNT 中，一个智能体可以看到并操作炸弹但没有拆解说明，另一个智能体有说明但看不到炸弹；两者都无法单独成功，而当前最先进的模型无法在实时中拆解任何一枚炸弹。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 多模态智能体结合视觉、语言和行动来完成任务。现有的基准测试通常孤立地测试组件能力，忽略了现实协作中出现的时间压力、信息不对称和不完美通信等综合挑战。

**标签**: `#multimodal agents`, `#benchmark`, `#multi-agent collaboration`, `#real-time communication`, `#AI evaluation`

---

<a id="item-14"></a>
## [IMCBench：多模态大语言模型在医疗对话中的基准测试](https://arxiv.org/abs/2606.28556) ⭐️ 8.0/10

研究人员推出了 IMCBench 基准，该基准将真实临床图像与合成患者档案配对，用于评估多模态大语言模型在多轮医疗对话中的安全性、准确性和不确定性。来自四个模型家族（Claude、GPT、Nova、Llama）的八个前沿模型使用经过专家临床医生校准的 LLM-as-Jury 评分，在 1-5 分制上进行了评分。 该基准通过结合多模态输入和多轮对话，填补了关键空白，为医疗 AI 提供了更真实的评估。研究发现准确的临床描述并不能保证安全的指导，这凸显了医疗 AI 中需要多维评估框架。 Claude Opus 4.6 获得了最高总分（3.61），但没有模型在所有维度上占优；对于恶性和罕见疾病，安全性下降（各Δ = -0.27）。消融研究表明，移除视觉输入或 EHR 上下文分别使安全评分平均降低 0.18 和 0.23。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 大语言模型和视觉语言模型在临床应用中显示出潜力，如决策支持和分诊。然而，现有的医疗 AI 基准要么支持无图像的多轮对话，要么为单轮问答提供多模态输入，缺乏真实的组合。IMCBench 通过使用真实临床图像和合成档案模拟患者与临床医生的互动，填补了这一空白。

**标签**: `#multimodal LLM`, `#medical AI`, `#benchmark`, `#clinical conversation`, `#vision-language model`

---

<a id="item-15"></a>
## [COMPASS：面向构图意图的统一多模态框架](https://arxiv.org/abs/2606.28696) ⭐️ 8.0/10

COMPASS 提出了一个统一的多模态框架，通过共享专家令牌在单一系统中实现构图感知和构图引导生成。 这解决了当前多模态模型在细粒度构图识别和可控生成方面的关键局限，有望实现更精确的图像编辑和布局控制。 该框架使用混合专家（MoE）骨干网络和共享专家令牌 τ_c，并在 Comp-11 数据集上训练，该数据集包含 11 类分类和推理增强标注。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 统一多模态模型旨在同时处理理解和生成任务，但在物体放置等细粒度构图任务上常表现不佳。COMPASS 通过引入专门的构图意图令牌来指导感知和生成，弥补了这一差距。

**标签**: `#multimodal`, `#composition`, `#generation`, `#MoE`, `#computer vision`

---

<a id="item-16"></a>
## [BV-Blend 稳定了基于可验证奖励的无评论家强化学习](https://arxiv.org/abs/2606.28707) ⭐️ 8.0/10

研究人员提出了 BV-Blend，一种无评论家强化学习框架，通过结合提示局部在线策略统计与语义聚类条件的历史矩来稳定优势估计，解决了 GRPO 中当提示组内所有生成结果获得相同奖励时的零优势问题。 这项工作提高了使用可验证奖励对齐大语言模型的训练稳定性和性能，特别是在使用二元验证器的冷启动场景中，且无需像 PPO 那样基于评论家方法的额外内存和计算开销。 BV-Blend 为每个语义聚类维护指数移动平均（EMA）跟踪的奖励矩，从均值标准误（SEM）代理中导出置信权重，并将历史与提示局部基线和方差统计量混合成标准化优势，用于 PPO 风格的裁剪更新。

rss · arXiv - AI · Jun 30, 04:00

**背景**: 组相对策略优化（GRPO）是一种无评论家强化学习方法，避免了训练价值函数，相比 PPO 减少了内存和计算。然而，GRPO 的优势估计依赖于组内奖励统计，当组内所有响应获得相同奖励时可能变得不稳定，导致零优势和学习停滞。BV-Blend 通过引入来自语义相似提示的历史奖励矩来解决这个问题。

**标签**: `#reinforcement learning`, `#large language models`, `#RLHF`, `#advantage estimation`, `#GRPO`

---

<a id="item-17"></a>
## [SciDraw-Bench：科学图形生成基准](https://arxiv.org/abs/2606.28406) ⭐️ 8.0/10

研究人员推出了 SciDraw-Bench，这是一个包含 32 个结构化任务的基准测试，涵盖八种图形类型和十个学科，旨在评估文本到图像和多模态模型生成科学图形的能力。 现有基准仅评估自然图像，而 SciDraw-Bench 通过测量文本保真度、语义正确性、结构质量和惯例遵循填补了关键空白，这些对于科学图形至关重要。 该基准采用四维评估协议，包括基于 OCR 的文本保真度和基于 VLM 的语义正确性，初步研究表明领域特定系统（SciDraw AI）在所有维度上优于通用模型，其中文本保真度是最难的维度。

rss · arXiv - Machine Learning · Jun 30, 04:00

**背景**: 像 DALL-E 和 Stable Diffusion 这样的文本到图像模型可以生成自然图像，但科学图形需要精确的标签、正确的关系以及遵循学科惯例。现有的 GenEval 和 T2I-CompBench 等基准不测试这些方面。SciDraw-Bench 为每个任务提供了机器可检查的规范，以实现自动评估。

**标签**: `#AI`, `#benchmark`, `#scientific figures`, `#text-to-image`, `#multimodal`

---

<a id="item-18"></a>
## [网格智能需要液态基底](https://arxiv.org/abs/2606.28413) ⭐️ 8.0/10

一篇新的 arXiv 论文证明，在主权代理网格中进行最优估计需要自适应时间尺度和间隙感知处理，而固定增益滤波器和间隙盲网络无法实现这一点。 这项工作为去中心化多智能体系统建立了基本的理论约束，对分布式 AI、自适应系统和网格智能架构具有重要影响。 论文证明了两个必要条件：自适应时间尺度是必要的（固定增益滤波器严格次优），以及间隙感知处理是必要的（间隙盲网络在任何宽度或深度下都无法恢复缺失的依赖性）。

rss · arXiv - Machine Learning · Jun 30, 04:00

**背景**: 主权代理网格没有中央时钟、模型或协调器；每个代理必须从不规则观测中估计潜在状态。论文表明，只有连续时间液态网络同时满足这两个必要条件，而 LSTM 仅满足第一个，固定连续时间滤波器仅满足第二个。

**标签**: `#mesh intelligence`, `#distributed systems`, `#adaptive estimation`, `#multi-agent systems`, `#theoretical computer science`

---

<a id="item-19"></a>
## [强化学习研究者需区分求解模拟器与将其作为代理使用](https://arxiv.org/abs/2606.28433) ⭐️ 8.0/10

一篇立场论文指出，强化学习研究者常混淆模拟器的两种不同用途：求解模拟器本身与将其作为真实世界部署的代理，这会导致研究方向偏离。 这一区分至关重要，因为两种场景在约束条件、算法选择和评估指标上存在根本差异，若不明确说明所用场景，可能得出误导性结论，阻碍通用决策能力的研究进展。 论文通过示例和简单实验展示了纯粹为模拟器性能优化的解决方案（例如利用模拟器漏洞）可能无法迁移到真实部署，并呼吁更清晰的实验规范。

rss · arXiv - Machine Learning · Jun 30, 04:00

**背景**: 强化学习研究常使用基准模拟器在真实部署前开发和测试算法。然而，追求在模拟器中获得高分的目标可能无意中使焦点转向求解模拟器本身，而这属于不同的研究问题。

**标签**: `#reinforcement learning`, `#simulators`, `#research methodology`, `#benchmarking`

---

<a id="item-20"></a>
## [深度单项式网络：数学解释简单模型偏好](https://arxiv.org/abs/2606.28464) ⭐️ 8.0/10

一篇新论文利用多项式代数和 Mason 定理证明，深度单项式网络中的临界点恰好对应于子网络，为深度学习中的奥卡姆剃刀式隐式偏差提供了数学基础。 这项工作为深度神经网络为何倾向于收敛到更简单的函数提供了严格的数学解释，这是深度学习理论中的一个基本问题，可能指导更可解释和高效架构的设计。 该分析聚焦于具有单项式激活的全连接网络，并利用 Mason 定理（多项式版本）证明，对于足够大的激活度，临界点恰好出现在某些神经元不活跃或冗余的参数配置处。

rss · arXiv - Machine Learning · Jun 30, 04:00

**背景**: 奇异学习理论（SLT）研究过参数化模型中损失景观的几何结构，其中奇点（秩亏点）占主导地位。隐式偏差是指基于梯度的优化倾向于选择更简单解的趋势，而无需显式正则化。本文通过连接 SLT 和多项式代数来解释这种偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/singular-learning-theory">Singular Learning Theory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mason's_theorem">Mason's theorem</a></li>

</ul>
</details>

**标签**: `#deep learning`, `#singular learning theory`, `#implicit bias`, `#neural networks`, `#mathematical theory`

---

<a id="item-21"></a>
## [LLM 心智理论出现晚且脆弱](https://arxiv.org/abs/2606.28524) ⭐️ 8.0/10

一项新研究追踪了 LLM 中心智状态推理的发展轨迹，表明错误信念任务表现出现在预训练后期，依赖于模型大小和训练量，并通过 SFT 和 DPO 等后训练干预得到最大改善。 这项工作为 LLM 中的心智理论提供了发展视角，解决了构念效度问题，并揭示了影响 AI 安全性和可解释性的脆弱性。 该研究使用 Olmo2 和 Pythia 模型套件，发现错误信念表现脆弱：即使在真实信念条件下，像“认为”这样的非事实动词也会增加错误信念归因，且情境模型在智能体知识状态方面表现出不一致。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 心智理论是将心理状态归因于他人的能力，错误信念任务是经典测试。近期研究表明 LLM 能通过此类任务，但构念效度问题仍存。本研究采用发展视角，追踪不同训练阶段的能力。

**标签**: `#LLMs`, `#theory of mind`, `#mentalizing`, `#AI safety`, `#cognitive science`

---

<a id="item-22"></a>
## [面向长上下文的轮次平均稀疏自编码器](https://arxiv.org/abs/2606.28548) ⭐️ 8.0/10

研究人员提出了轮次平均稀疏自编码器（SAE），用固定大小的特征向量表示整个人类或助手的轮次，从而在长模型转录中实现高效的特征发现和归因。 这解决了标准 SAE 的关键扩展限制（特征数量与上下文长度成正比），使得长上下文的可解释性在机制可解释性研究中变得实用。 轮次平均 SAE 重建整个轮次的平均模型激活而非单个 token 激活，论文表明，在 LLM 评判下，它们比逐 token 特征更完整地描述了轮次的高层特征。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 稀疏自编码器（SAE）是一种通过学习激活的稀疏表示从语言模型中提取可解释特征的常用工具。标准 SAE 对单个 token 激活进行操作，因此分析长对话或文档需要处理大量 token 级特征，扩展性差。

**标签**: `#sparse autoencoders`, `#interpretability`, `#mechanistic interpretability`, `#long-context`, `#language models`

---

<a id="item-23"></a>
## [静态斐波那契间隔在稀疏注意力中优于学习膨胀](https://arxiv.org/abs/2606.28560) ⭐️ 8.0/10

一篇新论文提出了一种静态的逐层交错斐波那契间隔的稀疏自注意力机制，其困惑度优于学习膨胀，并将推理延迟降低约五倍。 这一发现挑战了学习注意力模式的常见做法，提供了一种更简单、更高效的替代方案，并且能够外推到更长的序列，这对扩展 Transformer 模型至关重要。 该研究训练了 21 个 60M 参数的语言模型，比较了四种 alpha 设置方法；静态交错与学习型斐波那契注意力达到同等水平，且与基数无关，速度更快。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 稀疏注意力通过限制每个查询只关注一部分键来降低标准自注意力的二次复杂度。常见方法包括固定模式（如滑动窗口）或通过学习膨胀来学习模式。这项工作探索了一种静态斐波那契间隔模式，并带有一个逐层的标量 alpha 来压缩或扩展间隔。

**标签**: `#sparse attention`, `#transformer`, `#efficiency`, `#deep learning`, `#NLP`

---

<a id="item-24"></a>
## [SEAD：熵引导的在线策略蒸馏提升大模型训练效率](https://arxiv.org/abs/2606.28562) ⭐️ 8.0/10

SEAD 提出了一种基于熵引导的在线策略蒸馏方法，可选择性跳过约 50%的 token，将 KL 散度从正向退火到反向，并采用能力门控课程，在 OLMo-3 模型（7B-32B）的六个数学基准上平均准确率提升 4.8 个百分点。 该工作解决了在线策略蒸馏中一个关键的低效问题——忽略学生能力的统一监督，并在大模型上展示了显著提升，有望降低训练成本并提高 LLM 在数学推理任务中的表现。 SEAD 利用师生联合熵将 token 划分为不同区域，分别采用定制散度或零梯度；使用余弦调度从正向 KL 退火到反向 KL；以及能力门控课程从易到难引入提示；消融实验证实各组件之间存在超加性交互。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 在线策略蒸馏（OPD）是一种知识蒸馏技术，学生模型通过自身生成的 token 序列进行训练，不同于使用固定教师输出的离线蒸馏。在 OPD 中，教师监督质量取决于学生能力：不连贯的 rollout 会产生噪声梯度，而已掌握的 token 则产生冗余梯度。现有方法统一监督，在 token、阶段和提示三个尺度上浪费计算。SEAD 利用熵作为统一探针来检测这种依赖能力的退化，并相应调整监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/On-policy_distillation">On-policy distillation</a></li>

</ul>
</details>

**标签**: `#knowledge distillation`, `#on-policy distillation`, `#LLM training`, `#entropy`, `#curriculum learning`

---

<a id="item-25"></a>
## [用粒度校准验证 LLM 的构念测量](https://arxiv.org/abs/2606.28574) ⭐️ 8.0/10

本文提出了粒度校准方法，通过将构念分解为子句级组件，并用提取性证据逐一测试文本，来验证大型语言模型（LLM）是否正确地测量了理论构念，而不仅仅是可靠性。 这解决了当前 LLM 验证实践中的一个关键缺陷——常将可靠性与构念效度混为一谈，并提供了一个有理论基础的解决方案，有望提升 NLP 和社会科学研究的严谨性。 粒度校准使用显式的、源自理论的规则来组合组件结果，使推理过程透明，并能诊断是遗漏了某个组件还是误用了相邻构念。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 在社会科学和自然语言处理中，研究者常用 LLM 对文本进行理论构念（如情感、偏见）编码。通常检查的是可靠性（与人类标注者的一致性），但构念效度——即 LLM 是否真正测量了预期的概念——很少被评估。粒度校准旨在填补这一空白。

**标签**: `#LLM`, `#construct validity`, `#NLP`, `#measurement`, `#methodology`

---

<a id="item-26"></a>
## [探究手语模型的音系感知能力](https://arxiv.org/abs/2606.28667) ⭐️ 8.0/10

一项新研究探究了手语识别模型中的音系敏感性，发现基于姿态的模型擅长手形对比，而基于像素的模型更能捕捉位置变化。 这项工作解决了理解手语识别模型是学习抽象语言特征还是低级统计相关性的关键空白，对自然语言处理和语言学都有重要意义。 该研究使用最小对和人类行为数据评估了在美国手语上训练的模型，发现基于姿态的模型与人类感知相似性判断的相关性达到 r~0.49。

rss · arXiv - NLP · Jun 30, 04:00

**背景**: 手语是组合系统，意义通过组合手形、位置和运动等亚词汇音系参数产生。用于手语识别的深度学习模型在翻译基准上有所改进，但尚不清楚它们是否真正理解这些音系特征。

**标签**: `#sign language recognition`, `#phonological perception`, `#deep learning`, `#linguistics`, `#model interpretability`

---

<a id="item-27"></a>
## [RADIANT-PET：大语言模型与强化学习提升 PET/CT 病灶分割](https://arxiv.org/abs/2606.28392) ⭐️ 8.0/10

研究人员提出 RADIANT-PET 框架，将宽松分割模型与基于大语言模型的裁决和强化学习（GRPO）相结合，以提高 PET/CT 病灶分割的准确性。 该工作通过减少生理性示踪剂摄取造成的假阳性，解决了关键的临床挑战，有望改善肿瘤诊断和治疗规划。 该框架使用组相对策略优化（GRPO）微调本地大语言模型进行病灶级推理，并在提供放射学报告作为额外上下文时取得最大改进。

rss · arXiv - Computer Vision · Jun 30, 04:00

**背景**: PET/CT 是癌症诊断中常用的成像方式，但区分恶性病灶与良性示踪剂摄取很困难。传统分割模型在体素级别运行，常产生假阳性。RADIANT-PET 引入使用大语言模型的推理层来模拟临床解读。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Group_Relative_Policy_Optimization">Group Relative Policy Optimization</a></li>

</ul>
</details>

**标签**: `#medical imaging`, `#segmentation`, `#large language models`, `#reinforcement learning`, `#oncology`

---

<a id="item-28"></a>
## [双向自回归潜扩散模型用于磁流体动力学](https://arxiv.org/abs/2606.29620) ⭐️ 8.0/10

提出了一种新的双向自回归潜扩散模型，用于正向和逆向磁流体动力学（MHD），实现了自监督不确定性估计和非侵入式等离子体诊断。 这项工作推进了科学机器学习，提供了一种无需真实数据即可估计不确定性的方法，对可靠的等离子体诊断和聚变能研究至关重要。 该模型预测多个场（密度、压力、速度、磁场），并利用双向流一致性作为测试时不确定性和误差估计的自监督指标。

rss · arXiv - Data Science & Statistics · Jun 30, 04:00

**背景**: 磁流体动力学（MHD）研究导电流体与磁场的相互作用，应用于天体物理和聚变能。正向问题模拟 MHD 演化，逆向问题从观测推断初始或边界条件。潜扩散模型是在压缩潜空间中学习数据分布的生成模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1212.3447">Forward and inverse problems in fundamental and applied ... - arXiv</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/gamm.200790005">Forward and inverse problems in MHD: Numerical and experimental ...</a></li>
<li><a href="https://link.springer.com/article/10.1140/epjst/e2013-01793-3">Forward and inverse problems in fundamental and applied ...</a></li>

</ul>
</details>

**标签**: `#magnetohydrodynamics`, `#latent diffusion`, `#uncertainty estimation`, `#plasma diagnostics`, `#scientific machine learning`

---