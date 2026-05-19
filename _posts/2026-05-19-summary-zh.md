---
layout: default
title: "Horizon Summary: 2026-05-19 (ZH)"
date: 2026-05-19
lang: zh
---

> From 93 items, 37 important content pieces were selected

---

1. [llama.cpp：在本地硬件上高效运行大语言模型](#item-1) ⭐️ 9.0/10
2. [NVIDIA 发布 Sana：高效线性扩散 Transformer](#item-2) ⭐️ 9.0/10
3. [Simon Willison 在 PyCon US 2026 上的五分钟 LLM 回顾](#item-3) ⭐️ 8.0/10
4. [Benedict Evans：AI 吃掉世界（2026 春季）](#item-4) ⭐️ 8.0/10
5. [Supertonic：基于 ONNX 的快速本地多语言 TTS](#item-5) ⭐️ 8.0/10
6. [RuView 将 WiFi 信号转化为隐私保护传感器](#item-6) ⭐️ 8.0/10
7. [CloakBrowser：隐身 Chromium 浏览器绕过机器人检测](#item-7) ⭐️ 8.0/10
8. [ShadowBroker：开源地理空间情报平台](#item-8) ⭐️ 8.0/10
9. [Articraft：利用 LLM 大规模生成可动 3D 资产](#item-9) ⭐️ 8.0/10
10. [AgentWall：本地 AI 代理的运行时安全层](#item-10) ⭐️ 8.0/10
11. [ANNEAL：LLM 代理通过符号补丁修复流程知识](#item-11) ⭐️ 8.0/10
12. [AI 代理让科学家通过自然语言自动化实验室](#item-12) ⭐️ 8.0/10
13. [Skim：面向高效网络代理的推测执行框架](#item-13) ⭐️ 8.0/10
14. [LLM 谈判者缺乏战略博弈能力](#item-14) ⭐️ 8.0/10
15. [TTE-Flash：潜在思考令牌提升多模态嵌入](#item-15) ⭐️ 8.0/10
16. [LinAlg-Bench 揭示 LLM 在 4x4 矩阵上的数学失败阈值](#item-16) ⭐️ 8.0/10
17. [苹果 M3 Ultra 上实时扩散模型达 22.7 FPS](#item-17) ⭐️ 8.0/10
18. [IBPO：面向 LLM 推理的反事实信用分配](#item-18) ⭐️ 8.0/10
19. [SignMuon：1 比特分布式优化器将通信量降低 32 倍](#item-19) ⭐️ 8.0/10
20. [自对弈强化学习中的对抗性动作移除](#item-20) ⭐️ 8.0/10
21. [决策容量阈值导致自博弈强化学习崩溃](#item-21) ⭐️ 8.0/10
22. [AdaGraph：图原生聚类算法克服维度灾难](#item-22) ⭐️ 8.0/10
23. [语言游戏实现与非神经系统的对话](#item-23) ⭐️ 8.0/10
24. [LLM 智能体系统中技能的缩放定律](#item-24) ⭐️ 8.0/10
25. [CHI-Bench：评估 AI 代理在复杂医疗工作流中的表现](#item-25) ⭐️ 8.0/10
26. [受语言习得装置启发的预预训练提升 LLM 数据效率](#item-26) ⭐️ 8.0/10
27. [基于检索的法律标注方法超越生成式大模型](#item-27) ⭐️ 8.0/10
28. [Noise2Params：基于光子统计统一事件相机模型](#item-28) ⭐️ 8.0/10
29. [GeoSym127K：可扩展的神经符号几何推理引擎](#item-29) ⭐️ 8.0/10
30. [StreamPro：流式视频中的主动决策](#item-30) ⭐️ 8.0/10
31. [TaTok：使用全局令牌的自适应图像令牌化](#item-31) ⭐️ 8.0/10
32. [StAD：利用 Stein 算子实现扩散模型快速似然估计](#item-32) ⭐️ 8.0/10
33. [预测干预博弈与不变集](#item-33) ⭐️ 8.0/10
34. [傅里叶分析揭示神经网络的简单性偏好](#item-34) ⭐️ 8.0/10
35. [用于随机偏微分方程不确定性量化的随机算子网络](#item-35) ⭐️ 8.0/10
36. [含噪归纳矩阵补全实现样本效率](#item-36) ⭐️ 8.0/10
37. [安杜里尔与 Meta 合作开发军用 AR 眼镜](#item-37) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [llama.cpp：在本地硬件上高效运行大语言模型](https://github.com/ggml-org/llama.cpp) ⭐️ 9.0/10

llama.cpp 是一个 C/C++ 库，能够在消费级硬件（包括 CPU 和 GPU）上高效运行大语言模型推理。该项目获得了大量社区采用，并持续添加多模态支持、Hugging Face 缓存集成等新功能。 该项目通过允许用户在本地运行大语言模型，无需昂贵的云基础设施，从而降低了使用门槛，增强了隐私保护并支持离线使用。其高性能和广泛的硬件支持使其成为开源 AI 生态系统的关键工具。 llama.cpp 使用 GGML 张量库，并支持整数量化以减少内存占用。最近的更新包括 llama-server 的多模态支持、用于 FIM 补全的 VS Code 扩展，以及 Hugging Face Inference Endpoints 对 GGUF 的原生支持。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: 大语言模型通常需要强大的 GPU 和大量内存，使得本地部署具有挑战性。llama.cpp 利用 GGML 张量库，该库针对消费级硬件进行了优化，并支持多种量化技术以减小模型大小和内存占用。这使得 LLaMA 等模型可以在从笔记本电脑到树莓派的设备上运行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ggml-org/ggml">GitHub - ggml-org/ggml: Tensor library for machine learning</a></li>
<li><a href="https://ggml.ai/">ggml.ai</a></li>

</ul>
</details>

**社区讨论**: 社区表现出极大的热情，讨论集中在为下游消费者改进打包方式以及使用新 WebUI 的指南上。与 NVIDIA 合作支持 gpt-oss 模型也获得了积极反馈。

**标签**: `#LLM`, `#inference`, `#C++`, `#machine learning`, `#open source`

---

<a id="item-2"></a>
## [NVIDIA 发布 Sana：高效线性扩散 Transformer](https://github.com/NVlabs/Sana) ⭐️ 9.0/10

NVIDIA 发布了 Sana，这是一个面向高效高分辨率图像和视频生成的代码库，采用线性扩散 Transformer 架构，将二次复杂度降低到接近线性。该版本包含多个模型变体，如 SANA、SANA-1.5、SANA-Sprint、SANA-Video、SANA-WM 和 Sol-RL，支持高达 4096×4096 分辨率，并可在笔记本电脑 GPU 上部署。 Sana 显著降低了高分辨率图像合成的计算门槛，使其可在消费级硬件（如单张 RTX 3090）上运行。其线性注意力机制和深度压缩自编码器为生成式 AI 树立了新的效率标准，有望加速在创意工具、游戏和具身 AI 应用中的普及。 Sana 使用深度压缩自编码器，比传统自编码器压缩图像 8 倍以上，其线性注意力将复杂度从 O(N^2)降低到接近 O(N)。该代码库包含完整的训练和推理流程，并提供在单张 RTX 3090 上运行的 4 位量化、ControlNet 和 SANA-Sprint 演示。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: 扩散模型是一类生成模型，通过迭代去噪随机噪声来生成高质量图像。传统的扩散 Transformer（DiT）使用二次复杂度的注意力机制，在高分辨率下计算成本高昂。线性注意力以接近线性的复杂度近似标准注意力，从而高效扩展到更大图像。Sana 在此基础上进一步优化，包括深度压缩自编码器和高效训练方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvlabs.github.io/Sana/">Efficient High-Resolution Image Synthesis</a></li>
<li><a href="https://arxiv.org/abs/2410.10629">[2410.10629] SANA: Efficient High-Resolution Image Synthesis with ...</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，该仓库获得了大量星标和分支。Discord 和 GitHub 上的讨论显示，用户对线性注意力方法以及在消费级 GPU 上运行的能力充满热情，但也有用户对现有工作流的兼容性和自定义训练的学习曲线提出疑问。

**标签**: `#diffusion models`, `#image synthesis`, `#NVIDIA`, `#transformer`, `#generative AI`

---

<a id="item-3"></a>
## [Simon Willison 在 PyCon US 2026 上的五分钟 LLM 回顾](https://simonwillison.net/2026/May/19/5-minute-llms/#atom-everything) ⭐️ 8.0/10

Simon Willison 在 PyCon US 2026 上做了一个闪电演讲，总结了过去六个月 LLM 的发展，使用他的注释演示工具重点介绍了 2025 年 11 月的转折点，当时“最佳”模型在 Anthropic、OpenAI 和 Google 之间易手五次。 这次演讲提供了对 LLM 快速发展的简洁、高价值的概述，帮助开发者和研究人员快速把握关键趋势和模型变化，尤其是在编码能力方面的激烈竞争。 Willison 使用他的“骑自行车的鹈鹕”SVG 测试来说明模型差异，指出从 2025 年 11 月开始，Claude Sonnet 4.5、GPT-5.1、Gemini 3、GPT-5.1 Codex Max 和 Claude Opus 等模型相继占据榜首。

rss · Simon Willison · May 19, 01:09 · [社区讨论](https://news.ycombinator.com/item?id=48188183)

**背景**: Simon Willison 是著名的 Python 开发者，也是 Datasette 项目的创建者。他的注释演示工具允许演讲者为幻灯片图像添加详细注释和替代文本，使演讲更易于访问和分享。“骑自行车的鹈鹕”测试是他用来评估 LLM 图像生成能力的一个趣味基准，该任务不太可能出现在训练数据中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/May/19/5-minute-llms/">The last six months in LLMs in five minutes</a></li>
<li><a href="https://tools.simonwillison.net/annotated-presentations">Annotated Presentation Creator - tools.simonwillison.net</a></li>
<li><a href="https://us.pycon.org/2026/schedule/presentation/175/">Lightning Talks - PyCon US 2026</a></li>

</ul>
</details>

**社区讨论**: Hacker News 评论者讨论了 LLM 在非程序员和复杂编码任务中的实际局限性，一些人指出虽然模型有所改进，但在完整应用开发上仍有困难。其他人则强调了 2026 年春季的安全转折点。

**标签**: `#LLMs`, `#AI`, `#PyCon`, `#lightning talk`, `#Simon Willison`

---

<a id="item-4"></a>
## [Benedict Evans：AI 吃掉世界（2026 春季）](https://static1.squarespace.com/static/50363cf324ac8e905e7df861/t/6a0af5d0484fbf5fe9a7743e/1779103184855/2026-Spring-AI.pdf) ⭐️ 8.0/10

Benedict Evans 发布了 2026 年春季演讲《AI 吃掉世界》，这是一份 79 页的幻灯片，分析了 AI 行业从规模争论到产品部署的演变。 该演讲提供了对 AI 平台转变的高价值时间视角，强调了模型商品化以及价值向应用、工作流和专有数据上移的趋势。 Evans 的临时论点指出，模型很可能成为基础设施，而价值则向上层转移到应用、工作流、产品、专有数据/上下文、市场推广以及由廉价自动化带来的新问题。

hackernews · topherjaynes · May 18, 12:49 · [社区讨论](https://news.ycombinator.com/item?id=48179021)

**背景**: Benedict Evans 是一位知名的科技分析师，每半年发布一次关于宏观和战略技术趋势的演讲。他的 2026 年春季演讲是该系列的最新一期，追踪 AI 的影响，此前已有 2024 年 11 月和 2025 年 5 月的版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ben-evans.com/presentations">Presentations — Benedict Evans</a></li>
<li><a href="https://news.ycombinator.com/item?id=48179021">AI eats the world (Spring 26) [pdf] | Hacker News</a></li>
<li><a href="https://www.techtwitter.com/articles/ai-is-eating-the-world-79-slide-deck-from-benedict-evans">"AI Is Eating The World" 79 slide deck from Benedict Evans</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者欣赏这种时间视角，并就模型商品化展开辩论，有人将 AI 实验室比作移动电信公司或云服务提供商。一位评论者指出，巨型模型可能隐藏着低效，将当前方法比作大型机时代。

**标签**: `#AI`, `#industry analysis`, `#platform shifts`, `#Benedict Evans`, `#technology trends`

---

<a id="item-5"></a>
## [Supertonic：基于 ONNX 的快速本地多语言 TTS](https://github.com/supertone-inc/supertonic) ⭐️ 8.0/10

Supertone Inc. 发布了 Supertonic，这是一个开源的多语言文本转语音系统，通过 ONNX Runtime 完全在本地运行，支持 31 种语言，模型参数仅 99M。 Supertonic 无需依赖云端即可在边缘设备上实现高质量、低延迟的 TTS，保护隐私并降低成本，对无障碍、物联网和移动应用具有重要意义。 该模型输出 44.1kHz 16-bit WAV 音频，支持 <laugh> 和 <breath> 等表情标签，并提供 Python、Node.js、WebGPU、Java、C++、C#、Go、Swift、iOS、Rust 和 Flutter 的 SDK。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: ONNX Runtime 是一个跨平台的机器学习推理加速器，支持来自 PyTorch、TensorFlow 等框架的模型。WebGPU 使得在浏览器中直接进行 GPU 加速推理成为可能。Supertonic 利用这些技术，在包括 Raspberry Pi 和电子阅读器在内的各种硬件上本地运行 TTS。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform, high performance ML inferencing and training accelerator · GitHub</a></li>
<li><a href="https://onnxruntime.ai/docs/">ONNX Runtime | onnxruntime</a></li>
<li><a href="https://onnxruntime.ai/">ONNX Runtime | Home</a></li>

</ul>
</details>

**标签**: `#TTS`, `#ONNX`, `#multilingual`, `#on-device`, `#open-source`

---

<a id="item-6"></a>
## [RuView 将 WiFi 信号转化为隐私保护传感器](https://github.com/ruvnet/RuView) ⭐️ 8.0/10

RuView 是一个新的开源平台，利用普通 WiFi 信号检测存在、追踪运动并监测呼吸和心率等生命体征，全程无需摄像头或可穿戴设备。 该技术为智能家居、医疗保健和安全领域提供了隐私保护的传感方案，有望在敏感区域替代摄像头，同时利用现有的 WiFi 基础设施。 RuView 运行在低成本的 ESP32 节点上（每个低至 9 美元），利用 WiFi 信号的信道状态信息（CSI），无摄像头姿态估计的 PCK@20 约为 2.5%，目标通过摄像头监督达到 35% 以上。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: WiFi 传感通过分析无线电波如何被人体运动和呼吸干扰来工作，利用标准 WiFi 硬件的信道状态信息（CSI）。此前卡内基梅隆大学的“DensePose from WiFi”研究展示了从 WiFi 信号进行姿态估计，而 RuView 将其带到实用的边缘设备上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NTUMARS/Awesome-WiFi-CSI-Sensing">GitHub - NTUMARS/Awesome-WiFi-CSI-Sensing: A list of awesome papers and cool resources on WiFi CSI sensing. · GitHub</a></li>
<li><a href="https://info.support.huawei.com/info-finder/encyclopedia/en/CSI+Sensing.html">What Is CSI Sensing? - Huawei</a></li>
<li><a href="https://github.com/espressif/esp-csi">GitHub - espressif/esp-csi: Applications based on Wi-Fi CSI (Channel state information), such as indoor positioning, human detection · GitHub</a></li>

</ul>
</details>

**标签**: `#WiFi sensing`, `#spatial intelligence`, `#vital sign monitoring`, `#privacy-preserving`, `#IoT`

---

<a id="item-7"></a>
## [CloakBrowser：隐身 Chromium 浏览器绕过机器人检测](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser 是一款开源隐身 Chromium 浏览器，通过 49 个源码级 C++ 补丁修改浏览器指纹，通过了全部 30 项机器人检测测试，并获得了 0.9 的 reCAPTCHA v3 评分。 该项目解决了网页自动化和爬取中的关键痛点，提供了一个可直接替代 Playwright 的方案，能够绕过 Cloudflare Turnstile 和 DataDome 等高级反机器人系统，可能为开发者节省大量时间和资源。 CloakBrowser 可通过 pip 和 npm 安装，自动下载修改后的 Chromium 二进制文件，并包含 humanize=True 标志，可模拟类人鼠标移动和打字模式，进一步规避行为检测。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: 浏览器指纹是一种网站根据浏览器和设备的独特特征（如 Canvas 渲染、WebGL 和音频信号）来识别和追踪用户的技术。像 Playwright 这样的自动化浏览器常被反机器人服务检测到，因为它们暴露了自动化信号，导致被屏蔽或出现验证码。CloakBrowser 在 C++ 源码层面修补这些信号，使其与普通浏览器无法区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques : 6 Top Methods Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>
<li><a href="https://www.techtimes.com/articles/316664/20260515/cloakhqs-open-source-chromium-fork-defeats-cloudflare-datadome-perimeterx-without-configuration.htm">CloakHQ's Open-Source Chromium Fork Defeats Cloudflare, DataDome, and ...</a></li>

</ul>
</details>

**标签**: `#web automation`, `#browser fingerprinting`, `#anti-bot`, `#Playwright`, `#stealth browser`

---

<a id="item-8"></a>
## [ShadowBroker：开源地理空间情报平台](https://github.com/BigBodyCobain/Shadowbroker) ⭐️ 8.0/10

ShadowBroker 是一个新的开源地理空间情报平台，它将来自 60 多个公共来源的实时数据（包括公务机、间谍卫星和地震事件）聚合到一个统一的地图界面中，并集成了 AI 进行关联分析。 该平台使之前分散在多个工具中的全球遥测数据得以民主化访问，使分析师、研究人员和公众能够实时监控和关联事件。其开源特性允许完全审计和自托管，解决了隐私问题。 该平台基于 Next.js、MapLibre GL、FastAPI 和 Python 构建，具有 35 多个可切换的数据层，包括 SAR 地面变化检测，以及多种视觉模式（DEFAULT、SATELLITE、FLIR、NVG、CRT）。它包含一个可选的 Shodan 连接器，用于操作员提供的 API 访问。

rss · GitHub Trending - Daily (All) · May 19, 06:31

**背景**: 开源情报（OSINT）涉及收集和分析公开可用的数据以用于情报目的。许多全球遥测源，如飞机 ADS-B、海上 AIS 和卫星轨道数据，已经是公开的，但分散在不同的平台上。ShadowBroker 将这些数据聚合到一个界面中，使发现关联变得更加容易。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/BigBodyCobain/Shadowbroker">GitHub - BigBodyCobain/ Shadowbroker : Open-source intelligence for...</a></li>
<li><a href="https://www.explainx.ai/tools/shadowbroker">Shadowbroker — AI tool | explainx.ai | explainx.ai</a></li>
<li><a href="https://beta.pinokio.co/apps/github-com-dsrpt-shadowbroker-pinokio">Shadowbroker on Pinokio</a></li>

</ul>
</details>

**标签**: `#OSINT`, `#geospatial intelligence`, `#open-source`, `#AI`, `#real-time data`

---

<a id="item-9"></a>
## [Articraft：利用 LLM 大规模生成可动 3D 资产](https://github.com/mattzh72/articraft) ⭐️ 8.0/10

Articraft 是一个开源代理系统，利用 LLM 从文本描述以编程方式生成可动 3D 资产，绕过了传统的手动建模工具。 该方法能够规模化、自动化地创建可用于仿真的可动物体，可能显著加速机器人、游戏和 VR/AR 应用的 3D 内容管线。 该系统通过让 LLM 针对自定义 SDK 编写 Python 代码来生成资产，产出具有语义部件、稳健几何和物理关节的物体。它支持多种 LLM 提供商，并包含一个本地查看器用于检查。

rss · GitHub Trending - Python · May 19, 06:31

**背景**: 可动 3D 资产——具有铰链或关节等运动部件的物体——传统上在 Blender 等工具中手动创建，耗时且难以规模化。Articraft 将问题重新定义为代码生成，利用 LLM 编写程序以编程方式构建此类资产的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/mattzh72/articraft">mattzh72/articraft: An Agentic System for Scalable Articulated ...</a></li>
<li><a href="https://articraft3d.github.io/">Articraft: An Agentic System for Scalable Articulated 3 D Asset ...</a></li>
<li><a href="https://www.alphaxiv.org/audio/2605.15187">Articraft: An Agentic System for Scalable Articulated 3 D Asset ...</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#LLM`, `#computer graphics`, `#AI`, `#open source`

---

<a id="item-10"></a>
## [AgentWall：本地 AI 代理的运行时安全层](https://arxiv.org/abs/2605.16265) ⭐️ 8.0/10

AgentWall 是一个新的运行时安全层，它在执行前拦截每个 AI 代理提议的操作，根据声明式策略进行评估，并对敏感操作要求人工批准。 这通过在执行边界强制执行策略，填补了 AI 代理安全的关键空白，防止在本地环境中发生文件删除或凭证泄露等不安全行为。 AgentWall 在 14 项基准测试中实现了 92.9%的策略执行准确率，且开销低于毫秒级；它作为策略强制的 MCP 代理和 OpenClaw 插件实现。

rss · arXiv - AI · May 19, 04:00

**背景**: AI 代理正从被动的文本生成器演变为能够执行命令、修改文件和调用 API 的主动行动者。现有的安全措施如模型对齐和输入过滤无法在运行时控制操作，使本地环境面临风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.16265v1">AgentWall: A Runtime Safety Layer for Local AI Agents</a></li>
<li><a href="https://agentwall.dev/">AgentWall - Stop your AI agent before it goes too far</a></li>
<li><a href="https://github.com/reesepj/agentwall">GitHub - reesepj/agentwall: Runtime defense for agentic AI. Control ...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#autonomous agents`, `#runtime security`, `#local AI`

---

<a id="item-11"></a>
## [ANNEAL：LLM 代理通过符号补丁修复流程知识](https://arxiv.org/abs/2605.16309) ⭐️ 8.0/10

ANNEAL 提出了一种神经符号方法，使 LLM 代理能够通过生成受控的符号补丁来修复流程知识图中的重复执行错误，而无需修改模型权重。 这解决了自进化代理的一个关键限制——在安全保证下持久消除故障——并可能使 LLM 代理在复杂的现实任务中更可靠地部署。 核心机制——故障驱动知识获取（FDKA）——定位负责的操作符，通过受约束的 LLM 生成合成类型化补丁，并在提交前通过多维评分、符号护栏和金丝雀测试进行验证。

rss · arXiv - AI · May 19, 04:00

**背景**: LLM 代理经常在同一个故障上反复失败，因为底层的流程知识——操作符模式、前置条件和约束——未被修复。现有的自进化方法更新提示、记忆或权重，但不直接修复编码任务执行的符号结构。ANNEAL 通过结合神经生成与符号治理填补了这一空白。

**标签**: `#LLM Agents`, `#Neuro-Symbolic AI`, `#Self-Evolving Systems`, `#Knowledge Graphs`, `#AI Safety`

---

<a id="item-12"></a>
## [AI 代理让科学家通过自然语言自动化实验室](https://arxiv.org/abs/2605.16552) ⭐️ 8.0/10

研究人员提出了一种 AI 代理架构，将大语言模型与实验编排系统（EOS）集成，使科学家能够通过自然语言创建和监控自动化实验室协议。该代理首次尝试协议生成成功率达 97%，并将所需界面操作减少一个数量级。 这一突破降低了实验室自动化的门槛，使没有编程专长的科学家也能设计和运行复杂实验。它通过让自主实验室更易用、更高效，加速了材料科学、药物开发和生物学领域的科学发现。 该 AI 代理在具有自动验证和纠错功能的代理循环下运行，支持从协议创建到结果分析的完整实验生命周期。可视化图形编辑器将协议呈现为交互式节点图，支持在 AI 辅助和手动构建之间无缝切换。

rss · arXiv - AI · May 19, 04:00

**背景**: 传统实验室自动化需要科学家编写代码并管理复杂软件来协调仪器和机器人。实验编排系统（EOS）是一个软件框架，作为自主实验室的基础，处理任务调度、设备控制和优化活动。这项工作将大语言模型集成到 EOS 中，以实现自然语言交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://unc-robotics.github.io/eos/index.html">The Experiment Orchestration System ( EOS ) — EOS</a></li>
<li><a href="https://ieeexplore.ieee.org/document/11128578/">The Experiment Orchestration System ( EOS )... | IEEE Xplore</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#laboratory automation`, `#large language models`, `#scientific discovery`, `#orchestration`

---

<a id="item-13"></a>
## [Skim：面向高效网络代理的推测执行框架](https://arxiv.org/abs/2605.16565) ⭐️ 8.0/10

Skim 提出了一种推测执行框架，通过离线分析和轻量级验证，绕过昂贵的 LLM 推理来处理常规网络代理任务，在无精度损失的情况下将每任务中位成本降低 1.9 倍，延迟降低 33.4%。 这项工作解决了当前网络代理的高成本和延迟问题——当前代理每一步都依赖前沿模型推理和 ReAct 式规划。通过利用可预测的网站结构，Skim 使网络代理更适用于实际部署，可能推动 AI 驱动自动化的更广泛应用。 Skim 的离线分析器为每个站点捕获稳定的 URL 模式、答案格式和任务到轨迹的映射。运行时，它将查询匹配到模板，合成 URL，并使用小模型提取答案，轻量级验证器对快速路径输出进行把关；罕见的错误推测会回退到完整代理，并由快速路径的最终 URL 热启动以保留上游轨迹进度。

rss · arXiv - AI · May 19, 04:00

**背景**: 网络代理是自主在网站上执行任务的 AI 系统，通常使用大型语言模型（LLM）进行规划和推理。ReAct 式规划将推理轨迹与行动交织在一起，但计算成本高昂。推测执行是一种计算机体系结构中的技术，通过预测来加速处理，此处将其应用于网络代理，以跳过常规查询中不必要的 LLM 调用。

**标签**: `#web agents`, `#speculative execution`, `#LLM efficiency`, `#systems`

---

<a id="item-14"></a>
## [LLM 谈判者缺乏战略博弈能力](https://arxiv.org/abs/2605.16575) ⭐️ 8.0/10

arXiv 上的一项新研究揭示，大型语言模型智能体能够建模对手偏好，但无法将这一知识转化为战略谈判，常常做出损害自身利益的让步。 这一发现凸显了 LLM 在多智能体战略推理中的关键局限，对 AI 对齐以及需要战略权衡的现实谈判应用具有重要意义。 该研究使用受控的多属性讨价还价环境，发现即使智能体准确建模了对手偏好，它们也无法持续地将让步与自身高价值属性的收益配对，导致最终协议严重受初始锚点影响。

rss · arXiv - AI · May 19, 04:00

**背景**: 谈判涉及推断对方需求并利用该信息在多轮中提出有利报价。战略推理使智能体能够有效合作、沟通和竞争。本研究测试了 LLM 智能体是否能在讨价还价场景中执行此类推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semanticscholar.org/paper/Strategic-Reasoning-with-Language-Models-Gandhi-Sadigh/f1a3cd5cc340f47e3e966709f7dfddef23460aa2">[PDF] Strategic Reasoning with Language Models | Semantic Scholar</a></li>

</ul>
</details>

**标签**: `#LLM`, `#negotiation`, `#AI alignment`, `#multi-agent systems`, `#strategic reasoning`

---

<a id="item-15"></a>
## [TTE-Flash：潜在思考令牌提升多模态嵌入](https://arxiv.org/abs/2605.16638) ⭐️ 8.0/10

TTE-Flash 用潜在思考令牌替代昂贵的显式思维链推理，用于多模态嵌入，在恒定推理成本下达到可比性能。TTE-Flash-2B 模型在 MMEB-v2 基准测试上优于其显式 CoT 对应模型。 这项工作解决了基于推理的多模态表示中的关键效率瓶颈，无需高昂计算开销即可获得高质量嵌入。它可能加速检索、分类和视频理解等应用。 该方法使用 CoT 生成损失优化思考令牌，并通过对比损失优化嵌入令牌，涉及两种令牌提取和训练的架构设计。在 15 个视频数据集上的零样本评估显示，随着思考令牌数量增加呈现扩展行为，并提示自适应预算分配。

rss · arXiv - AI · May 19, 04:00

**背景**: 通用多模态嵌入（UME）受益于思维链（CoT）推理，但生成显式 CoT 轨迹计算成本高昂。潜在思考令牌是指导推理的内部表示，无需生成显式文本，提供了一种更高效的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/thinking-tokens">Thinking Tokens</a></li>
<li><a href="https://arxiv.org/html/2505.16782v1">Reasoning Beyond Language: A Comprehensive Survey on Latent ...</a></li>
<li><a href="https://www.luiscardoso.dev/blog/neuralese">Thinking Without Words | Luis Cardoso</a></li>

</ul>
</details>

**标签**: `#multimodal embeddings`, `#chain-of-thought`, `#latent reasoning`, `#efficiency`, `#representation learning`

---

<a id="item-16"></a>
## [LinAlg-Bench 揭示 LLM 在 4x4 矩阵上的数学失败阈值](https://arxiv.org/abs/2605.16675) ⭐️ 8.0/10

研究人员推出了 LinAlg-Bench，这是一个诊断性基准，用于评估 10 个前沿 LLM 在 3x3、4x4 和 5x5 矩阵上的线性代数任务，揭示了在 4x4 尺度上模型从执行错误转变为计算放弃的明显行为阈值。 该基准提供了一个结构化的失败分析流程，能够识别特定的错误类型，表明 LLM 的数学推理失败是由于工作记忆限制而非知识差距，这可以指导模型架构和训练的改进。 该基准包含 660 个经 SymPy 认证的问题，涵盖 9 种任务类型，并采用三阶段取证流程将 1,156 个失败分类为十种主要错误标签，其中工具角色扮演和约束一致虚构是新的失败模式。

rss · arXiv - AI · May 19, 04:00

**背景**: 大型语言模型（LLM）通常在复杂数学推理上表现不佳，但以往的基准只关注整体准确率，未分析失败模式。SymPy 是一个用于符号数学的开源 Python 库，用于验证正确答案。取证流程自动化了错误分类，揭示了 LLM 推理中的结构性约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SymPy">SymPy</a></li>

</ul>
</details>

**标签**: `#LLM`, `#benchmark`, `#mathematical reasoning`, `#linear algebra`, `#failure analysis`

---

<a id="item-17"></a>
## [苹果 M3 Ultra 上实时扩散模型达 22.7 FPS](https://arxiv.org/abs/2605.16259) ⭐️ 8.0/10

研究人员通过将蒸馏专用模型 SDXS-512 的 CoreML 转换与三线程相机流水线相结合，在苹果 M3 Ultra 上实现了 22.7 FPS 的实时相机到图像转换。 这项工作表明，针对 CUDA GPU 的优化策略不能直接迁移到苹果 Silicon 的统一内存架构，为在非 NVIDIA 平台上部署扩散模型提供了实用指南。 该研究探索了 10 个优化阶段，包括 CoreML 转换、量化、Token Merging、神经引擎利用和知识蒸馏，发现量化和并行推理在苹果 Silicon 上效果不佳。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 扩散模型是一类生成式 AI 模型，通过迭代去噪随机噪声来生成高质量图像。在消费级硬件上实现实时推理通常依赖 NVIDIA GPU 和 CUDA 优化，但苹果 Silicon 使用统一内存架构，行为不同。Token Merging (ToMe) 通过合并冗余 token 来加速 Transformer，而 SDXS-512 是为快速推理设计的蒸馏模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/diffusers/v0.19.0/optimization/tome">Token Merging</a></li>
<li><a href="https://arxiv.org/abs/2303.17604">[2303.17604] Token Merging for Fast Stable Diffusion</a></li>
<li><a href="https://huggingface.co/IDKiro/sdxs-512-dreamshaper">IDKiro/ sdxs - 512 -dreamshaper · Hugging Face</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#Apple Silicon`, `#real-time inference`, `#model optimization`, `#img2img`

---

<a id="item-18"></a>
## [IBPO：面向 LLM 推理的反事实信用分配](https://arxiv.org/abs/2605.16302) ⭐️ 8.0/10

研究人员提出了隐式行为策略优化（IBPO），这是一种基于反事实比较的信用分配框架，可降低大语言模型多步推理中的梯度方差。 这解决了 LLM 强化学习中的一个关键瓶颈——稀疏的终端奖励导致训练不稳定——并可能显著提升数学和代码生成等复杂推理任务的性能。 IBPO 在相同输入下采样多条推理轨迹，并利用它们的差异作为隐式优势估计器，提供步骤敏感的学习信号，将稀疏奖励转化为密集反馈。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 用于 LLM 多步推理的强化学习通常依赖稀疏的终端奖励，这些奖励被均等地传播到所有中间步骤，导致高梯度方差和低效更新。信用分配是衡量每个动作对未来奖励贡献的问题，反事实推理通过比较替代决策来隔离动作的效果。先前的工作如 Counterfactual Credit Assignment (CCA)和 COMA 在无模型和多智能体设置中探索了类似的想法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2011.09464">[2011.09464] Counterfactual Credit Assignment in Model-Free...</a></li>
<li><a href="https://kunkuang.github.io/papers/KDD21-ShapleyMARL.pdf">Shapley Counterfactual Credits for Multi-Agent Reinforcement ...</a></li>
<li><a href="https://proceedings.mlr.press/v139/mesnard21a/mesnard21a.pdf">Counterfactual Credit Assignment in Model-Free Reinforcement ...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#large language models`, `#credit assignment`, `#multi-step reasoning`, `#counterfactual reasoning`

---

<a id="item-19"></a>
## [SignMuon：1 比特分布式优化器将通信量降低 32 倍](https://arxiv.org/abs/2605.16311) ⭐️ 8.0/10

研究人员提出 SignMuon，一种结合 signSGD 的多数投票符号聚合与 Muon 的极坐标步长框架的分布式优化器，每次迭代仅需 1 比特梯度通信，实现了 O(1/sqrt(T))的收敛速度。 该工作解决了大规模神经网络分布式训练中的通信瓶颈，相比 float32 实现 32 倍带宽缩减，同时保持强收敛保证和实际性能提升。 SignMuon 使用 Newton-Schulz 迭代进行局部极分解，仅传输通过多数投票聚合的逐元素符号，在 330 种配置下对 CIFAR-10/ResNet-50 达到 92.15%的验证准确率。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 分布式训练通常需要通信全精度梯度，随着模型规模增长成为瓶颈。SignSGD 通过仅传输梯度符号来减少通信，而 Muon 通过极坐标步长利用矩阵结构进行优化。SignMuon 结合了这两种方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://kellerjordan.github.io/posts/muon/">Muon : An optimizer for hidden layers in neural networks</a></li>
<li><a href="https://grokipedia.com/page/newtonschulz-iteration">Newton–Schulz iteration</a></li>

</ul>
</details>

**标签**: `#distributed training`, `#optimization`, `#communication efficiency`, `#deep learning`

---

<a id="item-20"></a>
## [自对弈强化学习中的对抗性动作移除](https://arxiv.org/abs/2605.16312) ⭐️ 8.0/10

该论文提出了自对弈强化学习中的对抗性动作掩蔽，攻击者选择性移除受害者动作集中的合法动作，在多种算法和领域中造成显著损害。 这项工作将动作可用性确定为自对弈强化学习中一个独特的鲁棒性表面，凸显了一种可能影响竞争环境中 RL 系统安全性和可靠性的新漏洞。 该攻击对 Q-learning、PPO、NFSP、neural NFSP 和 DQN 受害者均有效，可在智能体间迁移，被自对弈放大，且在长时间掩蔽训练后仍无法恢复。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 自对弈强化学习是一种智能体通过与自身对弈来提升性能的技术，常用于国际象棋和围棋等游戏。动作掩蔽是一种限制智能体可用动作的方法，常用于强制执行游戏规则。本文研究了一种利用动作掩蔽移除关键动作的新型对抗攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Self-play_(reinforcement_learning_technique)">Self-play (reinforcement learning technique)</a></li>
<li><a href="https://arxiv.org/pdf/2006.14171">A Closer Look at Invalid Action Masking in Policy Gradient Algorithms</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#adversarial attack`, `#self-play`, `#robustness`, `#AI safety`

---

<a id="item-21"></a>
## [决策容量阈值导致自博弈强化学习崩溃](https://arxiv.org/abs/2605.16315) ⭐️ 8.0/10

一项新研究揭示了决策容量中的一个尖锐阈值，该阈值决定了自博弈强化学习代理在非对称规则扰动下是否崩溃，边界为零可达加权条件行动容量。 这一发现对多智能体强化学习和 AI 安全具有重要意义，因为它识别了一种可能导致自博弈系统灾难性失败的基本机制，而自博弈系统广泛应用于游戏 AI 和自主训练中。 崩溃的特征是快速收敛到接近最大损失的确定性利用吸引子，并且在恢复行动后完全可逆。该现象在函数近似下加剧，且与时间无关。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 自博弈强化学习是指代理通过与自身副本对弈进行训练，常用于围棋和扑克等游戏。决策容量指代理在不同状态下可采取的行动集合；可达加权条件行动容量衡量在策略下可达的决策点数量。非对称规则扰动改变一个代理的规则，可能导致共同适应问题。

**标签**: `#reinforcement learning`, `#self-play`, `#multi-agent systems`, `#AI safety`, `#game theory`

---

<a id="item-22"></a>
## [AdaGraph：图原生聚类算法克服维度灾难](https://arxiv.org/abs/2605.16320) ⭐️ 8.0/10

研究人员提出了 AdaGraph，一种完全在 kNN 图拓扑内运行的图原生聚类算法，无需预先指定聚类数量，并能原生处理噪声，从而克服了维度灾难。 AdaGraph 能够在基因组学和材料科学等高维领域实现科学发现，而传统基于距离的聚类在这些领域效果不佳，这可能会改变高维数据分析的无监督学习方式。 AdaGraph 与基于拓扑的聚类有效性指标 Graph-SCOPE 配合使用，在 d=10 到 d=5000 的合成基准上实现了平均 ARI=0.900，优于 Silhouette、Davies-Bouldin 和 Calinski-Harabasz。在文本聚类（20NG-6cat）上，相比 HDBSCAN 相对提升了 62%。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 高维数据聚类具有挑战性，因为欧氏距离变得无效——这种现象称为维度灾难。传统聚类算法依赖距离度量，在高维中效果不佳。AdaGraph 使用 kNN 图拓扑，即使在任意高维中也能保留有意义的关联结构，从根本上消除了维度灾难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://inria.hal.science/hal-01407514/document">Nearest Neighbors Graph Construction: Peer Sampling to the Rescue</a></li>
<li><a href="https://jmlr.csail.mit.edu/papers/volume21/19-1032/19-1032.pdf">I.e., although the topology of the original graph might</a></li>

</ul>
</details>

**标签**: `#clustering`, `#high-dimensional data`, `#graph algorithms`, `#unsupervised learning`, `#curse of dimensionality`

---

<a id="item-23"></a>
## [语言游戏实现与非神经系统的对话](https://arxiv.org/abs/2605.16321) ⭐️ 8.0/10

一种新框架将与非神经生物系统的通信视为语言游戏，使用强化学习仅训练线性接口，同时保持内部动态冻结，使基因调控网络等系统能够通过自身行为“说话”。 该方法挑战了当前以 AI 为中心的方法（即大型语言模型代表生物系统说话），可能实现与多种非人类智能的直接、真实通信，为 AI、生物学和哲学开辟新途径。 该框架使用语言模型将人类提示路由到语义最匹配的游戏，设计一个环境状态，使期望动作成为理性响应，让系统通过行为回复，而不改变任何系统参数。

rss · arXiv - Machine Learning · May 19, 04:00

**背景**: 基因调控网络和微生物群落等非神经生物系统越来越被认为是计算和决策的基质。传统方法使用大型语言模型作为代理来解释这些系统，但论文认为这压制了系统自身的智能。受维特根斯坦哲学（意义在于使用）启发，作者将通信视为一种游戏，系统的状态通过交互和奖励获得意义。

**标签**: `#reinforcement learning`, `#biological computation`, `#language games`, `#non-human intelligence`, `#philosophy of mind`

---

<a id="item-24"></a>
## [LLM 智能体系统中技能的缩放定律](https://arxiv.org/abs/2605.16508) ⭐️ 8.0/10

一篇新论文识别出 LLM 智能体系统中技能库的两个耦合缩放定律：路由准确率随库大小对数衰减，而正确执行可将困难决策的改善幅度提升约 4 倍。 这些定律为设计可扩展的 AI 智能体系统提供了可操作的见解，表明性能不仅取决于模型能力，还取决于技能库的结构、粒度和暴露策略。 该研究涉及 15 个前沿 LLM、1141 个真实世界技能和超过 300 万个路由或执行决策。定律引导的优化将保留路由准确率从 71.3%提升至 91.7%，并将劫持率从 22.4%降低至 4.1%。

rss · arXiv - NLP · May 19, 04:00

**背景**: LLM 智能体系统通常使用技能库——可重用函数或工具的集合——来执行复杂任务。随着这些库的增长，理解缩放如何影响性能对于高效系统设计至关重要。

**标签**: `#LLM agents`, `#scaling laws`, `#skill libraries`, `#AI systems`, `#empirical study`

---

<a id="item-25"></a>
## [CHI-Bench：评估 AI 代理在复杂医疗工作流中的表现](https://arxiv.org/abs/2605.16679) ⭐️ 8.0/10

研究人员推出了 CHI-Bench，这是一个用于评估 AI 代理在端到端、长周期医疗工作流中表现的基准测试，这些工作流要求高政策密度、多角色组合和多边交互。该基准测试包含 30 种代理配置，最佳代理仅能完成 28.0%的任务，且没有代理在严格 pass^3 指标上超过 20%。 该基准测试揭示了当前 AI 代理在处理政策密集、多角色且不可逆的企业工作流方面的关键缺陷，这类工作流在医疗和其他受监管行业中很常见。研究结果表明，类似的能力差距可能也存在于其他领域，凸显了开发更强大代理架构的必要性。 CHI-Bench 通过一个高保真模拟器模拟三个医疗领域（预先授权、利用管理、护理管理），该模拟器包含 20 个应用程序，通过 87 个 MCP 工具暴露，并配备 1290 多份文档的操作手册。当在单次会话中执行所有任务时，性能降至 3.8%，表明在长周期任务执行中存在严重挑战。

rss · arXiv - NLP · May 19, 04:00

**背景**: AI 代理越来越多地被用于自动化复杂工作流，但现有的基准测试通常侧重于简单、单一角色的任务，且政策约束有限。医疗操作涉及复杂的规则、多个角色（如提供者、支付者、患者）和多轮交互，使其成为测试代理能力的挑战性场景。CHI-Bench 旨在通过提供一个逼真且全面的评估环境来填补这一空白。

**标签**: `#AI agents`, `#healthcare automation`, `#benchmark`, `#workflow automation`, `#multi-role`

---

<a id="item-26"></a>
## [受语言习得装置启发的预预训练提升 LLM 数据效率](https://arxiv.org/abs/2605.16758) ⭐️ 8.0/10

本文提出了一种受语言习得装置（LAD）启发的预预训练方法，使用名为 MP-STRUCT 的形式语言，该语言通过 MERGE、AGREE 和 MOVE 操作编码层次结构、基于特征的依赖和长距离位移。仅需 500 步的 MP-STRUCT 预预训练即可在 token 效率上媲美强形式语言基线，并赋予模型类似人类的对结构不合理语言（如 REVERSE）的抵抗力。 这项工作解决了 LLM 与人类之间的数据效率差距，可能减少训练所需的自然语言数据量。它还通过展示精心设计的形式语言预预训练可以有效灌输先天结构偏见，架起了认知科学与 NLP 之间的桥梁。 MP-STRUCT 语言无法在 C-RASP（一种对 transformer 表达力的形式化界限）中定义，这挑战了先前认为有效的预预训练语言必须同时具备层次表达力和电路可学习性的假设。研究指出，减少依赖解析歧义的功能性标志是 MP-STRUCT 有效性的关键驱动因素。

rss · arXiv - NLP · May 19, 04:00

**背景**: 大型语言模型（LLM）需要大量文本数据才能达到类似人类的理解水平，而人类仅通过有限接触就能习得语言，部分原因是假设存在语言习得装置（LAD）所代表的先天偏见。在主要训练之前，使用合成形式语言进行预预训练（PPT）已被探索用于向 LLM 注入有用的归纳偏见。先前的工作集中在高度表达性的形式语言上，如 k-Shuffle Dyck，这些语言既具有层次结构又可以被 transformer 学习。

**标签**: `#large language models`, `#language acquisition`, `#pre-pretraining`, `#formal languages`, `#NLP`

---

<a id="item-27"></a>
## [基于检索的法律标注方法超越生成式大模型](https://arxiv.org/abs/2605.16767) ⭐️ 8.0/10

研究人员提出一种基于检索的多标签法律标注方法，使用冻结的检索模型和 k 近邻算法，避免重新训练，在准确性和效率上优于 GPT-5.2 等生成式大模型。 该方法为法律标注提供了一种实用、数据高效且无幻觉的替代方案，尤其适用于高基数且快速变化的标签空间，可能将计算成本降低 20-30 倍。 在包含 100 个标签的 Eurlex 数据集上，使用 Qwen-8B 的检索方法将 Macro-F1 从 40.41（GPT-5.2 零样本）提升到 49.12，同时相比微调减少计算量 20-30 倍。仅用 100 个训练样本，在 ECtHR-A 上检索方法的 Micro-F1 几乎翻倍，达到 48.29，而层次化 Legal-BERT 仅为 27.87。

rss · arXiv - NLP · May 19, 04:00

**背景**: 多标签法律标注涉及从大型、不断演变的分类体系中为冗长的法律文档分配多个标签。传统的参数化编码器在标签变化时需要重新训练，而生成式大模型可能产生分类体系之外的幻觉标签，且随着标签空间增长成本增加。

**标签**: `#legal annotation`, `#retrieval`, `#multi-label classification`, `#data efficiency`, `#NLP`

---

<a id="item-28"></a>
## [Noise2Params：基于光子统计统一事件相机模型](https://arxiv.org/abs/2605.16317) ⭐️ 8.0/10

研究人员提出了 Noise2Params 方法，该方法基于光子统计的统一概率模型，通过静态场景的噪声记录来确定事件相机参数。 这项工作为事件相机标定和噪声感知算法设计提供了定量基础，有望提升光子受限场景下的性能，并减少对专用动态光源的需求。 该模型将静态噪声事件和阶跃响应曲线（S 曲线）统一到单一分析框架中，推导出覆盖所有强度区间的三种概率分布（精确泊松、鞍点、高斯）。

rss · arXiv - Computer Vision · May 19, 04:00

**背景**: 事件相机是仿生传感器，异步报告像素级亮度变化，但其噪声和响应特性通常被分开建模。这项工作通过将模型建立在光子统计基础上，揭示了噪声事件与 S 曲线之间的联系。

**标签**: `#event cameras`, `#probabilistic model`, `#computer vision`, `#sensor calibration`

---

<a id="item-29"></a>
## [GeoSym127K：可扩展的神经符号几何推理引擎](https://arxiv.org/abs/2605.16371) ⭐️ 8.0/10

研究人员推出了 GeoSym127K，这是一个大规模数据集，包含 127K 个带有符号真值的问题和 55K 个经过答案验证的思维链对，由名为 GeoSym Engine 的新型神经符号引擎生成。该引擎使用类型条件语法和分析型 SymGT 求解器生成高精度几何图形和精确的符号解。 这项工作解决了大型多模态模型在几何推理中的关键限制，如视觉幻觉和缺乏精确的思维链数据。GeoSym Engine 能够可扩展地生成高质量训练数据，从而在依赖图形和多步几何任务上取得显著性能提升，Qwen3-VL-8B 模型在 MathVerse Vision-Only 子集上实现了 +22.21% 的提升。 该数据集包含 51K 张高分辨率图像，并按难度分层。作者还引入了 GeoSym-Bench，这是一个由专家策划的包含 511 个复杂样本的基准测试，用于严格评估。通过 GRPO 应用可验证奖励的强化学习表明，从结构化 SFT 检查点初始化可以进一步提升性能。

rss · arXiv - Computer Vision · May 19, 04:00

**背景**: 大型多模态模型结合了视觉和语言能力，但由于视觉幻觉和缺乏精确的逐步推理数据，在几何推理中常常失败。神经符号 AI 将神经网络与符号推理相结合，以结合模式识别和逻辑精度。SymGT 求解器是一种分析型求解器，可为几何问题推导出精确的符号真值，类似于形式验证中使用的 SMT 求解器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SMT_solver">SMT solver</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#geometric reasoning`, `#neuro-symbolic`, `#dataset`, `#LMM`

---

<a id="item-30"></a>
## [StreamPro：流式视频中的主动决策](https://arxiv.org/abs/2605.16381) ⭐️ 8.0/10

研究人员推出了 StreamPro-Bench，一个用于主动流式视频理解的基准，以及 StreamPro，一个两阶段训练框架，在该基准上达到 41.5，远超此前最佳成绩 10.4。 这项工作将视频理解从被动的“先看后答”转变为主动决策，使 AI 系统能在部分观察下做出及时可靠的决策，这对自动驾驶和监控等实时应用至关重要。 该基准从感知理解、时间推理和主动代理三个维度评估模型；框架使用 CB-Stream Loss 进行监督微调，并通过具有多粒度奖励的 GRPO 优化正确性和时机。

rss · arXiv - Computer Vision · May 19, 04:00

**背景**: 传统视频基准遵循“先看后答”范式，仅在明确证据出现后才触发响应，无法评估主动推理。主动理解要求模型在不完整观察下决定何时响应，平衡早期预测与充分证据。

**标签**: `#video understanding`, `#proactive decision-making`, `#benchmark`, `#streaming video`, `#AI`

---

<a id="item-31"></a>
## [TaTok：使用全局令牌的自适应图像令牌化](https://arxiv.org/abs/2605.16384) ⭐️ 8.0/10

TaTok 提出了一个理论基础的适应性图像令牌化框架，通过全局令牌和动态令牌过滤减少冗余并提升重建质量，实现了 1.3 倍的 gFID 改进和 8.7 倍的推理加速。 这项工作解决了离散图像令牌化中的一个基本限制——固定速率压缩忽略了可变信息密度——可以显著提高图像处理和生成模型的效率和质量。 TaTok 引入了全局令牌来建模补丁令牌之间的互信息，并基于累积条件熵提出了动态令牌过滤（DTF）算法以消除冗余，实现了最先进的性能。

rss · arXiv - Computer Vision · May 19, 04:00

**背景**: 离散图像令牌化将图像转换为离散令牌序列，供 Transformer 等模型处理。当前方法以固定速率压缩所有内容，导致低信息区域冗余和高细节区域信息丢失。TaTok 受信息熵理论启发，根据信息丰富度自适应分配令牌。

**标签**: `#image tokenization`, `#information entropy`, `#computer vision`, `#deep learning`, `#generative models`

---

<a id="item-32"></a>
## [StAD：利用 Stein 算子实现扩散模型快速似然估计](https://arxiv.org/abs/2605.16486) ⭐️ 8.0/10

StAD 提出了一种蒸馏方法，利用 Langevin-Stein 算子预测概率流 ODE 的散度，无需计算 Jacobian 矩阵，从而为扩散和流模型实现更快、更准确的似然估计。 这解决了生成模型似然估计中的关键计算瓶颈，对贝叶斯分析等工作流程至关重要，并且该方法在方差和速度上优于现有的随机估计器（如 Hutchinson）。 StAD 在 CIFAR-10、ImageNet 及其他密度估计任务上得到验证，在方差和速度上持续优于 Hutchinson 和 Hutch++估计器。该方法还能推广到多种生成模型，并在正则条件下满足 Stein 类。

rss · arXiv - Data Science & Statistics · May 19, 04:00

**背景**: 扩散和流模型使用概率流 ODE（PF-ODE）传输概率质量，似然估计需要计算 PF-ODE 的 Jacobian 矩阵的迹。精确计算复杂度为 O(D^2)，而 Hutchinson 等随机估计器提供 O(D)复杂度但带有噪声。StAD 利用 Langevin-Stein 算子直接学习散度，避免了 Jacobian 计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Hutchinson_Trace_Estimator">Hutchinson Trace Estimator</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#likelihood estimation`, `#normalizing flows`, `#density estimation`, `#machine learning`

---

<a id="item-33"></a>
## [预测干预博弈与不变集](https://arxiv.org/abs/2605.16828) ⭐️ 8.0/10

本文提出了预测干预博弈，这是一种 Stackelberg 博弈框架，其中领导者选择预测函数，跟随者干预协变量。论文证明，在两种常见的跟随者目标下，基于稳定毯（一种不变子集）的预测器总是至少与基于因果父节点的预测器一样好。 这项工作将因果推断与博弈论联系起来，为设计对抗战略干预的鲁棒预测器提供了原则性方法。它对部署在对抗性或交互式环境中的机器学习系统（如推荐系统或自动决策）具有重要意义。 稳定毯是一种特定的不变子集，它推广了因果父节点。论文提供了最坏情况风险界以及稳定毯预测器最优的充分条件，并在模拟和真实数据上测试了策略。

rss · arXiv - Data Science & Statistics · May 19, 04:00

**背景**: 在因果推断中，目标变量的因果父节点是其直接原因。不变预测旨在寻找在分布变化下仍保持预测能力的协变量子集。Stackelberg 博弈模拟了领导者先承诺的领导者-跟随者动态。本文结合这些思想来处理战略性干预。

**标签**: `#causal inference`, `#game theory`, `#invariant prediction`, `#machine learning`, `#structural causal models`

---

<a id="item-34"></a>
## [傅里叶分析揭示神经网络的简单性偏好](https://arxiv.org/abs/2605.16913) ⭐️ 8.0/10

本文利用傅里叶分析研究神经网络的学习动态，表明网络先学习幅度信息再学习相位信息，并引入了一个用于平移不变输入的合成数据模型。 作者严格证明，对于各向同性输入，SGD 在 n << N^3 步内无法区分结构化相位信息和噪声，但幂律谱可以显著加速相位信息的学习。

rss · arXiv - Data Science & Statistics · May 19, 04:00

**背景**: 使用梯度下降训练的神经网络通常表现出简单性偏好，即先学习简单特征再学习复杂特征。以往的分析集中于各向同性输入，但自然图像具有平移不变性和幂律谱。傅里叶分析将信号分解为幅度（与成对相关性相关）和相位（编码边缘和高阶相关性）。

**标签**: `#neural networks`, `#learning dynamics`, `#simplicity bias`, `#Fourier analysis`, `#image classification`

---

<a id="item-35"></a>
## [用于随机偏微分方程不确定性量化的随机算子网络](https://arxiv.org/abs/2605.17107) ⭐️ 8.0/10

研究人员提出了随机算子网络（SON），该框架将 DeepONet 与随机神经网络相结合，直接从含噪声数据中学习随机偏微分方程的解算子，输出均值解和不确定性。 这解决了科学机器学习中的一个关键空白，无需事先了解模型不确定性即可对随机偏微分方程进行不确定性量化，这对于复杂物理系统的可靠预测至关重要。 训练过程通过最小化哈密顿型损失函数，并利用随机最大值原理进行优化。在具有多种不确定性源的基准随机偏微分方程上的数值实验证明了其准确性和鲁棒性。

rss · arXiv - Data Science & Statistics · May 19, 04:00

**背景**: 随机偏微分方程（SPDE）用于建模不确定性下的物理系统，但需要指定未知的模型不确定性。深度算子网络（DeepONet）学习确定性解算子，而随机神经网络（SNN）建模概率输出。该工作将两者结合以处理含噪声数据。

**标签**: `#operator learning`, `#uncertainty quantification`, `#stochastic PDEs`, `#deep learning`, `#scientific machine learning`

---

<a id="item-36"></a>
## [含噪归纳矩阵补全实现样本效率](https://arxiv.org/abs/2605.17189) ⭐️ 8.0/10

一种结合谱初始化的非凸投影梯度下降算法，在含噪归纳矩阵补全中实现了样本复杂度随侧信息维度而非环境维度缩放。 这弥合了无噪与含噪场景之间的差距，使得在实际含噪环境中实现样本高效的矩阵补全成为可能，对推荐系统和信号处理有潜在影响。 该方法即使在侧信息不精确时仍保持较低的样本复杂度，且估计误差关于不精确度是阶最优的。在 MovieLens 数据集上的实验验证了理论。

rss · arXiv - Data Science & Statistics · May 19, 04:00

**背景**: 矩阵补全旨在从部分观测中恢复低秩矩阵。归纳矩阵补全（IMC）利用侧信息（如用户/物品特征）缩小搜索空间。先前的工作要么仅在无噪场景下实现样本效率，要么处理噪声但样本复杂度随环境维度缩放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bigdata.oden.utexas.edu/software/inductive-matrix-completion/">Inductive Matrix Completion | Center for Big Data Analytics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sample_complexity">Sample complexity</a></li>

</ul>
</details>

**标签**: `#matrix completion`, `#sample complexity`, `#nonconvex optimization`, `#side information`, `#low-rank`

---

<a id="item-37"></a>
## [安杜里尔与 Meta 合作开发军用 AR 眼镜](https://www.technologyreview.com/2026/05/18/1137412/inside-anduril-and-metas-quest-to-make-smart-glasses-for-warfare/) ⭐️ 8.0/10

安杜里尔公司透露了与 Meta 合作开发的增强现实头盔原型的新细节，该头盔可使士兵通过眼动追踪和语音命令指挥无人机打击。 这家主要国防承包商与领先科技公司的合作标志着将消费级 AR 技术整合到军事行动中的重要一步，可能改变战争的方式。 该头盔正在为美国军方进行原型开发，前陆军特种作战军官 Quay Barnett 在安杜里尔领导该项目。

rss · MIT Technology Review · May 18, 16:01

**背景**: 增强现实（AR）将数字信息叠加到现实世界上。安杜里尔是一家以 AI 驱动的监控系统闻名的国防科技公司，而 Meta 是一家大力投资 AR/VR 的消费科技巨头。他们的合作旨在将 Meta 的智能眼镜改造用于战场。

**标签**: `#augmented reality`, `#defense technology`, `#AI`, `#military`, `#Meta`

---