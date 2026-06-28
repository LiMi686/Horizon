---
layout: default
title: "Horizon Summary: 2026-06-28 (ZH)"
date: 2026-06-28
lang: zh
---

> From 46 items, 7 important content pieces were selected

---

1. [GLM 5.2 在网络安全基准测试中击败 Claude](#item-1) ⭐️ 8.0/10
2. [开发者用 Claude Code 分析自己的 MRI](#item-2) ⭐️ 8.0/10
3. [Jon Udell：将“人在回路中”重构为“智能体在回路中”](#item-3) ⭐️ 8.0/10
4. [SimpleX Chat：无任何用户标识符的通讯](#item-4) ⭐️ 8.0/10
5. [Openpilot：支持 300 多款车的开源驾驶辅助系统](#item-5) ⭐️ 8.0/10
6. [Free-for-Dev：免费云服务层级精选列表](#item-6) ⭐️ 8.0/10
7. [dbt Core v2.0 Alpha：Rust 重写提升速度](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM 5.2 在网络安全基准测试中击败 Claude](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

GLM 5.2 是一个拥有 7530 亿参数的开源混合专家模型，在 Semgrep 的网络安全漏洞检测基准测试中击败了 Claude，检测率达到 38%，每个漏洞发现成本仅为 0.17 美元。 这表明开源模型现在可以在网络安全等专业领域与专有领导者竞争，可能降低安全团队的成本并提高可及性。 GLM 5.2 采用混合专家架构，总参数为 7530 亿，但每个 token 仅激活部分专家，推理效率高。它还拥有 100 万 token 的上下文窗口和改进的推测解码。

hackernews · jms703 · Jun 28, 17:50 · [社区讨论](https://news.ycombinator.com/item?id=48709670)

**背景**: 大型语言模型越来越多地用于代码分析和漏洞检测。Semgrep 的基准测试评估模型发现真实安全漏洞的能力。GLM 5.2 是 GLM 系列的最新版本，权重完全开放且可商用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.2 - openlm.ai</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-glm-5-2-open-weight-model-3">What Is GLM 5.2? The Open-Weight Model Competing with Claude Opus on Coding | MindStudio</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 GLM 5.2 在日常编程任务中表现强劲，一位用户仅花费 20 美元就完成了两天的编码工作。其他人质疑基准测试方法，指出 Claude Code 是一个智能体框架，而非纯 LLM。一些人对中国在开源 AI 领域的快速进步表示惊讶。

**标签**: `#LLM`, `#benchmark`, `#cybersecurity`, `#open-source`, `#AI`

---

<a id="item-2"></a>
## [开发者用 Claude Code 分析自己的 MRI](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

一位开发者使用 Anthropic 的 AI 编程助手 Claude Code 分析自己的肩部 MRI 图像，获得了与最终诊断一致的第二意见。该实验展示了大型语言模型在医学影像解读中的新颖个人应用。 此案例既凸显了 AI 为患者提供可及的第二意见的潜力，也暴露了误诊、信任和临床监督方面的严重风险。它引发了放射科医生和患者之间关于 AI 在医疗中角色的辩论，尤其是在 LLM 能力日益增强的背景下。 该开发者没有医学背景，使用 Claude Code（可能是 Opus 模型）分析自己的 MRI，AI 的发现与医生的诊断一致。但社区指出，AI 可能在描述图像和解释推理时出错，即使最终答案正确，NIH 的研究也证实了这一点。

hackernews · engmarketer · Jun 28, 16:35 · [社区讨论](https://news.ycombinator.com/item?id=48708941)

**背景**: Claude Code 是基于 Anthropic 的 Claude 大型语言模型的工具，采用宪法 AI 训练以提高伦理合规性。AI 在医疗领域显示出前景，但也存在偏见、错误和患者安全风险，需要验证和监督。该开发者的实验是使用 LLM 进行个人医疗分析的草根案例，尚未经过临床验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://aihealthcare360.org/foundations/risks-of-ai-in-healthcare/">Risks of AI in Healthcare: Bias, Errors, and Patient Safety</a></li>
<li><a href="https://www.nih.gov/news-events/news-releases/nih-findings-shed-light-risks-benefits-integrating-ai-into-medical-decision-making">NIH findings shed light on risks and benefits of integrating ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论中既有赞叹也有谨慎。一位放射科医生指出需要完整的 3D 数据集来评估 AI 准确性，其他人则分享了个人误诊经历，并质疑将诊断视为确定性过程的观点。一些人欣赏可以无时间压力地向 AI 提问，但许多人强调 AI 尚不能完全信任用于医疗决策。

**标签**: `#AI in Healthcare`, `#Medical Diagnosis`, `#LLM Applications`, `#Patient Empowerment`, `#Radiology`

---

<a id="item-3"></a>
## [Jon Udell：将“人在回路中”重构为“智能体在回路中”](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell 提议将“人在回路中”重构为“智能体在回路中”，强调人类仍掌握控制权，邀请 AI 智能体作为团队成员，而非被排除在流程之外。 这种重构将叙事从人类监督 AI 转向人类主导与 AI 智能体的协作，可能影响团队设计智能体软件开发工作流的方式，并维护人类自主权。 Udell 特别警告智能体创建不可审查的拉取请求，倡导透明、人类邀请的智能体参与，而非黑箱特征生成。

rss · Simon Willison · Jun 28, 21:57

**背景**: 传统的“人在回路中”（HITL）概念将人类置于 AI 行动的监督者或验证者角色，往往暗示 AI 驱动流程。“智能体在回路中”则翻转了这一关系，主张人类拥有工作流并邀请 AI 智能体作为协作者。随着 AI 智能体在软件开发中日益自主，这一区分变得越来越重要，引发了关于不可审查代码变更的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://community.ibm.com/community/user/blogs/anuj-bahuguna/2025/05/25/ai-in-the-loop-vs-human-in-the-loop">AI in the Loop vs Human in the Loop: A Technical Analysis of ...</a></li>
<li><a href="https://www.trantorinc.com/blog/human-in-the-loop-vs-fully-autonomous-ai-agents">Human-in-the-Loop vs. Fully Autonomous AI Agents: Guide</a></li>
<li><a href="https://www.strata.io/blog/agentic-identity/practicing-the-human-in-the-loop/">A 2026 Guide to Human-in-the-Loop | Strata</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-4"></a>
## [SimpleX Chat：无任何用户标识符的通讯](https://github.com/simplex-chat/simplex-chat) ⭐️ 8.0/10

SimpleX Chat 发布了一个无需任何用户标识符即可运行的通讯网络，实现了设计上的 100% 隐私，并提供 iOS、Android 和桌面应用。 这种方法消除了基于标识符跟踪或分析用户的可能性，为私密通信设立了新标准，并可能影响更广泛的通讯生态系统。 SimpleX 不使用用户 ID，而是使用成对队列标识符，为 n 个用户创建多达 n*(n-1) 个消息队列，使网络图观察变得困难。它还采用抗量子端到端加密和双棘轮协议。

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**背景**: 传统的通讯应用如 WhatsApp 或 Signal 依赖用户标识符（电话号码、用户名）来路由消息，这些标识符可用于跟踪用户和构建社交图谱。SimpleX 完全移除了这些标识符，仅对每个连接使用临时队列地址。该设计受隐私设计原则启发，旨在从一开始就将隐私嵌入系统架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SimpleX_Chat">SimpleX Chat - Wikipedia</a></li>
<li><a href="https://github.com/simplex-chat/simplex-chat">GitHub - simplex-chat/simplex-chat: SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱!</a></li>
<li><a href="https://simplex.chat/messaging/">SimpleX Chat: The World's Most Secure Messaging</a></li>

</ul>
</details>

**标签**: `#privacy`, `#messaging`, `#decentralized`, `#open-source`

---

<a id="item-5"></a>
## [Openpilot：支持 300 多款车的开源驾驶辅助系统](https://github.com/commaai/openpilot) ⭐️ 8.0/10

Openpilot，一个用于机器人的开源操作系统，现已升级超过 300 款支持车型的驾驶辅助系统，最新硬件 comma four 售价 999 美元。 该项目使高级驾驶辅助功能大众化，让爱好者和研究人员能够在量产车上试验自动驾驶技术，可能加速该领域的创新。 Comma four 硬件尺寸仅为前代 comma 3X 的五分之一，并支持发布版和预发布版软件分支，以便提前体验新功能。

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**背景**: Openpilot 是由 comma.ai（由 George Hotz 于 2015 年创立）开发的开源驾驶辅助系统。它通过 comma four 等后装硬件，在兼容车辆上提供自适应巡航控制和自动车道居中功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Openpilot">openpilot - Wikipedia</a></li>
<li><a href="https://comma.ai/openpilot">comma.ai — make driving chill</a></li>
<li><a href="https://github.com/commaai/openpilot">GitHub - commaai/openpilot: openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. · GitHub</a></li>

</ul>
</details>

**标签**: `#autonomous driving`, `#open source`, `#robotics`, `#driver assistance`

---

<a id="item-6"></a>
## [Free-for-Dev：免费云服务层级精选列表](https://github.com/ripienaar/free-for-dev) ⭐️ 8.0/10

ripienaar/free-for-dev GitHub 仓库持续由超过 1600 名贡献者积极维护，为 DevOps 和基础设施开发者提供了一份精选的 SaaS、PaaS 和 IaaS 免费层级服务列表。 该列表为开发者节省了大量发现免费云服务的时间和精力，使他们能够无需前期成本即可构建和测试项目。由于其社区驱动的筛选和定期更新，它已成为 DevOps 社区中值得信赖的资源。 该列表仅包含提供真正免费层级（不仅仅是试用）的即服务产品，如果有时限，免费层级必须至少持续一年。它排除了自托管软件以及将 TLS 限制在付费层级的服务。

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**背景**: 许多云服务提供免费层级以吸引开发者，但查找和比较它们非常耗时。该 GitHub 仓库通过社区贡献，汇总了 CI/CD、分析和数据存储等类别的此类服务。

**标签**: `#devops`, `#free-tier`, `#SaaS`, `#PaaS`, `#IaaS`

---

<a id="item-7"></a>
## [dbt Core v2.0 Alpha：Rust 重写提升速度](https://github.com/dbt-labs/dbt-core) ⭐️ 8.0/10

dbt Labs 发布了 dbt Core v2.0 的 alpha 版本，这是用 Rust 完全重写的版本，作为 Fusion 引擎的基础，显著提升了解析和编译速度。 这次重写解决了大型 dbt 项目中的性能瓶颈，实现了更快的数据转换，并通过单一二进制文件简化了安装，可能加速数据工程团队的采用。 dbt Core v2.0 生成 Parquet 工件以支持可扩展分析，支持 macOS 和 Linux 的 x86-64 和 ARM 架构，Windows 仅支持 x86-64，同时保持与 JSON 工件的向后兼容性。

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**背景**: dbt（数据构建工具）是一个开源命令行工具，使数据分析师和工程师能够使用 SQL 转换仓库中的数据，并遵循版本控制和测试等软件工程最佳实践。原始的 dbt Core v1 用 Python 编写，而 v2.0 是用 Rust 重写的，旨在提高性能和可扩展性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_build_tool">Data build tool - Wikipedia</a></li>
<li><a href="https://www.getorchestra.io/guides/dbt-core-key-questions-answered">Dbt core : key questions answered | Orchestra</a></li>
<li><a href="https://jakubillner.github.io/2025/01/24/dbt-with-adb.html">Configuring dbt Core with Oracle Autonomous Database</a></li>

</ul>
</details>

**标签**: `#data engineering`, `#data transformation`, `#SQL`, `#open source`, `#analytics`

---