---
layout: default
title: "Horizon Summary: 2026-09-02 (ZH)"
date: 2026-09-02
lang: zh
---

> From 108 items, 30 important content pieces were selected

---

1. [Meta 发布 Muse Spark 1.3，改进代码与 SVG 生成能力](#item-1) ⭐️ 8.0/10
2. [谷歌发布 Gemini 3.8 Flash 及网络模型](#item-2) ⭐️ 8.0/10
3. [AI 生成的“最佳软件”页面污染 Perplexity 引用](#item-3) ⭐️ 8.0/10
4. [全球最大暗物质探测器记录到单个异常事件](#item-4) ⭐️ 8.0/10
5. [Paint.NET 借助 AI 从头重写 Direct2D 以支持 WINE](#item-5) ⭐️ 8.0/10
6. [MiniMind：两小时从零训练 64M 参数大语言模型](#item-6) ⭐️ 8.0/10
7. [Manim：3Blue1Brown 的数学视频动画引擎](#item-7) ⭐️ 8.0/10
8. [Crawl4AI：开源、面向 LLM 的网络爬虫备受关注](#item-8) ⭐️ 8.0/10
9. [Anthropic 推出 Claude Code：终端智能编程工具](#item-9) ⭐️ 8.0/10
10. [通过逐步执行 MD5 测试 LLM 的长程状态跟踪能力](#item-10) ⭐️ 8.0/10
11. [SCAFFOLD：用于计算机科学图表问答与思维链推理的大规模数据集](#item-11) ⭐️ 8.0/10
12. [UI-Venus-2：扩展环境、任务与验证，推动 GUI 智能体走向真实应用](#item-12) ⭐️ 8.0/10
13. [EULER：用于跨领域数学发现的多智能体系统](#item-13) ⭐️ 8.0/10
14. [ReNFT 通过内部概率质量重校准修复扩散模型后训练中的模式坍缩](#item-14) ⭐️ 8.0/10
15. [注意力敏感性不足以保持上下文学习能力](#item-15) ⭐️ 8.0/10
16. [仅看结果的 LLM 评测会漏掉智能体的隐性错误](#item-16) ⭐️ 8.0/10
17. [电路引导的权重缩放提升 LLM 安全拒绝能力](#item-17) ⭐️ 8.0/10
18. [LLM 增强对齐实现零样本呼吸音分类](#item-18) ⭐️ 8.0/10
19. [RePro：基于证明验证的基准重写，实现可靠的 LLM 数学评估](#item-19) ⭐️ 8.0/10
20. [Qwen-Drive-1.0：面向自动驾驶的统一视觉语言模型](#item-20) ⭐️ 8.0/10
21. [ZimaBlue：通过可扩展视频预训练实现泛化的世界动作模型](#item-21) ⭐️ 8.0/10
22. [流匹配的拉格朗日推导产生直线轨迹](#item-22) ⭐️ 8.0/10
23. [分布式隐式危害：MLLM 视频审核中的组合性安全盲点](#item-23) ⭐️ 8.0/10
24. [超越语言先验：诊断并修复多模态大模型中的视觉来源幻觉](#item-24) ⭐️ 8.0/10
25. [VeriOCRBench：OCR 推理中任务验证的基准测试](#item-25) ⭐️ 8.0/10
26. [CoLT-Drive：用于驾驶可供性预测的反事实长尾基准与知识保持适应框架](#item-26) ⭐️ 8.0/10
27. [StreamScout：面向流式视频问答的自适应推理框架](#item-27) ⭐️ 8.0/10
28. [Fed-LSVI：首个具有对数通信成本的可证明高效联邦强化学习算法](#item-28) ⭐️ 8.0/10
29. [去噪扩散蒙特卡洛实现精确全局 MCMC 采样](#item-29) ⭐️ 8.0/10
30. [有效学习率坍缩统一大语言模型预训练中的损失动态](#item-30) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Meta 发布 Muse Spark 1.3，改进代码与 SVG 生成能力](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 发布了 Muse Spark 1.3，这是一款升级版 AI 模型，用于代码和 SVG 生成，具有更好的输出质量和有竞争力的定价。该模型针对代理工作流进行了训练，并针对竞争性编码性能进行了优化，具有更高的首次尝试准确率和可靠的工具调用能力。 此次更新意义重大，因为它展示了 Meta 在开发高性能且成本效益高的 AI 模型方面的持续投入，可能降低开发者的使用门槛。代码生成和 SVG 动画质量的改进可能使 Muse Spark 成为其他模型更具竞争力的替代品，加剧 AI 模型市场的竞争。 Muse Spark 1.3 包含“最大推理”模式，用于处理具有挑战性的推理和代理任务，并专为长时间运行的代理、多代理和编码工作流而设计。社区测试表明，它在 SVG 生成方面优于之前的版本，其中一个示例花费 4.2266 美分，耗时 38 秒，并且其 DeepSWE 得分为 75.4，是迄今为止最好的。

hackernews · bvaldivielso · Sep 2, 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: Muse Spark 是 Meta 推出的一系列 AI 模型，专为代码生成和其他开发任务而设计。SVG（可缩放矢量图形）是一种广泛使用的矢量图像格式，能够根据文本提示生成 SVG 的 AI 模型对设计师和开发人员非常有价值。该模型可通过 Meta 的开发者平台获取，并可通过各种工具和 API 访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.meta.com/ai/models/muse-spark/">Muse Spark 1.3 | Meta</a></li>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://benchable.ai/models/meta/muse-spark-1.3-20260902">Meta: Muse Spark 1.3 - AI Model Details & Benchmarks</a></li>

</ul>
</details>

**社区讨论**: 社区成员正在积极测试 Muse Spark 1.3，一位用户指出它在 SVG 生成方面比 1.2 版本更好，例如更准确的车架和鹈鹕帽子。另一位用户强调其低成本和对非前沿任务的良好性能，而其他人则讨论与 Claude Code 和 OpenRouter 等工具的集成。此外，人们对其最高的 DeepSWE 得分以及竞争可能推动价格下降感到兴奋。

**标签**: `#Meta`, `#AI model`, `#code generation`, `#SVG`, `#Muse Spark`

---

<a id="item-2"></a>
## [谷歌发布 Gemini 3.8 Flash 及网络模型](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/) ⭐️ 8.0/10

谷歌发布了 Gemini 3.8 Flash 和 Gemini 3.8 Flash Cyber，后者是其最强大的网络安全模型，用于漏洞检测和自动修补。Flash 模型速度快且成本低，在基准测试中表现强劲，尤其在 HTML 和 JavaScript 生成方面。 此次发布标志着谷歌在 AI 模型竞赛中的激进步伐，六周内推出第三款 Flash 模型，为开发者和企业提供了高性价比的选择。Cyber 版本满足了日益增长的 AI 驱动安全需求，可能重塑漏洞修补的方式。 Gemini 3.8 Flash 在 Artificial Analysis 上获得 59 分的智能评分，与 Opus 5 medium 持平，并在 BenchLM 的编程类别中排名第 36。Cyber 模型通过谷歌新的 Fairwind 计划向受信任的防御者提供，Flash 模型支持包括音频和视频在内的多模态输入。

hackernews · bratao · Sep 2, 15:12 · [社区讨论](https://news.ycombinator.com/item?id=49537553)

**背景**: Gemini Flash 模型专为低延迟、高性价比的应用设计，常用于智能体工作流和媒体分析。谷歌的快速迭代旨在与 OpenAI 和 Anthropic 竞争，后者的旗舰模型仍仅支持图像，而 Gemini 的多模态支持提供了明显优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/">Introducing Gemini 3.8 Flash and 3.8 Flash Cyber</a></li>
<li><a href="https://deepmind.google/models/model-cards/gemini-3-8-flash/">Gemini 3 . 8 Flash - Model Card — Google DeepMind</a></li>
<li><a href="https://arstechnica.com/ai/2026/09/google-releases-gemini-3-8-flash-its-third-flash-model-in-six-weeks/">Google releases Gemini 3.8 Flash, its third Flash model in six weeks - Ars Technica</a></li>

</ul>
</details>

**社区讨论**: 社区成员对该模型的速度和成本印象深刻，Simon Willison 演示了 13 秒内生成 HTML 仅需 1.8 美分。其他人注意到其强劲的基准性能，但也有人提醒实际使用体验尚待观察，还有用户报告低思考努力级别相比 3.7 有所回退。

**标签**: `#AI`, `#Google`, `#Gemini`, `#model release`, `#benchmarks`

---

<a id="item-3"></a>
## [AI 生成的“最佳软件”页面污染 Perplexity 引用](https://trellner.com/reports/manufactured-sources-behind-ai-recommendations/) ⭐️ 8.0/10

Trellner 的一份报告揭示，三个网站生成了 215,128 个由 AI 编写的“最佳软件”页面，这些页面现在被 Perplexity 等 AI 搜索工具引用。这凸显了合成内容污染 AI 推荐这一日益严重的问题。 这很重要，因为它形成了一个反馈循环：AI 生成的低质量内容被 AI 工具用作来源，从而降低了 AI 辅助研究和推荐的可靠性。它影响了依赖 AI 搜索引擎获取准确信息的用户，并强调了在 AI 系统中改进来源过滤和保持怀疑态度的必要性。 该报告特别指出了三个网站，它们生成了这些页面的大部分，可能结合了程序化 SEO 技术和 AI 生成。这些页面旨在针对“最佳软件”查询进行排名，然后被 AI 工具引用，这暴露了当前 AI 引用实践中的一个漏洞。

hackernews · jakobgreenfeld · Sep 2, 13:59 · [社区讨论](https://news.ycombinator.com/item?id=49536375)

**背景**: 程序化 SEO 是一种技术，网站通过模板和数据自动生成大量针对特定关键词的页面。随着生成式 AI 的出现，内容农场现在可以以最少的人力大规模生产这些页面，导致低质量 AI 生成内容的激增。像 Perplexity 这样的 AI 搜索引擎使用检索和排序算法来选择来源，但它们可能无法充分过滤此类合成内容，从而导致引用不可靠的页面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.semrush.com/blog/programmatic-seo/">What Is Programmatic SEO? Examples + How to Do It - Semrush</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_farm">Content farm - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/2023/06/26/1075504/junk-websites-filled-with-ai-generated-text-are-pulling-in-money-from-programmatic-ads/">Next-gen content farms are using AI-generated text to spin up junk websites | MIT Technology Review</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了关于 AI 工具偏爱 AI 生成内容的个人轶事，例如 Claude 偏好自己生成的代码片段，以及 LLM 推荐不存在的地点。他们还指出，AI 模型缺乏对来源的怀疑精神，经常引用被比较公司托管的比较页面，并预测这种利用窗口最终会关闭。

**标签**: `#AI`, `#SEO`, `#content generation`, `#search`, `#misinformation`

---

<a id="item-4"></a>
## [全球最大暗物质探测器记录到单个异常事件](https://www.science.org/content/article/world-s-biggest-dark-matter-detector-spots-single-weird-particle) ⭐️ 8.0/10

全球最大的暗物质探测器 LUX-ZEPLIN（LZ）记录到一个单个异常粒子事件。研究人员已发布预印本详细分析，但警告称现在断言发现还为时过早。 这一事件可能成为暗物质的首次直接探测，暗物质是困扰物理学家数十年的谜团。如果得到确认，将彻底改变我们对宇宙的理解，但历史上 3 西格玛信号随更多数据消失的先例提醒我们需保持谨慎。 LZ 探测器使用 7 吨活性液氙来寻找弱相互作用大质量粒子（WIMP）与氙核的散射。该事件是在 2.84 吨·年的曝光量中记录到的，团队正在收集更多数据以确定其性质。

hackernews · randycupertino · Sep 2, 13:40 · [社区讨论](https://news.ycombinator.com/item?id=49536079)

**背景**: 暗物质是一种不可见的物质形式，约占宇宙的 27%，通过引力效应推断存在，但尚未被直接探测到。像 LZ 这样的直接探测实验旨在观察暗物质粒子与普通物质之间的罕见相互作用，通常使用大量惰性液体如氙。LZ 探测器位于南达科他州桑福德地下研究设施地下 1480 米处，以屏蔽宇宙射线。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LZ_experiment">LZ experiment - Wikipedia</a></li>
<li><a href="https://lz.lbl.gov/">The LZ Dark Matter Experiment | The status and science of the ...</a></li>
<li><a href="https://lz.lbl.gov/detector/">Detector | The LZ Dark Matter Experiment</a></li>

</ul>
</details>

**社区讨论**: 社区评论总体积极但谨慎。一位评论者称赞预印本背景分析的彻底性，另一位指出 3 西格玛信号历史上常会消失。一些人希望这是真正的发现，而怀疑者则认为暗物质可能是原初黑洞，此类探测器无法探测到。

**标签**: `#dark matter`, `#particle physics`, `#LZ detector`, `#scientific discovery`

---

<a id="item-5"></a>
## [Paint.NET 借助 AI 从头重写 Direct2D 以支持 WINE](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Paint.NET 开发者 Rick Brewster 宣布，该应用现在包含一个内部从头编写、通过 /wine 标志触发的 Direct2D 干净室逆向工程重写版，以实现实验性的 WINE/Linux 支持。这个约 18 万行的重写主要由 Anthropic 的 AI 助手 Claude 编写。 这标志着 WINE 兼容性的一个重要里程碑，因为 Direct2D 此前是 Paint.NET 在 Linux 上运行的主要障碍。同时，它也展示了 AI 辅助编程在复杂大型项目中的潜力，尽管其“氛围编码”的性质和缺乏全面审查引发了对其可靠性和可维护性的质疑。 该重写位于 PaintDotNet.Windows.Direct2D1.Managed.dll 中，之所以必要，是因为 WINE 中 Direct2D 永远无法完全满足 Paint.NET 的需求。Brewster 指出，Claude 需要大量监督，尤其是在资源管理方面（最初遗漏了 AddRef() 调用），并做出了一些糟糕的设计决策，但也在 Direct2D 内置效果库的逆向工程中表现出色。

rss · Simon Willison · Sep 2, 05:50

**背景**: Direct2D 是微软开发的 2D 矢量图形 API，用于 Windows 上的硬件加速渲染。WINE 是一个兼容层，允许 Windows 应用程序在类 Unix 系统上运行，通常采用干净室逆向工程以避免版权问题。干净室设计涉及在不侵犯版权的情况下重建系统，通常由一个团队分析原始系统，另一个团队根据规范进行实现。这一新闻凸显了 AI 在软件开发中日益增长的作用，即使是复杂的逆向工程任务也不例外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Clean-room_reverse_engineering">Clean-room reverse engineering</a></li>

</ul>
</details>

**标签**: `#Direct2D`, `#WINE`, `#AI-assisted coding`, `#Paint.NET`, `#reverse engineering`

---

<a id="item-6"></a>
## [MiniMind：两小时从零训练 64M 参数大语言模型](https://github.com/jingyaogong/minimind) ⭐️ 8.0/10

MiniMind 是 jingyaogong 开发的开源项目，展示了在单张 NVIDIA 3090 GPU 上约 2 小时、成本约 3 元人民币即可从零训练一个 64M 参数的语言模型。该项目提供了涵盖预训练、SFT、LoRA、RLHF 等完整训练流程的代码，且全部使用纯 PyTorch 实现。 该项目显著降低了 LLM 训练的门槛，使计算资源有限的个人和小型团队也能参与其中。通过提供透明、可复现的路径，它促进了 AI 社区的教育和创新，可能加速高效模型的研究与开发。 “2 小时”指在单张 NVIDIA 3090 上跑完 1 个 epoch 的 SFT 实测耗时，“3 块钱”指对应时段的 GPU 租用成本。项目还扩展了多模态模型如 MiniMind-V 和 MiniMind-O，并包含了 MoE、数据清洗、DPO、PPO、GRPO 等先进技术的实现。

rss · GitHub Trending - Daily (All) · Sep 2, 23:45

**背景**: 大型语言模型（LLM）的训练通常需要巨大的计算资源，往往涉及数千亿参数和专用硬件。MiniMind 旨在通过提供可在消费级 GPU 上运行的极简但完整的实现，揭开 LLM 训练的神秘面纱，使用纯 PyTorch，不依赖 transformers 或 peft 等库的高层抽象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jingyaogong/minimind">GitHub - jingyaogong/ minimind : Train a 64M-parameter LLM from...</a></li>
<li><a href="https://pyshine.com/MiniMind-Train-LLM-From-Scratch/">MiniMind: Train a 64M-Parameter LLM From Scratch in 2 Hours</a></li>
<li><a href="https://topgit.dev/repo/jingyaogong/minimind">MiniMind: Train a 64M LLM from Scratch | TopGit</a></li>

</ul>
</details>

**社区讨论**: 该项目在 GitHub 上获得了超过 11,000 颗星，显示出强烈的社区兴趣。讨论可能强调该项目的可访问性和教育价值，一些用户可能会指出训练小模型与大型模型之间的权衡。

**标签**: `#LLM`, `#training`, `#education`, `#open-source`, `#deep learning`

---

<a id="item-7"></a>
## [Manim：3Blue1Brown 的数学视频动画引擎](https://github.com/3b1b/manim) ⭐️ 8.0/10

由 Grant Sanderson 为 3Blue1Brown 创建的动画引擎 Manim 正在 GitHub 上流行。该仓库已更新为要求 Python 3.10 或更高版本，并且包名现在为 'manimgl'，以区别于社区版。 Manim 已成为创建教育数学视频的关键工具，能够制作精确而精美的动画，帮助数百万人学习复杂主题。其开源特性和活跃社区促进了教育内容和衍生项目的广泛生态。 Manim 有两个版本：原始版 ManimGL（此仓库）和社区版（ManimCommunity/manim），后者更稳定且对初学者更友好。安装需要 FFmpeg、OpenGL，以及可选的 LaTeX，并通过 'pip install manimgl' 安装。

rss · GitHub Trending - Daily (All) · Sep 2, 23:45

**背景**: Manim 是一个 Python 库，允许用户以编程方式创建数学动画。它最初由 YouTube 频道 3Blue1Brown 的创建者 Grant Sanderson 开发，用于制作他的教育视频动画。2020 年，一群开发者将其分叉为社区版，该版本已成为大多数用户推荐使用的版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/3b1b/manim">GitHub - 3b1b/ manim : Animation engine for explanatory math videos</a></li>
<li><a href="https://www.manim.community/">Manim is a community-maintained Python library for creating...</a></li>
<li><a href="https://3b1b.github.io/manim/">manim documentation</a></li>

</ul>
</details>

**社区讨论**: 社区讨论突出了 ManimGL 和社区版之间的分歧，许多用户推荐社区版，因为它更稳定且维护活跃。一些用户对安装哪个版本感到困惑，而另一些用户则分享学习 Manim 的技巧和资源。

**标签**: `#animation`, `#education`, `#mathematics`, `#python`, `#open-source`

---

<a id="item-8"></a>
## [Crawl4AI：开源、面向 LLM 的网络爬虫备受关注](https://github.com/unclecode/crawl4ai) ⭐️ 8.0/10

Crawl4AI，一个专为 LLM 友好数据提取设计的开源网络爬虫，已获得超过 50,000 个 GitHub 星标，并发布了 0.9.3 版本，该安全更新修复了五个协调披露的安全公告和 33 个错误。该项目还宣布其 Cloud API 进入封闭测试阶段，旨在提供高性价比的大规模网页提取服务。 这很重要，因为 Crawl4AI 满足了日益增长的对干净、结构化网页数据的需求，以支持 AI 模型，特别是 RAG 管道和 AI 代理。它的流行反映了开源工具简化 AI 应用数据提取的趋势，可能减少对专有服务的依赖。 0.9.3 版本修复了包括任意文件写入、SSRF、PDF 处理中的拒绝服务以及 Docker Playground 中的两个 XSS 问题在内的安全公告，没有新增功能或破坏性变更。该项目支持 Python，并在 PyPI 上可用，具有无头浏览和 HTML 到 Markdown 转换等功能，以适配 LLM。

rss · GitHub Trending - Daily (All) · Sep 2, 23:45

**背景**: 面向 LLM 的网络爬虫是提取网页内容并将其格式化为 JSON、干净 HTML 或 Markdown 等结构的工具，这些格式更易于大型语言模型处理。Crawl4AI 是 Firecrawl 等商业服务的开源替代品之一，为开发者提供控制权和成本节省，但需要自行托管并管理代理和反机器人措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/unclecode/crawl4AI">GitHub - unclecode/crawl4ai: 🚀🤖 Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper. Don't be shy, join here: https://discord.gg/jP8KfhDhyN</a></li>
<li><a href="https://cobusgreyling.medium.com/open-source-llm-friendly-web-crawler-scraper-cb394a965c14">Open-source LLM Friendly Web Crawler & Scraper | by Cobus Greyling | Medium</a></li>
<li><a href="https://byteful.com/blog/best-firecrawl-alternatives">The Best Firecrawl Alternatives in 2026: Which Should You Use ?</a></li>

</ul>
</details>

**标签**: `#web-crawler`, `#LLM`, `#open-source`, `#data-extraction`, `#AI`

---

<a id="item-9"></a>
## [Anthropic 推出 Claude Code：终端智能编程工具](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 发布了 Claude Code，这是一款直接在终端中运行的智能编程工具，允许开发者通过自然语言命令执行日常任务、理解复杂代码并管理 git 工作流。该工具支持 macOS、Linux 和 Windows，安装方式包括 curl、Homebrew、PowerShell 和 WinGet，而 npm 安装已弃用。 Claude Code 代表了 AI 辅助开发的重大进步，提供了终端原生的智能体体验，有望简化开发流程并减少日常编码任务的时间。它与现有工具和 GitHub 标签功能的集成，使其在快速增长的 AI 编程智能体市场中具有竞争力。 Claude Code 需要 Node.js 18+，并通过 npm 以 @anthropic-ai/claude-code 分发，但 npm 安装已弃用，推荐使用原生安装程序。该工具会收集使用数据，包括代码接受/拒绝和对话数据，并提供插件以扩展功能，支持通过 /bug 命令报告问题。

rss · GitHub Trending - Python · Sep 2, 23:45

**背景**: 智能编程工具是能够自主编写、修改、调试和重构代码的软件，能够理解多文件上下文并规划跨代码库的更改。与简单的代码补全不同，这些智能体执行多步骤任务并从项目约定中学习。Claude Code 是 AI 编程智能体更广泛趋势的一部分，这些智能体与 IDE 和终端集成，如 Cursor 和 Cline。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude by Anthropic</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://code.claude.com/docs/en/overview">Overview - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#developer tools`, `#Anthropic`, `#terminal`, `#natural language processing`

---

<a id="item-10"></a>
## [通过逐步执行 MD5 测试 LLM 的长程状态跟踪能力](https://arxiv.org/abs/2609.00012) ⭐️ 8.0/10

该论文提出了一种基准测试，让 LLM 通过 64 轮中 196 次依赖工具调用逐步计算 MD5，从而将长程状态跟踪与指令解释分离开来。模型 gpt-oss-120b 在大多数完成的运行中成功地在所有调用中携带完整状态并返回正确的摘要。 这项工作通过为状态跟踪提供一个干净、可控的测试，解决了 LLM 评估中的一个关键空白，而状态跟踪对于依赖多步工具使用的智能体系统至关重要。研究结果可以指导模型架构或提示策略的改进，以减少长程任务中的错误级联。 该基准测试从头实现了 MD5（RFC 1321），将每次调用与真实轨迹对齐，并逐位检查摘要，因此任何失败都纯粹是由于簿记问题。在最强的设置中，每个原始工具都被替换为第二个 LLM，从而移除了任何精确算术预言机，成功取决于将模型的推理保持在上下文中，并对启用思考的工作器进行投票。

rss · arXiv - AI · Sep 2, 04:00

**背景**: MD5 是一种广泛使用的密码哈希函数，产生 128 位哈希值，由 Ronald Rivest 于 1991 年设计，并在 RFC 1321 中规定。LLM 中的长程任务具有挑战性，因为错误可能在许多依赖步骤中级联，而现有基准测试常常将状态跟踪与指令解释混为一谈，缺乏控制组来隔离核心困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/MD5">MD 5 - Wikipedia</a></li>
<li><a href="https://posttrainllm.com/docs/prds/multi-turn-agentic-eval/">Multi-turn / agentic tool - calling eval (PRD) - posttrainllm docs</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#long-horizon tasks`, `#state tracking`, `#agentic AI`, `#benchmarking`

---

<a id="item-11"></a>
## [SCAFFOLD：用于计算机科学图表问答与思维链推理的大规模数据集](https://arxiv.org/abs/2609.00018) ⭐️ 8.0/10

研究人员推出了 SCAFFOLD，这是一个大规模的结构化计算机科学研究图表数据集，包含（图像、标题、上下文、问答、思维链）元组。它包含三个版本：SCAFFOLD-157K（来自 3058 篇论文中 29887 个图表的 157387 对）、SCAFFOLD-37K（36797 对）和 SCAFFOLD-12K（12000 对），并在 Qwen2.5-VL-3B-Instruct 上进行了基线实验。 该数据集填补了视觉语言研究中的一个关键空白，为理解计算机科学论文中的技术图表提供了专门的资源，这些图表往往比文本传达更多信息。它使得在图表问答和思维链推理上训练和评估视觉语言模型成为可能，有望提升模型解读学术文献中复杂图表的能力。 该数据集通过布局检测和 PDF 解析从 arXiv 计算机科学论文中构建，并包含 AI 辅助的问题生成步骤。最大版本 SCAFFOLD-157K 涵盖 3058 篇论文中的 29887 个图表，而最小版本 SCAFFOLD-12K 用于在 Qwen2.5-VL-3B-Instruct 上进行基线实验。

rss · arXiv - AI · Sep 2, 04:00

**背景**: 计算机科学论文经常使用图表，如架构图、系统流程图和流水线示意图，来传达复杂信息。视觉语言模型（VLM）需要图像与标题、上下文、问题、答案和推理轨迹的配对数据，才能学会理解此类技术图表。思维链（CoT）推理轨迹提供了逐步解释，帮助模型对视觉内容进行推理。该数据集解决了缺乏专门针对计算机科学研究图表的公共资源的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2504.09479">Draw with Thought: Unleashing Multimodal Reasoning for Scientific Diagram Generation</a></li>
<li><a href="https://openaccess.thecvf.com/content/CVPR2025W/MAR/papers/Huang_Autonomous_Multimodal_Reasoning_via_Implicit_Chain-of-Vision_CVPRW_2025_paper.pdf">Autonomous Multimodal Reasoning via Implicit Chain-of-Vision Yiqiao Huang1,*,</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0306457324000864">Explainable Knowledge reasoning via thought chains for knowledge-based visual question answering - ScienceDirect</a></li>

</ul>
</details>

**标签**: `#dataset`, `#vision-language`, `#diagram understanding`, `#question answering`, `#chain-of-thought`

---

<a id="item-12"></a>
## [UI-Venus-2：扩展环境、任务与验证，推动 GUI 智能体走向真实应用](https://arxiv.org/abs/2609.00028) ⭐️ 8.0/10

UI-Venus-2 是一个通用型基础 GUI 智能体，通过统一的闭环推理-行动框架在移动端、网页和桌面端运行。它将环境扩展到超过 170 个多语言移动应用和原生桌面操作系统，采用深度研究流程生成任务，并使用带有视觉关键点和多模型投票的轨迹级与样本级评估器，以提供可靠的强化学习信号。 这项工作通过同时扩展环境覆盖、任务构建和奖励验证这三个维度，解决了 GUI 智能体部署中的关键瓶颈。它提供了一个开源基础，可能加速开发更通用、更可验证的智能体，用于现实世界的数字任务自动化。 该智能体集成了安全感知机制，以确保对关键操作的可控执行。技术报告强调了一个能力强、高效且开源的基础，旨在推动通用、可验证且具有自我反思能力的智能体的发展。

rss · arXiv - AI · Sep 2, 04:00

**背景**: 多模态 GUI 智能体通过视觉感知并与图形界面交互，但面向基准测试的模型常因环境有限、任务脆弱和奖励不可靠而在真实场景中失败。强化学习（RL）越来越多地用于训练此类智能体，但需要可靠的奖励信号。UI-Venus-2 顺应这一趋势，通过扩展环境、任务和验证来弥合基准测试与实际部署之间的差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2604.27955">[2604.27955] GUI Agents with Reinforcement Learning: Toward ... GUI Agents with Reinforcement Learning:Toward Digital Inhabitants Awesome Reinforcement Learning for GUI Agents - GitHub Enhancing the Power of GUI Agents by Reinforcement Learning GitHub - lll6gg/UI-R1: [AAAI 2026] Code for "UI-R1: Enhancing ... UI-R1: Enhancing Efficient Action Prediction of GUI Agents by ... UI-R1: Reinforcement Learning for GUI Agents: A New Era of ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Foundation_model">Foundation model</a></li>
<li><a href="https://github.com/showlab/awesome-gui-agent">GitHub - showlab/Awesome-GUI-Agent: 💻 A curated list of papers and resources for multi-modal Graphical User Interface (GUI) agents.</a></li>

</ul>
</details>

**标签**: `#GUI agent`, `#multimodal`, `#reinforcement learning`, `#task automation`, `#arXiv`

---

<a id="item-13"></a>
## [EULER：用于跨领域数学发现的多智能体系统](https://arxiv.org/abs/2609.00032) ⭐️ 8.0/10

EULER 是一种新颖的多智能体系统，将跨领域的数学转移（即“桥梁”）作为搜索的基本单元。该系统在 120 个近期猜想上进行了评估，产生了 10 个证明和 3 个反例，以及 45 个有范围的局部结果。 这项工作通过系统性地探索未充分利用的跨领域联系，可能显著推进自动定理证明和 AI 驱动的数学研究。其在近期猜想上的成功表明，它有望加速组合学及相关领域的发现。 EULER 并行运行直接、相邻领域和远距离领域三条路线，并使用六项有序的压力测试，在昂贵搜索之前拒绝无效的桥梁。消融研究表明，桥梁特定的压力测试将错误结论从 9 个减少到 3 个，而将桥梁材料与目标原生操作结合，产生了+4.2 个已解决任务的正面交互效应。

rss · arXiv - AI · Sep 2, 04:00

**背景**: 数学界通常使用不同的对象、不变量和工具，使得跨领域问题转移成本高昂且经常被跳过。自动定理证明旨在利用计算机程序寻找证明，而大型语言模型（LLM）的最新进展已在该领域展现出潜力。EULER 基于这些思想，将转移本身作为可搜索的单元，并通过证据检查的返回来确保有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.00032">[2609.00032] EULER : Exploring Underused Links with...</a></li>
<li><a href="https://papers.cool/arxiv/2609.00032">EULER : Exploring Underused Links with Evidence-Checked Return for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving - Wikipedia</a></li>

</ul>
</details>

**标签**: `#multi-agent systems`, `#mathematical discovery`, `#automated theorem proving`, `#AI for science`

---

<a id="item-14"></a>
## [ReNFT 通过内部概率质量重校准修复扩散模型后训练中的模式坍缩](https://arxiv.org/abs/2609.00061) ⭐️ 8.0/10

ReNFT 是一种新方法，通过内部概率质量重校准来修复奖励后训练扩散模型中的模式坍缩，无需依赖外部信号。它在保留大部分已获得奖励的同时恢复提示内多样性，在 PickScore 和 GenEval 上分别保留了 NFT 奖励的 98.9%和 99.0%，同时将 DreamSim-Div 分别提高了 58.8%和 55.0%。 这项工作解决了扩散模型后训练中的一个关键限制——模式坍缩，它会消除多样性并限制创造性输出。通过证明坍缩是抑制而非删除，ReNFT 为现有的外部干预提供了一种互补的内部替代方案，有望提高微调生成模型的可靠性和质量。 ReNFT 使用无条件探针来识别“反枢纽”提示，然后从相同的提示和初始噪声生成匹配的反事实提议，以暴露被抑制的替代方案。通过带有自适应翻转守卫的联合配对 NFT 更新实现修复，该方法在保持高奖励的同时显著提高了多样性指标。

rss · arXiv - Machine Learning · Sep 2, 04:00

**背景**: 扩散模型的奖励后训练常常导致模式坍缩，即模型将概率质量集中在少数几个奖励偏好的模式上，从而降低多样性。现有的缓解方法依赖外部信号或接口，例如用感知目标增强奖励或调整参考正则化，但没有一种方法能在不损失奖励的情况下修复已经坍缩的适配器。ReNFT 的洞见在于，后训练主要是在预训练继承的能力上重新分配概率质量，因此坍缩是抑制而非删除，可以在内部逆转。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2410.08315">[2410.08315] Avoiding mode collapse in diffusion models fine-tuned...</a></li>
<li><a href="https://arxiv.org/abs/2601.02036">[2601.02036] GDRO: Group-level Reward Post-training Suitable for Diffusion Models</a></li>
<li><a href="https://arxiv.org/html/2608.06125v1">Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#mode collapse`, `#reward post-training`, `#generative AI`, `#fine-tuning`

---

<a id="item-15"></a>
## [注意力敏感性不足以保持上下文学习能力](https://arxiv.org/abs/2609.00064) ⭐️ 8.0/10

本文提出了形式化指标——上下文敏感性（ICS）和 ICL-GAP，并通过在 Llama-2-7B 上的受控消融实验证明，优化基于注意力的敏感性（ICS）并不能保持行为层面的上下文学习能力，揭示了古德哈特式的解离现象。 这一发现挑战了基于注意力的诊断指标在评估和指导大语言模型微调时的可靠性，对模型对齐和评估实践具有重要意义。它强调必须将代理指标与行为结果进行验证，以避免无意中损害上下文学习能力。 在 Llama-2-7B 上的四臂消融实验中，一个最大化 ICS 的正则化器将 ICS 提升至 1.413，接近其几何上限的 0.5%以内，但 ICL-GAP 仍接近零，MMLU 准确率从 0.371 降至 0.279。端点分析显示，注意力在不同前缀间变得尖锐且近乎不相交，路由到格式和演示主体标记而非标签，而随机标签协议确认行为探针家族保持了动态范围。

rss · arXiv - Machine Learning · Sep 2, 04:00

**背景**: 上下文学习（ICL）使大语言模型能够在不更新权重的情况下，根据演示适应新任务，但微调可能会削弱这种能力。基于注意力的代理指标（如测量注意力随演示的变化）常用于检测上下文敏感性，但本文表明，优化此类代理指标可能导致古德哈特定律，即代理指标不再反映真实目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.00064">Attention Sensitivity Is Not Enough: Dissociating Attention-Level and...</a></li>
<li><a href="https://arxiv.org/abs/2310.09144">[2310.09144] Goodhart's Law in Reinforcement Learning</a></li>
<li><a href="https://neuralnetworklexicon.wordpress.com/generalization-and-evaluation/goodharts-law-ml-context/">Goodhart’s Law (ML Context) – Neural Network Lexicon</a></li>

</ul>
</details>

**标签**: `#in-context learning`, `#fine-tuning`, `#LLM evaluation`, `#attention mechanisms`, `#Goodhart's law`

---

<a id="item-16"></a>
## [仅看结果的 LLM 评测会漏掉智能体的隐性错误](https://arxiv.org/abs/2609.00038) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.00038）量化了仅看结果的 LLM 智能体评测的盲区，显示它只能捕捉 45%的隐性错误，同时误判 33%的正确轨迹。而逐步评分裁判将隐性错误召回率提升至 77%，且零误报，但成本增加 3 倍。 这项研究解决了 LLM 智能体评测中的一个关键盲区，因为仅看结果的指标是生产环境中的默认做法，但可能漏掉那些通过错误或不安全路径达到正确答案的智能体。该发现推动了更严谨、关注轨迹的评测方法，对 AI 安全和基准测试实践具有重要影响。 该研究使用一个确定性的工具使用支持台环境，包含脚本化的预言机策略和故障注入器，在 400 条轨迹上测试了五种裁判。值得注意的是，没有裁判阅读最终回复，一个附加在完美轨迹上的虚构承诺完全避开了规则裁判，并在 82%的情况下避开了步骤裁判；自一致性集成使成本增加三倍但未改善结果。

rss · arXiv - NLP · Sep 2, 04:00

**背景**: LLM 智能体通常通过向裁判展示请求和最终回复来评估，这种方法称为仅看结果的评测。这种方式在结构上无法发现那些通过错误步骤达到正确答案的智能体，即所谓的隐性错误。该论文引入了一个具有已知真实答案的受控环境来测量这一盲区，并比较了不同的评估策略，包括评估中间步骤的逐步评分裁判。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.00038">[2609.00038] trajectory-judge: What Outcome-Only LLM Judges ...</a></li>
<li><a href="https://academ.us/article/2609.00038/">[2609.00038] trajectory-judge: What Outcome-Only LLM Judges ...</a></li>
<li><a href="https://deeplearn.org/arxiv/771160/reflect:-intervention-supported-error-attribution-for-silent-failures-in-llm-agent-traces">REFLECT: Intervention-Supported Error Attribution for Silent Failures...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#evaluation`, `#AI safety`, `#benchmarking`, `#agent trajectories`

---

<a id="item-17"></a>
## [电路引导的权重缩放提升 LLM 安全拒绝能力](https://arxiv.org/abs/2609.00051) ⭐️ 8.0/10

该论文识别了 LLM 中的多阶段安全电路，包括有害检测头、安全神经元和拒绝头，并提出了电路引导的权重缩放来增强拒绝行为。在六个 LLM 上，该方法在对抗性攻击下将安全率提高了 26.5%，而在标准基准上仅造成 1.7%的准确率下降。 这项工作提供了对 LLM 如何实现安全性的机制性理解，提出了一种新的、保持架构的干预方法，可增强对对抗性提示的鲁棒性。它连接了机制可解释性与实际安全，可能指导未来的对齐技术和安全审计。 该安全电路通过因果干预在多种 LLM 架构和对抗性设置中得到验证。所提出的权重缩放方法简单且不改变架构，使其成为一种实用的探针和干预手段；然而，该论文为预印本，尚未经过同行评审。

rss · arXiv - NLP · Sep 2, 04:00

**背景**: 机制可解释性旨在逆向工程神经网络的内部计算，通常通过识别电路——执行特定功能的神经元或注意力头组。对抗性提示涉及精心构造输入以绕过安全护栏，这是 LLM 部署中持续存在的挑战。本研究应用机制可解释性来揭示负责拒绝行为的电路，提供了一种有针对性的方式来加强安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2609.00051v1">From Detection to Refusal: Safer LLMs via Circuit-Guided ...</a></li>
<li><a href="https://www.promptingguide.ai/risks/adversarial">Adversarial Prompting in LLMs | Prompt Engineering Guide Adversarial prompting - GeeksforGeeks Adversarial Prompt Engineering: The Dark Art of Manipulating LLMs Adversarial prompting - Test and strengthen the security and ... AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs Adversarial Prompting: Risks, Types, and Defenses for LLMs</a></li>

</ul>
</details>

**标签**: `#LLM safety`, `#mechanistic interpretability`, `#adversarial robustness`, `#AI alignment`

---

<a id="item-18"></a>
## [LLM 增强对齐实现零样本呼吸音分类](https://arxiv.org/abs/2609.00055) ⭐️ 8.0/10

一种新框架利用 LLM 生成的报告将自监督呼吸音编码器与医学术语对齐，实现零样本分类。在 6 个数据集的 9 项任务上，平均零样本 AUC 达到 61.3%，超过 CLAP（51.4%）和 Qwen2-Audio（54.9%）。 这项工作解决了自监督呼吸音编码器缺乏语义基础的问题，有望在没有任务特定标注数据的情况下实现临床诊断。它表明，在医疗应用中，结构化语义对齐可以超越大规模通用音频语言模型。 训练结合了基于 sigmoid 的对比损失、编码器原有的自监督目标以及相似性感知的负采样。该方法仅使用全规模基线所用数据的 43%，就达到了最高的线性探测 AUC（71.6%）。

rss · arXiv - NLP · Sep 2, 04:00

**背景**: 零样本学习（ZSL）允许模型利用辅助语义信息对未见过的类别进行分类。自监督学习（SSL）在没有外部标签的数据上训练模型，对比学习则区分相似和不相似的样本对。该框架将这些概念结合用于呼吸音分析，而呼吸音分析中标注数据稀缺。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Zero-shot_learning">Zero-shot learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Self-supervised_learning">Self-supervised learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Contrastive_learning">Contrastive learning</a></li>

</ul>
</details>

**标签**: `#zero-shot learning`, `#respiratory sound classification`, `#LLM-augmented alignment`, `#self-supervised learning`, `#medical AI`

---

<a id="item-19"></a>
## [RePro：基于证明验证的基准重写，实现可靠的 LLM 数学评估](https://arxiv.org/abs/2609.00062) ⭐️ 8.0/10

RePro 是首个将面向 Lean 的神经自动定理证明器集成到基准重写中的框架，确保重写后的问题和答案通过 Lean 证明验证。在 GSM8K 和 MATH 上的实验表明，RePro 达到了 100%的良定义性、可行性和答案正确性，而现有方法仍会产生无效实例。 这通过提供一种在不损害有效性的前提下重写基准的可靠方法，解决了 LLM 评估中的数据污染问题。它还揭示了 LLM 在经证明验证的重写基准上性能下降，表明其分数部分反映的是记忆而非真正的推理能力。 RePro 利用 Lean 验证的证明来保证重写实例的正确性，源代码和数据已在 GitHub 上公开。多个模型观察到的准确率下降表明它们对表面和结构变化敏感，指向记忆效应。

rss · arXiv - NLP · Sep 2, 04:00

**背景**: Lean 是一种基于归纳构造演算的证明助手和函数式编程语言，用于形式化验证。神经自动定理证明器（ATPs）利用学习信号生成证明步骤。数据污染是指训练数据与评估基准重叠，导致性能虚高；重写基准是一种缓解策略，但以往方法缺乏正确性保证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_theorem_prover">Lean theorem prover</a></li>
<li><a href="https://arxiv.org/html/2411.03923v1">Evaluation data contamination in LLMs: how do we measure it ...</a></li>
<li><a href="https://aclanthology.org/2025.findings-naacl.291/">Does Data Contamination Detection Work (Well) for</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#data contamination`, `#automated theorem proving`, `#mathematical reasoning`, `#benchmark rewriting`

---

<a id="item-20"></a>
## [Qwen-Drive-1.0：面向自动驾驶的统一视觉语言模型](https://arxiv.org/abs/2609.00111) ⭐️ 8.0/10

Qwen-Drive-1.0 提出了一个视觉语言基础模型，将 3D 感知、视觉问答和运动规划统一用于自动驾驶。它保留了预训练 VLM 的架构，并添加了外部鸟瞰图（BEV）感知头和规划专家。 这项工作是将大型多模态模型应用于自动驾驶的重要一步，有望提高可解释性和泛化能力。它可能影响未来将感知、推理和规划结合的统一驾驶系统的研究。 BEV 感知头联合执行 3D 目标检测、语义占用预测和 BEV 地图分割，作为可检查的 3D 结构接口。该模型采用分阶段训练方法，将驾驶监督与通用视觉语言数据相结合，以保持广泛的能力。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 鸟瞰图（BEV）感知是自动驾驶中的主流范式，从多个传感器提供统一的空间表示。3D 语义占用预测提供体素级的几何和语义细节。视觉-语言-动作模型（VLA）正在兴起，以统一驾驶策略的视觉理解、语言推理和可操作输出。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2508.07560">Progressive Bird ' s Eye View Perception for Safety-Critical...</a></li>
<li><a href="https://arxiv.org/html/2512.16760v1">Vision-Language-Action Models for Autonomous Driving: Past ...</a></li>
<li><a href="https://arxiv.org/abs/2609.00111">Qwen-Drive-1.0: An Initial Step towards a Vision-Language ...</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#vision-language model`, `#3D perception`, `#motion planning`, `#BEV`

---

<a id="item-21"></a>
## [ZimaBlue：通过可扩展视频预训练实现泛化的世界动作模型](https://arxiv.org/abs/2609.00188) ⭐️ 8.0/10

ZimaBlue 提出了一个三阶段框架，在大规模第一人称视频上预训练世界动作模型，并通过统一动作表示将其适配到机器人控制。在真实机器人零样本评估中，从仅使用目标机器人数据扩展到超过 12 万小时的具身视频，成功率从 36.1%提升到 77.8%。 这项工作通过利用丰富且无需动作标注的第一人称视频，解决了机器人操作中的关键扩展挑战，可能减少对昂贵的动作标注机器人数据的需求。它可能显著推动具身 AI 和机器人学的发展，实现更泛化且更具成本效益的机器人学习。 ZimaBlue 采用异步的 Slow-Fast 双系统架构，其中高容量的 Slow 世界模型提供可泛化的时空表示，轻量级的 Fast 分支在 NVIDIA RTX 4090 上实现 30 Hz 的动作预测。该框架包括因果具身视频预训练、使用统一动作表示的视频-动作中间训练，以及最终针对目标机器人的特化。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 世界动作模型（WAM）是具身预测-动作模型，学习世界在干预下如何演变并据此生成动作。它们通常复用大型视频生成模型或使用视觉-语言骨干网络。第一人称视频预训练（例如使用 Ego4D）提供了无需动作标签的可扩展具身体验来源，这对于克服机器人学中的数据稀缺至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.12090">[2605.12090] World Action Models: The Next Frontier in ... [2606.20781] World Action Models: A Survey - arXiv.org What Is a World Action Model (WAM)? | NVIDIA Glossary World Action Models (WAM): A Survey — Taxonomy & Paper List World Models and World Action Models (WAM) - jinxindeep.github.io From World Models to World Action Models: A Concise Tutorial ... Pretrained to Imagine, Fine-Tuned to Act: The Rise of World ...</a></li>
<li><a href="https://arxiv.org/abs/2606.20781">[2606.20781] World Action Models: A Survey - arXiv.org</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/world-action-model/">What Is a World Action Model (WAM)? | NVIDIA Glossary</a></li>

</ul>
</details>

**标签**: `#robotics`, `#world models`, `#video pre-training`, `#embodied AI`, `#manipulation`

---

<a id="item-22"></a>
## [流匹配的拉格朗日推导产生直线轨迹](https://arxiv.org/abs/2609.00198) ⭐️ 8.0/10

本文提出了一种自下而上的拉格朗日推导流匹配的方法，表明强制目标身份守恒通过拟线性平流偏微分方程产生直线轨迹。它为直线流为何能实现大步长提供了新的理论视角。 这项工作加深了对流匹配这一流行生成建模范式的理论理解，并可能激发新的方法或改进。它还解释了为什么经验模型需要蒸馏，可能指导未来的算法设计。 推导使用了连续去噪器的局部泰勒展开和严格的不变性条件（目标身份守恒）。通过特征线法解析求解所得的拟线性平流偏微分方程，得到直线轨迹，并将去噪器的雅可比矩阵隔离为曲率的来源。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 流匹配是一种无模拟的生成建模框架，通过回归向量场来训练连续归一化流。它通常从欧拉（宏观）视角出发，使用最优传输和连续性方程进行推导。相比之下，拉格朗日（粒子中心）视角关注单个粒子的轨迹，可以提供不同的见解。特征线法是求解一阶偏微分方程的标准技术，通过找到使偏微分方程简化为常微分方程的曲线来求解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.02747">[2210.02747] Flow Matching for Generative Modeling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Method_of_characteristics">Method of characteristics - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lagrangian_and_Eulerian_specification_of_the_flow_field">Lagrangian and Eulerian specification of the flow field</a></li>

</ul>
</details>

**标签**: `#generative models`, `#flow matching`, `#optimal transport`, `#PDE`, `#theory`

---

<a id="item-23"></a>
## [分布式隐式危害：MLLM 视频审核中的组合性安全盲点](https://arxiv.org/abs/2609.00206) ⭐️ 8.0/10

该论文提出了分布式隐式危害（DIH），这是用于视频审核的多模态大语言模型（MLLM）中的一个组合性安全盲点，即单独良性的组件组合起来传达有害含义。它提出了一种多智能体合成框架，生成了超过 9000 个带有推理注释的 DIH 视频，并对 30 多个 MLLM 进行了基准测试，揭示了持续存在的检测缺陷。 这项工作凸显了 AI 驱动的视频审核中的关键安全漏洞，表明即使是前沿模型也无法检测出由组合关系产生的危害。它提供了新的数据集和方法来解决这一问题，可能为未来多模态系统的安全评估和训练提供参考。 该研究聚焦于 DIH 的两个维度：跨视觉片段的时间分布危害（DIH-T）和音频与视觉流之间的跨模态危害（DIH-M）。多智能体合成框架将良性组件组合成有害场景，数据集涵盖纯视觉和音视频设置；来自社交媒体的真实世界 DIH 视频也表现出相同的失败模式。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 多模态大语言模型（MLLM）越来越多地用于视频审核，但它们通常孤立地评估各个组件，从而忽略了由组合产生的危害。组合性危害是 AI 安全中的一个已知挑战，但本文识别了视频审核中的一个特定盲点，即良性部分共同传达有害含义。所提出的多智能体合成方法解决了此类案例训练数据缺乏的问题，因为手动收集这些数据很困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.00206v1">Distributed Implicit Harm: A Compositional Safety Blind Spot ...</a></li>
<li><a href="https://arxiv.org/pdf/2609.00206">Distributed Implicit Harm: A Compositional Safety Blind Spot in...</a></li>
<li><a href="https://papers.cool/arxiv/2609.00206">Distributed Implicit Harm: A Compositional Safety Blind Spot in...</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#multimodal LLM`, `#video moderation`, `#compositional harm`, `#data synthesis`

---

<a id="item-24"></a>
## [超越语言先验：诊断并修复多模态大模型中的视觉来源幻觉](https://arxiv.org/abs/2609.00231) ⭐️ 8.0/10

本文挑战了多模态大语言模型（MLLM）中物体幻觉主要源于语言先验的主流观点，提供了视觉来源幻觉这一独立成因的定量证据。作者提出了对抗对比微调（ACFT），利用对抗扰动构建对齐的正负样本对进行对比微调，在多个基准上取得了最先进的性能。 这项工作意义重大，因为它为 MLLM 中的幻觉机制提供了新的理解，可能有助于构建更可靠的多模态 AI 系统。所提出的 ACFT 方法效率高（仅需 COCO 数据集的 0.9%），且零推理开销，使其在实际应用中具有实用性。 诊断方法使用余弦相似度分析和 Smooth Grad-CAM 熵测量，显示幻觉样本的图像-文本相似度较低（平均 0.158 对比-0.122），并出现注意力模式反转。ACFT 包含对抗幻觉属性翻转（AHAF）过程，该过程同时作为诊断探针，揭示 MLLM 的视觉表示接近幻觉决策边界。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 多模态大语言模型（MLLM）结合了视觉和文本理解，但常常出现物体幻觉，即生成图像中不存在的物体描述。以往研究将其归因于语言先验，如过度依赖文本共现统计。本文提出了一个互补的成因：视觉来源幻觉，源于错误的视觉特征提取以及图像和文本嵌入之间的错位。所提出的 ACFT 方法利用对抗样本和对比学习对模型进行微调，提高了其可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_large_language_model">Multimodal large language model</a></li>
<li><a href="https://arxiv.org/abs/2306.13549">[2306.13549] A Survey on Multimodal Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/1908.01224">[1908.01224] Smooth Grad-CAM++: An Enhanced Inference Level ... Smooth Grad-CAM++: An Enhanced Inference Level Visualization ... Smooth Grad-CAM++: An Enhanced Inference Level Visualization ... GitHub - yiskw713/SmoothGradCAMplusplus: The re ... Smooth Grad-CAM++: Enhanced CNN Interpretation [1908.01224] Smooth Grad-CAM++: An Enhanced Inference Level ... GitHub - jacobgil/pytorch-grad-cam: Advanced AI ...</a></li>

</ul>
</details>

**标签**: `#multimodal LLM`, `#hallucination`, `#fine-tuning`, `#computer vision`, `#NLP`

---

<a id="item-25"></a>
## [VeriOCRBench：OCR 推理中任务验证的基准测试](https://arxiv.org/abs/2609.00232) ⭐️ 8.0/10

本文介绍了 VeriOCRBench，一个包含 1,800 个样本、经人工验证的基准，用于评估多模态大语言模型（MLLM）在 OCR 任务验证上的表现。该基准包含 1,600 个注入陷阱的无效任务（涵盖 8 种陷阱类型）和 200 个无陷阱对照任务，并评估了 15 个主流 MLLM，揭示了持续存在的盲目遵从和诊断失败问题。 该基准填补了基于 OCR 的 MLLM 评估中一个关键可靠性空白，将焦点从仅执行答案转向验证任务的可执行性。它为诊断失败和过度拒绝提供了框架，这对于在真实 OCR 场景中部署 MLLM 至关重要，因为查询可能是无效或无法回答的。 VeriOCRBench 基于 8 个 OCR 相关数据集的源图像构建，涵盖 8 个真实世界图像域，并包含四个验证维度：视觉、上下文、事实和逻辑。该基准采用以视觉原子事实（VAF）为锚点的流程，并经过全面人工审计，能够解耦评估任务验证、根本原因诊断和过度拒绝。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 多模态大语言模型（MLLM）在 OCR 为中心的基准上表现出色，但这些基准通常假设每个查询都是有效且可回答的。在真实世界的 OCR 中，查询可能涉及难以辨认的文本、被遮挡的证据或矛盾的先决条件，要求模型在回答前验证任务的可执行性。VeriOCRBench 引入了基于 OCR 的任务验证作为新的评估范式，建立在 OCRBench v2 等先前工作的基础上，但专注于无效任务的可靠性空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.00232v1">Beyond Blind Compliance: Benchmarking Task Verification in ...</a></li>
<li><a href="https://arxiv.org/html/2501.00321v1">OCRBench v2: An Improved Benchmark for Evaluating Large ...</a></li>
<li><a href="https://academ.us/article/2609.00232/">[2609.00232] Beyond Blind Compliance: Benchmarking Task ...</a></li>

</ul>
</details>

**标签**: `#MLLM`, `#OCR`, `#benchmark`, `#evaluation`, `#robustness`

---

<a id="item-26"></a>
## [CoLT-Drive：用于驾驶可供性预测的反事实长尾基准与知识保持适应框架](https://arxiv.org/abs/2609.00242) ⭐️ 8.0/10

该论文提出了 CoLT-Drive，一个包含 3,536 个样本的反事实长尾基准，用于驾驶可供性预测，并提出了 KPA，一种知识保持的适应框架，结合了结构化提示、基于 SLERP 的专家合并和 RegMoE（一种基于情境感知的 LoRA 混合专家模块）。KPA 在 CoLT-Drive 上达到了 60.8%的配对准确率，优于预训练的 Qwen3-VL-2B 基线（50.3%）和 LoRA SFT（32.4%），同时保持了有竞争力的域内准确率。 这项工作将自动驾驶安全的研究重点从罕见物体识别转向决策层面的可供性预测，解决了长尾场景中的关键空白。所提出的基准和适应框架使小型视觉语言模型能够处理罕见物体引起的动作变化，这对于部署安全可靠的自动驾驶系统至关重要。 KPA 使用结构化感知到决策提示、基于 SLERP 的专家合并和 RegMoE（一种基于情境感知的 LoRA 混合专家模块），在保留预训练模型开放世界知识的同时分配轻量级适应能力。该基准和代码已在 Hugging Face 和 GitHub 上公开。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 驾驶可供性预测是一种直接感知方法，它将输入图像映射到与道路/交通状态可供性相关的关键感知指标，而不是处理整个场景或直接映射到命令。长尾自动驾驶失败通常被归因于罕见物体识别错误，但本文认为决策关键问题在于模型是否能推断出异常物体如何改变自车的可行高层动作。SLERP（球面线性插值）是一种用于合并模型权重的技术，而 LoRA（低秩适应）是一种参数高效的微调方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/1903.08746.pdf">Affordance Learning In Direct Perception for Autonomous Driving</a></li>
<li><a href="http://deepdriving.cs.princeton.edu/paper.pdf">DeepDriving: Learning Affordance for Direct Perception in ...</a></li>
<li><a href="https://neelmishra.github.io/blog/mlops/sota-frontiers/model-merging.html">Model Merging: SLERP, TIES, DARE | Neel Mishra</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#long-tail`, `#affordance prediction`, `#vision-language models`, `#benchmark`

---

<a id="item-27"></a>
## [StreamScout：面向流式视频问答的自适应推理框架](https://arxiv.org/abs/2609.00291) ⭐️ 8.0/10

StreamScout 是一个用于流式视频理解的自适应推理框架，它在上下文中仅维护一个轻量级的文本时间线，并在查询时逐步用最多三种视觉视图（近期帧、均匀回看、查询显著检索）来增强该时间线。它针对每个查询决定是停止还是升级到更深的视图，并引入了两个变体：StreamScout-S（通过 LoRA 蒸馏）和 StreamScout-R（通过强化学习），它们在降低推理成本的同时优于先前的方法。 这项工作解决了流式视频理解中一个新颖且重要的问题：针对每个查询决定访问记忆的深度，而不是使用固定成本的过程。通过实现自适应推理，StreamScout 可以显著降低 token 消耗和延迟，使其适用于实时应用，并提高视频问答系统的效率。 StreamScout 使用三级视觉视图的级联结构以及“停止或升级”策略。它在辅助集上探测级联，并将模型的能力边界蒸馏为轻量级 LoRA 适应的监督信号（StreamScout-S），然后通过强化学习（StreamScout-R）进一步优化策略。在 OVO-Bench 上，StreamScout-S 将 Qwen3-VL-8B 提升了 14.65 个点，同时比均匀采样少使用 59% 的 token，平均回答时间为 1.04 秒。

rss · arXiv - Computer Vision · Sep 2, 04:00

**背景**: 流式视频理解涉及在无界视频流上回答任意时刻到达的问题。现有系统通常维护一个有界记忆，并对每个查询使用固定成本的访问过程，忽略了所需证据的变化。StreamScout 引入了自适应推理，模型根据每个查询决定访问记忆的深度，使用轻量级文本时间线和渐进式视觉增强。这种方法与多模态大语言模型中的自适应推理以及查询显著检索技术相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.00291v1">StreamScout: Learning When to Look Deeper for Streaming Video ...</a></li>
<li><a href="https://en.papernotes.org/ICCV2025/video_understanding/aim_adaptive_inference_of_multi-modal_llms_via_token_merging_and_pruning/">[Paper Note] AIM: Adaptive Inference of Multi-Modal LLMs via Token...</a></li>
<li><a href="https://www.youtube.com/watch?v=MxUAZSUHFEc">QSVideo: Query-Conditioned Semantic Temporal Retrieval for ... Multi-modal Fusion and Query Refinement Network for Video ... WACV Poster Beyond the Highlights: Video Retrieval with ... StreamScout: Learning When to Look Deeper for Streaming Video ... Beyond the Highlights: Video Retrieval with Salient and ... Query-Aware Spatiotemporal Transformer-Based Framework for ...</a></li>

</ul>
</details>

**标签**: `#streaming video understanding`, `#adaptive inference`, `#video question answering`, `#memory management`, `#arXiv`

---

<a id="item-28"></a>
## [Fed-LSVI：首个具有对数通信成本的可证明高效联邦强化学习算法](https://arxiv.org/abs/2609.00193) ⭐️ 8.0/10

该论文提出了 Fed-LSVI，这是首个在情节式马尔可夫决策过程中，针对线性函数逼近的在线强化学习，具有可证明高效性的联邦强化学习算法。它实现了 O~(√(Md^3H^4T))的遗憾界，同时将通信成本降低到对情节数 T 的对数依赖。 这项工作解决了联邦强化学习中的关键通信和隐私约束，使智能体无需共享原始轨迹即可协作。它匹配了多智能体在线强化学习在线性函数逼近下的最佳已知遗憾界，是一项重要的理论进展，对分布式强化学习系统具有潜在影响。 Fed-LSVI 结合了基于行列式的事件触发同步机制和逐步反向更新，使智能体仅交换压缩的充分统计量。其遗憾界与多智能体在线强化学习的最佳已知结果相匹配，而通信成本仅随 T 对数增长，相比先前线性扩展的方法有显著改进。

rss · arXiv - Data Science & Statistics · Sep 2, 04:00

**背景**: 联邦强化学习旨在协作训练智能体同时保护数据隐私，但传统方法通常需要共享原始轨迹，导致高通信成本和隐私风险。线性函数逼近是处理强化学习中大规模状态空间的常用技术，而情节式马尔可夫决策过程（MDP）是在线强化学习的标准框架。通信效率在联邦设置中至关重要，联邦学习的最新进展已探索压缩通信以减少开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.00193">Provably Efficient Federated Reinforcement Learning with ...</a></li>
<li><a href="https://arxivtldr.org/abs/2609.00193">TL;DR: Provably Efficient Federated Reinforcement Learning ...</a></li>

</ul>
</details>

**标签**: `#federated reinforcement learning`, `#linear function approximation`, `#communication efficiency`, `#regret bound`, `#online RL`

---

<a id="item-29"></a>
## [去噪扩散蒙特卡洛实现精确全局 MCMC 采样](https://arxiv.org/abs/2609.00279) ⭐️ 8.0/10

该论文提出了一种新方法——去噪扩散蒙特卡洛（DDMC），该方法利用去噪扩散模型作为全局 MCMC 提议，并通过精确的 Metropolis-Hastings 校正。DDMC 通过在局部收敛的 MALA 样本上训练扩散模型，在复杂的高维目标密度上实现了高接受率。 这项工作弥合了扩散模型与 MCMC 之间的鸿沟，提供了一种新的精确采样方法，可能改进高维问题的贝叶斯推断和生成建模。它表明标准扩散训练的扩展行为可迁移至精确采样，可能影响依赖 MCMC 的领域。 DDMC 将基于全局去噪器的路径采样器与局部 MALA 采样器相结合，使用 Metropolis-Hastings 步骤，其接受率包含离散时间 SDE 近似的前向和反向路径密度。实验表明在多种复杂目标上具有高接受率，为可扩展性提供了初步证据。

rss · arXiv - Data Science & Statistics · Sep 2, 04:00

**背景**: 马尔可夫链蒙特卡洛（MCMC）方法，如 Metropolis-Hastings 和 MALA，用于从复杂概率分布中采样，但常因局部陷阱而在高维或多模态目标上表现不佳。扩散模型通过学习逆转噪声过程，在生成建模中取得了成功。本文提出将其用作全局提议以提升 MCMC 效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2609.00279">Exact Global MCMC with Denoising Diffusion</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metropolis–Hastings_algorithm">Metropolis–Hastings algorithm - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Metropolis-adjusted_Langevin_algorithm">Metropolis-adjusted Langevin algorithm - Wikipedia</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#MCMC`, `#Monte Carlo`, `#sampling`, `#Bayesian inference`

---

<a id="item-30"></a>
## [有效学习率坍缩统一大语言模型预训练中的损失动态](https://arxiv.org/abs/2608.24814) ⭐️ 8.0/10

一篇新的 arXiv 论文（2608.24814）发现了“ELR 坍缩”：当有效学习率（ELR，即学习率与参数范数的比值）在各次运行中匹配时，即使学习率和参数范数不同，损失轨迹也会坍缩。这一现象在优化器、架构、数据集和模型规模上均成立，平均坍缩误差通常为几个 10^-3。 这一发现可能统一并简化对大语言模型预训练中损失动态的理解，为学习率调度、范数控制和损失动态提供一个公共坐标。它可能改进超参数调优，并实现更具迁移性的函数缩放定律，从而影响 AI 研究和模型开发效率。 系统性消融实验确定归一化设计和学习率-范数变化的时间尺度是坍缩精度的关键决定因素。受控干预表明，权重衰减和 Hyperball 主要通过它们诱导的 ELR 调度来塑造损失动态，而用 ELR 替换学习率可使拟合的函数缩放定律（FSL）在不同范数控制方法间迁移。

rss · arXiv - Data Science & Statistics · Sep 2, 04:00

**背景**: 在神经网络训练中，学习率（LR）控制梯度下降的步长，而参数范数（如 Frobenius 范数）衡量权重的幅度。有效学习率（ELR）定义为学习率与参数范数的比值，本文表明它是控制损失动态的主要因素。函数缩放定律（FSL）旨在基于规模变量预测模型性能，而这项工作通过使用 ELR 作为坐标扩展了 FSL。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.24814">Effective Learning Rate Governs Loss Dynamics in Language ...</a></li>
<li><a href="https://www.aimodels.fyi/papers/arxiv/effective-learning-rate-governs-loss-dynamics-language">Effective Learning Rate Governs Loss Dynamics in Language ...</a></li>
<li><a href="https://arxivtldr.org/abs/2608.24814">Effective Learning Rate Governs Loss Dynamics in Language ...</a></li>

</ul>
</details>

**标签**: `#language model pretraining`, `#learning rate`, `#loss dynamics`, `#scaling laws`, `#optimization`

---