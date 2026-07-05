---
layout: default
title: "Horizon Summary: 2026-07-05 (EN)"
date: 2026-07-05
lang: en
---

> From 36 items, 7 important content pieces were selected

---

1. [Leaked AI System Prompts Reveal Hidden Instructions](#item-1) ⭐️ 9.0/10
2. [Digital vs. Physical Games: The Real Issue Is Ownership](#item-2) ⭐️ 8.0/10
3. [Chrome DevTools MCP: AI Agents Gain Browser Control](#item-3) ⭐️ 8.0/10
4. [Harvard Releases Open-Source ML Systems Textbook](#item-4) ⭐️ 8.0/10
5. [354 Open-Source Skills for AI Coding Agents Released](#item-5) ⭐️ 8.0/10
6. [Google Releases ADK 2.0: Open-Source Python Toolkit for AI Agents](#item-6) ⭐️ 8.0/10
7. [Hugging Face Launches Modular Speech-to-Speech Pipeline](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Leaked AI System Prompts Reveal Hidden Instructions](https://github.com/asgeirtj/system_prompts_leaks) ⭐️ 9.0/10

A GitHub repository, system_prompts_leaks, has aggregated leaked system prompts from major AI chatbots including Claude, ChatGPT, Gemini, and Grok, with regular updates and diffs between versions. This collection provides unprecedented transparency into the proprietary instructions that govern AI behavior, enabling researchers, developers, and users to understand and audit safety constraints, biases, and capabilities. The repository includes prompts for Claude Fable 5, Opus 4.8, ChatGPT 5.5 Thinking, GPT 5.5 Instant, Gemini 3.5 Flash, and many more, with diff comparisons such as Claude Opus 4.8 to Fable 5.

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**Background**: System prompts are hidden instructions that define how an AI chatbot should behave, including safety rules, tone, and capabilities. Companies keep them proprietary to prevent manipulation, but leaks occur via prompt injection or user tricks. This repository centralizes such leaks for analysis.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks">System Prompts Leaks - GitHub</a></li>
<li><a href="https://deepwiki.com/asgeirtj/system_prompts_leaks">asgeirtj/system_prompts_leaks | DeepWiki</a></li>
<li><a href="https://github.com/asgeirtj/system_prompts_leaks/blob/main/Anthropic/claude-fable-5.md">system_prompts_leaks/Anthropic/claude-fable-5.md at main · asgeirtj/system_prompts_leaks</a></li>

</ul>
</details>

**Tags**: `#AI`, `#system prompts`, `#transparency`, `#security`, `#open source`

---

<a id="item-2"></a>
## [Digital vs. Physical Games: The Real Issue Is Ownership](https://popcar.bearblog.dev/its-about-ownership/) ⭐️ 8.0/10

A blog post argues that the core debate around digital versus physical games is not about format but about ownership, calling for legal protections to ensure buyers have transferable and irrevocable access to purchased digital goods. This matters because as game distribution shifts increasingly to digital, consumers risk losing the ownership rights they traditionally enjoyed with physical copies, such as resale, lending, and permanent access. The discussion highlights a growing need for regulatory frameworks that treat digital purchases as property rather than revocable licenses. The post emphasizes that digital stores could implement a 'transfer' functionality to allow resale or lending, and that companies should not be able to revoke access after sale. It also notes that Steam's DRM can be bypassed, allowing offline play, but this is not a legal guarantee.

hackernews · popcar2 · Jul 5, 14:56 · [Discussion](https://news.ycombinator.com/item?id=48794750)

**Background**: Digital rights management (DRM) is technology used to control access to copyrighted digital content, often restricting what users can do with purchased media. In gaming, DRM can tie a game to a specific platform or require online authentication, meaning that if servers shut down, the game may become unplayable. Unlike physical games, digital purchases are typically licensed, not owned, giving publishers the ability to revoke access.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://arbitrae.com/legal-frameworks-for-digital-ownership/">Understanding Legal Frameworks for Digital Ownership in the ...</a></li>
<li><a href="https://legalclarity.org/what-are-digital-rights-and-how-are-they-protected/">What Are Digital Rights and How Are They Protected?</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the ownership argument, sharing personal experiences of losing access to purchased digital games when servers were taken offline. Some note that piracy and cracks provide a practical workaround, but argue that legal protections are needed to ensure true ownership. Others point out that the industry's shift toward subscription models further erodes consumer rights.

**Tags**: `#digital ownership`, `#gaming`, `#consumer rights`, `#regulation`, `#DRM`

---

<a id="item-3"></a>
## [Chrome DevTools MCP: AI Agents Gain Browser Control](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

The Chrome DevTools team released an official Model Context Protocol (MCP) server called chrome-devtools-mcp, enabling AI coding agents to inspect, debug, and control a live Chrome browser. This bridges the gap between AI coding assistants and real browser environments, allowing for reliable automation, in-depth debugging, and performance analysis directly from AI agents, which could significantly streamline web development and testing workflows. The MCP server uses Puppeteer for automation and Chrome DevTools for performance tracing and network analysis; it officially supports Google Chrome and Chrome for Testing, and collects usage statistics by default with an opt-out flag.

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 that standardizes how AI systems integrate with external tools and data sources. Chrome DevTools MCP implements this protocol, allowing AI coding agents like Claude, Cursor, or Copilot to interact with a live browser as if they had access to the full DevTools suite.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/ChromeDevTools/chrome-devtools-mcp">GitHub - ChromeDevTools/ chrome - devtools - mcp : Chrome DevTools ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol</a></li>
<li><a href="https://modelcontextprotocol.io/docs/getting-started/intro">What is the Model Context Protocol (MCP)?</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#automation`, `#debugging`

---

<a id="item-4"></a>
## [Harvard Releases Open-Source ML Systems Textbook](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

Harvard University has released an open-source textbook titled 'Machine Learning Systems' on GitHub, covering principles and practices of engineering AI systems. The book is available in multiple languages including English, Chinese, Japanese, and Korean. This textbook fills a gap in ML systems education by providing a comprehensive, freely accessible resource for students and practitioners. Its open-source nature allows community contributions and continuous improvement, potentially becoming a standard reference in the field. The repository includes not only the book text but also supplementary materials such as labs, slides, and a TinyTorch implementation. It is licensed under CC-BY-NC-SA 4.0, allowing non-commercial sharing and adaptation.

rss · GitHub Trending - Daily (All) · Jul 5, 22:57

**Background**: Machine learning systems is an interdisciplinary field that combines ML algorithms with software engineering, distributed systems, and hardware design. Traditional ML education often focuses on models and algorithms, but deploying and maintaining ML systems in production requires additional knowledge of data pipelines, model serving, monitoring, and infrastructure.

**Tags**: `#machine learning`, `#systems`, `#textbook`, `#open-source`, `#AI engineering`

---

<a id="item-5"></a>
## [354 Open-Source Skills for AI Coding Agents Released](https://github.com/alirezarezvani/claude-skills) ⭐️ 8.0/10

Alireza Rezvani released claude-skills, an open-source repository containing 354 production-ready skills and plugins for Claude Code, OpenAI Codex, Gemini CLI, Cursor, and 9 other AI coding agents. The collection covers engineering, marketing, security, compliance, C-level advisory, and more. This is the most comprehensive open-source library of its kind, significantly lowering the barrier for teams to adopt AI coding agents across diverse domains. It enables non-engineers (e.g., marketers, compliance officers) to leverage AI agents with domain-specific expertise, potentially accelerating enterprise AI adoption. The repository includes 593 CLI scripts (stdlib-only, no pip installs), 711 reference templates, and 102 custom commands. It supports 13 platforms natively or via conversion scripts, and has earned over 5,200 GitHub stars.

rss · GitHub Trending - Python · Jul 5, 22:57

**Background**: AI coding agents like Claude Code and Codex can execute commands and generate code, but they lack built-in domain-specific knowledge. Skills (or plugins) are modular instruction packages that provide structured instructions, workflows, and decision frameworks to fill this gap. This repository aggregates such skills for a wide range of use cases.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/alirezarezvani/claude-skills">GitHub - alirezarezvani/claude-skills: 337 Claude Code skills & agent skills & plugins (30+ Agents, 70+ custom commands, 330+ skills, customizable references, scripts)for Claude Code, Codex, Gemini CLI, Cursor, and 8 more coding agents — engineering, marketing, product, compliance, C-level advisory, research, business operations, commercial & finance, and your daily productivity skills.</a></li>
<li><a href="https://code.claude.com/docs/en/skills">Extend Claude with skills - Claude Code Docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Answer_Engine_Optimization">Answer Engine Optimization</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#Claude Code`, `#plugins`, `#open-source`, `#productivity`

---

<a id="item-6"></a>
## [Google Releases ADK 2.0: Open-Source Python Toolkit for AI Agents](https://github.com/google/adk-python) ⭐️ 8.0/10

Google has released ADK 2.0, an open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents. The update introduces a Workflow Runtime for graph-based execution and a Task API for structured agent-to-agent delegation. This release from a major player like Google provides developers with a flexible, code-first framework to build production-grade AI agents, potentially accelerating adoption of agentic AI in enterprise applications. The open-source nature and multi-language support (Python, TypeScript, Go, Java, Kotlin) lower barriers for developers. ADK 2.0 includes breaking changes from version 1.x, affecting the agent API, event model, and session schema. Sessions generated by ADK 2.0 are readable by ADK 1.28+ but incompatible with older 1.x versions. The toolkit requires Python 3.10+ and can be installed via pip.

rss · GitHub Trending - Python · Jul 5, 22:57

**Background**: AI agents are autonomous programs that can perform tasks, make decisions, and interact with users or other systems. ADK is Google's open-source framework for building such agents, offering a code-first approach that gives developers fine-grained control. The 2.0 version adds workflow orchestration and task delegation capabilities, making it suitable for complex multi-agent systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/google/adk-python">GitHub - google/adk-python: An open-source, code-first Python toolkit for building, evaluating, and deploying sophisticated AI agents with flexibility and control. · GitHub</a></li>
<li><a href="https://adk.dev/2.0/">Welcome to ADK 2.0 - Agent Development Kit (ADK)</a></li>
<li><a href="https://adk.dev/">Agent Development Kit (ADK)</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#Python`, `#open-source`, `#Google`, `#toolkit`

---

<a id="item-7"></a>
## [Hugging Face Launches Modular Speech-to-Speech Pipeline](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face released an open-source speech-to-speech pipeline that combines VAD, STT, LLM, and TTS into a modular, low-latency voice agent, exposed via an OpenAI Realtime-compatible WebSocket API. This pipeline enables developers to build fully local, open-source voice agents with swappable components, reducing reliance on proprietary APIs and fostering innovation in voice AI. The pipeline uses Parakeet TDT for local STT, an OpenAI-compatible LLM, and Qwen3-TTS for speech output, and supports any OpenAI Realtime-compatible client. It is already in production for thousands of Reachy Mini robots.

rss · GitHub Trending - Python · Jul 5, 22:57

**Background**: Voice agents typically use a pipeline of VAD (Voice Activity Detection), STT (Speech-to-Text), LLM (Large Language Model), and TTS (Text-to-Speech). Hugging Face's offering modularizes each step, allowing developers to swap components easily and run everything locally with open-source models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huggingface/speech-to-speech">GitHub - huggingface/speech-to-speech: Build local voice agents with open-source models · GitHub</a></li>
<li><a href="https://livekit.com/blog/voice-agent-architecture-stt-llm-tts-pipelines-explained">Voice Agent Architecture: STT , LLM, and TTS Pipelines ... | LiveKit</a></li>
<li><a href="https://docs.runanywhere.ai/web/voice-agent">Voice Pipeline - RunAnywhere Documentation</a></li>

</ul>
</details>

**Tags**: `#speech-to-speech`, `#voice agents`, `#open-source`, `#Hugging Face`, `#AI pipeline`

---