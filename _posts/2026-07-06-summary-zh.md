---
layout: default
title: "Horizon Summary: 2026-07-06 (ZH)"
date: 2026-07-06
lang: zh
---

> From 51 items, 5 important content pieces were selected

---

1. [GitHub 仓库泄露主要 AI 聊天机器人的系统提示](#item-1) ⭐️ 9.0/10
2. [Anthropic 发现语言模型中的全局工作空间](#item-2) ⭐️ 8.0/10
3. [哈佛发布开源机器学习系统工程教材](#item-3) ⭐️ 8.0/10
4. [Facebook 开源 Astryx 设计系统](#item-4) ⭐️ 8.0/10
5. [Anthropic 发布 Claude Code 智能编码工具](#item-5) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GitHub 仓库泄露主要 AI 聊天机器人的系统提示](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 9.0/10

GitHub 仓库 asgeirtj/system_prompts_leaks 一直在收集并发布来自 Claude、ChatGPT、Gemini、Grok 等主要 AI 聊天机器人的泄露系统提示，截至 2026 年 7 月仍在定期更新。 该仓库为理解控制 AI 行为的隐藏指令提供了前所未有的透明度，使研究人员和开发者能够了解安全约束、工具集成和模型个性。它已被《华盛顿邮报》引用，凸显了其公共重要性。 该仓库包含 Claude Fable 5、Opus 4.8、ChatGPT 5.5 Thinking、GPT 5.5 Instant、Gemini 3.5 Flash 等模型的提示，以及显示模型版本间变化的差异对比。它还涵盖了 Claude Code、GitHub Copilot 和 Perplexity 等工具。

rss · GitHub Trending - Daily (All) · Jul 6, 23:00

**背景**: 系统提示是定义 AI 聊天机器人行为方式的隐藏指令，包括语气、格式、安全规则和工具使用。公司通常对这些提示保密，因此此类泄露对于逆向工程和研究来说非常罕见且宝贵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">GitHub - asgeirtj/system_prompts_leaks: Extracted system ...</a></li>
<li><a href="https://deepwiki.com/asgeirtj/system_prompts_leaks">asgeirtj/system_prompts_leaks | DeepWiki</a></li>
<li><a href="https://x.com/undefinedKi/status/2073463359962280350">Someone leaked the system prompts of every major AI ...</a></li>

</ul>
</details>

**社区讨论**: 社区对透明度表示兴奋，一些人指出泄露的提示允许通过复制行为以 Opus 的价格运行 Fable 5。其他人则争论泄露专有提示的道德问题，但大多数人认为这对研究有利。

**标签**: `#AI`, `#system prompts`, `#leaks`, `#chatbots`, `#reverse engineering`

---

<a id="item-2"></a>
## [Anthropic 发现语言模型中的全局工作空间](https://www.anthropic.com/research/global-workspace) ⭐️ 8.0/10

Anthropic 的研究在语言模型中发现了一个共享的表示子空间，称为“全局工作空间”或 J-Space，它能够整合不同上下文中的信息。该子空间类似于人类意识的全局工作空间理论。 这一发现为理解大型语言模型如何推理和整合信息提供了新视角，可能推动 AI 可解释性和安全性的发展。同时，它也重新引发了关于 AI 与意识关系的讨论。 J-Space 被定义为基于信息几何的、层激活的微小变化对最终输出 logits 影响最大的子空间。研究表明，该子空间在不同提示和任务中是共享的，暗示存在共同的推理路径。

hackernews · in-silico · Jul 6, 17:44 · [社区讨论](https://news.ycombinator.com/item?id=48808002)

**背景**: 全局工作空间理论（GWT）由 Bernard Baars 于 1988 年提出，认为意识源于一个整合来自专门模块信息的全局工作空间。Anthropic 的研究将这一概念应用于语言模型，识别出类似的整合性子空间。这项工作建立在 Anthropic 之前的可解释性研究（如电路追踪和归因图）基础之上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Global_workspace_theory">Global workspace theory - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/research/team/interpretability">Interpretability Research \ Anthropic</a></li>
<li><a href="https://venturebeat.com/ai/anthropic-scientists-expose-how-ai-actually-thinks-and-discover-it-secretly-plans-ahead-and-sometimes-lies">Anthropic scientists expose how AI actually 'thinks' — and ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了兴奋也表达了怀疑。一些用户注意到与先前实验（如通过复制层来提高数学能力）的相似性，而另一些用户则质疑与意识的比较，认为 J-Space 更适合描述为抽象推理子空间。Neel Nanda 的评论文章提供了独立的复现和批评。

**标签**: `#LLM`, `#interpretability`, `#AI research`, `#Anthropic`, `#consciousness`

---

<a id="item-3"></a>
## [哈佛发布开源机器学习系统工程教材](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

哈佛大学 EDGE 实验室在 GitHub 上发布了一本名为《机器学习系统：人工智能系统工程原理与实践》的开源教材，涵盖机器学习系统工程的完整生命周期。 该资源填补了机器学习教育中系统工程方面的空白，不仅关注模型训练，对构建生产级机器学习系统的学生和从业者极具价值。 该书提供多种语言版本（英语、中文、日语、韩语），并包含 TinyTorch、实验、工具包和幻灯片等配套材料，采用 CC-BY-NC-SA 4.0 许可协议。

rss · GitHub Trending - Daily (All) · Jul 6, 23:00

**背景**: 机器学习系统工程涵盖生产环境中 ML 系统的设计、部署和维护。哈佛 CS249r 课程教授这些原理，本书即为该课程的开源教材。

**标签**: `#machine learning`, `#systems engineering`, `#education`, `#open source`

---

<a id="item-4"></a>
## [Facebook 开源 Astryx 设计系统](https://github.com/facebook/astryx) ⭐️ 8.0/10

Facebook 开源了 Astryx，这是一个基于 React 和 StyleX 构建的完全可定制的设计系统，已在内部使用了 8 年，覆盖超过 13,000 个应用。 此次发布为更广泛的开发者社区提供了一个成熟、经过实战检验的设计系统，包含 150 多个无障碍组件、品牌级主题和 AI 就绪工具，可能影响设计系统的构建和采用方式。 Astryx 目前处于测试阶段，附带 CLI、暗色模式和可直接使用的模板；它通过允许使用任何 CSS 方式通过 className 进行覆盖来避免样式锁定，并且其组件设计为可在任何层级进行组合。

rss · GitHub Trending - Daily (All) · Jul 6, 23:00

**背景**: 设计系统是一组可复用的 UI 组件和指南，帮助团队构建一致的界面。StyleX 是 Meta 开发的用于样式化 Web 应用的 JavaScript 库，结合了 CSS-in-JS 的人体工程学和静态 CSS 的性能。Astryx 作为 Meta 的内部设计系统已有八年，支撑了大量应用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stylex">Stylex</a></li>

</ul>
</details>

**标签**: `#design system`, `#React`, `#open source`, `#UI components`, `#Meta`

---

<a id="item-5"></a>
## [Anthropic 发布 Claude Code 智能编码工具](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 发布了 Claude Code，这是一款在终端中运行的智能编码工具，能理解代码库并通过自然语言命令自动执行任务。用户可通过 curl、Homebrew 或 WinGet 安装，并集成到 IDE 和 GitHub 中。 Claude Code 是大语言模型在自主编码辅助方面的实际应用，通过自动化日常任务和复杂代码理解，有望提升开发者生产力。它与 OpenAI Codex CLI 和 Cursor 等其他智能编码工具形成竞争。 Claude Code 需要 Node.js 18+，支持多种安装方式，但 npm 安装已弃用。它包含用于自定义命令和代理的插件，并收集使用数据用于反馈，同时设有隐私保护措施。

rss · GitHub Trending - Python · Jul 6, 23:00

**背景**: 智能编码工具是基于 AI 的助手，能够以最少的人工干预自主规划、编写、测试和修改代码，不同于传统的代码补全工具。Claude Code 基于 Anthropic 的 Claude 模型，在终端中运行，与现有 IDE 和开发工作流协同工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kdnuggets.com/top-5-agentic-coding-cli-tools">Top 5 Agentic Coding CLI Tools - KDnuggets</a></li>
<li><a href="https://cloud.google.com/discover/what-is-agentic-coding">What is agentic coding? How it works and use cases | Google Cloud</a></li>
<li><a href="https://code.claude.com/docs/en/vs-code">Use Claude Code in VS Code - Claude Code Docs</a></li>

</ul>
</details>

**标签**: `#AI coding assistant`, `#developer tools`, `#Anthropic`, `#CLI`, `#agentic AI`

---