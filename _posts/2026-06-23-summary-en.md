---
layout: default
title: "Horizon Summary: 2026-06-23 (EN)"
date: 2026-06-23
lang: en
---

> From 69 items, 19 important content pieces were selected

---

1. [AI Industry Faces Affordability Crisis](#item-1) ⭐️ 8.0/10
2. [Baidu's Unlimited OCR Enables One-Shot Long Document Parsing](#item-2) ⭐️ 8.0/10
3. [The Coming Loop: AI Coding Needs Clear Specs](#item-3) ⭐️ 8.0/10
4. [Google Fires Employee for Creating Workspace CLI Tool](#item-4) ⭐️ 8.0/10
5. [Anthropic Launches Claude Tag: Multiplayer AI Agent for Slack](#item-5) ⭐️ 8.0/10
6. [LLM Prompt Injection Traced to Role Confusion](#item-6) ⭐️ 8.0/10
7. [Porting Moebius 0.2B Inpainting Model to Browser with WebGPU](#item-7) ⭐️ 8.0/10
8. [OpenMontage: First Open-Source Agentic Video Production System](#item-8) ⭐️ 8.0/10
9. [Open-Source Library of 817 Cybersecurity Skills for AI Agents](#item-9) ⭐️ 8.0/10
10. [Penpot: Open-Source Design Tool Gains DPG Status](#item-10) ⭐️ 8.0/10
11. [Stirling-PDF: Open-Source Self-Hosted PDF Platform](#item-11) ⭐️ 8.0/10
12. [Garry Tan's gstack: 23 AI tools to ship like a full team](#item-12) ⭐️ 8.0/10
13. [ByteDance Open-Sources DeerFlow 2.0 SuperAgent Framework](#item-13) ⭐️ 8.0/10
14. [Codebase-Memory-MCP: Sub-ms Code Queries via Knowledge Graph](#item-14) ⭐️ 8.0/10
15. [AirLLM Runs 70B LLMs on Single 4GB GPU](#item-15) ⭐️ 8.0/10
16. [Ultrasound Imaging Gives Robot Hands Human-like Dexterity](#item-16) ⭐️ 8.0/10
17. [Injectable Mini Livers Offer Alternative to Transplantation](#item-17) ⭐️ 8.0/10
18. [First drug to delay type 1 diabetes approved on NHS](#item-18) ⭐️ 8.0/10
19. [Glyphosate may fuel antibiotic-resistant superbugs](#item-19) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [AI Industry Faces Affordability Crisis](https://blog.dshr.org/2026/06/ais-affordability-crisis.html) ⭐️ 8.0/10

A blog post argues that the AI industry is in an affordability crisis driven by venture capital overinvestment and questionable ROI, with token-based pricing causing rapid shifts in enterprise adoption. This analysis challenges the sustainability of current AI business models, suggesting that many enterprises may realize AI offers little ROI, potentially leading to a market correction and reduced investment. The article claims that Anthropic and OpenAI may be subsidizing enterprise customers by up to 40x and 70x respectively, based on Zitron's numbers, though commenters dispute this.

hackernews · ilreb · Jun 23, 15:11 · [Discussion](https://news.ycombinator.com/item?id=48646276)

**Background**: Token-based pricing charges users per unit of AI processing (tokens), similar to API calls. Venture capital has poured billions into AI startups, often subsidizing usage to drive adoption, but critics question whether the technology delivers real business value.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.dshr.org/2026/06/ais-affordability-crisis.html">DSHR's Blog: AI's Affordability Crisis</a></li>
<li><a href="https://www.zenskar.com/blog/token-based-pricing">Token-Based Pricing for AI Products: The CFO's Guide 2026 | Zenskar</a></li>
<li><a href="https://fortune.com/2025/05/27/ai-venture-capital-bain-capital-ventures-cloud-computing-saas-openai-anthropic-venture-capital-opus-motive-partners/">AI-scaled startups are poised to disrupt the venture capital ...</a></li>

</ul>
</details>

**Discussion**: Commenters express skepticism about AI ROI, with some comparing the situation to Enron and predicting a market crash. Others note that token pricing has led to sudden shifts in enterprise behavior, with companies now monitoring and restricting AI usage.

**Tags**: `#AI`, `#economics`, `#venture capital`, `#industry analysis`

---

<a id="item-2"></a>
## [Baidu's Unlimited OCR Enables One-Shot Long Document Parsing](https://github.com/baidu/Unlimited-OCR) ⭐️ 8.0/10

Baidu released Unlimited OCR, a 3B-parameter model that uses a novel Recurrent Sliding Window Attention (R-SWA) mechanism to keep the KV cache fixed during long-document OCR, enabling one-shot parsing of hundreds of pages without memory overflow. This innovation removes the need to manually split long PDFs into pages, drastically simplifying OCR pipelines and making long-horizon document parsing practical for the first time. It could accelerate digitization of books, archives, and other lengthy documents. The model is released under the MIT license and supports both single-image and multi-page PDF processing. It uses a base size of 1024 pixels and can be configured with 'gundam' or 'base' modes for different trade-offs between speed and accuracy.

hackernews · ingve · Jun 23, 11:35 · [Discussion](https://news.ycombinator.com/item?id=48643426)

**Background**: Transformer-based OCR models use a KV cache to store previously computed key-value pairs, which grows linearly with the number of tokens processed. For long documents, this cache quickly exhausts GPU memory, forcing developers to split documents into small chunks. Unlimited OCR's R-SWA mechanism compresses the cache to a fixed size, enabling continuous processing of arbitrarily long inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2606.23050">Unlimited OCR Works Welcome the Era of One-shot Long-horizon Parsing Baidu Inc.</a></li>
<li><a href="https://github.com/baidu/Unlimited-OCR">GitHub - baidu/Unlimited-OCR: Unlimited OCR Works: Welcome the Era of One-shot Long-horizon Parsing. · GitHub</a></li>
<li><a href="https://aiweekly.co/alerts/baidu-releases-mit-licensed-3b-ocr-model-for-long-documents">Baidu Releases MIT-Licensed 3B OCR Model for Long Documents | AI Weekly</a></li>

</ul>
</details>

**Discussion**: The community praised the approach as a clever architectural hack to prevent memory hoarding, and noted its potential for niche applications like optical music recognition. Some commenters also appreciated the acknowledgment of DeepSeek-OCR and PaddleOCR in the paper.

**Tags**: `#OCR`, `#AI`, `#memory optimization`, `#deep learning`, `#NLP`

---

<a id="item-3"></a>
## [The Coming Loop: AI Coding Needs Clear Specs](https://lucumr.pocoo.org/2026/6/23/the-coming-loop/) ⭐️ 8.0/10

The article reflects on the iterative 'loop' in AI-assisted software development, arguing that clear human-written specifications are essential before leveraging AI agents effectively. This discussion highlights a critical bottleneck in AI-assisted coding: the need for human clarity and specification writing, which challenges the narrative that AI can fully automate software development. The author notes that even with advanced agents, developers often need 5-6 failed iterations to understand what they want, and that AI cannot replace the human thinking time required for clarity.

hackernews · ingve · Jun 23, 11:06 · [Discussion](https://news.ycombinator.com/item?id=48643180)

**Background**: AI-assisted coding tools like GitHub Copilot and Claude Code use large language models to generate code from prompts. However, generating complex, maintainable code often requires precise specifications, a skill that remains human-dependent.

**Discussion**: Commenters agree that specification writing is a bottleneck; one user notes that agents perform well when given a clear spec, but the burden of writing specs falls on the human. Another highlights that excessive null checking generated by AI can be harmful.

**Tags**: `#AI-assisted development`, `#software engineering`, `#LLMs`, `#coding workflows`, `#spec-driven development`

---

<a id="item-4"></a>
## [Google Fires Employee for Creating Workspace CLI Tool](https://twitter.com/JPoehnelt/status/2069482265953087602) ⭐️ 8.0/10

Google employee Justin Poehnelt was fired for creating and releasing a Google Workspace CLI tool on GitHub, which was later adopted as an official project by Google. This incident highlights tensions between employee initiative and corporate bureaucracy, raising questions about how companies handle unsanctioned but valuable contributions. The CLI tool, built in Rust, provides a unified interface for Google Workspace services like Drive, Gmail, and Calendar, and was dynamically built from Google Discovery Service.

hackernews · justinwp · Jun 23, 18:13 · [Discussion](https://news.ycombinator.com/item?id=48649011)

**Background**: Google has a history of encouraging side projects through its '20% time' policy, but also has strict policies regarding open source releases that may conflict with company interests. The fired employee's tool was initially personal but later became an official Google project, suggesting the termination was about process rather than value.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/googleworkspace/cli">GitHub - googleworkspace/cli: Google Workspace CLI — one command-line ...</a></li>
<li><a href="https://www.infoq.com/news/2026/06/google-workspace-cli/">Google Workspace CLI: Unified Command-Line Tool Built for ... - InfoQ</a></li>
<li><a href="https://opensource.google/documentation/policies/overview">Google Open Source Policies</a></li>

</ul>
</details>

**Discussion**: Community comments are divided: some argue the employee showed poor judgment by releasing a tool that could be mistaken for official, while others criticize Google's bureaucracy and lament the loss of the '20% time' culture. A few reference Pournelle's Iron Law of Bureaucracy to describe the situation.

**Tags**: `#Google`, `#CLI`, `#bureaucracy`, `#employment`, `#open source`

---

<a id="item-5"></a>
## [Anthropic Launches Claude Tag: Multiplayer AI Agent for Slack](https://www.anthropic.com/news/introducing-claude-tag) ⭐️ 8.0/10

Anthropic has introduced Claude Tag, an always-on AI agent that lives in Slack and acts as a collaborative teammate, available in beta for Claude Enterprise and Team customers. It learns from channel conversations and maintains a single identity across the company, enabling multi-user collaboration. Claude Tag represents a significant step in agentic AI for enterprise collaboration, moving beyond single-user chatbots to a persistent, shared AI teammate. This could reshape how teams work in Slack, but raises important questions about token costs, security, and permission alignment. Claude Tag is multiplayer, meaning one Claude interacts with everyone in a given Slack channel, allowing anyone to see its work and continue conversations. Anthropic reports that 65% of their product team's code is created by an internal version of Claude Tag.

hackernews · adocomplete · Jun 23, 17:09 · [Discussion](https://news.ycombinator.com/item?id=48648039)

**Background**: AI agents are partially autonomous systems that can operate independently over extended periods using various tools. Slack has been integrating AI agents through platforms like Agentforce and Slackbot's MCP client, but Claude Tag is unique in its persistent, shared identity across an entire company.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/23/anthropics-claude-tag-is-learning-your-company-one-slack-message-at-a-time/">Anthropic’s Claude Tag is learning your company, one Slack message at a time | TechCrunch</a></li>
<li><a href="https://www.anthropic.com/news/introducing-claude-tag">Introducing Claude Tag \ Anthropic</a></li>
<li><a href="https://fortune.com/2026/06/23/anthropic-claude-tag-virtual-employee-tool-slack/">Anthropic releases Claude Tag, a virtual employee that works within Slack | Fortune</a></li>

</ul>
</details>

**Discussion**: Community comments express excitement about the multiplayer collaboration aspect but raise concerns about token consumption, enterprise security, and Claude's ability to distinguish what to learn. Some users note that permission alignment and memory management remain significant challenges.

**Tags**: `#AI agents`, `#enterprise AI`, `#Slack integration`, `#Anthropic`, `#collaboration`

---

<a id="item-6"></a>
## [LLM Prompt Injection Traced to Role Confusion](https://simonwillison.net/2026/Jun/22/prompt-injection-as-role-confusion/#atom-everything) ⭐️ 8.0/10

Researchers Charles Ye, Jasmine Cui, and Dylan Hadfield-Menell published a paper showing that LLMs suffer from 'role confusion': they infer the source of text from its style rather than its role tag, making prompt injection fundamentally difficult to defend against. This research confirms a fundamental limitation of current LLMs, implying that prompt injection defenses will remain a 'whack-a-mole game' unless models achieve genuine role perception. It also reveals a new jailbreak vector where style overrides content, enabling attacks that are nearly invisible to humans. The researchers introduced 'destyling'—rewriting text in a slightly different style—which reduced attack success from 61% to 10% on their dataset. They also developed a zero-shot attack called CoT Forgery that injects fabricated chain-of-thought reasoning to confuse the model.

rss · Simon Willison · Jun 22, 23:59

**Background**: Prompt injection is a security vulnerability where malicious inputs manipulate an LLM's behavior, often bypassing safety filters. Role tags like <system> and <user> are used to separate privileged instructions from untrusted input, but this research shows models rely on stylistic cues rather than these tags.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.12277">[2603.12277] Prompt Injection as Role Confusion - arXiv.org When AI Exposes Role Confusion in the Organization The Hidden Cost of AI Adoption: Identity Drift, Role ... When AI Exposes Role Confusion in the Organization Prompt Injection as Role Confusion Why Role Conflicts Hijack Your AI - And How to Reclaim Control Researchers Demonstrate Prompt Injection as Role Confusion</a></li>
<li><a href="https://genai.owasp.org/llmrisk/llm01-prompt-injection/">LLM01:2025 Prompt Injection - OWASP Gen AI Security Project</a></li>
<li><a href="https://owasp.org/www-community/attacks/PromptInjection">Prompt Injection - OWASP Foundation</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (linked in the article) likely includes comments praising the blog-style writeup and discussing the implications for LLM security, though specific comments are not provided here.

**Tags**: `#prompt injection`, `#LLM security`, `#jailbreak`, `#AI safety`

---

<a id="item-7"></a>
## [Porting Moebius 0.2B Inpainting Model to Browser with WebGPU](https://simonwillison.net/2026/Jun/22/porting-moebius/#atom-everything) ⭐️ 8.0/10

Simon Willison successfully ported the Moebius 0.2B image inpainting model to run entirely in a web browser using WebGPU, and released a working demo at simonw.github.io/moebius-web/. The port was achieved with the help of Claude Code, using ONNX Runtime Web on the WebGPU backend. This makes a state-of-the-art lightweight inpainting model accessible to anyone with a modern browser, eliminating the need for expensive NVIDIA GPUs or complex Python setups. It demonstrates the growing feasibility of running sophisticated machine learning models directly in the browser, which could democratize AI-powered image editing tools. The original Moebius model required PyTorch and NVIDIA CUDA, but Willison used ONNX Runtime Web with the WebGPU backend to run inference in-browser. The model has only 0.2 billion parameters yet claims performance comparable to 10B+ parameter models like FLUX.1-Fill-Dev, with over 15x inference acceleration.

rss · Simon Willison · Jun 22, 23:43

**Background**: Image inpainting is a technique where missing or unwanted regions of an image are filled in by a model that generates plausible content. Moebius is a lightweight inpainting framework that achieves high-quality results with only 0.2 billion parameters. WebGPU is a modern browser API that allows web applications to access the GPU for accelerated computation, enabling machine learning inference in the browser without server-side processing.

<details><summary>References</summary>
<ul>
<li><a href="https://hustvl.github.io/Moebius/">Moebius Project Page</a></li>
<li><a href="https://simonwillison.net/2026/Jun/22/porting-moebius/">Porting the Moebius 0.2B image inpainting model to run in the browser with Claude Code</a></li>
<li><a href="https://github.com/hustvl/Moebius">GitHub - hustvl/Moebius: [ECCV 2026] Moebius: 0.2B Lightweight Image Inpainting Framework with 10B-Level Performance · GitHub</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (referenced in the article) likely praised the practical demo and the clever use of Claude Code for porting. Some commenters may have discussed the trade-offs of running models in-browser versus on dedicated hardware, and the implications for privacy and accessibility.

**Tags**: `#machine learning`, `#webgpu`, `#image inpainting`, `#browser`, `#porting`

---

<a id="item-8"></a>
## [OpenMontage: First Open-Source Agentic Video Production System](https://github.com/calesthio/OpenMontage) ⭐️ 8.0/10

OpenMontage, the first open-source agentic video production system, has been released with 12 pipelines, 52 tools, and over 500 agent skills, allowing users to turn an AI coding assistant into a full video production studio. This system democratizes professional video production by enabling natural language-driven creation, potentially disrupting the video editing industry similar to how Cursor transformed coding. OpenMontage can produce real video videos using free stock footage and open archives, not just image-based animations, and includes features like cinematic trailers and animated shorts as examples.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Agentic video production refers to AI systems that autonomously handle multiple steps of video creation, from scripting to editing. OpenMontage is the first open-source system of its kind, contrasting with proprietary solutions like ViMax.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/calesthio/OpenMontage">GitHub - calesthio/OpenMontage: World's first open-source, agentic video production system. 12 pipelines, 52 tools, 500+ agent skills. Turn your AI coding assistant into a full video production studio. · GitHub</a></li>
<li><a href="https://pyshine.com/OpenMontage-Agentic-Video-Production-System/">OpenMontage - Agentic Video Production System with 12 Pipelines and 500+ Skills | PyShine</a></li>
<li><a href="https://a16z.com/its-time-for-agentic-video-editing/">It's time for agentic video editing | Andreessen Horowitz</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#video production`, `#AI agents`, `#agentic systems`

---

<a id="item-9"></a>
## [Open-Source Library of 817 Cybersecurity Skills for AI Agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

A new open-source library, Anthropic Cybersecurity Skills, provides 817 structured cybersecurity skills for AI agents, mapped to six major frameworks including MITRE ATT&CK, NIST CSF 2.0, and MITRE ATLAS, and compatible with over 26 AI platforms. This library standardizes and democratizes cybersecurity expertise for AI agents, enabling automated security tasks across multiple platforms and frameworks, which could accelerate AI-driven security automation and reduce manual effort. The library covers 29 security domains, uses the agentskills.io standard, and is licensed under Apache 2.0. It works with Claude Code, GitHub Copilot, Codex CLI, Cursor, Gemini CLI, and 20+ other platforms.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: AI agents are increasingly used for cybersecurity tasks, but they often lack structured, reusable skill definitions. Frameworks like MITRE ATT&CK and NIST CSF provide taxonomies for threats and defenses, while the agentskills.io standard defines how to package capabilities for AI agents. This library bridges these by offering pre-built, framework-aligned skills.

<details><summary>References</summary>
<ul>
<li><a href="https://atlas.mitre.org/">MITRE ATLAS™</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-10"></a>
## [Penpot: Open-Source Design Tool Gains DPG Status](https://github.com/penpot/penpot) ⭐️ 8.0/10

Penpot, an open-source design platform for design and code collaboration, has been recognized as a Digital Public Good (DPG) by the Digital Public Goods Alliance. This recognition validates Penpot as a free, open alternative to proprietary tools like Figma, potentially transforming design workflows by enabling full ownership and self-hosting for teams. Penpot supports real-time collaboration, open standards (SVG, CSS, HTML, JSON), design tokens, and an MCP server for bidirectional code-design workflows.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Digital Public Goods are open-source solutions that meet the DPG Standard, often forming the basis for digital public infrastructure. Penpot is a web-based design tool that allows teams to self-host, ensuring data sovereignty and compliance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_public_goods">Digital public goods - Wikipedia</a></li>
<li><a href="https://github.com/penpot/penpot">GitHub - penpot/penpot: Penpot: The open-source design tool for design and code collaboration · GitHub</a></li>
<li><a href="https://penpot.app/">Penpot: The open-source design platform for teams.</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#design-tool`, `#collaboration`, `#UI/UX`

---

<a id="item-11"></a>
## [Stirling-PDF: Open-Source Self-Hosted PDF Platform](https://github.com/Stirling-Tools/Stirling-PDF) ⭐️ 8.0/10

Stirling-PDF has become the #1 PDF application on GitHub, offering a self-hosted, open-source platform for editing, signing, converting, and automating PDFs locally or in the browser with a private API. This project addresses growing privacy concerns by allowing users to process PDFs without sending documents to external services, making it valuable for individuals and enterprises that require data sovereignty. Stirling-PDF includes over 50 PDF tools, supports no-code automation pipelines, and offers REST APIs for integration. It can be deployed via Docker, as a desktop app, or on Kubernetes.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Traditional PDF editing often relies on cloud services that may compromise privacy. Self-hosted solutions like Stirling-PDF give users full control over their data. The project has gained over 30 million Docker pulls and strong community support.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Stirling-Tools/Stirling-PDF">GitHub - Stirling-Tools/Stirling-PDF: #1 PDF Application on GitHub that lets you edit PDFs on any device anywhere · GitHub</a></li>
<li><a href="https://stirling.com/">Stirling - PDF Processor | 30M+ Downloads</a></li>
<li><a href="https://www.howtogeek.com/how-i-self-host-a-pdf-editor/">I Self-Host a PDF Editor to Save Money and Protect My Privacy</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#PDF`, `#self-hosted`, `#privacy`, `#Docker`

---

<a id="item-12"></a>
## [Garry Tan's gstack: 23 AI tools to ship like a full team](https://github.com/garrytan/gstack) ⭐️ 8.0/10

Garry Tan, CEO of Y Combinator, released gstack, an open-source collection of 23 opinionated Claude Code tools that enable a single developer to act as a full engineering team, including roles like CEO, designer, and QA lead. This setup demonstrates a paradigm shift where AI-assisted solo developers can match or exceed the output of traditional teams, potentially reshaping how startups and small teams build software. Tan claims his 2026 logical code change rate is ~810× his 2013 pace, with 1,237 GitHub contributions in 2026 vs. 772 in all of 2013. The tools are all MIT-licensed, free, and work as slash commands in Claude Code.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Claude Code is an AI coding agent by Anthropic that reads codebases, edits files, and runs commands via natural language. Andrej Karpathy recently claimed he hasn't typed code since December 2025, inspiring Tan to share his setup. OpenClaw, a solo-built project with 247K GitHub stars, further illustrates this trend.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/garrytan/gstack">GitHub - garrytan/gstack: Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://en.wikipedia.org/wiki/OpenClaw">OpenClaw - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#developer tools`, `#Claude Code`, `#solo development`, `#Y Combinator`

---

<a id="item-13"></a>
## [ByteDance Open-Sources DeerFlow 2.0 SuperAgent Framework](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

ByteDance released DeerFlow 2.0, a ground-up rewrite of its open-source SuperAgent framework, on GitHub on February 28, 2026, where it quickly reached #1 on GitHub Trending. DeerFlow 2.0 addresses the challenge of long-horizon tasks in AI agents by combining sandboxes, memory, tools, and subagents, making it a significant contribution to the open-source AI agent ecosystem. DeerFlow 2.0 is a complete rewrite with no shared code from v1, and it supports extensible skills, subagents, memory, and sandboxes. It recommends using models like Doubao-Seed-2.0-Code, DeepSeek v3.2, and Kimi 2.5.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Long-horizon tasks require AI agents to perform many sequential steps, often taking minutes to hours. DeerFlow is a super agent harness that orchestrates sub-agents, memory, and sandboxes to handle such tasks, building on the concept of agentic AI frameworks.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bytedance/deer-flow">GitHub - bytedance/deer-flow: An open-source long-horizon ...</a></li>
<li><a href="https://deerflow.tech/">DeerFlow</a></li>
<li><a href="https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/">Measuring AI Ability to Complete Long Tasks - METR</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Open Source`, `#Autonomous Systems`, `#ByteDance`, `#Long-Horizon Tasks`

---

<a id="item-14"></a>
## [Codebase-Memory-MCP: Sub-ms Code Queries via Knowledge Graph](https://github.com/DeusData/codebase-memory-mcp) ⭐️ 8.0/10

DeusData released codebase-memory-mcp, a high-performance MCP server that indexes entire codebases into a persistent knowledge graph, enabling sub-millisecond structural queries across 158 languages. It can index the Linux kernel (28M LOC) in 3 minutes and ships as a single static binary with zero dependencies. This tool dramatically reduces token usage and tool calls for AI coding agents, improving efficiency and accuracy in code understanding. By providing a persistent knowledge graph, it enables faster and more context-aware code exploration, potentially transforming how AI assistants interact with large codebases. The server uses tree-sitter AST analysis for all 158 languages, with Hybrid LSP semantic type resolution for 11 major languages. It provides 14 MCP tools and has been evaluated on 31 real-world repositories, achieving 83% answer quality with 10× fewer tokens and 2.1× fewer tool calls compared to file-by-file exploration.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: MCP (Model Context Protocol) is a protocol that allows AI agents to interact with external tools and data sources. Code intelligence tools traditionally rely on file-by-file exploration, which is token-inefficient and slow for large codebases. Knowledge graphs provide a structured representation of code entities and their relationships, enabling efficient querying.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://github.com/colbymchenry/codegraph">GitHub - colbymchenry/codegraph: Pre-indexed code knowledge ...</a></li>
<li><a href="https://github.com/CodeGraphContext/CodeGraphContext">GitHub - CodeGraphContext/CodeGraphContext: An MCP server ...</a></li>

</ul>
</details>

**Tags**: `#code intelligence`, `#MCP`, `#knowledge graph`, `#developer tools`, `#performance`

---

<a id="item-15"></a>
## [AirLLM Runs 70B LLMs on Single 4GB GPU](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

AirLLM is an open-source framework that enables inference of large language models up to 405B parameters on a single GPU with as little as 4GB VRAM, without using quantization, pruning, or distillation. This breakthrough dramatically lowers the hardware barrier for running state-of-the-art LLMs, making them accessible to individual developers and researchers with consumer-grade GPUs, which could accelerate innovation and democratize AI. AirLLM achieves this through layer-wise streaming and optimized memory management, loading only the active layer into GPU memory at a time. It supports models like Llama 3.1 405B on 8GB VRAM and Llama 3 70B on 4GB VRAM, and also offers optional 8-bit/4-bit quantization for further memory savings.

rss · GitHub Trending - Daily (All) · Jun 23, 23:02

**Background**: Large language models typically require multiple high-end GPUs with large VRAM (e.g., 80GB A100s) for inference due to their massive parameter counts. Traditional methods to reduce memory usage, such as quantization, pruning, and distillation, often degrade model quality. AirLLM takes a different approach by streaming model layers between CPU and GPU, trading some latency for drastically reduced GPU memory requirements.

<details><summary>References</summary>
<ul>
<li><a href="https://deepwiki.com/lyogavin/airllm/5.1-memory-management">Memory Management | lyogavin/airllm | DeepWiki</a></li>
<li><a href="https://deepwiki.com/0xSojalSec/airllm/3.3-memory-optimization-techniques">Memory Optimization Techniques | 0xSojalSec/airllm | DeepWiki</a></li>
<li><a href="https://manjeet.info/blog/airllm-run-large-language-models-low-memory-gpu">AirLLM Explained: Run Large Language Models on Low-Memory ...</a></li>

</ul>
</details>

**Tags**: `#LLM inference`, `#GPU optimization`, `#open source`, `#machine learning`, `#efficiency`

---

<a id="item-16"></a>
## [Ultrasound Imaging Gives Robot Hands Human-like Dexterity](https://www.technologyreview.com/2026/06/23/1138279/ultrasound-imaging-turns-a-robot-hand-into-a-skillful-mimic/) ⭐️ 8.0/10

Researchers have developed a wearable ultrasound wristband that captures real-time images of hand muscles and tendons, allowing a robot hand to mimic human movements with unprecedented accuracy. This breakthrough addresses a key challenge in robotics—replicating human hand dexterity—and could significantly advance prosthetics, human-robot interaction, and virtual reality applications. The ultrasound wristband uses AI to interpret tendon movements like 'puppet strings,' enabling continuous, high-resolution tracking without the limitations of camera-based or glove-based systems.

rss · MIT Technology Review · Jun 23, 21:00

**Background**: Human hands are incredibly complex, with 34 muscles, 27 joints, and over 100 tendons. Previous robotic hands struggled to mimic dexterity because capturing internal movements non-invasively was difficult. Ultrasound imaging offers a non-invasive way to see inside the hand in real time.

<details><summary>References</summary>
<ul>
<li><a href="https://neurosciencenews.com/ultrasound-wristband-hand-tracking-30408/">Ultrasound Wristband Translates Muscle "Strings" into Robotic ...</a></li>
<li><a href="https://www.technologyreview.com/2026/06/23/1138279/ultrasound-imaging-turns-a-robot-hand-into-a-skillful-mimic/">Ultrasound imaging turns a robot hand into a skillful mimic</a></li>
<li><a href="https://www.sciengine.com/doi/10.1007/s40843-026-4270-8">Ultrasound wrist imaging enables continuous and high ...</a></li>

</ul>
</details>

**Tags**: `#robotics`, `#ultrasound imaging`, `#dexterous manipulation`, `#human-robot interaction`, `#prosthetics`

---

<a id="item-17"></a>
## [Injectable Mini Livers Offer Alternative to Transplantation](https://www.technologyreview.com/2026/06/23/1138285/engineered-mini-livers-could-be-injected-as-an-alternative-to-transplantation/) ⭐️ 8.0/10

Researchers led by Professor Sangeeta Bhatia at MIT have developed injectable mini livers that can grow into functional tissue inside the body, potentially replacing traditional liver transplants for chronic liver disease patients. This breakthrough could address the critical shortage of donor livers and provide a treatment option for patients too weak to undergo transplantation, potentially saving thousands of lives annually. The technology, named BOOST (bioengineered on-demand outgrowth via synthetic biology triggering), uses genetically engineered liver cells and supportive fibroblasts that can be injected and then triggered to grow into functional liver tissue in mice.

rss · MIT Technology Review · Jun 23, 21:00

**Background**: Chronic liver disease affects millions worldwide, and liver transplantation is often the only cure, but donor organs are scarce. Tissue engineering aims to create functional liver tissue in the lab, but previous approaches required surgical implantation of pre-formed constructs. The new injectable approach could simplify delivery and reduce invasiveness.

<details><summary>References</summary>
<ul>
<li><a href="https://www.regmednet.com/implantable-mini-livers-could-transform-liver-disease-treatment/">Implantable Mini-Livers Could Transform Liver Disease Treatment - RegMedNet</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sangeeta_Bhatia">Sangeeta Bhatia - Wikipedia</a></li>
<li><a href="https://www.technologyreview.com/innovator/sangeeta-bhatia/">Sangeeta Bhatia | MIT Technology Review</a></li>

</ul>
</details>

**Tags**: `#biomedical engineering`, `#liver disease`, `#organ transplantation`, `#tissue engineering`, `#regenerative medicine`

---

<a id="item-18"></a>
## [First drug to delay type 1 diabetes approved on NHS](https://www.bbc.co.uk/news/articles/ce8mzd94r76o?at_medium=RSS&at_campaign=rss) ⭐️ 8.0/10

The NHS in England and Wales will offer teplizumab (Tzield), the first drug that can delay the onset of type 1 diabetes by up to three years, for children over eight and adults with stage 2 type 1 diabetes. This marks a paradigm shift in type 1 diabetes care, moving from managing symptoms to delaying disease progression, which can significantly improve patients' quality of life by postponing lifelong insulin dependence. Teplizumab is an immunotherapy that targets the immune system to preserve insulin-producing beta cells; it is approved for use in stage 2 type 1 diabetes, where blood sugar is abnormal but symptoms are not yet present.

rss · BBC Health · Jun 22, 23:44

**Background**: Type 1 diabetes is an autoimmune condition where the immune system attacks insulin-producing beta cells in the pancreas. Patients must take insulin for life. Teplizumab, a monoclonal antibody, was previously approved by the FDA in 2022 and now by NICE for NHS use.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.co.uk/news/articles/ce8mzd94r76o">Teplizumab drug to delay type 1 diabetes to be rolled out on the NHS - BBC News</a></li>
<li><a href="https://www.diabetes.org.uk/about-us/news-and-views/teplizumab-first-treatment-slow-type-1-diabetes-approved-use-nhs">Teplizumab, the first treatment to slow type 1 diabetes, approved for use on the NHS | Diabetes UK</a></li>
<li><a href="https://breakthrought1d.org.uk/news/nice-approves-teplizumab-marking-a-new-era-in-type-1-diabetes-care/">NICE approves teplizumab to treat type 1 diabetes on the NHS</a></li>

</ul>
</details>

**Tags**: `#healthcare`, `#diabetes`, `#immunotherapy`, `#NHS`

---

<a id="item-19"></a>
## [Glyphosate may fuel antibiotic-resistant superbugs](https://www.sciencedaily.com/releases/2026/06/260620100434.htm) ⭐️ 8.0/10

Researchers discovered that highly drug-resistant bacteria from hospitals are also resistant to glyphosate, the active ingredient in the widely used weedkiller Roundup. This finding suggests that agricultural herbicides may be contributing to the spread of antibiotic-resistant superbugs beyond healthcare settings, posing a significant public health risk. The study highlights a potential cross-resistance mechanism where the same genes (e.g., encoding efflux pumps) confer resistance to both glyphosate and antibiotics.

rss · ScienceDaily Health · Jun 23, 11:31

**Background**: Glyphosate is a broad-spectrum herbicide that inhibits the EPSPS enzyme in plants and microorganisms. Antibiotic resistance is a global crisis, and this research links two major selective pressures—herbicides and antibiotics—potentially accelerating the evolution of superbugs.

<details><summary>References</summary>
<ul>
<li><a href="https://journals.asm.org/doi/10.1128/msystems.01482-21">A Glyphosate-Based Herbicide Cross-Selects for Antibiotic ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0048969722051567">Response of microbial antibiotic resistance to pesticides: An ...</a></li>

</ul>
</details>

**Tags**: `#antibiotic resistance`, `#glyphosate`, `#public health`, `#agriculture`, `#microbiology`

---