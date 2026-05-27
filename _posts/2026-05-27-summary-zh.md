---
layout: default
title: "Horizon Summary: 2026-05-27 (ZH)"
date: 2026-05-27
lang: zh
---

> From 109 items, 40 important content pieces were selected

---

1. [AI 生成的安全报告压垮 curl 维护者](#item-1) ⭐️ 9.0/10
2. [LeJEPA 证明世界模型的线性可识别性](#item-2) ⭐️ 9.0/10
3. [Anthropic 和 OpenAI 实现产品市场契合](#item-3) ⭐️ 8.0/10
4. [Go 语言批准泛型方法提案](#item-4) ⭐️ 8.0/10
5. [私募股权对基本服务的收购](#item-5) ⭐️ 8.0/10
6. [烹饪知识压缩成 2MB 的食材原语](#item-6) ⭐️ 8.0/10
7. [面向 AI 代理的开源网络安全技能库](#item-7) ⭐️ 8.0/10
8. [微软发布 AI 代理治理工具包，保障安全可靠](#item-8) ⭐️ 8.0/10
9. [哈佛发布开源机器学习系统教科书](#item-9) ⭐️ 8.0/10
10. [新论文质疑 LLM 内省能力](#item-10) ⭐️ 8.0/10
11. [重新思考 AI 智能体记忆作为数据管理](#item-11) ⭐️ 8.0/10
12. [AgingBench：衡量 AI 智能体寿命可靠性的基准](#item-12) ⭐️ 8.0/10
13. [Anchor：防止智能体基准测试中的工件漂移](#item-13) ⭐️ 8.0/10
14. [OmniToM：通过显式信念建模测试大语言模型的心智理论新基准](#item-14) ⭐️ 8.0/10
15. [JobBench：与人类委托需求对齐的 AI 智能体基准](#item-15) ⭐️ 8.0/10
16. [GEM：用于最优 LLM 数据整理的几何熵混合方法](#item-16) ⭐️ 8.0/10
17. [约束税：衡量小语言模型结构化输出中的准确性损失](#item-17) ⭐️ 8.0/10
18. [AirCast-SR：公里级天气降尺度的基础模型](#item-18) ⭐️ 8.0/10
19. [神经贝叶斯顺序路由：不确定性感知推理框架](#item-19) ⭐️ 8.0/10
20. [TSFMAudit：首个用于时间序列基础模型数据污染审计的方法](#item-20) ⭐️ 8.0/10
21. [ARBITER 揭示 LLM 推理中多数投票的失败](#item-21) ⭐️ 8.0/10
22. [自验证蒸馏：大模型无需外部监督即可自我提升](#item-22) ⭐️ 8.0/10
23. [首个关于大模型预训练数据暴露的统一综述](#item-23) ⭐️ 8.0/10
24. [SPEAR：代码增强的智能提示优化器](#item-24) ⭐️ 8.0/10
25. [CroCo：无需语言特定数据的跨语言偏好调优](#item-25) ⭐️ 8.0/10
26. [RICE-PO：面向推理智能体的无评论家策略优化](#item-26) ⭐️ 8.0/10
27. [RAG 作为上下文梯度下降](#item-27) ⭐️ 8.0/10
28. [LLM 在结构化知识上产生幻觉的原因](#item-28) ⭐️ 8.0/10
29. [通过激活引导调整大语言模型文化价值观](#item-29) ⭐️ 8.0/10
30. [新基准揭示多轮文本到 SQL 中的记忆崩溃](#item-30) ⭐️ 8.0/10
31. [RoMo：大规模人体运动数据集与语义分类体系](#item-31) ⭐️ 8.0/10
32. [LongAV-Compass：分钟级音视频生成的统一基准](#item-32) ⭐️ 8.0/10
33. [VesselSim：无需专家标注的零样本 3D 血管分割](#item-33) ⭐️ 8.0/10
34. [学习具有未知单调链接的非线性因子模型](#item-34) ⭐️ 8.0/10
35. [用于比率型 CATE 的双重稳健元学习器](#item-35) ⭐️ 8.0/10
36. [随机控制理论打开 CART 随机森林黑箱](#item-36) ⭐️ 8.0/10
37. [Transformer 可通过上下文学习后验预测分布](#item-37) ⭐️ 8.0/10
38. [信噪比与样本量控制神经网络表征对齐](#item-38) ⭐️ 8.0/10
39. [因果表征学习提升推荐系统泛化能力](#item-39) ⭐️ 8.0/10
40. [抗衰老药物组合导致小鼠严重脑损伤](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI 生成的安全报告压垮 curl 维护者](https://simonwillison.net/2026/May/26/the-pressure/#atom-everything) ⭐️ 9.0/10

Daniel Stenberg 报告称，curl 项目收到的安全报告数量是 2024 年的 4-5 倍，每天超过一份，且所有报告都极其详细且可信，这主要归功于 AI 辅助的漏洞发现。 这种前所未有的涌入威胁到维护者的健康，并可能为其他开源项目树立先例，凸显了迫切需要新工具和流程来处理 AI 放大的安全报告。 尽管数量庞大，但发现的漏洞大多为低或中等严重性；curl 最后一个高严重性 CVE 是在 2023 年 10 月。Stenberg 指出，他的妻子首次对他工作与生活的平衡表示担忧。

rss · Simon Willison · May 26, 23:48

**背景**: curl 是一个广泛使用的开源命令行工具，用于通过 URL 传输数据，支持多种协议。开源维护者通常无偿工作，面临倦怠；2023 年的一项调查发现，58%的维护者因倦怠而考虑过或已经退出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CURL">cURL - Wikipedia</a></li>
<li><a href="https://curl.se/">curl</a></li>
<li><a href="https://www.sonarsource.com/blog/maintainer-burnout-is-real">Maintainer burnout is real. Almost 60% of maintainers have quit or...</a></li>

</ul>
</details>

**社区讨论**: Lobste.rs 上的讨论表达了对 Stenberg 的同情，并担忧 AI 对开源维护的广泛影响。一些评论者建议使用自动分类工具，而另一些人则争论在没有人工验证的情况下使用 AI 生成安全报告的伦理问题。

**标签**: `#open-source`, `#security`, `#AI`, `#curl`, `#maintainer burnout`

---

<a id="item-2"></a>
## [LeJEPA 证明世界模型的线性可识别性](https://arxiv.org/abs/2605.26379) ⭐️ 9.0/10

一篇新论文证明，结合对齐和高斯正则化的表示学习方法 LeJEPA，在平稳加性噪声转移下能够线性恢复潜在世界变量，确立了线性可识别性。 这一理论保证确保学习到的表示保留了世界的真实结构，从而在 AI 系统中实现可靠的规划和组合泛化。 高斯分布对可识别性而言是唯一最优的；证明利用谱分解，其中非线性被对齐惩罚。实验范围从二维到 1024 维潜在变量，包括基于像素的机器人控制。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: LeJEPA 是一种表示学习框架，通过对齐表示并应用高斯正则化，从高维观测中学习潜在变量。世界模型旨在捕捉环境的潜在动态，用于规划和推理。线性可识别性意味着学习到的表示是真实潜在变量的线性变换，从而保留其结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.26379v1">When Does LeJEPA Learn a World Model? - arXiv.org</a></li>
<li><a href="https://www.semanticscholar.org/paper/When-Does-LeJEPA-Learn-a-World-Model-Klindt-LeCun/36863b6dd7968bca4efb3f6e93cf06cb84568f0f">When Does LeJEPA Learn a World Model? - Semantic Scholar</a></li>
<li><a href="https://www.emergentmind.com/papers/2605.26379">LeJEPA: Conditions for World Model Identifiability</a></li>

</ul>
</details>

**标签**: `#representation learning`, `#world models`, `#identifiability`, `#LeJEPA`, `#theoretical machine learning`

---

<a id="item-3"></a>
## [Anthropic 和 OpenAI 实现产品市场契合](https://simonwillison.net/2026/May/27/product-market-fit/#atom-everything) ⭐️ 8.0/10

Simon Willison 认为，尽管存在成本和投资回报率的担忧，但 Anthropic 和 OpenAI 已实现产品市场契合，这体现在企业 API 支出增加和盈利传闻上。 这标志着 AI 行业的一个重大转变，领先实验室正从实验性工具转向盈利的企业产品，可能重塑软件开发和知识工作。 Anthropic 将其企业计划改为每月每席位 20 美元加 API 定价，OpenAI 在 2026 年 4 月也做出了类似调整，将 Codex 定价与 token 使用量挂钩。

rss · Simon Willison · May 27, 16:38 · [社区讨论](https://news.ycombinator.com/item?id=48296794)

**背景**: 产品市场契合（PMF）是指产品满足强大市场需求的程度，通常能带来有机增长和盈利。Simon Willison 是一位备受尊敬的开发者和博主，他根据自己的使用情况和报道的企业行为来分析行业趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Product-market_fit">Product-market fit - Wikipedia</a></li>
<li><a href="https://www.geeksforgeeks.org/product-management/what-is-product-market-fit-definition-importance-and-example/">Product-Market Fit : Definition , Importance and Example</a></li>
<li><a href="https://leanlm.ai/blog/llm-cost-optimization">LLM Cost Optimization: Why Enterprises Overspend 50–90% and...</a></li>

</ul>
</details>

**社区讨论**: 评论者就非编码用例是否真正存在 PMF 展开辩论，一些人指出盈利能力和 PMF 是不同的概念。其他人质疑高 token 支出的可持续性，而少数人则强调开源替代方案可能成为颠覆者。

**标签**: `#AI`, `#LLMs`, `#product-market fit`, `#Anthropic`, `#OpenAI`

---

<a id="item-4"></a>
## [Go 语言批准泛型方法提案](https://github.com/golang/go/issues/77273) ⭐️ 8.0/10

Go 团队正式接受了一项为语言添加泛型方法的提案，推翻了 FAQ 中长期坚持的立场。该提案由 Go 联合设计者 Robert Griesemer 撰写，现已进入实现阶段。 这填补了 Go 泛型实现中的一个重大空白，使开发者能够在结构体和接口上编写泛型方法。它将减少样板代码并提高代码复用性，尤其适用于数据访问和函数式编程模式。 该提案允许方法除了接收者类型上的类型参数外，还拥有自己的类型参数。实现细节仍在制定中，但预计该变更将向后兼容。

hackernews · f311a · May 27, 09:02 · [社区讨论](https://news.ycombinator.com/item?id=48291575)

**背景**: Go 在 1.18 版本中通过函数和类型的类型参数引入了泛型，但明确排除了泛型方法。Go FAQ 曾表示不需要泛型方法，并且会复杂化实现。该提案推翻了这一立场，回应了社区需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/golang/go/issues/77273">spec: generic methods for Go · Issue #77273 · golang/go</a></li>
<li><a href="https://www.theregister.com/2026/03/02/generic_methods_go/">Generic methods approved for Go, devs miss other features</a></li>
<li><a href="https://www.reddit.com/r/golang/comments/1rfmjbq/the_proposal_for_generic_methods_for_go_from/">r/golang on Reddit: The proposal for generic methods for Go, from Robert Griesemer himself, has been officially accepted</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户对长期存在的限制得到解决表示欣慰。一些评论者指出这最初被推迟为“现在不做，并非永远不做”，其他人则幽默地警告单子库的出现。少数反对者认为 Go 正在慢慢添加之前声称不必要的功能。

**标签**: `#Go`, `#generics`, `#programming languages`, `#software engineering`

---

<a id="item-5"></a>
## [私募股权对基本服务的收购](https://rubbishtalk.com/economy/how-private-equity-bought-americas-essential-services/) ⭐️ 8.0/10

一篇文章指出，私募股权对医疗、住房等基本服务的收购导致了系统性脆弱和道德沦丧，社区讨论强调了养老基金的作用和历史相似性。 这很重要，因为私募股权以利润为导向的模式可能削弱基本服务的可靠性和可负担性，影响数百万依赖这些服务的美国人，而养老基金对 PE 回报的依赖则造成了利益冲突。 文章批评私募股权优先考虑短期收益而非长期稳定，导致养老院和租赁住房等领域投资不足和风险增加。社区评论指出，养老基金是 PE 的主要投资者，寻求高回报以维持偿付能力。

hackernews · NoRagrets · May 27, 12:00 · [社区讨论](https://news.ycombinator.com/item?id=48292941)

**背景**: 私募股权公司通过借入资金收购公司，旨在提高盈利能力并在几年内出售获利。基本服务包括医疗、住房和公用事业，对日常生活至关重要。养老基金投资私募股权以获得高于传统资产的回报，但这可能使其面临更高风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pension_investment_in_private_equity">Pension investment in private equity - Wikipedia</a></li>
<li><a href="https://eqtgroup.com/thinq/Education/pension-funds-and-private-equity-how-they-work-together">How Pension Funds Work and Why They Invest In PE | EQT</a></li>
<li><a href="https://www.gsb.stanford.edu/insights/why-more-public-pensions-are-taking-chance-alternative-investments">Why More Public Pensions Are Taking a Chance on Alternative Investments | Stanford Graduate School of Business</a></li>

</ul>
</details>

**社区讨论**: 评论者对私募股权逐利动机的道德影响表示担忧，有人将其与历史上的克拉苏相提并论。其他人则指出，代表工人退休储蓄的养老基金助长了损害基本服务的 PE 模式，这具有讽刺意味。

**标签**: `#private equity`, `#economics`, `#public policy`, `#pensions`, `#essential services`

---

<a id="item-6"></a>
## [烹饪知识压缩成 2MB 的食材原语](https://arxiv.org/abs/2605.22391) ⭐️ 8.0/10

研究人员发表了一篇论文，将全球烹饪知识压缩成 1800 个食材原语，形成一个名为 Epicure 的 2MB 数据集，支持跨文化的风味搭配。 这个轻量级数据集可以在有限硬件上驱动高效的烹饪 AI 工具，普及烹饪知识的获取，并推动 AI 对文化饮食实践的理解。 该数据集来自 7 种语言的 11 个来源，但仅关注食材和风味搭配，不涉及烹饪方法或比例，社区评论指出了这一点。

hackernews · josefchen · May 27, 08:14 · [社区讨论](https://news.ycombinator.com/item?id=48291225)

**背景**: 风味搭配基于食材共享关键香气化合物时味道更佳的原理。此前如 Flavor Network 和 Foodpairing.com 等研究已探索这一概念，但 Epicure 将知识压缩成高效的 2MB 表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.foodpairing.com/the-science-behind-great-ingredient-pairings/">The Science behind great ingredient pairings - Foodpairing</a></li>
<li><a href="https://theculinarygene.com/ingredient-intelligence/all-of-human-cooking-compressed-into-2-megabytes/">All of human cooking compressed into... - The Culinary Gene</a></li>
<li><a href="https://1000worldrecipes.com/world-cuisines/all-of-human-cooking-compressed-into-2-megabytes/">All of human cooking compressed into... - 1000 World Recipes</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这项工作，但批评标题具有误导性，指出它只涵盖食材而非烹饪方法。一些人分享了相关资源，如公共领域食谱和旧版本的演示。

**标签**: `#machine learning`, `#food science`, `#data compression`, `#flavor pairing`

---

<a id="item-7"></a>
## [面向 AI 代理的开源网络安全技能库](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

一个新的开源库 Anthropic Cybersecurity Skills 为 AI 代理提供了 754 个结构化网络安全技能，映射到包括 MITRE ATT&CK 和 NIST CSF 2.0 在内的五个主要框架，并兼容 20 多个 AI 平台。 该库弥合了网络安全专业知识与 AI 代理之间的差距，支持在多个平台和框架上自动执行安全任务，可能加速 AI 在安全运维中的应用。 这些技能涵盖 26 个安全领域，遵循 agentskills.io 开放标准，并采用 Apache 2.0 许可证。该库兼容 Claude Code、GitHub Copilot、Codex CLI、Cursor、Gemini CLI 等 20 多个平台。

rss · GitHub Trending - Daily (All) · May 27, 23:12

**背景**: AI 代理越来越多地用于网络安全任务，但缺乏标准化的结构化技能定义。agentskills.io 标准提供了一种将能力定义为代理可读取的 markdown 文件的方式。MITRE ATT&CK 和 NIST CSF 是广泛采用的网络安全框架，而 MITRE ATLAS 和 D3FEND 则针对 AI 特定的威胁和防御。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/home">Agent Skills</a></li>
<li><a href="https://www.vectra.ai/topics/mitre-atlas">MITRE ATLAS : AI security framework with 16 tactics and 84 techniques</a></li>
<li><a href="https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/">MITRE ATLAS Framework 2026 - Guide to Securing AI Systems</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#MITRE ATT&CK`, `#open-source`, `#skills library`

---

<a id="item-8"></a>
## [微软发布 AI 代理治理工具包，保障安全可靠](https://github.com/microsoft/agent-governance-toolkit) ⭐️ 8.0/10

微软发布了 Agent Governance Toolkit，这是一个开源框架，为自主 AI 代理提供策略执行、零信任身份、执行沙箱和可靠性工程，覆盖 OWASP Agentic Top 10 全部 10 项。 随着 AI 代理在生产环境中广泛部署，安全与治理变得至关重要。该工具包应对 OWASP Agentic Top 10 风险，帮助开发者安全可靠地交付代理，对企业采用至关重要。 该工具包以 MIT 许可证在 GitHub 上公开预览，并提供 PyPI、npm 和 NuGet 包。它包含规范、快速入门指南以及托管在 GitHub Pages 上的完整文档。

rss · GitHub Trending - Python · May 27, 23:12

**背景**: OWASP Agentic Top 10 是一个框架，识别自主 AI 代理最严重的安全风险，例如身份和权限滥用。零信任架构假设被攻破并验证每个请求，而执行沙箱隔离代理活动以防止未授权访问。微软的工具包整合了这些概念，提供全面的治理解决方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://owasp.org/www-project-agentic-skills-top-10/">OWASP Agentic Skills Top 10 | OWASP Foundation</a></li>
<li><a href="https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/">OWASP Top 10 for Agentic Applications for 2026 - OWASP Gen AI...</a></li>
<li><a href="https://blogs.cisco.com/security/security-agentic-ai-how-cisco-brings-zero-trust-to-your-new-digital-workforce">Zero Trust for AI Agents – Identity, Access Control, and Behavioral Protection for the Agentic Era</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#governance`, `#security`, `#Microsoft`, `#OWASP`

---

<a id="item-9"></a>
## [哈佛发布开源机器学习系统教科书](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

哈佛大学在 GitHub 上发布了一本名为《机器学习系统：工程人工智能系统的原理与实践》的开源教科书，提供包括英语、中文、日语和韩语在内的多种语言版本。 这本教科书填补了机器学习教育中侧重于系统工程而非仅算法的空白，对于构建生产级 AI 系统的学生和从业者来说非常有价值。 该仓库不仅包含书籍内容，还包括幻灯片、实验和 TinyTorch 实现等补充材料，全部采用 CC-BY-NC-SA 4.0 许可协议。

rss · GitHub Trending - Python · May 27, 23:12

**背景**: 机器学习系统工程涵盖生产环境中 ML 模型的设计、部署和维护，包括数据管道、模型服务和监控。这本教科书旨在为这一新兴领域提供全面资源，而传统 ML 课程通常不涉及这些内容。

**标签**: `#machine learning`, `#systems`, `#textbook`, `#education`, `#open-source`

---

<a id="item-10"></a>
## [新论文质疑 LLM 内省能力](https://arxiv.org/abs/2605.26242) ⭐️ 8.0/10

一篇新的 arXiv 论文认为，当前关于 LLM 内省能力的证据尚不充分，表明模型可能依赖模式匹配而非真正的自我意识。作者提出了更严格的评估标准，并证明行为测试无法区分内部状态检测与异常检测。 这项工作挑战了 LLM 具备内省能力的日益流行的说法，这对 AI 安全性和可解释性具有重要意义。如果 LLM 不能可靠地报告其内部状态，那么关于 AI 系统自我意识的主张必须重新评估。 该论文重新审视了两种评估范式：检测内部状态被篡改以及从隐藏状态预测标签。在这两种情况下，控制实验表明模型的表现并不优于仅基于输入的分类器或随机水平，这表明先前的结果将内省与一般的异常检测或语义线索混为一谈。

rss · arXiv - AI · May 27, 04:00

**背景**: 大型语言模型（LLM）是在海量文本语料上训练的神经网络，用于生成和理解人类语言。在此背景下，内省指的是 LLM 访问和报告自身内部状态（如隐藏表示或处理错误）的能力。人类元认知研究探讨人们如何监控和评估自己的认知过程，为评估机器自我意识的主张提供了框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2409.16708v2">Performance and Metacognition Disconnect when Reasoning in...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#introspection`, `#metacognition`, `#AI interpretability`, `#evaluation`

---

<a id="item-11"></a>
## [重新思考 AI 智能体记忆作为数据管理](https://arxiv.org/abs/2605.26252) ⭐️ 8.0/10

一篇新论文认为，长期 AI 智能体记忆应被视为数据管理工作负载，而非单纯存储，并提出了受控演化记忆（GEM），包含四个状态级操作符和六个正确性条件。 这种重新定义解决了当前智能体记忆系统中的关键故障模式，如无节制增长和缺乏语义修订，可能从根本上改善 AI 智能体在长时间会话中学习、适应和保持上下文的方式。 GEM 用状态级操作符（摄入、修订、遗忘和检索）取代了记录级操作。作者证明，没有任何记录级系统能满足这六个正确性条件，并在属性图后端上实现了原型 MemState。

rss · arXiv - AI · May 27, 04:00

**背景**: 当前的 AI 智能体记忆系统将记忆视为静态存储，导致无控制增长和无法修订语义等故障。该论文提出了一种新范式，其中记忆正确性是整个状态轨迹的属性，而非单个记录。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26252">[2605.26252] Is Agent Memory a Database? Rethinking Data...</a></li>
<li><a href="https://thecodersblog.com/optimizing-agent-memory-the-failure-of-uniform-memory-allocation/">Optimizing Agent Memory : The Failure of... | The Coders Blog | Home</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#memory systems`, `#data management`, `#formalization`, `#arXiv`

---

<a id="item-12"></a>
## [AgingBench：衡量 AI 智能体寿命可靠性的基准](https://arxiv.org/abs/2605.26302) ⭐️ 8.0/10

一篇新论文提出了 AgingBench，这是一个纵向基准，用于衡量 AI 智能体随时间推移的性能退化，并诊断其老化机制，包括压缩老化、干扰老化、修订老化和维护老化。 当前的评估仅在第一天测试智能体，忽略了长期部署中的可靠性退化；AgingBench 填补了这一空白，使开发者能够设计具有持续可靠性的智能体。 AgingBench 利用时间依赖图和对偶反事实探针来诊断记忆流水线中写入、检索和利用阶段的故障，并在 7 个场景、14 个模型和约 400 次运行中进行了测试。

rss · arXiv - AI · May 27, 04:00

**背景**: 长期运行的 AI 智能体被部署为持久化系统，但评估方式仍如同刚初始化的模型。由于交互历史压缩、记忆增长、事实修订和维护，它们的有效状态随时间变化，使得可靠性成为整个智能体框架的寿命属性，而不仅仅是基础模型的快照属性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.26302v1">Your Agents Are Aging Too: Agent Lifespan Engineering for Deployed ...</a></li>
<li><a href="https://www.reddit.com/r/LLMDevs/comments/1tp9pi2/agents_appear_to_age_over_time_just_like_people/">Agents appear to age over time, just like people. We built a tool to figure ...</a></li>

</ul>
</details>

**社区讨论**: 在 Reddit 上，用户指出 AgingBench 揭示了令人惊讶的结果，例如随着上下文和轮次增加，Opus 4.7 的表现不如其前代和较小的 Sonnet 4.6，凸显了智能体老化的非平凡性。

**标签**: `#AI agents`, `#reliability`, `#benchmark`, `#deployment`, `#lifespan engineering`

---

<a id="item-13"></a>
## [Anchor：防止智能体基准测试中的工件漂移](https://arxiv.org/abs/2605.26321) ⭐️ 8.0/10

研究人员推出了 Anchor，这是一个从单一参数化规范中联合生成指令、环境、解决方案和验证器的流水线，以消除智能体基准测试中的不一致性。他们还发布了 ERP-Bench，这是一个使用 Anchor 构建的包含 300 个长周期企业任务的基准测试集。 工件漂移是智能体评估中的一个关键故障模式，会导致基准测试无法解决或奖励可被利用。Anchor 提供了一种原则性的方法来创建可审计、一致的评估环境，这对于推动企业自动化中的 AI 智能体至关重要。 Anchor 使用约束优化程序来形式化领域专家的规范，生成与测试框架无关的环境，其中奖励仅取决于最终状态的业务正确性。在 ERP-Bench 中，前沿模型在 26.1%的试验中满足了显式任务约束，但仅在 17.4%的试验中达到了完全最优解。

rss · arXiv - AI · May 27, 04:00

**背景**: AI 智能体基准测试常常遭受工件漂移问题，即指令、环境、预言机和验证器由松散耦合的过程创建，导致不一致性。约束优化程序（如 Google OR-Tools 中的程序）有助于找到满足所有给定约束的解决方案，使其适用于生成一致的任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.statsig.com/perspectives/model-drift-detection">Model drift detection: Identifying performance decay - Statsig</a></li>
<li><a href="https://developers.google.com/optimization/cp">Constraint Optimization | OR-Tools | Google for Developers</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark generation`, `#constraint optimization`, `#enterprise automation`, `#evaluation`

---

<a id="item-14"></a>
## [OmniToM：通过显式信念建模测试大语言模型的心智理论新基准](https://arxiv.org/abs/2605.26322) ⭐️ 8.0/10

研究人员推出了 OmniToM 基准，通过要求对叙事中所有角色的信念结构进行显式建模来评估大语言模型的心智理论，采用信念提取和标注的两阶段流程，包含 22,343 个标注的信念命题。 该基准通过直接测试大语言模型是否构建心理状态表征，解决了现有端点问答评估的关键局限，揭示了当前模型在特定角色信念追踪上的瓶颈。 OmniToM 基于 ToMBench 语料库中的 895 个故事构建，并使用人类校准的 LLM 辅助标注流程；它在零样本设置下通过两个阶段评估模型：信念提取和七维模式标注。

rss · arXiv - AI · May 27, 04:00

**背景**: 心智理论（ToM）是推断他人信念、意图等心理状态的能力。以往的大语言模型评估使用端点问答，可能无法捕捉模型是否真正理解心理状态表征。OmniToM 通过要求显式信念结构建模来直接评估这些表征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26322">OmniToM : Benchmarking Theory of Mind in LLMs via Explicit ...</a></li>
<li><a href="https://github.com/omnitom01/omnitom-benchmark-review">GitHub - omnitom01/ omnitom-benchmark -review</a></li>
<li><a href="https://huggingface.co/omnitom/datasets">omnitom ( omnitom ) - Hugging Face</a></li>

</ul>
</details>

**标签**: `#Theory of Mind`, `#LLM evaluation`, `#benchmark`, `#AI reasoning`, `#belief modeling`

---

<a id="item-15"></a>
## [JobBench：与人类委托需求对齐的 AI 智能体基准](https://arxiv.org/abs/2605.26329) ⭐️ 8.0/10

研究人员推出了 JobBench，这是一个评估 AI 智能体在 35 个职业中 130 个专家认定的委托任务上的基准，发现最佳模型（Claude Code 下的 Claude Opus 4.7）仅达到 45.9%的准确率。 JobBench 将焦点从经济替代转向人类赋能，衡量 AI 智能体在专业人士真正希望委托的任务上的表现。这可能会引导 AI 开发走向更有用的人机协作，而非工作替代。 每个任务包含一个由异构参考文件组成的工作空间，要求智能体在杂乱的信息流中进行推理，输出通过一个基于事实的评分链进行评估，每个任务平均有 35.6 个二元标准。该基准覆盖了 36 个模型，最强模型仅达到 45.9%。

rss · arXiv - AI · May 27, 04:00

**背景**: 当前的职业 AI 智能体基准主要基于经济价值，讲述的是替代故事。JobBench 则评估专家认为高优先级的委托工作流，根据人类需求赋能。Claude Opus 4.7 是 Anthropic 最新的旗舰模型，Claude Code 是其智能体编码工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.26329v1">JobBench: Aligning Agent Work With Human Will - arXiv</a></li>
<li><a href="https://action.ucsb.edu/news/university-washington-releases-jobbench-aligning-agent-work-human-desire">University of Washington releases "JobBench: Aligning Agent Work ...</a></li>
<li><a href="https://www.anthropic.com/news/claude-opus-4-7">Introducing Claude Opus 4.7 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#benchmark`, `#human-AI collaboration`, `#occupational tasks`, `#evaluation`

---

<a id="item-16"></a>
## [GEM：用于最优 LLM 数据整理的几何熵混合方法](https://arxiv.org/abs/2605.26121) ⭐️ 8.0/10

GEM 将 LLM 数据整理重新表述为超球面上的变分问题，利用几何熵混合发现平衡的语义结构，并在 1.1B 参数模型上取得了最先进的结果。 这解决了 LLM 预训练中的一个关键挑战，超越了人类分类法和欧几里得聚类，提供了一种有理论依据的方法，与现有混合策略集成时可将下游准确率提升高达 1.2%。 GEM 使用 Minorize-Maximize (MM)算法进行优化，并引入几何影响分数（GIS）用于可解释的类别生成，同时采用师生蒸馏技术扩展到网络规模的语料库。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: LLM 预训练的有效性越来越依赖于数据组成。传统的数据整理依赖于人类分类法（存在本体论错位）或欧几里得聚类（无法解决嵌入各向异性——嵌入在向量空间中占据狭窄锥形区域，限制语义多样性的现象）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.26121">GEM: Geometric Entropy Mixing for Optimal LLM Data Curation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Embedding_(machine_learning)">Embedding (machine learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#data curation`, `#geometric learning`, `#pre-training`, `#entropy`

---

<a id="item-17"></a>
## [约束税：衡量小语言模型结构化输出中的准确性损失](https://arxiv.org/abs/2605.26128) ⭐️ 8.0/10

一篇新论文引入了“约束税”概念，用于衡量结构化输出约束如何降低小语言模型的答案准确性，表明硬约束虽然能将模式有效性提升至 100%，但答案准确率却从 19.7%降至 11.0%。 这挑战了“结构化输出约束不影响答案质量”的常见假设，对依赖小模型实现成本和隐私优势的端侧 AI 及生产系统具有直接影响。 该研究在 Qwen2.5-0.5B、Qwen2.5-1.5B 和 SmolLM2-1.7B 上进行了 15000 次 GPU 生成测试，发现硬约束下错误有效模式输出从 49.5%增至 88.9%，且即使 3B 参数模型仍存在“直接模式税”。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: 结构化输出（如 JSON、工具调用）被广泛用于使 LLM 输出可被机器解析。小语言模型（参数低于 3B）因隐私和低延迟而常用于端侧部署，但其能力有限，难以同时满足模式约束和任务准确性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.10671">[2407.10671] Qwen2 Technical Report - arXiv.org</a></li>

</ul>
</details>

**标签**: `#LLM`, `#structured outputs`, `#small language models`, `#constraint tax`, `#AI reliability`

---

<a id="item-18"></a>
## [AirCast-SR：公里级天气降尺度的基础模型](https://arxiv.org/abs/2605.26130) ⭐️ 8.0/10

AirCast-SR 是一个基础模型，利用潜在一致性扩散将全球 AI 天气预报从 28 公里降尺度到 1 公里分辨率，同时生成 8 个地表变量的 67 小时预报。 该模型使公里级天气预报在计算上变得可行，惠及需要精细预报的能源、农业和灾害管理等行业。它还展示了零样本全球迁移能力，无需重新训练即可在不同地区使用。 该模型在潜在一致性模型（LCM）扩散框架内使用 3D U-Net，在美国本土使用 GraphCast 预报和 NOAA 的 AORC 数据集进行训练。它实现了接近零的偏差，并在 10-100 公里波长范围内保留了精细的大气结构。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: 传统的数值天气预报（NWP）模型在公里级计算成本高昂，限制了高分辨率预报的获取。像 GraphCast 这样的 AI 天气预报模型提供较粗分辨率（如 28 公里）的全球预报。AirCast-SR 使用基于扩散的超分辨率方法，将这些粗预报高效提升到 1 公里。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://registry.opendata.aws/noaa-nws-aorc/">NOAA Analysis of Record for Calibration (AORC) Dataset - Registry...</a></li>
<li><a href="https://aws.amazon.com/marketplace/pp/prodview-m2sp7gsk5ts6s">AWS Marketplace: NOAA Analysis of Record for Calibration ...</a></li>

</ul>
</details>

**标签**: `#weather forecasting`, `#super-resolution`, `#diffusion models`, `#foundation model`, `#AI for science`

---

<a id="item-19"></a>
## [神经贝叶斯顺序路由：不确定性感知推理框架](https://arxiv.org/abs/2605.26147) ⭐️ 8.0/10

研究人员提出了神经贝叶斯顺序路由（NBSR）框架，该框架将神经推理建模为主动证据积累，使用 Dirichlet-Categorical 共轭更新和 Gumbel-Softmax 路由实现硬性、路径依赖的计算。 NBSR 通过提供内置的不确定性量化、动态提前退出和资源理性推理，解决了标准神经网络的关键局限性，有望提高 AI 系统的效率和可解释性。 该框架使用 Dirichlet 信念状态，通过全局知识 oracle 的精确共轭加法更新，并采用 Gumbel-Softmax Straight-Through 估计器实现可微路由。在正证据提取下，它保证了总 Dirichlet 精度的单调增加和有界边际预测方差。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: 标准神经网络通常执行静态、密集的前向传播，没有显式的不确定性估计或动态计算。贝叶斯方法通过将参数视为分布来引入不确定性，但通常需要昂贵的采样。NBSR 结合了贝叶斯共轭更新与神经路由，实现了高效、不确定性感知的推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.26147">[PDF] Neural Bayesian Sequential Routing - arXiv</a></li>

</ul>
</details>

**标签**: `#Bayesian Neural Networks`, `#Uncertainty Quantification`, `#Neural Routing`, `#Probabilistic Inference`, `#Deep Learning`

---

<a id="item-20"></a>
## [TSFMAudit：首个用于时间序列基础模型数据污染审计的方法](https://arxiv.org/abs/2605.26161) ⭐️ 8.0/10

研究人员提出了 TSFMAudit，这是首个通过检测微调过程中异常高效的适应性来审计时间序列基础模型数据污染的方法。 这项工作填补了时间序列基础模型评估中的一个关键空白，因为数据污染可能导致过于乐观的性能估计，从而误导模型选择和部署。 TSFMAudit 在 6 个时间序列基础模型和 187 个数据集上进行了评估，使用有记录的训练源证据作为监督，并优于从 LLM 文献中改编的 10 个基线方法。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: 时间序列基础模型（TSFM）在大规模语料库上进行预训练，引发了评估数据集可能在预训练期间被暴露的担忧。与 NLP 不同，时间序列信号是连续且异质的，使得污染审计更具挑战性。TSFMAudit 利用探针适应动态：受污染的数据集在微调过程中表现出更快的损失下降和更小的骨干网络移动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26161">[2605.26161] TSFMAudit: Data Contamination Auditing in...</a></li>

</ul>
</details>

**标签**: `#time series`, `#foundation models`, `#data contamination`, `#auditing`, `#machine learning`

---

<a id="item-21"></a>
## [ARBITER 揭示 LLM 推理中多数投票的失败](https://arxiv.org/abs/2605.26172) ⭐️ 8.0/10

ARBITER 是一种新的模型无关方法，它表明 LLM 推理轨迹会聚集成盆地，导致多数投票偏向稳定但错误的答案，并引入保守的基于证据的修正来恢复准确性。 这揭示了 LLM 测试时采样中多数投票的一个根本缺陷——多数投票被广泛用于提高推理可靠性——并提供了一种实用的修正方法，无需外部数据即可提高准确性。 在 GSM8K 上使用 Qwen3-4B，ARBITER 在零外部信息的情况下恢复了部分 oracle 上限；在 Llama-3.1-8B 的 MMLU-HS-Math 上，它将准确率从约 78%提高到约 82%，恢复了约 22%的可用 oracle 上限。

rss · arXiv - Machine Learning · May 27, 04:00

**背景**: 大型语言模型（LLM）通常使用测试时采样生成多条推理路径，并通过多数投票选择答案，假设轨迹是独立的。然而，这项工作表明轨迹会聚集成推理盆地，使得多数投票选择最稳定的盆地而非最准确的盆地，从而导致错误多数失败。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26172">[2605.26172] ARBITER: Reasoning Trajectory Basins and Majority Vote ...</a></li>
<li><a href="https://arxiv.org/html/2605.26172v1">ARBITER: Reasoning Trajectory Basins and Majority Vote Failures in ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#reasoning`, `#test-time sampling`, `#majority vote`, `#AI safety`

---

<a id="item-22"></a>
## [自验证蒸馏：大模型无需外部监督即可自我提升](https://arxiv.org/abs/2605.26132) ⭐️ 8.0/10

研究人员提出自验证蒸馏（Self-Verified Distillation），一种后训练精炼方法：大模型对无标签提示生成候选解答，通过三级级联自验证检查进行过滤，并在自筛选数据上训练。该方法在数学、科学和编程领域的推理基准上取得了显著提升。 这项工作表明，大模型仅使用无标签提示即可自我改进，减少了对昂贵人工标注或外部工具的依赖。它提供了一条可扩展的后训练精炼路径，有望使模型改进更加普及，并降低专业推理任务的门槛。 三级级联包括循环一致性、事实性和正确性检查，只有通过所有阶段且评委一致同意的解答才被接受。在 Qwen3-4B 上，该方法在数学（AIME26 和 HMMT）上提升 pass@1 达+16.7 个百分点，科学（GPQA Diamond 和 HLE）上+11.1，编程（LCBv5 和 LCBv6）上+8.3。

rss · arXiv - NLP · May 27, 04:00

**背景**: 大语言模型通常通过监督微调或基于人类反馈的强化学习进行后训练，两者都需要昂贵的标注数据或人工标注。自训练方法试图利用模型自身的输出，但往往因缺乏外部验证而存在质量问题。自验证蒸馏通过使用模型自身作为验证器，采用结构化级联检查来解决这一问题，其灵感来源于 UQ 基准的多验证器方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26132">[2605.26132] Self - Verified Distillation : Your Language Model Is...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#self-training`, `#distillation`, `#reasoning`, `#self-verification`

---

<a id="item-23"></a>
## [首个关于大模型预训练数据暴露的统一综述](https://arxiv.org/abs/2605.26133) ⭐️ 8.0/10

该论文首次将数据污染和成员推断统一在大型语言模型预训练数据暴露（PDE）框架下进行综述。 PDE 对于确保评估完整性和保护隐私至关重要，这一统一视角有助于研究人员和实践者更好地理解和缓解相关风险。 该综述在不同暴露级别上形式化定义了 PDE，回顾了攻击与防御方法，综合了实证发现，并指出了开放挑战和未来方向。

rss · arXiv - NLP · May 27, 04:00

**背景**: 大型语言模型在庞大且往往不透明的数据集上训练，引发了对特定数据是否出现在训练集中的担忧。数据污染指测试数据泄露到训练集中，导致基准分数虚高；而成员推断攻击旨在判断特定记录是否用于训练，带来隐私风险。这两个领域传统上被分开研究，但本综述将它们统一在 PDE 概念下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.26133">[PDF] Pretraining Data Exposure in Large Language Models - arXiv</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leakage_(machine_learning)">Leakage (machine learning) - Wikipedia</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/">LLM04:2025 Data and Model Poisoning</a></li>

</ul>
</details>

**标签**: `#LLM`, `#data contamination`, `#membership inference`, `#privacy`, `#survey`

---

<a id="item-24"></a>
## [SPEAR：代码增强的智能提示优化器](https://arxiv.org/abs/2605.26275) ⭐️ 8.0/10

SPEAR 是一种新型智能提示优化器，它通过在沙盒环境中编写和执行 Python 代码来自主改进用于 LLM 作为评判任务的提示，并使用护栏确保单调改进。 这项工作将代码即行动范式引入自动提示工程，在工业级 LLM 作为评判任务上显著优于现有方法，展示了智能代码执行在提示优化中的强大能力。 SPEAR 使用四个工具：evaluate、python、set_prompt 和 finish，其中 Python 沙盒支持结构错误分析，如混淆矩阵和错误聚类。护栏包括指标回退时的自动回滚和可选的护栏指标下限。

rss · arXiv - NLP · May 27, 04:00

**背景**: 自动提示工程（APE）旨在重写提示以提高任务性能，但现有方法将优化器视为固定流水线。SPEAR 将 CodeAct 范式（将代码视为动作）移植到 APE，允许优化器自由编写和执行 Python 进行分析。

**标签**: `#prompt engineering`, `#LLM optimization`, `#agentic systems`, `#code execution`, `#NLP`

---

<a id="item-25"></a>
## [CroCo：无需语言特定数据的跨语言偏好调优](https://arxiv.org/abs/2605.26293) ⭐️ 8.0/10

研究人员提出 CroCo 方法，通过使用自生成响应和仅基于英语的奖励模型，将对比偏好调优扩展到多种语言，实现了无需语言特定偏好数据的跨语言迁移。 这项工作通过消除每种语言中偏好标注的需求，显著降低了多语言大语言模型对齐的成本，对低资源语言和实际部署尤其有价值。 CroCo 需要在线策略数据；离线策略响应会降低收益，且在线偏好优化并未优于离线变体。该方法在 EuroLLM-9B 的结构化任务上提升了 6/7 种语言的性能，在 Aya-3B 上提升了 4/7 种语言，并在 11 种语言的开放式生成任务中胜出。

rss · arXiv - NLP · May 27, 04:00

**背景**: 偏好调优通过奖励模型和偏好数据使大语言模型输出与人类价值观对齐。对比偏好调优通过基于奖励分数对比自生成响应来改进这一过程。CroCo 将其扩展到多语言场景，表明仅使用英语的奖励模型也能有效对其他语言的响应进行排序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26293">[2605.26293] CroCo : Cross - Lingual Contrastive Preference Tuning ...</a></li>

</ul>
</details>

**标签**: `#multilingual NLP`, `#preference tuning`, `#LLM alignment`, `#cross-lingual transfer`, `#contrastive learning`

---

<a id="item-26"></a>
## [RICE-PO：面向推理智能体的无评论家策略优化](https://arxiv.org/abs/2605.26352) ⭐️ 8.0/10

研究人员提出了 RICE-PO，一种无评论家策略优化框架，将检索交互转化为局部学习信号，以解决训练推理智能体中的信用分配问题。在 BRIGHT 和 BEIR 基准测试中，它优于基于提示的智能体和基于组的强化学习基线。 这项工作解决了训练检索推理智能体的一个基本挑战：潜在推理步骤的信用分配。通过消除对评论家网络的需求并直接使用检索指标，RICE-PO 为交互式检索系统提供了一种更高效、可扩展的训练方法。 RICE-PO 选择高不确定性的可执行动作作为锚点，使用检索指标评估局部反事实分支，并且仅在推理到动作的影响强且未来残差效应稳定时，将信用传播到潜在推理步骤。它在相同检索器设置下在 BRIGHT 和 BEIR 基准上进行了测试。

rss · arXiv - NLP · May 27, 04:00

**背景**: 训练检索推理智能体涉及信用分配：像查询这样的可执行动作可以直接评估，但潜在推理步骤无法直接观察。传统的强化学习方法通常使用评论家网络来估计优势，但这可能复杂且不稳定。RICE-PO 是一种无评论家方法，利用智能体-环境交互的结构提供局部监督。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2501.03262">REINFORCE++: Stabilizing Critic-Free Policy Optimization with ...</a></li>
<li><a href="https://neurips.cc/virtual/2025/131906">Learning Without Critics? Revisiting GRPO in Classical Reinforcement ...</a></li>

</ul>
</details>

**标签**: `#retrieval`, `#reasoning agents`, `#reinforcement learning`, `#credit assignment`, `#policy optimization`

---

<a id="item-27"></a>
## [RAG 作为上下文梯度下降](https://arxiv.org/abs/2605.26356) ⭐️ 8.0/10

一篇新论文证明，线性自注意力层可以在统一的 RAG 目标上实现一步梯度下降，从而在特定条件下证明检索增强预测与上下文优化在数学上是等价的。 这一理论联系为理解检索文档如何不仅作为静态证据、而且作为模型适应信号提供了原则性框架，有望带来更高效、更可解释的 RAG 系统。 该论文涵盖了基于投影和基于点积的检索接口，在线性和非线性扩展下测试了对应关系，并提出了一种轻量级的前向更新方法，在七个 QA 基准测试、两个检索器和两个冻结 LLM 上提升了性能。

rss · arXiv - NLP · May 27, 04:00

**背景**: 大型语言模型中的上下文学习已被证明与线性自注意力中的隐式梯度下降有关，即模型可以根据上下文更新其行为而无需显式改变权重。检索增强生成（RAG）结合了检索器和生成器以融入外部知识，但传统上将检索到的文档视为固定上下文而非适应信号。这项工作通过证明 RAG 可以被视为一个上下文优化过程，将这两个概念联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.26356">In-Context Optimization for Retrieval -Augmented Generation...</a></li>

</ul>
</details>

**标签**: `#retrieval-augmented generation`, `#in-context learning`, `#gradient descent`, `#self-attention`, `#optimization`

---

<a id="item-28"></a>
## [LLM 在结构化知识上产生幻觉的原因](https://arxiv.org/abs/2605.26362) ⭐️ 8.0/10

该论文对 LLM 在线性化结构化知识推理时产生幻觉的机制进行了分析，指出注意力集中在捷径上以及前馈层中语义基础失败是主要原因。 理解这些内部动态有助于开发更好的幻觉检测和缓解策略，提高 LLM 在知识密集型任务中的可靠性。 研究发现注意力不成比例地集中在类似捷径的结构线索上，而不是分布在完整上下文中；前馈表示未能将提供的知识接地，导致模型退回到参数记忆。

rss · arXiv - NLP · May 27, 04:00

**背景**: LLM 通常依赖图、表格等结构化外部知识，这些知识被线性化为序列令牌。即使知识充足，幻觉仍会发生，这项工作揭示了这些失败背后的系统性内部动态。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/Transformer-Feed-Forward-Layers-Are-Key-Value-Geva-Schuster/4a54d58a4b20e4f3af25cea3c188a12082a95e02">[PDF] Transformer Feed-Forward Layers Are Key-Value Memories</a></li>

</ul>
</details>

**标签**: `#LLM`, `#hallucination`, `#structured knowledge`, `#mechanistic analysis`, `#reasoning`

---

<a id="item-29"></a>
## [通过激活引导调整大语言模型文化价值观](https://arxiv.org/abs/2605.26365) ⭐️ 8.0/10

研究人员提出一种框架，通过基于场景的探测和激活引导，在不重新训练的情况下映射和调整大语言模型的文化价值观。 这项工作解决了大语言模型中文化同质化的关键问题，提供了一种计算高效的文化对齐方法，有望提升 AI 在全球部署中的安全性和公平性。 该框架使用 300 个情境困境提取潜在 token 概率，绕过安全对齐的拒绝响应，并在前向传播过程中应用激活引导来调整文化维度。

rss · arXiv - NLP · May 27, 04:00

**背景**: 大语言模型常因训练数据偏差而表现出同质化的文化视角。世界价值观调查（WVS）是一个全球性研究项目，用于跨文化映射人类价值观。激活引导是一种在推理过程中调整内部表示以修改模型行为的技术，无需重新训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_Values_Survey">World Values Survey</a></li>

</ul>
</details>

**标签**: `#LLM`, `#cultural alignment`, `#activation steering`, `#AI safety`, `#value alignment`

---

<a id="item-30"></a>
## [新基准揭示多轮文本到 SQL 中的记忆崩溃](https://arxiv.org/abs/2605.26394) ⭐️ 8.0/10

研究人员推出了 EnterpriseMem-Bench，这是一个包含 300 个会话和 1400 轮的多轮文本到 SQL 基准，并在五种记忆条件下评估了五个前沿模型，发现无状态方法在第三轮时准确率降至零。 这项工作揭示了当前 LLM 在多轮企业分析中的关键局限性，表明记忆架构对于持续性能至关重要，并为未来研究提供了标准化基准。 该基准涵盖三个企业领域（BIRD 金融、SEC EDGAR、Northwind），具有确定性真实标签和每轮记忆关键注释。引入了记忆收益分数（MBS）作为每轮诊断指标。

rss · arXiv - NLP · May 27, 04:00

**背景**: 多轮文本到 SQL 涉及在多个对话轮次中生成 SQL 查询，要求模型保持上下文。先前的工作集中在单轮设置上，未解决记忆挑战。该基准系统研究了记忆架构，包括工作记忆、情景检索和语义增强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.26394">[2605.26394] Memory Architectures for Multi-Turn Text-to-SQL - arXiv</a></li>
<li><a href="https://arxiv.org/html/2605.26394v1">Memory Architectures for Multi-Turn Text-to-SQL: A Benchmark ... - arXiv</a></li>

</ul>
</details>

**标签**: `#Text-to-SQL`, `#memory architectures`, `#benchmark`, `#multi-turn`, `#LLM evaluation`

---

<a id="item-31"></a>
## [RoMo：大规模人体运动数据集与语义分类体系](https://arxiv.org/abs/2605.26241) ⭐️ 8.0/10

研究人员推出了 RoMo，这是一个大规模、精心策划的野外人体运动数据集，具有新颖的三级语义分类体系，以及基于分类意识的过滤流程和每个序列的详细描述。 该数据集包含一个基于分类意识的过滤流程，可积极去除静态和易出现伪影的序列，每个序列都附有详细描述。层次化分类体系支持按类别评估，发布的 Motion Toolbox 标准化了指标、数据转换和可视化。

rss · arXiv - Computer Vision · May 27, 04:00

**背景**: 人体运动生成一直受限于缺乏大规模高质量数据集。现有选择要么是小规模高保真但多样性有限的运动捕捉数据集，要么是常包含静态或低质量序列的大规模野外集合。语义分类体系将运动组织成有意义的类别，有助于更好的评估和模型训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Semantics">Semantics - Wikipedia</a></li>

</ul>
</details>

**标签**: `#human motion generation`, `#dataset`, `#semantic taxonomy`, `#3D human motion`, `#generative modeling`

---

<a id="item-32"></a>
## [LongAV-Compass：分钟级音视频生成的统一基准](https://arxiv.org/abs/2605.26244) ⭐️ 8.0/10

该基准填补了长时音视频生成评估的关键空白，因为现有基准仅关注短视频且缺乏跨模态统一评估。它提供了诊断工具，用于分析身份一致性、叙事连贯性和音视频对齐在长时间尺度上的退化情况，从而指导未来模型改进。 该基准评估超过 20 个细粒度维度，包括段内质量、跨段一致性、全局叙事连贯性、语义对齐和音视频同步，使用 DINO-v2、ArcFace、CLIP 和 ImageBind 等指标。实验涵盖 11 个代表性模型，并进行了人工对齐验证。

rss · arXiv - Computer Vision · May 27, 04:00

**背景**: 音视频生成已从短视频快速发展到分钟级内容，但评估方法仍局限于短时设置。现有基准主要关注 5-10 秒的文本条件生成，很少支持跨文本、图像和视频条件的统一评估。LongAV-Compass 通过提供分钟级生成的系统基准填补了这一空白。

**标签**: `#audio-visual generation`, `#benchmark`, `#multimodal`, `#long-form evaluation`, `#MLLM`

---

<a id="item-33"></a>
## [VesselSim：无需专家标注的零样本 3D 血管分割](https://arxiv.org/abs/2605.26277) ⭐️ 8.0/10

VesselSim 提出了一个两阶段框架，首先生成 16,500 个合成 3D 血管造影体积，并仅在此数据上训练 3D U-Net，然后通过测试时自适应来弥合与真实临床扫描的域差距。 该工作消除了 3D 血管分割中对专家标注的需求，这是医学图像分析中的一个主要瓶颈，并在多个数据集的零样本设置中取得了与最先进基础模型相竞争的性能。 合成数据生成使用随机、几何驱动的血管模拟，包括递归分支、曲率控制生长和碰撞感知拓扑，随后进行域随机化强度合成。测试时自适应采用自监督掩码重建解码器，无需先验域知识即可适应未见过的临床扫描。

rss · arXiv - Computer Vision · May 27, 04:00

**背景**: 血管分割对于诊断血管疾病和手术规划至关重要，但深度学习模型通常需要大量手动标注的医学图像，这些图像获取成本高且耗时。合成数据生成和测试时自适应是减少这种依赖性的新兴技术。VesselSim 结合了这两种技术以实现零样本分割。

**标签**: `#medical image analysis`, `#deep learning`, `#synthetic data`, `#segmentation`, `#domain adaptation`

---

<a id="item-34"></a>
## [学习具有未知单调链接的非线性因子模型](https://arxiv.org/abs/2605.26271) ⭐️ 8.0/10

提出了一种投影块坐标下降算法，用于从不完整且有噪声的数据中学习具有未知单调链接函数的非线性因子模型，并提供了收敛保证。 这项工作将经典线性因子模型扩展到广泛的非线性领域，以理论保证解决了一个具有挑战性且尚未充分探索的问题，对机器学习和统计学具有重要意义。 链接函数在再生核希尔伯特空间（RKHS）中建模，以实现灵活的非参数建模同时保持可识别性，算法使用显式正则化来解决尺度和旋转模糊性。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: 因子模型是统计工具，用较少的未观测潜在因子来解释观测变量。线性因子模型假设因子与观测之间存在线性关系，但许多现实关系是非线性的。本文引入了一种非线性因子模型，其中链接函数未知但单调，并使用 RKHS 对链接函数进行非参数建模。

**标签**: `#nonlinear factor models`, `#RKHS`, `#block coordinate descent`, `#nonparametric statistics`, `#low-rank matrix recovery`

---

<a id="item-35"></a>
## [用于比率型 CATE 的双重稳健元学习器](https://arxiv.org/abs/2605.26288) ⭐️ 8.0/10

本文提出了 Q-Learner，一种新颖的元学习器，它将基于比率的条件平均处理效应（CATE）分解为两个优势比的乘积，并为 S/T 型和 Q 型学习器提出了双重稳健增强方法。 在医学和营销等领域，基于比率的 CATE 是自然的估计目标，但现有估计器缺乏稳健性；这项工作提供了有理论基础的稳健估计器，在低转化率和混杂观测数据场景中优于其他方法。 Q-Learner 将二元结果的比率 CATE 估计简化为两个倾向性分类任务，避免了不平衡回归。针对 S/T 型和 Q 型估计器的双重稳健（DR）学习器在倾向性或结果模型之一正确设定时实现稳健性。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: 条件平均处理效应（CATE）衡量处理效果如何随协变量变化。基于比率的 CATE 定义为处理组与对照组期望结果的比值，适用于效应为乘法关系的情况。双重稳健估计结合了倾向性得分和结果建模，使得只要其中一个模型正确，估计量就保持一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://matheusfacure.github.io/python-causality-handbook/12-Doubly-Robust-Estimation.html">12 - Doubly Robust Estimation — Causal Inference for the Brave...</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#meta-learning`, `#treatment effects`, `#doubly robust estimation`, `#machine learning`

---

<a id="item-36"></a>
## [随机控制理论打开 CART 随机森林黑箱](https://arxiv.org/abs/2605.26675) ⭐️ 8.0/10

该论文提出了 CART-ROSA，一个将 CART 随机森林中的特征子采样建模为随机机会集的随机控制框架，从而能够显式分析集成风险。 这项工作弥合了理解 CART 随机森林工作机制的根本性差距，可能为实践中广泛使用的集成方法带来更好的设计和理论保证。 该框架分离了两个设计杠杆：特征子采样带来的信息机会率和分裂策略的收缩强度，并表明 CART 策略局部稳定但对森林目标全局次优。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: CART 随机森林是一种集成方法，结合了许多基于随机特征子集构建的决策树。尽管经验上成功，但由于算法复杂性，其内部动态一直难以理解。本文应用随机控制理论（一种在不确定性下进行决策的框架）将顺序分裂过程建模为受控随机过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stochastic_process">Stochastic process - Wikipedia</a></li>

</ul>
</details>

**标签**: `#random forests`, `#stochastic control`, `#ensemble methods`, `#machine learning theory`, `#CART`

---

<a id="item-37"></a>
## [Transformer 可通过上下文学习后验预测分布](https://arxiv.org/abs/2605.26713) ⭐️ 8.0/10

一篇新论文证明，Transformer 可以通过上下文梯度下降近似高斯过程回归中的后验预测分布，并给出了依赖于注意力深度和分箱分辨率的严格误差界。 这项工作为先验数据拟合网络（PFN）提供了理论基础，解释了 Transformer 如何学习超越点预测的分布，这对贝叶斯深度学习和不确定性估计至关重要。 Transformer 通过实现梯度下降来计算后验均值和方差，然后应用非线性映射生成后验预测分布的分箱概率。误差界随注意力深度和分箱分辨率变化，归一化在超出预训练样本量的外推中起关键作用。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: 先验数据拟合网络（PFN）是一类通过从先验分布采样数据训练 Transformer 来近似贝叶斯推理的模型，从而实现上下文后验预测。高斯过程是一种流行的贝叶斯非参数模型，提供函数上的分布。本文通过证明 Transformer 可以模拟高斯过程回归的梯度下降，弥合了 PFN 经验成功与理论理解之间的差距。

**标签**: `#transformers`, `#in-context learning`, `#Bayesian inference`, `#Gaussian processes`, `#theory`

---

<a id="item-38"></a>
## [信噪比与样本量控制神经网络表征对齐](https://arxiv.org/abs/2605.26973) ⭐️ 8.0/10

一篇新论文表明，信噪比（SNR）和训练样本量控制着神经网络中的表征对齐，对齐程度随 SNR 单调变化，随样本量非单调变化，且在不同设置下均成立。 这项工作为表征对齐提供了新的理论见解，表征对齐是迁移学习和模型可解释性的关键现象，并揭示了对齐与泛化性能解耦，这对训练策略和理解神经表征具有重要意义。 这些发现在线性和非线性网络、回归和分类任务以及合成和真实数据中均成立，对齐程度在插值阈值附近最小。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: 表征对齐是指在不同神经网络中，针对相似任务训练出的潜在表示的结构相似性。研究它通常是为了理解迁移学习和模型比较。信噪比（SNR）衡量信号功率与噪声功率之比，样本量指训练样本的数量。本文使用简单的线性网络推导出解析结果，然后在更复杂的设置中验证它们。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2112.07806">[2112.07806] Representation Alignment in Neural Networks</a></li>
<li><a href="https://www.emergentmind.com/topics/representational-alignment">Representational Alignment : Methods & Metrics</a></li>

</ul>
</details>

**标签**: `#neural networks`, `#representational alignment`, `#signal-to-noise ratio`, `#sample size`, `#theoretical analysis`

---

<a id="item-39"></a>
## [因果表征学习提升推荐系统泛化能力](https://arxiv.org/abs/2605.27043) ⭐️ 8.0/10

研究人员提出了一种因果表征学习方法，包含信息论解缠准则和可处理的变分下界，以解决推荐系统中的分布偏移问题。该方法通过 Spotify 上数百万用户的 A/B 测试验证，在听众参与度上取得了显著的在线提升。 这项工作直接解决了推荐系统中的根本性分布偏移问题，该问题常导致离线指标无法准确预测在线性能。通过提供一个实用的因果解缠目标，该目标可与现有模型配合使用且不增加推理成本，有望提升许多已部署推荐系统的可靠性和有效性。 该方法的目标是在分布偏移下实现更好的泛化，而非完全识别所有潜在因果因素，因此仅需混淆日志即可实用。它适用于任何标准监督模型，并在 Spotify 的个性化播放列表生成生产排序器、KuaiRand 数据集以及一个合成基准上进行了测试。

rss · arXiv - Data Science & Statistics · May 27, 04:00

**背景**: 推荐系统通常在受部署策略、过去用户行为和平台过滤混淆的交互日志上训练，导致训练与服务之间的分布偏移。因果表征学习（CRL）旨在学习捕捉高层因果变量及其关系的表征，从而改善分布外泛化。本文引入了一个信息论解缠准则，用于隔离因果成分，无需完全因果识别即可实现更好的泛化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2102.11107">[2102.11107] Towards Causal Representation Learning - arXiv</a></li>

</ul>
</details>

**标签**: `#causal representation learning`, `#recommender systems`, `#distribution shift`, `#machine learning`, `#information theory`

---

<a id="item-40"></a>
## [抗衰老药物组合导致小鼠严重脑损伤](https://www.sciencedaily.com/releases/2026/05/260526022024.htm) ⭐️ 8.0/10

根据《科学日报》发表的一项新研究，一种被广泛探索的抗衰老药物组合在小鼠中导致严重的髓鞘丢失和脑损伤，类似于多发性硬化症的病理变化。 这一发现挑战了流行抗衰老药物组合的安全性，并意外地为多发性硬化症研究提供了新的动物模型，可能改变这两个领域的研究方向。 该药物组合诱导了与“化疗脑”相关的变化，并造成了类似于多发性硬化症的髓鞘损伤，为理解和修复该疾病提供了新线索。

rss · ScienceDaily Health · May 27, 12:23

**背景**: 髓鞘是神经细胞周围的保护鞘，能加速信号传递；其丢失是多发性硬化症的特征。“化疗脑”指化疗患者常经历的认知模糊。这项研究意外地将一种抗衰老药物组合与这两种情况联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://my.clevelandclinic.org/health/body/22974-myelin-sheath">Myelin Sheath: What It Is, Purpose & Function - Cleveland Clinic</a></li>
<li><a href="https://www.mayoclinic.org/diseases-conditions/chemo-brain/symptoms-causes/syc-20351060">Chemo brain - Symptoms and causes - Mayo Clinic</a></li>

</ul>
</details>

**标签**: `#anti-aging`, `#neuroscience`, `#multiple sclerosis`, `#drug safety`, `#preclinical research`

---