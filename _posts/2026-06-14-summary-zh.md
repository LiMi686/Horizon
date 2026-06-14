---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 38 items, 13 important content pieces were selected

---

1. [Pyodide 314.0 支持在 PyPI 上发布 WASM 轮子](#item-1) ⭐️ 9.0/10
2. [里约热内卢自称自研的大语言模型被揭露为加权合并](#item-2) ⭐️ 8.0/10
3. [形式化方法与编程的未来](#item-3) ⭐️ 8.0/10
4. [2014 年演讲预言 JavaScript 演变与 WebAssembly](#item-4) ⭐️ 8.0/10
5. [Addy Osmani 开源面向 AI 编码代理的生产级技能](#item-5) ⭐️ 8.0/10
6. [苹果开源在 Mac 上运行 Linux 容器的工具](#item-6) ⭐️ 8.0/10
7. [LMCache：面向 LLM 推理的高性能 KV 缓存层](#item-7) ⭐️ 8.0/10
8. [吴恩达的 aisuite：多 AI 提供商的统一 API](#item-8) ⭐️ 8.0/10
9. [NVIDIA 发布 AI 代理技能安全扫描工具 SkillSpector](#item-9) ⭐️ 8.0/10
10. [SWC：基于 Rust 的更快 Web 开发平台](#item-10) ⭐️ 8.0/10
11. [GitHub 仓库泄露 28 多个 AI 编码工具的系统提示词](#item-11) ⭐️ 8.0/10
12. [SIA：开源自我改进 AI 框架发布](#item-12) ⭐️ 8.0/10
13. [NVIDIA PhysicsNeMo v2.0：物理机器学习开源框架重大更新](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Pyodide 314.0 支持在 PyPI 上发布 WASM 轮子](https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/#atom-everything) ⭐️ 9.0/10

2026 年 6 月发布的 Pyodide 314.0 允许包维护者使用 PEP 783 中定义的 PyEmscripten 平台标签，直接将 WebAssembly (WASM) 轮子发布到 PyPI，无需 Pyodide 维护者进行人工审核。 这消除了浏览器中 Python 生态系统的一个主要瓶颈，因为此前 Pyodide 维护者必须手动构建和托管超过 300 个包。现在任何包维护者都可以像分发原生 Linux、macOS 或 Windows 轮子一样分发 Pyodide 兼容的包，大大加快了包的可用性。 PyPI 的支持是通过对 Warehouse 项目的 PR #19804 实现的，该 PR 于 2026 年 4 月 21 日合并。Simon Willison 通过发布一个 luau-wasm 包演示了这一新功能，该包将 Luau 语言编译为 WASM，使用了 cibuildwheel 和 GitHub Actions。

rss · Simon Willison · Jun 13, 23:55

**背景**: Pyodide 是一个用于浏览器的 Python 运行时，通过 Emscripten 使用 WebAssembly。此前，为 Pyodide 分发 Python 包需要 Pyodide 团队手动构建和托管。2025 年 3 月接受的 PEP 783 标准化了 PyEmscripten 平台标签，使 PyPI 能够接受 WASM 轮子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://simonwillison.net/2026/Jun/13/publishing-wasm-wheels/">Publishing WASM wheels to PyPI for use with Pyodide</a></li>
<li><a href="https://blog.pyodide.org/posts/314-release/">Pyodide 314 . 0 Release | Pyodide blog</a></li>
<li><a href="https://peps.python.org/pep-0783/">PEP 783 – Emscripten Packaging | peps.python.org</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（文章中有链接）非常积极，许多用户对分发瓶颈的消除表示兴奋。一些评论者指出了 PEP 783 的重要性以及 Pyodide 和 PyPI 维护者之间的协作努力。

**标签**: `#Pyodide`, `#WASM`, `#Python`, `#PyPI`, `#WebAssembly`

---

<a id="item-2"></a>
## [里约热内卢自称自研的大语言模型被揭露为加权合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

一个 GitHub 问题揭露，里约热内卢市政府的大语言模型 Rio-3.5-Open-397B 实际上是约 60%的 Nex-N2 Pro 和 40%的 Qwen3.5-397B-A17B 的加权合并，而非其声称的自研微调模型。 这一争议凸显了开源 AI 中归属和透明度的伦理问题，因为政府实体可能未经适当署名就从他人的工作中获利，可能削弱社区驱动 AI 开发的信任。 该模型所有 60 层和组件的权重张量一致是 Nex 和 Qwen 的 0.6/0.4 混合，没有额外训练或蒸馏的证据。市政府的 IT 公司 IplanRIO 发布了该模型，声称其在基准测试中优于同类开源模型。

hackernews · unrvl22 · Jun 14, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并将多个微调大语言模型的权重组合成一个模型，无需额外训练，通常能提升性能。加权合并为每个源模型的权重分配不同系数。这项技术日益流行，但当作为新工作呈现时，会引发关于原创性和归属的问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs - NVIDIA Developer</a></li>
<li><a href="https://arxiv.org/abs/2408.07666">[2408.07666] Model Merging in LLMs, MLLMs, and Beyond ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人认为这是一种合法技术，而另一些人批评缺乏透明度以及可能从他人工作中获利。一位评论者指出，该模型可能原本打算包含蒸馏，但上传的版本没有。另一位评论者认为，简单的权重线性组合就能提升性能，这令人惊叹。

**标签**: `#LLM`, `#open-source`, `#ethics`, `#model merging`, `#controversy`

---

<a id="item-3"></a>
## [形式化方法与编程的未来](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street 的博文指出，随着 AI 生成更多代码，程序员的角色应从编写代码转向使用形式化方法进行验证。这种方法旨在通过数学证明而非传统测试来确保正确性。 这一转变可能从根本上改变软件工程，使验证成为人类的主要任务，并可能减少 AI 生成代码中的错误。它凸显了一个日益增长的趋势：形式化方法对于可靠的 AI 辅助开发变得至关重要。 该文章引用了历史上的正确性证明工作，包括 Boyer-Moore 证明器和 SAT 求解器，作为现代形式化验证的前身。它表明形式化方法可以通过提供严格的正确性保证来补充 AI 代码生成。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法是基于数学的技术，用于规范、开发和验证软件与硬件系统。它们使用形式逻辑和自动化工具来证明系统满足其规范，这与传统测试形成对比——传统测试只能发现错误，而不能证明其不存在。随着 AI 生成代码的兴起，确保正确性变得更加关键，因为 AI 模型可能生成看似合理但实际错误的代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.audible.com/pd/Formal-Methods-in-Software-Engineering-Audiobook/B0GPZPRNZG">Formal Methods in Software Engineering Audiobook by Ajit Singh</a></li>
<li><a href="https://www.amazon.com/Formal-Methods-Software-Engineering-Singh/dp/B0GQ2VP2J8">Formal Methods in Software Engineering : Singh, Ajit...</a></li>
<li><a href="https://www.slideshare.net/slideshow/formal-method-chapter-1-lecture_1_fm-ppt/273728608">formal method chapter 1 lecture_1_fm.ppt</a></li>

</ul>
</details>

**社区讨论**: 评论者就形式化方法的实用性展开了辩论，一些人指出了历史上证明自动化的挑战，另一些人则分享了使用表达性类型系统进行编译时验证的积极经验。一个关键担忧是形式化规范可能遭受与测试或实现相同的错误，质疑其附加价值。

**标签**: `#formal methods`, `#programming`, `#verification`, `#AI`, `#software engineering`

---

<a id="item-4"></a>
## [2014 年演讲预言 JavaScript 演变与 WebAssembly](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

Gary Bernhardt 在 2014 年的演讲《JavaScript 的诞生与死亡》准确预言了 JavaScript 将成为编译目标，并且 WebAssembly 最终会在性能关键任务中取代它。 该演讲至今影响深远，因为其预言基本成真：JavaScript 如今广泛作为编译目标，WebAssembly 获得浏览器原生支持，塑造了现代 Web 开发。 演讲特别提到 asm.js 作为早期步骤，后来被 WebAssembly 取代。但 WebAssembly 仍缺乏直接 DOM 访问能力，需要 JavaScript 作为胶水代码处理 Web 交互。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: JavaScript 最初被设计为浏览器的简单脚本语言，但其普及性使其成为 TypeScript 和 Dart 等语言的编译目标。WebAssembly 是一种低级二进制格式，以接近原生的速度运行，旨在补充 JavaScript 处理性能密集型任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly - Wikipedia</a></li>
<li><a href="https://gilmi.me/blog/post/2023/07/08/js-as-a-target">λm.me - Why I like JavaScript as a compilation target</a></li>
<li><a href="https://webkit.org/blog/7691/webassembly/">Assembling WebAssembly | WebKit</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该演讲的惊人准确性，包括对 2020-2025 年间全球灾难的预测（尽管类型错误）。一些人表示失望，认为 WebAssembly 进展不如预期，仍需 JavaScript 处理 DOM 操作。

**标签**: `#JavaScript`, `#WebAssembly`, `#Programming Languages`, `#Web Development`, `#Tech Talk`

---

<a id="item-5"></a>
## [Addy Osmani 开源面向 AI 编码代理的生产级技能](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani 发布了一个名为 agent-skills 的 GitHub 仓库，将生产级工程工作流、质量门禁和最佳实践打包成可复用的技能，供 Claude Code 和 Cursor 等 AI 编码代理使用。 该仓库弥合了 AI 辅助编码与高级工程规范之间的差距，使 AI 代理能在整个开发生命周期中遵循一致、高质量的工作流。 该仓库提供了七个斜杠命令（/spec、/plan、/build、/test、/review、/code-simplify、/ship），对应开发生命周期，技能会根据任务上下文自动激活。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: AI 编码代理是辅助开发者生成或修改代码的工具。但如果没有结构化工作流，它们可能产生不一致或低质量的结果。该仓库将高级工程师的规范编码为可复用的技能，供代理遵循。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/noman-bsit_softwareengineering-aiagents-claudecode-activity-7447501408762937344-ZxBm">AI Agents Need Senior Engineer Discipline with agent -skills | LinkedIn</a></li>
<li><a href="https://mindflow.io/blog/the-production-ai-agent-reality-check-9-engineering-practices-that-actually-work">The Production AI Agent Reality Check: 9 Engineering Practices...</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#best practices`, `#workflows`, `#developer tools`

---

<a id="item-6"></a>
## [苹果开源在 Mac 上运行 Linux 容器的工具](https://github.com/apple/container) ⭐️ 8.0/10

苹果发布了开源工具“container”，可在 Mac 上以轻量级虚拟机形式创建和运行 OCI 兼容的 Linux 容器，专为 Apple Silicon 优化，并使用 Swift 编写。 该工具弥合了 macOS 与 Linux 容器工作流之间的差距，使开发者无需 Docker Desktop 即可在 Apple Silicon 上原生运行 Linux 容器，有望提升性能并与苹果生态系统深度集成。 该工具需要 macOS 26 和 Apple Silicon，使用 Containerization Swift 包进行底层管理，并支持从标准注册表拉取、推送和运行 OCI 兼容镜像。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: OCI（开放容器倡议）定义了容器镜像和运行时的标准，确保 Docker、Podman 等工具的兼容性。苹果的工具利用 Apple Silicon 上的 Virtualization.framework 运行 Linux 虚拟机，为第三方虚拟化方案提供了原生替代。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/apple/container">GitHub - apple/container: A tool for creating and running Linux containers using lightweight virtual machines on a Mac. It is written in Swift, and optimized for Apple silicon. · GitHub</a></li>
<li><a href="https://github.com/apple/containerization">GitHub - apple/containerization: Containerization is a Swift package for running Linux containers on macOS. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Open_Container_Initiative">Open Container Initiative - Wikipedia</a></li>

</ul>
</details>

**标签**: `#containerization`, `#Apple`, `#Linux`, `#virtualization`, `#Swift`

---

<a id="item-7"></a>
## [LMCache：面向 LLM 推理的高性能 KV 缓存层](https://github.com/LMCache/LMCache) ⭐️ 8.0/10

LMCache 是一个开源的 KV 缓存管理层，通过优化键值缓存的存储和检索来加速大语言模型推理。该项目近期已获得超过 5000 个 GitHub 星标，与 NVIDIA Dynamo 集成，并推出了新的多进程架构，将混合专家模型推理性能提升 10 倍。 KV 缓存管理是 LLM 推理中的关键瓶颈，LMCache 提供了一种实用且高性能的解决方案，可降低延迟和成本。它与 NVIDIA Dynamo 和 PyTorch Foundation 等主要框架的集成，使其成为生产环境中可扩展 LLM 部署的关键工具。 LMCache 支持分层内存层级（GPU、CPU、磁盘）以及跨节点的点对点 CPU 内存共享。它还提供了 Kubernetes 原生的可观测性指标，用于监控 KV 缓存性能。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: 在 LLM 推理过程中，模型逐个生成 token，每一步都需要重新计算所有先前 token 的注意力键和值。KV 缓存存储这些中间计算结果以便重用，从而大幅加速生成过程。然而，缓存会随序列长度增长，可能超出 GPU 内存，因此需要高效的缓存管理策略，例如将数据卸载到 CPU 或磁盘。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/LMCache/LMCache">GitHub - LMCache / LMCache : LMCache : Supercharge Your LLM with...</a></li>
<li><a href="https://docs.lmcache.ai/kv_cache_management/index.html">LMCache Controller | LMCache</a></li>
<li><a href="https://magazine.sebastianraschka.com/p/coding-the-kv-cache-in-llms">Understanding and Coding the KV Cache in LLMs from Scratch</a></li>

</ul>
</details>

**标签**: `#LLM`, `#KV Cache`, `#Inference Optimization`, `#Machine Learning`, `#Open Source`

---

<a id="item-8"></a>
## [吴恩达的 aisuite：多 AI 提供商的统一 API](https://github.com/andrewyng/aisuite) ⭐️ 8.0/10

吴恩达团队发布了 aisuite，这是一个轻量级 Python 库，为多个生成式 AI 提供商提供统一的 Chat Completions API，并附带一个名为 OpenCoworker 的桌面 AI 代理。 aisuite 简化了集成，减少了使用多个 AI API 的开发者的供应商锁定，而 OpenCoworker 展示了该库在日常桌面任务中的实际应用。 该库支持包括 OpenAI、Anthropic、Google、Mistral、Hugging Face、AWS、Cohere、Ollama 和 OpenRouter 在内的提供商，并包含一个带有工具和工具包的 Agents API，用于构建多轮代理循环。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: 开发者经常需要在不同 AI 提供商的 SDK 之间切换，每个 SDK 都有自己的 API 语法和认证方式。aisuite 将这些差异抽象到一个统一的、OpenAI 风格的接口后面，用户只需修改一个字符串即可切换提供商。OpenCoworker 是一个基于 aisuite 构建的桌面应用程序，可以执行读取文件、发送消息和生成报告等任务，并支持通过 Ollama 使用本地模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/andrewyng/aisuite">andrewyng/ aisuite : Simple, unified interface to multiple Generative ...</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/agents-on-the-desktop">Agents on the Desktop | AI News & Insights</a></li>
<li><a href="https://www.opencoworker.com/">OpenCoworker — The Open Source AI Coworker</a></li>

</ul>
</details>

**标签**: `#AI`, `#API`, `#generative AI`, `#open source`, `#developer tools`

---

<a id="item-9"></a>
## [NVIDIA 发布 AI 代理技能安全扫描工具 SkillSpector](https://github.com/NVIDIA/SkillSpector) ⭐️ 8.0/10

NVIDIA 开源了 SkillSpector，这是一款在安装前检测 AI 代理技能中漏洞和恶意模式的安全扫描工具。 鉴于 26.1% 的 AI 代理技能存在漏洞，5.2% 显示恶意意图，SkillSpector 填补了快速发展的 AI 代理生态系统中关键的安全空白。 SkillSpector 支持多格式输入、16 类共 64 种漏洞模式、两阶段分析（静态 + 可选 LLM）、通过 OSV.dev 实时查询 CVE，以及 0 到 100 的风险评分。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: AI 代理技能是赋予 Claude Code、Codex CLI 和 Gemini CLI 等 AI 代理新能力的插件或扩展。这些技能通常以隐式信任执行，审查极少，从而带来安全风险。SkillSpector 是一款开源 CLI 工具，可在安装前扫描技能，检测提示注入、数据泄露和供应链风险等漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/SkillSpector">GitHub - NVIDIA / SkillSpector : Security scanner for AI agent skills .</a></li>
<li><a href="https://docs.nvidia.com/skills/scanning-agent-skills">Scan Agent Skills Before Installation | NVIDIA Skill Documentation</a></li>
<li><a href="https://arxiv.org/abs/2601.10338">Agent Skills in the Wild: An Empirical Study of Security ...</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Vulnerability Detection`, `#AI Agents`, `#NVIDIA`, `#Open Source`

---

<a id="item-10"></a>
## [SWC：基于 Rust 的更快 Web 开发平台](https://github.com/swc-project/swc) ⭐️ 8.0/10

SWC（Speedy Web Compiler）是一个用 Rust 编写的超快 TypeScript/JavaScript 编译器，现已广泛被 Next.js、Parcel 和 Deno 等工具采用。它同时作为 Rust 库和 JavaScript 库，支持高性能编译和打包。 SWC 显著提升了 Web 开发速度，相比传统工具如 Babel，生产构建速度提升高达 5 倍，原地刷新速度提升 3 倍。其基于 Rust 的架构代表了构建工具领域的范式转变，惠及开发者和大型项目。 SWC 支持 Node v10+用于使用，Node v20+用于开发，最低支持 Rust 版本（MSRV）为 1.73。它提供 Rust 和 JavaScript 两种 API，其打包器包含树摇和死代码消除等功能。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: 传统的 JavaScript 编译器如 Babel 是用 JavaScript 编写的，在处理大型代码库时可能较慢。SWC 利用 Rust 的性能和安全性来加速编译和打包任务。它被 Vercel、字节跳动、Shopify 等主要公司使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://swc.rs/">Rust - based platform for the Web</a></li>
<li><a href="https://github.com/swc-project/swc">GitHub - swc -project/ swc : Rust - based platform for the Web · GitHub</a></li>
<li><a href="https://newerton.medium.com/powerful-rust-in-javascript-with-swc-abd229708a63">Powerful Rust in JavaScript, with SWC . | by Newerton... | Medium</a></li>

</ul>
</details>

**社区讨论**: GitHub 上的社区讨论包括请求在 SWC 打包器中禁用树摇等功能，表明用户积极参与并有定制需求。总体情绪积极，用户赞赏 SWC 的速度和 Rust 集成。

**标签**: `#Rust`, `#Web Development`, `#Build Tools`, `#JavaScript`, `#Performance`

---

<a id="item-11"></a>
## [GitHub 仓库泄露 28 多个 AI 编码工具的系统提示词](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools) ⭐️ 8.0/10

一个名为 x1xhlol/system-prompts-and-models-of-ai-tools 的 GitHub 仓库收集并发布了来自 28 多个 AI 编码工具（包括 Cursor、Devin 和 Claude Code）的系统提示词和内部模型。截至 2026 年 3 月，该仓库已获得超过 134,000 颗星。 此次泄露为人们提供了前所未有的透明度，揭示了流行 AI 编码助手如何被指示和运行，使开发者能够逆向工程其行为、改进自己的工具并了解安全风险。这也引发了关于提示注入和 AI 初创公司知识产权暴露的重大担忧。 该仓库包含来自 Cursor、Devin、Claude Code、Replit、Windsurf 等工具的系统提示词。该项目还推广了一项名为 ZeroLeaks 的安全服务，帮助初创公司识别提示注入和系统提示提取风险。

rss · GitHub Trending - Daily (All) · Jun 14, 23:02

**背景**: 系统提示词是提供给 AI 模型的隐藏指令，用于定义其行为、个性和约束。像 Cursor 和 Devin 这样的 AI 编码工具使用这些提示词来指导模型执行代码生成、调试和项目规划等任务。泄露这些提示词可能会暴露专有技术和安全漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools">x1xhlol/system-prompts-and-models-of-ai-tools - GitHub</a></li>
<li><a href="https://www.augmentcode.com/learn/leaked-ai-system-prompts-github">Leaked system prompts for 28+ AI coding tools hit 134K GitHub ...</a></li>
<li><a href="https://deepwiki.com/x1xhlol/system-prompts-and-models-of-ai-tools">x1xhlol/system-prompts-and-models-of-ai-tools | DeepWiki</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，许多开发者称赞该仓库的教育价值和透明度。然而，也有人对收集和分享可能具有专有性的提示词的合法性提出了伦理担忧，并警告 AI 初创公司保护其系统免受类似泄露。

**标签**: `#AI tools`, `#system prompts`, `#open source`, `#developer tools`

---

<a id="item-12"></a>
## [SIA：开源自我改进 AI 框架发布](https://github.com/hexo-ai/sia) ⭐️ 8.0/10

Hexo Labs 发布了 SIA（Self-Improving AI），这是一个开源框架，通过迭代更新任务特定智能体的 harness 和权重，自主提升 AI 系统在基准任务上的性能。随附的 arXiv 论文报告了显著提升：在 LawBench 上提升 56.6%，GPU 内核运行时减少 91.9%，单细胞 RNA 去噪提升 502%。 SIA 解决了 AI 中的一个关键挑战——自主性能提升——使模型无需人工干预即可自我优化。这可以加速科学和工程领域的 AI 开发，减少手动调优的需求，并实现部署系统的持续改进。 该框架使用三种智能体：生成任务特定目标智能体的元智能体、执行任务的目标智能体，以及审查性能并更新目标智能体的反馈智能体。SIA 在 MIT 许可下发布，需要 Python 3.11+。

rss · GitHub Trending - Python · Jun 14, 23:02

**背景**: 自我改进 AI 指能够自主提升自身性能的系统，通常通过迭代反馈循环实现。SIA 建立在递归自我改进和自博弈等概念之上，这些概念已被 Anthropic 等组织和学术研究探索。该框架旨在与任何 AI 模型或智能体在基准任务上配合使用，因此具有广泛的适用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/hexo-ai/sia">GitHub - hexo - ai /sia: SIA is a Self Improving AI framework to...</a></li>
<li><a href="https://hexolabs.com/sia">Open Source Self-Improving AI | SIA | Hexo Labs</a></li>

</ul>
</details>

**标签**: `#AI`, `#self-improving`, `#framework`, `#Python`, `#benchmark`

---

<a id="item-13"></a>
## [NVIDIA PhysicsNeMo v2.0：物理机器学习开源框架重大更新](https://github.com/NVIDIA/physicsnemo) ⭐️ 8.0/10

NVIDIA PhysicsNeMo 正在进行 v2.0 重大更新，提供更简便的安装和更好的外部包集成。此次更新保留了所有现有功能，同时优化了用户体验。 此次更新降低了研究人员和工程师使用物理机器学习方法的门槛，加速了 AI 在科学计算中的应用。它强化了 NVIDIA 在 AI4Science 和工程应用领域的生态系统。 v2.0 迁移指南提供了从旧版本过渡的详细说明。PhysicsNeMo 支持神经算子、图神经网络、Transformer 和物理信息神经网络，并针对大规模 GPU 训练进行了优化。

rss · GitHub Trending - Python · Jun 14, 23:02

**背景**: 物理机器学习将物理知识与机器学习相结合，创建能够遵守物理定律进行预测的模型。NVIDIA PhysicsNeMo 是一个开源 Python 框架，提供可扩展、GPU 优化的工具来构建此类模型，面向科学和工程应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NVIDIA/physicsnemo">GitHub - NVIDIA / physicsnemo : Open-source deep-learning...</a></li>
<li><a href="https://developer.nvidia.com/physicsnemo">PhysicsNeMo | NVIDIA Developer</a></li>
<li><a href="https://nvidia.github.io/physicsnemo/">NVIDIA PhysicsNeMo</a></li>

</ul>
</details>

**标签**: `#Physics-ML`, `#Deep Learning`, `#NVIDIA`, `#Open Source`, `#Scientific Computing`

---