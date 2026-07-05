---
layout: default
title: "Horizon Summary: 2026-07-05 (ZH)"
date: 2026-07-05
lang: zh
---

> From 36 items, 7 important content pieces were selected

---

1. [泄露的 AI 系统提示揭示隐藏指令](#item-1) ⭐️ 9.0/10
2. [数字游戏 vs 实体游戏：核心问题是所有权](#item-2) ⭐️ 8.0/10
3. [Chrome DevTools MCP：AI 代理获得浏览器控制能力](#item-3) ⭐️ 8.0/10
4. [哈佛发布开源机器学习系统教科书](#item-4) ⭐️ 8.0/10
5. [发布 354 个 AI 编程代理开源技能包](#item-5) ⭐️ 8.0/10
6. [谷歌发布 ADK 2.0：用于构建 AI 智能体的开源 Python 工具包](#item-6) ⭐️ 8.0/10
7. [Hugging Face 推出模块化语音到语音流水线](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [泄露的 AI 系统提示揭示隐藏指令](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 9.0/10

一个名为 system_prompts_leaks 的 GitHub 仓库汇集了来自 Claude、ChatGPT、Gemini 和 Grok 等主要 AI 聊天机器人的泄露系统提示，并定期更新及提供版本差异对比。 这一集合提供了前所未有的透明度，揭示了控制 AI 行为的专有指令，使研究人员、开发者和用户能够理解并审计安全约束、偏见和能力。 该仓库包含 Claude Fable 5、Opus 4.8、ChatGPT 5.5 Thinking、GPT 5.5 Instant、Gemini 3.5 Flash 等模型的提示，并提供如 Claude Opus 4.8 到 Fable 5 的差异对比。

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**背景**: 系统提示是定义 AI 聊天机器人行为方式的隐藏指令，包括安全规则、语气和能力。公司将其保密以防止操纵，但通过提示注入或用户技巧会发生泄露。该仓库集中了此类泄露以供分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">System Prompts Leaks - GitHub</a></li>
<li><a href="https://deepwiki.com/asgeirtj/system_prompts_leaks">asgeirtj/system_prompts_leaks | DeepWiki</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-fable-5.md">system_prompts_leaks/Anthropic/claude-fable-5.md at main · asgeirtj/system_prompts_leaks</a></li>

</ul>
</details>

**标签**: `#AI`, `#system prompts`, `#transparency`, `#security`, `#open source`

---

<a id="item-2"></a>
## [数字游戏 vs 实体游戏：核心问题是所有权](https://popcar.bearblog.dev/its-about-ownership/) ⭐️ 8.0/10

一篇博客文章指出，数字游戏与实体游戏之争的核心并非格式问题，而是所有权问题，呼吁通过法律保护确保买家对所购数字商品拥有可转让且不可撤销的访问权。 这很重要，因为随着游戏发行日益转向数字化，消费者面临失去传统实体版所享有的所有权权利（如转售、出借和永久访问）的风险。该讨论凸显了建立监管框架的迫切需求，以将数字购买视为财产而非可撤销的许可。 文章强调，数字商店可以实现“转让”功能以允许转售或出借，并且公司不应在销售后撤销访问权限。它还指出，Steam 的 DRM 可以被绕过以实现离线游玩，但这并非法律保障。

hackernews · popcar2 · Jul 5, 14:56 · [社区讨论](https://news.ycombinator.com/item?id=48794750)

**背景**: 数字版权管理（DRM）是一种用于控制对受版权保护的数字内容访问的技术，通常限制用户对已购媒体的操作。在游戏中，DRM 可能将游戏绑定到特定平台或要求在线验证，这意味着如果服务器关闭，游戏可能无法游玩。与实体游戏不同，数字购买通常只是获得许可而非所有权，这使得发行商能够撤销访问权限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://arbitrae.com/legal-frameworks-for-digital-ownership/">Understanding Legal Frameworks for Digital Ownership in the ...</a></li>
<li><a href="https://legalclarity.org/what-are-digital-rights-and-how-are-they-protected/">What Are Digital Rights and How Are They Protected?</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认同所有权论点，分享了在服务器下线后失去已购数字游戏访问权限的个人经历。一些人指出，盗版和破解提供了实用的变通方法，但认为需要法律保护来确保真正的所有权。其他人指出，行业向订阅模式的转变进一步侵蚀了消费者权利。

**标签**: `#digital ownership`, `#gaming`, `#consumer rights`, `#regulation`, `#DRM`

---

<a id="item-3"></a>
## [Chrome DevTools MCP：AI 代理获得浏览器控制能力](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Chrome DevTools 团队发布了名为 chrome-devtools-mcp 的官方模型上下文协议（MCP）服务器，使 AI 编码代理能够检查、调试和控制实时的 Chrome 浏览器。 这弥合了 AI 编码助手与真实浏览器环境之间的差距，使 AI 代理能够直接进行可靠的自动化、深入的调试和性能分析，从而显著简化 Web 开发和测试工作流程。 该 MCP 服务器使用 Puppeteer 进行自动化，并使用 Chrome DevTools 进行性能追踪和网络分析；它正式支持 Google Chrome 和 Chrome for Testing，默认收集使用统计信息，但可通过标志选择退出。

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**背景**: 模型上下文协议（MCP）是 Anthropic 于 2024 年 11 月推出的开放标准，它规范了 AI 系统与外部工具和数据源的集成方式。Chrome DevTools MCP 实现了该协议，使 Claude、Cursor 或 Copilot 等 AI 编码代理能够与实时浏览器交互，就像拥有完整的 DevTools 套件一样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/ chrome - devtools - mcp : Chrome DevTools ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>

</ul>
</details>

**标签**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#automation`, `#debugging`

---

<a id="item-4"></a>
## [哈佛发布开源机器学习系统教科书](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

哈佛大学在 GitHub 上发布了一本名为《机器学习系统》的开源教科书，涵盖工程化人工智能系统的原理与实践。该书提供多种语言版本，包括英文、中文、日文和韩文。 这本教科书填补了机器学习系统教育的空白，为学生和从业者提供了全面且免费获取的资源。其开源特性允许社区贡献和持续改进，有望成为该领域的标准参考。 该仓库不仅包含教科书文本，还提供实验、幻灯片和 TinyTorch 实现等补充材料。采用 CC-BY-NC-SA 4.0 许可，允许非商业性分享和改编。

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**背景**: 机器学习系统是一个跨学科领域，结合了机器学习算法与软件工程、分布式系统和硬件设计。传统的机器学习教育通常侧重于模型和算法，但在生产环境中部署和维护 ML 系统还需要数据管道、模型服务、监控和基础设施等方面的额外知识。

**标签**: `#machine learning`, `#systems`, `#textbook`, `#open-source`, `#AI engineering`

---

<a id="item-5"></a>
## [发布 354 个 AI 编程代理开源技能包](https://github.com/alirezarezvani/claude-skills) ⭐️ 8.0/10

Alireza Rezvani 发布了 claude-skills，这是一个开源仓库，包含 354 个可用于 Claude Code、OpenAI Codex、Gemini CLI、Cursor 等 13 个 AI 编程代理的生产级技能和插件，涵盖工程、营销、安全、合规、高管顾问等领域。 这是同类中最全面的开源库，大大降低了团队在不同领域采用 AI 编程代理的门槛。它使非工程人员（如营销人员、合规官员）也能利用具有领域专业知识的 AI 代理，可能加速企业 AI 应用。 该仓库包含 593 个 CLI 脚本（仅使用标准库，无需 pip 安装）、711 个参考模板和 102 个自定义命令。它原生支持 13 个平台或通过转换脚本支持，已获得超过 5200 个 GitHub 星标。

rss · GitHub Trending - Python · Jul 5, 22:57

**背景**: 像 Claude Code 和 Codex 这样的 AI 编程代理可以执行命令和生成代码，但缺乏内置的领域特定知识。技能（或插件）是模块化的指令包，提供结构化指令、工作流和决策框架来填补这一空白。该仓库聚合了适用于各种用例的技能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/alirezarezvani/claude-skills">GitHub - alirezarezvani/claude-skills: 337 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom commands, 330+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills.</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Answer_Engine_Optimization">Answer Engine Optimization</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#Claude Code`, `#plugins`, `#open-source`, `#productivity`

---

<a id="item-6"></a>
## [谷歌发布 ADK 2.0：用于构建 AI 智能体的开源 Python 工具包](https://github.com/google/adk-python) ⭐️ 8.0/10

谷歌发布了 ADK 2.0，这是一个开源、代码优先的 Python 工具包，用于构建、评估和部署复杂的 AI 智能体。该更新引入了用于基于图执行的工作流运行时，以及用于结构化智能体间委托的任务 API。 来自谷歌这样的主要参与者的这一版本，为开发者提供了一个灵活、代码优先的框架来构建生产级 AI 智能体，可能加速智能体 AI 在企业应用中的采用。其开源特性和多语言支持（Python、TypeScript、Go、Java、Kotlin）降低了开发者的门槛。 ADK 2.0 包含与 1.x 版本的不兼容变更，影响了智能体 API、事件模型和会话模式。ADK 2.0 生成的会话可被 ADK 1.28+ 读取，但与更旧的 1.x 版本不兼容。该工具包需要 Python 3.10+，并可通过 pip 安装。

rss · GitHub Trending - Python · Jul 5, 22:57

**背景**: AI 智能体是能够执行任务、做出决策并与用户或其他系统交互的自主程序。ADK 是谷歌用于构建此类智能体的开源框架，提供代码优先的方法，使开发者能够进行细粒度控制。2.0 版本增加了工作流编排和任务委托能力，使其适用于复杂的多智能体系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/adk-python">GitHub - google/adk-python: An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. · GitHub</a></li>
<li><a href="https://adk.dev/2.0/">Welcome to ADK 2.0 - Agent Development Kit (ADK)</a></li>
<li><a href="https://adk.dev/">Agent Development Kit (ADK)</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#Python`, `#open-source`, `#Google`, `#toolkit`

---

<a id="item-7"></a>
## [Hugging Face 推出模块化语音到语音流水线](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face 发布了一个开源语音到语音流水线，将 VAD、STT、LLM 和 TTS 组合成一个模块化、低延迟的语音代理，并通过兼容 OpenAI Realtime 的 WebSocket API 暴露。 该流水线使开发者能够构建完全本地、开源的语音代理，组件可互换，减少了对专有 API 的依赖，促进了语音 AI 领域的创新。 该流水线使用 Parakeet TDT 进行本地 STT，兼容 OpenAI 的 LLM，以及 Qwen3-TTS 进行语音输出，并支持任何兼容 OpenAI Realtime 的客户端。它已投入生产，用于数千台 Reachy Mini 机器人。

rss · GitHub Trending - Python · Jul 5, 22:57

**背景**: 语音代理通常使用 VAD（语音活动检测）、STT（语音转文本）、LLM（大语言模型）和 TTS（文本转语音）的流水线。Hugging Face 的产品将每一步模块化，使开发者能够轻松互换组件，并使用开源模型在本地运行所有内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/speech-to-speech">GitHub - huggingface/speech-to-speech: Build local voice agents with open-source models · GitHub</a></li>
<li><a href="https://livekit.com/blog/voice-agent-architecture-stt-llm-tts-pipelines-explained">Voice Agent Architecture: STT , LLM, and TTS Pipelines ... | LiveKit</a></li>
<li><a href="https://docs.runanywhere.ai/web/voice-agent">Voice Pipeline - RunAnywhere Documentation</a></li>

</ul>
</details>

**标签**: `#speech-to-speech`, `#voice agents`, `#open-source`, `#Hugging Face`, `#AI pipeline`

---