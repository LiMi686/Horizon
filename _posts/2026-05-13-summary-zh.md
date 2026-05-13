---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 94 items, 40 important content pieces were selected

---

1. [dnsmasq 六个严重 CVE：远程代码执行风险](#item-1) ⭐️ 9.0/10
2. [LLMs-from-scratch：用 PyTorch 从零构建 GPT 类大模型](#item-2) ⭐️ 9.0/10
3. [首个全球 10 米分辨率农田地块边界图发布](#item-3) ⭐️ 9.0/10
4. [GitHub 仓库旨在恢复 Bambu 网络支持](#item-4) ⭐️ 8.0/10
5. [Elevator：无需启发式方法的确定性静态二进制翻译](#item-5) ⭐️ 8.0/10
6. [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](#item-6) ⭐️ 8.0/10
7. [Scrcpy v4.0 发布，带来灵活虚拟显示功能](#item-7) ⭐️ 8.0/10
8. [DuckDB 推出 Quack 客户端-服务器协议](#item-8) ⭐️ 8.0/10
9. [Obsidian 推出新社区网站与自动化插件审核](#item-9) ⭐️ 8.0/10
10. [CloakBrowser：隐形 Chromium 浏览器绕过所有机器人检测](#item-10) ⭐️ 8.0/10
11. [Fish Speech：最先进的开源多语言文本转语音系统](#item-11) ⭐️ 8.0/10
12. [LiteLLM：支持 100 多个 LLM 的开源 AI 网关](#item-12) ⭐️ 8.0/10
13. [Open Interpreter：计算机的自然语言界面](#item-13) ⭐️ 8.0/10
14. [MetaGPT：多智能体框架实现 AI 软件开发](#item-14) ⭐️ 8.0/10
15. [字节跳动开源 UI-TARS，实现 GUI 自动化](#item-15) ⭐️ 8.0/10
16. [VLM 可靠性隐藏在隐藏状态中，而非注意力](#item-16) ⭐️ 8.0/10
17. [自动评分作为奖励：用显式标准实现稳健多模态对齐](#item-17) ⭐️ 8.0/10
18. [面向偏好的嵌入，而非语义](#item-18) ⭐️ 8.0/10
19. [自由能框架区分能力激发与创造](#item-19) ⭐️ 8.0/10
20. [MemQ：基于溯源 DAG 的 Q 学习提升 LLM 智能体](#item-20) ⭐️ 8.0/10
21. [LLM 通过双重机制在上下文中学习图结构](#item-21) ⭐️ 8.0/10
22. [离散扩散语言模型的自适应引导](#item-22) ⭐️ 8.0/10
23. [Vertex-Softmax：通过精确 Softmax 优化实现紧致 Transformer 验证](#item-23) ⭐️ 8.0/10
24. [LLM 多样性崩溃归因于校准问题](#item-24) ⭐️ 8.0/10
25. [ClinicalBench：面向临床问答的断言感知检索压力测试](#item-25) ⭐️ 8.0/10
26. [双室模型：语言模型间的隐藏状态耦合](#item-26) ⭐️ 8.0/10
27. [差分隐私对 LLM 社会偏见的影响：结果不一](#item-27) ⭐️ 8.0/10
28. [指令影响语言模型的输出生成而非输入处理](#item-28) ⭐️ 8.0/10
29. [ReVision 将计算机智能体的视觉令牌使用量减少 46%](#item-29) ⭐️ 8.0/10
30. [Hebatron：希伯来语专用 MoE 语言模型](#item-30) ⭐️ 8.0/10
31. [ReAD：面向大语言模型的强化引导能力蒸馏框架](#item-31) ⭐️ 8.0/10
32. [HiDream-O1-Image：统一像素空间扩散 Transformer](#item-32) ⭐️ 8.0/10
33. [利用线性结构实现 VLM 背景不变表示](#item-33) ⭐️ 8.0/10
34. [视角主义分类器根据身份预测政治情感](#item-34) ⭐️ 8.0/10
35. [ABRA：放射学 AI 代理的新基准](#item-35) ⭐️ 8.0/10
36. [AdamW 训练 Transformer 的一致缩放极限](#item-36) ⭐️ 8.0/10
37. [未知网络干扰下的自适应策略学习的汤普森采样算法](#item-37) ⭐️ 8.0/10
38. [后 ADC 推断：主动数据收集后的有效推断](#item-38) ⭐️ 8.0/10
39. [树集成的最小最大速率与谱蒸馏](#item-39) ⭐️ 8.0/10
40. [锚点引导的方差感知奖励建模解决不可识别性问题](#item-40) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [dnsmasq 六个严重 CVE：远程代码执行风险](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT 发布了 dnsmasq 的六个严重安全漏洞 CVE，包括远程堆溢出、无限循环和缓冲区溢出，影响数百万台设备。 这些漏洞允许对嵌入式设备、路由器和 Android 中广泛使用的 DNS/DHCP 服务器进行远程代码执行和拒绝服务攻击，对网络基础设施构成重大威胁。 远程攻击者可通过 DNS 查询导致堆上的越界写入，通过畸形 DNS 响应触发无限循环，或利用恶意 DHCP 请求造成缓冲区溢出。

hackernews · chizhik-pyzhik · May 12, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48112042)

**背景**: dnsmasq 是一个轻量级开源 DNS 转发器和 DHCP 服务器，常用于家庭路由器、物联网设备和 Android。它专为小型网络设计，资源需求低。CVE（通用漏洞与暴露）系统为公开已知的安全漏洞提供标准化参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Heap_overflow">Heap overflow</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区表达了对采用内存安全语言的紧迫感，指出最近大多数漏洞源于 C 等非内存安全语言。用户还感叹 dnsmasq 在很少收到更新的设备中广泛使用，放大了风险。

**标签**: `#security`, `#dnsmasq`, `#CVE`, `#memory safety`, `#embedded systems`

---

<a id="item-2"></a>
## [LLMs-from-scratch：用 PyTorch 从零构建 GPT 类大模型](https://github.com/rasbt/LLMs-from-scratch) ⭐️ 9.0/10

Sebastian Raschka 发布了其著作《从零构建大语言模型》的官方代码仓库，提供了用 PyTorch 逐步实现开发、预训练和微调类 ChatGPT 大模型的完整代码。 该资源通过从零构建大模型的方式揭开了 LLM 的神秘面纱，使学生、研究人员和从业者能够理解高级 AI 概念，并弥合理论与实践之间的差距。 该仓库包含一个约 33K 参数的小型但功能完整的类 GPT 模型代码，并支持加载更大的预训练权重进行微调。代码仅使用 PyTorch，不依赖任何外部 LLM 库。

rss · GitHub Trending - Daily (All) · May 13, 14:40

**背景**: 像 GPT-4 这样的大语言模型驱动着许多 AI 应用，但其内部工作原理往往不透明。本书及代码仓库旨在通过引导读者从零实现类 GPT 模型，涵盖分词、注意力机制、训练和微调等环节，来教授其内部机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rasbt/LLMs-from-scratch">GitHub - rasbt/LLMs- from - scratch : Implement a ChatGPT- like LLM in...</a></li>
<li><a href="https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/1633437167">Build a Large Language Model (From Scratch): Raschka, Sebastian: 9781633437166: Amazon.com: Books</a></li>
<li><a href="https://www.goodreads.com/book/show/209234015-build-a-large-language-model">Build a Large Language Model (From Scratch) by Sebastian Raschka | Goodreads</a></li>

</ul>
</details>

**标签**: `#LLM`, `#PyTorch`, `#GPT`, `#deep learning`, `#tutorial`

---

<a id="item-3"></a>
## [首个全球 10 米分辨率农田地块边界图发布](https://arxiv.org/abs/2605.11055) ⭐️ 9.0/10

研究人员利用 U-Net 模型和 Sentinel-2 影像，制作了首个全球 10 米分辨率的农田地块边界图，覆盖 2024-2025 年，包含 241 个国家的 31.7 亿个多边形。 该数据集填补了关键空白，为作物监测、粮食安全和环境分析提供了全球一致、公开可用的地块级分析单元，取代了像素级产品。 该地图在 24 个国家的实地验证中平均像素级召回率达到 0.85，在奥地利、拉脱维亚和芬兰的 F1 分数分别为 0.89、0.88 和 0.74。还包含一个 500 米置信度图层以指示预测可靠性。

rss · arXiv - Computer Vision · May 13, 04:00

**背景**: 农田地块边界对于精准农业和政策制定至关重要，但此前缺乏全球地图。U-Net 是一种用于图像分割的深度学习架构，本研究使用 Fields of The World 数据集进行训练，该数据集覆盖 24 个国家的多样化农业景观。Sentinel-2 提供免费的高分辨率卫星影像。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fieldsofthe.world/">Fields of The World: A Global Field Boundary Ecosystem</a></li>
<li><a href="https://en.wikipedia.org/wiki/U-Net">U-Net - Wikipedia</a></li>

</ul>
</details>

**标签**: `#remote sensing`, `#agriculture`, `#deep learning`, `#geospatial`, `#field boundaries`

---

<a id="item-4"></a>
## [GitHub 仓库旨在恢复 Bambu 网络支持](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

一个 GitHub 仓库（FULU-Foundation/OrcaSlicer-bambulab）已被创建，旨在恢复 Bambu Lab 打印机的完整 Bambu 网络支持，此前一次有争议的固件更新移除了本地打印功能。 这一努力凸显了 3D 打印社区中用户权利与制造商控制之间日益紧张的关系，因为 Bambu Lab 的固件更新因限制本地打印并要求云认证而引发了广泛反对。 该仓库似乎是 OrcaSlicer 之前状态的克隆，该状态在 Bambu Lab 更改之前支持完整的本地网络打印。Bambu Lab 的新系统引入了两种模式：默认/云模式需要使用 Bambu Studio 或 Bambu Connect，以及功能受限的局域网模式。

hackernews · Murfalo · May 12, 21:55 · [社区讨论](https://news.ycombinator.com/item?id=48115127)

**背景**: Bambu Lab 是一家总部位于深圳的 3D 打印机制造商，由前大疆工程师创立。2025 年初，该公司宣布了一次固件更新，引入了授权控制系统，最初甚至要求本地局域网打印也需云认证，后在社区反对下部分撤回。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Bambu_Lab">Bambu Lab - Wikipedia</a></li>
<li><a href="https://consumerrights.wiki/w/Wiki/Bambu_Lab_Authorization_Control_System">Bambu Lab Authorization Control System - Consumer Rights Wiki</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈不满，用户称移除本地打印功能是“盗窃”，并批评 Bambu Lab 的做法。一些用户将 Bambu Lab 的系统与 Ubiquiti 更友好的远程访问模式进行不利比较，而另一些用户则指出，最初的反对迫使 Bambu Lab 在局域网模式要求上部分让步。

**标签**: `#3D printing`, `#open source`, `#firmware`, `#maker community`, `#Bambu Lab`

---

<a id="item-5"></a>
## [Elevator：无需启发式方法的确定性静态二进制翻译](https://arxiv.org/abs/2605.08419) ⭐️ 8.0/10

研究人员提出了 Elevator，这是首个完全静态的二进制翻译器，无需启发式方法、调试信息或源代码即可将整个 x86-64 可执行文件转换为 AArch64，实现了确定性翻译，性能与 QEMU 的 JIT 相当。 这项工作使得在监管行业（航空、医疗设备）中能够进行认证，这些行业无法接受 JIT，因为翻译后的代码必须是确定性的且可审计的。它也为在性能关键场景中使用静态二进制翻译而不依赖运行时回退打开了大门。 Elevator 考虑每个字节的所有可能解释，并提前为每种可行解释生成单独的翻译，导致 .text 段大小增加 50 倍。它原则上支持多线程和异常处理，但这些不在当前项目的范围内。

hackernews · matt_d · May 13, 04:25 · [社区讨论](https://news.ycombinator.com/item?id=48117810)

**背景**: 二进制翻译将可执行代码从一种指令集架构（ISA）转换为另一种。静态二进制翻译旨在执行前翻译所有代码，但传统方法依赖启发式方法来区分代码和数据，这可能会失败并需要运行时回退。QEMU 使用即时（JIT）编译进行动态翻译，比解释执行更快，但非确定性且不适合认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">[2605.08419] Deterministic Fully-Static Whole-Binary Translation without Heuristics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_translation">Binary translation - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2605.08419">Deterministic Fully-Static Whole-Binary Translation without Heuristics</a></li>

</ul>
</details>

**社区讨论**: 评论者强调认证角度是最引人注目的用例，指出监管行业无法使用 JIT。其他人认为 50 倍的代码大小增加是确定性的合理代价，并对处理间接跳转和 VM 保护二进制文件表示好奇。

**标签**: `#binary translation`, `#static analysis`, `#compilers`, `#performance`, `#systems`

---

<a id="item-6"></a>
## [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus 发布了 Needle，这是一个从 Gemini 蒸馏出的 2600 万参数工具调用模型，仅使用注意力和门控层，没有 MLP，在消费级设备上实现了 6000 tok/s 的预填充和 1200 tok/s 的解码速度。 这表明小型高效模型可以有效处理工具调用，使得在廉价手机、可穿戴设备和物联网设备上实现设备端智能体 AI 成为可能，无需依赖云端 API。 该模型在 16 个 TPU v6e 上使用 2000 亿 token 预训练了 27 小时，然后在 20 亿 token 的合成函数调用数据上后训练了 45 分钟。它在单次函数调用上优于 FunctionGemma-270M 和 Qwen-0.6B 等更大模型，但对话能力有限。

hackernews · HenryNdubuaku · May 12, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=48111896)

**背景**: 工具调用（或函数调用）允许 LLM 与外部工具（如 API、数据库或传感器）交互，从而实现智能体行为。模型蒸馏将知识从大型教师模型（如 Gemini）转移到较小的学生模型，降低计算成本。传统 Transformer 使用 MLP 进行推理，但 Needle 的架构表明，对于检索和组装任务，注意力和门控就足够了。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.ibm.com/think/topics/tool-calling">What Is Tool Calling? | IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者对模型在复杂工具使用中的判别能力表示兴趣，有人指出简单的天气查询十年前就已可解决。其他人则担心谷歌可能采取的反蒸馏防御措施，并建议发布实时演示。还有人兴奋地表示，将微型模型嵌入命令行工具以实现自然语言参数解析成为可能。

**标签**: `#tool calling`, `#model distillation`, `#on-device AI`, `#function calling`, `#efficient models`

---

<a id="item-7"></a>
## [Scrcpy v4.0 发布，带来灵活虚拟显示功能](https://github.com/Genymobile/scrcpy/releases/tag/v4.0) ⭐️ 8.0/10

Scrcpy v4.0 引入了可动态调整大小的灵活虚拟显示功能，并改进了性能，为 Android 屏幕镜像和控制带来新特性。 此次更新增强了 scrcpy 的多功能性，使其对需要同时操作多个显示或动态调整窗口大小的 Android 开发者、测试人员和高级用户更具价值。 新的 --flex-display（或 -x）标志允许虚拟显示随客户端窗口调整大小，scrcpy v4.0 还包含多项性能优化和错误修复。

hackernews · xnx · May 12, 20:50 · [社区讨论](https://news.ycombinator.com/item?id=48114356)

**背景**: Scrcpy 是一款免费开源工具，允许用户通过 USB 或无线方式从桌面电脑显示和控制 Android 设备，具有低延迟且无需 root 权限。它被开发者广泛用于应用测试、演示和远程控制。虚拟显示功能在 v3.0 中引入，允许镜像设备上的独立屏幕，而 v4.0 使其变得灵活可调。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Genymobile/scrcpy/blob/master/doc/virtual_display.md">scrcpy/doc/virtual_display.md at master · Genymobile/scrcpy</a></li>
<li><a href="https://en.wikipedia.org/wiki/Scrcpy">scrcpy - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员对灵活显示功能表示兴奋，有用户称 scrcpy 是一个令人惊叹的项目。其他人分享了创意用例，例如将手机用作网络桥接器，或通过 scrcpy-mobile 从 iOS 控制 Android。

**标签**: `#Android`, `#open-source`, `#screen mirroring`, `#tooling`, `#release`

---

<a id="item-8"></a>
## [DuckDB 推出 Quack 客户端-服务器协议](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB 宣布了名为 'Quack' 的新客户端-服务器协议，该协议支持远程连接和并发写入，从而实现水平扩展和更便捷的数据探索。 这解决了 DuckDB 嵌入式特性的一个关键限制，使其能够在多用户、网络化环境中使用，并跨机器扩展，从而拓宽了其在数据工程和分析领域的适用性。 Quack 协议支持通过网络传输完整的 DuckDB 功能集，并针对性能进行了优化。它作为 beta 扩展提供，允许网络上的任意两个 DuckDB 进程充当客户端和服务器。

hackernews · aduffy · May 12, 17:54 · [社区讨论](https://news.ycombinator.com/item?id=48111765)

**背景**: DuckDB 是一个嵌入式、进程内 SQL OLAP 数据库管理系统，传统上设计用于单进程使用。客户端-服务器协议允许远程访问和并发操作，这是大多数数据库的标准功能，但此前 DuckDB 缺少这一功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack : The DuckDB Client - Server Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">The quack : protocol allows you to introduce remote access to DuckDB .</a></li>
<li><a href="https://motherduck.com/blog/duckdb-client-server/">If It Quacks Like a Duck : DuckDB Gets a Client - Server Protocol</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，用户对解决远程访问和水平扩展等实际问题表示兴奋。一些用户指出需要更清晰的并发写入文档，而另一些用户则讨论了 DuckDB 不断演变的定位。

**标签**: `#DuckDB`, `#database`, `#client-server protocol`, `#scalability`, `#data engineering`

---

<a id="item-9"></a>
## [Obsidian 推出新社区网站与自动化插件审核](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian 宣布推出新的社区网站和自动化审核系统，以简化插件提交流程，解决因开发者倦怠和提交瓶颈导致几乎无法提交新插件的问题。 此次更新对 Obsidian 生态系统至关重要，它消除了一个主要的扩展瓶颈，减轻了开发者的挫败感，确保插件市场能够持续健康发展。 新系统包含针对恶意代码的自动检查，但部分社区成员认为，采用带有明确权限系统的沙盒机制在安全方面会更有效。

hackernews · xz18r · May 12, 15:45 · [社区讨论](https://news.ycombinator.com/item?id=48109970)

**背景**: Obsidian 是一款流行的笔记应用，拥有开放的插件 API，允许用户扩展其功能。插件生态系统发展迅速，已有数千个插件，但人工审核流程成为瓶颈，导致长时间延迟和开发者倦怠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.obsidian.md/Plugins/Releasing/Submit+your+plugin">Submit your plugin - Developer Documentation</a></li>
<li><a href="https://docs.obsidian.md/Plugins/Releasing/Submission+requirements+for+plugins">Submission requirements for plugins - Developer Documentation</a></li>

</ul>
</details>

**社区讨论**: 社区表达了宽慰和兴奋，许多人承认之前的瓶颈问题非常严重。然而，一些用户提出了安全担忧，认为自动检查不够充分，需要沙盒权限系统。CEO kepano 回应称，团队正在持续努力并欢迎反馈。

**标签**: `#Obsidian`, `#plugin ecosystem`, `#developer tools`, `#community management`, `#scaling`

---

<a id="item-10"></a>
## [CloakBrowser：隐形 Chromium 浏览器绕过所有机器人检测](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser 是一款隐形 Chromium 浏览器，通过应用 49 个源代码级 C++ 指纹补丁，通过了全部 30 项机器人检测测试，并可作为 Playwright 和 Puppeteer 的直接替代品。 该项目通过提供一个免费、开源解决方案来规避 Cloudflare Turnstile 和 reCAPTCHA v3 等高级反机器人系统，解决了网页抓取和自动化中的关键痛点，可能为开发者节省大量时间和成本。 CloakBrowser 在 C++ 源代码级别修改 Chromium，而非使用 JavaScript 注入或配置补丁，确保指纹与正常浏览器完全一致。它还包含 humanize=True 标志，用于模拟真实的鼠标移动和打字模式。

rss · GitHub Trending - Daily (All) · May 13, 14:40

**背景**: Playwright 和 Puppeteer 等浏览器自动化工具广泛用于测试和抓取，但许多网站部署了检测自动化信号的反机器人系统。传统的隐身方法通常依赖 JavaScript 补丁或配置调整，容易被检测到。CloakBrowser 则直接修补 Chromium 二进制文件本身，使其与真实用户的浏览器无法区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/CloakHQ/CloakBrowser">GitHub - CloakHQ/CloakBrowser: Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. · GitHub</a></li>
<li><a href="https://cloakbrowser.dev/">CloakBrowser — Stealth Chromium for Browser Automation</a></li>
<li><a href="https://playwright.dev/">Fast and reliable end-to-end testing for modern web apps | Playwright</a></li>

</ul>
</details>

**标签**: `#browser automation`, `#bot detection`, `#web scraping`, `#Playwright`, `#fingerprinting`

---

<a id="item-11"></a>
## [Fish Speech：最先进的开源多语言文本转语音系统](https://github.com/fishaudio/fish-speech) ⭐️ 8.0/10

Fish Speech 是由 Fish Audio 开发的最先进的开源文本转语音系统，支持多语言语音合成，具有高自然度和情感表现力。 该项目使高质量 TTS 技术大众化，使开发者和研究人员能够构建具有逼真语音生成的应用，而无需依赖专有服务。 该模型在约 50 种语言的超过 1000 万小时音频上训练，在 Seed-TTS Eval 上实现了评估模型中最低的词错误率，包括闭源系统。

rss · GitHub Trending - Python · May 13, 14:40

**背景**: 文本转语音（TTS）系统将书面文本转换为口语音频。像 Fish Speech 这样的开源 TTS 模型允许任何人使用、修改和部署该技术，从而促进语音应用、无障碍工具和内容创作领域的创新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/fishaudio/fish-speech">GitHub - fishaudio/fish-speech: SOTA Open Source TTS · GitHub</a></li>
<li><a href="https://speech.fish.audio/">Fish Audio</a></li>
<li><a href="https://huggingface.co/fishaudio/fish-speech-1.5">fishaudio/fish-speech-1.5 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#TTS`, `#open-source`, `#AI`, `#speech synthesis`, `#GitHub trending`

---

<a id="item-12"></a>
## [LiteLLM：支持 100 多个 LLM 的开源 AI 网关](https://github.com/BerriAI/litellm) ⭐️ 8.0/10

BerriAI 的 LiteLLM 是一个开源 AI 网关，提供统一的 SDK 和代理服务器，使用 OpenAI 格式调用超过 100 个 LLM API，并内置成本跟踪、护栏和负载均衡功能。 LiteLLM 简化了多提供商 LLM 集成，减少了开发开销，使团队无需重写代码即可切换或组合模型，从而加速 AI 应用的开发和部署。 LiteLLM 支持包括 Bedrock、Azure、OpenAI、VertexAI、Cohere、Anthropic、Sagemaker、HuggingFace、VLLM 和 NVIDIA NIM 在内的提供商，并提供虚拟密钥、支出跟踪和管理仪表板等企业级功能。

rss · GitHub Trending - Python · May 13, 14:40

**背景**: AI 网关作为中间件管理 LLM API 调用，处理集成、路由、安全和优化。护栏是监控和规范用户与 LLM 交互的安全控制，而负载均衡则将请求分配到多个资源以优化性能并避免过载。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/API_gateway">API gateway</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-gateway">What Is An AI Gateway? | IBM</a></li>
<li><a href="https://www.wiz.io/academy/ai-security/llm-guardrails">LLM Guardrails Explained: Securing AI Applications in Production | Wiz</a></li>

</ul>
</details>

**标签**: `#LLM`, `#API Gateway`, `#OpenAI`, `#Python`, `#AI/ML`

---

<a id="item-13"></a>
## [Open Interpreter：计算机的自然语言界面](https://github.com/openinterpreter/open-interpreter) ⭐️ 8.0/10

Open Interpreter 是一个开源工具，允许用户通过自然语言控制计算机，在本地通过类似 ChatGPT 的终端界面执行代码（Python、JavaScript、Shell 等）。 该项目通过提供 GPT-4 代码解释器的免费本地替代方案，使 AI 辅助自动化大众化，让开发者和非开发者都能通过简单对话自动完成数据分析、文件编辑和网络研究等任务。 Open Interpreter 默认使用 OpenAI 的 GPT-4o，但支持其他提供商和本地模型；出于安全考虑，执行任何代码前需要用户批准。

rss · GitHub Trending - Python · May 13, 14:40

**背景**: 像 GPT-4 这样的大型语言模型可以生成代码，但通常在沙盒环境中运行。Open Interpreter 将此能力带到用户本地机器，让 LLM 直接与操作系统、文件和应用程序交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openinterpreter/open-interpreter">GitHub - openinterpreter/open-interpreter: A natural language interface for computers · GitHub</a></li>
<li><a href="https://docs.openinterpreter.com/getting-started/introduction">Introduction - Open Interpreter</a></li>
<li><a href="https://docs.openinterpreter.com/code-execution/usage">Usage - Open Interpreter</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#natural-language-interface`, `#automation`, `#Python`

---

<a id="item-14"></a>
## [MetaGPT：多智能体框架实现 AI 软件开发](https://github.com/FoundationAgents/MetaGPT) ⭐️ 8.0/10

MetaGPT 是一个多智能体框架，为 GPT 智能体分配不同角色（如产品经理、架构师、工程师），使其协作完成从单一自然语言需求开始的复杂软件开发任务。该框架近期推出了全球首个 AI 智能体开发团队 MGX（MetaGPT X），其论文 AFlow 被 ICLR 2025 接收为口头报告（前 1.8%）。 该框架代表了向自然语言编程迈出的重要一步，通过允许非程序员用简单需求生成代码，可能降低软件开发的门槛。同时，它展示了多智能体协作如何克服单个 LLM 智能体在复杂多步骤任务中的局限性。 MetaGPT 将标准操作程序（SOP）编码为提示序列，实现智能体之间的结构化协作。该框架能从一行输入中输出用户故事、竞品分析、需求、数据结构、API 和文档。

rss · GitHub Trending - Python · May 13, 14:40

**背景**: 自然语言编程旨在让用户使用日常语言而非传统编程语言来创建软件。MetaGPT 基于这一概念，通过多个具有特定角色的 LLM 智能体模拟软件公司的工作流程。该框架利用 GPT 模型，并在 GitHub 上获得了广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/FoundationAgents/MetaGPT">GitHub - FoundationAgents/MetaGPT: 🌟 The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming</a></li>
<li><a href="https://arxiv.org/abs/2308.00352">[2308.00352] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework</a></li>
<li><a href="https://docs.deepwisdom.ai/main/en/guide/get_started/introduction.html">MetaGPT: The Multi-Agent Framework | MetaGPT</a></li>

</ul>
</details>

**标签**: `#multi-agent`, `#LLM`, `#software development`, `#AI framework`, `#natural language programming`

---

<a id="item-15"></a>
## [字节跳动开源 UI-TARS，实现 GUI 自动化](https://github.com/bytedance/UI-TARS) ⭐️ 8.0/10

字节跳动开源了 UI-TARS，这是一个原生 GUI 智能体框架，包含模型、论文和部署工具，最新版本 UI-TARS-2 于 2025 年 9 月 4 日发布，增强了在 GUI、游戏、代码和工具使用方面的能力。 UI-TARS 代表了从重度封装的商业模型向端到端原生智能体的转变，其性能优于现有框架，有望通过提高 GUI 交互的效率和可及性，改变软件测试、无障碍和桌面自动化领域。 UI-TARS-1.5 基于视觉语言模型构建，并利用强化学习实现高级推理，在标准基准测试上取得了最先进的结果。该框架包含桌面应用（UI-TARS-desktop），并与 Midscene.js 集成用于 Web 自动化。

rss · GitHub Trending - Python · May 13, 14:40

**背景**: 传统的 GUI 自动化依赖于脚本化工作流或带有自定义提示的商业 AI 模型。UI-TARS 是一个原生智能体，以截图作为输入并执行类人交互（键盘和鼠标），无需专家精心设计的提示和工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bytedance/ui-tars">GitHub - bytedance/UI-TARS: Pioneering Automated GUI Interaction with Native Agents · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2501.12326">[2501.12326] UI-TARS: Pioneering Automated GUI Interaction with Native Agents</a></li>
<li><a href="https://seed.bytedance.com/en/ui-tars">Introducing UI-TARS-1.5 - ByteDance Seed</a></li>

</ul>
</details>

**标签**: `#GUI automation`, `#AI agents`, `#open-source`, `#ByteDance`, `#software testing`

---

<a id="item-16"></a>
## [VLM 可靠性隐藏在隐藏状态中，而非注意力](https://arxiv.org/abs/2605.08200) ⭐️ 8.0/10

一篇新论文驳斥了视觉语言模型（VLM）中的注意力-置信度假设，表明注意力图与正确性的相关性几乎为零（R_pb=0.001）。该论文引入了 VLM 可靠性探针（VRP）流水线，对三个 VLM 系列（LLaVA-1.5、PaliGemma、Qwen2-VL）进行机制性可靠性分析。 这挑战了 VLM 可解释性和 AI 安全中的常见直觉，表明注意力锐度对于可信度具有误导性。该发现可能引导未来研究转向隐藏状态几何和稀疏后期层电路进行可靠性监控。 研究发现，单个隐藏状态线性探针在 POPE 上对三个系列中的两个达到了 AUROC>0.95，而 K=10 时的自一致性是最强的行为预测因子（R_pb=0.43）。因果消融实验揭示了明显的架构差异：后期融合的 LLaVA 将可靠性集中在脆弱的后期瓶颈中，而早期融合的 PaliGemma 和 Qwen2-VL 则广泛分布可靠性。

rss · arXiv - AI · May 13, 04:00

**背景**: 视觉语言模型（VLM）同时处理图像和文本以生成输出。注意力-置信度假设认为，当注意力图尖锐地聚焦于相关区域时，模型更可靠。机制可解释性旨在通过分析注意力头和隐藏状态等组件来理解模型内部机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.16320">[2406.16320] What Do VLMs NOTICE? A Mechanistic Interpretability Pipeline for Gaussian-Noise-free Text-Image Corruption and Evaluation</a></li>
<li><a href="https://d2jud02ci9yv69.cloudfront.net/2025-04-28-vlm-understanding-29/blog/vlm-understanding/">Mechanistic Interpretability Meets Vision Language Models: Insights and Limitations | ICLR Blogposts 2025</a></li>
<li><a href="https://huggingface.co/blog/vlms">Vision Language Models Explained</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#interpretability`, `#mechanistic interpretability`, `#AI reliability`, `#attention`

---

<a id="item-17"></a>
## [自动评分作为奖励：用显式标准实现稳健多模态对齐](https://arxiv.org/abs/2605.08354) ⭐️ 8.0/10

Auto-Rubric as Reward (ARR) 提出一个框架，将隐式人类偏好转化为显式、组合式的评分标准，用于多模态生成式 AI 的奖励建模，并提出了 Rubric Policy Optimization (RPO) 将这些标准蒸馏为稳健的二元奖励以用于强化学习。 该工作通过将隐式偏好外化为可解释的评分标准，解决了 RLHF 中的奖励黑客和标量坍缩问题，实现了更可靠、数据高效的多模态对齐。在文本到图像生成和图像编辑基准上，它优于成对奖励模型和 VLM 评判器。 ARR 在任何成对比较之前，将 VLM 内化的偏好知识外化为提示特定的评分标准，抑制了位置偏差等评估偏差。RPO 随后使用基于评分标准的偏好决策来稳定策略梯度，取代了不透明的标量回归。

rss · arXiv - AI · May 13, 04:00

**背景**: 基于人类反馈的强化学习（RLHF）通常将多维人类偏好简化为标量或成对标签，这可能导致奖励黑客和细微差别丢失。最近的 Rubrics-as-Reward (RaR) 方法尝试使用显式标准，但大规模生成可靠标准仍具挑战。ARR 在此基础上通过从 VLM 的隐式知识自动生成评分标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cameronrwolfe.substack.com/p/rubric-rl">Rubric-Based Rewards for RL - Deep (Learning) Focus</a></li>
<li><a href="https://arxiv.org/html/2510.14738">AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning</a></li>
<li><a href="https://arxiv.org/abs/2507.17746">[2507.17746] Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains</a></li>

</ul>
</details>

**标签**: `#RLHF`, `#multimodal generative models`, `#reward modeling`, `#AI alignment`, `#rubrics`

---

<a id="item-18"></a>
## [面向偏好的嵌入，而非语义](https://arxiv.org/abs/2605.08360) ⭐️ 8.0/10

一篇新的 arXiv 论文指出，标准文本嵌入无法捕捉集体决策所需的偏好相似性，并提出使用合成训练数据来打破语义信号与偏好信号之间相关性的框架。 这项工作解决了将 AI 应用于民主过程和公平聚类时的一个根本性缺陷，有望实现从自由文本意见中更准确地聚合偏好。 论文将问题形式化为一个不变性问题：文本嵌入同时编码了与偏好相关的立场和语义干扰（如风格），并表明旨在打破相关性的合成数据在 11 个在线讨论数据集上提升了偏好预测。

rss · arXiv - AI · May 13, 04:00

**背景**: 设施选址问题和公平聚类是依赖于距离度量来表示相似性的优化技术。像 BERT 这样的标准文本嵌入衡量的是语义相似性，它与偏好相似性（即一个人对某个陈述的同意程度）相关但不相等。本文指出，当这种相关性被打破时，直接使用语义嵌入会导致错误的偏好聚合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Facility_location_problem">Facility location problem - Wikipedia</a></li>
<li><a href="https://www.fairclustering.com/">Fair Clustering Tutorial</a></li>

</ul>
</details>

**标签**: `#embeddings`, `#collective decision-making`, `#fair clustering`, `#preference learning`, `#AI alignment`

---

<a id="item-19"></a>
## [自由能框架区分能力激发与创造](https://arxiv.org/abs/2605.08368) ⭐️ 8.0/10

一篇新的 arXiv 论文提出了基于自由能的框架，在 LLM 后训练中操作性地区分能力激发与能力创造，引入了“可达支撑”概念。 该框架通过提供一种原则性方法来判断训练方法是否仅重新加权现有行为或扩展模型的可达行为空间，从而澄清了后训练研究中的一个核心争论，可能指导更有效的训练策略。 论文将“可达支撑”定义为模型在有限预算下实际能产生的行为集合，并认为 SFT 和 RL 都重新加权预训练参考分布，关键区别在于更新是否保持接近基础模型。

rss · arXiv - AI · May 13, 04:00

**背景**: 大型语言模型后训练通常包括监督微调（SFT）和强化学习（RL），但模仿与发现之间的区别一直存在争议。自由能原理起源于神经科学，描述系统如何通过最小化变分自由能来维持稳定，并已被应用于机器学习以理解感知和行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Free_energy_principle">Free energy principle - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2107.00140">[2107.00140] Applications of the Free Energy Principle to Machine Learning and Neuroscience</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8871280/">The Free Energy Principle for Perception and Action: A Deep Learning Perspective - PMC</a></li>

</ul>
</details>

**标签**: `#large language models`, `#post-training`, `#capability elicitation`, `#free-energy`, `#AI alignment`

---

<a id="item-20"></a>
## [MemQ：基于溯源 DAG 的 Q 学习提升 LLM 智能体](https://arxiv.org/abs/2605.08374) ⭐️ 8.0/10

MemQ 提出了一种方法，将 TD(λ)资格迹应用于记忆 Q 值，通过记录每个新记忆创建时检索了哪些记忆的溯源 DAG 向后传播信用。 这解决了当前 LLM 智能体记忆系统的一个关键局限——将记忆独立对待而忽略依赖链。通过改进信用分配，MemQ 在六个不同基准测试中均取得最高成功率，在多步任务上提升高达 5.7 个百分点。 信用权重按(γλ)^d 随 DAG 深度 d 衰减，用结构接近度替代时间距离。该方法被形式化为外生上下文 MDP，将外生任务流与内生记忆存储解耦。

rss · arXiv - AI · May 13, 04:00

**背景**: LLM 智能体中的情景记忆存储过去经验以供检索，但当前方法独立评估每个记忆的质量。TD(λ)资格迹是一种强化学习技术，根据最近性和频率沿时间序列分配信用。溯源 DAG 记录记忆之间的依赖关系，显示哪些记忆被用于创建其他记忆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuglr.medium.com/eligibility-trace-in-temporal-difference-learning-391aa94ba091">Eligibility trace in Temporal difference learning | by Guilin Zhu | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_decision_process">Markov decision process - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#LLM agents`, `#episodic memory`, `#credit assignment`, `#provenance DAG`

---

<a id="item-21"></a>
## [LLM 通过双重机制在上下文中学习图结构](https://arxiv.org/abs/2605.08405) ⭐️ 8.0/10

一篇新论文通过图随机游走任务提供了因果证据，表明 LLM 在上下文学习中同时编码局部和全局图结构，挑战了其仅仅是模式匹配的观点。 通过 PCA，作者发现中间混合比例下两种图拓扑被编码在正交的主子空间中。激活修补和引导实验因果地证实了后期层表示携带图族信息。

rss · arXiv - AI · May 13, 04:00

**背景**: 上下文学习（ICL）允许 LLM 通过基于包含示例的提示进行条件化，无需权重更新即可执行新任务。激活修补是一种机制可解释性技术，通过替换内部激活来测试因果关系。图随机游走任务涉及预测两个可能图之一上的游走的下一个节点，要求模型推断底层结构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.lakera.ai/blog/what-is-in-context-learning">What is In-context Learning, and how does it work: The Beginner’s Guide | Lakera – Protecting AI teams that disrupt the world.</a></li>
<li><a href="https://www.neelnanda.io/mechanistic-interpretability/attribution-patching">Attribution Patching: Activation Patching At Industrial Scale — Neel Nanda</a></li>
<li><a href="https://en.wikipedia.org/wiki/Random_walk">Random walk - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#in-context learning`, `#causal inference`, `#graph learning`, `#interpretability`

---

<a id="item-22"></a>
## [离散扩散语言模型的自适应引导](https://arxiv.org/abs/2605.10971) ⭐️ 8.0/10

该论文发现均匀干预调度会降低离散扩散语言模型（DLM）中受控生成的质量，并提出一种自适应调度器，将干预集中在目标属性正在形成的步骤上。 这项工作通过提供对属性形成的机制性理解，填补了 DLM 研究的关键空白，实现了在不降低质量的前提下进行精确的多属性控制，这对于内容审核和个性化生成等实际应用至关重要。 自适应调度器在同时控制三个属性时达到了高达 93%的引导强度，比最强基线高出最多 15 个百分点，其优势由承诺分布的单一离散统计量决定。

rss · arXiv - Machine Learning · May 13, 04:00

**背景**: 离散扩散语言模型通过并行迭代去噪所有位置来生成文本，不同于自回归模型逐个生成 token。DLM 的受控生成方法从自回归模型引入，但在每一步都施加均匀干预，本文表明这会降低质量。稀疏自编码器通过从激活中学习稀疏特征来解读模型内部机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.13759">[2506.13759] Discrete Diffusion in Large Language and Multimodal Models: A Survey</a></li>
<li><a href="https://arxiv.org/abs/2309.08600">[2309.08600] Sparse Autoencoders Find Highly Interpretable Features in Language Models</a></li>
<li><a href="https://arxiv.org/abs/2507.07050">[2507.07050] Discrete Diffusion Models for Language Generation</a></li>

</ul>
</details>

**标签**: `#diffusion language models`, `#controlled generation`, `#mechanistic interpretability`, `#sparse autoencoders`, `#NLP`

---

<a id="item-23"></a>
## [Vertex-Softmax：通过精确 Softmax 优化实现紧致 Transformer 验证](https://arxiv.org/abs/2605.10974) ⭐️ 8.0/10

这项工作提供了仅从分数区间可获得的最紧致可靠边界，显著提高了基于注意力的神经网络的认证验证率，对安全关键型 AI 系统至关重要。 Vertex-Softmax 在序列长度上实现对数线性复杂度，并集成到具有形式化可靠性保证的 CROWN 风格验证器中，在 MNIST、Fashion-MNIST 和 CIFAR-10 上以远低于 alpha-CROWN 和分支定界基线的成本，持续匹配或超越它们。

rss · arXiv - Machine Learning · May 13, 04:00

**背景**: 神经网络的认证验证旨在为输入扰动下的模型行为提供形式化保证。对于 Transformer，在区间约束下对 softmax 函数进行定界是一个关键挑战，因为现有的松弛方法会引入松弛量。CROWN 是一个使用凸松弛计算输出边界的神经网络验证框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/IBM/CROWN-Robustness-Certification">CROWN: A Neural Network Verification Framework for ... - GitHub</a></li>
<li><a href="https://arxiv.org/abs/1811.00866">Efficient Neural Network Robustness Certification with General Activation ...</a></li>

</ul>
</details>

**标签**: `#transformer verification`, `#softmax optimization`, `#formal verification`, `#neural network verification`, `#CROWN`

---

<a id="item-24"></a>
## [LLM 多样性崩溃归因于校准问题](https://arxiv.org/abs/2605.11128) ⭐️ 8.0/10

一篇新论文提出了一个有效性-多样性框架，将 LLM 输出多样性崩溃归因于两种校准失调：顺序校准（有效 token 未能可靠地排在无效 token 之上）和形状校准（概率质量过度集中在少数有效 token 上）。 这项工作为 LLM 为何产生重复或狭窄输出提供了理论解释，这对改进创意生成、科学发现和 AI 安全至关重要。它表明多样性崩溃不仅仅是采样启发式问题，而是一个根本性的分布问题。 该框架将瓶颈分解为顺序和形状校准失调，并表明局部失败会在解码步骤中累积，导致显著的序列级多样性损失。对 14 个语言模型的实证测试证实了校准失调是一个普遍问题。

rss · arXiv - NLP · May 13, 04:00

**背景**: LLM 通过每一步预测下一个 token 的概率分布来生成文本。像 top-k 或 top-p 采样这样的解码策略依赖于模型的置信度排序和概率形状。当这些校准失调时，模型要么包含无效 token，要么集中在太少有效 token 上，从而降低多样性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11128v1">Calibration is the Diversity Bottleneck in LLMs - arXiv</a></li>
<li><a href="https://arxiv.org/html/2504.12522">Evaluating the Diversity and Quality of LLM Generated Content</a></li>

</ul>
</details>

**标签**: `#LLM`, `#diversity`, `#calibration`, `#decoding`, `#AI safety`

---

<a id="item-25"></a>
## [ClinicalBench：面向临床问答的断言感知检索压力测试](https://arxiv.org/abs/2605.11143) ⭐️ 8.0/10

研究人员推出了 ClinicalBench（一个基于 MIMIC-IV 中 43 名患者的 400 道题基准测试）和 EpiKG（一种断言感知检索方法），该方法在患者知识图谱中使用断言标签和时间性标签，根据问题意图路由检索，在精确匹配准确率上相比密集 RAG 基线提升了 22.0 个百分点。 这项工作通过关注真实电子健康记录笔记上的检索，填补了临床问答中的一个关键空白——否定、时间性和归属可能改变正确答案，并证明了断言感知检索显著优于标准方法，这对安全的临床决策支持至关重要。 主要终点基于两位外部医生评判的 50 个一致严格项目，显示提升了 22.0 个百分点（p=0.0192）。医生评判发现，56%的自动生成参考答案存在缺陷，凸显了临床问答基准中人工验证的必要性。

rss · arXiv - NLP · May 13, 04:00

**背景**: 基于电子健康记录的临床问答具有挑战性，因为笔记中包含否定发现（如“无胸痛”）、时间约束（如“既往史”与“当前”）以及归属问题（如家族史与患者自身）。标准的检索增强生成方法通常忽略这些细微差别，导致错误答案。EpiKG 通过构建患者知识图谱来解决这一问题，其中每个事实都标注了断言标签（如存在、不存在）和时间性标签（如过去、当前），然后根据问题意图路由检索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11143">ClinicalBench: Stress-Testing Assertion -Aware Retrieval for...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s00521-025-11666-9">A survey on retrieval-augmentation generation (RAG) models for healthcare applications | Neural Computing and Applications | Springer Nature Link</a></li>
<li><a href="https://aclanthology.org/2024.cl4health-1.23.pdf">Revisiting the MIMIC-IV Benchmark: Experiments Using ...</a></li>

</ul>
</details>

**标签**: `#clinical QA`, `#retrieval`, `#EHR`, `#benchmark`, `#NLP`

---

<a id="item-26"></a>
## [双室模型：语言模型间的隐藏状态耦合](https://arxiv.org/abs/2605.11167) ⭐️ 8.0/10

双室模型引入了一个可训练的神经接口，使两个冻结的语言模型能够通过连续的隐藏状态进行通信，无需文本序列化即可使用工具。在算术任务上，将两个 0.5B 模型与计算器耦合，准确率从 36%提升至 96%。 这项工作展示了工具增强型大语言模型的新范式，以极少的额外参数实现了显著的准确率提升。它有望在不重新训练大型模型的情况下，实现更高效、更强大的多模型系统。 该接口包括一个翻译网络和一个可学习的抑制门（约占组合参数的 1%），仅从任务损失中学习选择性通信协议。辅助模型可以从隐藏状态信号中生成特定于问题的代码，而无需看到问题文本。

rss · arXiv - NLP · May 13, 04:00

**背景**: 现有的多模型系统通过生成文本进行通信，每次交换都通过输出词汇表进行序列化。而双室模型则通过隐藏状态使用连续的并发通道，使两个模型在每个生成步骤中同步运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.11167v1">Bidirectional Hidden-State Coupling Between Parallel Language Models</a></li>
<li><a href="https://d2l.ai/chapter_recurrent-modern/bi-rnn.html">10.4. Bidirectional Recurrent Neural Networks — Dive into Deep Learning 1.0.3 documentation</a></li>

</ul>
</details>

**标签**: `#language models`, `#multi-model systems`, `#tool-augmented LLMs`, `#neural interfaces`, `#machine learning`

---

<a id="item-27"></a>
## [差分隐私对 LLM 社会偏见的影响：结果不一](https://arxiv.org/abs/2605.11195) ⭐️ 8.0/10

一项系统评估发现，差分隐私（DP）在句子评分任务中减少了 LLM 的社会偏见，但并非在所有任务中都有效，揭示了 logit 层面偏见与输出层面偏见之间的差距。 这项研究意义重大，因为它挑战了隐私保证会自动改善公平性的假设，表明 DP 对偏见的影响取决于任务，需要多范式评估。 该评估使用 DP-SGD 训练了一个预训练 LLM，并在四个范式（句子评分、文本补全、表格分类和问答）中与非 DP 基线进行了比较。

rss · arXiv - NLP · May 13, 04:00

**背景**: 差分隐私（DP）是一种限制单个训练数据点对模型影响程度的框架，通常通过 DP-SGD 实现。LLM 中的社会偏见是指模型输出基于性别或种族等属性的系统性不公平。Logit 层面偏见指在 token 选择之前的原始输出分数中的偏见，而输出层面偏见指最终生成文本中的偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2206.02617">[2206.02617] Individual Privacy Accounting for Differentially Private Stochastic Gradient Descent</a></li>
<li><a href="https://arxiv.org/pdf/2605.11195">How Does Differential Privacy Affect Social Bias in LLMs?</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/logit-bias">Logit Bias - LLM Parameter Guide - Vellum AI</a></li>

</ul>
</details>

**标签**: `#differential privacy`, `#social bias`, `#LLMs`, `#fairness`, `#privacy`

---

<a id="item-28"></a>
## [指令影响语言模型的输出生成而非输入处理](https://arxiv.org/abs/2605.11206) ⭐️ 8.0/10

一项新研究通过探测和基于注意力的干预，在五个二元判断任务中发现，语言模型中的指令主要影响输出生成而非输入处理。 这一发现挑战了关于指令在 LLM 中如何工作的常见假设，表明改进指令遵循可能需要关注生成阶段而非输入编码。 这种不对称性在不同模型家族和任务中得到了确认，并且随着模型规模和指令微调而加剧，后者对生成阶段的影响尤为显著。

rss · arXiv - NLP · May 13, 04:00

**背景**: 探测是一种通过在隐藏状态上训练分类器来分析神经网络内部表示的技术。基于注意力的干预通过操纵注意力模式来研究对模型行为的因果影响。本研究应用这些方法来理解指令如何影响语言模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.01333">Probing Language Models for Pre-training Data Detection - arXiv</a></li>
<li><a href="https://direct.mit.edu/coli/article/48/1/207/107571/Probing-Classifiers-Promises-Shortcomings-and">Probing Classifiers: Promises, Shortcomings, and Advances</a></li>
<li><a href="https://www.datacamp.com/blog/attention-mechanism-in-llms-intuition">Attention Mechanism in LLMs: An Intuitive Explanation</a></li>

</ul>
</details>

**标签**: `#LLM`, `#instruction-following`, `#cognitive science`, `#probing`, `#attention`

---

<a id="item-29"></a>
## [ReVision 将计算机智能体的视觉令牌使用量减少 46%](https://arxiv.org/abs/2605.11212) ⭐️ 8.0/10

研究人员提出了 ReVision 方法，通过移除连续截图中的冗余补丁，将计算机智能体的视觉令牌使用量减少约 46%，同时在三个基准测试中平均成功率提升 3%。 这解决了计算机智能体的一个关键瓶颈——视觉历史的高令牌成本——使得在固定预算下能够处理更长的轨迹，并揭示了以往性能饱和是由于令牌效率低下，而非历史信息的有用性有限。 ReVision 使用一个学习的补丁选择器，比较连续截图间的补丁表示并保留空间结构，在 OSWorld、WebTailBench 和 AgentNetBench 上使用 Qwen2.5-VL-7B 和 5 张历史截图进行了评估。

rss · arXiv - NLP · May 13, 04:00

**背景**: 计算机智能体通过将截图作为视觉令牌输入多模态语言模型来自动化 GUI 交互。随着轨迹变长，令牌成本迅速增加，限制了历史信息的整合。以往工作观察到增加历史信息时性能饱和，但 ReVision 表明这是由于冗余令牌而非收益递减。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/daixiangzi/Awesome-Token-Compress">GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub</a></li>
<li><a href="https://openai.com/index/computer-using-agent/">Computer - Using Agent | OpenAI</a></li>

</ul>
</details>

**标签**: `#computer-use agents`, `#visual token reduction`, `#multimodal language models`, `#GUI automation`, `#efficiency`

---

<a id="item-30"></a>
## [Hebatron：希伯来语专用 MoE 语言模型](https://arxiv.org/abs/2605.11255) ⭐️ 8.0/10

研究人员推出了 Hebatron，这是首个基于 NVIDIA Nemotron-3 架构的开放权重希伯来语专用混合专家语言模型，仅用 3B 活跃参数就达到了 73.8%的希伯来语推理准确率。 这项工作解决了希伯来语高质量 NLP 资源稀缺的问题，并展示了高效的 MoE 架构能够为低资源语言实现有竞争力的性能，可能降低其他语言的门槛。 该模型采用三阶段由易到难的课程学习并带有抗遗忘锚定，随后在 200 万双语样本上进行 SFT，支持高达 65,536 token 的原生上下文长度，推理吞吐量约为稠密模型的 9 倍。

rss · arXiv - NLP · May 13, 04:00

**背景**: 混合专家（MoE）模型每个 token 只激活一部分参数，从而在相似计算成本下实现更大的总容量。Nemotron-3 是 NVIDIA 的稀疏 MoE 架构，结合了 Mamba 和 Transformer 层。希伯来语 NLP 历史上缺乏大型开放模型，之前的工作如 DictaLM 和 AlephBERT 规模较小或是稠密模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Super-Technical-Report.pdf">Nemotron 3 Super: Open, Efficient Mixture-of-Experts ...</a></li>
<li><a href="https://arxiv.org/abs/2309.14568">[2309.14568] Introducing DictaLM -- A Large Generative Language Model for Modern Hebrew</a></li>
<li><a href="https://arxiv.org/abs/2104.04052">[2104.04052] AlephBERT:A Hebrew Large Pre-Trained Language Model to Start-off your Hebrew NLP Application With</a></li>

</ul>
</details>

**标签**: `#NLP`, `#Mixture-of-Experts`, `#Hebrew`, `#Language Model`, `#Efficient Inference`

---

<a id="item-31"></a>
## [ReAD：面向大语言模型的强化引导能力蒸馏框架](https://arxiv.org/abs/2605.11290) ⭐️ 8.0/10

研究人员提出了 ReAD，这是一个强化引导的能力蒸馏框架，显式建模跨能力迁移，以在固定 token 预算下改进面向特定任务的大语言模型压缩。 这项工作解决了现有能力蒸馏方法将能力视为独立训练目标的关键局限性，提供了一种更高效、更有效的方法来压缩大语言模型，同时保留与任务相关的能力。 ReAD 使用不确定性感知的上下文 bandit 算法，根据预期效用增益自适应分配蒸馏预算，实验表明，与强基线相比，它减少了有害溢出和浪费的蒸馏努力。

rss · arXiv - NLP · May 13, 04:00

**背景**: 能力蒸馏将知识蒸馏应用于选定的模型能力，以将大语言模型压缩为较小的模型，同时保留所需的能力。然而，现有方法通常将能力视为独立的，并忽略了跨能力迁移，这可能导致在固定 token 预算下性能次优。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.14216">Understanding Accuracy and Capability in LLM Reasoning - arXiv</a></li>
<li><a href="https://nebius.com/blog/posts/concept-behind-distilling-llm">The concept behind distilling an LLM - Nebius</a></li>
<li><a href="https://iclr.cc/virtual/2026/poster/10006741">Knowledge Fusion of Large Language Models via Modular SkillPacks</a></li>

</ul>
</details>

**标签**: `#LLM`, `#knowledge distillation`, `#model compression`, `#reinforcement learning`, `#capability transfer`

---

<a id="item-32"></a>
## [HiDream-O1-Image：统一像素空间扩散 Transformer](https://arxiv.org/abs/2605.11061) ⭐️ 8.0/10

HiDream-O1-Image 提出了一种原生统一的像素空间扩散 Transformer，将原始图像像素、文本标记和任务条件映射到单个共享标记空间，无需独立的编码器或 VAE。 该架构代表了从模块化到端到端视觉生成的范式转变，可能简化模型设计并提高可扩展性；仅用 8B 参数即可匹敌或超越 27B Qwen-Image 等更大模型，而 200B+版本则树立了新的 SOTA 基准。 该模型采用统一 Transformer（UiT）架构，将多种生成和编辑任务视为上下文推理，并已扩展到超过 200B 参数（HiDream-O1-Image-Pro），性能卓越。

rss · arXiv - Computer Vision · May 13, 04:00

**背景**: 传统图像生成模型依赖独立的文本编码器（如 CLIP）和变分自编码器（VAE）将图像压缩到潜在空间，这增加了复杂性并导致信息损失。像素空间扩散 Transformer 直接在原始像素上操作，避免了此类模块化组件。HiDream-O1-Image 通过将所有模态统一到单个标记空间，实现了真正的端到端方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2511.20645">PixelDiT: Pixel Diffusion Transformers for Image Generation - arXiv</a></li>
<li><a href="https://pixeldit.github.io/">PixelDiT: Pixel Diffusion Transformers</a></li>

</ul>
</details>

**标签**: `#image generation`, `#diffusion transformer`, `#unified architecture`, `#multimodal`, `#AI research`

---

<a id="item-33"></a>
## [利用线性结构实现 VLM 背景不变表示](https://arxiv.org/abs/2605.11107) ⭐️ 8.0/10

一种新的预训练方法利用 VLM 嵌入空间的线性可加性，将场景表示分解为前景和背景成分，在完美虚假相关条件下，在 Waterbirds 数据集上实现了超过 90%的最差组准确率。 这项工作解决了 VLM 中的一个关键鲁棒性问题，提供了一种实用且数据高效的方法来消除背景偏差，无需真实世界的去偏数据，可显著提升 VLM 在实际部署中的可靠性。 该方法使用合成数据构建背景不变表示，并展现出强大的模拟到真实迁移能力。在训练数据中无少数群体样本的 100%虚假相关条件下，首次在 Waterbirds 上实现了超过 90%的最差组准确率。

rss · arXiv - Computer Vision · May 13, 04:00

**背景**: 像 CLIP 这样的视觉语言模型（VLM）容易受到虚假相关的影响，例如将水鸟与水背景关联。Waterbirds 数据集是这一问题的基准，任务是将鸟类分类为水鸟或陆鸟，但背景与标签存在虚假相关。先前的方法通常需要组标注或去偏数据，获取成本高昂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kempnerinstitute.harvard.edu/research/deeper-learning/interpreting-the-linear-structure-of-vision-language-model-embedding-spaces/">Interpreting the Linear Structure of Vision-Language Model Embedding Spaces - Kempner Institute</a></li>
<li><a href="https://arxiv.org/abs/2204.02070">Improving Worst-group Accuracy with Spurious Attribute Estimation - arXiv</a></li>
<li><a href="https://arxiv.org/pdf/2510.02818">Mitigating Spurious Correlation via Distributionally Robust Learning...</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#robustness`, `#spurious correlations`, `#representation learning`, `#CLIP`

---

<a id="item-34"></a>
## [视角主义分类器根据身份预测政治情感](https://arxiv.org/abs/2605.11166) ⭐️ 8.0/10

一篇新论文提出了视角主义视觉政治情感（PVPS）分类器，该分类器从 5,575 名美国成年人的 82,000 条评估中学习，预测不同政治和社会身份群体如何评价同一张图像，保留分歧而非将其平均化。 这项工作挑战了计算社会科学中的标准单一评分方法，表明政治图像对不同受众传达不同含义，对政治传播、AI 公平性以及自动情感分析的有效性具有启示意义。 PVPS 分类器被应用于抗议图像研究，发现当考虑受众身份时，感知到的暴力和情感机制会发生实质性变化。该模型返回一个评估档案，记录谁同意、谁分歧以及沿着哪些身份维度。

rss · arXiv - Computer Vision · May 13, 04:00

**背景**: 政治和社会身份强烈影响人们如何评估政治信息，这是政治学中公认的发现。然而，大多数计算工具产生单一情感分数，隐含地假设图像对每个人都意味着相同的事情。AI 中的视角主义旨在保留多种有效视角，而非强制达成共识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2408.04103">[2408.04103] Decoding Visual Sentiment of Political Imagery</a></li>
<li><a href="https://arxiv.org/html/2405.05860v1">The Perspectivist Paradigm Shift: Assumptions and Challenges of Capturing Human Labels</a></li>

</ul>
</details>

**标签**: `#computational social science`, `#political sentiment`, `#perspectivism`, `#AI fairness`, `#visual sentiment analysis`

---

<a id="item-35"></a>
## [ABRA：放射学 AI 代理的新基准](https://arxiv.org/abs/2605.11224) ⭐️ 8.0/10

ABRA 是一个新的放射学 AI 代理基准，要求代理使用 21 个函数调用工具在真实的 DICOM 环境中操作，包含 655 个任务，涵盖三个难度级别和八种任务类型。 与使用预选图像的现有基准不同，ABRA 在真实的临床工作流程中测试代理，揭示当前模型由于感知瓶颈而执行得分高但结果得分低。 该基准使用 OHIF Viewer 和 Orthanc DICOM 服务器，任务包括查看器控制、元数据问答、注释和 BI-RADS 报告；自动评分评估规划、执行和结果。

rss · arXiv - Computer Vision · May 13, 04:00

**背景**: 放射学 AI 代理旨在通过与医学影像系统交互来辅助放射科医生。DICOM 是医学图像的标准格式，OHIF Viewer 和 Orthanc 服务器等工具常用于临床环境。BI-RADS 是乳腺影像报告的标准化系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/OHIF/Viewers">GitHub - OHIF / Viewers : OHIF zero-footprint DICOM viewer and...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Orthanc_(server)">Orthanc (server) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI Benchmark`, `#Radiology`, `#Medical AI`, `#Agent`, `#DICOM`

---

<a id="item-36"></a>
## [AdamW 训练 Transformer 的一致缩放极限](https://arxiv.org/abs/2605.11059) ⭐️ 8.0/10

一篇新论文证明，使用 AdamW 训练的 Transformer 的隐藏状态动态一致收敛到前向-后向 ODE 的解，并给出了依赖于深度 L 和注意力头数 H 的显式收敛速率。 这首次为 AdamW 优化下的 Transformer 缩放极限提供了严格的理论分析，揭示了深度和注意力头如何影响训练动态，可能指导架构设计和训练实践。 收敛速率为 O(L^{-1} + L^{-1/3} H^{-1/2})，当注意力头没有因果掩码时，极限 ODE 系统简化为 McKean–Vlasov ODE。这些界在紧初始条件上一致，并且在 AdamW 适应下与 token 数量和嵌入维度无关。

rss · arXiv - Data Science & Statistics · May 13, 04:00

**背景**: Transformer 是广泛用于 NLP 等领域的深度神经网络，通常使用 AdamW 优化器训练。理解其随深度增加的行为对于模型缩放至关重要。该工作将隐藏状态建模为通过注意力耦合的相互作用粒子系统，这一视角将 Transformer 动态与物理学中的平均场理论联系起来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/McKean–Vlasov_process">McKean–Vlasov process - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2007.02876">arXiv:2007.02876v2 [stat.ML] 20 Jul 2020 A Mathematical Theory of Attention</a></li>
<li><a href="https://optimization.cbe.cornell.edu/index.php?title=AdamW">AdamW - Cornell University Computational Optimization Open Textbook - Optimization Wiki</a></li>

</ul>
</details>

**标签**: `#transformers`, `#deep learning theory`, `#optimization`, `#scaling limits`, `#attention mechanism`

---

<a id="item-37"></a>
## [未知网络干扰下的自适应策略学习的汤普森采样算法](https://arxiv.org/abs/2605.11191) ⭐️ 8.0/10

本文提出了一种汤普森采样算法，通过吉布斯采样器在自适应实验中联合学习未知的干扰网络并优化个体层面的处理分配。 这项工作通过处理未知的网络干扰（这在社交网络和在线平台中很常见）填补了自适应实验中的一个关键空白，从而实现了更有效的策略学习和因果推断。 该算法在精确后验采样下实现了阶数为 √(nT·B log(en/B)) 的贝叶斯遗憾界，并且与现有方法相比，经验上实现了超过一个数量级的遗憾减少。

rss · arXiv - Data Science & Statistics · May 13, 04:00

**背景**: 自适应实验（如多臂老虎机）顺序分配处理以最大化累积奖励，但标准方法假设单元之间没有干扰。在许多现实场景中，例如社交网络，一个单元的结果依赖于邻居的处理，从而产生网络干扰。现有方法要么假设网络已知，要么使用粗略的聚类级随机化，这可能效率低下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thompson_sampling">Thompson sampling - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gibbs_sampling">Gibbs sampling - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC6935347/">Causal Inference Under Interference And Network Uncertainty - PMC</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#reinforcement learning`, `#network interference`, `#Thompson sampling`, `#adaptive experimentation`

---

<a id="item-38"></a>
## [后 ADC 推断：主动数据收集后的有效推断](https://arxiv.org/abs/2605.11511) ⭐️ 8.0/10

提出了一种名为后 ADC 推断的新框架，能够在数据自适应收集且推断目标事后确定的情况下实现有效的统计推断。该框架提供有效的 p 值和置信区间，纠正了主动数据收集和数据驱动目标构建带来的偏差。 这解决了黑箱优化和序贯模型优化中的一个基本问题，即传统推断因自适应采样偏差而失效。该框架具有广泛的适用性，且无需对黑箱函数或代理模型做出假设，使其在实际应用中切实可行。 该方法基于选择性推断，仅对观测噪声施加假设。实证结果表明，对于由 GP-UCB 和 TPE 算法收集的数据，该框架能提供有效的推断。

rss · arXiv - Data Science & Statistics · May 13, 04:00

**背景**: 主动数据收集（ADC）自适应地选择数据点，常见于黑箱优化中，导致样本有偏。事后推断是指在看到数据后才指定的统计分析，可能引入额外偏差。序贯模型优化（SMBO）方法如 TPE 和 GP-UCB 将评估集中在有希望的区域，加剧了偏差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post_hoc">Post hoc - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2603.08002v1">Post - Hoc Large-Sample Statistical Inference</a></li>
<li><a href="https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/11-LION5-SMAC.pdf">Sequential Model-Based Optimization for General Algorithm Conﬁguration</a></li>

</ul>
</details>

**标签**: `#statistical inference`, `#active data collection`, `#black-box optimization`, `#sequential model-based optimization`

---

<a id="item-39"></a>
## [树集成的最小最大速率与谱蒸馏](https://arxiv.org/abs/2605.11841) ⭐️ 8.0/10

本文推导了随机森林回归的最小最大最优收敛速率，并引入了谱蒸馏方法，在保持预测性能的同时压缩树集成模型。 它首次为随机森林提供了最小最大最优收敛结果，填补了统计学习理论中的空白，并提供了实用的压缩技术，可将模型大小减少几个数量级，适用于资源受限的应用。 谱视角揭示，核算子的主导特征函数（对于随机森林）或平滑矩阵的主导奇异向量（对于梯度提升机）捕获了主要预测方向，从而可以通过非线性映射进行蒸馏。

rss · arXiv - Data Science & Statistics · May 13, 04:00

**背景**: 随机森林和梯度提升等树集成方法被广泛使用，但缺乏完整的理论理解。最小最大最优性刻画了在最坏情况下的最佳可能收敛速率，而谱方法通过特征值和特征向量分析算子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.11841">Minimax Rates and Spectral Distillation for Tree Ensembles - arXiv</a></li>
<li><a href="https://arxiv.org/html/2605.11841v1">Minimax Rates and Spectral Distillation for Tree Ensembles - arXiv</a></li>

</ul>
</details>

**标签**: `#random forests`, `#gradient boosting`, `#spectral methods`, `#model compression`, `#statistical learning theory`

---

<a id="item-40"></a>
## [锚点引导的方差感知奖励建模解决不可识别性问题](https://arxiv.org/abs/2605.11865) ⭐️ 8.0/10

研究人员提出了锚点引导的方差感知奖励建模框架，通过用两个粗粒度的响应级锚点标签扩充偏好数据，解决了多元偏好场景下高斯奖励模型中的不可识别性问题，并提供了包括非渐近收敛率在内的理论保证。 这项工作解决了多元偏好场景下 Bradley-Terry 奖励模型的一个根本性局限，能够实现更准确的奖励建模并提升下游 RLHF 性能，这对于将大语言模型与多样化的人类价值观对齐至关重要。 该方法证明两个锚点足以实现识别，开发了联合训练目标，并为奖励均值和方差函数建立了非渐近收敛率。在模拟实验和四个真实世界数据集上，该方法持续提升了奖励建模和下游 RLHF（PPO 和最佳 N 选）的性能。

rss · arXiv - Data Science & Statistics · May 13, 04:00

**背景**: 标准的 Bradley-Terry 奖励模型假设每个响应有一个标量奖励，无法捕捉多元偏好中的分歧。高斯奖励模型联合预测均值和方差以表达不确定性，但存在不可识别性问题：不同的参数对可以从成对偏好中产生相同的似然。本文引入了锚点标签——对响应质量的粗粒度人工判断——来打破这种对称性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.11865">[2605.11865] Variance-aware Reward Modeling with Anchor Guidance</a></li>

</ul>
</details>

**标签**: `#reward modeling`, `#preference learning`, `#RLHF`, `#pluralistic preferences`, `#machine learning`

---