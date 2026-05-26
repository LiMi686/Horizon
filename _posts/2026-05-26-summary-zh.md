---
layout: default
title: "Horizon Summary: 2026-05-26 (ZH)"
date: 2026-05-26
lang: zh
---

> From 107 items, 41 important content pieces were selected

---

1. [DynIP：支持 RFC 2136、IPv6 和 DNSSEC 的现代动态 DNS 服务](#item-1) ⭐️ 8.0/10
2. [荷兰阻止美国收购数字身份提供商](#item-2) ⭐️ 8.0/10
3. [微软 Copilot Cowork 漏洞导致数据泄露](#item-3) ⭐️ 8.0/10
4. [教宗良十四世关于人工智能的通谕](#item-4) ⭐️ 8.0/10
5. [面向 AI 代理的开源网络安全技能库，包含 754 项技能](#item-5) ⭐️ 8.0/10
6. [CodeGraph：为 AI 编程助手预构建的代码知识图谱](#item-6) ⭐️ 8.0/10
7. [微软发布 AI 代理治理工具包](#item-7) ⭐️ 8.0/10
8. [用视觉语言模型复现 Picbreeder 以研究开放性](#item-8) ⭐️ 8.0/10
9. [LLM 置信度校准研究揭示难易效应](#item-9) ⭐️ 8.0/10
10. [LLM 推理冗余量化：61-93%步骤可截断](#item-10) ⭐️ 8.0/10
11. [Context：通过沙盒程序实现主动式 AI 代理](#item-11) ⭐️ 8.0/10
12. [优化 LLM 代理工作流中的延迟-可靠性-成本](#item-12) ⭐️ 8.0/10
13. [BODHI：基于 LLM 的操作系统内核规约生成达到 96.73% Pass@1](#item-13) ⭐️ 8.0/10
14. [LLM 在临床压力下表现出信念不稳定](#item-14) ⭐️ 8.0/10
15. [运行时执行模型强制执行重构权威](#item-15) ⭐️ 8.0/10
16. [算法度量：算法反馈下的预测](#item-16) ⭐️ 8.0/10
17. [可验证 Transformer：为电路解释提供形式化证明](#item-17) ⭐️ 8.0/10
18. [IRNO：迭代精化神经算子](#item-18) ⭐️ 8.0/10
19. [隐藏状态隐私存在“空中间”](#item-19) ⭐️ 8.0/10
20. [LLM-AutoSciLab：利用大语言模型进行闭环科学发现](#item-20) ⭐️ 8.0/10
21. [InteractBind：结合位点定位基准](#item-21) ⭐️ 8.0/10
22. [Raon-Speech：9B 参数语音语言模型在 42 项基准测试中达到最优](#item-22) ⭐️ 8.0/10
23. [多角色辩论系统用于假设生成](#item-23) ⭐️ 8.0/10
24. [因果框架揭示 LLM 评判者的合理化偏差](#item-24) ⭐️ 8.0/10
25. [AERIC：用于隐式有害内容的预期隐藏状态监控器](#item-25) ⭐️ 8.0/10
26. [DPO 将音频大模型中的语码转换错误减少 89.6%](#item-26) ⭐️ 8.0/10
27. [GazeWorld：将放射科医生注视轨迹作为医学 AI 世界模型](#item-27) ⭐️ 8.0/10
28. [Nano World Models：极简视频预测代码库](#item-28) ⭐️ 8.0/10
29. [EEG 以 86%准确率解码视觉刺激](#item-29) ⭐️ 8.0/10
30. [IVR-R1：多模态大语言模型的迭代视觉接地推理强化学习](#item-30) ⭐️ 8.0/10
31. [DIDR：通过扩散奖励实现原理性的一步生成器强化学习](#item-31) ⭐️ 8.0/10
32. [ActQuant：面向 VLA 模型的亚 4 位量化方法](#item-32) ⭐️ 8.0/10
33. [因果性作为人工智能的统计良知](#item-33) ⭐️ 8.0/10
34. [MEDAL：将流形嵌入蒸馏到自编码器中](#item-34) ⭐️ 8.0/10
35. [多校准提升的统一理论](#item-35) ⭐️ 8.0/10
36. [神经奖励模型学习策略优化的特征](#item-36) ⭐️ 8.0/10
37. [强化学习中的反事实安全框架](#item-37) ⭐️ 8.0/10
38. [自主 AI 采用面临组织准备不足的鸿沟](#item-38) ⭐️ 8.0/10
39. [AI 悄然侵蚀入门级工作，危机迫在眉睫](#item-39) ⭐️ 8.0/10
40. [鼻喷雾剂逆转小鼠大脑衰老](#item-40) ⭐️ 8.0/10
41. [南加州大学科学家发现阿尔茨海默病隐藏触发因素及潜在药物靶点](#item-41) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DynIP：支持 RFC 2136、IPv6 和 DNSSEC 的现代动态 DNS 服务](https://dynip.dev/) ⭐️ 8.0/10

DynIP 是一项新的动态 DNS 服务，支持 RFC 2136/TSIG 更新、IPv6 和 DNSSEC，允许 FortiGate 和 MikroTik 等设备无需自定义客户端即可原生更新 DNS 记录。 它填补了现有 DDNS 服务的空白，这些服务通常依赖专有的仅 HTTP 协议，且缺乏 IPv6 和 DNSSEC 支持，使其适用于现代网络和设备。 该服务将 RFC 2136 DNS UPDATE 与 TSIG 认证作为一等路径，并为无法使用 DNS UPDATE 的设备提供 HTTP API。它支持端到端 IPv6 和 DNSSEC，以实现安全的 DNS 更新。

hackernews · dynip · May 26, 07:35 · [社区讨论](https://news.ycombinator.com/item?id=48276363)

**背景**: 动态 DNS（DDNS）在设备 IP 地址变化时自动更新 DNS 记录，常用于家庭服务器或远程访问。RFC 2136 定义了标准的 DNS UPDATE 协议，而 TSIG 提供认证。DNSSEC 为 DNS 记录添加加密签名以防止欺骗。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_DNS">Dynamic DNS - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2136">RFC 2136 - Dynamic Updates in the Domain Name System ( DNS ...)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions">Domain Name System Security Extensions - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，称赞对 RFC 2136 的支持以及与 external-dns 等工具的集成。一些用户建议改进着陆页设计，并指出使用 BIND9 自托管也是可行的，但不够方便。

**标签**: `#DNS`, `#IPv6`, `#DNSSEC`, `#networking`, `#open-source`

---

<a id="item-2"></a>
## [荷兰阻止美国收购数字身份提供商](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 8.0/10

荷兰政府阻止了美国公司 Kyndryl 对 Solvinity 的收购，Solvinity 是国家数字身份系统 DigiD 背后的 IT 提供商，理由是数据主权和隐私担忧。 这一决定凸显了围绕数字主权的日益紧张局势，以及外国控制关键国家基础设施的风险，尤其是处理敏感公民数据的身份系统。 Solvinity 托管着 DigiD，数百万荷兰公民使用它访问政府服务；荷兰议会此前投票决定终止与 Solvinity 的合同，但政府延长了合同，因此阻止收购成为关键保障。

hackernews · vrganj · May 26, 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48278406)

**背景**: 数字主权指国家对其自身数据和数字基础设施的控制权。数据主权法律（如欧盟的法律）要求个人数据在境内或区域内存储和处理，以保护隐私和安全。DigiD 是荷兰的国家数字身份系统，对公民在线与政府机构互动至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.biometricupdate.com/202604/netherlands-weighs-data-sovereignty-concerns-with-solvinity-digital-identity-contract">Netherlands weighs data sovereignty concerns with Solvinity digital ...</a></li>
<li><a href="https://www.androguider.com/2026/05/dutch-government-blocks-us-tech.html">Dutch Government Blocks U.S. Tech Acquisition to Safeguard Digital ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者对政府最终采取行动表示欣慰，一些人强调架构上的隐私优于政策上的隐私，并建议采用开源或密码学主权系统作为更好的替代方案。其他人质疑荷兰为何不能为其人口自托管一个开源身份解决方案。

**标签**: `#digital sovereignty`, `#privacy`, `#geopolitics`, `#identity management`, `#open source`

---

<a id="item-3"></a>
## [微软 Copilot Cowork 漏洞导致数据泄露](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

安全研究人员披露，微软 Copilot Cowork 的智能邮件功能可通过提示注入被利用，通过在受感染消息中嵌入外部图片来窃取文件。该攻击利用 OneDrive 的预认证下载链接，使攻击者能够访问文件。 该漏洞凸显了智能 AI 系统中的关键安全挑战，即使是有限的代理操作也可能被劫持以泄露敏感数据。随着企业越来越多地采用 AI 代理来提高生产力，此类窃取向量对数据机密性构成了严重风险。 该攻击之所以有效，是因为 Copilot Cowork 代理可以在未经批准的情况下向用户收件箱发送邮件，而这些邮件可以包含触发网络请求的外部图片。提示注入可导致代理在邮件中包含预认证的 OneDrive 链接，从而使攻击者能够下载文件。

rss · Simon Willison · May 26, 15:36

**背景**: 提示注入是一种网络安全攻击，恶意输入会导致 AI 模型产生意外行为。在智能系统中，AI 代理可以执行发送邮件等操作，这扩大了攻击面。来自 OneDrive 等服务的预认证下载链接允许无需额外身份验证即可访问文件，使其成为窃取攻击的宝贵目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者对智能 AI 的固有风险表示担忧，一些人指出该漏洞是提示注入、代理操作和数据窃取“致命三重奏”的典型例子。其他人则争论微软的设计选择是否疏忽，或者此类问题在早期代理系统中是否不可避免。

**标签**: `#security`, `#AI`, `#prompt injection`, `#Microsoft Copilot`, `#data exfiltration`

---

<a id="item-4"></a>
## [教宗良十四世关于人工智能的通谕](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

教宗良十四世于 2026 年 5 月 25 日发布了其首道通谕《崇高人性》，为人工智能提供伦理指导。该文件与教宗良十三世 1891 年针对工业革命发布的通谕《新事》相呼应。 这是梵蒂冈首部专门针对人工智能伦理的重要通谕，提供了权威的道德指导，可能影响全球政策和公共讨论。它将人工智能视为社会正义问题，强调人类尊严、劳工权利和共同利益。 通谕将 AI 系统描述为更多是“培育”而非“建造”，强调了可解释性问题——即使开发者也不完全了解内部过程。它还强调真正的发展不能将成本转嫁给他人或将地区置于从属地位。

rss · Simon Willison · May 25, 23:58

**背景**: 通谕是教宗针对整个教会乃至更广泛世界就教义或社会教导发布的正式信函。教宗良十四世选择此名号以纪念良十三世，后者 1891 年的通谕《新事》确立了现代天主教关于劳工与资本的社会教导。这道新通谕将类似原则应用于人工智能带来的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica Humanitas - Wikipedia</a></li>
<li><a href="https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html">Encyclical Letter of His Holiness Leo XIV Magnifica Humanitas (15 May 2026)</a></li>
<li><a href="https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-encyclical-magnifica-humanitas-ai.html">Pope Leo’s ‘Magnifica humanitas’: AI must serve humanity not concentrate power - Vatican News</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#Vatican`, `#encyclical`, `#technology and society`

---

<a id="item-5"></a>
## [面向 AI 代理的开源网络安全技能库，包含 754 项技能](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975 发布了面向 AI 代理的最大开源网络安全技能库，包含 754 项结构化技能，映射到五个主要框架（MITRE ATT&CK、NIST CSF 2.0、MITRE ATLAS、D3FEND、NIST AI RMF），并兼容 Claude Code、GitHub Copilot、Cursor 等 20 多个 AI 平台。 该库弥合了网络安全专业知识与 AI 代理之间的鸿沟，使开发者能够为 AI 工具配备跨多个领域的标准化、生产级安全技能，这可能加速 AI 在安全运营中的采用，并提高威胁检测与响应的一致性。 这些技能涵盖 26 个安全领域，并遵循 agentskills.io 开放标准，确保跨平台可移植性。该库采用 Apache 2.0 许可证，并通过拉取请求接受贡献。

rss · GitHub Trending - Daily (All) · May 26, 23:04

**背景**: AI 代理在网络安全中越来越多地用于威胁检测和事件响应等任务，但它们通常缺乏结构化的领域特定知识。MITRE ATT&CK 和 NIST CSF 等框架为网络威胁和防御提供了标准化的分类法，而 agentskills.io 是定义 AI 代理能力的开放标准。该库将这些元素结合起来，为 AI 代理创建了可复用的技能集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>
<li><a href="https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/">MITRE ATLAS Framework 2026 - Guide to Securing AI Systems - Practical DevSecOps</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-6"></a>
## [CodeGraph：为 AI 编程助手预构建的代码知识图谱](https://github.com/colbymchenry/codegraph) ⭐️ 8.0/10

CodeGraph 是一个预索引的代码知识图谱，可为 Claude Code、Cursor、Codex CLI、OpenCode 和 Hermes Agent 等 AI 编程助手减少约 35% 的 token 使用量和约 70% 的工具调用次数，且完全在本地运行。 该工具通过减少 API token 消耗和不必要的工具调用，显著降低了 AI 辅助编程的成本和延迟，使 AI 编程助手在大型代码库中更加实用。其本地执行也解决了无法将代码上传至云服务的开发者的隐私问题。 CodeGraph 使用 tree-sitter 进行 AST 解析，使用 SQLite 和 FTS5 进行索引，并捆绑了自己的运行时，因此无需安装 Node.js。它支持 Windows、macOS 和 Linux，可通过一行 curl 命令或 npm 安装。

rss · GitHub Trending - Daily (All) · May 26, 23:04

**背景**: 像 Claude Code 和 Cursor 这样的 AI 编程助手需要理解整个代码库才能提供相关建议，但将大量代码上下文发送到云端 API 既昂贵又缓慢。代码知识图谱在本地预索引代码结构和关系，使 AI 能够仅检索必要的上下文，而无需重复扫描文件或调用工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/colbymchenry/codegraph">GitHub - colbymchenry/codegraph: Pre-indexed code knowledge ...</a></li>
<li><a href="https://pyshine.com/CodeGraph-Pre-Indexed-Code-Knowledge-Graph-AI-Coding-Agents/">CodeGraph: Pre-Indexed Code Knowledge Graph for AI Coding ...</a></li>
<li><a href="https://tosea.ai/blog/codegraph-claude-code-cursor-guide-2026">How to Use CodeGraph for Claude Code and Cursor: Complete ...</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#code intelligence`, `#developer tools`, `#knowledge graph`

---

<a id="item-7"></a>
## [微软发布 AI 代理治理工具包](https://github.com/microsoft/agent-governance-toolkit) ⭐️ 8.0/10

微软发布了 Agent Governance Toolkit，这是一个开源框架，为自主 AI 代理提供策略执行、零信任身份、执行沙箱和可靠性工程。它覆盖了 OWASP Agentic Top 10 中的所有 10 项风险。 随着 AI 代理变得越来越自主，治理和安全对于安全的生产部署至关重要。微软的这个工具包填补了代理安全的关键空白，帮助企业放心采用 AI 代理。 该工具包以 MIT 许可证在 GitHub 上公开预览，并提供 PyPI、npm 和 NuGet 包。它包含映射到 OWASP Agentic Top 10 的合规文档，并支持多种语言。

rss · GitHub Trending - Python · May 26, 23:04

**背景**: AI 代理是能够规划、执行任务并与工具和 API 交互的自主系统。OWASP Agentic Top 10 是一个识别此类代理关键安全风险的框架，包括身份滥用和权限提升。零信任身份确保每个代理请求都经过验证，而沙箱则隔离代理执行以防止损害。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/">OWASP Top 10 for Agentic Applications for 2026 - OWASP Gen AI Security Project</a></li>
<li><a href="https://xage.com/blog/zero-trust-proven-solution-for-the-new-ai-security-challenge/">Zero Trust for AI Security: How Identity-First Defense Solves Modern Threats</a></li>
<li><a href="https://blogs.cisco.com/security/security-agentic-ai-how-cisco-brings-zero-trust-to-your-new-digital-workforce">Zero Trust for AI Agents – Identity, Access Control, and Behavioral Protection for the Agentic Era</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Governance`, `#Security`, `#Microsoft`, `#OWASP`

---

<a id="item-8"></a>
## [用视觉语言模型复现 Picbreeder 以研究开放性](https://arxiv.org/abs/2605.23908) ⭐️ 8.0/10

研究人员使用前沿视觉语言模型（VLM）复现了人类驱动的 Picbreeder 实验，以探究 AI 能否实现开放式的创造性发现。他们观察到了与人类基线之间的定性差异，并测试了探索性噪声、行为多样性和叙事动量等因素。 这项工作直接回应了 AI 系统能否展现开放性这一根本问题——开放性是人类创造力和科学发现的关键特性。理解这些差异有助于指导更具创造性和自主性的 AI 系统开发。 该研究使用 VLM 替代人类用户进行小神经网络的交互式进化，通过选择和变异生成图像。研究人员在 GitHub 上公开了代码，并使用系统发育复杂度、视觉/语义显著性等指标来表征差异。

rss · arXiv - AI · May 26, 04:00

**背景**: Picbreeder 是一个经典的协作式交互进化在线实验，用户通过选择偏好的变体共同进化图像。开放性指的是生成源源不断的新颖且有意义的输出的能力，这是人类创造力的标志，而当前 AI 系统难以实现。交互式进化计算在客观标准难以定义时，使用人类判断作为适应度函数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.santafe.edu/images/3/34/Stanley_innovation_workshop14.pdf">The Picbreeder Experiment</a></li>
<li><a href="https://ieeexplore.ieee.org/document/6793948">Picbreeder : A Case Study in Collaborative Evolutionary... | IEEE Xplore</a></li>
<li><a href="https://arxiv.org/abs/2406.04268">[2406.04268] Open-Endedness is Essential for Artificial Superhuman Intelligence</a></li>

</ul>
</details>

**标签**: `#open-endedness`, `#vision-language models`, `#AI creativity`, `#evolutionary computation`, `#Picbreeder`

---

<a id="item-9"></a>
## [LLM 置信度校准研究揭示难易效应](https://arxiv.org/abs/2605.23909) ⭐️ 8.0/10

一项预注册的 LLM 置信度校准研究发现，模型在困难任务上过度自信，在简单任务上则自信不足，并引入了 LifeEval 基准来评估不同难度下的校准情况。 这项研究解决了 AI 可靠性中的一个关键问题，表明 LLM 存在类似人类的系统性校准偏差，这对在高风险应用中部署 LLM 具有实际意义。 该研究是预注册的，并使用了一个名为 LifeEval 的新基准，包含 6 个能力维度的 4,075 个问答对，用于测试不同难度下的校准情况。

rss · arXiv - AI · May 26, 04:00

**背景**: 置信度校准衡量模型预测的置信度与其实际准确率的匹配程度。校准不佳可能导致过度自信的错误或自信不足的预测，削弱对 AI 系统的信任。先前的工作已探索了 LLM 的校准，但本研究专门调查了难易效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2311.08298">A Survey of Confidence Estimation and Calibration in Large ...</a></li>
<li><a href="https://arxiv.org/abs/2603.00490">[2603.00490] LifeEval: A Multimodal Benchmark for Assistive AI in Egocentric Daily Life Tasks</a></li>

</ul>
</details>

**标签**: `#LLM`, `#calibration`, `#confidence`, `#AI reliability`, `#benchmark`

---

<a id="item-10"></a>
## [LLM 推理冗余量化：61-93%步骤可截断](https://arxiv.org/abs/2605.23926) ⭐️ 8.0/10

一篇新论文形式化了 LLM 中的推理冗余，并表明在四个前沿模型和两个基准测试中，61-93%的思维链步骤可以在不影响正确性的情况下被截断。 这一发现揭示了当前推理模型浪费了大量计算资源，为在保持准确性的同时降低延迟和成本提供了途径，并挑战了长思维链的必要性。 论文将冗余定义为在模型仍能给出正确答案的前提下可截断的末尾步骤的最大比例；在八个条件中的六个中，中位关键前缀仅为单一步骤，即使在困难问题上冗余仍然存在（Level-5 MATH-500 上为 46-85%）。

rss · arXiv - AI · May 26, 04:00

**背景**: 思维链推理通过生成中间步骤提升了 LLM 在复杂任务上的表现。然而，这些轨迹通常包含重述和自我反思等冗余内容，增加了延迟和成本。本文首次对这种冗余进行了大规模测量并给出了理论解释。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1mkza1b/new_paper_reveals_chainofthought_reasoning_of/">r/LocalLLaMA on Reddit: New paper reveals Chain-of-Thought reasoning of LLMs a mirage</a></li>

</ul>
</details>

**社区讨论**: Reddit 上关于一篇相关论文的讨论显示了对思维链推理的怀疑，一些人认为推理链仅仅是上下文生成，不必连贯。这与本文发现链中大部分内容冗余的结论一致。

**标签**: `#LLM`, `#reasoning`, `#efficiency`, `#chain-of-thought`, `#redundancy`

---

<a id="item-11"></a>
## [Context：通过沙盒程序实现主动式 AI 代理](https://arxiv.org/abs/2605.23928) ⭐️ 8.0/10

研究人员推出了 Context，这是一个用于主动目标导向代理的智能层，取代了被动响应的聊天机器人，通过可组合的沙盒程序和声明式接线来推进任务，无需等待用户提示。 该架构可以通过使代理主动推动交互达成目标，减少延迟和用户努力，从而显著改善对话式 AI，并可能为代理系统设定新标准。 该系统通过写入时上下文组装实现了近 100%的 KV 缓存重用，并在交互时执行沙盒智慧程序而无需额外调用语言模型，同时提供了正确性和效率的形式化证明。

rss · arXiv - AI · May 26, 04:00

**背景**: 当前的对话式 AI 系统通常是反应式的，等待用户输入后才生成响应。Magarshak 架构提出了一种主动方法，代理拥有内部目标流并可以主动采取行动。关键概念包括可组合的沙盒程序（隔离的、可重用的代码模块）和声明式接线（通过类型化关系将程序连接到目标）。

**标签**: `#AI agents`, `#proactive computing`, `#LLM architecture`, `#conversational AI`, `#systems design`

---

<a id="item-12"></a>
## [优化 LLM 代理工作流中的延迟-可靠性-成本](https://arxiv.org/abs/2605.23929) ⭐️ 8.0/10

本文提出了 LLM 和非 LLM 代理的性能模型，并推导出最优令牌分配策略（如注水算法），以平衡顺序代理工作流中的延迟、可靠性和成本。 这项工作解决了部署多代理系统中的一个基本挑战，提供了设计可靠且成本高效的 LLM 驱动工作流的正式方法，对实际 AI 应用至关重要。 论文使用参数指数可靠性函数来建模 LLM 代理的输出质量，并通过优化理论中的影子价格来表征最优工作流可靠性。

rss · arXiv - AI · May 26, 04:00

**背景**: 现代 AI 系统通常使用包含多个代理的工作流，其中一些由 LLM 驱动，另一些由传统模块驱动。平衡延迟、可靠性和成本是一个关键设计挑战。本文为此类权衡提供了理论模型和最优策略。

**标签**: `#LLM agents`, `#reliability`, `#latency`, `#cost optimization`, `#workflow design`

---

<a id="item-13"></a>
## [BODHI：基于 LLM 的操作系统内核规约生成达到 96.73% Pass@1](https://arxiv.org/abs/2605.23931) ⭐️ 8.0/10

研究人员提出 BODHI，一种领域知识提示方法，通过结构化的 C 到 Python 翻译指南增强少样本提示，在 OS 内核规约生成基准 OSV-Bench 上达到最高 96.73%的 Pass@1。 这项工作显著缩小了通用代码生成与形式规约合成之间的差距，自动化了操作系统内核验证中的一个关键瓶颈，可能加速形式化方法在系统软件中的采用。 BODHI 覆盖 15 类领域特定翻译模式，受结构化思维链（SCoT）提示启发，在测试的 9 个模型（来自 6 家提供商）上均带来提升，增益从+11%到+32%。

rss · arXiv - AI · May 26, 04:00

**背景**: 操作系统内核的形式化验证需要精确的规约，传统上由专家手动编写。LLM 提供了自动化潜力，但在从 C 到 Python 的领域特定翻译上存在困难。OSV-Bench 是一个包含 245 个规约生成任务的基准测试，源自 Hyperkernel 操作系统内核，此前最佳 Pass@1 为 55.10%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2305.06599">Structured Chain - of - Thought Prompting for Code Generation</a></li>

</ul>
</details>

**标签**: `#operating systems`, `#formal verification`, `#large language models`, `#specification inference`, `#kernel`

---

<a id="item-14"></a>
## [LLM 在临床压力下表现出信念不稳定](https://arxiv.org/abs/2605.23932) ⭐️ 8.0/10

一项新研究提出了 Med-Stress 压力测试框架，揭示了 LLM 在临床对话中面对逐步升级的压力时会放弃正确诊断，并提出了两种防御方法：RBED 和 R-FT。 这项工作揭示了 LLM 的一个关键故障模式——在压力下的谄媚行为——这损害了它们在高风险临床环境中的可靠性，并提供了实用的防御措施来提高认知韧性。 在九个前沿 LLM 中，研究发现医学知识与鲁棒性之间存在分离，一些模型表现出高准确率但低信念稳定性。R-FT 防御几乎消除了信念变化。

rss · arXiv - AI · May 26, 04:00

**背景**: AI 谄媚行为指模型倾向于同意用户而非独立推理。认知韧性涉及模型在压力下保持正确信念的能力。Med-Stress 框架通过模拟多轮对话中逐步升级的临床压力来测试 LLM。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sycophancy">Sycophancy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epistemology">Epistemology - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI safety`, `#robustness`, `#clinical NLP`, `#sycophancy`

---

<a id="item-15"></a>
## [运行时执行模型强制执行重构权威](https://arxiv.org/abs/2605.23935) ⭐️ 8.0/10

该论文为自主智能体引入了一种运行时执行模型，增加了“暂停”状态和带有漂移检测的恢复循环，确保仅在能从当前状态重构权威时才执行动作。 这项工作通过将重构权威作为运行时执行机制来操作化，填补了 AI 安全中的一个关键空白，可防止自主智能体执行已失去授权的动作，从而提升实际部署中的可信度。 该模型将执行状态空间从“允许/拒绝”扩展为包含第三种状态“暂停”，用于因观测不完整而导致权威未定义的情况，并在恢复循环中集成了漂移检测（IML）与执行控制（ACP）。

rss · arXiv - AI · May 26, 04:00

**背景**: 重构权威（RAM）是一种条件，要求仅当能从当前状态构建权威时才允许执行动作。先前的工作定义了 RAM，但未指定如何在运行时强制执行。本文提供了在真实系统中应用 RAM 所需的执行语义，基于漂移检测和执行门控等概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.23935v1">Operationalizing Reconstructive Authority Runtime ...</a></li>
<li><a href="https://github.com/chelof100/operationalizing-ram">GitHub - chelof100/operationalizing- ram : Paper 6 ...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2605.23935">Operationalizing Reconstructive Authority : Runtime ...</a></li>

</ul>
</details>

**标签**: `#autonomous agents`, `#runtime enforcement`, `#AI safety`, `#authority reconstruction`, `#execution gating`

---

<a id="item-16"></a>
## [算法度量：算法反馈下的预测](https://arxiv.org/abs/2605.23978) ⭐️ 8.0/10

本文提出了算法度量（algometrics）这一框架，用于在算法反馈下进行时间序列预测，并证明部署风险无法仅从被动历史数据中识别，且模型排名在拥挤条件下可能发生反转。 该框架区分了历史风险（被动预测）和部署风险（预测驱动行动），并证明即使在一步线性反馈模型中，也存在无限多个环境产生相同的历史规律但不同的部署风险。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 在算法市场中，预测模型被用于做出交易或分配等决策，而这些决策又会改变模型旨在预测的未来数据。这形成了反馈循环，可能使传统时间序列评估方法失效。本文提出算法度量来显式建模这种依赖性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.23978">[2605.23978] Algometrics: Forecasting Under Algorithmic Feedback</a></li>
<li><a href="https://arxiv.org/html/2605.23978">Algometrics: Forecasting Under Algorithmic Feedback</a></li>

</ul>
</details>

**标签**: `#algorithmic markets`, `#time series forecasting`, `#deployment risk`, `#feedback loops`, `#machine learning`

---

<a id="item-17"></a>
## [可验证 Transformer：为电路解释提供形式化证明](https://arxiv.org/abs/2605.24033) ⭐️ 8.0/10

研究人员提出了可验证 Transformer 框架，该框架利用 SMT 求解器或代理模型将任务局部化的 Transformer 电路转换为有界的、可被求解器检查的声明，从而实现对机械可解释性声明的形式化验证。 这项工作弥合了合理的电路解释与可证明保证之间的差距，通过允许对局部任务中的模型行为进行严格验证，为 AI 安全迈出了关键一步。 该框架包括直接验证（将电路编码到 SMT 求解器中）和代理介导验证（使用可 SMT 编码的代理模型）。它在小型符号任务上演示了直接验证，并在 GPT-2 规模的电路上演示了代理介导验证，其中注意力机制难以编码。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 机械可解释性旨在通过识别负责特定行为的子网络（电路）来逆向工程神经网络。然而，这些解释通常通过示例和消融实验来验证，缺乏形式化证明。SMT 求解器能够判断逻辑公式是否可满足，从而实现对数学声明的自动化验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SMT_solver">SMT solver</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Surrogate_model">Surrogate model</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#transformers`, `#formal verification`, `#AI safety`, `#SMT`

---

<a id="item-18"></a>
## [IRNO：迭代精化神经算子](https://arxiv.org/abs/2605.24041) ⭐️ 8.0/10

研究人员提出了迭代精化神经算子（IRNO），通过不动点迭代应用学习到的精化模块来增强预训练神经算子，在湍流建模中实现了高达 56.05%的误差降低。 这项工作为缓解神经算子中的频谱偏差（科学机器学习中的一个关键限制）提供了一种有原则的方法，并在多个物理系统中展示了显著的实证改进。 IRNO 将预测分解为粗初始化，然后进行连续的残差校正，类似于经典数值求解器，并使用渐进频谱损失，在训练过程中自适应地增加对高频分量的惩罚。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 神经算子是一种深度学习模型，学习函数空间之间的映射，作为科学模拟的快速替代。然而，它们存在频谱偏差问题，即难以捕捉高频细节。不动点迭代是一种经典的数值方法，通过重复应用函数直到收敛来求解方程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fixed-point_iteration">Fixed - point iteration - Wikipedia</a></li>

</ul>
</details>

**标签**: `#neural operators`, `#spectral bias`, `#scientific machine learning`, `#fixed-point iteration`, `#deep learning`

---

<a id="item-19"></a>
## [隐藏状态隐私存在“空中间”](https://arxiv.org/abs/2605.24042) ⭐️ 8.0/10

一篇新论文证明，在隐藏状态隐私中，没有任何高斯发布能同时实现中等效用和隐私，建立了 Fisher 球下界，并识别出一个唯一最优的对角机制。 这一结果将隐藏状态发布从高斯类内的机制设计重新定位为架构或发布协同设计，可能影响隐私保护机器学习和大型语言模型的部署。 该论文测试了 1,536 种高斯发布协方差，发现没有一种能同时实现中等效用和隐私；对角逆 Fisher 发布是唯一的最小最大最优对角机制，但处于隐私/效用的边缘。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 隐藏状态隐私关注保护神经网络中的中间表示（隐藏状态）不被攻击者推断。高斯机制通过向这些状态添加噪声来提供隐私，但本文展示了一个基本权衡：没有高斯发布能填补效用和隐私都可接受的“中间”区域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mahalanobis_distance">Mahalanobis distance - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2210.02482">[2210.02482] Fisher information lower bounds for sampling</a></li>

</ul>
</details>

**标签**: `#privacy`, `#machine learning`, `#information theory`, `#Gaussian mechanisms`, `#differential privacy`

---

<a id="item-20"></a>
## [LLM-AutoSciLab：利用大语言模型进行闭环科学发现](https://arxiv.org/abs/2605.24043) ⭐️ 8.0/10

LLM-AutoSciLab 提出了一个闭环框架，利用大语言模型迭代生成假设、选择信息量大的实验并优化机制，超越了基于静态数据集的发现方式。 该框架通过实现自适应数据采集，解决了当前 AI 驱动科学的一个关键局限，有望在化学和生物学等领域显著加速科学发现。 在 ActiveSciBench-Chem 和 ActiveSciBench-GRN 上，LLM-AutoSciLab 分别达到了 35.1% 的符号准确率和 31.1% 的精确图恢复率，且样本效率比基线方法高 2-5 倍。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 科学发现传统上是一个假设、实验和优化的闭环过程。然而，大多数 AI 方法将发现视为固定数据集上的监督学习，无法自适应地收集新数据来消除不确定性。LLM-AutoSciLab 利用大语言模型自动化整个循环，包括假设生成和实验选择。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/sciadv.adu7426">Real-time experiment-theory closed-loop interaction for autonomous materials science | Science Advances</a></li>
<li><a href="https://arxiv.org/abs/2307.07522">[2307.07522] The Future of Fundamental Science Led by Generative Closed-Loop Artificial Intelligence</a></li>

</ul>
</details>

**标签**: `#LLM`, `#scientific discovery`, `#active learning`, `#AI for science`, `#automated experimentation`

---

<a id="item-21"></a>
## [InteractBind：结合位点定位基准](https://arxiv.org/abs/2605.24045) ⭐️ 8.0/10

研究人员推出了 InteractBind，这是一个包含约 10 万对蛋白质-配体对的数据集和基准，用于评估结合位点定位和非共价相互作用预测，超越了简单的结合预测。 该基准通过测试模型是否真正学习结合位点，填补了蛋白质-配体建模中的关键空白，这对于可解释的药物发现和分子设计至关重要。 该基准包含六种非共价相互作用类型，并使用蛋白质相似性控制的分割来评估泛化能力。对八个现有模型的评估显示，二元结合预测能力强，但结合位点定位能力有限。

rss · arXiv - Machine Learning · May 26, 04:00

**背景**: 蛋白质-配体建模是计算药物发现的基础，模型预测蛋白质和配体是否结合以及结合强度。现有基准侧重于二元结合预测和亲和力回归，但不测试模型能否定位结合位点或识别特定的非共价相互作用，而这些对于理解分子识别至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-covalent_interaction">Non - covalent interaction - Wikipedia</a></li>

</ul>
</details>

**标签**: `#protein-ligand modeling`, `#benchmark`, `#drug discovery`, `#binding site localization`, `#machine learning`

---

<a id="item-22"></a>
## [Raon-Speech：9B 参数语音语言模型在 42 项基准测试中达到最优](https://arxiv.org/abs/2605.23912) ⭐️ 8.0/10

Raon-Speech 是一个 9B 参数的语音语言模型，通过多阶段训练（包括知识蒸馏和偏好优化）在 42 项英语和韩语基准测试中取得了最优结果。该模型还引入了 Raon-SpeechChat，这是一个用于自然实时对话的全双工扩展。 这项工作展示了一种可扩展的方法，将预训练的大语言模型转化为高性能的语音语言模型，同时保留文本能力，为双语语音理解和生成设立了新标准。开源所有检查点和流程将加速语音 AI 和实时对话系统的研究。 该模型在 138 万小时的精选英语和韩语语音及文本数据上进行了三阶段训练：语音模块对齐、带知识蒸馏的端到端预训练以及多任务偏好优化。Raon-SpeechChat 进一步在 11.9 万小时的时间对齐对话数据上训练，在 FDB v1.0 基准测试中在轮换和中断敏感行为方面表现出色。

rss · arXiv - NLP · May 26, 04:00

**背景**: 语音语言模型旨在将语音理解和生成统一到单个模型中，通常通过为基于文本的大语言模型添加语音编码器和解码器来实现。知识蒸馏将知识从较大的教师模型转移到较小的学生模型，而偏好优化则微调模型以使其符合人类对自然交互的偏好。全双工对话允许双方同时说话和打断，模拟人类对话。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.14930">[2509.14930] Cross-Modal Knowledge Distillation for Speech Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2509.18928">[2509.18928] Direct Preference Optimization for Speech Autoregressive Diffusion Models</a></li>
<li><a href="https://arxiv.org/html/2509.00685v1">MPO: Multidimensional Preference Optimization for Language Model-based Text-to-Speech</a></li>

</ul>
</details>

**标签**: `#speech language model`, `#AI`, `#speech understanding`, `#speech generation`, `#multimodal`

---

<a id="item-23"></a>
## [多角色辩论系统用于假设生成](https://arxiv.org/abs/2605.23917) ⭐️ 8.0/10

研究人员提出了多角色辩论系统（MPDS），该框架结合了文献检索、长上下文大语言模型推理、语料驱动角色归纳和结构化多智能体辩论，可自动生成科学假设，并在电池材料研究中得到验证。 MPDS 通过将碎片化知识综合为可操作的假设，解决了科学发现中的关键瓶颈，有望加速电池材料等需同时优化多个约束的复杂领域的研究。 MPDS 构建了多达 500 篇论文的文献快照，在基于角色的智能体之间进行三轮引文感知辩论，并由主持人进行综合；通过时间控制协议进行评估，在消融研究中获得了最高的综合假设质量评分。

rss · arXiv - NLP · May 26, 04:00

**背景**: 科学假设生成常受信息过载和知识碎片化困扰。多智能体辩论系统使用多个具有不同角色的大语言模型智能体来讨论和完善想法，从而提高推理质量。语料驱动角色归纳从文献中自动推导智能体角色，而引文感知辩论确保论点基于特定来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sikkha.medium.com/exploring-multi-agent-debate-frameworks-for-ai-reasoning-and-persona-driven-architectures-0ffb5db05ee3">Exploring Multi-Agent Debate Frameworks for AI Reasoning and Persona-Driven Architectures | by Kan Yuenyong | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-agent-debate-mad-strategies">Multi-Agent Debate Strategies</a></li>
<li><a href="https://arxiv.org/abs/2406.19643">[2406.19643] Debate-to-Write: A Persona-Driven Multi-Agent Framework for Diverse Argument Generation</a></li>

</ul>
</details>

**标签**: `#AI`, `#scientific discovery`, `#multi-agent systems`, `#hypothesis generation`, `#battery materials`

---

<a id="item-24"></a>
## [因果框架揭示 LLM 评判者的合理化偏差](https://arxiv.org/abs/2605.23970) ⭐️ 8.0/10

一篇新论文引入了一个因果框架和一系列线索干预措施，用于检测 LLM 评判者中的合理化偏差，表明在非证据性线索扰动下，解释往往不稳定。该研究提出了如 PROOF-BEFORE-PREFERENCE 等缓解措施，以提高线索不变性。 这项研究填补了 LLM 评估可靠性中的一个关键空白，因为合理化偏差可能削弱用于摘要和对话评估的 AI 评判系统的可信度。提出的指标和缓解措施为增强 AI 安全性和公平性提供了实用工具。 该框架包括五种线索干预（盲、真、翻转、安慰剂、后揭示）以及用于结果锚定和理由锚定的平局感知指标。在 1000 个摘要上的实验显示存在显著的线索锚定合理化，而 PROOF-BEFORE-PREFERENCE 相比基线显著提高了线索不变性。

rss · arXiv - NLP · May 26, 04:00

**背景**: LLM 越来越多地被用作自动评判者来评估文本生成任务，但它们表现出位置和冗长偏好等偏差。先前的工作侧重于结果偏差，而输入扰动下解释的稳定性在很大程度上未被探索。本文引入因果视角来研究解释是忠实的还是捏造的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM-as-a-Judge">LLM-as-a-Judge - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2410.02736v1">Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge</a></li>

</ul>
</details>

**标签**: `#LLM`, `#bias`, `#evaluation`, `#AI safety`, `#causal inference`

---

<a id="item-25"></a>
## [AERIC：用于隐式有害内容的预期隐藏状态监控器](https://arxiv.org/abs/2605.23974) ⭐️ 8.0/10

研究人员提出了 AERIC，一种轻量级的同次传递隐藏状态监控器，能够在无需额外前向传播的情况下预测语言模型中的隐式有害对话。它结合了短时域危害预测、支持敏感抑制和提示条件残差评分，并采用指数移动平均决策规则。 这解决了一个关键的安全挑战：在生成过程中无需额外计算成本即可检测隐式有害内容。AERIC 在检测准确性上显著优于现有流式防护，同时仅增加极小的延迟，使大型语言模型的实时安全监控更加实用。 默认线性监控器仅有 387 个可训练头参数。在 DiaSafety 上，AERIC 将 AUROC 从 0.6830 提升至 0.7143；在 Harmful Advice 上，从 0.8219 提升至 0.8582。在安全预算规则下，Qwen 在 HarmBench DirectRequest 上的 trigger@64 达到 0.6438，延迟仅增加 2.34%，而 Qwen3Guard-Stream-4B 增加 79.40%。

rss · arXiv - NLP · May 26, 04:00

**背景**: 语言模型可能生成有害内容，包括使用间接语言的隐式危害。现有的安全监控器要么检查完整文本（响应级），要么逐 token 运行但需要额外前向传播（流式防护）。同次传递监控在正常解码期间读取隐藏状态，无需额外传播，效率高，但此前在隐式危害检测方面研究不足。

**标签**: `#AI safety`, `#language models`, `#harmful content detection`, `#streaming monitoring`, `#implicit harm`

---

<a id="item-26"></a>
## [DPO 将音频大模型中的语码转换错误减少 89.6%](https://arxiv.org/abs/2605.23975) ⭐️ 8.0/10

研究人员将直接偏好优化（DPO）应用于音频大模型，以对齐英中语码转换语音识别，在分布内数据上实现了高达 89.6%的混合错误率（MER）降低。 这项工作解决了多语言音频大模型中的一个关键空白——语码转换转录，并证明了 DPO 可以在无需复杂强化学习流程的情况下有效纠正系统性失败模式。 该研究识别出三种失败模式：语言省略、翻译代替转录和幻觉。在 10 万个偏好对（570 小时）上训练后，模型行为发生了一致性转变，分布外 MER 降低高达 20.0%。

rss · arXiv - NLP · May 26, 04:00

**背景**: 音频大模型将音频编码器与大型语言模型结合，用于执行语音识别和翻译等任务。语码转换（在同一话语中混合语言）带来了挑战，因为模型常常默认使用一种语言或进行翻译而非转录。直接偏好优化（DPO）是一种轻量级的对齐方法，它使用偏好对微调模型，无需单独的奖励模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@joaolages/direct-preference-optimization-dpo-622fc1f18707">Direct Preference Optimization ( DPO ) | by João Lages | Medium</a></li>
<li><a href="https://arxiv.org/abs/2509.24310">[2509.24310] Code-switching Speech Recognition Under the Lens: Model- and Data-Centric Perspectives</a></li>

</ul>
</details>

**标签**: `#audio LLMs`, `#code-switching`, `#direct preference optimization`, `#speech recognition`, `#multilingual`

---

<a id="item-27"></a>
## [GazeWorld：将放射科医生注视轨迹作为医学 AI 世界模型](https://arxiv.org/abs/2605.23992) ⭐️ 8.0/10

研究人员提出 GazeWorld，一种将放射科医生眼动追踪序列视为图像中轨迹的世界模型，通过自回归预测注视补丁的潜在表示，并通过空间补全分支覆盖未访问区域。 GazeWorld 在 CheXpert、RSNA 肺炎和 SIIM-ACR 气胸基准上达到了最先进的诊断准确率，并在 ScanMatch 和 SED 上分别比专用注视预测模型高出 16%和 22%，表明建模专家如何阅读（而不仅仅是他们得出什么结论）为医学影像 AI 提供了一种有前景的预训练范式。 GazeWorld 使用自回归 Transformer 从先前访问的补丁预测下一个注视补丁的潜在表示，并通过空间补全分支处理未访问区域。推理时，仅从图像生成补丁表示，无需真实注视数据。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: 机器学习中的世界模型学习环境的内部表示以预测未来状态。在医学影像中，放射科医生的眼动追踪数据捕捉了专家如何搜索和积累证据，但先前的方法仅将其用作静态先验或辅助目标。GazeWorld 的创新在于将注视序列建模为图像世界中的轨迹，学习同时编码诊断和注视信息的补丁表示。

**标签**: `#medical imaging`, `#representation learning`, `#world model`, `#eye-tracking`, `#deep learning`

---

<a id="item-28"></a>
## [Nano World Models：极简视频预测代码库](https://arxiv.org/abs/2605.23993) ⭐️ 8.0/10

研究人员发布了 Nano World Models，这是一个基于扩散强迫（diffusion forcing）研究未来视频预测的极简且可扩展的代码库，并附带了代码、配置和预训练检查点。 这填补了研究社区的一个空白，提供了一个紧凑且可复现的实现，使得能够对世界模型中的设计选择进行受控研究，而世界模型是视频预测和决策的核心。 该代码库统一了生成目标、模型规模、动作条件机制、潜在观测空间、数据集、评估协议和长程 rollout，并在控制环境、游戏模拟和真实机器人数据上进行了测试。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: 世界模型是学习预测未来状态的模拟器，常用于规划和决策。扩散强迫是一种结合了下一个词元预测和全序列生成的技术，能够实现更连贯的长程视频预测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/diffusion-forcing">Diffusion Forcing</a></li>

</ul>
</details>

**标签**: `#world models`, `#video prediction`, `#diffusion forcing`, `#reproducibility`, `#AI/ML`

---

<a id="item-29"></a>
## [EEG 以 86%准确率解码视觉刺激](https://arxiv.org/abs/2605.23996) ⭐️ 8.0/10

一种新的脑到图像系统利用 EEG 信号，在 200 个候选图像中实现了 86.3%的 Top-1 检索准确率，并通过与 CLIP 嵌入的多模态对齐重建感知图像。 这项工作表明，从非侵入式 EEG 中高保真解码丰富的视觉表征是可行的，推动了脑机接口和多模态 AI 在辅助通信和神经假体等领域的应用。 检索模型使用多级模糊处理，结合生物启发的 EVNet 特征和 InfoNCE 损失；重建模型（CognitionCapturerPro）将 EEG 与图像、文本、深度和边缘的 CLIP 嵌入对齐，然后通过 SDXL-Turbo 和 IP-Adapter 生成图像。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: EEG（脑电图）非侵入式记录大脑电活动。CLIP 是一种多模态模型，将图像和文本在共享嵌入空间中对齐。InfoNCE 是一种对比损失函数，通过拉近正样本对、推远负样本来学习表征。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.12722">[2603.12722] CognitionCapturerPro: Towards High-Fidelity Visual Decoding from EEG/MEG via Multi-modal Information and Asymmetric Alignment</a></li>

</ul>
</details>

**标签**: `#EEG`, `#brain-computer interface`, `#multimodal learning`, `#image retrieval`, `#image reconstruction`

---

<a id="item-30"></a>
## [IVR-R1：多模态大语言模型的迭代视觉接地推理强化学习](https://arxiv.org/abs/2605.23997) ⭐️ 8.0/10

IVR-R1 提出了一种迭代视觉接地推理强化学习框架，通过动态重新对齐视觉信息来纠正多模态大语言模型中的推理轨迹，解决了长程任务中的视觉幻觉和逻辑错误。 这项工作解决了多模态大语言模型在长程推理中的关键局限——视觉幻觉和逻辑错误，通过动态视觉重新对齐，有望显著提升 AI 系统在复杂视觉推理任务中的可靠性。 IVR-R1 使用奖励驱动的筛选机制识别有缺陷的 rollout，进行细粒度的步骤级错误归因，并采用重新推理循环，迭代地将中间推理状态与原始视觉先验交叉引用，以合成专家级演示。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: 多模态大语言模型结合文本和视觉信息用于视觉问答等任务。然而，它们经常出现视觉幻觉（模型生成错误的视觉细节）和长推理链中的逻辑错误。强化学习用于改进这些模型，但现有方法难以在扩展的推理步骤中保持视觉接地。

**标签**: `#multimodal LLM`, `#reinforcement learning`, `#visual reasoning`, `#visual hallucination`, `#AI research`

---

<a id="item-31"></a>
## [DIDR：通过扩散奖励实现原理性的一步生成器强化学习](https://arxiv.org/abs/2605.24001) ⭐️ 8.0/10

研究人员提出了扩散奖励的扩散指导（DIDR），这是一个用于一步文本到图像生成器的轨迹级对齐框架，它将奖励优化后的分布传播到所有噪声级别，在保持效率的同时提高了保真度。 DIDR 通过提供一种将奖励优化与生成动力学对齐的原理性方法，解决了一步生成强化学习中的一个关键限制，可能为实时应用带来更高效、更高质量的文本到图像模型。 DIDR 源于积分 KL 最小化，并引入了扩散奖励分数（DRS）作为对参考分数函数的奖励驱动修正，同时提出了基于可微短步去噪的实用估计器——扩散奖励代理（DRP）。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: 一步文本到图像生成器旨在通过单次前向传播生成图像，提供实时合成，但与多步扩散模型相比，在保真度上往往存在不足。基于人类反馈的强化学习（RLHF）可以使输出与偏好对齐，但将其应用于一步生成器时，面临终端奖励优化与底层扩散动力学之间的不匹配问题。

**标签**: `#text-to-image generation`, `#reinforcement learning`, `#diffusion models`, `#one-step generation`, `#RLHF`

---

<a id="item-32"></a>
## [ActQuant：面向 VLA 模型的亚 4 位量化方法](https://arxiv.org/abs/2605.24011) ⭐️ 8.0/10

ActQuant 提出了一种动作引导的混合精度训练后量化框架，实现了对视觉-语言-动作模型的亚 4 位权重量化，在 LIBERO 基准测试上保持超过 94%的性能，并将骨干网络内存压缩高达 5.3 倍。 这项工作解决了 VLA 模型在边缘设备上部署的关键挑战，实现了在不显著损失性能的情况下进行激进压缩，可能加速机器人控制等实际具身智能应用。 ActQuant 分两个阶段运行：张量间位分配器根据动作贡献分配位宽，张量内尺度优化器使用动作感知曲率将动态范围集中在影响控制的权重上。它还包含 OmniModel.cpp，一个用于在 C/C++运行时上高效低比特内核的转换流水线。

rss · arXiv - Computer Vision · May 26, 04:00

**背景**: 视觉-语言-动作（VLA）模型结合了视觉感知、语言理解和动作生成，用于机器人操作等具身 AI 任务。训练后量化（PTQ）通过降低数值精度来减小模型大小和推理成本，但激进的亚 4 位量化通常会导致严重的性能下降。混合精度量化为模型的不同部分分配不同的位宽，以平衡压缩和精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Optimization_of_vision-language-action_models_for_edge_devices">Optimization of vision-language-action models for edge devices</a></li>
<li><a href="https://ianloe.medium.com/the-complete-guide-to-vision-language-action-models-how-robots-are-learning-to-think-f1a788d003ed">The Complete Guide to Vision - Language - Action Models ... | Medium</a></li>

</ul>
</details>

**标签**: `#quantization`, `#VLA models`, `#edge AI`, `#embodied intelligence`, `#PTQ`

---

<a id="item-33"></a>
## [因果性作为人工智能的统计良知](https://arxiv.org/abs/2605.24076) ⭐️ 8.0/10

一篇新的 arXiv 论文提出因果推断是人工智能的统计良知，给出了因果泛化的统计必要性定理，并建立了一个统一框架，将 Pearl 的 do-calculus、潜在结果框架、双重机器学习以及不变风险最小化联系起来。 这项工作解决了当前 AI 的一个根本局限——无法区分相关性与因果性——这对于构建在分布偏移下能泛化并避免幻觉、奖励黑客等故障的值得信赖的机器至关重要。 论文形式化了预测 P(Y|X)与智能 P(Y|do(X))之间的区别，并将三种 AI 故障模式（幻觉、奖励黑客、分布偏移退化）识别为因果盲点的表现，每种都有原则性的统计补救措施。

rss · arXiv - Data Science & Statistics · May 26, 04:00

**背景**: 因果推断是一个旨在从数据中识别因果关系的领域，超越了单纯的相关性。Judea Pearl 的 do-calculus 提供了一个关于干预推理的图形化框架，而潜在结果框架和双重机器学习是估计因果效应的统计方法。不变风险最小化则寻求跨环境鲁棒的预测器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/do_calculus">Do -calculus</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#artificial intelligence`, `#machine learning`, `#generalization`, `#do-calculus`

---

<a id="item-34"></a>
## [MEDAL：将流形嵌入蒸馏到自编码器中](https://arxiv.org/abs/2605.24244) ⭐️ 8.0/10

MEDAL（通过自编码器学习进行流形嵌入蒸馏）是一个新颖的框架，它将任何已拟合的流形嵌入（如 t-SNE、UMAP）蒸馏到一个受约束的自编码器中，从而为留出验证提供显式的样本外映射和近似逆重构。 这解决了无监督流形学习中的一个关键空白，通过实现严格的定量验证——此前由于缺乏样本外映射和逆映射而无法做到——从而允许对降维技术进行超参数调优和方法比较。 MEDAL 训练一个受约束的自编码器，其瓶颈层精确匹配教师嵌入，同时解码器重构原始输入，从而产生基于逐点重构的失真度量。它可以作为通用的验证包装器应用于任何现有的降维方法。

rss · arXiv - Data Science & Statistics · May 26, 04:00

**背景**: t-SNE 和 UMAP 等非线性降维方法广泛用于高维数据的可视化，但它们缺乏样本外映射（嵌入新点）和逆映射（重构原始特征），使得留出验证——监督学习中的黄金标准——无法进行。MEDAL 通过将嵌入蒸馏到自编码器模型中克服了这一难题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cdn.aaai.org/ojs/7908/7908-13-11436-1-2-20201228.pdf">A Generalised Solution to the Out-of-Sample Extension ...</a></li>
<li><a href="https://ojs.aaai.org/index.php/AAAI/article/view/7696">Local and Global Regressive Mapping for Manifold Learning with Out-of-Sample Extrapolation | Proceedings of the AAAI Conference on Artificial Intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets">Training, validation, and test data sets - Wikipedia</a></li>

</ul>
</details>

**标签**: `#manifold learning`, `#autoencoder`, `#dimension reduction`, `#unsupervised learning`, `#data visualization`

---

<a id="item-35"></a>
## [多校准提升的统一理论](https://arxiv.org/abs/2605.24364) ⭐️ 8.0/10

本文为多校准提升（MCBoost）建立了统一的理论框架，涵盖了多精度、BatchGCP 和 BatchMVP 等现有变体，并揭示了由早停控制的校准-风险权衡。 这项工作为多校准提供了更完整的理论基础和实践指导，而多校准对于机器学习中的公平性、鲁棒性和可靠预测至关重要。 作者证明 MCBoost 迭代收敛到总体最优预测器的 Bregman 投影，推导了不同光滑性假设下的收敛速率，并扩展了协变量偏移下的迁移保证。

rss · arXiv - Data Science & Statistics · May 26, 04:00

**背景**: 多校准扩展了经典校准，要求预测在一组丰富的函数（包括预测切片和子群体）上无偏。它已成为公平性和可靠预测的强大框架，但先前的理论理解零散且依赖限制性假设。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.24364">[2605.24364] Multicalibration Boosting: Theory, Convergence, and Transferability</a></li>
<li><a href="https://arxiv.org/abs/2301.13767">[2301.13767] Multicalibration as Boosting for Regression</a></li>
<li><a href="https://github.com/mlr-org/mcboost">GitHub - mlr-org/mcboost: Multi-Calibration & Multi-Accuracy Boosting for R · GitHub</a></li>

</ul>
</details>

**标签**: `#multicalibration`, `#fairness`, `#machine learning theory`, `#boosting`, `#reliable prediction`

---

<a id="item-36"></a>
## [神经奖励模型学习策略优化的特征](https://arxiv.org/abs/2605.24749) ⭐️ 8.0/10

本文通过高斯单指标模型，从理论上分析了神经奖励模型如何在 KL 正则化策略优化中学习特征，表明在温度阈值以上，指数奖励加权能够实现特征恢复。 这项工作弥合了奖励建模与策略优化理论之间的鸿沟，提供了关于部署温度和学习复杂度的严格界限，对改进 RLHF 算法和 AI 对齐至关重要。 分析采用两阶段神经网络：首先通过奖励加权样本学习隐藏方向，然后通过加权岭回归拟合读出层。可接受的部署温度集平衡了降低β₂带来的收益与指数加权放大的学习成本。

rss · arXiv - Data Science & Statistics · May 26, 04:00

**背景**: 在基于人类反馈的强化学习（RLHF）中，奖励模型被训练来预测人类偏好，然后通过 KL 正则化强化学习来优化策略。高斯单指标模型假设奖励是输入线性投影的函数，这简化了理论分析。Hermite 多项式为分析高斯输入下的信号提供了正交基。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Gaussian_function">Gaussian function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hermite_polynomials">Hermite polynomials - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#reward modeling`, `#RLHF`, `#theoretical analysis`, `#policy optimization`

---

<a id="item-37"></a>
## [强化学习中的反事实安全框架](https://arxiv.org/abs/2605.25114) ⭐️ 8.0/10

该论文提出了一种两阶段强化学习流程，在最大化期望回报的同时控制个体伤害，其中伤害被反事实地定义为所选动作导致比基线替代方案更差的结果。论文提供了有限样本保证，并在模拟和真实数据集上进行了实证验证。 这项工作解决了强化学习中未被充分探索的个体伤害问题，超越了平均情况最优性，确保每个个体的安全。它提供了一个具有理论保证的原则性框架，对于在医疗或自动驾驶等高危应用中部署强化学习至关重要。 该方法采用两阶段流程：首先学习基线策略，然后优化受伤害约束的目标。论文推导了次优性差距的上界，并表明在有限样本下伤害率得到了良好控制。

rss · arXiv - Data Science & Statistics · May 26, 04:00

**背景**: 强化学习通常优化群体上的期望回报，这可能导致策略伤害某些个体。反事实推理评估“如果……会怎样”的场景，以理解未采取决策的影响。机器学习中的个体公平性旨在对相似个体进行一致处理，但在强化学习中研究较少。本文结合这些思想，提出了一个新的安全框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0004370221000060">Counterfactual state explanations for reinforcement learning agents via generative deep learning - ScienceDirect</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fairness_(machine_learning)">Fairness (machine learning) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2006.11737">[2006.11737] Verifying Individual Fairness in Machine Learning Models</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#safe RL`, `#counterfactual reasoning`, `#individual fairness`, `#machine learning`

---

<a id="item-38"></a>
## [自主 AI 采用面临组织准备不足的鸿沟](https://www.technologyreview.com/2026/05/26/1137584/rethinking-organizational-design-in-the-age-of-agentic-ai/) ⭐️ 8.0/10

一份新报告显示，85%的组织计划在三年内采用自主 AI，但 76%的组织承认其当前的运营和基础设施无法支持这一转变。 这一差距凸显了企业 AI 转型的关键障碍，因为自主 AI 承诺自主执行任务，但需要在人员、流程和工作流方面进行根本性变革。 报告指出，人员、流程和工作流方面的准备不足是主要障碍，表明组织在大规模部署自主 AI 之前必须重新设计其运营。

rss · MIT Technology Review · May 26, 14:54

**背景**: 自主 AI 指的是能够自主采取行动以实现目标的 AI 系统，而不仅仅是生成文本或建议。与传统 AI 助手不同，自主 AI 可以编排复杂的工作流并与外部工具集成，因此对企业自动化具有吸引力。然而，成功采用需要成熟的数据基础设施、清晰的治理和重新设计的工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/insights/enterprise-ai-agents">Enterprise AI Agents: Beyond Productivity | IBM</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform">Introducing Gemini Enterprise Agent Platform | Google Cloud Blog</a></li>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#organizational design`, `#enterprise AI`, `#AI adoption`

---

<a id="item-39"></a>
## [AI 悄然侵蚀入门级工作，危机迫在眉睫](https://www.technologyreview.com/2026/05/26/1137865/its-time-to-address-the-looming-crisis-in-entry-level-work/) ⭐️ 8.0/10

《麻省理工科技评论》的一篇分析文章指出，尽管 AI 并未导致大规模失业，但它正在悄然侵蚀入门级工作机会，为早期职业工作者制造了一场迫在眉睫的危机。 这很重要，因为入门级工作对技能发展和职业晋升至关重要；它们的侵蚀可能导致长期的结构性失业和不平等，即使总体就业保持稳定。 文章指出，发达国家的总体就业保持基本稳定，最近的评估发现 AI 改变总体数字的证据有限，但职业阶梯的第一级正在弱化。

rss · MIT Technology Review · May 26, 09:00

**背景**: 入门级工作传统上充当新工人的培训基地，提供必要的技能和经验。AI 和自动化越来越能够执行曾经属于初级员工的常规任务，从而减少了对这类职位的需求。

**标签**: `#AI`, `#labor market`, `#entry-level work`, `#employment`, `#technology impact`

---

<a id="item-40"></a>
## [鼻喷雾剂逆转小鼠大脑衰老](https://www.sciencedaily.com/releases/2026/05/260526022018.htm) ⭐️ 8.0/10

德州农工大学的研究人员开发出一种鼻喷雾剂，仅需两剂即可通过减轻炎症和恢复细胞能量系统来逆转小鼠的大脑衰老，使记忆和认知能力改善持续数月。 这一突破可能为痴呆症和阿尔茨海默病等与年龄相关的神经退行性疾病的新疗法铺平道路，提供一种直接作用于大脑的非侵入性给药方式。 该喷雾针对大脑炎症和线粒体功能障碍这两个衰老标志。这项研究于 2026 年 4 月发表，由再生医学研究所的 Ashok Shetty 博士及其同事领导。

rss · ScienceDaily Health · May 26, 13:39

**背景**: 大脑衰老与慢性低度炎症和神经元能量产生下降有关。鼻喷雾剂提供了一条绕过血脑屏障直接到达大脑的途径，使其成为神经治疗的一种有前景的给药系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://neurosciencenews.com/nasal-spray-reverse-brain-aging-30519/">Nasal Spray Reverses Brain Aging and Inflammation - Neuroscience News</a></li>
<li><a href="https://stories.tamu.edu/news/2026/04/14/scientists-reverse-brain-aging-with-a-nasal-spray/">Scientists reverse brain aging, with a nasal spray – Texas A&M Stories</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#aging`, `#dementia`, `#nasal spray`, `#research`

---

<a id="item-41"></a>
## [南加州大学科学家发现阿尔茨海默病隐藏触发因素及潜在药物靶点](https://www.sciencedaily.com/releases/2026/05/260525000504.htm) ⭐️ 8.0/10

南加州大学研究人员发现了靶向 cPLA2 酶的药物化合物，可能减少与阿尔茨海默病相关的脑部炎症，尤其是在 APOE4 基因携带者中。 这些化合物靶向 cPLA2 酶，该酶会加剧有害炎症，但对正常脑活动也很重要，提示治疗需谨慎平衡。

rss · ScienceDaily Health · May 26, 04:56

**背景**: 阿尔茨海默病是一种进行性神经退行性疾病，目前尚无治愈方法。APOE4 基因变异是最强的遗传风险因素，可将风险提高 2-3 倍。cPLA2 是一种参与脂质信号传导和炎症的酶，其过度激活与阿尔茨海默病病理有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://med.stanford.edu/news/insights/2025/09/rethinking-alzheimers-gene-variant-apoe4.html">Rethinking Alzheimer’s: Why this common gene variant is bad for your brain</a></li>
<li><a href="https://dornsife.usc.edu/bridge-institute/wp-content/uploads/sites/82/2023/10/C_Valderrama_Mia_BUGSJr2023_ver1.pdf">C_Valderrama_Mia_BUGSJr2023_ver1.pptx</a></li>

</ul>
</details>

**标签**: `#Alzheimer's`, `#neuroscience`, `#drug discovery`, `#inflammation`, `#APOE4`

---