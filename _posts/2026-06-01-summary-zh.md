---
layout: default
title: "Horizon Summary: 2026-06-01 (ZH)"
date: 2026-06-01
lang: zh
---

> From 108 items, 35 important content pieces were selected

---

1. [黑客利用 Meta AI 机器人劫持 Instagram 账户](#item-1) ⭐️ 9.0/10
2. [ComfyUI：面向创作者的模块化节点式 AI 引擎](#item-2) ⭐️ 9.0/10
3. [中国批准全球首款侵入式脑机接口芯片](#item-3) ⭐️ 9.0/10
4. [每日药片使胰腺癌患者生存期翻倍](#item-4) ⭐️ 9.0/10
5. [斯坦福 CS336：从头构建 LLM](#item-5) ⭐️ 8.0/10
6. [英伟达发布 RTX Spark Arm 芯片，进军 Windows PC 市场](#item-6) ⭐️ 8.0/10
7. [Anthropic 秘密提交 IPO 申请](#item-7) ⭐️ 8.0/10
8. [Red Hat 云服务中发现恶意 npm 包](#item-8) ⭐️ 8.0/10
9. [OpenBMB 发布 VoxCPM2：无分词器文本转语音模型](#item-9) ⭐️ 8.0/10
10. [Anthropic 推出 Claude Code：终端中的智能编码代理](#item-10) ⭐️ 8.0/10
11. [通过从零重建技术来掌握编程](#item-11) ⭐️ 8.0/10
12. [Kronos：首个开源金融市场基础模型](#item-12) ⭐️ 8.0/10
13. [PhyDrawGen：用于物理图的神经符号流水线](#item-13) ⭐️ 8.0/10
14. [面向具身 AI 的查询条件世界模型](#item-14) ⭐️ 8.0/10
15. [自进化 LLM 代理中的能力解耦：更新与收益](#item-15) ⭐️ 8.0/10
16. [EHRBench：面向 LLM 临床决策的自动化基准](#item-16) ⭐️ 8.0/10
17. [通过策略即代码搜索实现医疗机制设计](#item-17) ⭐️ 8.0/10
18. [Unicorn：通用时间序列相关性建模框架](#item-18) ⭐️ 8.0/10
19. [线性探针以近乎完美的准确率检测 LLM 欺骗](#item-19) ⭐️ 8.0/10
20. [NumLeak 揭示 LLM 记忆公开数值基准](#item-20) ⭐️ 8.0/10
21. [LongDS 基准揭示 AI 智能体在长时数据分析中的失败](#item-21) ⭐️ 8.0/10
22. [校准偏好学习：标签排序框架](#item-22) ⭐️ 8.0/10
23. [自主智能体数据工程将 LLM 专业化提升 57%](#item-23) ⭐️ 8.0/10
24. [跨语言引导的比喻语言生成](#item-24) ⭐️ 8.0/10
25. [多模态语音模型的首个偏见研究](#item-25) ⭐️ 8.0/10
26. [英文提问导致大语言模型中的全球叙事主导](#item-26) ⭐️ 8.0/10
27. [可配置奖励模型实现平衡安全对齐](#item-27) ⭐️ 8.0/10
28. [SANA-Streaming：在消费级 GPU 上实现实时视频编辑](#item-28) ⭐️ 8.0/10
29. [Dex2HOI：统一扩散模型实现双手双物体交互生成](#item-29) ⭐️ 8.0/10
30. [VLM 在空间问题上不知何时不应回答](#item-30) ⭐️ 8.0/10
31. [从 Best-of-N 偏好数据中学习奖励函数的理论分析](#item-31) ⭐️ 8.0/10
32. [最后一层线性化在不确定性量化上媲美全网络](#item-32) ⭐️ 8.0/10
33. [弱单调性提升少样本学习](#item-33) ⭐️ 8.0/10
34. [贝叶斯滤波统一次二次序列模型](#item-34) ⭐️ 8.0/10
35. [任意有效推断修复在线决策树的分裂选择](#item-35) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [黑客利用 Meta AI 机器人劫持 Instagram 账户](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/#atom-everything) ⭐️ 9.0/10

黑客利用 Meta 的 AI 支持聊天机器人，通过简单要求机器人更改关联邮箱地址，绕过了正常的账户恢复流程，从而接管了高知名度 Instagram 账户。 这一漏洞凸显了 AI 支持系统中的关键设计缺陷：赋予 AI 机器人账户恢复工具的特权访问权限可能导致严重的安全漏洞，影响数百万用户，并削弱对 AI 驱动客户支持的信任。 攻击涉及使用与目标位置相近的 VPN IP 地址，请求密码重置，然后与 Meta 的 AI 机器人聊天以关联新邮箱，之后机器人发送了一次性验证码，允许密码重置。该漏洞不需要复杂的提示注入，只是一个直接的请求。

rss · Simon Willison · Jun 1, 21:14

**背景**: 提示注入是一种安全漏洞，攻击者通过提供恶意输入来操纵 AI 聊天机器人的行为，覆盖其预期指令。在此案例中，Meta 的 AI 支持机器人能够更改账户邮箱和禁用双因素认证，这些通常是保留给经过验证的支持人员的高安全性操作。机器人缺乏适当的身份验证和授权检查，导致了该漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/">Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts</a></li>
<li><a href="https://www.engadget.com/2185225/meta-ai-support-chatbot-made-it-ridiculously-easy-for-hackers-to-take-over-instagram-accounts/">Meta's AI support chatbot made it ridiculously easy for hackers to take over Instagram accounts - Engadget</a></li>
<li><a href="https://gbhackers.com/meta-ai-vulnerability/">Meta AI Vulnerability Allegedly Enables Instagram Password Resets</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Meta 的疏忽表示震惊，指出支持请求一直是安全链中的薄弱环节。有人质疑这是否是 AI 特有的问题，还是仅仅是糟糕的设计；其他人指出，AI 本不应被赋予移除双因素认证或向任意地址发送邮件的权限。一位用户分享了他们通过外包支持被盗取用户名的亲身经历，突显了这一反复出现的模式。

**标签**: `#security`, `#AI safety`, `#Meta`, `#Instagram`, `#vulnerability`

---

<a id="item-2"></a>
## [ComfyUI：面向创作者的模块化节点式 AI 引擎](https://github.com/Comfy-Org/ComfyUI) ⭐️ 9.0/10

ComfyUI 已发布，作为一个强大且模块化的 AI 内容创作引擎，采用图形/节点界面，支持扩散模型，可生成图像、视频、3D 模型和音频。 ComfyUI 通过提供灵活的开源工具，让创作者完全掌控模型和参数，实现可集成到生产流程中的复杂工作流，从而普及了先进的 AI 内容创作。 ComfyUI 原生支持最新的开源最先进模型，并为 Nano Banana、Seedance 等闭源模型提供 API 节点。它可通过桌面应用、便携安装或云服务在 Windows、Linux 和 macOS 上使用。

rss · GitHub Trending - Python · Jun 1, 23:22

**背景**: 扩散模型是一类生成式 AI，通过从随机噪声开始逐步细化生成有意义的输出。它们广泛用于图像和视频生成，著名例子包括 Stable Diffusion 和 DALL-E。ComfyUI 提供基于节点的图形界面，让用户可以直观地设计和连接不同模型组件，使复杂的 AI 工作流更易上手。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>

</ul>
</details>

**标签**: `#AI`, `#diffusion models`, `#GUI`, `#content creation`, `#open source`

---

<a id="item-3"></a>
## [中国批准全球首款侵入式脑机接口芯片](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/) ⭐️ 9.0/10

2026 年 3 月，中国国家药品监督管理局（NMPA）批准了 Neuracle Medical Technology 开发的神经电子机会（NEO）脑机接口，使其成为全球首款获批在临床试验之外商业使用的侵入式脑机接口产品。 这一里程碑标志着神经技术的重大飞跃，可能改变瘫痪及其他神经系统疾病的治疗方式，并使中国在与 Neuralink 等对手的全球脑机接口竞赛中占据领先地位。 NEO 设备比 Neuralink 的植入物侵入性更小，因为它不插入脑组织，而是放置在脑表面，并且已帮助一名名为董辉的瘫痪患者恢复部分活动能力，例如握笔写字。

rss · MIT Technology Review · Jun 1, 09:09

**背景**: 脑机接口（BCI）是一种读取神经信号以控制外部设备的系统。侵入式脑机接口需要通过手术将电极直接植入大脑表面或内部，提供比非侵入式方法更高的信号质量。中国批准 NEO 设备之前，经过了多年的研究和临床试验，包括 2023 年 1 月发表的一项研究，显示使用类似支架电极阵列的患者未出现严重不良事件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/">China has approved the world’s first invasive brain-computer chip—here’s what’s next | MIT Technology Review</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-03-13/china-approves-first-brain-implant-for-commercial-use">China Approves First Brain Implant for Commercial Use - Bloomberg</a></li>
<li><a href="https://en.people.cn/n3/2026/0421/c98649-20448814.html">China approves world's first implantable brain-computer interface for medical use - People's Daily Online</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#neurotechnology`, `#medical device`, `#China`, `#regulatory approval`

---

<a id="item-4"></a>
## [每日药片使胰腺癌患者生存期翻倍](https://www.bbc.com/news/articles/cy82l435171o?at_medium=RSS&at_campaign=rss) ⭐️ 9.0/10

一种名为 daraxonrasib 的每日药片已被证明能使胰腺癌患者的生存时间翻倍，标志着治疗这种致命疾病的一项重大突破。 胰腺癌是主要癌症中生存率最低的之一，五年生存率仅为 13%。这种新型口服疗法可能显著改善目前缺乏有效治疗选择的患者的预后。 Daraxonrasib (RMC-6236) 是一种口服活性、多选择性 RAS 抑制剂，靶向 RAS 蛋白的活性 GTP 结合形式，包括突变型和野生型。它采用三复合机制来克服其他 KRAS 抑制剂中出现的耐药性。

rss · BBC Health · Jun 1, 02:50

**背景**: 胰腺癌以难以治疗著称，大多数患者在晚期才被诊断，此时已无法手术。IV 期胰腺癌的五年生存率仅约 1%，诊断后平均生存期约为一年。RAS 突变（尤其是 KRAS）存在于超过 90% 的胰腺癌中，使其成为关键的治疗靶点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Daraxonrasib">Daraxonrasib - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/org/science/article/pii/S1520480425002959">Discovery of Daraxonrasib (RMC-6236), a Potent and Orally ...</a></li>
<li><a href="https://www.cancer.org/cancer/types/pancreatic-cancer/detection-diagnosis-staging/survival-rates.html">Survival Rates for Pancreatic Cancer - American Cancer Society</a></li>

</ul>
</details>

**标签**: `#cancer`, `#pharmaceuticals`, `#breakthrough`, `#health`, `#pancreatic cancer`

---

<a id="item-5"></a>
## [斯坦福 CS336：从头构建 LLM](https://cs336.stanford.edu/) ⭐️ 8.0/10

斯坦福大学的 CS336 课程提供了从头实现语言模型的严格训练，涵盖从数据预处理到训练和评估的完整流程，所有作业均在线开放。 该课程通过提供现代语言模型核心组件的动手实践，填补了实用 LLM 教育的关键空白，对寻求深入理解的研究人员和工程师极具价值。 该课程需要大量 GPU 算力（例如 B200 每小时 4.99 美元）和扎实的机器学习基础（如 CS229 或同等水平）。社区反馈指出前两个作业尤其具有挑战性且耗时。

hackernews · kristianpaul · Jun 1, 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48357075)

**背景**: 像 GPT-4 这样的语言模型通常使用深度学习框架（如 PyTorch）构建，并在大规模 GPU 集群上训练。CS336 去除了抽象层，要求学生仅使用基础库从头实现关键组件（如注意力机制和训练循环），这与早期 Transformer 研究的方法类似。

**社区讨论**: 社区评论非常积极，用户称赞课程的深度和严谨性。一位用户分享完成 2025 版本花费了数月业余时间，另一位用户则讨论了 GPU 需求，指出 Vast.ai 上的 4090 足以应对早期阶段。还有用户询问注重实现的先修课程，表明自学者的兴趣。

**标签**: `#LLM`, `#deep learning`, `#NLP`, `#education`, `#Stanford`

---

<a id="item-6"></a>
## [英伟达发布 RTX Spark Arm 芯片，进军 Windows PC 市场](https://www.nvidia.com/en-us/products/rtx-spark/) ⭐️ 8.0/10

这标志着英伟达进入 Windows on ARM PC 市场，直接挑战英特尔、AMD 和苹果 M 系列芯片。RTX Spark 将英伟达的 GPU 和 AI 能力与 Arm CPU 核心相结合，可能重塑 PC 格局。 RTX Spark 是一款 1 petaflop 超级芯片，支持完整的 CUDA 和 RTX 生态系统，超过 100 家软件提供商（包括 Adobe、Blender 以及 Riot Games 等游戏开发商）已承诺推出原生 Arm 版本。然而，兼容性、性能和功耗方面仍存在担忧。

hackernews · shenli3514 · Jun 1, 05:24 · [社区讨论](https://news.ycombinator.com/item?id=48352939)

**背景**: Windows on ARM 历来在软件兼容性和性能方面与 x86 系统相比存在困难。苹果成功过渡到自研的基于 Arm 的 M 系列芯片展示了定制硅片的潜力，但 Windows on ARM 尚未取得类似的进展。英伟达的 RTX Spark 旨在利用其 GPU 和 AI 专业知识改变这一现状。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/05/31/nvidias-new-chip-to-power-fresh-line-of-windows-laptops-by-dell-hp.html">Nvidia jumps into PCs with new Arm-based chip debuting in laptops from Microsoft, Dell, HP</a></li>
<li><a href="https://www.pcmag.com/news/nvidia-rtx-spark-reinvent-pc-computex-2026">Nvidia Unveils RTX Spark, an Arm-Based Superchip for Windows PCs | PCMag</a></li>
<li><a href="https://www.mediatek.com/products/personal-computing/nvidia-rtx-spark">MediaTek | RTX Spark | Next Era of Windows PCs</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了兴奋也表达了怀疑。一些用户称赞英伟达能够为大型游戏和创意应用争取到原生 Arm 移植，而另一些用户则指出了兼容性问题、性能夸大和发热等尖锐问题。此外，也有用户对 Linux 支持表示好奇。

**标签**: `#Nvidia`, `#RTX Spark`, `#Arm`, `#Windows on Arm`, `#hardware`

---

<a id="item-7"></a>
## [Anthropic 秘密提交 IPO 申请](https://www.anthropic.com/news/confidential-draft-s1-sec) ⭐️ 8.0/10

Anthropic 已向美国证券交易委员会（SEC）秘密提交了 S-1 注册声明草案，这是其迈向首次公开募股（IPO）的重要一步。 此举标志着 Anthropic 作为领先 AI 公司的成熟，将使其接受公开市场 scrutiny，可能影响更广泛的 AI 行业和散户投资者。此次 IPO 也可能加剧前沿 AI 实验室之间的竞争。 根据 JOBS 法案，秘密提交允许 Anthropic 在临近 IPO 日期前对其财务细节保密。该公司尚未披露股票数量或价格范围。

hackernews · surprisetalk · Jun 1, 16:00 · [社区讨论](https://news.ycombinator.com/item?id=48358646)

**背景**: S-1 是 SEC 要求计划上市的公司提交的注册声明，包含详细的财务和业务信息。秘密提交允许新兴成长公司最初私下提交 S-1，减少市场猜测，并允许他们在公开披露前完善文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Form_S-1">Form S-1 - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/s/sec-form-s-1.asp">What Is SEC Form S-1? Filing Steps & Amendment Guidelines</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Confidential IPO Filings | DFIN</a></li>

</ul>
</details>

**社区讨论**: 评论者对时机和潜在风险表示担忧，指出 IPO 热潮可能由当前良好的财务状况驱动，并希望在市场条件恶化前上市。一些人担心季度盈利压力可能挑战 AI 公司的长期理念，并导致反竞争行为。

**标签**: `#Anthropic`, `#IPO`, `#AI industry`, `#finance`, `#regulation`

---

<a id="item-8"></a>
## [Red Hat 云服务中发现恶意 npm 包](https://github.com/RedHatInsights/javascript-clients/issues/492) ⭐️ 8.0/10

在 @redhat-cloud-services 范围内的多个 npm 包被发现包含恶意负载，通过预安装钩子执行，窃取 AWS、Azure、GCP 等平台的云凭证和密钥。 此次针对 Red Hat 官方包的真实供应链攻击凸显了 npm 生态系统面临的持续威胁，并强调了采取依赖冷却期和多因素认证等更强防御措施的紧迫性。 恶意包部署了一个多阶段凭证窃取器，目标包括 AWS 访问密钥、GCP 服务账户、Azure 令牌、Kubernetes 密钥等。受影响的版本涵盖 RedHat Cloud Services 前端生态系统中的多个包。

hackernews · kurmiashish · Jun 1, 13:30 · [社区讨论](https://news.ycombinator.com/item?id=48356625)

**背景**: npm 供应链攻击是指攻击者入侵合法包以注入恶意代码，通常在安装时执行。建议的缓解措施包括依赖冷却期（将新包的安装延迟 1-3 天）和发布时使用多因素认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised">Multiple redhat-cloud-services npm Packages compromised - StepSecurity</a></li>
<li><a href="https://cybersecuritynews.com/red-hat-cloud-services-npm-packages/">Multiple Red Hat Cloud Services npm Packages Compromised to Deploy Credential-Stealing Malware</a></li>
<li><a href="https://www.mend.io/blog/redhat-cloud-services-packages-drop-multi-cloud-credential-stealer/">Miasma: Red Hat Cloud Services npm Packages Hit by a Mini Shai-Hulud-Style Campaign</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了依赖冷却期和多因素认证的有效性，有人指出 yarn 4 等工具已提供冷却期选项。其他人指出许多攻击在 1-3 天内就会被发现，因此冷却期是一种实用的防御手段。

**标签**: `#npm`, `#supply chain security`, `#Red Hat`, `#open source`, `#dependency management`

---

<a id="item-9"></a>
## [OpenBMB 发布 VoxCPM2：无分词器文本转语音模型](https://github.com/OpenBMB/VoxCPM) ⭐️ 8.0/10

OpenBMB 发布了 VoxCPM2，这是一个 20 亿参数的无分词器文本转语音模型，基于超过 200 万小时的多语言语音数据训练，支持 30 种语言、语音设计和语音克隆。 VoxCPM2 通过消除离散分词化，实现了更自然、更具表现力的语音合成，并支持仅凭文本描述进行创意语音设计，推动了开源 TTS 的发展。 该模型采用基于 MiniCPM-4 骨干网络的扩散自回归架构，输出 48kHz 录音室级音频。它支持带可选风格引导的可控语音克隆，以及保留所有声音细节的终极克隆。

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**背景**: 传统 TTS 系统通常使用离散分词器（如音频编解码器）将语音转换为令牌，这可能会丢失韵律和情感细节。像 VoxCPM2 这样的无分词器模型直接生成连续语音表示，保留了自然度。OpenBMB 以开源大语言模型（如 MiniCPM）而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/OpenBMB/VoxCPM/">GitHub - OpenBMB/VoxCPM: VoxCPM2: Tokenizer-Free TTS for ...</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/voxcpm-1-5-tokenizer-free-tts-with-voice-cloning-c63059b85882">VoxCPM 1.5: Tokenizer-Free TTS with Voice Cloning | by Mehul Gupta | Data Science in Your Pocket | Medium</a></li>
<li><a href="https://deepwiki.com/OpenBMB/VoxCPM/5.2-voxcpmmodel-and-voxcpm2model">VoxCPMModel and VoxCPM2Model | OpenBMB/VoxCPM | DeepWiki</a></li>

</ul>
</details>

**标签**: `#TTS`, `#speech generation`, `#voice cloning`, `#multilingual`, `#open-source`

---

<a id="item-10"></a>
## [Anthropic 推出 Claude Code：终端中的智能编码代理](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 发布了 Claude Code，这是一款直接在终端中运行的智能编码工具，能够理解整个代码库，并通过自然语言命令自动完成代码编辑、git 工作流和复杂代码解释等任务。 Claude Code 将强大的 AI 辅助直接带入开发者的终端环境，减少了上下文切换，实现了更快、更直观的编码工作流。它与 Cursor、Cline 等其他智能编码工具竞争，可能重塑开发者在日常开发中与 AI 交互的方式。 Claude Code 支持通过 curl、Homebrew、WinGet 和 npm（已弃用）安装，需要 Node.js 18+。它还提供插件以扩展功能，并通过 @claude 提及与 GitHub 集成。

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**背景**: 智能编码工具是 AI 驱动的助手，可以在开发者的环境中自主执行编码任务，例如编辑文件、运行命令和管理版本控制。与传统的代码补全工具不同，它们能理解项目的完整上下文，并根据自然语言指令执行多步骤工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude</a></li>

</ul>
</details>

**标签**: `#AI`, `#developer-tools`, `#coding-assistant`, `#Anthropic`, `#CLI`

---

<a id="item-11"></a>
## [通过从零重建技术来掌握编程](https://github.com/codecrafters-io/build-your-own-x) ⭐️ 8.0/10

GitHub 上的 'build-your-own-x' 仓库精选了超过 20 种流行技术的从零开始逐步指南，包括数据库、Git、Docker 和编程语言。 该资源通过鼓励开发者自己构建技术来促进深度学习，这比被动消费更有效。它已成为开发者社区中广泛引用的动手学习汇编。 该仓库涵盖了 3D 渲染器、区块链、模拟器、神经网络、操作系统和搜索引擎等主题。每个指南都写得很好且步骤清晰，适合中高级程序员。

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**背景**: 该仓库受理查德·费曼名言启发：“我无法创造的东西，我就无法理解。”它符合通过构建来学习的方法，这是掌握复杂系统的有效途径。该项目由 CodeCrafters 维护，该平台提供交互式编程挑战。

**标签**: `#learning`, `#programming`, `#tutorials`, `#open-source`, `#curriculum`

---

<a id="item-12"></a>
## [Kronos：首个开源金融市场基础模型](https://github.com/shiyu-coder/Kronos) ⭐️ 8.0/10

Kronos 是首个针对金融 K 线图的开源基础模型，已在超过 45 个全球交易所的数据上完成训练。该模型已被 AAAI 2026 接收，并提供了在线演示。 Kronos 填补了基础模型在金融时间序列应用上的空白，为价格预测、波动率预测等任务提供了统一模型，有望推动量化金融工具的普及。 Kronos 采用两阶段框架：专用分词器将 OHLCV 数据离散化为分层令牌，然后自回归 Transformer 在其上进行预训练。模型系列包括 Kronos-mini（4M 参数）等变体。

rss · GitHub Trending - Python · Jun 1, 23:22

**背景**: 基础模型是能够适应多种下游任务的大型预训练模型。尽管在自然语言处理和通用时间序列领域取得了成功，但由于金融 K 线数据（包含开盘价、最高价、最低价、收盘价和成交量）噪声高且模式独特，其应用一直受限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2508.02739">Kronos: A Foundation Model for the Language of Financial Markets GitHub - shiyu-coder/Kronos: Kronos: A Foundation Model for ... Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the Language of Financial Markets NeurIPS Kronos: A Foundation Model for the Language of ... Kronos Live Forecast | BTC/USDT</a></li>
<li><a href="https://github.com/shiyu-coder/Kronos">GitHub - shiyu-coder/Kronos: Kronos: A Foundation Model for ...</a></li>
<li><a href="https://ojs.aaai.org/index.php/AAAI/article/download/39730/43691">Kronos: A Foundation Model for the Language of Financial Markets</a></li>

</ul>
</details>

**标签**: `#AI`, `#Finance`, `#Foundation Model`, `#LLM`

---

<a id="item-13"></a>
## [PhyDrawGen：用于物理图的神经符号流水线](https://arxiv.org/abs/2605.30512) ⭐️ 8.0/10

PhyDrawGen 是一种神经符号流水线，通过结合基于大语言模型的场景图提取、确定性约束求解和迭代视觉验证，从自然语言生成物理上准确的图表。 这解决了当前生成模型在力向量幻觉和违反物理定律方面的关键限制，对人工智能/机器学习和物理教育具有潜在影响。 该流水线首先使用大语言模型提取类型化场景图，然后通过确定性求解器将其转换为平面直线图（PSLG），最后使用微调后的 Qwen-VL 模型在提议-验证循环中纠正违规。在涵盖力学、光学和电磁学的 1,449 个问题基准上，它优于 GPT-5-image、Gemini 2.5 Flash 和 Gemini 3 Pro。

rss · arXiv - AI · Jun 1, 04:00

**背景**: 当前的生成模型如 GPT-5 和 Gemini 能生成视觉上合理的图像，但常常违反力平衡和守恒定律等物理约束。神经符号人工智能将神经网络与符号推理相结合以减少幻觉。平面直线图（PSLG）是一种嵌入平面且边为直线的图，在此用于精确编码几何约束。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuro-symbolic_AI">Neuro-symbolic AI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Planar_straight-line_graph">Planar straight - line graph - Wikipedia</a></li>
<li><a href="https://medium.com/@sebuzdugan/how-to-build-a-propose-verify-loop-for-reliable-llm-reasoning-in-production-f85d246fd0c1">How to build a propose - verify loop for reliable LLM... | Medium</a></li>

</ul>
</details>

**标签**: `#AI`, `#diagram generation`, `#physics`, `#neuro-symbolic`, `#NLP`

---

<a id="item-14"></a>
## [面向具身 AI 的查询条件世界模型](https://arxiv.org/abs/2605.30542) ⭐️ 8.0/10

本文主张具身 AI 需要物理可行的世界模型，通过识别最简单的物理抽象来回答干预查询，而不仅仅是预测观察结果。 这项工作揭示了当前观察预测世界模型的一个基本结构缺陷，这些模型可能产生物理上错误的推演并推荐不安全的行为。它为构建可解释、可验证和可审计的世界模型提供了设计原则，对机器人和 AI 安全具有潜在影响。 论文引入了控制基准测试，固定可见场景同时改变潜在物理属性以暴露失败。它提出了一种模块化架构，包含一个自主编排器，为给定的干预查询选择最简单的足够物理抽象。

rss · arXiv - AI · Jun 1, 04:00

**背景**: 具身 AI 中的世界模型是预测动作如何影响未来状态的内部模拟器。当前模型通常预测未来观察（如视频帧），但未能捕捉潜在物理属性，导致视觉上合理但物理上错误的推演。干预查询询问如果采取特定动作会发生什么，需要对环境有因果理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.16732">A Comprehensive Survey on World Models for Embodied AI A Survey of Embodied World Models GitHub - Li-Zn-H/AwesomeWorldModels: A Comprehensive Survey ... Frontiers | A review of embodied intelligence systems: a ... Embodied AI: From LLMs to World Models [Feature] | IEEE ... World Action Models: The Next Frontier in Embodied AI ‘World models’ are AI’s latest sensation: what are they and ...</a></li>
<li><a href="https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf">A Survey of Embodied World Models</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#world models`, `#physics`, `#robotics`, `#AI safety`

---

<a id="item-15"></a>
## [自进化 LLM 代理中的能力解耦：更新与收益](https://arxiv.org/abs/2605.30621) ⭐️ 8.0/10

该论文将自进化 LLM 代理中的两种能力解耦：产生有用更新（harness-updating）和从更新中受益（harness-benefit），并发现更新能力在不同能力层级的模型中出奇地平坦。 这些发现挑战了关于模型能力层级的常见假设，表明投资于任务求解代理而非进化器可能更有效，对设计和评估代理系统具有重要影响。 弱层模型无法激活或遵循工具制品，中层模型受益最大，强层模型受益少于中层；Qwen3.5-9B 的更新产生的收益与 Claude Opus 4.6 相当。

rss · arXiv - AI · Jun 1, 04:00

**背景**: LLM 代理使用外部工具（提示、技能、记忆、工具）来塑造任务执行而不改变模型参数。工具自进化通过从执行证据中更新工具来适应这些代理，但基础能力与进化能力之间的关系尚不清楚。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness - langchain.com</a></li>
<li><a href="https://parallel.ai/articles/what-is-an-agent-harness">What is an agent harness in the context of large-language ...</a></li>
<li><a href="https://harness-engineering.ai/blog/agent-harness-complete-guide/">The Complete Guide to Agent Harness: What It Is and Why It ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#self-evolution`, `#harness`, `#capability analysis`, `#AI research`

---

<a id="item-16"></a>
## [EHRBench：面向 LLM 临床决策的自动化基准](https://arxiv.org/abs/2605.30637) ⭐️ 8.0/10

研究人员推出了 EHRBench，这是一个基于电子健康记录（EHR）的自动化且可靠的基准，用于评估 LLM 在诊断、治疗和预后等临床决策任务上的表现。 EHRBench 填补了评估 LLM 在真实临床决策中表现的关键空白，提供了一个可扩展且可靠的流程，有助于提高医疗 AI 的安全性和可信度。 该基准通过 EHR-LLM-KB 交互流程构建，生成了近 100 万个涵盖三个核心任务的问答条目，并用于评估 30 多个代表性 LLM，揭示了一致的能力趋势和可操作的差距。

rss · arXiv - AI · Jun 1, 04:00

**背景**: 临床决策（CDM）涉及在不完整证据下推断诊断、选择治疗方案或预测结果。LLM 因其语言能力和生物医学知识而被越来越多地用于支持 CDM，但它们在真实任务上的可靠性尚不明确。现有基准往往缺乏自动化、可扩展性或基于真实患者数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30637">[2605.30637] EHRBench : An Automated and Reliable EHR -based...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#clinical decision-making`, `#benchmark`, `#EHR`, `#healthcare AI`

---

<a id="item-17"></a>
## [通过策略即代码搜索实现医疗机制设计](https://arxiv.org/abs/2605.30680) ⭐️ 8.0/10

该论文将医院机制设计重新定义为语言模型的程序合成，使用多智能体模拟器（Medi-Sim）评估战略提供者响应，并合成可检查的规则程序。 这种方法能够根据政策产生的均衡来评估医疗政策，而不是假设提供者行为固定，这可能导致更稳健有效的医疗 AI 和政策设计。 模拟器包含五个战略提供者渠道（编码、选择、延迟、努力、分诊），LLM 引导的进化代码搜索合成一个混合目标程序，消除了编码升级，将拒绝率减半，并保留了大部分以利润为导向的基线资金。

rss · arXiv - AI · Jun 1, 04:00

**背景**: 策略即代码是将组织策略表达为可执行、版本控制的代码，自动执行规则的做法。古德哈特定律指出，当一项指标成为目标时，它就不再是一个好指标。本文将这些概念应用于医疗机制设计，使用大型语言模型的程序合成来生成可检查的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Goodhart's_law">Goodhart ' s law - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2108.07732">[2108.07732] Program Synthesis with Large Language Models</a></li>

</ul>
</details>

**标签**: `#healthcare AI`, `#mechanism design`, `#program synthesis`, `#multi-agent simulation`, `#policy-as-code`

---

<a id="item-18"></a>
## [Unicorn：通用时间序列相关性建模框架](https://arxiv.org/abs/2605.30376) ⭐️ 8.0/10

Unicorn 提出了一种潜在原型码本，将相关性建模与特定通道身份解耦，从而实现了高维时间序列预测的可扩展多数据集预训练。 该方法弥合了通道独立模型与通道依赖模型之间的差距，尤其在少样本迁移场景中取得了最先进性能，为多变量时间序列基础模型铺平了道路。 Unicorn 学习跨不同维度和语义的异构数据集的与身份无关的可重用交互模式，在少样本设置中显著优于现有架构。

rss · arXiv - Machine Learning · Jun 1, 04:00

**背景**: 时间序列预测模型面临一个权衡：通道独立模型扩展性好但忽略通道间依赖，而通道依赖模型能捕捉依赖但难以跨数据集泛化。Unicorn 使用潜在原型码本学习通用相关性模式，从而实现跨领域迁移。

**标签**: `#time series forecasting`, `#deep learning`, `#transfer learning`, `#high-dimensional data`, `#correlation modeling`

---

<a id="item-19"></a>
## [线性探针以近乎完美的准确率检测 LLM 欺骗](https://arxiv.org/abs/2605.30381) ⭐️ 8.0/10

一项多模型研究表明，线性探针可以在五个 transformer 架构的早期层中以近乎完美的 AUC（≥0.99）检测 LLM 中的合成不诚实行为，支持线性表征假说。 这项工作提供了一种稳健、领域不变的方法来检测 LLM 中的欺骗行为，这对于 AI 安全和对齐研究至关重要，尤其是在高风险应用中监控模型时。 逻辑回归探针始终匹配或优于 MLP 探针，且在 TruthfulQA 上训练的探针以近乎零损失泛化到未见的 MMLU 科目。后期层表示对高斯噪声表现出强鲁棒性，其中 Gemma-2 模型展现出卓越的稳定性。

rss · arXiv - Machine Learning · Jun 1, 04:00

**背景**: 线性表征假说认为，高级概念在模型的表征空间中线性地表示为方向。合成不诚实是通过对错误答案进行直接优化来诱导的，为研究习得的欺骗行为提供了一个受控的测试平台。LoRA（低秩适应）是一种参数高效的微调方法，通过引入小型可训练矩阵，允许高效地适应大型模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30381">[2605.30381] When LLMs Learn to Be Consistently Wrong: A ...</a></li>
<li><a href="https://arxiv.org/abs/2311.03658">[2311.03658] The Linear Representation Hypothesis and the ...</a></li>
<li><a href="https://github.com/vzm1399/llm-dishonesty-representations/blob/main/README.md">llm-dishonesty-representations/README.md at main - GitHub</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#deceptive alignment`, `#LLM interpretability`, `#probing`, `#representation learning`

---

<a id="item-20"></a>
## [NumLeak 揭示 LLM 记忆公开数值基准](https://arxiv.org/abs/2605.30393) ⭐️ 8.0/10

NumLeak 这一新测量框架表明，GPT-4 和 Claude 等顶级 LLM 以近乎完美的相关性（r=0.97-0.99）记忆了 Fama-French 市场超额收益等公开数值基准，削弱了样本外评估的有效性。 这项研究暴露了 LLM 评估方法中的一个关键缺陷：许多被认为衡量推理或技能的基准实际上可能是在衡量记忆，这可能导致模型能力被高估，并误导 AI 安全评估。 该框架结合了对生产模型的 API 边界探测和在开放因果 LM 上的白盒验证，并表明一行系统提示防御能以接近零的效用成本阻止 99.8%的非自适应后缀攻击。

rss · arXiv - Machine Learning · Jun 1, 04:00

**背景**: 基准污染是指评估数据出现在模型的训练集中，使得难以判断模型是在回忆记忆中的答案还是展示真正的技能。Fama-French 因子是广泛使用的金融模型，通过市场、规模和价值因子来解释股票收益。NumLeak 专门测试 LLM 是否从这些及其他公开数据集中回忆出精确的历史数值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30393">[2605.30393] NumLeak: Public Numeric Benchmarks as Latent ...</a></li>
<li><a href="https://github.com/akotawala10/NumLeak_ICML2026">akotawala10/NumLeak_ICML2026 - GitHub</a></li>

</ul>
</details>

**标签**: `#LLM`, `#memorization`, `#benchmark contamination`, `#evaluation`, `#AI safety`

---

<a id="item-21"></a>
## [LongDS 基准揭示 AI 智能体在长时数据分析中的失败](https://arxiv.org/abs/2605.30434) ⭐️ 8.0/10

研究人员推出了 LongDS-Bench，这是一个包含 68 个来自真实 Kaggle 笔记本的任务、共 2225 轮、覆盖六个领域的基准测试，用于评估 AI 智能体在长时多轮数据分析中的表现。最佳模型仅达到 48.45%的准确率，从早期到后期轮次性能下降了近 47 个百分点。 该基准测试揭示了当前 AI 智能体的一个关键缺陷：它们在长时间交互中难以维持和组合分析状态，而这对于现实世界中的迭代数据分析至关重要。研究结果表明，改进状态追踪而非增加交互步骤是推进智能体推理的关键。 任务围绕状态演化模式设计，如反事实扰动、回滚和多状态组合，平均依赖跨度为 11.3 轮。长时错误占失败的 52%–69%，且增加智能体步骤并不一定能提升性能。

rss · arXiv - Machine Learning · Jun 1, 04:00

**背景**: 现实世界的数据分析通常是迭代的，要求智能体在多个步骤中跟踪不断变化的上下文。现有基准测试大多评估孤立或短期的交互任务，未能测试长时推理。LongDS 通过关注在多轮中维持和组合分析状态来填补这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/longbench-v2">LongBench v2 Benchmark Leaderboard</a></li>
<li><a href="https://arxiv.org/html/2601.02872v1">LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#data analysis`, `#AI agents`, `#long-horizon reasoning`, `#evaluation`

---

<a id="item-22"></a>
## [校准偏好学习：标签排序框架](https://arxiv.org/abs/2605.30447) ⭐️ 8.0/10

该论文为概率标签排序中的校准问题提供了形式化定义，引入了一个包含全排序、子排序和 top-k 校准的层次结构，并证明了它们之间的关系。实验表明，包括 RLHF 奖励模型在内的流行标签排序模型通常校准不佳。 这项工作将校准研究扩展到标签排序领域，填补了相关空白，对偏好学习中的可靠决策至关重要。其发现对于提高用于对齐大语言模型的 RLHF 奖励模型的可信度具有直接意义。 论文证明全排序校准蕴含子排序和 top-k 校准，但反之不成立，且子排序与 top-k 校准不可比较。实验表明，在 RLHF 奖励模型中，校准与基准准确率强相关但不完全一致，说明校准捕捉了一个独立的质量维度。

rss · arXiv - Machine Learning · Jun 1, 04:00

**背景**: 校准衡量预测概率与实际结果的匹配程度，在分类和回归中已有深入研究。概率标签排序（ProLR）对标签所有可能排序的分布进行建模，其结构比多类分类更复杂。RLHF 奖励模型为响应分配分数以对齐大语言模型与人类偏好，其校准对于可靠训练至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30447">Calibrated Preference Learning: The Case of Label Ranking</a></li>
<li><a href="https://arxiv.org/abs/2410.09724">Taming Overconfidence in LLMs: Reward Calibration in RLHF Images TAMING OVERCONFIDENCE IN LLMS: REWARD CALIBRATION IN RLHF Reward Calibration for Continual Reinforcement Learning from ... Calibration of Reward Models - apxml.com Reward models: 8 calibration steps that reduce overconfidence Taming Overconfidence in LLMs: Reward Calibration in RLHF GitHub - SeanLeng1/Reward-Calibration</a></li>

</ul>
</details>

**标签**: `#calibration`, `#label ranking`, `#RLHF`, `#machine learning`, `#probability`

---

<a id="item-23"></a>
## [自主智能体数据工程将 LLM 专业化提升 57%](https://arxiv.org/abs/2605.30407) ⭐️ 8.0/10

研究人员提出了自主智能体数据工程，让 LLM 自主规划、生成并迭代优化训练数据以实现模型专业化，使用 GPT-5.2 在学生模型上取得了 57.29%的性能提升。 这项工作表明 LLM 可以自主驱动模型专业化的整个数据工程流程，有望减少人工投入，实现更高效的专业领域适配。 论文形式化了一个名为“自主智能体数据工程”的新任务，并表明迭代式智能体驱动数据适配能带来显著收益。代码将在 GitHub 上发布。

rss · arXiv - NLP · Jun 1, 04:00

**背景**: 大型语言模型（LLM）因缺乏高质量领域数据而常在专业领域表现不佳。传统数据整理方法依赖人工设计的工作流，而这项工作探索了由 LLM 智能体完全自主进行数据工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30407">Exploring Autonomous Agentic Data Engineering for Model ...</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-ai-data-engineering-autonomous-pipeline-ashutosh-sharma-jxwrc">Agentic AI in Data Engineering: The Autonomous Data Pipeline ...</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/three-step-design-pattern-for-specializing-llms/">A three-step design pattern for specializing LLMs | Google ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#data engineering`, `#model specialization`, `#autonomous agents`, `#AI`

---

<a id="item-24"></a>
## [跨语言引导的比喻语言生成](https://arxiv.org/abs/2605.30443) ⭐️ 8.0/10

研究人员证明，在一种语言中学习到的比喻语言激活引导方向可以迁移到其他语言，有时甚至达到或超越目标语言的原生方向。 这一发现为比喻生成中可复用的跨语言信号提供了直接证据，可能实现更高效的多语言大模型控制，并提升可解释性。 该研究测试了五种比喻类别、六种语言和四种多语言大模型，发现德语是跨语言迁移中最易接受的目标语言之一。

rss · arXiv - NLP · Jun 1, 04:00

**背景**: 激活引导是一种推理时方法，通过修改模型的内部表示来引导其行为。比喻语言生成（FLG）涉及将文本改写以包含比喻或明喻等修辞手法。该工作探究比喻语言的内部信号是语言特有的还是可跨语言复用的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sidn.baulab.info/steering/">The Development of Activation Steering - sidn.baulab.info</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3654795">A Survey on Automatic Generation of Figurative Language : From...</a></li>

</ul>
</details>

**标签**: `#multilingual LLMs`, `#figurative language`, `#activation steering`, `#NLP`, `#interpretability`

---

<a id="item-25"></a>
## [多模态语音模型的首个偏见研究](https://arxiv.org/abs/2605.30472) ⭐️ 8.0/10

研究人员首次对多模态语音识别模型进行了偏见评估，发现将不同面孔与相同音频配对会导致转录准确率下降，跨性别和族裔的 WER 最高增加 4.05 个百分点。 这表明添加视觉模态可能引入人口统计偏见，与“更多数据总能提升公平性”的假设相悖，并凸显了多模态 AI 系统中进行偏见评估的必要性。 该研究评估了 mWhisper-Flamingo 和 Gemini 模型，测量了将不同自我宣称性别和族裔的面孔与相同音频片段配对时词错误率（WER）的变化。

rss · arXiv - NLP · Jun 1, 04:00

**背景**: 多模态语音识别结合音频与视觉线索（如唇部运动）以提高嘈杂环境下的准确性。词错误率（WER）衡量转录错误的单词百分比。先前的偏见研究集中于单模态系统，多模态模型尚未被检验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.01547v1">mWhisper- Flamingo for Multilingual Audio-Visual Noise-Robust...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Word_error_rate">Word error rate - Wikipedia</a></li>

</ul>
</details>

**标签**: `#bias`, `#multimodal`, `#speech recognition`, `#fairness`, `#AI ethics`

---

<a id="item-26"></a>
## [英文提问导致大语言模型中的全球叙事主导](https://arxiv.org/abs/2605.30481) ⭐️ 8.0/10

一篇新论文引入了包含 717 个孟加拉文化实例的数据集 CulturalNB，并评估了九个大语言模型，发现用英文提问会系统性地增加全球叙事主导并减少本地视角覆盖。 这项研究揭示了作为跨语言知识接口的大语言模型的一个关键缺陷：它们以牺牲本地文化知识为代价传播全球主导叙事，可能导致 AI 系统中的文化抹除和偏见。 该研究使用了仅问题提示和基于证据的提示，结合人类和 LLM 评判者，测量了跨语言一致性、语言锚定、全球替代、制度偏见和认知视角覆盖。

rss · arXiv - NLP · Jun 1, 04:00

**背景**: 大语言模型（LLMs）越来越多地被用作跨语言知识接口，但它们往往反映全球主导叙事而非本地文化背景。本文聚焦于低资源语言孟加拉语，研究这一被称为“全球叙事主导”的现象。CulturalNB 数据集提供了平行的孟加拉语-英语问答对及社会文化注释，以便进行系统评估。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.22749">Representational Harms in LLM-Generated Narratives Against ...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3774904.3793008">From Words to Worlds: Measuring Cultural Narrative Bias in ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#cross-lingual`, `#cultural bias`, `#NLP`, `#dataset`

---

<a id="item-27"></a>
## [可配置奖励模型实现平衡安全对齐](https://arxiv.org/abs/2605.30487) ⭐️ 8.0/10

研究人员提出了可配置安全奖励模型（CSRM），该模型能适应不同的安全规范，并在 CoSApien（F1 94.6%）和 DynaBench（F1 75.8%）等可配置安全基准上取得了最先进性能，且无需额外人工标注。 这项工作通过使大语言模型灵活遵守异构且不断变化的安全要求，改善了有用性与安全性的权衡，解决了 AI 安全中的关键挑战。它为在不同安全标准的多样化实际场景中部署大语言模型提供了实用方案。 CSRM 联合优化了校准的安全合规性和奖励建模，采用面向配置的数据增强，在保持相对严重性结构的同时强制遵循指令。它对未见过的安全配置具有很强的泛化能力。

rss · arXiv - NLP · Jun 1, 04:00

**背景**: 大语言模型通常通过指令微调或奖励模型来对齐安全要求，但这些方法难以泛化到新的或多样化的安全配置。CoSApien 和 DynaBench 等可配置安全基准评估模型遵循不同安全策略的能力。CSRM 建立在先前可控安全对齐工作的基础上，例如微软的 CoSAlign 模型和数据集。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.30487v1">Configurable Reward Model for Balanced Safety Alignment</a></li>
<li><a href="https://huggingface.co/datasets/microsoft/CoSApien/blob/main/README.md">README.md · microsoft/CoSApien at main - Hugging Face</a></li>
<li><a href="https://github.com/microsoft/controllable-safety-alignment">Controllable Safety Alignment - GitHub</a></li>

</ul>
</details>

**标签**: `#LLM alignment`, `#reward model`, `#AI safety`, `#configurable safety`

---

<a id="item-28"></a>
## [SANA-Streaming：在消费级 GPU 上实现实时视频编辑](https://arxiv.org/abs/2605.30409) ⭐️ 8.0/10

SANA-Streaming 提出了一种混合扩散 Transformer 与系统协同设计，在单张 RTX 5090 GPU 上实现了 1280x704 分辨率、24 FPS 的实时视频到视频编辑。 该工作使得在消费级硬件上实现实时、高分辨率的流式视频编辑成为可能，这对直播和游戏等交互式应用至关重要，并且在时间一致性和吞吐量上显著优于现有最先进方法。 该框架结合了混合扩散 Transformer（部分块使用 softmax 注意力以增强局部建模）、循环反向正则化训练策略（无需成对长视频即可实现时间一致性），以及针对 NVIDIA Blackwell 架构优化的融合 GDN 内核与混合精度量化的系统协同设计。

rss · arXiv - Computer Vision · Jun 1, 04:00

**背景**: 视频到视频编辑需要在帧间保持时间一致性，同时为实时应用实现高吞吐量。扩散 Transformer 虽有潜力，但受限于二次注意力复杂度，使得实时高分辨率编辑具有挑战性。结合 softmax 和线性注意力的混合注意力机制旨在平衡质量与效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30409">SANA-Streaming: Real-time Streaming Video Editing with Hybrid...</a></li>

</ul>
</details>

**标签**: `#video editing`, `#diffusion transformer`, `#real-time`, `#system co-design`, `#AI/ML`

---

<a id="item-29"></a>
## [Dex2HOI：统一扩散模型实现双手双物体交互生成](https://arxiv.org/abs/2605.30444) ⭐️ 8.0/10

Dex2HOI 提出了一种统一的扩散模型，能够根据文本描述生成灵巧的双手与两个物体的交互，采用双流扩散方法和运动融合网络。 这项工作解决了双手双物体交互生成这一尚未充分探索的问题，超越了单物体 HOI 合成，为机器人、动画和 VR 应用提供了更逼真的人体运动。 该模型通过在前缀条件窗口上自回归采样，消除了测试时优化，推理速度相比先前方法提升高达 540 倍。它还引入了手相对物体表示和接触感知条件。

rss · arXiv - Computer Vision · Jun 1, 04:00

**背景**: 人-物交互（HOI）生成旨在合成与物体交互的逼真人体运动。先前的工作主要关注单物体场景，但真实的人类行为通常涉及双手同时操作多个物体。扩散模型因其能够建模复杂分布而成为运动生成的主流方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.27607">Dual-Stream Diffusion for World-Model Augmented Vision ... Dual-Stream Diffusion for World-Model Augmented Vision ... DiffuFuse: Diffusion-Driven Dual-Stream Fusion Framework for ... Dual-Stream Diffusion for World-Model Augmented Vision ... Dual-Stream Diffusion for World-Model Augmented Vision ... MMFace-DiT: Dual-Stream Diffusion Transformer DiffuFuse:Diffusion-Driven Dual-Stream Fusion Framework for ...</a></li>
<li><a href="https://arxiv.org/abs/2409.16855">[2409.16855] A Versatile and Differentiable Hand-Object ... Images A Versatile and Differentiable Hand-Object Interaction ... A Versatile and Differentiable Hand-Object Interaction ... Symbolic representation of objects relative poses for robotic ... GitHub Pages - HandyPriors The real-time hand and object recognition for virtual ... A Versatile and Differentiable Hand-Object Interaction ...</a></li>

</ul>
</details>

**标签**: `#human-object interaction`, `#diffusion models`, `#motion generation`, `#bimanual manipulation`, `#4D synthesis`

---

<a id="item-30"></a>
## [VLM 在空间问题上不知何时不应回答](https://arxiv.org/abs/2605.30557) ⭐️ 8.0/10

研究人员提出了 SpatialUncertain 框架，用于评估视觉语言模型（VLM）是否能识别因遮挡或视角模糊而无法回答的空间问题，而不仅仅是生成正确答案。 这项工作挑战了现有空间推理基准中“观察总是充分”的假设，揭示了 VLM 常常过度自信地回答无法回答的问题，这对安全部署至关重要。 在遮挡条件下，平均准确率降至约 30%，在视角模糊条件下低于 10%。即使提供了额外视角，一些模型在识别哪个视角提供可靠证据时表现接近随机水平。

rss · arXiv - Computer Vision · Jun 1, 04:00

**背景**: 视觉语言模型（VLM）结合视觉和文本理解来回答关于图像的问题。空间推理基准通常测试模型能否回答关于物体位置或关系的问题，但假设图像包含所有必要信息。实际上，遮挡和视角可能使某些问题无法回答，模型应放弃回答而非猜测。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.30557">Seeing Isn’t Knowing: Do VLMs Know When Not to Answer Spatial ...</a></li>
<li><a href="https://arxiv.org/abs/2401.12168">SpatialVLM: Endowing Vision-Language Models with Spatial ...</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#spatial reasoning`, `#benchmark`, `#AI safety`, `#computer vision`

---

<a id="item-31"></a>
## [从 Best-of-N 偏好数据中学习奖励函数的理论分析](https://arxiv.org/abs/2605.30619) ⭐️ 8.0/10

本文对从 Best-of-N 偏好数据中学习 Bradley-Terry 奖励函数进行了理论分析，为独立参考变体推导出闭式奖励目标，并表明像 Best-vs-Random 和 Best-vs-Worst 这样的耦合变体仅在 N 增大时逼近这些目标。 这项工作阐明了 RLHF 中广泛使用但理解不足的数据收集方法的理论基础，为选择 N 和基础分布提供了设计原则，可提高奖励模型训练效率和对齐质量。 分析揭示了边际与连通性之间的权衡：较大的 N 会扩大成对边际但降低连通性，从而影响样本效率。论文建议在偏好标签成为瓶颈时使用较大的 N，在生成成为瓶颈时使用较小的 N。

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**背景**: Best-of-N 采样是一种推理时对齐技术，从基础模型生成 N 个候选回复，并选择奖励分数最高的一个。Bradley-Terry 模型是从成对偏好数据中学习奖励函数的常用方法，但其在 Best-of-N 采样下的行为在理论上尚未被充分理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.03156">[2505.03156] Soft Best-of-n Sampling for Model Alignment Best-of-N Sampling: AI Inference-Time Alignment | Inference ... Best-of-N sampling — Grokipedia Regularized Best-of-N Sampling with Minimum Bayes Risk ... Best of N sampling: Alternative ways to get better model ... Soft Best-of-$n$ Sampling for Model Alignment - IEEE Xplore GitHub - saschaschramm/best-of-n-sampling: Toy example for ...</a></li>
<li><a href="https://inferensys.com/glossary/agentic-cognitive-architectures/reinforcement-learning-from-ai-feedback/best-of-n-sampling">Best-of-N Sampling: AI Inference-Time Alignment | Inference ...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning from human feedback`, `#reward learning`, `#preference data`, `#Bradley-Terry model`, `#Best-of-N sampling`

---

<a id="item-32"></a>
## [最后一层线性化在不确定性量化上媲美全网络](https://arxiv.org/abs/2605.30741) ⭐️ 8.0/10

一篇新论文（arXiv:2605.30741）从理论和实验上证明，深度神经网络中用于认知不确定性量化的最后一层线性化与全网络线性化性能相当，但计算效率显著更高。 这一发现挑战了“全网络线性化是高质量不确定性量化所必需”的普遍观点，而不确定性量化对于关键任务中 AI 的安全部署至关重要。这使得从业者能够使用更便宜的最后一层近似方法，而无需牺牲 UQ 质量。 理论分析使用随机矩阵理论比较了两种线性化方法的预测后验分布，发现全网络线性化没有带来有意义的改进。跨现代机器学习任务的大规模实验证实了这种等价性。

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**背景**: 认知不确定性量化（UQ）衡量模型因数据有限而不知道的内容，这对 AI 安全至关重要。贝叶斯广义线性模型（GLM）通过线性化神经网络来近似后验分布，但全网络线性化计算成本高昂。最后一层线性化是一种更便宜的近似方法，通常被认为会降低 UQ 性能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/epistemic-uncertainty-quantification">Epistemic Uncertainty Quantification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_linear_regression">Bayesian linear regression - Wikipedia</a></li>

</ul>
</details>

**标签**: `#uncertainty quantification`, `#deep learning`, `#Bayesian neural networks`, `#random matrix theory`, `#epistemic uncertainty`

---

<a id="item-33"></a>
## [弱单调性提升少样本学习](https://arxiv.org/abs/2605.30997) ⭐️ 8.0/10

一篇新论文提出利用跨基准的弱单调性来改进少样本学习，并提供了理论保证和实用的对冲算法。 这项工作提供了一种原则性方法，利用公开基准评估来处理样本稀少的新任务，有望改进 AI/ML 研究中的迁移学习和模型选择。 论文在迁移学习和模型选择聚合两种范式下探索了弱单调性，并表明在前沿上进行对冲可以适应权衡的几何结构。

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**背景**: 少样本学习旨在仅从少量标注样本中学习新任务。弱单调性是指如果一个模型在许多基准上优于另一个模型，那么它在新任务上也往往表现更好。本文利用这一特性来修剪模型类别并改进学习。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/cracking-the-code-task-relatedness-in-few-shot-learning-qju8">Cracking the Code: Task Relatedness in Few-Shot Learning</a></li>
<li><a href="https://arxiv.org/html/2305.00799">How to Address Monotonicity for Model Risk Management?</a></li>
<li><a href="https://arxiv.org/abs/2205.06743">[2205.06743] A Comprehensive Survey of Few-shot Learning ...</a></li>

</ul>
</details>

**标签**: `#few-shot learning`, `#transfer learning`, `#model selection`, `#statistical learning theory`

---

<a id="item-34"></a>
## [贝叶斯滤波统一次二次序列模型](https://arxiv.org/abs/2605.31163) ⭐️ 8.0/10

一篇新论文提出了设计-模型框架，从贝叶斯滤波假设中推导出高效的循环序列映射，将线性注意力、GLA、Mamba-2 和 DeltaNet 统一在一个概率记忆模型下。 该框架为高效序列模型提供了原则性设计原理，可能指导开发更鲁棒、更可解释的次二次架构，用于长上下文任务。 贝叶斯层同时传播均值和协方差，跟踪存储关联的不确定性，并将写入导向不确定方向。将贝叶斯层蒸馏到预训练的 340M Gated DeltaNet 中，在相同计算量下提升了 RULER 长上下文检索性能。

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**背景**: 许多现代序列模型（如线性注意力和 Mamba-2）通过使用循环公式实现次二次复杂度，但通常缺乏统一的理论基础。贝叶斯滤波是一种递归估计技术，随着新观测到达而更新对隐藏状态的信念。本文通过展示几种流行架构在特定设计模型下是精确的贝叶斯滤波器，弥合了这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.22791">[2605.22791] Gated DeltaNet-2: Decoupling Erase and Write in ...</a></li>
<li><a href="https://sustcsonglin.github.io/blog/2024/deltanet-3/">DeltaNet Explained (Part III) | Songlin Yang</a></li>

</ul>
</details>

**标签**: `#machine learning`, `#recurrent neural networks`, `#Bayesian filtering`, `#sequence modeling`, `#attention`

---

<a id="item-35"></a>
## [任意有效推断修复在线决策树的分裂选择](https://arxiv.org/abs/2605.31239) ⭐️ 8.0/10

本文提出了一种基于任意有效推断的方法，用于纠正在线决策树中的分裂选择，在任意数据流下提供有效的统计保证和有限承诺时间。 这解决了广泛使用的 Hoeffding 树中的一个根本缺陷，即由于数据依赖的停止规则，固定样本集中界会失效。新方法提高了性能并生成更小的树，有利于数据流学习应用。 该方法在非平稳流下提供对错误分裂的任意有效控制，在预测优势下提供有限承诺时间，并在平稳独立同分布数据下风险严格递减。在非平稳流上的实证评估显示，性能提升且树规模显著减小。

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**背景**: 在线决策树（如 Hoeffding 树）通过使用集中不等式测试分裂来增量生长。然而，这些测试依赖固定样本界，而决策基于数据依赖的停止规则，导致统计保证失效。任意有效推断提供了有效的序贯检验，能在所有停止时间控制错误率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/any-time-inference">Any - Time Inference</a></li>
<li><a href="https://medium.com/@techynilesh/the-hoeffding-tree-classifier-for-real-time-data-mining-09b117486a95">The Hoeffding Tree Classifier for Real-Time Data Mining | Medium</a></li>
<li><a href="https://www.activeloop.ai/resources/glossary/hoeffding-trees/">What is Hoeffding Trees ? | Activeloop Glossary</a></li>

</ul>
</details>

**标签**: `#online learning`, `#decision trees`, `#anytime-valid inference`, `#data streams`, `#statistical guarantees`

---