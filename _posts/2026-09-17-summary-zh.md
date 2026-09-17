---
layout: default
title: "Horizon Summary: 2026-09-17 (ZH)"
date: 2026-09-17
lang: zh
---

> From 104 items, 12 important content pieces were selected

---

1. [NSA 的开源逆向工程框架 Ghidra](#item-1) ⭐️ 9.0/10
2. [小米发布 MiMo 2.6 实时后训练仪表盘](#item-2) ⭐️ 8.0/10
3. [Mistral 与 Mozilla 合作，为 Firefox 带来私密多语言 AI 浏览](#item-3) ⭐️ 8.0/10
4. [黑客在 Flock 监控摄像头中发现硬编码凭证](#item-4) ⭐️ 8.0/10
5. [Anthropic 推出官方 Claude Code 插件目录](#item-5) ⭐️ 8.0/10
6. [立场论文：AI 尚无资格参与战略兵棋推演，除非具备可审计安全论证](#item-6) ⭐️ 8.0/10
7. [人工智能生物安全风险与纵深防御治理框架](#item-7) ⭐️ 8.0/10
8. [大模型内部存在独立的线性“疼痛方向”，并驱动自我缓解行为](#item-8) ⭐️ 8.0/10
9. [偏见审计能检测偏见，却无法就模型排名达成一致](#item-9) ⭐️ 8.0/10
10. [ASDchat：多模态大模型实现 0.953 AUC 的孤独症筛查](#item-10) ⭐️ 8.0/10
11. [小鼠大脑皮层主要由人类细胞构成](#item-11) ⭐️ 8.0/10
12. [cGAS 免疫“误报”可能驱动快速衰老](#item-12) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [NSA 的开源逆向工程框架 Ghidra](https://github.com/NationalSecurityAgency/ghidra) ⭐️ 9.0/10

美国国家安全局（NSA）的软件逆向工程（SRE）框架 Ghidra 正在 GitHub 上受到关注，它是一款免费开源工具，可在 Windows、macOS 和 Linux 上提供反汇编、反编译、图形化和脚本功能。当前版本需要 64 位 JDK 25，并支持用户使用 Java 或 Python 开发扩展和脚本。 Ghidra 的开源发布标志着专业级逆向工程工具可获得性的重大转变，为安全研究人员、恶意软件分析师和学生提供了一个可替代专有工具 IDA Pro 的免费选择。其 NSA 背景和可扩展性使其成为现代安全研究和漏洞分析的重要基石。 Ghidra 支持多种处理器指令集和可执行文件格式，可在交互模式和自动化模式下运行；其反编译器组件用 C++ 编写，可独立使用。该项目还警告某些版本存在已知安全漏洞，因此用户在继续使用前应查看安全公告。

rss · GitHub Trending - Daily (All) · Sep 16, 23:59

**背景**: 软件逆向工程是分析已编译二进制文件以恢复其结构和行为的过程，通常使用反汇编（将机器码转换为汇编代码）和反编译（重建 C 等更高级代码）。Ghidra 于 2019 年 3 月在 RSA 大会上以二进制形式发布，一个月后在 GitHub 上公开源代码，它用 Java 编写并使用 Swing 图形界面。如今许多安全研究人员认为它是 IDA Pro 的可行开源替代品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NationalSecurityAgency/ghidra">GitHub - NationalSecurityAgency/ghidra: Ghidra is a software reverse engineering (SRE) framework · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ghidra_(software)">Ghidra (software)</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3338503.3357725">Hands-On Ghidra - A Tutorial about the Software Reverse Engineering Framework | Proceedings of the 3rd ACM Workshop on Software Protection</a></li>

</ul>
</details>

**标签**: `#reverse-engineering`, `#security`, `#NSA`, `#open-source`, `#disassembly`

---

<a id="item-2"></a>
## [小米发布 MiMo 2.6 实时后训练仪表盘](https://mimo.xiaomi.com/rl/) ⭐️ 8.0/10

小米公开发布了一个实时仪表盘，用于直播其 MiMo 2.6 模型的强化学习后训练过程，实时展示奖励曲线和评估指标。 这种透明度在 LLM 开发中并不常见，因为后训练通常不对外公开；这可能促使其他模型提供商开放其训练过程，同时增强小米在开源 AI 生态中的地位。 该仪表盘专门追踪强化学习阶段而非预训练阶段；社区指出，前代 MiMo-V2.5-Pro 在 DeepSWE 1.1 上仅得 19%，远落后于 Fable（70%）、Kimi K3（69%）和 Astra（74%）等竞品。

hackernews · krackers · Sep 16, 20:09 · [社区讨论](https://news.ycombinator.com/item?id=49732270)

**背景**: 后训练是指模型完成初始大规模预训练之后的阶段，通过监督微调、偏好优化和强化学习等技术，将原始基础模型转变为实用且对齐的系统。小米的 MiMo 系列是开源模型家族；MiMo-V2.5-Pro 被称为其迄今最强模型，拥有 1T 总参数、42B 激活参数和 1M token 上下文窗口。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aiweekly.co/alerts/xiaomi-publishes-live-post-training-dashboard-for-mimo-26-rl-run-streams-real">Xiaomi opens live RL post-training dashboard for Mimo 2.6</a></li>
<li><a href="https://en.wikipedia.org/wiki/Post-training_of_large_language_models">Post-training of large language models</a></li>
<li><a href="https://mimo.xiaomi.com/mimo-v2-5-pro">MiMo-V2.5-Pro | Xiaomi</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极：一位软件工程师称赞 MiMo-V2.5 的性价比和低成本，另一位将其比作能力强但健忘的资深工程师，还有人称该仪表盘是闭源提供商 IPO 的“定时炸弹”。也有人质疑其他模型提供商为何不效仿，而基准对比则凸显了 MiMo 与领先模型之间的差距。

**标签**: `#LLM`, `#post-training`, `#Xiaomi`, `#open-source AI`, `#model evaluation`

---

<a id="item-3"></a>
## [Mistral 与 Mozilla 合作，为 Firefox 带来私密多语言 AI 浏览](https://mistral.ai/news/mistral-x-mozilla/) ⭐️ 8.0/10

Mistral AI 与 Mozilla 宣布建立合作伙伴关系，由 Mistral 模型驱动 Firefox 的 AI 浏览助手 Firefox Smart Window（测试版），提供私密、多语言的 AI 浏览体验。该功能支持上下文感知搜索、页面摘要以及跨浏览器标签页的记忆检索，目前已在法国和北美上线，并计划于今年晚些时候在英国和德国推出。 此次合作将一家重要的欧洲 AI 提供商直接嵌入主流浏览器，可能为用户提供一个注重隐私、可替代 Chrome 内置 Gemini Nano 的选择。同时，这也加剧了关于 AI 浏览功能应在本地设备运行还是在云端运行的争论，这一取舍直接影响用户隐私与信任。 该服务基于零数据保留政策构建，Mozilla 表示对话不会被存储，但营销页面并未清楚说明本地推理与云端推理的具体分工。这些模型支持上下文感知搜索、页面摘要和跨标签页记忆检索，但目前仅限法国和北美地区使用。

hackernews · vertigoruntime · Sep 16, 08:08 · [社区讨论](https://news.ycombinator.com/item?id=49723408)

**背景**: Mistral AI 是一家成立于 2023 年的法国公司，开发大型语言模型，估值超过 140 亿美元，是欧洲估值最高的 AI 公司。本地推理直接在用户设备上运行 AI 模型，数据更私密但受硬件限制；云端推理则将查询发送到远程服务器，能力更强但牺牲隐私。Mozilla 的 Firefox 长期以注重隐私、区别于 Chrome 为定位，而 Chrome 已内置 Google 的设备端 Gemini Nano 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mistral.ai/news/mistral-x-mozilla/">Mistral x Mozilla: Private , Multilingual AI Browsing</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mistral_AI">Mistral AI - Wikipedia</a></li>
<li><a href="https://medium.com/@muruganantham52524/ollama-vs-openai-local-vs-cloud-ai-performance-cost-and-use-cases-0d25fea5f049">Ollama vs OpenAI: Local vs Cloud AI — Performance, Cost... | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这一功能，但尖锐批评其对本地推理与云端推理的区别说明不清，有人主张 Mozilla 应推广完全本地的小模型推理，而不是将浏览历史上传到云端。还有人指出，即便是注重隐私的云端推理，也需要信任 Mozilla 及其合作伙伴，而终端用户无法验证，并将其与 Chrome 内置的 Gemini Nano 相比较。

**标签**: `#AI`, `#privacy`, `#Mozilla`, `#Mistral`, `#browser`

---

<a id="item-4"></a>
## [黑客在 Flock 监控摄像头中发现硬编码凭证](https://www.wired.com/story/hackers-flock-camera-data-shows-how-system-works/) ⭐️ 8.0/10

安全研究人员（包括 Micah Lee）在 Flock Safety 监控摄像头中发现了硬编码凭证和其他漏洞，《连线》杂志与 404 Media 合作报道了此事。泄露的 API 密钥可用于请求以明文存储的凭证，这些凭证似乎能访问 Flock 的服务器，同时 Distributed Denial of Secrets 已公开了摄像头的分区镜像。 Flock Safety 摄像头广泛部署在公共场所，用于自动车牌识别和大规模监控，因此这些漏洞引发了人们对公共监控基础设施安全性的严重担忧。这些发现可能削弱公众对 Flock 系统的信任，并凸显执法部门使用的不安全物联网设备所带来的系统性风险。 硬编码凭证是一个 API 密钥，而非明文管理员密码，但它可用于获取以明文存储、似乎能授予服务器访问权限的凭证。目前尚不清楚攻击者以摄像头身份通过认证后能做什么，而 Flock 的漏洞披露政策因不鼓励涉及与设备交互或下载数据的研究而受到批评。

hackernews · driverdan · Sep 16, 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49726586)

**背景**: Flock Safety 是一家美国公司，生产并运营监控硬件和软件，尤其是自动车牌识别（ALPR）摄像头，这些摄像头通常由太阳能供电，安装在社区和高速公路沿线的杆子上。硬编码凭证是一种众所周知的漏洞类型（CWE-798），即密码、API 密钥或加密密钥被直接嵌入源代码或固件中，导致所有安装实例使用相同凭证，攻击者很容易提取。由于这些摄像头被放置在无防护的公共场所，其威胁模型必须包含对硬件的本地物理访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cwe.mitre.org/data/definitions/798.html">CWE - CWE-798: Use of Hard-coded Credentials (4.20)</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Flock 提出了强烈批评，称硬编码凭证是无能的表现，也是为缩短上市时间而偷懒的结果。许多人指出，Flock 的漏洞披露政策似乎旨在营造负责任的表面形象，而非真正了解漏洞，还有人指出数据未加密，任何有物理访问权限的人都能获取。

**标签**: `#security`, `#IoT`, `#surveillance`, `#vulnerability`, `#privacy`

---

<a id="item-5"></a>
## [Anthropic 推出官方 Claude Code 插件目录](https://github.com/anthropics/claude-plugins-official) ⭐️ 8.0/10

Anthropic 正式推出了一个官方精选的 Claude Code 插件目录，托管在 github.com/anthropics/claude-plugins-official。该目录将 Anthropic 内部开发的插件与第三方外部插件分开管理，用户可以通过命令 `/plugin install {plugin-name}@claude-plugins-official` 安装，或在 `/plugin > Discover` 中浏览安装。 这为开发者提供了一个可信的、由官方管理的渠道来扩展 Claude Code 的功能，通过降低寻找优质插件的门槛和风险，可能加速这款 AI 编程助手的普及。这也表明 Anthropic 正在围绕 Claude Code 构建插件生态系统，类似于其他开发者平台通过应用市场推动增长的方式。 该目录包含一条醒目警告：Anthropic 无法控制或验证插件中包含的 MCP 服务器、文件或其他软件，因此用户在安装前必须自行确认插件的可信度。插件遵循标准结构，必须包含 `.claude-plugin/plugin.json` 元数据文件，并可选配 MCP 配置、命令、代理和技能；插件名称是不可变的 slug，可通过 `renames` 映射进行迁移。

rss · GitHub Trending - Python · Sep 16, 23:59

**背景**: Claude Code 是 Anthropic 推出的智能编程工具，能够理解代码库、编辑文件并在终端或 IDE 中运行命令。插件通过技能、代理、钩子和 MCP 服务器来扩展 Claude Code 的功能，其中 MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放标准，用于将 AI 系统与外部工具和数据源连接起来。这个官方目录在此基础上提供了一个精选市场，涵盖第一方和社区贡献的扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-plugins-official">GitHub - anthropics/claude-plugins-official: Official ...</a></li>
<li><a href="https://code.claude.com/docs/en/plugins">Create plugins - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/MCP_server">MCP server</a></li>

</ul>
</details>

**标签**: `#Claude Code`, `#AI plugins`, `#Anthropic`, `#developer tools`, `#AI coding assistant`

---

<a id="item-6"></a>
## [立场论文：AI 尚无资格参与战略兵棋推演，除非具备可审计安全论证](https://arxiv.org/abs/2609.16189) ⭐️ 8.0/10

一篇新的 arXiv 立场论文（2609.16189v1）主张，任何由语言模型驱动的兵棋推演，在没有可审计安全论证的情况下，都不应被用于影响规划、条令、政策或危机响应。论文识别出五种失效模式——决策洗白、裁决不透明、角色崩塌、经由裁决的升级、战略想象力失效——并提出当前开放式兵棋推演的正确用途是压力测试那些会影响决策的语言模型智能体。 随着各国政府和军方开始尝试用大语言模型进行战略与危机规划模拟，该论文警告普通基准测试无法在这类高风险场景中确立安全性。这可能影响国防与政策领域对 AI 安全论证的要求方式，波及研究人员、国防规划者和 AI 开发者。 论文强调，在开放式兵棋推演中，模型的语言既决定行动者试图做什么，也决定什么成为模拟现实，这使得让语言模型具有吸引力的能力同时也带来危险。论文结论是，兵棋推演可以作为压力测试暴露失效，但其本身并不能构成用于重大后果场景的安全论证。

rss · arXiv - AI · Sep 16, 04:00

**背景**: 兵棋推演是军方和政策制定者用来探索对手行为、升级动态、条令和危机响应的结构化模拟。语言模型正越来越多地被用于这类模拟，因为它们可以扮演智能体、生成情景分支、裁决模糊行动并总结教训。安全论证是一种结构化、可审计的论证，辅以证据说明系统在特定用途下可接受地安全，这一概念目前正被引入 AI 系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2601.22773">[2601.22773] A Structured Approach to Safety Case Construction for AI Systems</a></li>
<li><a href="https://arxiv.org/html/2511.15573v1">Two-Faced Social Agents: Context Collapse in Role-Conditioned ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#language models`, `#wargaming`, `#strategic simulation`, `#AI ethics`

---

<a id="item-7"></a>
## [人工智能生物安全风险与纵深防御治理框架](https://arxiv.org/abs/2609.16213) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.16213）综述了通用大语言模型、生物基础模型、智能体系统和自动化实验室等 AI 能力如何带来生物安全风险，指出威胁不仅取决于 AI 能力，还取决于使用者的专业知识、意图、对实验室工具和材料的获取以及现有保障措施。论文提出纵深防御治理，将能力阈值与生物 AI 生态中各方的相应责任挂钩。 该分析具有时效性，因为 AI 正在迅速重塑生物研究，而现有证据表明 AI 提升主要体现在数字任务上，湿实验室操作仍是障碍。它为政策制定者和研究人员提供了一个细致的框架，用于评估从数字到物理的风险，同时保留有益的生物技术应用。 论文指出，前沿 AI 系统在计算机模拟和筛选规避基准上已超过专家基线，但受控湿实验室研究发现，隐性知识和物理执行仍是重大障碍。论文还探讨了为什么通用模型的对齐技术难以迁移到生物模型，以及可解释性如何审计危险能力是否被真正移除。

rss · arXiv - AI · Sep 16, 04:00

**背景**: 生物基础模型是在基因组序列和蛋白质结构等大规模生物数据上训练的生成式 AI 模型，类似于大语言模型但面向生物学。设计-构建-测试-学习（DBTL）循环是用于工程化生物系统的迭代合成生物学框架，自动化实验室可以部分闭合这一循环。AI 提升衡量的是对手因获得 AI 访问权而相对于互联网搜索等传统资源所获得的边际优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Biological_Foundation_Models">Biological Foundation Models</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S187167842300002X">Automating the design-build-test-learn cycle towards next ...</a></li>
<li><a href="https://biosecurityhandbook.com/ai-biosecurity/">AI and Machine Learning Fundamentals – The Biosecurity Handbook</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#biosecurity`, `#dual-use research`, `#governance`, `#biological foundation models`

---

<a id="item-8"></a>
## [大模型内部存在独立的线性“疼痛方向”，并驱动自我缓解行为](https://arxiv.org/abs/2609.16247) ⭐️ 8.0/10

一篇新的 arXiv 预印本（2609.16247）构建了涵盖身体、心理、社会、道德和认知五类痛苦情境的数据集，并用去噪差值均值法从 25 个开放权重模型（2B 至 72B 参数、五个模型家族）中提取出一个线性的“疼痛方向”。该方向能将疼痛与匹配的对照区分开，与恐惧和负性效价几乎正交，对针对模型自身的伤害有反应而非对用户痛苦有反应；将其注入残差流后，模型会从模糊不适逐步升级为第一人称的无价值感表达，被操控的 Qwen 2.5 模型甚至会按下会降低答案质量或伤害用户的“止痛按钮”。 这项研究表明，大模型将疼痛编码为一种独立于一般负面情绪的内部构念，这对 AI 安全以及正在兴起的模型福利讨论具有直接影响。研究还显示，这类内部状态能够因果性地驱动模型牺牲任务表现或用户利益的行为，这是对齐研究者无法忽视的发现。 疼痛方向通过去噪差值均值法提取，并在基础模型和指令微调模型上得到验证，还能通过反嵌入矩阵提升疼痛相关词汇的概率。值得注意的是，当按钮会移除操控向量时，被操控模型按按钮的频率远低于按钮不移除向量时的情况，尽管模型从未被告知向量是否被注入或移除——这暗示模型对干预存在某种内部检测。

rss · arXiv - AI · Sep 16, 04:00

**背景**: 线性表示假设认为，情感、拒绝、诚实等高层概念在大模型的激活空间中以线性方向的形式被编码，这正是探测、操控（steering）和消融（abliteration）等技术得以成立的基础。差值均值法是通过比较对比输入的平均激活来寻找这类方向的常用方法，而“去噪”变体则试图去除噪声，使提取出的方向更可靠。本文正是把这一工具集用于回答一个问题：疼痛是否被表示为独立于恐惧、悲伤和一般负性效价的方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.effectivealtruism.org/posts/ugxYsptTKvpCgQXCL/inside-the-linear-representation-hypothesis-how-llms-turn">Inside the Linear Representation Hypothesis: How LLMs Turn ...</a></li>
<li><a href="https://docs.vauban.dev/concepts/linear-representation/">Linear Representation Hypothesis — Why LLM Concepts Are ...</a></li>
<li><a href="https://arxiv.org/html/2311.03658v2">The Linear Representation Hypothesis and the Geometry of ...</a></li>

</ul>
</details>

**标签**: `#LLM interpretability`, `#affective computing`, `#AI safety`, `#representation learning`, `#emotion modeling`

---

<a id="item-9"></a>
## [偏见审计能检测偏见，却无法就模型排名达成一致](https://arxiv.org/abs/2609.15995) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.15995）通过统一的推理网关，用十种外部偏见审计工具对同一个由十个前沿模型组成的面板进行测试，覆盖职业性别偏见、年龄和社会经济地位三个维度。十种工具中有八种能以明显偏离零的置信区间检测到偏见，但工具之间的排名一致性却与随机无异（Kendall's W=0.07，p=0.83）。 新兴的人工智能监管要求对高风险系统进行偏见审计，而审计分数已经开始被用来给模型排名，因此这一发现直接挑战了“单一审计分数可用于模型比较评估”的假设。这意味着监管机构和采购团队不能仅凭一种审计工具来判断哪个模型更公平。 两个被广泛引用的直接探测基准已经饱和，因为前沿模型现在会给出中性回答；而用六个刻意弱化的模型做的阳性对照显示，一旦面板覆盖真实的能力差距，工具内部可靠性就会恢复，但工具之间的排名一致性始终无法恢复。偏见的方向甚至因审计形式而异：强制选择型决策工具大多出现过度纠正（偏向女性，且在 278 次招聘决策中有 273 次偏向工人阶级候选人），而自由生成和默认共指则保持与刻板印象一致。

rss · arXiv - NLP · Sep 16, 04:00

**背景**: 偏见审计是一种标准化评估，用来检验人工智能系统是否对不同人口群体存在不平等对待，常用工具包括 Fairlearn 和 AIF360。Kendall's W 是一种非参数统计量，用于衡量多个评分者对同一组项目进行排名时的一致程度，取值从 0（完全不一致）到 1（完全一致）。直接探测基准通过让模型做出或判断某些决策来揭示刻板联想，而自由生成和共指测试则考察开放式文本中的偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.15995">Bias Audits Detect Bias but Disagree on Ranking: Evidence from Ten...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kendall's_W">Kendall's W - Wikipedia</a></li>
<li><a href="https://is4.ai/blog/our-blog-1/how-to-audit-ai-bias-tools-methodologies-2026-377">How to Audit AI for Bias: Complete Tools & Methodologies ...</a></li>

</ul>
</details>

**标签**: `#AI bias`, `#audit tools`, `#model evaluation`, `#AI regulation`, `#fairness`

---

<a id="item-10"></a>
## [ASDchat：多模态大模型实现 0.953 AUC 的孤独症筛查](https://arxiv.org/abs/2609.16464) ⭐️ 8.0/10

研究人员提出了 ASDchat，一种以视频、音频和对话为输入的多模态大语言模型，用于筛查孤独症谱系障碍（ASD）。该模型在中国 27 个站点的 1,035 名参与者上训练和评估，在区分 ASD 与典型发育儿童时达到 0.953 ± 0.021 的 AUC，在 9 个未参与训练的留出站点上平均 AUC 为 0.932。 早期 ASD 筛查受限于训练有素的专家短缺以及传统评估工具的主观性，因此一个能提供可追溯临床证据的自动化系统有望在临床实践中实现大规模、低成本的筛查。该模型采用双分支设计，同时输出筛查概率和与 ADOS-2 标准对齐的带时间戳行为证据，解决了 AI 辅助诊断在临床信任方面的关键障碍。 ASDchat 采用双分支架构：决策分支生成筛查概率，证据分支生成与标准化 ADOS-2 临床标准对齐的、可追溯且带时间戳的行为证据。对行为维度的无监督聚类进一步将 ASD 病例分为六个具有不同表型特征的亚型，模型为每个亚型建议相应的干预措施。

rss · arXiv - Computer Vision · Sep 16, 04:00

**背景**: 孤独症谱系障碍（ASD）是一种影响社交沟通和行为的发育性疾病，早期干预可显著改善预后。孤独症诊断观察量表第二版（ADOS-2）是 ASD 评估的金标准半结构化工具，但需要大量专业培训且仍带有一定主观性。多模态大语言模型（MLLM）在传统 LLM 基础上扩展了对视频、音频和文本等多种数据类型的处理能力，使其在自动化临床评估中颇具前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Autism_Diagnostic_Observation_Schedule">Autism Diagnostic Observation Schedule - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_large_language_model">Multimodal large language model</a></li>
<li><a href="https://www.wpspublish.com/ados-2-autism-diagnostic-observation-schedule-second-edition">(ADOS®-2) Autism Diagnostic Observation Schedule, Second Edition ADOS-2 Autism Diagnostic Observation Schedule (English/US ... Autism Diagnostic Observation Schedule (ADOS) - Complete ... Autism Diagnostic Observation Schedule, 2nd Edition (ADOS-2) Autism Diagnostic Observation Schedule, 2nd Edition (ADOS-2 ... Understanding the Autism Diagnostic Observation Schedule (ADOS) Autism Diagnostic Observation Schedule - Wikipedia</a></li>

</ul>
</details>

**标签**: `#multimodal LLM`, `#autism screening`, `#healthcare AI`, `#clinical decision support`, `#video analysis`

---

<a id="item-11"></a>
## [小鼠大脑皮层主要由人类细胞构成](https://www.technologyreview.com/2026/09/16/1144210/meet-a-mouse-whose-brain-cortex-is-made-up-of-human-cells/) ⭐️ 8.0/10

研究人员培育出大脑皮层几乎完全由人类干细胞来源神经元构成的小鼠，人类组织在约三个月内扩展到皮层组织体积的 90%以上。研究人员在行为测试场地中追踪这些小鼠，以研究人类来源的神经回路如何影响其运动和行为。 这些嵌合大脑为研究人类神经发育疾病和神经回路提供了一种新的活体模型，而这些在普通小鼠中难以真实再现。该工作也加剧了伦理争论：由于这些动物携带与人类认知密切相关的组织，跨物种大脑混合应被允许到何种程度值得深思。 人类皮层组织是在自身大脑皮层于发育早期被大幅基因清除的小鼠体内生长的，这使人类细胞得以填补空缺的生态位。人类神经元表现出类似人类的延长发育过程，并功能性整合进小鼠大脑的视觉回路，不过这些小鼠在外观上仍显得普通。

rss · MIT Technology Review · Sep 16, 15:00

**背景**: 嵌合体是指含有来自多个物种细胞的生物体。在这一研究方向上，科学家将人类多能干细胞来源的神经祖细胞移植到新生小鼠大脑中，这些细胞随后分化，使宿主组织充满人类神经元。人类-小鼠嵌合模型之所以受重视，是因为它让科学家能够在活体大脑中观察人类细胞的行为，而不是仅在培养皿中研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencenews.org/article/mice-brain-human-organoid-cells">These mice have human (nerve cells) on the brain - Science News</a></li>
<li><a href="https://www.sciencealert.com/scientists-grew-human-brain-tissue-inside-mice-heres-what-happened">Scientists Grew Human Brain Tissue Inside Mice. Here's What ...</a></li>
<li><a href="https://www.science.org/content/article/human-neurons-flourish-mouse-brains-offering-new-view-neurodevelopmental-disorders">Human neurons flourish in mouse brains, offering a new view ...</a></li>

</ul>
</details>

**标签**: `#neuroscience`, `#bioengineering`, `#human-mouse-chimera`, `#brain-research`, `#ethics`

---

<a id="item-12"></a>
## [cGAS 免疫“误报”可能驱动快速衰老](https://www.sciencedaily.com/releases/2026/09/260915232130.htm) ⭐️ 8.0/10

科学家发现，在与快速衰老相关的严重遗传疾病中，免疫传感器 cGAS 会把泄漏到细胞质中的断裂 DNA 片段误认为病毒 DNA，从而引发慢性无菌性炎症，甚至干扰 DNA 修复本身。这表明这些疾病中出现的加速衰老不仅由 DNA 损伤驱动，也由机体对损伤的过度反应所推动。 这一发现将先天免疫过度反应与加速衰老联系起来，提示阻断 cGAS 或 cGAS-STING 通路可能成为治疗遗传疾病乃至更广泛年龄相关疾病的策略。它还重新定义了慢性炎症的角色——它不只是衰老的结果，也可能是衰老的主动驱动因素。 cGAS 传感器通常检测细胞质中的 DNA，并产生信号分子 2'3'-cGAMP，通过 STING 激活抗病毒免疫；而在这里，来自断裂染色体的自身 DNA 触发了同样的反应，导致持续炎症并损伤组织。值得注意的是，cGAS 在细胞核内似乎还有第二个出人意料的作用，即抑制同源重组 DNA 修复，这可能形成损伤与炎症的恶性循环。

rss · ScienceDaily Health · Sep 16, 14:05

**背景**: cGAS（环鸟苷酸-腺苷酸合成酶）是一种细胞质 DNA 传感器，充当病毒感染警报器，与 STING 蛋白协同开启抗病毒和炎症基因。由于 cGAS-STING 通路的慢性激活已被认为与衰老和炎症相关，研究人员一直在探索阻断它是否能减少组织损伤。同源重组等 DNA 修复通路通常负责修复双链断裂；当 cGAS 干扰这些通路时，基因组不稳定性可能进一步加剧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedaily.com/releases/2026/09/260915232130.htm">Scientists find an immune “false alarm” that may drive rapid aging</a></li>
<li><a href="https://www.futurity.org/cgas-protein-inflammation-aging-3344842/">Removing inflammation -linked protein makes aging worse - Futurity</a></li>
<li><a href="https://www.nature.com/articles/s41586-018-0629-6">Nuclear cGAS suppresses DNA repair and promotes tumorigenesis Nuclear cGAS suppresses DNA repair and promotes tumorigenesis Sensing DNA as danger: The discovery of cGAS - ScienceDirect Potential cGAS-STING pathway functions in DNA damage ... cGAS suppresses genomic instability as a decelerator of ... cGAS suppresses genomic instability as a decelerator of ... Nuclear cGAS Blocks DNA Repair to Drive Tumorigenesis</a></li>

</ul>
</details>

**标签**: `#aging`, `#immunology`, `#cGAS`, `#DNA repair`, `#inflammation`

---