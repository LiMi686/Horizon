---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> From 41 items, 8 important content pieces were selected

---

1. [OpenAI 的 Astra 以每个不到 2000 美元解决十个十年未解数学难题](#item-1) ⭐️ 9.0/10
2. [NetBSD 11.0 发布，带来快速启动的 MICROVM 内核和防火墙改进](#item-2) ⭐️ 8.0/10
3. [DeepSeek V4-Flash-0731：304B 参数模型，性价比领先](#item-3) ⭐️ 8.0/10
4. [无状态 MCP 2.0 重燃兴趣，催生新工具](#item-4) ⭐️ 8.0/10
5. [GitHub 发布官方多平台 Copilot Agent SDK](#item-5) ⭐️ 8.0/10
6. [Deepfakes Faceswap：开源深度学习换脸工具](#item-6) ⭐️ 8.0/10
7. [Hugging Face 发布低延迟语音代理库 Speech-to-Speech](#item-7) ⭐️ 8.0/10
8. [微软 TRELLIS.2：用于 3D 生成的原生紧凑结构化潜变量](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 的 Astra 以每个不到 2000 美元解决十个十年未解数学难题](https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything) ⭐️ 9.0/10

OpenAI 宣布，其下一代主要模型的内部版本 Astra 解决了十个至少十年未有进展的数学问题，每个问题的解决成本按 GPT-5.6 Sol 代币价格计算不到 2000 美元。结果已在 Lean 4 中形式化，并发布在 openai/ten-proofs 仓库中，同时附有一篇论文和一份 LLM 生成的推理过程说明。 这标志着 AI 驱动研究的一个重要里程碑，可能改变数学和理论计算机科学问题的处理方式。它可能加速几何、密码学和复杂性等领域的发现，并可能为 AI 系统作为“发现基础设施”开辟市场。 OpenAI 没有透露有多少问题在花费 2000 美元后仍未解决，这是一个值得注意的保留点。仓库包含 Lean 4 形式化证明、一篇论文和一份 LLM 生成的 PDF，用于重建证明过程，但未公开所使用的提示词。

rss · Simon Willison · Aug 1, 20:34

**背景**: 这一公告紧随 Anthropic 声称其 Claude Mythos Preview 模型发现密码学弱点之后，后者花费了 10 万美元的代币。数学家们表现出既敬畏又存在性担忧的复杂情绪，有人（如 Kirwin Hampshire）描述了一种“深刻的精神危机”，而另一些人（如 Terence Tao）则展望了人机协作的“大数学”未来。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://runtimewire.com/article/openai-astra-ten-open-math-problems">OpenAI says unreleased Astra model solved 10 open... - RuntimeWire</a></li>
<li><a href="https://gist.github.com/lrehmann/ec36cc83f19bdf85b9f3ea19f02c9727">GPT - 5 . 6 Sol , Terra, and Luna model-selection guide — updated for...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论可能反映了兴奋与怀疑的混合情绪，评论者质疑成本效益和未披露的失败，同时也认可发布形式化证明的透明度。一些人可能会将其与 Deep Blue 对国际象棋的影响相提并论，认为这是 AI 在研究领域的转折点。

**标签**: `#AI research`, `#mathematics`, `#OpenAI`, `#theoretical computer science`, `#machine learning`

---

<a id="item-2"></a>
## [NetBSD 11.0 发布，带来快速启动的 MICROVM 内核和防火墙改进](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 8.0/10

NetBSD 11.0 已正式发布，引入了面向 x86 的新 MICROVM 内核，可在约 10 毫秒内启动，并改进了 npf 防火墙，包括二层和用户/组过滤。该版本还增加了 64 位 RISC-V 支持和更广泛的 Linux 系统调用。 此次发布意义重大，因为它增强了 NetBSD 的虚拟化能力，使其非常适合对启动速度要求极高的微服务和边缘计算场景。防火墙改进和新架构支持也巩固了 NetBSD 作为通用且可移植操作系统的地位，可能吸引新的用户和开发者。 MICROVM 内核利用 PVH 启动、VirtIO MMIO 和多项内核优化来实现快速启动。NetBSD 11.0 支持 57 个平台，该版本包含各种硬件改进和已知问题，这些问题已在官方发布说明中记录。

hackernews · jaypatelani · Aug 1, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49136736)

**背景**: NetBSD 是一个免费、开源的类 Unix 操作系统，以其可移植性和简洁设计而闻名。它是历史最悠久的 BSD 变体之一，专注于在广泛的硬件上运行。MICROVM 内核专为虚拟化环境设计，能够为轻量级虚拟机提供极快的启动时间，这对云和容器化工作负载非常有利。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.netbsd.org/releases/formal-11/NetBSD-11.0.html">Announcing NetBSD 11.0 RC7 (July 21, 2026)</a></li>
<li><a href="https://www.phoronix.com/news/smolBSD">smolBSD Builds On The NetBSD-MicroVM Kernel For Booting To Service VMs In Milliseconds - Phoronix</a></li>
<li><a href="https://www.theregister.com/2025/08/05/netbsd_11_is_near/?td=keepreading">NetBSD 11 prepares for launch with 57 supported platforms</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 BSD 的现状表示好奇，有用户询问它们的使用情况以及与 Linux 的比较。另一位用户询问 NetBSD 上 Wine 对运行 Windows 软件的支持，而其他人则强调了该版本的有用功能，如 MICROVM 内核和防火墙改进。一些人注意到发布公告对已知问题的坦诚态度，认为这令人耳目一新。

**标签**: `#NetBSD`, `#operating systems`, `#BSD`, `#release`, `#virtualization`

---

<a id="item-3"></a>
## [DeepSeek V4-Flash-0731：304B 参数模型，性价比领先](https://simonwillison.net/2026/Jul/31/deepseek-v4-flash-0731/#atom-everything) ⭐️ 8.0/10

DeepSeek 发布了 DeepSeek-V4-Flash-0731，这是一个 304B 参数的模型，智能体能力大幅增强，取代了预览版。其定价为每百万输入 tokens 0.14 美元，每百万输出 tokens 0.27 美元，Artificial Analysis 在智能指数上将其排在 MiniMax M3 之前。 该模型提供了顶尖的每美元性能，可能成为市场上性价比最高的智能选项，这可能会促使其他提供商降低价格或提高效率。其强大的智能体能力使其对构建 AI 智能体和自动化工作流的开发者极具相关性。 该模型有 304B 参数（Hugging Face 上 167GB），采用 MIT 许可证，MoE 架构激活 13B 参数。根据 Artificial Analysis，在智能指数与每任务成本图表中，它独自位于最具吸引力的象限，智能得分约 50，每任务成本约 0.028 美元。

rss · Simon Willison · Jul 31, 23:59

**背景**: DeepSeek 是一家以发布具有竞争力的开源权重模型而闻名的中国 AI 实验室。V4-Flash-0731 是 V4 系列的一部分，专为高效率和智能体用例设计。Artificial Analysis 智能指数聚合多个基准测试，提供单一的智能得分，而每任务成本衡量在标准化工作负载上运行模型的总成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/">DeepSeek Upgrades DeepSeek-V4-Flash-0731 with Major Agentic and Coding Gains - MarkTechPost</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek-ai/DeepSeek-V4-Flash-0731 · Hugging Face</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence , Performance, and Price</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的讨论强调了该模型令人印象深刻的性价比，一些用户注意到智能体能力的显著提升。还有关于模型推理级别的讨论，因为默认设置生成的鹈鹕图像不佳，但高推理努力产生了更好的结果。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#cost efficiency`

---

<a id="item-4"></a>
## [无状态 MCP 2.0 重燃兴趣，催生新工具](https://simonwillison.net/2026/Jul/31/stateless-mcp/#atom-everything) ⭐️ 8.0/10

2026-07-28 版 Model Context Protocol 规范（MCP 2.0）发布，引入了无状态协议核心，简化了客户端和服务端的实现。Simon Willison 本周构建了三个新工具，包括 mcp-explorer 和 datasette-mcp，以探索更新后的协议。 此次更新显著降低了构建 MCP 客户端和服务端的复杂性，使协议更易于使用且更适合 Web 应用扩展。它还通过提供比给代理完整 shell 访问更可审计的替代方案，解决了安全问题，可能重振 MCP 在 AI 生态系统中的采用。 新的无状态方法使用单个 HTTP 请求，通过头部路由（如 MCP-Protocol-Version、Mcp-Method）代替之前的两步会话初始化。这消除了服务器端会话状态的需求，提高了可扩展性并简化了实现，正如发布候选博客文章中的前后对比示例所示。

rss · Simon Willison · Jul 31, 23:13

**背景**: MCP（模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放协议，用于向 LLM 驱动的代理暴露工具。它在 2025 年获得了巨大关注，但后来被 Anthropic 的“Skills”功能所掩盖，后者允许代理使用终端和 curl 进行更灵活的工具访问。新的无状态规范解决了复杂性和可扩展性问题，使 MCP 再次具有竞争力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/">The 2026-07-28 MCP Specification Release Candidate | Model Context Protocol Blog</a></li>
<li><a href="https://blog.modelcontextprotocol.io/posts/2026-07-28/">The 2026-07-28 Specification | Model Context Protocol Blog</a></li>
<li><a href="https://en.wikipedia.org/wiki/Stateless_protocol">Stateless protocol</a></li>

</ul>
</details>

**标签**: `#MCP`, `#AI`, `#protocol`, `#LLM`, `#tools`

---

<a id="item-5"></a>
## [GitHub 发布官方多平台 Copilot Agent SDK](https://github.com/github/copilot-sdk) ⭐️ 8.0/10

GitHub 发布了官方多平台 SDK，用于将 GitHub Copilot Agent 集成到应用程序和服务中。该 SDK 支持 Python、TypeScript、Go、.NET、Java 和 Rust，并于 2026 年 6 月 2 日正式全面可用。 该 SDK 为开发者提供了对 GitHub Copilot 背后代理运行时的直接编程访问，无需构建自定义编排。它支持跨多种编程语言创建自定义 Copilot 扩展和代理工作流，可能加速整个生态系统中 AI 驱动的开发工具的发展。 该 SDK 提供了规划、工具调用、文件编辑、流式传输和多轮会话等功能。每种语言的 SDK 可通过相应的包管理器获取，如 npm、PyPI、NuGet、Go modules、crates.io 和 Maven Central，并提供了 cookbook 和 API 文档。

rss · GitHub Trending - Daily (All) · Aug 1, 22:47

**背景**: GitHub Copilot 是一个 AI 结对程序员，通过建议代码和自动化任务来帮助开发者。Copilot Agent 是一个更先进的系统，可以自主规划并执行多步骤任务。该 SDK 允许开发者将这种代理工作流嵌入到自己的应用程序中，利用与 Copilot CLI 相同的经过生产测试的运行时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for integrating GitHub Copilot Agent into apps and services · GitHub</a></li>
<li><a href="https://github.blog/changelog/2026-06-02-copilot-sdk-is-now-generally-available/">Copilot SDK is now generally available - GitHub Changelog</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-sdk/getting-started">Build your first Copilot-powered app - GitHub Docs</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#API`

---

<a id="item-6"></a>
## [Deepfakes Faceswap：开源深度学习换脸工具](https://github.com/deepfakes/faceswap) ⭐️ 8.0/10

Deepfakes/faceswap 作为一个广为人知的开源项目，持续提供用于在图片和视频中换脸的深度学习工具，最近更新包括 Phaze-A 和 Villain 等新模型，并通过 Discord 和论坛提供活跃的社区支持。 该项目普及了深度伪造技术，使高级换脸功能对公众开放，对人工智能伦理、隐私以及检测技术的需求产生了重大影响。其开源特性促进了创新，但也引发了关于滥用的担忧。 该工具包括三个主要步骤：提取、训练和转换，并提供 GUI 以方便使用。需要按照 INSTALL.md 进行安装，支持多种模型，例如使用 Phaze-A 模型进行 Emma Stone/Scarlett Johansson 的换脸示例。

rss · GitHub Trending - Daily (All) · Aug 1, 22:47

**背景**: 深度伪造是指使用深度学习创建的合成媒体，通常涉及换脸。deepfakes/faceswap 项目始于 2017 年左右，利用自编码器学习面部特征并在图像或视频之间进行交换。它已成为展示人工智能能力和突出伦理挑战的基准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepfakes/faceswap">GitHub - deepfakes/faceswap: Deepfakes Software For All · GitHub</a></li>
<li><a href="https://faceswap.dev/">Welcome - Faceswap</a></li>
<li><a href="https://www.insightface.ai/blog/the-evolution-of-neural-network-face-swapping-from-deepfakes-to-one-shot-innovation-with-insightface">The Evolution of Neural Network Face Swapping: From Deepfakes to One-Shot Innovation with InsightFace | InsightFace Blog</a></li>

</ul>
</details>

**社区讨论**: deepfakes/faceswap 的社区活跃，论坛和 Discord 上的讨论集中在技术支持、模型改进和伦理考量上。一些用户表达了对滥用的担忧，而另一些则强调该工具在娱乐和研究中的合法用途。

**标签**: `#deepfakes`, `#deep learning`, `#computer vision`, `#open source`, `#AI ethics`

---

<a id="item-7"></a>
## [Hugging Face 发布低延迟语音代理库 Speech-to-Speech](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face 发布了一个名为 speech-to-speech 的新开源库，提供低延迟、模块化的语音代理构建管道。该库已在 PyPI 和 GitHub 上可用，并支持 OpenAI Realtime 兼容的 WebSocket API，允许开发者轻松替换 VAD、STT、LLM 和 TTS 等组件。 该发布通过提供完全开源、模块化且低延迟的解决方案，显著降低了构建语音 AI 应用的门槛。它使开发者能够在本地硬件或托管提供商上完全运行语音代理，促进创新并减少对专有服务的依赖。 该管道由 VAD -> STT -> LLM -> TTS 组成，每个组件都可替换。LLM 插槽支持 OpenAI 兼容协议，允许与托管提供商、HF Inference Providers 或本地服务器（如 vLLM 和 llama.cpp）集成。该库已作为数千台 Reachy Mini 机器人的后端投入生产。

rss · GitHub Trending - Python · Aug 1, 22:47

**背景**: 语音代理通常需要多个组件：语音活动检测（VAD）、语音转文本（STT）、用于推理的语言模型（LLM）和用于输出的文本转语音（TTS）。Hugging Face 的 speech-to-speech 库将这些组件打包成一个连贯的管道，并暴露 OpenAI Realtime 兼容的 API 以便集成。这种方法符合开源语音 AI 的增长趋势，为专有解决方案提供了替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/speech-to-speech">GitHub - huggingface/speech-to-speech: Build local voice agents with open-source models · GitHub</a></li>
<li><a href="https://www.marktechpost.com/2024/08/27/hugging-face-speech-to-speech-library-a-modular-and-efficient-solution-for-real-time-voice-processing/">Hugging Face Speech-to-Speech Library: A Modular and Efficient Solution for Real-Time Voice Processing - MarkTechPost</a></li>
<li><a href="https://huggingface.co/blog/s2s_endpoint">Deploying Speech-to-Speech on Hugging Face</a></li>

</ul>
</details>

**标签**: `#speech-to-speech`, `#voice agents`, `#Hugging Face`, `#open-source`, `#AI/ML`

---

<a id="item-8"></a>
## [微软 TRELLIS.2：用于 3D 生成的原生紧凑结构化潜变量](https://github.com/microsoft/TRELLIS.2) ⭐️ 8.0/10

微软发布了 TRELLIS.2，这是一个 4B 参数的图像转 3D 生成模型，引入了名为 O-Voxel 的新型“无场”稀疏体素表示，并提供了论文、模型和交互式演示。它能够在高达 1536³的分辨率下生成具有复杂拓扑和 PBR 材质的高保真 3D 资产。 TRELLIS.2 代表了 3D 生成的重大进步，与以往方法相比，提供了一种更高效、更通用的途径。它处理任意拓扑和丰富纹理的能力可能加速游戏、电影和 VR/AR 领域的 3D 内容创作，而微软的开源发布可能进一步激发创新。 该模型使用具有 16 倍空间下采样的稀疏 3D VAE 将资产编码为紧凑的潜空间，并在 vanilla DiTs 上运行。在 NVIDIA H100 GPU 上，它在 512³分辨率下生成时间约 3 秒，1024³约 17 秒，1536³约 60 秒，数据处理无需渲染和优化。

rss · GitHub Trending - Python · Aug 1, 22:47

**背景**: 从图像生成 3D 通常依赖于网格或神经场等表示，这些表示在处理复杂拓扑和精细外观时往往存在困难。TRELLIS.2 建立在先前关于结构化潜变量（如 SLAT）的工作基础上，但引入了一种原生、紧凑的表示，直接编码 3D 数据而无需有损转换，从而实现高效、高质量的生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2512.14692">[2512.14692] Native and Compact Structured Latents for 3D Generation</a></li>
<li><a href="https://www.patreon.com/aifuturetech/posts/microsoft-2-4b-146837887">Microsoft TRELLIS . 2 4B 3 D Model Nailed It! Turn ANY... | Patreon</a></li>
<li><a href="https://www.nextdiffusion.ai/tutorials/generate-high-quality-3d-assets-trellis2-comfyui">Generate High-Quality 3 D Assets with TRELLIS . 2 in... | Next Diffusion</a></li>

</ul>
</details>

**社区讨论**: 来自 Patreon 和 Next Diffusion 等来源的社区评论强调，TRELLIS.2 是可访问的 3D 生成 AI 的重大飞跃，称赞其质量和速度。与 Meshy 和 Hunyuan 3D 等其他工具的比较表明它具有竞争力，但用户指出更高分辨率需要强大的硬件。

**标签**: `#3D generation`, `#structured latents`, `#Microsoft`, `#AI research`, `#GitHub`

---