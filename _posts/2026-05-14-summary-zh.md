---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 87 items, 33 important content pieces were selected

---

1. [3D 高斯泼溅：实时辐射场渲染](#item-1) ⭐️ 9.0/10
2. [MacBook Neo 深度剖析：基准测试、晶圆经济学与 8GB 内存赌注](#item-2) ⭐️ 8.0/10
3. [Supertonic：基于 ONNX 的快速设备端多语言 TTS](#item-3) ⭐️ 8.0/10
4. [CloakBrowser：绕过机器人检测的隐形 Chromium 浏览器](#item-4) ⭐️ 8.0/10
5. [Hysteria：快速抗审查代理工具](#item-5) ⭐️ 8.0/10
6. [EleutherAI 更新 LM Evaluation Harness，重构 CLI](#item-6) ⭐️ 8.0/10
7. [MinerU：开源 PDF 转 Markdown/JSON 工具](#item-7) ⭐️ 8.0/10
8. [BenchJack：AI 智能体基准的自动化审计](#item-8) ⭐️ 8.0/10
9. [REVELIO 揭示 VLM 的可解释故障模式](#item-9) ⭐️ 8.0/10
10. [一阶进展的规模与可判定性分析](#item-10) ⭐️ 8.0/10
11. [DisaBench：参与式评估语言模型中的残疾伤害](#item-11) ⭐️ 8.0/10
12. [CHAL：多智能体辩论作为信念优化](#item-12) ⭐️ 8.0/10
13. [BEHAVE：实时集体人类动力学的混合 AI 框架](#item-13) ⭐️ 8.0/10
14. [状态中心决策过程连接语言环境与 MDP](#item-14) ⭐️ 8.0/10
15. [AI 与人类信心对齐降低学习复杂度](#item-15) ⭐️ 8.0/10
16. [KAN 在 DP-SGD 和相关噪声下的首个总体风险界](#item-16) ⭐️ 8.0/10
17. [嵌入时序逻辑：自主系统运行时监控新方法](#item-17) ⭐️ 8.0/10
18. [scShapeBench：自动检测单细胞 RNA 测序数据中的几何结构](#item-18) ⭐️ 8.0/10
19. [LLM 多样性崩溃与校准问题相关](#item-19) ⭐️ 8.0/10
20. [ClinicalBench：对临床问答中的断言感知检索进行压力测试](#item-20) ⭐️ 8.0/10
21. [分解进化混合 LoRA：路由器重写是关键](#item-21) ⭐️ 8.0/10
22. [双室模型：通过隐藏状态耦合冻结语言模型](#item-22) ⭐️ 8.0/10
23. [差分隐私在某些任务中减少 LLM 偏见，但并非全部](#item-23) ⭐️ 8.0/10
24. [指令塑造输出生成，而非输入处理](#item-24) ⭐️ 8.0/10
25. [ReVision 将计算机使用代理的视觉令牌减少 46%](#item-25) ⭐️ 8.0/10
26. [VideoSEAL：长视频问答的解耦框架](#item-26) ⭐️ 8.0/10
27. [自注意力中逆温度缩放的统一理论](#item-27) ⭐️ 8.0/10
28. [鲁棒序贯 A/B 测试框架](#item-28) ⭐️ 8.0/10
29. [理论证明弱到强泛化可激发潜在特征](#item-29) ⭐️ 8.0/10
30. [黑盒生成-验证 AI 工作流的始终有效发布方法](#item-30) ⭐️ 8.0/10
31. [CCVFM：基于核心集增强的流匹配生成模型](#item-31) ⭐️ 8.0/10
32. [基于小波的 DPP 核改进小批量方差缩减](#item-32) ⭐️ 8.0/10
33. [AI 聊天机器人泄露真实电话号码，引发骚扰](#item-33) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [3D 高斯泼溅：实时辐射场渲染](https://github.com/graphdeco-inria/gaussian-splatting) ⭐️ 9.0/10

Inria 研究团队发布了 3D 高斯泼溅的官方实现，这是一种新方法，能够在无界场景中实现 1080p 分辨率下最先进的视觉质量和实时（≥30 fps）新视角合成。 这项工作标志着辐射场渲染的范式转变，克服了 NeRF 等先前方法的速度-质量权衡，为 VR、游戏和 3D 重建中的实际实时应用提供了可能。 该方法使用从稀疏 SfM 点初始化的 3D 高斯表示场景，优化各向异性协方差，并采用支持各向异性泼溅的快速可见性感知渲染算法。仓库包含预训练模型、评估图像和 Windows 查看器。

rss · GitHub Trending - Python · May 14, 14:21

**背景**: 像 NeRF 这样的辐射场方法可以从多张图像合成新视角，但训练和渲染速度慢。3D 高斯泼溅用显式 3D 高斯代替神经网络，实现了高效优化和实时渲染，且不牺牲质量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/3D_Gaussian_splatting">3D Gaussian splatting</a></li>
<li><a href="https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/">3D Gaussian Splatting for Real-Time Radiance Field Rendering</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_radiance_field">Neural radiance field - Wikipedia</a></li>

</ul>
</details>

**标签**: `#3D Gaussian Splatting`, `#Radiance Fields`, `#Computer Graphics`, `#NeRF`, `#Real-Time Rendering`

---

<a id="item-2"></a>
## [MacBook Neo 深度剖析：基准测试、晶圆经济学与 8GB 内存赌注](https://www.jdhodges.com/blog/macbook-neo-benchmarks-analysis/) ⭐️ 8.0/10

对 MacBook Neo 的详细分析显示，其 8GB 内存配置在 macOS 系统开销后仅剩 1.5-2GB 可用应用内存，引发了对计划性报废的担忧。文章还通过晶圆经济学和基准测试评估了该产品的价值。 该分析揭示了苹果公司一项有争议的决定，可能影响用户体验和产品寿命，甚至触发计划性报废法规。这对考虑购买 MacBook Neo 的消费者以及关于现代笔记本电脑内存配置的广泛讨论具有重要意义。 MacBook Neo 的 I/O 接口有限，只有一个 USB 2.0 端口且不支持 Thunderbolt，充电占用唯一的 USB 3 端口。8GB 内存型号被视为一场赌注，因为未来的 macOS 更新可能增加内存占用，进一步减少可用内存。

hackernews · tosh · May 13, 18:30 · [社区讨论](https://news.ycombinator.com/item?id=48125617)

**背景**: 晶圆经济学涉及半导体制造的成本分析，其中良率和晶圆尺寸影响每颗芯片的成本。计划性报废是一种策略，产品被设计为有限寿命以促进重复购买。MacBook Neo 的 8GB 内存配置之所以有争议，是因为随着软件需求增长，它可能变得不足。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Wafer_(electronics)">Wafer (electronics) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Planned_obsolescence">Planned obsolescence</a></li>
<li><a href="https://anysilicon.com/wafer-cost/">Understanding Wafer Cost - AnySilicon</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：一些人批评 8GB 型号内存不足且存在计划性报废风险，而另一些人则分享了 8GB M1 Mac 的长期良好使用体验。还有关于 I/O 限制和文章写作风格的讨论，一位评论者怀疑文章由 AI 撰写。

**标签**: `#Apple`, `#hardware`, `#memory`, `#benchmarks`, `#planned obsolescence`

---

<a id="item-3"></a>
## [Supertonic：基于 ONNX 的快速设备端多语言 TTS](https://github.com/supertone-inc/supertonic) ⭐️ 8.0/10

Supertone Inc. 发布了 Supertonic，这是一个极快的设备端多语言文本转语音系统，通过 ONNX Runtime 原生运行，提供 v1、v2 和 v3 版本。最新的 v3 版本支持 31 种语言，并提高了阅读准确性，减少了重复/跳过失败。 Supertonic 实现了完全在设备端的高质量 TTS，无需依赖云端，解决了隐私和延迟问题。其开源发布和多语言支持对构建跨语言语音应用的开发者极具价值。 Supertonic 使用 ONNX Runtime 进行跨平台推理，并提供可通过 pip 安装的 Python SDK。v3 版本支持 31 种语言，并包含与 v2 兼容的公共 ONNX 资产，同时 Voice Builder 工具允许用户创建自定义语音。

rss · GitHub Trending - Daily (All) · May 14, 14:21

**背景**: 文本转语音（TTS）系统将书面文本转换为语音音频。传统的基于云的 TTS 需要互联网连接并引发隐私问题。ONNX Runtime 是一个跨平台的机器学习模型加速器，可实现高效的本地推理。Supertonic 利用 ONNX 直接在用户设备上运行 TTS 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://onnxruntime.ai/">ONNX Runtime | Home</a></li>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform, high performance ML inferencing and training accelerator · GitHub</a></li>
<li><a href="https://koshurai.medium.com/supertonic-tts-the-ai-that-turns-text-into-human-like-speech-in-seconds-9e9450dd9579">Supertonic TTS : The AI That Turns Text Into Human-Like... | Medium</a></li>

</ul>
</details>

**标签**: `#TTS`, `#ONNX`, `#multilingual`, `#open-source`, `#machine learning`

---

<a id="item-4"></a>
## [CloakBrowser：绕过机器人检测的隐形 Chromium 浏览器](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser 是一款隐形 Chromium 浏览器，通过应用 49 个源码级 C++ 补丁修改浏览器指纹，通过了 30/30 的机器人检测测试。它可以作为 Playwright 和 Puppeteer 的直接替代品，只需更改导入语句即可。 该项目解决了网络自动化和反机器人规避中的关键需求，为面临 Cloudflare Turnstile 和 reCAPTCHA 等日益严格机器人检测的开发者提供了实用解决方案。其开源特性和易用性可能使隐形浏览技术更加普及。 该浏览器实现了 0.9 的 reCAPTCHA v3 分数，并通过了 Cloudflare Turnstile、FingerprintJS 和 BrowserScan 测试。它包含 humanize=True 标志以模拟人类行为，并在后台自动更新二进制文件。

rss · GitHub Trending - Daily (All) · May 14, 14:21

**背景**: 浏览器指纹是一种网站根据浏览器和设备独特配置识别用户的技术，常用于机器人检测。Playwright 是一个流行的开源自动化库，用于浏览器测试和网页抓取，但其自动化信号可能被反机器人系统检测到。CloakBrowser 在 C++ 源码级别修改 Chromium，移除这些可检测信号，使其看起来像普通浏览器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques : 6 Top Methods Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Playwright_(software)">Playwright (software) - Wikipedia</a></li>
<li><a href="https://www.browserscan.net/bot-detection">BrowserScan - Robot Detection /WebDriver | BrowserScan</a></li>

</ul>
</details>

**标签**: `#web automation`, `#anti-bot`, `#browser fingerprinting`, `#Playwright`, `#stealth browser`

---

<a id="item-5"></a>
## [Hysteria：快速抗审查代理工具](https://github.com/apernet/hysteria) ⭐️ 8.0/10

Hysteria 是一款开源代理工具，采用定制的 QUIC 协议实现高速和抗审查能力，并将流量伪装成标准 HTTP/3 流量。 Hysteria 提供了一种新颖的网络审查绕过方法，性能损失极小，对受限环境中的用户很有价值，并为更广泛的抗审查生态系统做出了贡献。 Hysteria 支持多种模式，包括 SOCKS5、HTTP 代理、TCP/UDP 转发、Linux TProxy 和 TUN，并且跨平台，支持所有主流平台和架构。

rss · GitHub Trending - Daily (All) · May 14, 14:21

**背景**: 传统的代理协议如 WireGuard 和 OpenVPN 容易被深度包检测（DPI）检测并封锁。Hysteria 基于 QUIC 协议构建，该协议也被 HTTP/3 使用，并被 Google、Cloudflare 等主要服务广泛部署，因此在不造成附带损害的情况下更难被封锁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hysteria.network/">Home - Hysteria 2</a></li>
<li><a href="https://www.samnet.dev/learn/guides/hysteria2-setup/">Hysteria2 Setup Guide: The Fastest Censorship ... | SamNet Learn</a></li>
<li><a href="https://hy2.app/docs/developers/Protocol/">Protocol - Hysteria 2</a></li>

</ul>
</details>

**标签**: `#proxy`, `#censorship`, `#networking`, `#open-source`

---

<a id="item-6"></a>
## [EleutherAI 更新 LM Evaluation Harness，重构 CLI](https://github.com/EleutherAI/lm-evaluation-harness) ⭐️ 8.0/10

EleutherAI 发布了 lm-evaluation-harness 的重大更新，包括重构的 CLI（支持 run、ls、validate 子命令和 YAML 配置文件），以及更轻量的基础安装，将模型后端分离。 此次更新显著提升了评估大语言模型的可用性和模块化程度，使研究人员和开发者更容易集成和定制评估，这对于 NLP 社区中可重复和透明的基准测试至关重要。 基础包不再包含 transformers 或 torch；用户必须通过 lm_eval[hf] 或 lm_eval[vllm] 等额外选项单独安装模型后端。此次更新还增加了对 SGLang、HF 模型引导以及多模态输入任务（原型）的支持。

rss · GitHub Trending - Python · May 14, 14:21

**背景**: LM Evaluation Harness 是 EleutherAI 开发的开源框架，用于对自回归语言模型进行标准化的少样本评估。它通过提供跨模型和任务的统一接口，解决了 LLM 评估中的可重复性和可比性问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/EleutherAI/lm-evaluation-harness">GitHub - EleutherAI/lm- evaluation -harness: A framework for few - shot ...</a></li>
<li><a href="https://www.eleuther.ai/projects/large-language-model-evaluation">Evaluating LLMs — EleutherAI</a></li>
<li><a href="https://medium.com/disassembly/llm-evaluation-eleutherai-lm-evaluation-harness-cc379495d545">LLM evaluation | EleutherAI lm - evaluation - harness | Medium</a></li>

</ul>
</details>

**标签**: `#NLP`, `#language models`, `#evaluation`, `#open source`

---

<a id="item-7"></a>
## [MinerU：开源 PDF 转 Markdown/JSON 工具](https://github.com/opendatalab/MinerU) ⭐️ 8.0/10

OpenDataLab 推出的开源文档解析工具 MinerU，可将 PDF、图片及 Office 文档（DOCX、PPTX、XLSX）转换为面向 LLM 智能体工作流优化的 Markdown 和 JSON 格式。 该工具通过将复杂的非结构化文档转换为机器可读格式，解决了 AI 流程中的关键瓶颈，为大型语言模型的训练和推理提供更高效的数据准备。 MinerU 支持 PDF、图片、DOCX、PPTX 和 XLSX 等多种输入类型，输出结构化的 Markdown 或 JSON。该工具在 InternLM 预训练期间开发，并在 GitHub 和 PyPI 上可用。

rss · GitHub Trending - Python · May 14, 14:21

**背景**: 大型语言模型（LLM）通常需要干净、结构化的文本用于训练或检索增强生成（RAG）。然而，许多现实文档是 PDF 或 Office 格式，包含复杂布局、表格和图像，提取困难。MinerU 自动化了这一提取过程，生成 LLM 可直接使用的格式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opendatalab.github.io/MinerU/">MinerU - MinerU</a></li>
<li><a href="https://github.com/opendatalab/MinerU">GitHub - opendatalab/ MinerU : Transforms complex documents like...</a></li>
<li><a href="https://levelup.gitconnected.com/from-pdf-chaos-to-data-gold-how-mineru-is-revolutionizing-document-intelligence-50180c76e74f">Zero-Effort PDF to Markdown: How MinerU Handles... | Level Up Coding</a></li>

</ul>
</details>

**标签**: `#document-processing`, `#LLM`, `#data-preparation`, `#open-source`, `#Python`

---

<a id="item-8"></a>
## [BenchJack：AI 智能体基准的自动化审计](https://arxiv.org/abs/2605.12673) ⭐️ 8.0/10

研究人员推出了 BenchJack，这是一个自动化红队系统，用于审计 AI 智能体基准中的奖励黑客漏洞，并在 10 个流行基准上进行了演示，发现了 219 个不同的缺陷，并将四个基准上的可攻击任务比例从接近 100%降低到 10%以下。 这项工作揭示了 AI 智能体评估流程中的关键安全漏洞，并提供了一种系统性的方法来提高基准的鲁棒性，这对于可靠的模型选择和 AI 智能体的安全部署至关重要。 BenchJack 使用生成对抗式流程，迭代发现并修补缺陷，在三轮迭代内完全修复了 WebArena 和 OSWorld。该分类法包含八个常见缺陷模式，并整理成 Agent-Eval 检查表供基准设计者使用。

rss · arXiv - AI · May 14, 04:00

**背景**: 奖励黑客是指 AI 智能体利用基准中的漏洞，在不执行预期任务的情况下获得高分。这是 AI 安全中的一个关键挑战，因为设计不良的基准可能会对智能体的真实能力发出误导信号。红队测试是一种技术，专家尝试利用 AI 系统中的漏洞来识别弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.12673">Do Androids Dream of Breaking the Game? Systematically Auditing AI...</a></li>
<li><a href="https://github.com/benchjack/benchjack">GitHub - benchjack / benchjack : AI agent benchmark hackability...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reward_hacking">Reward hacking</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#benchmarking`, `#reward hacking`, `#red-teaming`, `#agent evaluation`

---

<a id="item-9"></a>
## [REVELIO 揭示 VLM 的可解释故障模式](https://arxiv.org/abs/2605.12674) ⭐️ 8.0/10

研究人员提出了 REVELIO 框架，该框架通过使用多样性感知波束搜索和高斯过程汤普森采样在组合概念空间中进行搜索，系统地发现视觉语言模型中的可解释故障模式。 这项工作解决了 VLM 中的一个关键安全问题，VLM 越来越多地用于自动驾驶和机器人等安全关键应用，通过提供一种方法来发现结构化的漏洞，从而指导有针对性的安全改进。 REVELIO 结合了多样性感知波束搜索以高效映射故障景观，以及高斯过程汤普森采样以更广泛地探索复杂故障模式。它被应用于自动驾驶和室内机器人领域，揭示了之前未报告的漏洞，如空间定位能力弱和过度保守。

rss · arXiv - AI · May 14, 04:00

**背景**: 视觉语言模型（VLM）结合了视觉和文本理解能力，用于执行图像描述和视觉问答等任务。尽管功能强大，VLM 在特定情况下可能会灾难性地失败，这被称为故障模式。识别这些故障模式具有挑战性，因为它们涉及可解释概念的组合，导致搜索空间呈指数级增长。REVELIO 通过使用先进的搜索策略来高效地发现这些故障。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1610.02424">[1610.02424] Diverse Beam Search: Decoding Diverse Solutions from Neural Sequence Models</a></li>
<li><a href="https://arxiv.org/abs/2410.08071">[2410.08071] Gaussian Process Thompson Sampling via Rootfinding</a></li>

</ul>
</details>

**标签**: `#Vision-Language Models`, `#AI Safety`, `#Failure Mode Analysis`, `#Interpretability`, `#Combinatorial Search`

---

<a id="item-10"></a>
## [一阶进展的规模与可判定性分析](https://arxiv.org/abs/2605.12691) ⭐️ 8.0/10

本文证明，对于局部效应、正规和循环动作，一阶进展的规模呈多项式增长，并且保持在可判定片段（如二变量一阶逻辑）内。 这一结果确保了进展（AI 中的关键推理任务）对于重要的动作类别在计算上可行，从而支持规划和验证等实际应用。 该分析使用情境演算框架，表明在合理假设下进展规模是多项式的；当知识库属于可判定片段时，它还能保持可判定性。

rss · arXiv - AI · May 14, 04:00

**背景**: 进展是在动作发生后更新知识库以反映新状态的任务。它通常需要二阶逻辑，但受限的动作类别（局部效应、正规、循环）允许一阶进展。本文首次对这些类别进行了系统的规模分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.12691">On the Size Complexity and Decidability of First - Order ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Situation_calculus">Situation calculus</a></li>
<li><a href="https://www.ijcai.org/proceedings/2024/385">First-Order Progression beyond Local-Effect and Normal Actions | IJCAI</a></li>

</ul>
</details>

**标签**: `#reasoning about actions`, `#situation calculus`, `#first-order logic`, `#decidability`, `#knowledge representation`

---

<a id="item-11"></a>
## [DisaBench：参与式评估语言模型中的残疾伤害](https://arxiv.org/abs/2605.12702) ⭐️ 8.0/10

研究人员推出了 DisaBench，这是一个与残疾人和红队专家共同创建的参与式评估框架，包含 12 个残疾伤害类别的分类法、175 个提示及 525 个标注的提示-响应对的数据集，以及评估大型语言模型中残疾相关伤害的方法。 该框架揭示了标准安全基准无法捕捉只有领域专家才能识别的细微残疾伤害，从而填补了 AI 安全中的关键空白，有望推动更具包容性和公平性的 AI 系统。 研究发现伤害率因残疾类型而异，并在非文本模态中叠加，且术语驱动的伤害具有文化和时间依赖性。数据集和方法将通过 Hugging Face 和开源红队框架发布。

rss · arXiv - AI · May 14, 04:00

**背景**: 大型语言模型的通用安全基准通常无法充分评估与残疾相关的伤害。参与式评估让残疾人等利益相关者参与评估过程，以捕捉自动化或仅专家评估可能遗漏的细微伤害。先前的研究已发现 LLM 中对残疾群体的偏见，但缺乏系统的评估框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/fullHtml/10.1145/3593013.3593989">"I wouldn't say offensive but...": Disability-Centered Perspectives on Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2510.10998">[2510.10998] ABLEIST: Intersectional Disability Bias in LLM-Generated Hiring Scenarios</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#disability`, `#LLM evaluation`, `#fairness`, `#participatory design`

---

<a id="item-12"></a>
## [CHAL：多智能体辩论作为信念优化](https://arxiv.org/abs/2605.12718) ⭐️ 8.0/10

研究人员提出了 CHAL（分层代理语言委员会），这是一个多智能体辩证框架，将可废止论证视为信念优化，采用受贝叶斯启发的信念模式和梯度信息动态。 CHAL 通过关注可废止领域而非事实性任务，解决了当前多智能体辩论方法的局限性，可能改善 LLM 在论点可被更好推理推翻的领域的推理能力。 每个智能体维护一个 CHAL 信念模式（CBS），这是一种具有贝叶斯启发架构的图结构信念表示，元认知价值系统作为可配置超参数，控制推理和裁决。

rss · arXiv - AI · May 14, 04:00

**背景**: 多智能体辩论已被用于改进 LLM 推理，但当前方法存在鞅信念轨迹和置信度升级等问题。可废止论证允许结论在新证据面前被撤回，因此适用于真理非绝对的领域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Argument">Argument - Wikipedia</a></li>
<li><a href="https://plato.stanford.edu/entries/reasoning-defeasible/">Defeasible Reasoning (Stanford Encyclopedia of Philosophy)</a></li>

</ul>
</details>

**标签**: `#multi-agent debate`, `#LLM reasoning`, `#defeasible reasoning`, `#belief revision`, `#Bayesian inference`

---

<a id="item-13"></a>
## [BEHAVE：实时集体人类动力学的混合 AI 框架](https://arxiv.org/abs/2605.12730) ⭐️ 8.0/10

研究人员提出了 BEHAVE，这是一个混合 AI 框架，利用复杂动力系统理论将集体人类动力学建模为连续行为场，能够实时预测群体行为。 该框架填补了现有 AI 系统仅建模个体或事后检测事件的空白，有望变革人群管理、危机应对和社会科学研究等领域。 BEHAVE 通过张力场、场基和临界性指数定义集体状态，并使用神经模型进行感知和预测；已在 7 个智能体的谈判快照上进行了演示。

rss · arXiv - AI · May 14, 04:00

**背景**: 复杂动力系统理论研究具有许多相互作用组件的系统，这些系统表现出非线性、涌现性和相变。集体人类行为（如人群动力学）可被视为这样的系统，但传统 AI 方法难以捕捉实时的涌现动力学。BEHAVE 提供了将这些动力学建模为连续场的数学基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Complex_dynamic_systems_theory">Complex dynamic systems theory</a></li>
<li><a href="https://en.wikipedia.org/wiki/Human_dynamics">Human dynamics - Wikipedia</a></li>
<li><a href="https://www.nature.com/articles/s41598-019-54296-7">Phase transitions, collective emotions and decision-making problem in heterogeneous social systems | Scientific Reports</a></li>

</ul>
</details>

**标签**: `#AI`, `#collective dynamics`, `#complex systems`, `#human behavior modeling`, `#real-time`

---

<a id="item-14"></a>
## [状态中心决策过程连接语言环境与 MDP](https://arxiv.org/abs/2605.12755) ⭐️ 8.0/10

研究人员提出了状态中心决策过程（SDP），这是一个运行时框架，使智能体能够从语言环境中的原始文本构建状态空间、观测到状态的映射、认证转移和终止条件。 SDP 弥合了非结构化语言环境与形式化 MDP 分析之间的鸿沟，使强化学习和交互系统能够在网页浏览、科学探索等领域受益于结构化决策。 SDP 在涵盖规划、科学探索、网页推理和多跳问答的五个基准上取得了最佳的无训练结果，且随着任务长度的增加优势更加明显。

rss · arXiv - AI · May 14, 04:00

**背景**: 马尔可夫决策过程（MDP）是强化学习中用于序列决策的形式化框架，需要明确的状态空间、转移和奖励。然而，像网页浏览器或代码终端这样的语言环境输出原始文本，缺乏此类结构，导致 MDP 分析无法直接应用。SDP 通过让智能体使用自然语言谓词逐步构建必要组件来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12755">[2605.12755] State - Centric Decision Process</a></li>
<li><a href="https://en.wikipedia.org/wiki/Markov_decision_process">Markov decision process - Wikipedia</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#MDP`, `#language environments`, `#decision process`, `#AI`

---

<a id="item-15"></a>
## [AI 与人类信心对齐降低学习复杂度](https://arxiv.org/abs/2605.12646) ⭐️ 8.0/10

一篇新论文将 AI 辅助的二元决策形式化为在线学习问题，并证明 AI 与人类信心之间的对齐越好，遗憾界越低，在完美对齐下可从Ω(√(|H||B|T))降至 O(√(T log T))。 这一理论结果量化了人机团队中信心对齐的益处，指导 AI 系统设计使其适应人类信心，从而在医疗、金融等高风险领域提高决策效率。 论文建立了期望遗憾的下界Ω(√(|H|·|B|·T))，其中 H 和 B 分别是人类和 AI 信心值的集合，并证明在完美对齐下，当√|H| = O(log T)且 B 可数时，遗憾界可改进至 O(√(T log T))。在真实人类受试者数据上的实验验证了鲁棒性。

rss · arXiv - Machine Learning · May 14, 04:00

**背景**: AI 辅助决策通常涉及 AI 模型以置信度分数预测结果，人类决策者结合自身判断使用该分数。先前研究表明，这种辅助的效用取决于 AI 信心与人类自我信心的对齐程度。本文通过分析对齐如何影响重复交互中学习最优决策的复杂度，扩展了该研究方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41598-025-12205-1">Human-alignment influences the utility of AI-assisted decision making | Scientific Reports</a></li>
<li><a href="https://arxiv.org/abs/2502.13062">[2502.13062] AI-Assisted Decision Making with Human Learning</a></li>

</ul>
</details>

**标签**: `#AI-assisted decision-making`, `#human-AI alignment`, `#online learning`, `#confidence calibration`

---

<a id="item-16"></a>
## [KAN 在 DP-SGD 和相关噪声下的首个总体风险界](https://arxiv.org/abs/2605.12648) ⭐️ 8.0/10

本文首次为使用小批量 SGD 和带有相关噪声的 DP-SGD 训练的 Kolmogorov-Arnold 网络建立了总体风险界，弥合了差分隐私训练的理论与实践差距。 这项工作意义重大，因为它为 KAN 在更接近实际实现的训练条件（小批量 SGD 和相关噪声）下提供了理论保证，超越了以往的全批量分析。它还引入了非凸 DP 训练中相关噪声的新型分析框架，可能影响隐私保护机器学习。 本文涵盖了非私有 SGD 和 DP-SGD，其中高斯扰动在独立噪声和时间相关噪声之间插值。技术核心包括辅助无投影动力学、吸收当前噪声扰动的移位迭代，以及证明投影不活动的高概率自举方法。

rss · arXiv - Machine Learning · May 14, 04:00

**背景**: Kolmogorov-Arnold 网络是一种受 Kolmogorov-Arnold 表示定理启发的神经网络架构，其中每个权重被替换为可学习的单变量函数。DP-SGD 是一种标准的差分隐私训练方法，通过裁剪梯度并添加噪声来保护隐私；相关噪声机制在经验上表现出比独立噪声更好的隐私-效用权衡。总体风险衡量真实数据分布上的期望损失，提供了泛化能力的理论界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://arxiv.org/abs/2404.19756">[2404.19756] KAN: Kolmogorov - Arnold Networks</a></li>
<li><a href="https://arxiv.org/html/2601.22334">DP-𝜆CGD: Efficient Noise Correlation for Differentially Private Model Training</a></li>

</ul>
</details>

**标签**: `#Kolmogorov-Arnold Networks`, `#Differential Privacy`, `#DP-SGD`, `#Population Risk`, `#Correlated Noise`

---

<a id="item-17"></a>
## [嵌入时序逻辑：自主系统运行时监控新方法](https://arxiv.org/abs/2605.12651) ⭐️ 8.0/10

研究人员提出嵌入时序逻辑（ETL），这是一种新颖的时序逻辑，可直接在学习的嵌入空间中对基于感知的自主系统进行运行时监控，从而能够指定高级感知概念，如视觉目标和语义区域。 ETL 解决了传统运行时监控的一个关键限制——需要脆弱且昂贵的学习模块将传感器数据映射到逻辑命题，有望提高自动驾驶汽车和机器人等安全关键自主系统的安全性和可靠性。 ETL 通过观测嵌入与参考观测目标嵌入之间的距离定义谓词，并包含一个保形校准过程，以实现可靠、面向安全的谓词评估。该方法在多个操作环境中进行了评估，与真实语义表现出高度一致性。

rss · arXiv - Machine Learning · May 14, 04:00

**背景**: 自主系统的运行时监控传统上使用时序逻辑来检查系统行为是否符合规范，但需要将连续传感器数据映射到离散逻辑命题——这一过程通常依赖额外的学习模块，这些模块可能计算成本高昂且语义不对齐。嵌入空间是深度学习中常用的技术，它将高维数据（如图像、传感器读数）表示为保留语义关系的低维向量，从而能够直接比较感知概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12651">[2605.12651] Runtime Monitoring of Perception-Based Autonomous ...</a></li>

</ul>
</details>

**标签**: `#temporal logic`, `#runtime monitoring`, `#autonomous systems`, `#perception`, `#embedding`

---

<a id="item-18"></a>
## [scShapeBench：自动检测单细胞 RNA 测序数据中的几何结构](https://arxiv.org/abs/2605.12662) ⭐️ 8.0/10

研究人员提出了 scShapeBench，这是一个用于单细胞 RNA 测序数据形状检测的基准数据集，以及 scReebTower，一种利用扩散几何提取 Reeb 图以自动选择分析流程的基线方法。 这项工作通过自动化检测几何结构（聚类、轨迹、原型），解决了单细胞分析中的一个关键瓶颈，减少了对人工视觉检查的依赖，并为生物信息学提供了更客观的流程选择。 scShapeBench 包括从真实骨架图采样的合成数据集和由专家注释为四类（聚类、单轨迹、多分支和原型）的真实单细胞数据集。scReebTower 在合成数据和真实数据上均优于 PAGA 和 Mapper 等现有基线方法。

rss · arXiv - Machine Learning · May 14, 04:00

**背景**: 单细胞 RNA 测序（scRNA-seq）测量单个细胞中的基因表达，产生高维数据。常见的分析流程如 Seurat 假设数据是聚类的，而 Monocle 等则假设是轨迹结构，因此选择正确的流程通常需要人工检查。自动形状检测可以简化这一过程，尤其对于自主 AI 科学家而言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nnoll/seqspace">GitHub - nnoll/seqspace: Library to normalize scRNAseq expression data and learn its underlying geometric structure · GitHub</a></li>
<li><a href="https://satijalab.org/seurat/articles/pbmc3k_tutorial.html">Seurat - Guided Clustering Tutorial • Seurat</a></li>

</ul>
</details>

**标签**: `#single-cell RNA-seq`, `#geometry learning`, `#benchmark`, `#bioinformatics`, `#high-dimensional data`

---

<a id="item-19"></a>
## [LLM 多样性崩溃与校准问题相关](https://arxiv.org/abs/2605.11128) ⭐️ 8.0/10

该论文提出了一个有效性-多样性框架，将 LLM 多样性崩溃归因于两种校准失调：顺序校准（有效 token 未能可靠排在无效 token 之上）和形状校准（概率质量过度集中在少数有效延续上）。 这项工作为 LLM 为何产生狭窄输出提供了理论解释，这对于改进创意生成、科学发现等需要多样化输出的应用至关重要。它表明修复校准问题可以在不牺牲质量的情况下提高多样性。 该框架将多样性崩溃分解为局部失败，这些失败在解码步骤中累积，导致序列级别的多样性严重损失。在 14 个语言模型上的实证测试证实，问题不仅是采样启发式的局限，更是校准失调的结果。

rss · arXiv - NLP · May 14, 04:00

**背景**: LLM 通过逐步预测下一个 token 来生成文本。多样性崩溃指的是模型即使存在多个有效延续，也倾向于产生相似或重复输出的现象。先前的工作侧重于测量多样性，但未理解其背后的概率原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2504.12522">Evaluating the Diversity and Quality of LLM Generated Content</a></li>
<li><a href="https://www.researchgate.net/publication/390892668_Evaluating_the_Diversity_and_Quality_of_LLM_Generated_Content">(PDF) Evaluating the Diversity and Quality of LLM Generated Content</a></li>

</ul>
</details>

**标签**: `#LLM`, `#diversity`, `#calibration`, `#decoding`, `#generation`

---

<a id="item-20"></a>
## [ClinicalBench：对临床问答中的断言感知检索进行压力测试](https://arxiv.org/abs/2605.11143) ⭐️ 8.0/10

研究人员推出了 ClinicalBench，这是一个基于 43 名 MIMIC-IV 患者的 400 道题基准测试，以及 EpiKG，一种通过引入断言标签和时间性标签来改进临床问答的检索方法。 这项工作解决了临床问答中常被忽视但至关重要的断言感知检索步骤，其中否定、时间性和归属可能将正确答案变为错误答案，从而可能提高 AI 辅助临床决策支持的可靠性。 EpiKG 在主要终点上比基线提高了 22.0 个百分点（p=0.0192），并且医生裁决显示 56%的自动生成参考答案存在缺陷，凸显了临床问答基准测试中人工评估的必要性。

rss · arXiv - NLP · May 14, 04:00

**背景**: 从电子健康记录（EHR）中进行临床问答需要准确检索相关事实，但真实的临床笔记包含否定（例如“无胸痛”）、时间约束（例如“上周”）和归属问题（例如家族史与患者状况）。标准检索方法通常忽略这些细微差别，导致答案错误。ClinicalBench 和 EpiKG 旨在通过显式建模断言和时间性来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://link.springer.com/article/10.1007/s00521-025-11666-9">A survey on retrieval-augmentation generation (RAG) models for healthcare applications | Neural Computing and Applications | Springer Nature Link</a></li>
<li><a href="https://physionet.org/content/mimic-iv-ext-medicalbench/1.0.0/">MIMIC-IV-Ext-MedicalBench: Evaluating Large Language Models Towards Improved Medical Concept Extraction v1.0.0</a></li>

</ul>
</details>

**标签**: `#clinical QA`, `#retrieval`, `#EHR`, `#benchmark`, `#NLP`

---

<a id="item-21"></a>
## [分解进化混合 LoRA：路由器重写是关键](https://arxiv.org/abs/2605.11153) ⭐️ 8.0/10

一篇新论文在 1.5 亿参数模型上分解了进化混合 LoRA 系统，发现路由器重写贡献了全部性能提升，而生命周期机制反而是净拖累。 这项工作为进化微调中的增益提供了严格的归因，帮助研究人员聚焦于最有影响力的组件，避免无效的复杂性。 路由器重写使用并行 sigmoid 门控，具有可学习的每适配器下限和有界温度退火，输入为堆叠后的隐藏状态。生命周期包括死亡、alpha 混合继承、SVD 变异和槽位重分配，但被发现使性能下降约-0.028 nats。

rss · arXiv - NLP · May 14, 04:00

**背景**: 混合 LoRA（MoA）将多个低秩适配器（LoRA）与路由机制结合，以高效处理多个任务。进化算法可以随时间优化路由和适配器参数。本文使用析因实验来隔离每个组件的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2403.03432">[2403.03432] Mixture-of-LoRAs: An Efficient Multitask Tuning for Large Language Models</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LoRA`, `#mixture-of-experts`, `#evolutionary algorithms`, `#fine-tuning`, `#deep learning`

---

<a id="item-22"></a>
## [双室模型：通过隐藏状态耦合冻结语言模型](https://arxiv.org/abs/2605.11167) ⭐️ 8.0/10

双室模型引入了一个可训练的神经接口，通过连续的隐藏状态交换耦合两个冻结的语言模型，使它们无需生成文本即可协调。在算术任务上，将 0.5B 模型与计算器耦合，准确率从 36%提升至 96%。 这项工作展示了多模型和工具增强系统的新范式，从基于文本的序列化转向连续并发通信。它可能实现更高效、更强大的 AI 系统，无需重新训练即可组合专用模型。 该接口由一个翻译网络和一个可学习的抑制门组成，仅增加约 1%的组合参数。该门仅从任务损失中学习选择性通信协议，无需预设格式。该方法在算术、逻辑谜题和数学推理任务上使用不同工具后端进行了演示。

rss · arXiv - NLP · May 14, 04:00

**背景**: 传统的多模型系统通过生成文本来通信，每次交换都通过输出词汇表序列化。双室模型则使用中间隐藏状态上的连续通道，使两个冻结的语言模型同步运行并相互调节激活。这种方法受到“双室心智”概念的启发，即两个独立过程相互协调。

**标签**: `#language models`, `#multi-model systems`, `#neural interfaces`, `#tool augmentation`, `#hidden-state coupling`

---

<a id="item-23"></a>
## [差分隐私在某些任务中减少 LLM 偏见，但并非全部](https://arxiv.org/abs/2605.11195) ⭐️ 8.0/10

一项新的系统评估显示，使用差分隐私（DP-SGD）训练 LLM 在句子评分任务中减少了社会偏见，但在文本补全、表格分类或问答任务中并非普遍有效。 这项研究强调隐私和公平并非自动一致，敦促研究者在部署差分隐私 LLM 时跨多种范式评估偏见。 该论文在四种范式下比较了 DP 模型与非 DP 基线，并发现 logit 级偏见（模型内部分数）与输出级偏见（生成文本）之间存在差异。

rss · arXiv - NLP · May 14, 04:00

**背景**: 差分隐私（DP）限制单个训练数据点对模型的影响程度，通常通过 DP-SGD 实现，该方法裁剪梯度并添加噪声。LLM 中的社会偏见指模型输出中的系统性不公平倾向。先前的工作通常分别研究偏见或隐私；这项工作考察了它们的相互作用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/pytorch/differential-privacy-series-part-1-dp-sgd-algorithm-explained-12512c3959a3">Differential Privacy Series Part 1 | DP-SGD Algorithm Explained | by PyTorch | PyTorch | Medium</a></li>
<li><a href="https://arxiv.org/html/2503.11985v1">No LLM is Free From Bias: A Comprehensive Study of Bias Evaluation in Large Language models</a></li>
<li><a href="https://www.semanticscholar.org/paper/On-Measuring-Social-Biases-in-Sentence-Encoders-May-Wang/5e9c85235210b59a16bdd84b444a904ae271f7e7">[PDF] On Measuring Social Biases in Sentence Encoders | Semantic Scholar</a></li>

</ul>
</details>

**标签**: `#differential privacy`, `#social bias`, `#large language models`, `#fairness`, `#DP-SGD`

---

<a id="item-24"></a>
## [指令塑造输出生成，而非输入处理](https://arxiv.org/abs/2605.11206) ⭐️ 8.0/10

一篇新论文揭示，语言模型中的指令主要影响输出词元的生成，而非输入词元的处理，并通过基于注意力的因果干预证实了这种不对称性。 这一发现挑战了关于指令如何影响模型行为的常见假设，为 LLM 可解释性和对齐研究提供了更深入的见解。 该研究使用了五个二元判断任务，并在不同提示变体中测量样本词元和输出词元中的任务特定信息，发现输出词元信息与行为强相关，而样本词元信息则不然。

rss · arXiv - NLP · May 14, 04:00

**背景**: 语言模型处理输入词元以理解上下文，并生成输出词元以产生响应。注意力机制使模型能够关注输入的相关部分。因果推断方法有助于确定模型内部因果关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2109.00725">[2109.00725] Causal Inference in Natural Language Processing: Estimation, Prediction, Interpretation and Beyond</a></li>
<li><a href="https://en.wikipedia.org/wiki/Attention_(machine_learning)">Attention (machine learning) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#interpretability`, `#instructions`, `#causal analysis`, `#language models`

---

<a id="item-25"></a>
## [ReVision 将计算机使用代理的视觉令牌减少 46%](https://arxiv.org/abs/2605.11212) ⭐️ 8.0/10

研究人员提出了 ReVision，该方法通过移除连续截图中的冗余补丁，将计算机使用代理的视觉令牌使用量减少约 46%，同时在 OSWorld、WebTailBench 和 AgentNetBench 等基准测试上将成功率提升 3%。 这解决了计算机使用代理中的一个关键瓶颈——视觉令牌爆炸——使得在不增加计算量的情况下处理更长的历史记录成为可能，从而可能显著改进 GUI 自动化和多模态 AI 系统。 ReVision 使用一个学习到的补丁选择器，比较连续截图间的补丁表示并保留空间结构，并在 Qwen2.5-VL-7B 上训练。该方法表明，当冗余被移除时，性能随着历史记录增加而持续提升，这与先前的饱和观察结果相矛盾。

rss · arXiv - NLP · May 14, 04:00

**背景**: 计算机使用代理（CUA）依赖图形用户界面的视觉观察，将每个截图编码为大量视觉令牌。随着交互轨迹增长，令牌成本迅速增加，限制了在固定计算预算下可纳入的历史信息量。ReVision 通过选择性移除连续帧之间的视觉冗余补丁来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.11212">[2605.11212] ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction</a></li>
<li><a href="https://arxiv.org/html/2605.11212">ReVision: Scaling Computer-Use Agents via Temporal Visual Redundancy Reduction</a></li>

</ul>
</details>

**标签**: `#computer-use agents`, `#multimodal language models`, `#visual token reduction`, `#GUI automation`, `#efficient AI`

---

<a id="item-26"></a>
## [VideoSEAL：长视频问答的解耦框架](https://arxiv.org/abs/2605.12571) ⭐️ 8.0/10

VideoSEAL 提出了一种解耦的规划器-检查器框架，将规划与答案权威分离，以缓解智能体长视频理解中的证据错位问题，在 LVBench 上达到 55.1%，在 LongVideoBench 上达到 62.0%。 该框架引入了两个诊断指标（时间基础性和语义基础性），并揭示了提示压力和奖励压力会加剧错位。解耦架构支持即插即用的 MLLM 升级，无需重新训练规划器。

rss · arXiv - Computer Vision · May 14, 04:00

**背景**: 长视频问答需要在长视频中定位稀疏的证据，通常需要多轮智能体交互。现有智能体存在证据错位问题，即正确答案缺乏支持性视觉证据，这是由于将规划与答案权威混为一谈所致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.14468">[2603.14468] LongVidSearch: An Agentic Benchmark for Multi-hop Evidence Retrieval Planning in Long Videos</a></li>
<li><a href="https://arxiv.org/abs/2601.18157">[2601.18157] Agentic Very Long Video Understanding</a></li>

</ul>
</details>

**标签**: `#video understanding`, `#multi-modal LLMs`, `#agentic systems`, `#evidence alignment`, `#long video QA`

---

<a id="item-27"></a>
## [自注意力中逆温度缩放的统一理论](https://arxiv.org/abs/2605.12697) ⭐️ 8.0/10

一篇新论文提出了一个统一框架，解决了自注意力中逆温度缩放定律的冲突，表明关键尺度由间隙计数函数 N_n 决定。 这项工作提供了一个统一先前矛盾结果的通用理论，为注意力分数族提供了诊断工具，并可能指导更稳定的长上下文 Transformer 的设计。 该框架基于间隙计数函数 N_n 定义了一个上尾累积尺度，该函数统计每个间隙内与最大 logit 竞争的对手数量。低于该尺度时，顶级竞争者无法区分；高于该尺度时，注意力熵崩溃。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: Transformer 中的自注意力机制通常使用温度参数在 softmax 之前缩放 logits。对于长序列，逆温度必须随上下文长度缩放，以避免注意力崩溃或均匀平均，但先前的工作提出了冲突的缩放定律（例如 sqrt(log n)、log n、(log n)^2）。本文提供了一个统一的理论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08505">[2605.08505] Scaling Limits of Long-Context Transformers</a></li>

</ul>
</details>

**标签**: `#self-attention`, `#transformers`, `#scaling laws`, `#theory`, `#deep learning`

---

<a id="item-28"></a>
## [鲁棒序贯 A/B 测试框架](https://arxiv.org/abs/2605.12899) ⭐️ 8.0/10

提出了一种新的鲁棒序贯实验设计框架，用于 A/B 测试，能够处理模型误设问题，并给出了最坏情况均方误差的理论界，以及来自一家领先科技公司的真实数据实证验证。 这项工作解决了 A/B 测试中的一个关键空白，即在假设模型不正确（实践中常见）时提供鲁棒性保证，可提高许多行业实验的可靠性和样本效率。 该框架涵盖上下文赌博机和动态设置，并在理论上限制了估计处理效应的最坏情况均方误差。在合成和真实数据集上的实证结果证明了其有效性。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: A/B 测试广泛用于比较产品或策略的两个版本。序贯实验设计根据累积数据自适应分配用户到不同处理组，以提高效率。然而，现有设计通常假设统计模型正确设定，这在实践中可能不成立，导致结论不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Design_of_experiments">Design of experiments - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Statistical_model_specification">Statistical model specification - Wikipedia</a></li>

</ul>
</details>

**标签**: `#A/B testing`, `#experimental design`, `#causal inference`, `#robustness`, `#sequential decision making`

---

<a id="item-29"></a>
## [理论证明弱到强泛化可激发潜在特征](https://arxiv.org/abs/2605.12908) ⭐️ 8.0/10

一篇新的理论论文证明，在两层神经网络的奖励模型学习设置中，弱到强泛化能够从强模型中激发潜在特征，同时保留其通用能力。 这项工作为弱到强泛化提供了严格的理论基础，这是对齐超人类 AI 系统的关键方法，并表明它可以避免标准微调导致的灾难性遗忘。 强模型的预训练表示被组织成低维子空间，论文证明多步 SGD 可以学习目标特征方向，同时保留非目标特征，即使它们之间存在相关性。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: 弱到强泛化是一种对齐技术，其中弱模型监督强模型，旨在利用强模型的能力同时使其与人类意图对齐。先前的理论工作要么固定学生模型的表示，要么使用受限设置，未解决特征学习能否成功的问题。本文通过分析两层神经网络填补了这一空白，表明强模型可以在不遗忘的情况下激发预训练知识。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wandb.ai/byyoung3/ml-news/reports/OpenAI-s-New-Alignment-Paper--Vmlldzo2MzA0NzQ3">OpenAI's New Alignment Paper | ml-news – Weights & Biases</a></li>
<li><a href="https://www.lesswrong.com/posts/ELbGqXiLbRe6zSkTu/a-review-of-weak-to-strong-generalization-ai-safety-camp">A Review of Weak to Strong Generalization [ AI Safety...] — LessWrong</a></li>
<li><a href="https://www.alignmentforum.org/posts/bkbaXuo5mh8LP34rM/weak-to-strong-generalization">Weak - To - Strong Generalization — AI Alignment Forum</a></li>

</ul>
</details>

**标签**: `#AI alignment`, `#weak-to-strong generalization`, `#feature learning`, `#neural networks`, `#theoretical analysis`

---

<a id="item-30"></a>
## [黑盒生成-验证 AI 工作流的始终有效发布方法](https://arxiv.org/abs/2605.12947) ⭐️ 8.0/10

研究人员提出了一种用于黑盒生成-验证 AI 工作流的始终有效发布包装器，它利用硬负例参考池和 e-process 来确保在可选监控下做出有效的停止决策。 这通过提供一种原则性的统计方法来决定何时停止并发布结果，填补了部署基于 LLM 的迭代工作流的关键空白，减少了过早的错误发布，同时保持了效率。 该包装器将部署时的评估器分数与高得分失败的硬负例参考池进行校准，并通过 e-process 累积证据，从而在不可行任务上提供有限样本的发布控制。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: AI 工作流通常使用生成-验证循环来迭代改进输出。决定何时停止具有挑战性，因为评估器分数是自适应生成并重复监控的，违反了标准统计假设。始终有效推断和 e-process 是允许在持续监控下进行有效假设检验的统计工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1512.04922">[1512.04922] Always Valid Inference: Bringing Sequential Analysis to A/B Testing</a></li>
<li><a href="https://en.wikipedia.org/wiki/E-values">E-values - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI workflows`, `#statistical inference`, `#LLM`, `#e-process`, `#generate-verify`

---

<a id="item-31"></a>
## [CCVFM：基于核心集增强的流匹配生成模型](https://arxiv.org/abs/2605.12951) ⭐️ 8.0/10

CCVFM 提出了一种新方法，将层次流匹配中的各向同性高斯噪声源替换为从目标数据核心集导出的高斯混合，仅需一个轻量级校正流来优化从代理分布到目标分布的残差。 该方法通过从数据驱动的源分布出发，减轻了学习负担，有望提高生成建模的效率和少步生成质量，可能对图像生成等应用产生影响。 核心集通过熵 Sinkhorn 核心集方法构建，代理源分布是一个闭式高斯混合，无需神经网络即可采样。论文提供了理论保证，将代理传输成本与 Wasserstein 差距联系起来，并在 MNIST、CIFAR-10、ImageNet-32 和 CelebA-HQ 上展示了具有竞争力的结果。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: 流匹配是一种生成建模技术，通过常微分方程学习从简单源分布（如高斯噪声）到复杂数据分布的连续变换。层次整流流通过在速度空间中建模速度场来扩展这一方法，但其内部流仍从各向同性高斯噪声开始。核心集方法将大型数据集压缩为一小组加权代表点，保留关键分布特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2502.17436">[2502.17436] Towards Hierarchical Rectified Flow</a></li>
<li><a href="https://arxiv.org/html/2504.20194">Coreset selection for the Sinkhorn divergence and generic smooth divergences</a></li>
<li><a href="https://github.com/amkokot/sinkhorn_coresets">GitHub - amkokot/sinkhorn_coresets</a></li>

</ul>
</details>

**标签**: `#generative models`, `#flow matching`, `#coreset`, `#machine learning`, `#arXiv`

---

<a id="item-32"></a>
## [基于小波的 DPP 核改进小批量方差缩减](https://arxiv.org/abs/2605.13127) ⭐️ 8.0/10

本文提出了基于小波的新型行列式点过程（DPP）核，在理论上比现有方法实现了更好的小批量与核心集方差缩减，并提供了一种从连续 DPP 到离散 DPP 的通用转换方法，该转换保留了方差衰减特性并支持高效采样。 这项工作通过解决两个关键瓶颈推动了机器学习中基于 DPP 的子采样：方差缩减 DPP 的有限族以及离散 DPP 的临时构造问题。它还扩展了低正则性目标函数的适用性，可能提高更广泛机器学习模型的训练效率。 所提出的欧几里得空间上的小波 DPP 在理论上实现了比已知最佳速率更好的精度保证。转换方法揭示了离散核的低秩分解，使得采样计算成本低廉。

rss · arXiv - Data Science & Statistics · May 14, 04:00

**背景**: 行列式点过程（DPP）是捕捉点之间排斥性的概率模型，适用于生成多样化的子集。在机器学习中，DPP 用于小批量选择和核心集构建，以减少随机优化中的方差。然而，现有的 DPP 核通常缺乏理论上的方差缩减保证，且将连续 DPP 转换为适用于真实数据集的离散 DPP 具有挑战性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Determinantal_point_process">Determinantal point process</a></li>
<li><a href="https://en.wikipedia.org/wiki/Coreset">Coreset - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2004.13146">[2004.13146] The Impact of the Mini-batch Size on the Variance of Gradients in Stochastic Gradient Descent</a></li>

</ul>
</details>

**标签**: `#determinantal point processes`, `#minibatches`, `#coresets`, `#wavelets`, `#variance reduction`

---

<a id="item-33"></a>
## [AI 聊天机器人泄露真实电话号码，引发骚扰](https://www.technologyreview.com/2026/05/13/1137203/ai-chatbots-are-giving-out-peoples-real-phone-numbers/) ⭐️ 8.0/10

谷歌的生成式 AI 聊天机器人向用户泄露了真实的个人电话号码，导致许多人遭受骚扰电话的困扰。一位 Reddit 用户报告称，他不断接到陌生人的电话，对方称是从谷歌的 AI 那里得到了他的号码。 这一隐私泄露事件使数百万聊天机器人用户面临潜在的“人肉搜索”和骚扰风险，削弱了人们对 AI 系统的信任。它凸显了在大型语言模型中加强数据清洗和隐私保护措施的紧迫性。 泄露的号码似乎来自从公共互联网抓取的训练数据，包括企业名录和个人联系页面。受影响的人表示，目前没有简单的退出机制来防止他们的信息被 AI 暴露。

rss · MIT Technology Review · May 13, 18:09

**背景**: 像谷歌 Gemini 这样的 AI 聊天机器人是在从网络抓取的海量数据集上训练的，这些数据可能无意中包含个人联系信息。当用户询问某个企业或服务时，模型可能会产生幻觉或直接从训练数据中输出真实的电话号码。这是 AI 隐私风险大趋势的一部分，还包括数据泄露和未经授权与第三方共享数据等问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/13/1137203/ai-chatbots-are-giving-out-peoples-real-phone-numbers/">AI chatbots are giving out people’s real phone numbers | MIT Technology Review</a></li>
<li><a href="https://www.the-independent.com/tech/ai-doxxing-gemini-hallucination-google-b2973008.html">‘AI gave me your number’: AI doxxing turning ChatGPT hallucinations into harassment | The Independent</a></li>
<li><a href="https://news.stanford.edu/stories/2025/10/ai-chatbot-privacy-concerns-risks-research">Study exposes privacy risks of AI chatbot conversations | Stanford Report</a></li>

</ul>
</details>

**社区讨论**: Reddit 等平台上的社区评论表达了愤怒和沮丧，许多人呼吁立即修复并提高透明度。一些用户分享了类似经历，而另一些人则争论责任在于 AI 公司还是数据被抓取的个人。

**标签**: `#AI`, `#privacy`, `#chatbots`, `#safety`, `#Google`

---