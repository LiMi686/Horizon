---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> From 37 items, 6 important content pieces were selected

---

1. [微软牵头公开信支持开放权重 AI 模型](#item-1) ⭐️ 8.0/10
2. [GitHub 发布官方多平台 Copilot Agent SDK](#item-2) ⭐️ 8.0/10
3. [Hugging Face 发布低延迟开源语音到语音库](#item-3) ⭐️ 8.0/10
4. [微软 TRELLIS.2：紧凑结构化潜变量实现高效 3D 生成](#item-4) ⭐️ 8.0/10
5. [字节跳动 DeerFlow 2.0：开源长时程超级智能体框架](#item-5) ⭐️ 8.0/10
6. [Karpathy 的 Autoresearch：用于夜间 LLM 训练的自主 AI 代理](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软牵头公开信支持开放权重 AI 模型](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

2026 年 7 月 24 日，微软牵头发布了一封题为《开放权重与美国 AI 领导力》的公开信，由包括 NVIDIA、亚马逊、Y Combinator、Linux 基金会以及后来加入的 OpenAI 在内的 235 家 AI 相关公司签署，反对美国政府可能对开放权重模型的限制。值得注意的是，Anthropic 没有签署，而是在三天后发布了自己的立场声明；另一封由前沿 AI 公司 1324 名员工签署的《Pacing the Frontier》公开信于 7 月 28 日发布。 这封公开信代表了行业对可能限制开放权重 AI 模型的政府政策的重大联合反对，凸显了一场对 AI 发展、竞争和安全具有广泛影响的重大政策辩论。主要科技公司的参与以及 Anthropic 的明显缺席，凸显了 AI 社区在如何平衡开放与风险方面的战略分歧。 该信明确支持蒸馏技术，即模型利用其他模型的输出进行训练，认为政策制定者不应将其与盗用混为一谈。Anthropic 的回应《我们对开放权重模型的立场》表达了对威权政府构建强大 AI 的担忧，并呼吁打击工业规模的蒸馏操作，同时表示从未主张禁止开放权重模型。

rss · Simon Willison · Aug 2, 04:16

**背景**: 开放权重模型是指其核心组件（包括训练后的权重）公开发布的 AI 模型，允许任何人下载和使用。这与保持专有的封闭模型形成对比。关于开放权重模型的争论集中在平衡透明度与创新以及潜在滥用和国家安全风险之间，尤其是在美中 AI 竞争的背景下。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.nytimes.com/2026/07/28/technology/open-weight-ai.html">What Is Open-Weights A.I.? - The New York Times</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**标签**: `#AI policy`, `#open source`, `#open-weight models`, `#industry letter`, `#Simon Willison`

---

<a id="item-2"></a>
## [GitHub 发布官方多平台 Copilot Agent SDK](https://github.com/github/copilot-sdk) ⭐️ 8.0/10

GitHub 已发布官方多平台 SDK，用于将 GitHub Copilot Agent 集成到应用程序中，目前处于技术预览阶段。该 SDK 支持 Python、TypeScript、Go、.NET、Java 和 Rust，可通过 npm、PyPI、NuGet、Go modules、crates.io 和 Maven Central 获取。 该 SDK 通过公开 Copilot CLI 背后的生产级代理运行时，降低了开发者构建基于 Copilot 的应用的门槛。它允许以编程方式访问规划、工具调用、文件编辑和命令执行，可能加速代理式 AI 在软件开发中的采用。 该 SDK 支持 Node.js/TypeScript、Python、Go、.NET、Rust 和 Java，安装命令包括 'npm install @github/copilot-sdk' 和 'pip install github-copilot-sdk'。大多数语言都提供了 cookbook，Go 和 Rust 提供了 API 文档。该 SDK 目前处于技术预览阶段，功能可能会发生变化。

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**背景**: GitHub Copilot 是一款 AI 驱动的编码助手，帮助开发者编写代码。Copilot Agent 是一个更先进的系统，可以自主规划和执行任务，例如编辑文件和运行命令。此前，开发者必须自行构建编排才能集成此类功能，而该 SDK 提供了一个现成的运行时。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for ...</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-sdk">Copilot SDK - GitHub Docs</a></li>
<li><a href="https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/">Build an agent into any app with the GitHub Copilot SDK</a></li>

</ul>
</details>

**标签**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#API`

---

<a id="item-3"></a>
## [Hugging Face 发布低延迟开源语音到语音库](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face 发布了一个名为“speech-to-speech”的新开源库，通过模块化流水线（VAD -> STT -> LLM -> TTS）和兼容 OpenAI Realtime 的 WebSocket API，支持构建本地语音代理。该库目前是 GitHub 今日趋势榜第一名。 此次发布满足了日益增长的端侧 AI 和低延迟语音代理需求，使开发者无需依赖云服务即可构建完全本地、开源的语音应用。它还提供了灵活、可替换的架构，可集成多种 LLM 后端，包括托管提供商或本地服务器，使其成为 AI 开发者社区的重要工具。 该流水线包括语音活动检测（VAD）、语音转文本（STT）、语言模型（LLM）和文本转语音（TTS），每个组件都可替换。默认配置使用 Parakeet TDT 进行本地 STT、OpenAI 兼容的 LLM 和 Qwen3-TTS 进行本地语音输出，并支持 CUDA 和 Apple Silicon。该库已在生产环境中作为数千台 Reachy Mini 机器人的对话后端运行。

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**背景**: 语音代理通常需要一系列组件：检测用户何时说话（VAD）、将语音转录为文本（STT）、使用语言模型生成响应（LLM）以及将文本转换回语音（TTS）。传统上，这些组件通常托管在云端，导致延迟和隐私问题。Hugging Face 的库旨在通过集成开源模型和兼容 OpenAI Realtime 的 API，提供低延迟、完全本地的替代方案，使开发者更容易在自己的硬件上构建和部署语音代理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/speech-to-speech">GitHub - huggingface/speech-to-speech: Build local voice agents with...</a></li>
<li><a href="https://www.linkedin.com/posts/andimarafioti_introducing-hugging-faces-speech-to-speech-activity-7231548059388723201-zFfS">Hugging Face 's Speech to Speech library | Andrés... | LinkedIn</a></li>
<li><a href="https://drose.io/aitools/tools/hugging-face-speech-to-speech">Hugging Face Speech - to - Speech | AI Developer Tools Tool</a></li>

</ul>
</details>

**标签**: `#speech-to-speech`, `#voice agents`, `#open-source`, `#Hugging Face`, `#AI`

---

<a id="item-4"></a>
## [微软 TRELLIS.2：紧凑结构化潜变量实现高效 3D 生成](https://github.com/microsoft/TRELLIS.2) ⭐️ 8.0/10

微软发布了 TRELLIS.2，这是一个 40 亿参数的大型 3D 生成模型，引入了名为 O-Voxel 的新型“无场”稀疏体素结构，用于高保真图像到 3D 生成。模型、代码和演示已在 GitHub 和 Hugging Face 上开源。 TRELLIS.2 通过从单张图像高效生成高质量 3D 资产，显著推进了 3D 生成技术，降低了游戏开发、产品设计和 AR/VR 等领域非专家的门槛。其开源发布促进了广泛采用和进一步研究。 该模型使用具有 16 倍空间下采样的稀疏 3D VAE 将资产编码为紧凑的潜空间，并支持任意拓扑，如开放表面和非流形几何。在 H100 GPU 上，生成 512³分辨率约需 3 秒，并能建模 PBR 材质，包括基础颜色、粗糙度、金属度和不透明度。

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**背景**: TRELLIS.2 基于早期的 TRELLIS 模型，该模型引入了用于 3D 生成的结构化潜变量（SLAT）。SLAT 在活动体素上使用局部潜变量来表示 3D 资产，允许解码为网格和辐射场等不同格式。TRELLIS.2 通过使用无场的 O-Voxel 表示改进了这一点，避免了有损转换，并更稳健地处理复杂拓扑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/microsoft/TRELLIS.2">GitHub - microsoft/TRELLIS.2: Native and Compact Structured ...</a></li>
<li><a href="https://microsoft.github.io/TRELLIS/">TRELLIS: Structured 3D Latents for Scalable and Versatile 3D ...</a></li>
<li><a href="https://arxiv.org/abs/2412.01506">[2412.01506] Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>

</ul>
</details>

**标签**: `#3D generation`, `#structured latents`, `#machine learning`, `#computer vision`, `#Microsoft`

---

<a id="item-5"></a>
## [字节跳动 DeerFlow 2.0：开源长时程超级智能体框架](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

字节跳动发布了 DeerFlow 2.0，这是对其开源智能体框架的彻底重写，现已成为一个长时程超级智能体框架，通过编排子智能体、记忆、沙箱和消息网关来处理持续数分钟到数小时的任务。该项目于 2026 年 2 月 28 日登上 GitHub Trending 榜首。 该版本通过支持此前对 AI 系统而言颇具挑战的复杂长时程任务，推动了自主智能体的发展。它为研究人员和开发者提供了一个开源选择，用于构建复杂的智能体，有望加速 AI 自动化和软件工程领域的创新。 DeerFlow 2.0 是一次彻底重写，与 v1 不共享任何代码；原始的深度研究框架在 1.x 分支上维护。它需要 Python 3.12+ 和 Node.js 22+，采用 MIT 许可证，字节跳动建议使用 Doubao-Seed-2.0-Code、DeepSeek v3.2 或 Kimi 2.5 模型。

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**背景**: 长时程智能体任务涉及数小时或数天的扩展动作序列，需要复杂的规划和适应能力。超级智能体框架是一种编排子智能体的框架，每个子智能体具有受限的上下文和工具，以处理复杂任务。消息网关为智能体间的通信提供受治理的层，处理认证、日志记录和路由。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bytedance/deer-flow">GitHub - bytedance/deer-flow: An open-source long-horizon ...</a></li>
<li><a href="https://ai-tldr.dev/releases/bytedance-deerflow-2/">DeerFlow 2.0 — open-source SuperAgent harness — ByteDance ...</a></li>
<li><a href="https://www.ibm.com/think/topics/agent-gateway">What is an Agent Gateway? | IBM</a></li>

</ul>
</details>

**标签**: `#AI`, `#Agent`, `#Open Source`, `#Automation`, `#ByteDance`

---

<a id="item-6"></a>
## [Karpathy 的 Autoresearch：用于夜间 LLM 训练的自主 AI 代理](https://github.com/karpathy/autoresearch) ⭐️ 8.0/10

Andrej Karpathy 发布了 'autoresearch'，这是一个 GitHub 仓库，允许 AI 代理在夜间自主运行 LLM 训练实验。代理修改训练代码，运行 5 分钟的实验，并迭代以改进模型的验证每字节比特数（val_bpb）。 该项目展示了一种新颖的工作流程，其中 AI 代理接管迭代研究过程，可能加速发现并减少人类工作量。它可能影响 AI 研究的进行方式，向更自主的实验方向发展。 该仓库非常精简，包含三个关键文件：prepare.py（固定）、train.py（代理编辑）和 program.md（人类编辑）。训练在单个 GPU（在 H100 上测试）上运行，固定 5 分钟时间预算，指标是 val_bpb，它与词汇表大小无关。

rss · GitHub Trending - Python · Aug 2, 22:48

**背景**: Karpathy 之前的项目 nanochat 是一个极简的单 GPU LLM 训练框架，涵盖分词、预训练、微调、评估和推理。Autoresearch 在此基础上添加了一个自主代理层，可以修改训练代码并在无需人工干预的情况下运行实验，旨在创建一个自我改进的研究循环。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can buy. · GitHub</a></li>
<li><a href="https://trelis.substack.com/p/train-an-llm-from-scratch-with-karpathys">Train an LLM from Scratch with Karpathy's Nanochat</a></li>
<li><a href="https://aiengineering.academy/LLM/ServerLessFinetuning/TrainNanochatModalTutorial/">Training Nanochat on Modal - AI Engineering Academy</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#LLM training`, `#automation`, `#research`, `#Karpathy`

---