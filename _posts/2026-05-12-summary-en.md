---
layout: default
title: "Horizon Summary: 2026-05-12 (EN)"
date: 2026-05-12
lang: en
---

> From 92 items, 39 important content pieces were selected

---

1. [TanStack NPM Supply-Chain Compromise Postmortem](#item-1) ⭐️ 9.0/10
2. [UCLA discovers first stroke rehab drug to repair brain damage](#item-2) ⭐️ 9.0/10
3. [AUTOMATIC1111's Stable Diffusion WebUI: The Go-To Interface](#item-3) ⭐️ 9.0/10
4. [Real-Time Multimodal Transformer with Micro-Turns](#item-4) ⭐️ 8.0/10
5. [GitLab Lays Off Staff, Drops CREDIT Values in 'Act 2' Pivot](#item-5) ⭐️ 8.0/10
6. [AI Coding Agents Must Cut Maintenance Costs Proportionally](#item-6) ⭐️ 8.0/10
7. [AI Writing Creates 'Zombie Internet'](#item-7) ⭐️ 8.0/10
8. [Shopify's River: Public Coding Agent as Teaching Workshop](#item-8) ⭐️ 8.0/10
9. [ByteDance Open-Sources Multimodal AI Agent Stack TARS](#item-9) ⭐️ 8.0/10
10. [CloakBrowser: Stealth Chromium That Passes All Bot Tests](#item-10) ⭐️ 8.0/10
11. [Build a ChatGPT-like LLM from Scratch with PyTorch](#item-11) ⭐️ 8.0/10
12. [Agentmemory: Persistent Memory for AI Coding Agents](#item-12) ⭐️ 8.0/10
13. [WeChat 4.x Database Decryptor Extracts Keys from Memory](#item-13) ⭐️ 8.0/10
14. [VLM Reliability Probe Challenges Attention-Confidence Assumption](#item-14) ⭐️ 8.0/10
15. [Auto-Rubric as Reward: Explicit Multimodal Generative Criteria](#item-15) ⭐️ 8.0/10
16. [Embeddings for Preferences, Not Semantics](#item-16) ⭐️ 8.0/10
17. [Free-Energy Framework Distinguishes Capability Elicitation from Creation](#item-17) ⭐️ 8.0/10
18. [MemQ: Q-Learning with Eligibility Traces for Self-Evolving Memory Agents](#item-18) ⭐️ 8.0/10
19. [SkillLens: Hierarchical Skill Reuse for Cost-Efficient LLM Agents](#item-19) ⭐️ 8.0/10
20. [LLMs Learn In-Context via Dual Mechanisms](#item-20) ⭐️ 8.0/10
21. [BaLoRA: Bayesian Low-Rank Adaptation Boosts Accuracy and Uncertainty](#item-21) ⭐️ 8.0/10
22. [Statistical Analysis of KV Cache Quantization Schemes](#item-22) ⭐️ 8.0/10
23. [Sanity Checks for Long-Form Hallucination Detection](#item-23) ⭐️ 8.0/10
24. [LLM Circuits Not Task-Specific, Study Finds](#item-24) ⭐️ 8.0/10
25. [Frozen-Tower Composition for Efficient Multimodal Embeddings](#item-25) ⭐️ 8.0/10
26. [LLM-Based Model Turns Explanations into Action Plans](#item-26) ⭐️ 8.0/10
27. [Sem-ECE: New Calibration Metric for Open-Ended QA](#item-27) ⭐️ 8.0/10
28. [Self-Captioning Boosts Robustness in Vision-Language Models](#item-28) ⭐️ 8.0/10
29. [VT-Bench: First Unified Benchmark for Visual-Tabular Learning](#item-29) ⭐️ 8.0/10
30. [HY-Himmel: Efficient Long Video Understanding via Hierarchical Motion Encoding](#item-30) ⭐️ 8.0/10
31. [WATCH Framework for Month-Level Archaeological Change Detection](#item-31) ⭐️ 8.0/10
32. [MULTITEXTEDIT: Benchmark for Cross-Lingual Text-in-Image Editing](#item-32) ⭐️ 8.0/10
33. [Sinkhorn Treatment Effects: Causal Optimal Transport Measure](#item-33) ⭐️ 8.0/10
34. [Mean-Field Theory Reveals Phase Transitions in Multi-Component ICA](#item-34) ⭐️ 8.0/10
35. [CONTRA: Conformal Prediction with Normalizing Flows](#item-35) ⭐️ 8.0/10
36. [Core-Halo Decomposition for Decentralized Fixed-Point Problems](#item-36) ⭐️ 8.0/10
37. [New Diffusion-Based Method Measures Mode Separation in High Dimensions](#item-37) ⭐️ 8.0/10
38. [Transformers' Approximation Power Proven via Softmax Partition](#item-38) ⭐️ 8.0/10
39. [Tight Generalization Bounds for Noiseless Inverse Optimization](#item-39) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TanStack NPM Supply-Chain Compromise Postmortem](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 9.0/10

TanStack Router's NPM package was compromised via a CI pipeline attack, where an attacker gained access to a GitHub Actions cache and stole a publish token, leading to a malicious payload with a dead-man's switch that wipes the user's home directory if the token is revoked. This incident highlights critical vulnerabilities in CI/CD security and the risks of using long-lived tokens for package publishing, affecting the entire npm ecosystem and potentially thousands of developers who depend on TanStack libraries. The attack exploited GitHub Actions cache poisoning and a postinstall script to execute the payload, which installed a systemd service or LaunchAgent that monitors the stolen token's validity and triggers data destruction upon revocation.

hackernews · varunsharma07 · May 11, 21:08 · [Discussion](https://news.ycombinator.com/item?id=48100706)

**Background**: Supply-chain attacks target the software development pipeline to inject malicious code into trusted packages. NPM packages often use lifecycle scripts like postinstall that run automatically during installation, making them a common vector. CI/CD pipelines with cached dependencies and long-lived tokens are attractive targets for attackers.

<details><summary>References</summary>
<ul>
<li><a href="https://cyberpress.org/84-tanstack-npm-packages-compromised-in-ongoing-supply-chain-attack-targeting-ci-credentials/">84 TanStack npm Packages Compromised in Ongoing Supply-Chain Attack Targeting CI Credentials</a></li>
<li><a href="https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem">TeamPCP's Mini Shai-Hulud Is Back: A Self-Spreading Supply Chain Attack Compromises TanStack npm Packages - StepSecurity</a></li>
<li><a href="https://cyberpress.org/dead-mans-switch-widespread-npm-supply-chain-attack-driving-malware-attacks/">Dead Man’s Switch: Widespread npm Supply Chain Attack Driving ...</a></li>

</ul>
</details>

**Discussion**: Community comments warn about the dead-man's switch that deletes home directories upon token revocation, and discuss the complexity of CI pipeline YAML configurations that can lead to cache poisoning. Some argue that Trusted Publishing alone is insufficient, and highlight that postinstall scripts are dangerous, recommending pnpm as a safer alternative.

**Tags**: `#supply-chain security`, `#npm`, `#CI/CD`, `#open-source`, `#incident response`

---

<a id="item-2"></a>
## [UCLA discovers first stroke rehab drug to repair brain damage](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

UCLA researchers have identified the first drug candidate for stroke rehabilitation that targets the disconnection of brain cells remote from the stroke lesion, restoring lost connections and function in surviving networks. The compound, a parvalbumin neuron modulator, was tested in mice and showed significant recovery of motor and cognitive functions. Stroke is the leading cause of adult disability, and currently no drugs exist for stroke recovery—only physical rehabilitation. This breakthrough could transform stroke treatment by enabling pharmacological repair of brain connections, potentially improving outcomes for millions of patients worldwide. The drug specifically targets parvalbumin neurons, which are crucial for maintaining brain rhythms and connections after stroke. The study was published in a peer-reviewed journal, and the compound is identified as a potential first-in-class stroke rehabilitation drug, though it has only been tested in mice so far.

hackernews · bookofjoe · May 11, 17:53 · [Discussion](https://news.ycombinator.com/item?id=48098261)

**Background**: A stroke occurs when blood supply to part of the brain is interrupted, causing brain cell death in the affected area. However, surviving brain cells can become 'bruised' and lose connections with distant networks, leading to persistent disability. Until now, no drug has been able to repair these lost connections; rehabilitation relies on physical therapy and neuroplasticity.

<details><summary>References</summary>
<ul>
<li><a href="https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage">UCLA discovers first stroke rehabilitation drug to repair brain damage</a></li>
<li><a href="https://www.uclahealth.org/news/release/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain">UCLA discovers first stroke rehabilitation drug to repair brain damage in mice | UCLA Health</a></li>
<li><a href="https://newsroom.ucla.edu/releases/ucla-discovers-first-stroke-rehabilitation-drug-to-reestablish-brain-connections-in-mice">UCLA discovers first stroke rehabilitation drug to reestablish brain connections in mice | UCLA</a></li>

</ul>
</details>

**Discussion**: Commenters clarified that the drug targets disconnection of surviving brain cells, not cell death at the stroke core, which remains irreversible. Some expressed excitement about the potential for Alzheimer's disease, while others referenced science fiction stories like Ted Chiang's 'Understand' to highlight the dramatic implications.

**Tags**: `#neuroscience`, `#stroke`, `#drug discovery`, `#brain repair`, `#medical breakthrough`

---

<a id="item-3"></a>
## [AUTOMATIC1111's Stable Diffusion WebUI: The Go-To Interface](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ⭐️ 9.0/10

The AUTOMATIC1111/stable-diffusion-webui repository provides a comprehensive Gradio-based web interface for Stable Diffusion, featuring txt2img, img2img, inpainting, outpainting, and many advanced options like attention control, textual inversion, and upscaling. This web UI has become the de facto standard for interacting with Stable Diffusion, democratizing AI image generation for artists, hobbyists, and researchers. Its extensive feature set and active development have shaped the AI art community's workflow. The UI supports 4GB VRAM (and reportedly 2GB), includes one-click install scripts, and saves generation parameters in PNG/EXIF metadata. It also offers a negative prompt, styles, X/Y/Z plot, and live preview with minimal VRAM usage.

rss · GitHub Trending - Daily (All) · May 12, 14:31

**Background**: Stable Diffusion is a latent text-to-image diffusion model that generates images from text descriptions. Gradio is an open-source Python library for quickly creating web UIs for machine learning models. This web UI bundles these technologies into an accessible tool.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gradio.app/">Gradio</a></li>
<li><a href="https://stable-diffusion-art.com/outpainting/">How to use outpainting to extend images - Stable Diffusion Art</a></li>

</ul>
</details>

**Tags**: `#stable-diffusion`, `#AI-art`, `#image-generation`, `#machine-learning`, `#open-source`

---

<a id="item-4"></a>
## [Real-Time Multimodal Transformer with Micro-Turns](https://thinkingmachines.ai/blog/interaction-models/) ⭐️ 8.0/10

A blog post and demos from Thinking Machines AI showcase a transformer-based model that processes text, image, and audio input and produces text and audio output in near real-time using time-aligned micro-turns of 200ms each. This novel interaction model enables continuous, interleaved input and output, making human-AI conversations feel more natural and responsive, which could transform applications like virtual assistants, customer service, and accessibility tools. The architecture is a multimodal transformer trained jointly on text, image, and audio, operating in micro-turns of 200ms input processing and 200ms output generation, enabling near real-time interaction.

hackernews · smhx · May 11, 20:53 · [Discussion](https://news.ycombinator.com/item?id=48100524)

**Background**: Traditional AI models process a complete input (e.g., a full sentence) before generating a response, causing delays. This model uses time-aligned micro-turns, continuously interleaving small chunks of input and output, similar to how humans pause and react during conversation.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_learning">Multimodal learning - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/multimodal-transformer-models">Multimodal Transformer Models</a></li>

</ul>
</details>

**Discussion**: Commenters were impressed by the natural pauses and real-time behavior, with some calling it a breakthrough for interactive AI. However, concerns were raised about potential misuse in surveillance, and some felt the demos were contrived and lacked clear commercial applications.

**Tags**: `#AI`, `#machine learning`, `#real-time interaction`, `#transformer`, `#multimodal`

---

<a id="item-5"></a>
## [GitLab Lays Off Staff, Drops CREDIT Values in 'Act 2' Pivot](https://about.gitlab.com/blog/gitlab-act-2/) ⭐️ 8.0/10

GitLab announced a workforce reduction and the retirement of its CREDIT values framework, framing the changes as a strategic pivot to capitalize on the 'agentic era' in software development. This move signals a major shift at a leading DevOps company, potentially affecting thousands of developers and the broader DevSecOps ecosystem, while raising questions about the true motivations behind AI-driven corporate restructuring. GitLab's stock price has dropped 50% over the past year, from ~$52 to $26, and the company is retiring its CREDIT values (Collaboration, Results, Efficiency, Diversity, Iteration, Transparency) as part of 'GitLab Act 2'.

hackernews · AnonGitLabEmpl · May 11, 20:51 · [Discussion](https://news.ycombinator.com/item?id=48100500)

**Background**: GitLab is a major DevOps platform used for software development, CI/CD, and security. Its CREDIT values were a core part of its corporate culture, guiding how teams operated. The 'agentic era' refers to a trend where AI agents autonomously perform tasks, which GitLab claims will increase demand for software.

<details><summary>References</summary>
<ul>
<li><a href="https://about.gitlab.com/blog/gitlab-act-2/">GitLab Act 2</a></li>
<li><a href="https://news.ycombinator.com/item?id=48100500">GitLab Announces Workforce Reduction and End of Their CREDIT Values | Hacker News</a></li>
<li><a href="https://docs.gitlab.com/subscriptions/gitlab_credits/">GitLab Credits and usage billing | GitLab Docs</a></li>

</ul>
</details>

**Discussion**: Community comments are skeptical: one user notes GitLab's stock is down 50% in 12 months, suggesting the AI pivot may be a response to investor pressure. Another questions how reducing resources aligns with claiming the 'largest opportunity ever'. Others criticize GitLab's product roadmap and long-unresolved issues.

**Tags**: `#GitLab`, `#layoffs`, `#AI strategy`, `#DevOps`, `#corporate culture`

---

<a id="item-6"></a>
## [AI Coding Agents Must Cut Maintenance Costs Proportionally](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 8.0/10

James Shore argues that AI coding agents must reduce maintenance costs in proportion to productivity gains, otherwise teams face unsustainable technical debt. He presents a mathematical model showing that doubling code output without halving maintenance costs quadruples total maintenance burden. This insight highlights a critical blind spot in the AI-assisted coding boom: faster code generation without corresponding maintenance cost reduction leads to exponential debt. It forces teams and tool vendors to prioritize maintainability alongside raw productivity. Shore's argument is mathematically framed: if productivity multiplier is P and maintenance cost multiplier is M, total maintenance burden is P × M. To keep burden constant, M must equal 1/P. He warns that without such reduction, teams trade temporary speed for permanent indenture.

rss · Simon Willison · May 11, 19:48

**Background**: AI coding agents are tools that assist developers in writing, debugging, and optimizing code, often using large language models (LLMs). Technical debt refers to the future cost of maintaining a system due to expedient short-term solutions. Shore's argument connects these concepts, warning that AI-generated code can accumulate debt faster than traditional code if maintenance costs are not addressed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt - Wikipedia</a></li>
<li><a href="https://github.com/resources/articles/what-are-ai-agents">What are AI agents ? · GitHub</a></li>

</ul>
</details>

**Tags**: `#AI-assisted coding`, `#software maintenance`, `#productivity`, `#technical debt`

---

<a id="item-7"></a>
## [AI Writing Creates 'Zombie Internet'](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler published an angry but excellent piece coining the term 'Zombie Internet' to describe how AI-generated writing is polluting the internet and distorting human writing styles. This matters because it highlights a growing mental exhaustion from filtering AI content and warns that AI is not just adding noise but actively reshaping how humans write online, threatening authentic communication. Koebler distinguishes 'Zombie Internet' from the 'Dead Internet' theory: the former involves people interacting with bots and AI agents, not just bots talking to bots. He cites examples like AI influencers, automated YouTube channels, and AI summaries sold as real books.

rss · Simon Willison · May 11, 19:21

**Background**: The 'Dead Internet' theory is a conspiracy theory claiming that since around 2016, most internet content and interactions are generated by bots and algorithms. Koebler's 'Zombie Internet' concept updates this for the AI era, describing a more insidious mix of human and AI activity where people knowingly use AI to create content and interact with others, blurring the line between authentic and synthetic.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>
<li><a href="https://www.fastcompany.com/91489308/zombie-internet-devastating-consequences-advertising-social-media-human-web-dead-internet-moltbook-ai-tbpn">The ‘ zombie internet ’ has arrived—and it has... - Fast Company</a></li>

</ul>
</details>

**Tags**: `#AI`, `#internet culture`, `#content quality`, `#ethics`, `#writing`

---

<a id="item-8"></a>
## [Shopify's River: Public Coding Agent as Teaching Workshop](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything) ⭐️ 8.0/10

Shopify CEO Tobias Lütke revealed that their internal coding agent, River, operates entirely in public Slack channels, refusing direct messages and encouraging open collaboration. This approach turns every coding session into a transparent, searchable, and educational experience for all employees. This model transforms AI-assisted development from a private productivity tool into a shared learning platform, potentially accelerating knowledge transfer and onboarding across the organization. It also sets a precedent for how companies can design AI tools to foster transparency and collective skill-building. River operates in public channels like #tobi_river, where over 100 people can observe, react, and contribute. Lütke describes this as a 'Lehrwerkstatt' (teaching workshop), enabling 'osmosis learning' without formal curriculum or training plans.

rss · Simon Willison · May 11, 15:46

**Background**: AI coding agents like Claude Code and Jules are typically used privately by individual developers. Shopify's approach contrasts by making the agent's work fully visible, drawing inspiration from Midjourney's early public Discord channels where users shared prompts and learned collectively. The German concept of 'Lehrwerkstatt' refers to a workshop where practical skills are taught through hands-on, production-independent learning.

<details><summary>References</summary>
<ul>
<li><a href="https://wirtschaftslexikon.gabler.de/definition/lehrwerkstatt-38603">Lehrwerkstatt • Definition | Gabler Wirtschaftslexikon</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#software engineering`, `#team collaboration`, `#knowledge sharing`, `#Shopify`

---

<a id="item-9"></a>
## [ByteDance Open-Sources Multimodal AI Agent Stack TARS](https://github.com/bytedance/UI-TARS-desktop) ⭐️ 8.0/10

ByteDance has released an open-source multimodal AI agent stack called TARS, which includes two components: Agent TARS, a general multimodal AI agent with CLI and Web UI, and UI-TARS Desktop, a desktop application that provides a native GUI agent based on the UI-TARS vision-language model. This release from a major tech company like ByteDance significantly lowers the barrier for developers and researchers to build and deploy multimodal AI agents that can control computers and browsers through natural language, accelerating innovation in GUI automation and agent-based systems. Agent TARS integrates with MCP tools and supports human-like task completion via multimodal LLMs, while UI-TARS Desktop offers both local and remote computer and browser operators. The stack is fully open-source and available on GitHub.

rss · GitHub Trending - Daily (All) · May 12, 14:31

**Background**: A multimodal AI agent can process and act on multiple types of data, such as text, images, and GUI screenshots, to perform tasks autonomously. Agent-based models simulate interactions of autonomous agents to understand complex systems. ByteDance's TARS stack combines these concepts into a practical, open-source toolkit.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bytedance/UI-TARS-desktop">Agent TARS UI-TARS-desktop - GitHub</a></li>
<li><a href="https://agent-tars.com/">Agent TARS - Open-source Multimodal AI Agent Stack</a></li>
<li><a href="https://ui-tarsai.com/">Bytedance UI - TARS AI Desktop : AI Agent for Computer Control</a></li>

</ul>
</details>

**Discussion**: The community has shown strong interest, with many praising ByteDance for open-sourcing such a practical tool. Some discussions focus on the potential for local AI agents to replace cloud-dependent solutions, while others note the need for more documentation and examples.

**Tags**: `#AI`, `#open-source`, `#multimodal`, `#agent`, `#ByteDance`

---

<a id="item-10"></a>
## [CloakBrowser: Stealth Chromium That Passes All Bot Tests](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser is a new open-source stealth Chromium browser that passes 30/30 bot detection tests, including Cloudflare Turnstile and reCAPTCHA v3, by applying 49 source-level C++ fingerprint patches. It serves as a drop-in replacement for Playwright and Puppeteer, requiring only a change of import. This tool addresses a major pain point in web scraping and automation by providing a reliable way to bypass advanced bot detection systems, potentially saving developers significant time and resources. Its open-source nature and zero-config setup lower the barrier for anyone needing undetectable browser automation. The patches modify fingerprints at the C++ source level, covering canvas, WebGL, audio, fonts, GPU, screen, WebRTC, network timing, automation signals, and CDP input behavior. It also includes a humanize=True flag that simulates human-like mouse curves, keyboard timing, and scroll patterns, achieving a 0.9 reCAPTCHA v3 score.

rss · GitHub Trending - Daily (All) · May 12, 14:31

**Background**: Websites use bot detection systems like Cloudflare Turnstile and reCAPTCHA to distinguish automated browsers from human users. Traditional automation tools like Playwright and Puppeteer are often detected because they leave identifiable fingerprints in the browser environment. CloakBrowser modifies the Chromium source code itself to remove these fingerprints, making the browser appear identical to a normal user's browser.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/CloakHQ/CloakBrowser">GitHub - CloakHQ/CloakBrowser: Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. · GitHub</a></li>
<li><a href="https://cloakbrowser.dev/">CloakBrowser — Stealth Chromium for Browser Automation</a></li>

</ul>
</details>

**Tags**: `#web scraping`, `#browser automation`, `#anti-detection`, `#chromium`, `#playwright`

---

<a id="item-11"></a>
## [Build a ChatGPT-like LLM from Scratch with PyTorch](https://github.com/rasbt/LLMs-from-scratch) ⭐️ 8.0/10

Sebastian Raschka released a comprehensive GitHub repository and accompanying book that teaches how to build a GPT-like large language model from scratch using PyTorch, covering development, pretraining, and finetuning. This resource provides an accessible, step-by-step path for AI practitioners and researchers to deeply understand LLM internals, bridging the gap between theory and practice. It also includes code to load larger pretrained models for finetuning, making it practical for real-world applications. The repository is the official code for the book 'Build a Large Language Model (From Scratch)' (ISBN 9781633437166) and includes a table of contents, setup guides, and continuous integration tests for Linux and Windows. The method mirrors the approach used in creating large-scale foundational models like ChatGPT.

rss · GitHub Trending - Daily (All) · May 12, 14:31

**Background**: Large language models (LLMs) like GPT are deep neural networks trained on vast text data to generate human-like text. Building one from scratch involves understanding transformer architectures, attention mechanisms, and training pipelines. This repository simplifies that process for educational purposes.

**Tags**: `#LLM`, `#PyTorch`, `#GPT`, `#deep learning`, `#tutorial`

---

<a id="item-12"></a>
## [Agentmemory: Persistent Memory for AI Coding Agents](https://github.com/rohitg00/agentmemory) ⭐️ 8.0/10

Agentmemory is a new open-source library that provides persistent memory for AI coding agents like Claude Code, Cursor, and Gemini CLI, built on the iii engine and extending Karpathy's LLM Wiki pattern with confidence scoring, lifecycle management, knowledge graphs, and hybrid search. This addresses a major pain point for developers using AI coding agents, who often have to re-explain context across sessions. By enabling agents to remember past interactions, agentmemory can significantly boost productivity and reduce token usage by up to 92%. Agentmemory achieves 95.2% retrieval recall at R@5, provides 51 MCP tools and 12 auto hooks, requires zero external databases, and has 827 passing tests. It works with any MCP client and is available on npm.

rss · GitHub Trending - Daily (All) · May 12, 14:31

**Background**: AI coding agents like Claude Code and Cursor assist developers by writing code, but they lack persistent memory, so they forget context between sessions. The Model Context Protocol (MCP) is an open standard for connecting AI agents with data sources. Karpathy's LLM Wiki pattern uses structured markdown files as a knowledge base for LLMs, which agentmemory extends with advanced features.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/rohitg00/agentmemory">GitHub - rohitg00/agentmemory: #1 Persistent memory for AI coding agents based on real-world benchmarks · GitHub</a></li>
<li><a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">llm-wiki · GitHub</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#persistent memory`, `#MCP`, `#developer tools`, `#LLM`

---

<a id="item-13"></a>
## [WeChat 4.x Database Decryptor Extracts Keys from Memory](https://github.com/ylytdeng/wechat-decrypt) ⭐️ 8.0/10

A new open-source tool, wechat-decrypt, can extract encryption keys from the memory of a running WeChat 4.x process and decrypt all local SQLCipher 4 databases on Windows, macOS, and Linux. It also provides real-time message monitoring and rich media parsing, with recent updates adding inline emoji display, hidden message detection, and improved Web UI. This tool significantly lowers the barrier for security researchers and forensic analysts to access WeChat's encrypted local data, enabling deeper investigation into message histories and user activity. It also demonstrates a practical memory extraction technique against a widely-used application, highlighting potential privacy and security implications for millions of users. The tool works by scanning process memory for a specific pattern: the raw key in format x'<64hex_enc_key><32hex_salt>', then verifies correctness via HMAC on page 1. It requires administrator/root privileges and supports Python 3.10+; macOS additionally needs ad-hoc code signing and Xcode Command Line Tools.

rss · GitHub Trending - Python · May 12, 14:31

**Background**: WeChat 4.x uses SQLCipher 4 to encrypt its local databases with AES-256-CBC and HMAC-SHA512, with PBKDF2-HMAC-SHA512 key derivation (256,000 iterations) and a page size of 4096 bytes. The encryption keys are cached in process memory by WeChat's WCDB wrapper, making them extractable via memory scanning. SQLCipher is a widely-used SQLite extension that provides transparent full-database encryption.

<details><summary>References</summary>
<ul>
<li><a href="https://www.zetetic.net/sqlcipher/">SQLCipher - Full Database Encryption for SQLite | Zetetic</a></li>
<li><a href="https://github.com/sqlcipher/sqlcipher">GitHub - sqlcipher/sqlcipher: SQLCipher is a standalone fork ... SQLCipher: AES 256 Bit - SQLite3 Multiple Ciphers sqlcipher/sqlcipher | DeepWiki SQLCipher - Download - Softpedia SQLCipher API - Full Database Encryption PRAGMAs, Functions ... Releases · sqlcipher/sqlcipher - GitHub</a></li>
<li><a href="https://aibit.im/blog/post/wechat-4-x-decryptor-extract-keys-decrypt-dbs">WeChat 4.x Decryptor: Extract Keys & Decrypt DBs | AIBit</a></li>

</ul>
</details>

**Discussion**: The project has gained significant attention on GitHub with 1.9k stars and 1.3k forks, and an active Telegram group for support. Community discussions likely focus on the tool's effectiveness, cross-platform compatibility, and potential ethical concerns regarding unauthorized access to WeChat data.

**Tags**: `#security`, `#forensics`, `#reverse engineering`, `#wechat`, `#python`

---

<a id="item-14"></a>
## [VLM Reliability Probe Challenges Attention-Confidence Assumption](https://arxiv.org/abs/2605.08200) ⭐️ 8.0/10

Researchers introduced the VLM Reliability Probe (VRP), a mechanistic pipeline that analyzes attention, hidden states, and causal circuits in three VLM families (LLaVA-1.5, PaliGemma, Qwen2-VL). They found that attention structure is a near-zero predictor of correctness (R_pb=0.001), contradicting the common belief that sharp attention implies reliability. This study challenges a pervasive intuition in vision-language model interpretability, showing that attention maps are misleading for trustworthiness assessment. The findings have direct implications for building more reliable VLMs and designing better monitoring tools, especially in high-stakes applications. The VRP revealed that reliability becomes legible later in computation: a single hidden-state linear probe achieved AUROC>0.95 on POPE for two of three families. Additionally, causal neuron-level ablations exposed a sharp architectural split: late-fusion LLaVA concentrates reliability in a fragile late bottleneck, while early-fusion PaliGemma and Qwen2-VL distribute it widely.

rss · arXiv - AI · May 12, 04:00

**Background**: Vision-language models (VLMs) combine visual and textual information to answer questions about images. Mechanistic interpretability aims to understand the internal computations of neural networks by tracing causal circuits and analyzing hidden states. The Attention-Confidence Assumption posits that models are more reliable when their attention maps are sharply focused on relevant image regions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/itsloganmann/VLM-Reliability-Probe">GitHub - itsloganmann/VLM-Reliability-Probe</a></li>
<li><a href="https://arxiv.org/pdf/2605.08200">Where Reliability Lives in Vision–Language Models: A ...</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#mechanistic interpretability`, `#reliability`, `#attention`, `#causal circuits`

---

<a id="item-15"></a>
## [Auto-Rubric as Reward: Explicit Multimodal Generative Criteria](https://arxiv.org/abs/2605.08354) ⭐️ 8.0/10

Auto-Rubric as Reward (ARR) is a novel framework that converts implicit preferences from vision-language models (VLMs) into explicit, prompt-specific rubrics for reward modeling, and introduces Rubric Policy Optimization (RPO) to distill these rubrics into robust binary rewards for multimodal generative alignment. This approach addresses key limitations in RLHF for multimodal models, such as reward hacking and lack of interpretability, by externalizing preferences into inspectable criteria, potentially leading to more reliable and data-efficient alignment in text-to-image generation and image editing. ARR externalizes a VLM's internalized preference knowledge as prompt-specific rubrics before any pairwise comparison, suppressing evaluation biases like positional bias. RPO then uses these rubrics to condition preference decisions, replacing opaque scalar regression and stabilizing policy gradients.

rss · arXiv - AI · May 12, 04:00

**Background**: Reinforcement Learning from Human Feedback (RLHF) aligns generative models with human preferences but often reduces complex judgments to scalar or pairwise labels, leading to reward hacking. Rubrics-as-Reward (RaR) methods attempt to use explicit criteria, but generating reliable rubrics scalably remains challenging. ARR builds on RaR by automatically generating rubrics from VLMs' implicit knowledge.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.17746">[2507.17746] Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains</a></li>
<li><a href="https://arxiv.org/abs/2510.17314">[2510.17314] Auto-Rubric: Learning to Extract Generalizable Criteria for Reward Modeling</a></li>
<li><a href="https://arxiv.org/html/2510.14738">AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning</a></li>

</ul>
</details>

**Tags**: `#RLHF`, `#multimodal alignment`, `#reward modeling`, `#generative AI`, `#VLM`

---

<a id="item-16"></a>
## [Embeddings for Preferences, Not Semantics](https://arxiv.org/abs/2605.08360) ⭐️ 8.0/10

A new paper formalizes the problem that standard text embeddings measure semantic similarity, not preferential similarity needed for facility location and fair clustering in collective decision-making, and proposes synthetic training data to break the correlation between preference-relevant signals and semantic nuisance. This work addresses a fundamental mismatch between semantic embeddings and preference-based decision-making, which could significantly improve AI-driven collective decision-making and fair clustering by enabling embeddings that truly capture participants' preferences. The paper formalizes an invariance problem where text embedding models encode both preference-relevant signals (stance and values) and semantic nuisance (style and wording), which are observationally correlated, so a geometry relying on nuisance can appear preference-correct when it is not.

rss · arXiv - AI · May 12, 04:00

**Background**: Facility location problems and fair clustering are mathematical frameworks used to find representative points or partitions that minimize distances to participants. Standard text embeddings like those from BERT or GPT map text to vectors based on semantic similarity, but for collective decision-making, distances should reflect preferential agreement rather than semantic closeness. This paper identifies that off-the-shelf embeddings only capture a coarse preference signal through correlation, which fails when the correlation breaks.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08360">[2605.08360] Embeddings for Preferences, Not Semantics</a></li>
<li><a href="https://aidailypost.com/news/new-embeddings-prioritize-preferential-similarity-over-semantics">New embeddings prioritize preferential similarity over...</a></li>

</ul>
</details>

**Tags**: `#embeddings`, `#collective decision-making`, `#fair clustering`, `#preference learning`, `#NLP`

---

<a id="item-17"></a>
## [Free-Energy Framework Distinguishes Capability Elicitation from Creation](https://arxiv.org/abs/2605.08368) ⭐️ 8.0/10

A new arXiv paper introduces a free-energy-based framework to distinguish capability elicitation from capability creation in LLM post-training, operationalized via the concept of accessible support. This distinction clarifies whether post-training merely reweights existing behaviors or expands the model's reachable behavioral space, which has significant implications for AI alignment and training methodology. The paper defines accessible support as the set of behaviors a model can practically produce under finite budgets; reweighting within this support is elicitation, while changing the support is creation. Both SFT and RL are viewed as reweighting a pretrained reference distribution with different external signals.

rss · arXiv - AI · May 12, 04:00

**Background**: The free-energy principle, originally from neuroscience, states that systems minimize variational free energy to maintain their existence. In LLM post-training, debates often treat SFT as imitation and RL as discovery, but this paper argues that a more nuanced distinction is needed based on whether the training changes the model's reachable behavior space.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08368">[2605.08368] On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective</a></li>
<li><a href="https://en.wikipedia.org/wiki/Free_energy_principle">Free energy principle - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#post-training`, `#capability elicitation`, `#free-energy`, `#AI alignment`

---

<a id="item-18"></a>
## [MemQ: Q-Learning with Eligibility Traces for Self-Evolving Memory Agents](https://arxiv.org/abs/2605.08374) ⭐️ 8.0/10

MemQ introduces a novel method that applies TD(λ) eligibility traces to memory Q-values in LLM agents, propagating credit backward through a provenance DAG to enable self-evolving memory. It achieves state-of-the-art results across six diverse benchmarks, including OS interaction, function calling, and code generation. This work addresses a key limitation of current memory systems that treat each memory independently, by propagating credit through dependency chains. It has the potential to significantly improve LLM agent performance on multi-step tasks, advancing the development of more autonomous and adaptive AI agents. MemQ formalizes the setting as an Exogenous-Context MDP (EC-MDP), where the task stream is exogenous and the memory store is endogenous. Credit weight decays as (γλ)^d with DAG depth d, replacing temporal distance with structural proximity, and the method shows largest gains on multi-step tasks (up to +5.7 pp) and smallest on single-step classification (+0.77 pp).

rss · arXiv - AI · May 12, 04:00

**Background**: Episodic memory in LLM agents allows them to store and retrieve past experiences, but current methods evaluate each memory independently, ignoring how memories enable future memories. TD(λ) eligibility traces are a reinforcement learning technique that assigns credit to states based on recency and frequency, and provenance DAGs record the dependency relationships between memories. The Exogenous-Context MDP framework separates the external task stream from the agent's internal memory, enabling more principled credit assignment.

<details><summary>References</summary>
<ul>
<li><a href="https://zhuglr.medium.com/eligibility-trace-in-temporal-difference-learning-391aa94ba091">Eligibility trace in Temporal difference learning | by Guilin Zhu | Medium</a></li>
<li><a href="https://arxiv.org/abs/2207.06272">Hindsight Learning for MDPs with Exogenous Inputs Hindsight Learning for MDPs with Exogenous Inputs (PDF) Hindsight Learning for MDPs with Exogenous Inputs Learning a Fast Mixing Exogenous Block MDP using a Single ... Contextual Markov Decision Processes - arXiv.org Learning a Fast Mixing Exogenous Block MDP using a Single ... Learning Efficiently Function Approximation for Contextual MDP</a></li>

</ul>
</details>

**Tags**: `#LLM Agents`, `#Reinforcement Learning`, `#Memory Systems`, `#Provenance DAG`, `#Q-Learning`

---

<a id="item-19"></a>
## [SkillLens: Hierarchical Skill Reuse for Cost-Efficient LLM Agents](https://arxiv.org/abs/2605.08386) ⭐️ 8.0/10

SkillLens introduces a four-layer hierarchical skill graph (policies, strategies, procedures, primitives) and an adaptive retrieval mechanism that enables mixed-granularity skill reuse for LLM agents, achieving up to 6.31 percentage-point improvement in bug localization accuracy and raising success rate from 45.00% to 51.31% on ALFWorld. This work addresses the critical tension between relevance and cost in skill reuse for LLM agents, potentially making them more efficient and adaptable in complex, long-horizon tasks. The hierarchical approach could influence future agent architectures and reduce operational costs. SkillLens uses degree-corrected random walk to expand skill seeds over the graph and a verifier to decide whether to accept, decompose, rewrite, or skip each visited unit. Theoretical analysis shows sublinear cost under sparse mismatch assumptions and monotonic improvement of the validation objective.

rss · arXiv - AI · May 12, 04:00

**Background**: LLM agents often reuse skills from flat libraries, but coarse skills may introduce irrelevant context while rewriting entire skills is expensive. SkillLens organizes skills hierarchically to allow fine-grained reuse, reducing cost and improving relevance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08386">SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost ...</a></li>
<li><a href="https://aipulselab.tech/news/skilllens-adaptive-multi-granularity-skill-reuse-for-cost-efficient-llm-agents-e9f6c1">SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#skill reuse`, `#hierarchical framework`, `#cost efficiency`, `#graph-based retrieval`

---

<a id="item-20"></a>
## [LLMs Learn In-Context via Dual Mechanisms](https://arxiv.org/abs/2605.08405) ⭐️ 8.0/10

A new paper provides causal evidence that LLMs use both pattern-matching and latent structure inference during in-context learning, using a graph random-walk task and techniques like PCA, activation patching, and steering. This research clarifies a fundamental debate in LLM interpretability, showing that in-context learning is not purely memorization but involves genuine reasoning, which has implications for model understanding and safety. The study uses a toy graph random-walk task with two competing graph structures, and finds via PCA that both topologies are encoded in orthogonal subspaces at intermediate mixture ratios, contradicting a pure pattern-matching account.

rss · arXiv - AI · May 12, 04:00

**Background**: In-context learning (ICL) allows LLMs to perform tasks based on examples in the prompt without weight updates. Two competing theories explain ICL: pattern-matching (copying local transitions) and latent structure inference (building a global model). This paper provides causal evidence that both mechanisms coexist.

<details><summary>References</summary>
<ul>
<li><a href="https://ai.stanford.edu/blog/understanding-incontext/">How does in-context learning work? A framework for ...</a></li>
<li><a href="https://arxiv.org/abs/2507.16003">[2507.16003] Learning without training: The implicit dynamics ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#in-context learning`, `#interpretability`, `#causal inference`

---

<a id="item-21"></a>
## [BaLoRA: Bayesian Low-Rank Adaptation Boosts Accuracy and Uncertainty](https://arxiv.org/abs/2605.08110) ⭐️ 8.0/10

BaLoRA extends LoRA with Bayesian inference, introducing an input-adaptive Bayesian parameterization that adds minimal parameters and compute, improving accuracy and providing well-calibrated uncertainty estimates. This narrows the accuracy gap between LoRA and full fine-tuning while adding uncertainty quantification, making fine-tuned models more reliable for safety-critical applications like drug discovery or autonomous driving. The adaptive noise injection underlying BaLoRA not only yields uncertainty estimates but also significantly improves prediction accuracy across natural language reasoning and vision tasks; in metal-organic framework band gap prediction, BaLoRA's zero-shot uncertainty estimates correlate more strongly with error than a trained ensemble of LoRA models.

rss · arXiv - Machine Learning · May 12, 04:00

**Background**: LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that freezes pre-trained weights and injects trainable low-rank matrices, reducing memory and compute. However, LoRA produces point estimates without uncertainty quantification, limiting its use in reliability-critical domains. Bayesian neural networks provide probabilistic predictions by learning distributions over weights, but are often computationally expensive. BaLoRA combines the efficiency of LoRA with Bayesian principles to address these limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">LoRA: Low-Rank Adaptation of Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2302.13425">[2302.13425] A Survey on Uncertainty Quantification Methods for Deep Learning</a></li>

</ul>
</details>

**Tags**: `#Bayesian methods`, `#Low-Rank Adaptation`, `#fine-tuning`, `#large language models`, `#uncertainty quantification`

---

<a id="item-22"></a>
## [Statistical Analysis of KV Cache Quantization Schemes](https://arxiv.org/abs/2605.08114) ⭐️ 8.0/10

This paper provides a rigorous statistical analysis of three KV cache quantization schemes (KV, KQV, QKQV) under a fair bit budget, revealing that KQV outperforms QKQV in KL divergence across all budgets and distributions, with a budget-dependent crossover in geometric K reconstruction. This work provides novel insights into K-V asymmetry and budget-dependent crossover, which are critical for optimizing LLM inference efficiency and reducing memory footprint without sacrificing quality. The paper identifies that at n=4 (the practically dominant budget), KQV wins on every measure, while QKQV achieves better geometric K reconstruction at n∈{2,3,5}. The crossover is attributed to the Jensen mechanism amplified by softmax.

rss · arXiv - Machine Learning · May 12, 04:00

**Background**: KV cache quantization reduces memory usage in large language models by compressing the key-value cache used during autoregressive decoding. Common techniques include scalar quantization, Walsh-Hadamard Transform (WHT), and Quaternion Johnson-Lindenstrauss (QJL) transform. This paper compares three schemes: a scalar MSE baseline (KV), a hybrid using WHT+MSE on K and WHT+MSE+QJL on V (KQV), and a full QJL approach (QKQV).

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.03482">[2406.03482] QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead</a></li>
<li><a href="https://arxiv.org/html/2603.20397v1">KV Cache Optimization Strategies for Scalable and Efficient LLM Inference</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#quantization`, `#LLM inference`, `#statistical inference`, `#machine learning`

---

<a id="item-23"></a>
## [Sanity Checks for Long-Form Hallucination Detection](https://arxiv.org/abs/2605.08346) ⭐️ 8.0/10

The paper introduces a controlled-invariance methodology with two oracle tests (Force and Remove) to distinguish whether hallucination detection methods evaluate reasoning or exploit answer-level artifacts. It also presents TRACT, a lightweight lexical scorer that achieves strong robustness by using trajectory features like hedging trends and step-length dynamics. This work addresses a critical gap in LLM evaluation by revealing that many hallucination detectors may succeed by relying on answer artifacts rather than genuine reasoning assessment. The findings suggest that the central challenge is isolating trace-level signal from endpoint cues, which can improve the reliability of chain-of-thought reasoning evaluation. The Force oracle replaces the final answer with the ground truth while preserving the reasoning trace, and the Remove oracle strips answer-announcement steps. TRACT uses lexical trajectory features including hedging trends, step-length dynamics, and cross-response vocabulary convergence, and it remains competitive with or outperforms existing baselines on unperturbed traces.

rss · arXiv - NLP · May 12, 04:00

**Background**: Hallucination detection in large language models (LLMs) aims to identify when generated content is factually incorrect or unsupported. Recent methods analyze chain-of-thought reasoning traces to detect hallucinations, but it is unclear whether they evaluate reasoning quality or simply exploit surface patterns in the final answer. The proposed oracle tests provide a sanity check to separate these factors.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08346v1">Sanity Checks for Long-Form Hallucination Detection - arXiv.org</a></li>
<li><a href="https://arxiv.org/html/2605.07209">Hallucination Detection via Activations of Open-Weight Proxy Analyzers</a></li>
<li><a href="https://arxiv.org/html/2508.18473">Principled Detection of Hallucinations in Large Language Models via Multiple Testing</a></li>

</ul>
</details>

**Tags**: `#hallucination detection`, `#large language models`, `#chain-of-thought`, `#evaluation methodology`

---

<a id="item-24"></a>
## [LLM Circuits Not Task-Specific, Study Finds](https://arxiv.org/abs/2605.08348) ⭐️ 8.0/10

A new paper systematically measures the consistency and specificity of language model circuits across six tasks and seven models, finding high within-task reuse but low task-specificity due to substantial overlap across tasks. This challenges the common assumption that circuits are task-specific, raising questions about the degree to which circuits can support targeted understanding and intervention on model behavior. Using edge attribution patching, the authors found that ablating one task's circuit damages another task's performance about as much as that task's own circuit does, indicating substantial overlap.

rss · arXiv - NLP · May 12, 04:00

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by identifying sparse subgraphs (circuits) responsible for specific behaviors. The circuits framework typically evaluates circuits by measuring necessity and sufficiency. This paper introduces two less-studied properties: consistency (recurrence of components within a task) and specificity (uniqueness to a task).

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2310.10348">[2310.10348] Attribution Patching Outperforms Automated Circuit Discovery</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#language models`, `#circuits`, `#interpretability`, `#deep learning`

---

<a id="item-25"></a>
## [Frozen-Tower Composition for Efficient Multimodal Embeddings](https://arxiv.org/abs/2605.08384) ⭐️ 8.0/10

Researchers introduce jina-embeddings-v5-omni, a pair of multimodal embedding models that encode text, image, audio, and video into a single semantic space using frozen-encoder composition, training only 0.35% of total weights. This approach dramatically reduces training cost while preserving the text embedding geometry, enabling efficient multimodal retrieval and analysis without full model retraining. The model uses frozen image and audio encoders from Qwen3.5 and Qwen2.5-Omni, respectively, and only trains lightweight connecting components, achieving competitive performance with larger multimodal models.

rss · arXiv - NLP · May 12, 04:00

**Background**: Multimodal embedding models aim to represent different data types (text, image, audio, video) in a shared vector space. Traditional approaches often require full fine-tuning of large models, which is computationally expensive. Frozen-encoder composition, a parameter-efficient transfer learning method, keeps pre-trained encoders frozen and only trains small adapters, significantly reducing training overhead.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08384v1">jina - embeddings - v 5 - omni : Text-Geometry-Preserving Multimodal...</a></li>
<li><a href="https://www.elastic.co/search-labs/blog/jina-embeddings-v5-omni-all-media-one-index">jina - embeddings - v 5 - omni for text, images, video... - Elasticsearch Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_learning">Multimodal learning - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#multimodal embeddings`, `#frozen-encoder composition`, `#VLM architecture`, `#efficient training`, `#AI/ML research`

---

<a id="item-26"></a>
## [LLM-Based Model Turns Explanations into Action Plans](https://arxiv.org/abs/2605.08406) ⭐️ 8.0/10

Researchers propose a computational model that uses a large language model to convert natural language explanations into program-like guidance (a policy prior and value map), which a planning agent then executes under partial observability. The model scores explanations by the efficiency and reliability of the resulting paths, and was validated across four preregistered experiments with 1,200 explanations over 24 maps. This work bridges explanation generation and planning under uncertainty, offering a principled way to evaluate and generate helpful explanations for navigation tasks. It has implications for AI systems that need to communicate instructions effectively, such as autonomous agents or assistive technologies. The model uses an LLM to produce a policy prior and value map from an explanation, then a planner executes under partial observability, penalizing replanning. Higher-scored explanations were judged more helpful and improved navigation performance in human experiments.

rss · arXiv - NLP · May 12, 04:00

**Background**: Planning under uncertainty involves making decisions when the agent has incomplete information about the environment. A policy prior guides which actions to consider, while a value map estimates the desirability of states. This model combines these concepts with LLM-based explanation generation to simulate how listeners ground language into action.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12633763/">Between planning and map-building: prioritizing replay when future goals are uncertain - PMC</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/fully-observable-vs-partially-observable-environment-in-ai/">Fully Observable vs. Partially Observable Environment in AI</a></li>

</ul>
</details>

**Tags**: `#explanation generation`, `#planning under uncertainty`, `#large language models`, `#cognitive science`, `#AI`

---

<a id="item-27"></a>
## [Sem-ECE: New Calibration Metric for Open-Ended QA](https://arxiv.org/abs/2605.08432) ⭐️ 8.0/10

Researchers introduced Sem-ECE, a calibration evaluation framework for open-ended question answering that uses semantic sampling to group model outputs into semantic classes and uses the resulting frequencies as confidence estimates. This addresses a critical gap in LLM calibration evaluation for realistic open-ended QA, which is the most common deployment setting for modern LLMs and is essential for safe deployment in high-stakes domains like medicine and law. Sem-ECE includes two estimators: Sem1-ECE (same-sample self-consistency) and Sem2-ECE (held-out variant), both proven asymptotically unbiased, with Sem2 achieving strictly smaller calibration error on hard questions.

rss · arXiv - NLP · May 12, 04:00

**Background**: Calibration measures whether a model's predicted confidence matches its actual accuracy. Expected Calibration Error (ECE) is a standard metric for classification, but open-ended QA lacks a reliable calibration evaluation method because logit-based and verbalized confidence approaches have limitations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08432v1">A Semantic-Sampling Framework for Evaluating Calibration in ...</a></li>
<li><a href="https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/">Expected Calibration Error (ECE): A Step-by-Step Visual Explanation | Towards Data Science</a></li>

</ul>
</details>

**Tags**: `#LLM calibration`, `#open-ended QA`, `#AI safety`, `#evaluation framework`

---

<a id="item-28"></a>
## [Self-Captioning Boosts Robustness in Vision-Language Models](https://arxiv.org/abs/2605.08145) ⭐️ 8.0/10

Researchers propose a self-captioning workflow with a Multimodal Interaction Gate that converts unique interactions into redundant ones, reducing visual-induced errors by 38.3% and improving consistency by 16.8% in vision-language models. This work directly addresses the critical issues of hallucination and robustness in vision-language models, which are essential for reliable deployment in real-world applications like autonomous driving and medical imaging. The method amplifies redundant multimodal interactions—shared information between vision and language—to compensate for corrupted or ambiguous modalities, bridging a gap in current instruction datasets that often eliminate redundancies.

rss · arXiv - Computer Vision · May 12, 04:00

**Background**: Vision-language models (VLMs) combine visual and textual information to perform tasks like image captioning and visual question answering. They often suffer from hallucinations (generating false details) and lack robustness when one modality is corrupted. Multimodal interactions can be categorized into redundant (shared), unique (exclusive), and synergistic (emergent) information. This paper proposes amplifying redundant interactions to improve reliability.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.07402">[2409.07402] What to align in multimodal contrastive learning?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_interaction">Multimodal interaction - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#multimodal learning`, `#robustness`, `#hallucination`, `#redundancy`

---

<a id="item-29"></a>
## [VT-Bench: First Unified Benchmark for Visual-Tabular Learning](https://arxiv.org/abs/2605.08146) ⭐️ 8.0/10

Researchers introduced VT-Bench, the first unified benchmark for visual-tabular multi-modal learning, aggregating 14 datasets across 9 domains with over 756K samples and evaluating 23 representative models. This benchmark addresses an underexplored area in multi-modal learning that is critical for high-stakes domains like healthcare and industry, providing a standardized evaluation to drive progress in visual-tabular foundation models. VT-Bench covers both discriminative prediction and generative reasoning tasks, and includes models ranging from unimodal experts to specialized visual-tabular models and general-purpose vision-language models (VLMs).

rss · arXiv - Computer Vision · May 12, 04:00

**Background**: Multi-modal learning typically combines text, images, or audio, but visual-tabular data—where images are paired with structured tables—is less studied despite its importance in medical imaging and industrial inspection. Existing benchmarks often focus on visual-text tasks, leaving a gap for standardized evaluation of visual-tabular models. VT-Bench fills this gap by providing a unified platform with diverse datasets and model evaluations.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08146">VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal ...</a></li>

</ul>
</details>

**Tags**: `#multi-modal learning`, `#benchmark`, `#visual-tabular`, `#machine learning`, `#healthcare`

---

<a id="item-30"></a>
## [HY-Himmel: Efficient Long Video Understanding via Hierarchical Motion Encoding](https://arxiv.org/abs/2605.08158) ⭐️ 8.0/10

HY-Himmel introduces a hierarchical video-language framework that separates semantic and motion processing using sparse anchor I-frames and a lightweight compressed-domain tri-stream adapter for motion encoding. This approach addresses key bottlenecks in long-video understanding—high decode cost, token growth, and weak motion perception—achieving superior performance with fewer tokens, which could enable more efficient multimodal AI systems. On Video-MME, HY-Himmel surpasses the dense 32-frame baseline by +2.3 percentage points (61.2% to 63.5%) while using 3.6× fewer context tokens.

rss · arXiv - Computer Vision · May 12, 04:00

**Background**: Long-video understanding with multimodal language models typically requires decoding all frames into RGB, which is computationally expensive. Sparse keyframe sampling reduces cost but loses motion information. HY-Himmel leverages compressed-domain data (motion vectors, residuals) from video codecs to efficiently capture motion without full decoding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0925231224001607">Action recognition in compressed domains: A survey</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10262342">Compressed Video Action Recognition With Dual-Stream and Dual ...</a></li>
<li><a href="https://ottverse.com/i-p-b-frames-idr-keyframes-differences-usecases/">I, P, and B-frames – Differences and Use Cases Made Easy</a></li>

</ul>
</details>

**Tags**: `#video understanding`, `#multimodal language models`, `#motion encoding`, `#compressed domain`, `#hierarchical framework`

---

<a id="item-31"></a>
## [WATCH Framework for Month-Level Archaeological Change Detection](https://arxiv.org/abs/2605.08160) ⭐️ 8.0/10

Researchers introduced WATCH, a framework that uses PlanetScope satellite mosaics and three scoring methods (Temporal Embedding Distance, Self-Supervised Change Detection, and Weakly Supervised localization) to detect changes at archaeological sites at monthly resolution from 2017 to 2024. This work enables scalable, automated monitoring of cultural heritage sites, addressing a critical need in archaeology where manual inspection is impractical. The framework's high recall within a three-month tolerance (92.5%) makes it decision-relevant for heritage protection. The benchmark includes 1,943 archaeological sites in Afghanistan and tests six foundation models (CLIP, GeoRSCLIP, SatMAE, Prithvi-EO-2.0, DINOv3, Satlas-Pretrain). Unsupervised methods (TED, SSCD) consistently outperform the weakly supervised alternative, with TED+SatMAE achieving 55% exact-month recall.

rss · arXiv - Computer Vision · May 12, 04:00

**Background**: Satellite-based change detection typically relies on supervised learning with labeled data, which is scarce for archaeological sites. WATCH combines training-free and self-supervised approaches to overcome this limitation. PlanetScope provides high-frequency (daily) imagery at 4.7 m/px resolution, enabling monthly mosaics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.planet.com/products/mosaics/">Planet Mosaics : Comprehensive, High-Frequency Mosaics for Analysis</a></li>
<li><a href="https://docs.sentinel-hub.com/api/latest/data/planet/planet-scope/">PlanetScope</a></li>

</ul>
</details>

**Tags**: `#remote sensing`, `#change detection`, `#archaeology`, `#machine learning`, `#satellite imagery`

---

<a id="item-32"></a>
## [MULTITEXTEDIT: Benchmark for Cross-Lingual Text-in-Image Editing](https://arxiv.org/abs/2605.08163) ⭐️ 8.0/10

Researchers introduced MULTITEXTEDIT, a benchmark of 3,600 instances across 12 languages, 5 visual domains, and 7 editing operations, along with a new language fidelity metric (LSF) to evaluate cross-lingual degradation in text-in-image editing. This benchmark addresses a critical gap in evaluating multilingual text-in-image editing, revealing that all tested models suffer from cross-lingual degradation, especially for scripts like Arabic and Hebrew, which is vital for developing equitable multilingual AI systems. The LSF metric uses a two-stage LVM protocol to detect script-level errors like missing diacritics and reversed RTL order, achieving a quadratic-weighted kappa of 0.76 against human annotators. The benchmark also found a pervasive mismatch between semantic correctness and pixel-level fidelity.

rss · arXiv - Computer Vision · May 12, 04:00

**Background**: Text-in-image editing involves modifying text within an image while preserving the background and visual style. Existing benchmarks are mostly English-centric and fail to evaluate performance across different languages and scripts, leading to biased AI systems.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/nameoffly/MultiTextEdit">GitHub - nameoffly/MultiTextEdit</a></li>
<li><a href="https://arxiv.org/pdf/2605.08163">MULTITEXTEDIT: Benchmarking Cross-Lingual Degradation in Text ...</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#text-in-image editing`, `#multilingual`, `#AI evaluation`, `#computer vision`

---

<a id="item-33"></a>
## [Sinkhorn Treatment Effects: Causal Optimal Transport Measure](https://arxiv.org/abs/2605.08485) ⭐️ 8.0/10

The paper introduces the Sinkhorn treatment effect, an entropic optimal transport measure that quantifies divergence between entire counterfactual distributions, and provides debiased estimators and asymptotically valid hypothesis tests for distributional treatment effects. This work advances causal inference beyond average treatment effects by capturing distributional differences, enabling more nuanced analysis of treatment impacts across entire populations, with rigorous statistical guarantees. The Sinkhorn treatment effect is expressed as a smooth transformation of counterfactual mean embeddings, allowing first- and second-order pathwise differentiability. An aggregated test across regularization parameters is proposed to address power dependence on the entropic penalty.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Optimal transport measures the cost of transforming one probability distribution into another. Entropic optimal transport adds a regularization term for computational efficiency. Counterfactual mean embeddings represent distributions in reproducing kernel Hilbert spaces, enabling nonparametric causal inference. The Sinkhorn treatment effect combines these ideas to compare counterfactual distributions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08485">[2605.08485] Sinkhorn Treatment Effects: A Causal Optimal ...</a></li>
<li><a href="https://icml.cc/virtual/2026/poster/65027">ICML Poster Sinkhorn Treatment Effects</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#optimal transport`, `#treatment effects`, `#statistical theory`, `#hypothesis testing`

---

<a id="item-34"></a>
## [Mean-Field Theory Reveals Phase Transitions in Multi-Component ICA](https://arxiv.org/abs/2605.08552) ⭐️ 8.0/10

A new paper develops an asymptotically exact mean-field theory for high-dimensional multi-component online ICA, revealing initialization-driven phase transitions between decoupled and competitive learning regimes. This work extends ICA theory beyond single-component recovery, providing a unified framework to understand collective learning dynamics and phase behavior, which could impact unsupervised representation learning and high-dimensional statistics. The theory yields a closed ODE system for the overlap matrix between learned directions and true components, and predicts a staircase phenomenon where the number of recoverable components changes discretely with the learning rate.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Independent Component Analysis (ICA) is a method for separating a multivariate signal into additive, independent components, often used in blind source separation. Traditional high-dimensional ICA theory has focused on recovering a single component, but real-world applications often require simultaneous recovery of multiple components, which introduces coupling effects.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08552">Learnability and Competition in High-Dimensional Multi ...</a></li>

</ul>
</details>

**Tags**: `#ICA`, `#high-dimensional statistics`, `#mean-field theory`, `#unsupervised learning`, `#representation learning`

---

<a id="item-35"></a>
## [CONTRA: Conformal Prediction with Normalizing Flows](https://arxiv.org/abs/2605.08561) ⭐️ 8.0/10

CONTRA introduces a method that uses normalizing flows to define nonconformity scores for conformal prediction, enabling sharp prediction regions for multi-dimensional outputs. It also extends to enhance any predictive model by training a flow on residuals. This addresses a key limitation of conformal prediction in multi-dimensional settings, where traditional methods produce overly conservative regions. It improves uncertainty quantification in machine learning, benefiting applications like autonomous driving and medical diagnosis. CONTRA maps high-density regions in latent space to sharp prediction regions in output space, outperforming hyperrectangular or elliptical conformal regions. The extension trains a simple normalizing flow on residuals to add reliable prediction regions to any model.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Conformal prediction is a distribution-free method that produces prediction sets with guaranteed coverage, but it struggles with multi-dimensional outputs because it relies on one-dimensional nonconformity scores. Normalizing flows are generative models that transform a simple distribution into a complex one via invertible mappings, enabling tractable density estimation. CONTRA combines these ideas to create more expressive prediction regions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Normalizing_flows">Normalizing flows</a></li>
<li><a href="https://arxiv.org/abs/1908.09257">[1908.09257] Normalizing Flows: An Introduction and Review of ... Introduction to Normalizing Flows - Towards Data Science Normalizing Flow Models - GitHub Pages 15 Normalizing Flows – Machine Learning for Mechanical ... Normalizing Flows for Probabilistic Modeling and Inference Normalizing Flows: An Introduction and Review of Current Methods</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#normalizing flows`, `#uncertainty quantification`, `#density estimation`, `#machine learning`

---

<a id="item-36"></a>
## [Core-Halo Decomposition for Decentralized Fixed-Point Problems](https://arxiv.org/abs/2605.08681) ⭐️ 8.0/10

Researchers propose Core-Halo decomposition, a novel method that separates write ownership from read-only evaluation context to faithfully implement large-scale fixed-point problems in decentralized multi-agent systems. This addresses structural bias inherent in strict decomposition, enabling near-centralized performance while retaining parallelism benefits, with potential impact on decentralized optimization and multi-agent systems. The method aligns decomposition with the block-dependence structure of the operator, and the paper characterizes a Bellman closure condition and a blockwise bias lower bound for strict decomposition.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Fixed-point problems of the form x* = F(x*) are common in optimization and control. In decentralized settings, strict decomposition assigns each agent disjoint variable blocks, but many operators have dependencies across blocks, causing structural bias when truncated. Core-Halo decomposition allows overlapping read-only halos to preserve the original operator.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08681">[2605.08681] Core-Halo Decomposition: Decentralizing Large ...</a></li>
<li><a href="https://arxiv.org/pdf/2605.08681">Core-Halo Decomposition: Decentralizing Large-Scale Fixed ...</a></li>

</ul>
</details>

**Tags**: `#decentralized optimization`, `#fixed-point problems`, `#multi-agent systems`, `#decomposition methods`

---

<a id="item-37"></a>
## [New Diffusion-Based Method Measures Mode Separation in High Dimensions](https://arxiv.org/abs/2605.08777) ⭐️ 8.0/10

The paper introduces a diffusion-based framework that measures mode separation in high-dimensional densities using autocovariance analysis, proposing two readouts: SSA (Sum of Squared Autocorrelations) and DA (Dominant Autocorrelation directions). This provides a principled way to quantify clustering structure in high-dimensional data, which is crucial for clustering, generative modeling, and molecular dynamics, where traditional methods like PCA and entropy fail to capture barrier-separated clusters. The method uses a reversible diffusion with the target density as its stationary distribution and extracts SSA and DA from the autocovariance matrix; it requires only samples and a score function, scaling via pretrained score-based models using Tweedie's identity.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Mode separation refers to how sharply a distribution splits into clusters separated by low-density barriers, a key geometric property in high-dimensional statistics. Existing measures like entropy and PCA capture dispersion but not fragmentation, while mutual information requires known mixture components. The paper leverages the autocovariance of a reversible diffusion process, which is linked to the density's metastability, to quantify separation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08777">[2605.08777] Measuring and Decomposing Mode Separation via the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reversible_diffusion">Reversible diffusion - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autocovariance">Autocovariance - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#mode separation`, `#diffusion processes`, `#high-dimensional statistics`, `#density estimation`

---

<a id="item-38"></a>
## [Transformers' Approximation Power Proven via Softmax Partition](https://arxiv.org/abs/2605.08811) ⭐️ 8.0/10

A new paper proves that a two-block Transformer with softmax attention can uniformly approximate Hölder continuous functions with optimal parameter efficiency, using a local-to-global construction via softmax partition of unity. This provides the first rigorous theoretical framework showing that shallow Transformers can achieve near minimax-optimal generalization, bridging the gap between practice and theory for attention-based models. The Transformer uses only two encoder blocks and single-hidden-layer feed-forward networks, achieving ε-approximation with O(ε^{-d/α}) parameters for α-Hölder functions on [0,1]^d and manifolds.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Transformers are deep learning models that use attention mechanisms to process sequential data. The softmax function normalizes attention weights, and a partition of unity is a set of functions that sum to one, enabling local-to-global approximation. Hölder continuity measures function smoothness, with exponent α in (0,1].

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partition_of_unity">Partition of unity - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#transformers`, `#approximation theory`, `#deep learning theory`, `#attention mechanism`, `#function approximation`

---

<a id="item-39"></a>
## [Tight Generalization Bounds for Noiseless Inverse Optimization](https://arxiv.org/abs/2605.08866) ⭐️ 8.0/10

This paper establishes tight O(d/T) high-probability generalization bounds for noiseless inverse optimization, matching lower bounds and showing that the stochastic setting is effectively adversarial. These results significantly advance the theoretical foundations of inverse optimization, connecting it to bandit literature and providing tight regret guarantees that impact learning from expert demonstrations. The bounds hold for the induced action set and are strengthened under uniqueness conditions, matching best-arm identification rates; a parameter-free algorithm with lower per-iteration complexity is also proposed.

rss · arXiv - Data Science & Statistics · May 12, 04:00

**Background**: Inverse optimization infers the parameters of a decision-maker's objective from observed context-action data. Generalization bounds quantify how well a learned model performs on unseen data, and best-arm identification is a bandit problem where the goal is to find the best action efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2109.03920">[2109.03920] Inverse Optimization: Theory and Applications Inverse Optimization: Theory and Applications | Operations ... Inverse optimization for multi-objective linear programming - PMC Inverse Optimization | Springer Nature Link Inverse Optimization - MOOSE Introduction to inverse optimization - jsaezgallego.com Inverse Optimization: Theory and Applications - PubsOnLine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Best_arm_identification">Best arm identification</a></li>

</ul>
</details>

**Tags**: `#inverse optimization`, `#generalization bounds`, `#learning theory`, `#bandit algorithms`

---