---
layout: default
title: "Horizon Summary: 2026-08-05 (EN)"
date: 2026-08-05
lang: en
---

> From 88 items, 28 important content pieces were selected

---

1. [Google DeepMind Leadership Shakeup: Hassabis to Chair, Dean Departs](#item-1) ⭐️ 9.0/10
2. [Uber Open-Sources ADR for Enterprise AI Agent Security](#item-2) ⭐️ 9.0/10
3. [Jeff Dean and Sanjay Ghemawat Leave Google to Launch Discovery Loop](#item-3) ⭐️ 8.0/10
4. [Meta Ran Ads Containing AI-Generated Child Sexual Abuse Imagery](#item-4) ⭐️ 8.0/10
5. [Cloudflare Computer: Virtual Filesystem for Agents in Durable Objects](#item-5) ⭐️ 8.0/10
6. [System Design Primer: Comprehensive Guide for Interview Prep](#item-6) ⭐️ 8.0/10
7. [Addy Osmani's Agent Skills: Production-Grade Workflows for AI Coding Agents](#item-7) ⭐️ 8.0/10
8. [Superpowers: A New Agentic Skills Framework for Coding Agents](#item-8) ⭐️ 8.0/10
9. [AirLLM Runs 70B LLMs on 4GB GPU Without Quantization](#item-9) ⭐️ 8.0/10
10. [Self-Organising Digital Circuits Achieve Fault Tolerance via Meta-Learning](#item-10) ⭐️ 8.0/10
11. [BLAZE: A Socialized AI Paradigm for Scientific Discovery](#item-11) ⭐️ 8.0/10
12. [LLMs Automate Attribution Graph Annotation for Circuit Tracing](#item-12) ⭐️ 8.0/10
13. [Output-Aware Rotation for INT2 KV-Cache Quantization](#item-13) ⭐️ 8.0/10
14. [MemArena: New Benchmark for On-Device Personal Memory Assistants](#item-14) ⭐️ 8.0/10
15. [OncoTriad-QA: New Benchmark Integrates Radiology, Pathology, Genomics for Cancer QA](#item-15) ⭐️ 8.0/10
16. [OpenAI Privacy Filter Fails on Narrative Prose and Non-Latin Scripts](#item-16) ⭐️ 8.0/10
17. [Pairwise Preference Is a Poor Proxy for Clinical Safety in LLMs](#item-17) ⭐️ 8.0/10
18. [JudgeArena: Unified Framework for Reproducible LLM-Judge Evaluation](#item-18) ⭐️ 8.0/10
19. [Diagnosing and Repairing Interface Injury in KDA Linearized 0.6B Model](#item-19) ⭐️ 8.0/10
20. [Hunyuan3D-Buffalo 1.0: Unified Multimodal Model for 3D Generation, Understanding, and Editing](#item-20) ⭐️ 8.0/10
21. [Agent-Centric World Proxies Redefine World Modeling](#item-21) ⭐️ 8.0/10
22. [Vision-Language Models Show Poor Confidence Calibration on Brain MRI](#item-22) ⭐️ 8.0/10
23. [SAGE: Semantic Global Explanations for Attention-Based Survival Models in Pathology](#item-23) ⭐️ 8.0/10
24. [In-Context Collapse in VLMs: A New Failure Mode and Mitigation](#item-24) ⭐️ 8.0/10
25. [Unified Particle-Based Stochastic Optimization Framework with Convergence Guarantees](#item-25) ⭐️ 8.0/10
26. [Causal Inference for Unstructured Outcomes via Maximally Contrasting Features](#item-26) ⭐️ 8.0/10
27. [Minimax-Optimal Policy for Contextual Dynamic Pricing with Multimodal Revenue](#item-27) ⭐️ 8.0/10
28. [GFlowNets Training via Information Geometry and Natural Gradients](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Google DeepMind Leadership Shakeup: Hassabis to Chair, Dean Departs](https://blog.google/company-news/inside-google/message-ceo/next-chapter-ai-momentum/) ⭐️ 9.0/10

On August 5, 2026, Google announced a major leadership reshuffle at Google DeepMind: Demis Hassabis transitions from CEO to Chair, while Jeff Dean and Sanjay Ghemawat depart to launch a new public benefit corporation called Discovery Loop. This marks a significant shift in AI research leadership at Google. This leadership change signals a potential turning point for Google's AI strategy, as it loses two of its most iconic technical leaders. The departure of Jeff Dean and Sanjay Ghemawat, along with other recent exits, raises concerns about talent retention and the future of Google's AI research, especially with the Gemini flagship model still unreleased. Jeff Dean and Sanjay Ghemawat are launching Discovery Loop, an independent public benefit corporation focused on accelerating discoveries in machine learning, science, and engineering. Alphabet's stock fell about 4-5% following the announcement, reflecting investor concern.

hackernews · colesantiago · Aug 5, 16:05 · [Discussion](https://news.ycombinator.com/item?id=49184755)

**Background**: Google DeepMind was formed in 2023 by merging Google Brain and DeepMind, with Demis Hassabis as CEO and Jeff Dean as Chief Scientist. Jeff Dean has been a legendary figure at Google for 27 years, known for his contributions to systems like MapReduce and TensorFlow. The leadership change comes at a critical time as Google faces intense competition in AI, and the departure of key figures may impact its ability to innovate.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reuters.com/business/google-shakes-up-ai-leadership-deepmind-chief-shifts-role-2026-08-05/">Google shakes up AI leadership as DeepMind chief shifts role</a></li>
<li><a href="https://www.nytimes.com/2026/08/05/technology/google-ai-leadership.html">Google Names Demis Hassabis to New AI Role in a Leadership Shake-up</a></li>
<li><a href="https://www.nytimes.com/2026/08/05/technology/google-researchers-ai-startup.html">Four Top Google A.I. Researchers Form New Start-Up - The New York...</a></li>

</ul>
</details>

**Discussion**: The community expressed shock and concern, with many viewing this as the end of a golden era for Google AI. Commenters noted the loss of Jeff Dean and Sanjay Ghemawat is a major blow, and some pointed out a pattern of prominent researchers leaving Google, while few new ones join. There was also speculation about the impact on Google's stock and future AI development.

**Tags**: `#Google DeepMind`, `#AI leadership`, `#Jeff Dean`, `#Demis Hassabis`, `#tech industry`

---

<a id="item-2"></a>
## [Uber Open-Sources ADR for Enterprise AI Agent Security](https://github.com/uber/ADR) ⭐️ 9.0/10

Uber has open-sourced ADR (Agentic AI Detection and Response), a production-deployed enterprise security system for AI agents, including the ADR Sensor, ADR-Bench, and ADR Detector components. The accompanying paper was accepted to MLSys 2026. This release addresses the critical and emerging need for securing AI agents in enterprise environments, providing a production-proven framework that combines observability, benchmarking, and threat detection. It could set a standard for AI agent security and accelerate safe adoption of AI agents across industries. ADR-Bench includes over 300 tasks, 133 MCP servers, and coverage of all 17 agent attack techniques. The ADR Prevention component is not included in the current open-source release, and the offline ADR Explorer engine is also excluded.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: AI agents, such as coding assistants and customer support bots, operate through the Model Context Protocol (MCP) to interact with tools and data. Securing these agents is challenging because they can perform actions autonomously, potentially leading to data breaches or unsafe operations. ADR provides a framework to observe, benchmark, detect, and prevent such risks in enterprise settings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.17380">[2605.17380] ADR: An Agentic Detection System for Enterprise Agentic AI Security</a></li>
<li><a href="https://github.com/uber/ADR">GitHub - uber/ADR: ADR secures enterprise AI agents through observability, security benchmarking, and threat detection. Deployed at Uber. · GitHub</a></li>
<li><a href="https://mlsys.org/">2026 Conference</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#AI agents`, `#enterprise`, `#observability`, `#MLSys`

---

<a id="item-3"></a>
## [Jeff Dean and Sanjay Ghemawat Leave Google to Launch Discovery Loop](https://www.discoveryloop.com/) ⭐️ 8.0/10

Jeff Dean, Sanjay Ghemawat, and other senior Google executives have departed Google to co-found Discovery Loop, a public benefit corporation aimed at automating the experimental loop in ML research and engineering. The startup will initially focus on ML research and engineering but plans to scale across many scientific fields. This is significant because it brings together some of the most influential figures in computer science to tackle the automation of scientific experimentation, which could dramatically accelerate discovery in fields like drug development and chip design. The move also signals a major shift in how AI research might be conducted, potentially reshaping the competitive landscape in AI. Discovery Loop is a public benefit corporation, and the founders include Jeff Dean and Sanjay Ghemawat, who co-authored foundational papers on MapReduce, Bigtable, Spanner, and the Google File System. The company aims to automate complex, multi-step scientific and engineering experiments, with an initial focus on ML research and engineering.

hackernews · xtreak29 · Aug 5, 16:19 · [Discussion](https://news.ycombinator.com/item?id=49184960)

**Background**: The experimental loop in research involves iteratively designing experiments, running them, analyzing results, and refining hypotheses. Automating this loop with AI could allow for faster, more efficient scientific discovery. The concept is related to earlier ideas like Karpathy's 'autoresearch' and human-in-the-loop ML systems used in automated experiments.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/jeff-dean-google-discovery-loop-startup/">Google’s Top AI Brains Are Leaving to Launch Discovery Loop | WIRED</a></li>
<li><a href="https://www.techtimes.com/articles/323197/20260805/jeff-dean-sanjay-ghemawat-depart-google-co-found-discovery-loop.htm">Jeff Dean and Sanjay Ghemawat Depart Google to Co-Found Discovery Loop</a></li>
<li><a href="https://www.discoveryloop.com/">Discovery Loop — Continuous Exploration</a></li>

</ul>
</details>

**Discussion**: Community comments reflect a mix of excitement and skepticism. Some see it as a massively scaled version of Karpathy's 'autoresearch' idea, while others question how experimentation can be automated, especially in physical domains. One commenter suggests it's a way for Google to retain senior talent, while another notes the mission statement is complex.

**Tags**: `#automation`, `#machine learning`, `#research`, `#experimentation`, `#AI`

---

<a id="item-4"></a>
## [Meta Ran Ads Containing AI-Generated Child Sexual Abuse Imagery](https://www.wired.com/story/meta-ran-ads-that-contained-ai-generated-child-sexual-abuse-imagery/) ⭐️ 8.0/10

Meta reportedly ran advertisements that contained AI-generated child sexual abuse imagery, raising serious concerns about the effectiveness of its content moderation systems. The ads slipped through despite Meta's stated policies against such material. This incident highlights systemic failures in AI-driven content moderation on major platforms, especially regarding synthetic CSAM, which is increasingly realistic and difficult to detect. It underscores the urgent need for stronger safeguards and regulatory oversight to protect children and maintain platform accountability. The ads reportedly contained AI-generated imagery depicting child sexual abuse, which is illegal and violates Meta's community standards. This comes amid a broader surge in AI-generated CSAM, with reports indicating a significant increase in such content online.

hackernews · malshe · Aug 5, 19:47 · [Discussion](https://news.ycombinator.com/item?id=49187977)

**Background**: AI-generated child sexual abuse material (CSAM) refers to synthetic images or videos created using generative AI, often depicting minors in sexual situations. Detecting such content is challenging because it can be highly realistic and may not match existing databases of known CSAM. Meta uses AI tools like computer vision and machine learning for content moderation, but these systems have limitations, especially with novel synthetic content. The rise of generative AI has made it easier to produce realistic CSAM at scale, posing significant risks to child safety.

<details><summary>References</summary>
<ul>
<li><a href="https://factually.co/fact-checks/technology/detecting-ai-generated-sexual-imagery-methods-reliability-8d727f">What Technical Methods Detect AI ‑ Generated Sexual Imag...</a></li>
<li><a href="https://www.aol.com/articles/reports-ai-generated-child-sexual-082142600.html">Reports of AI - generated child sexual abuse imagery soar by... - AOL</a></li>
<li><a href="https://blog.com.bot/meta-ai-content-moderation/">Meta AI : Role, Tools, and Limitations in Content Moderation</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Meta's moderation failures, noting that similar issues occur on other platforms like YouTube. Some argued that fines are merely a cost of doing business and won't drive change until they hurt financially. Others questioned whether AI moderation is better than human editorial oversight, citing slow response times to reports and inconsistent enforcement.

**Tags**: `#AI safety`, `#content moderation`, `#Meta`, `#ethics`, `#regulation`

---

<a id="item-5"></a>
## [Cloudflare Computer: Virtual Filesystem for Agents in Durable Objects](https://github.com/cloudflare/computer) ⭐️ 8.0/10

Cloudflare has released Cloudflare Computer, a preview package that provides a virtual filesystem inside a Durable Object, with the authoritative state stored in SQLite and exposed through a pluggable execution surface. It ships with three backends: a container with FUSE mount, an isolate shell running just-bash, and an isolate JavaScript backend. This introduces a novel approach to giving AI agents a persistent, unified filesystem with multiple execution environments, potentially simplifying agent infrastructure and enabling more complex agent workflows. It could influence how developers build stateful agent applications on Cloudflare's edge platform. The Durable Object holds authoritative state in SQLite and exposes a single execution entry point via workspace.runtime.exec(source, { backend }). The container backend uses a sandbox-side daemon (computerd) to mount state as a FUSE filesystem and syncs changes over capnweb RPC, while the isolate shell and JavaScript backends run in Dynamic Workers and communicate over Workers RPC. The package is explicitly marked as preview-only, with unstable APIs and not suitable for production use.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: Cloudflare Durable Objects are a special type of Cloudflare Worker that combine compute and storage, enabling stateful serverless applications. FUSE (Filesystem in Userspace) allows userspace programs to implement filesystems, and capnweb is a JavaScript-native RPC protocol developed by Cloudflare. This project leverages these technologies to create a virtual filesystem for agents.

<details><summary>References</summary>
<ul>
<li><a href="https://developers.cloudflare.com/durable-objects/">Overview · Cloudflare Durable Objects docs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Filesystem_in_Userspace">Filesystem in Userspace - Wikipedia</a></li>
<li><a href="https://blog.cloudflare.com/capnweb-javascript-rpc-library/">Cap'n Web: A new RPC system for browsers and web servers | The Cloudflare Blog</a></li>

</ul>
</details>

**Tags**: `#cloudflare`, `#virtual-filesystem`, `#agents`, `#durable-objects`, `#sqlite`

---

<a id="item-6"></a>
## [System Design Primer: Comprehensive Guide for Interview Prep](https://github.com/donnemartin/system-design-primer) ⭐️ 8.0/10

The System Design Primer, a popular open-source repository by Donne Martin, continues to be a top resource for learning large-scale system design and preparing for system design interviews. It includes Anki flashcards and is available in multiple languages, with recent updates and community contributions. System design interviews are a critical component of technical hiring at major tech companies, and this resource provides a structured, comprehensive approach to mastering the topic. Its high community engagement and frequent references make it a valuable asset for engineers at all levels. The repository includes a study guide, sample interview questions with solutions, and Anki flashcards for spaced repetition. It is translated into over 20 languages, and contributions are actively encouraged.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: System design involves architecting scalable and reliable systems, a skill essential for building large-scale applications. The primer organizes scattered web resources into a coherent curriculum, covering topics like load balancing, caching, and database scaling. Anki is a flashcard app that uses spaced repetition to enhance memory retention, making it useful for studying system design concepts.

<details><summary>References</summary>
<ul>
<li><a href="https://apps.ankiweb.net/">Anki - powerful, intelligent flashcards</a></li>
<li><a href="https://play.google.com/store/apps/details?id=com.ichi2.anki&hl=en_US">AnkiDroid Flashcards - Apps on Google Play</a></li>
<li><a href="https://anki-decks.com/">Anki Decks - Generate Flashcards Fast with AI</a></li>

</ul>
</details>

**Discussion**: The community generally praises the primer for its thoroughness and practical value, with many users crediting it for successful interview outcomes. Some discussions highlight the need for more advanced topics and real-world case studies, while others appreciate the active translation efforts.

**Tags**: `#system design`, `#interview prep`, `#scalability`, `#architecture`, `#learning resource`

---

<a id="item-7"></a>
## [Addy Osmani's Agent Skills: Production-Grade Workflows for AI Coding Agents](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released agent-skills, a GitHub repository containing 24 production-grade engineering skills and 8 slash commands that encode senior engineering practices for AI coding agents. The skills can be installed into 70+ agents via the skills CLI, with commands like /spec, /plan, /build, /test, /review, /webperf, /code-simplify, and /ship. This addresses a critical gap in AI-assisted development: agents often skip essential engineering steps like spec writing, testing, and code review, leading to technical debt. By packaging best practices from Google's engineering culture, this repository has the potential to significantly improve code quality and agent reliability across the industry. The skills include concepts like Hyrum's Law in API design, the Beyonce Rule and test pyramid in testing, Chesterton's Fence in simplification, and trunk-based development in git workflow. The /build auto command allows autonomous execution after a single plan approval, with each task still test-driven and committed individually, pausing on failures.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: AI coding agents are tools that autonomously plan, execute, and verify multi-file code changes, but they often lack adherence to engineering processes. The skills CLI from Vercel Labs enables installing these skills into various agents like Claude Code, Cursor, and Copilot. Addy Osmani, formerly at Google Chrome DevRel and now at Anthropic, created this resource to encode senior engineering practices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">GitHub - addyosmani/agent-skills: Production-grade engineering skills for AI coding agents. · GitHub</a></li>
<li><a href="https://dev.to/vikrant_bagal_afae3e25ca7/production-grade-engineering-skills-for-ai-coding-agents-56nb">Production-Grade Engineering Skills for AI Coding Agents - DEV Community</a></li>
<li><a href="https://dev.to/_46ea277e677b888e0cd13/agent-skills-19-production-grade-skills-that-make-ai-coding-agents-work-like-senior-engineers-5bi9">agent-skills: 19 Production-Grade Skills That Make AI Coding Agents Work Like Senior Engineers - DEV Community</a></li>

</ul>
</details>

**Discussion**: The community has responded positively, with the repository gaining over 33,000 stars on GitHub. Developers praise it as a de facto standard for reliable AI-assisted development, though some may question the need for such structured workflows.

**Tags**: `#AI coding agents`, `#software engineering`, `#best practices`, `#developer tools`, `#workflows`

---

<a id="item-8"></a>
## [Superpowers: A New Agentic Skills Framework for Coding Agents](https://github.com/obra/superpowers) ⭐️ 8.0/10

Superpowers is an open-source agentic skills framework and software development methodology for AI coding agents, released on GitHub. It provides a structured approach that includes composable skills and initial instructions to guide agents through a spec-driven, test-driven development process. This framework could significantly improve the effectiveness and reliability of AI coding agents, potentially transforming software development workflows. It is trending on GitHub, indicating strong community interest in structured methodologies for agentic development. Superpowers supports multiple coding agents including Claude Code, Cursor, Codex, and Gemini CLI, with installation via plugin marketplaces. It emphasizes true red/green TDD, YAGNI, and DRY principles, and can run autonomously for hours using a subagent-driven development process.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: Agent skills are a concept introduced by Anthropic, where instructions, scripts, and resources are packaged into composable modules that agents can discover and load dynamically. This allows general-purpose agents to become specialized for specific tasks, improving performance and flexibility.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/obra/superpowers">GitHub - obra/superpowers: An agentic skills framework & software...</a></li>
<li><a href="https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills">Equipping agents for the real world with Agent Skills \ Anthropic</a></li>
<li><a href="https://grokipedia.com/page/Superpowers_agentic_skills_framework">Superpowers (agentic skills framework)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#software-development`, `#agentic-framework`, `#developer-tools`, `#GitHub`

---

<a id="item-9"></a>
## [AirLLM Runs 70B LLMs on 4GB GPU Without Quantization](https://github.com/lyogavin/airllm) ⭐️ 8.0/10

AirLLM, an open-source tool, now enables running 70B parameter large language models on a single 4GB GPU without quantization, distillation, or pruning. It also supports running 405B Llama 3.1 on 8GB, DeepSeek-V3 (671B) on ~12GB, and Kimi K3 (2.8T) on under 4GB VRAM. This breakthrough democratizes access to large language models, allowing researchers and developers with limited hardware to experiment with state-of-the-art models. It challenges the assumption that high-end GPUs are necessary for large model inference, potentially accelerating innovation in edge computing and on-premise deployments. AirLLM uses layer-by-layer streaming inference to minimize VRAM usage, and for sparse MoE models like Kimi K3, it streams one expert at a time. Optional 4-bit and 8-bit block-wise quantization can be enabled for up to 3x speed improvement, though the core feature works without quantization.

rss · GitHub Trending - Daily (All) · Aug 5, 22:51

**Background**: Large language models (LLMs) typically require massive GPU memory due to their billions of parameters, making them inaccessible to most individuals and small organizations. Traditional optimization methods include quantization (reducing numerical precision), distillation (training smaller models), and pruning (removing less important weights), but these often degrade model quality. AirLLM's approach avoids these trade-offs by loading only the necessary parts of the model into memory at a time, using techniques like layer-wise inference and expert streaming for MoE models.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@bnjmn_marie/airllm-layered-inference-for-low-memory-hardware-5af46a960be5">AirLLM: Layered Inference for Low-Memory Hardware - Medium</a></li>
<li><a href="https://www.everydev.ai/tools/airllm">AirLLM - Run Large LLMs Low VRAM | EveryDev.ai</a></li>
<li><a href="https://github.com/lyogavin/airllm">GitHub - lyogavin/airllm: AirLLM 70 B inference with single 4GB GPU</a></li>

</ul>
</details>

**Discussion**: The community has expressed excitement and skepticism. Many praise the technical achievement and its potential to lower barriers, while some question the inference speed and practicality for real-time applications. There are also discussions about the trade-offs between memory savings and latency, with some users sharing benchmarks and comparing it to other optimization techniques.

**Tags**: `#LLM`, `#inference`, `#GPU`, `#memory optimization`, `#open source`

---

<a id="item-10"></a>
## [Self-Organising Digital Circuits Achieve Fault Tolerance via Meta-Learning](https://arxiv.org/abs/2608.02606) ⭐️ 8.0/10

The paper introduces Self-Organising Digital Circuits, a meta-learning architecture that uses a topology-masked Transformer to configure Lookup Tables (LUTs) in digital circuits, enabling self-assembly and fault recovery. It extends Neural Cellular Automata to navigate the Boolean search space for functional logic generation, achieving >99.99% recovery from soft errors. This work bridges biological self-organisation with digital hardware, offering a novel alternative to static fault-tolerance methods like redundancy and error-correcting codes. It could lead to more resilient hardware that adapts to faults dynamically, impacting fields like aerospace, autonomous systems, and critical infrastructure. The architecture uses a topology-masked Transformer to configure LUTs, and the policy generalises across circuit scales, improving accuracy on wider graphs than seen in training. For soft errors, it achieves near-perfect recovery (>99.99% accuracy) even for damage sizes far exceeding training conditions.

rss · arXiv - AI · Aug 5, 04:00

**Background**: Fault tolerance in classical computing relies on static strategies like hardware redundancy and error-correcting codes, while biological systems exhibit adaptive plasticity. Neural Cellular Automata (NCA) are bio-inspired systems where cells iteratively apply local rules to self-organize into complex patterns. Lookup Tables (LUTs) are fundamental components in FPGAs that can implement arbitrary Boolean functions, and configuring them is key to circuit functionality.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.22899">[2506.22899] Neural Cellular Automata: From Cells to Pixels</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lookup_table">Lookup table - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2410.03462v1">Linear Transformer Topological Masking with Graph Random Features</a></li>

</ul>
</details>

**Tags**: `#fault tolerance`, `#meta-learning`, `#neural cellular automata`, `#digital circuits`, `#transformers`

---

<a id="item-11"></a>
## [BLAZE: A Socialized AI Paradigm for Scientific Discovery](https://arxiv.org/abs/2608.02775) ⭐️ 8.0/10

The paper introduces BLAZE (Bridging Literature, Agents, and Zero-gap Experimentation), a new paradigm that treats AI as organizational infrastructure for scientific discovery rather than a mere assistant. It integrates persistent knowledge, collective reasoning, empirical validation, and human judgment into a continuous research lifecycle. This paradigm shift could make scientific discovery more traceable, reproducible, and cumulative, addressing the challenge of organizing expanding knowledge. It may influence how AI is integrated into research across disciplines, potentially accelerating scientific progress while preserving human creativity and responsibility. BLAZE emphasizes that scientific intelligence emerges from sustained interaction among knowledge, hypotheses, experiments, and collective verification, not from computation alone. It aims to extend the scale, depth, and continuity of collective scientific inquiry without replacing human discovery.

rss · arXiv - AI · Aug 5, 04:00

**Background**: Scientific discovery has evolved through paradigms: empirical, theoretical, computational, and data-driven. The paper argues that the next frontier is organizing knowledge, reasoning, and evidence into a coherent process, which BLAZE addresses by socializing AI within the scientific process.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.02775">[2608.02775] Towards a new paradigm of scientific discovery with socialized artificial intelligence</a></li>
<li><a href="https://arxiv.org/html/2608.02775">Towards a new paradigm of scientific discovery with socialized artificial intelligence</a></li>
<li><a href="https://cacm.acm.org/opinion/the-5th-paradigm-ai-driven-scientific-discovery/">The 5th Paradigm: AI-Driven Scientific Discovery – Communications of the ACM</a></li>

</ul>
</details>

**Tags**: `#AI for Science`, `#Scientific Discovery`, `#Multi-agent Systems`, `#Knowledge Organization`

---

<a id="item-12"></a>
## [LLMs Automate Attribution Graph Annotation for Circuit Tracing](https://arxiv.org/abs/2608.02632) ⭐️ 8.0/10

This paper introduces a pipeline that uses LLMs to automatically group individual features or MLP neurons into supernodes for circuit tracing, eliminating the time-intensive manual step. The supernodes generated by the pipeline are shown to be as interpretable as those created by human annotators, and it recovers the intermediate hop in 97 of 100 prompts on a two-hop Capitals task. This work significantly accelerates circuit tracing, a key technique in mechanistic interpretability, by automating a bottleneck step. It could enable large-scale interpretability analysis, making it practical to analyze many more circuits and potentially leading to faster progress in understanding and controlling LLMs. The pipeline directly presents feature descriptions to an LLM, which groups them into supernodes. The paper also demonstrates a proof of concept for open-ended exploration, automatically annotating 1000 attribution graphs from Wikipedia prompt completions and using an LLM judge to flag interesting graphs for human review.

rss · arXiv - Machine Learning · Aug 5, 04:00

**Background**: Attribution graphs are a mechanistic interpretability technique developed by Anthropic that trace the internal circuits a language model uses to turn a prompt into an output. Circuit tracing involves identifying the relevant features and grouping them into supernodes, which is traditionally done manually and is time-consuming. This paper addresses that bottleneck by using LLMs to automate the grouping step.

<details><summary>References</summary>
<ul>
<li><a href="https://aiwiki.ai/wiki/attribution_graphs">Attribution Graphs | AI Wiki</a></li>
<li><a href="https://pub.towardsai.net/mechanistic-interpretability-is-having-its-moment-what-engineers-actually-need-to-know-e4421f305f84">Mechanistic Interpretability Is Having Its Moment: What... | Towards AI</a></li>
<li><a href="https://www.technologyreview.com/2025/03/27/1113916/anthropic-can-now-track-the-bizarre-inner-workings-of-a-large-language-model/">Anthropic can now track the bizarre inner workings of a large language ...</a></li>

</ul>
</details>

**Tags**: `#LLM interpretability`, `#circuit tracing`, `#automation`, `#attribution graphs`, `#mechanistic interpretability`

---

<a id="item-13"></a>
## [Output-Aware Rotation for INT2 KV-Cache Quantization](https://arxiv.org/abs/2608.02691) ⭐️ 8.0/10

The paper introduces OptR, an output-aware rotation method that minimizes post-output-projection attention error for INT2 KV-cache quantization, improving LLM inference efficiency. It consistently outperforms existing rotation-based methods like QuaRot and OSCAR across multiple benchmarks. KV cache is a major memory and bandwidth bottleneck in long-context LLM inference, and ultra-low-bit quantization is crucial. OptR addresses the mismatch between optimizing cache statistics and the actual attention output error, potentially enabling more efficient deployment of LLMs with longer contexts. OptR decomposes the post-W_O attention-output error into key- and value-induced terms and learns per-head orthogonal corrections through the full INT2 quantization and attention path. It also applies an attention-equivalent key reparameterization to reduce large channel-wise offsets without changing the softmax distribution, preserving the paged KV-cache format with negligible inference overhead.

rss · arXiv - Machine Learning · Aug 5, 04:00

**Background**: KV cache quantization reduces memory usage by storing keys and values in lower precision, but aggressive quantization like INT2 can introduce significant errors. Rotation-based methods aim to mitigate outliers by rotating the activation space, but previous approaches optimized proxy errors rather than the final attention output. OptR directly targets the post-output-projection error, aligning quantization with the actual model behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.02691">Output-Aware Rotation for INT 2 KV-Cache Quantization</a></li>
<li><a href="https://arxiv.org/abs/2401.18079">[2401.18079] KVQuant: Towards 10 Million Context Length LLM Inference with KV Cache Quantization</a></li>

</ul>
</details>

**Tags**: `#KV-cache quantization`, `#LLM inference`, `#quantization`, `#attention mechanism`, `#efficiency`

---

<a id="item-14"></a>
## [MemArena: New Benchmark for On-Device Personal Memory Assistants](https://arxiv.org/abs/2608.02613) ⭐️ 8.0/10

MemArena is a new ego-centric benchmark for evaluating on-device personal memory assistants, built with the MASim agent simulator. It simulates 50 agents over 15 days, generating 10.3M dialog tokens and 24.1K ego-observed tokens per agent per day, and evaluates five open-weight readers with various memory backends. This benchmark addresses a critical gap in evaluating ego-centric, multi-session conversational memory for on-device assistants, which is essential for privacy-preserving edge AI. The finding that memory backend choice impacts accuracy more than model scaling could guide system design and resource allocation in real-world deployments. The benchmark evaluates six dimensions: recall, reasoning, and trustworthiness. Results show that switching from Memobase to MemSearch improves accuracy by +32.5/+19.2 percentage points at Qwen3-0.6B, exceeding gains from scaling the reader model (+10.6/+6.8 pp). Permission-aware access fails universally, with Oracle leaking heavily and other backends being too timid. On a Spark GB10 edge node, memory search adds a fixed latency of 87/7/48 ms for BM25-RAG/Memobase/MemSearch.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: On-device personal memory assistants are AI systems that run locally on edge devices to manage private interpersonal conversations, using open-weight models. Existing memory benchmarks often fail to combine activity-dense interaction, ego-centric perspective, and coherent multi-session worlds. MemArena fills this gap by providing a single-world conversational benchmark with ground truth for multiple evaluation dimensions, enabling systematic comparison of memory backends and reader models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.02613">[2608.02613] MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale</a></li>
<li><a href="https://arxiv.org/html/2608.02613">MemArena: An Ego-Centric Benchmark for On-Device Agentic Personal Memory Assistants at Scale</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#memory systems`, `#edge AI`, `#LLM`, `#personal assistants`

---

<a id="item-15"></a>
## [OncoTriad-QA: New Benchmark Integrates Radiology, Pathology, Genomics for Cancer QA](https://arxiv.org/abs/2608.02615) ⭐️ 8.0/10

Researchers introduced OncoTriad-QA, a patient-level benchmark for pan-cancer question answering that integrates radiology, pathology, genomics, and clinical data across 32 cancer types. It includes 86.1k questions from 9,281 TCGA patient cases, along with a reference multimodal model called OncoVLM. This benchmark addresses a critical gap in medical AI evaluation by enabling patient-level, multi-modal reasoning across diverse cancer types. It provides a comprehensive testbed for developing and assessing medical LLMs and VLMs, potentially accelerating progress toward integrated cancer diagnosis and treatment support. OncoTriad-QA aligns CT/MRI radiology, whole-slide histopathology, somatic mutations, copy-number alterations, DNA methylation, bulk RNA-seq, and clinical metadata. The reference model OncoVLM, after fine-tuning on the benchmark, outperformed MedGemma-4B by an average of 10.7 points in MCQ accuracy and BERTScore-F1 across multiple settings.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: Cancer diagnosis typically requires integrating diverse evidence from imaging, pathology, and molecular profiling. However, most existing medical LLM/VLM benchmarks focus on single modalities or narrow tasks, lacking patient-level integration. TCGA (The Cancer Genome Atlas) is a landmark program that molecularly characterized over 11,000 cancer cases, providing the data foundation for this benchmark.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cancer.gov/ccg/research/genome-sequencing/tcga">The Cancer Genome Atlas Program ( TCGA ) - NCI</a></li>
<li><a href="https://arxiv.org/pdf/2608.02615">OncoTriad-QA: A Patient -Level Radiology-Pathology-Genomics...</a></li>

</ul>
</details>

**Tags**: `#medical AI`, `#benchmark`, `#multi-modal`, `#cancer`, `#LLM`

---

<a id="item-16"></a>
## [OpenAI Privacy Filter Fails on Narrative Prose and Non-Latin Scripts](https://arxiv.org/abs/2608.02616) ⭐️ 8.0/10

An independent evaluation of OpenAI's Privacy Filter (OPF) across 42 benchmarks spanning 22 languages and 5 domains reveals that while OPF excels on structured PII, it degrades sharply on narrative prose and non-Latin scripts, with F1 scores as low as 0.04 for Arabic and 0.03 for Cyrillic. This evaluation provides critical insights into the strengths and weaknesses of a widely used privacy tool, highlighting the need for more robust multilingual and context-aware PII detection. It has significant implications for privacy technology and multilingual NLP, especially for users relying on OPF for data anonymization in diverse linguistic contexts. Zero-shot, OPF achieves F1=0.855 on AI4Privacy and 0.464 on SPY medical, outperforming Presidio and XLM-RoBERTa on PII-annotated benchmarks, but XLM-RoBERTa leads on all 13 Indic and non-Latin languages. OPF is strongest on structurally regular PII (email: 0.78, phone: 0.76) and weakest on culturally variable ones (person: 0.40, address: 0.49), with global precision ranging from 0.31 to 0.86.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: OpenAI Privacy Filter (OPF) is a 1.5B-parameter bidirectional token classifier designed to detect personally identifiable information (PII) across eight categories, including account numbers, secrets, and more. It is pretrained autoregressively and converted into a bidirectional classifier, similar to the gpt-oss architecture. Presidio is an open-source framework for PII detection and anonymization, while XLM-RoBERTa is a multilingual masked language model trained on 100 languages. This evaluation compares these tools across diverse benchmarks to assess their real-world applicability.

<details><summary>References</summary>
<ul>
<li><a href="https://openai.com/index/introducing-openai-privacy-filter/">Introducing OpenAI Privacy Filter | OpenAI</a></li>
<li><a href="https://huggingface.co/openai/privacy-filter">openai/privacy-filter · Hugging Face</a></li>
<li><a href="https://huggingface.co/docs/transformers/en/model_doc/xlm-roberta">XLM-RoBERTa · Hugging Face</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#PII detection`, `#OpenAI`, `#multilingual NLP`, `#benchmark`

---

<a id="item-17"></a>
## [Pairwise Preference Is a Poor Proxy for Clinical Safety in LLMs](https://arxiv.org/abs/2608.02617) ⭐️ 8.0/10

A new study using the MOOVE platform analyzed 26,804 pairwise judgments from over 736 clinicians across 28+ countries, evaluating 13 LLMs, and found that clinician pairwise preferences are a poor proxy for clinical safety. Models that rank highly under pairwise preference can still exhibit substantial rates of clinically meaningful failures on dimensions such as Harmlessness and Accuracy. This finding challenges the common practice of using pairwise preference as a proxy for safety in LLM evaluation, especially in high-stakes fields like healthcare. It underscores the need for evaluation methods that directly measure safety-critical failures and incorporate clinically grounded adjustments, which could lead to safer deployment of medical AI systems. The study introduces a clinically adjusted preference ranking that combines pairwise preference with rubric-derived feedback, producing a more safety-aware ordering than raw Bradley–Terry strength alone. It also analyzes contributing factors such as prompt length, refusal and escalation behavior, and finds that surface-level characteristics explain slightly more preference variation than safety-critical rubric differences.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: Pairwise preference is a common method for evaluating LLMs, where human judges compare two outputs and choose the better one. However, in clinical settings, safety is paramount, and this study shows that preference may not align with safety. The MOOVE platform is a global initiative that collects clinician feedback on medical AI outputs, providing a large dataset for such analyses.

<details><summary>References</summary>
<ul>
<li><a href="https://jointhemoove.org/">MOOVE | Massive Open Online Validation & Evaluation</a></li>
<li><a href="https://arxiv.org/pdf/2403.16950">Aligning with Human Judgement: The Role of Pairwise Pref</a></li>
<li><a href="https://github.com/JJRober/llm-clinical-safety-framework">GitHub - JJRober/ llm - clinical - safety -framework: Evaluating Large...</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#clinical safety`, `#AI in healthcare`, `#pairwise preference`, `#safety-critical AI`

---

<a id="item-18"></a>
## [JudgeArena: Unified Framework for Reproducible LLM-Judge Evaluation](https://arxiv.org/abs/2608.02620) ⭐️ 8.0/10

JudgeArena is an open-source framework that unifies major LLM-judge benchmarks (AlpacaEval, Arena-Hard, MT-Bench, and m-Arena-Hard) under a single interface, allowing swappable judges and comprehensive metadata logging. It also provides tuned judge configurations for open models that match or outperform closed-model judges, and can simulate LMArena Elo scores with high accuracy. This framework addresses the fragmentation in LLM-as-a-judge evaluation, enabling systematic and reproducible studies of how design choices affect model quality conclusions. It reduces reliance on opaque closed-model judges and offers a low-cost alternative to large-scale human annotation, benefiting the research community and industry practitioners. JudgeArena supports any model accessible via vLLM, llama.cpp, or OpenRouter as both candidate and judge. The framework includes tuned judge configurations validated on human preference datasets in English and multilingual settings, and can simulate LMArena Elo scores by combining human annotations with LLM-judge evaluations.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: LLM-as-a-judge is an evaluation methodology where a large language model assesses the quality of outputs from another LLM, using a scoring rubric. Benchmarks like AlpacaEval and Arena-Hard are popular for evaluating instruction-following models, but they often have separate codebases and hardcoded judges, making comparisons difficult. JudgeArena aims to standardize this process.

<details><summary>References</summary>
<ul>
<li><a href="https://langfuse.com/docs/evaluation/evaluation-methods/llm-as-a-judge">LLM - as - a - Judge - Langfuse</a></li>
<li><a href="https://github.com/lmarena/arena-hard-auto">GitHub - lmarena/arena-hard-auto: Arena-Hard-Auto: An automatic LLM benchmark. · GitHub</a></li>
<li><a href="https://klu.ai/glossary/alpaca-eval">AlpacaEval — Klu</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#LLM-as-a-judge`, `#benchmarking`, `#reproducibility`, `#open-source`

---

<a id="item-19"></a>
## [Diagnosing and Repairing Interface Injury in KDA Linearized 0.6B Model](https://arxiv.org/abs/2608.02689) ⭐️ 8.0/10

Researchers converted 21 of 28 full-attention layers of Qwen3-0.6B-Base into KDA linear-attention layers on a single consumer GPU, and found that while perplexity and hidden-state alignment improved, multiple-choice accuracy remained near random. They introduced a four-permutation diagnostic that revealed the model was sticking to option labels (predicting 'A' 81% of the time) rather than following content, and repaired this with a 1,000-step format-targeted completion-only KL distillation stage. This work highlights a critical failure mode in model conversion and distillation: standard metrics like perplexity can mask 'interface injuries' where models rely on superficial cues rather than understanding content. The proposed diagnostic and repair method offers a practical approach for improving the reliability of linearized attention models, which are important for efficient inference in large language models. The four-permutation test rotates answer options while keeping content fixed, revealing label-stickiness (106/161 questions kept the same label under all rotations). The repair stage improved C-Eval accuracy by +12.48 points and roughly halved label-stickiness, while subsequent persona SFT and one round of on-policy DPO preserved benchmark scores within noise. The paper also documents an FP32-master failure mode where bf16 optimizer updates were silently swallowed, which was critical for convergence.

rss · arXiv - NLP · Aug 5, 04:00

**Background**: Linear attention mechanisms, such as Kimi Delta Attention (KDA), aim to reduce the quadratic complexity of standard attention, enabling longer contexts and faster inference. However, converting pre-trained full-attention models to linear attention often degrades performance, and this paper investigates what exactly breaks. The four-permutation test is a novel diagnostic that distinguishes between content-based and label-based answering, which is not captured by perplexity or KL divergence.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/magickong/learn-linear-attention-from-kimi-k3s-kda-mechanism-in-20-lines-of-python-cop">Learn Linear Attention From Kimi K3's KDA ... - DEV Community</a></li>
<li><a href="https://arxiv.org/pdf/2510.26692">Kimi Linear : An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://snowchord.com/blog/linear-attention-visualized/">Linear Attention , Visualized: From Mamba-2 to KDA | Haoran Zhang</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#linear attention`, `#distillation`, `#diagnostics`, `#model conversion`

---

<a id="item-20"></a>
## [Hunyuan3D-Buffalo 1.0: Unified Multimodal Model for 3D Generation, Understanding, and Editing](https://arxiv.org/abs/2608.02711) ⭐️ 8.0/10

Hunyuan3D-Buffalo 1.0 is a unified multimodal framework that integrates 3D understanding, text-to-3D generation, instruction-guided 3D editing, and text-grounded part generation within a single architecture. It is trained on an 87M-scale 3D multimodal corpus, including 25M understanding samples, 50M text-to-3D pairs, and 12M editing pairs generated using Nano3D-v2. This work addresses a critical gap in unified 3D modeling by providing a large-scale, geometrically consistent dataset and a single model that handles multiple 3D tasks. It achieves state-of-the-art performance on text-to-3D generation and editing benchmarks, potentially accelerating research and applications in 3D content creation, virtual reality, and gaming. The framework combines Hunyuan3D-VLM for semantic, structural, and spatial understanding with Hunyuan3D DiT for high-fidelity 3D synthesis. The VLM provides multimodal semantic conditions, while editing and part generation also condition on the source object representation to preserve structure and unedited regions.

rss · arXiv - Computer Vision · Aug 5, 04:00

**Background**: Recent advances in image generation have shown the potential of unified multimodal models that integrate understanding, generation, and editing. However, unified 3D modeling has been limited by scarce multimodal data, especially the lack of large-scale and geometrically consistent editing data. This paper proposes a unified framework and constructs a large corpus to overcome this limitation.

<details><summary>References</summary>
<ul>
<li><a href="https://tencent-hunyuan.github.io/Hunyuan3D-Buffalo1.0/">Hunyuan 3 D -Buffalo 1.0</a></li>
<li><a href="https://arxiv.org/html/2608.02711v1">Hunyuan 3 D -Buffalo 1.0 A Unified Multimodal Model for Scalable...</a></li>
<li><a href="https://dev.to/y_hnhnhan_2f26de65ffcc4/top-ai-papers-on-hugging-face-2026-08-05-3oeo">Top AI Papers on Hugging Face - 2026-08-05 - DEV Community</a></li>

</ul>
</details>

**Discussion**: The community has shown positive interest, with the paper being highlighted as a top AI paper on Hugging Face. Discussions likely focus on the novelty of the unified architecture and the scale of the dataset, though no specific comments were provided.

**Tags**: `#3D generation`, `#multimodal learning`, `#text-to-3D`, `#3D editing`, `#diffusion models`

---

<a id="item-21"></a>
## [Agent-Centric World Proxies Redefine World Modeling](https://arxiv.org/abs/2608.02713) ⭐️ 8.0/10

The paper 'Quo Vadis, World Modeling?' introduces Agent-Centric Interactive World Proxies, shifting world modeling from physical state prediction to agent-usable information transitions. It organizes these proxies into six functional forms and three progressive empowerment levels for continual agent improvement. This paradigm shift addresses a key limitation in current world models, which are often too narrow for actionable agent feedback. It could significantly impact AI agent development by enabling more versatile and efficient learning, planning, and evolution in real-world applications. The six proxy forms are dynamics, spatial, execution, memory/experience, skill, and reward/verification proxies. The three empowerment levels are L.1 Inference-Time Guidance, L.2 Training-Time Optimization, and L.3 Agent-Proxy Co-Evolution, which together characterize how world modeling serves agent improvement.

rss · arXiv - Computer Vision · Aug 5, 04:00

**Background**: World models in reinforcement learning typically predict future physical states to simulate environments, but this is often insufficient for agents needing actionable feedback. The paper generalizes this concept to 'world proxies'—environment-grounded interfaces that return information transitions (e.g., execution outcomes, retrieved experiences) to support continual learning. This builds on prior work in model-based RL and world models, such as DIAMOND, which uses diffusion models for visual world modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2608.02713">Quo Vadis, World Modeling? | alphaXiv</a></li>
<li><a href="https://worldbench.github.io/awesome-agentic-world-model/">Quo Vadis, World Modeling?</a></li>
<li><a href="https://arxiv.org/html/2608.02713">1 Conceptual shift and design space of Agent-Centric World Proxies. We shift from world models for physical state prediction to interactive world proxies for information transition prediction, enabling continual agent improvement through six proxy functions and three empowerment levels: L.1 inference-time guidance, L.2 training-time optimization, and L.3 Agent-Proxy co-evolution.</a></li>

</ul>
</details>

**Tags**: `#world models`, `#reinforcement learning`, `#AI agents`, `#interactive learning`, `#arXiv`

---

<a id="item-22"></a>
## [Vision-Language Models Show Poor Confidence Calibration on Brain MRI](https://arxiv.org/abs/2608.02790) ⭐️ 8.0/10

A behavioral safety audit of six vision-language models on brain MRI reveals that their verbalized confidence is poorly calibrated, with models often highly confident even when incorrect. The study, using 4,102 images, found ECE values ranging from 0.27 to 0.40 and 33-46% of answered items being high-confidence errors. This matters because it highlights a critical safety issue for deploying VLMs in medical imaging, where overconfident errors could mislead clinicians and harm patients. The findings argue for evaluating confidence reliability alongside accuracy in medical AI, potentially influencing future model development and regulatory standards. The audit covered five general-purpose and one medical specialist VLM, using automatically graded labels from public metadata and expert segmentation masks. Notably, the most accurate model was also the most confident on its errors, and medical adaptation improved tumor detection without improving confidence calibration.

rss · arXiv - Computer Vision · Aug 5, 04:00

**Background**: Vision-language models (VLMs) combine image and text understanding, and are increasingly proposed for medical imaging tasks. Confidence calibration measures how well a model's expressed certainty matches its actual accuracy; poor calibration can lead to over-trust in AI outputs. Expected Calibration Error (ECE) is a common metric for quantifying miscalibration.

<details><summary>References</summary>
<ul>
<li><a href="https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/">Expected Calibration Error (ECE): A Step-by-Step Visual Explanation | Towards Data Science</a></li>
<li><a href="https://arxiv.org/html/2501.19047v2">Understanding Model Calibration - A gentle introduction and visual exploration of calibration and the expected calibration error (ECE)</a></li>
<li><a href="https://precious-okoro.medium.com/confidence-calibration-the-ai-design-problem-no-one-is-talking-about-d89d74c5db45">Confidence Calibration : The AI Design Problem No One Is... | Medium</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#medical imaging`, `#AI safety`, `#confidence calibration`, `#brain MRI`

---

<a id="item-23"></a>
## [SAGE: Semantic Global Explanations for Attention-Based Survival Models in Pathology](https://arxiv.org/abs/2608.02803) ⭐️ 8.0/10

SAGE is a novel post-hoc framework that provides global, language-grounded explanations for attention-based multiple instance learning (ABMIL) survival models in computational pathology. It aggregates vision-language model concept scores with learned attention to quantify how histological concepts relate to prediction risk across a cohort. This addresses a significant gap in interpretability of ABMIL survival models, which previously only offered local attention maps. By enabling cohort-level, semantic explanations, SAGE can help pathologists understand model behavior, validate against known biology, and potentially identify new biomarkers, impacting clinical adoption and research. SAGE was applied to seven TCGA cancer cohorts and three foundation models, recovering established prognostic features like necrosis and revealing cancer-specific biology such as a favorable angiogenic signature in renal cell carcinoma. Ablation studies confirmed that associations depend on learned attention, not just concept prevalence, and that the concept dictionary captures much of the prognostic information in foundation model features.

rss · arXiv - Computer Vision · Aug 5, 04:00

**Background**: Attention-based multiple instance learning (ABMIL) is a common approach for slide-level prediction in computational pathology, but its attention maps only show where the model focuses, not what features drive predictions. Vision-language models (VLMs) like those used in pathology can score image patches against semantic concepts, enabling language-grounded explanations. TCGA (The Cancer Genome Atlas) is a landmark program that molecularly characterized thousands of cancer samples across many cancer types, providing a rich resource for validating prognostic features.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cancer.gov/ccg/research/genome-sequencing/tcga">The Cancer Genome Atlas Program (TCGA) - NCI</a></li>
<li><a href="https://www.emergentmind.com/topics/attention-based-multiple-instance-learning-abmil">Attention - Based Multiple Instance Learning</a></li>

</ul>
</details>

**Tags**: `#computational pathology`, `#explainability`, `#attention-based multiple instance learning`, `#survival analysis`, `#vision-language models`

---

<a id="item-24"></a>
## [In-Context Collapse in VLMs: A New Failure Mode and Mitigation](https://arxiv.org/abs/2608.02830) ⭐️ 8.0/10

This paper identifies a phenomenon called 'in-context collapse' in vision-language models (VLMs), where adding more demonstrations in many-shot in-context learning sharply degrades performance, sometimes below chance. The authors propose a mitigation called CircA, a one-time integration vaccine that transfers collapse-resistance to unseen task families. This finding challenges the common assumption that more demonstrations always improve in-context learning, which has significant implications for deploying VLMs in few-shot and many-shot settings. The proposed lightweight intervention could enable more reliable use of VLMs across various tasks without expensive fine-tuning. The collapse is graded across an open VLM panel (0.5B–11B) and a frontier model (Claude Sonnet 4.5), and is causally localized to the vision-language integration pathway via lesion-and-rescue experiments. An adapter on the connector and early/mid layers restores genuine learning (remap accuracy 0.39→0.91 at 16 shots), while an equal-capacity adapter on the late readout does not.

rss · arXiv - Computer Vision · Aug 5, 04:00

**Background**: In-context learning (ICL) allows models to adapt to new tasks by providing demonstrations in the prompt without updating weights. Many-shot ICL, which uses hundreds or thousands of examples, has been shown to improve performance in large language models, but its effect on vision-language models is less understood. This paper reveals a failure mode specific to VLMs where the integration of visual and linguistic information breaks down as context length grows.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.02830">In - Context Collapse in Vision - Language Models and How to...</a></li>
<li><a href="https://arxiv.org/abs/2404.11018">[2404.11018] Many - Shot In - Context Learning</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#in-context learning`, `#AI safety`, `#machine learning`, `#arXiv`

---

<a id="item-25"></a>
## [Unified Particle-Based Stochastic Optimization Framework with Convergence Guarantees](https://arxiv.org/abs/2608.02844) ⭐️ 8.0/10

This paper introduces a general class of diffusion-based stochastic particle optimization methods for loss functions with intractable gradients, unifying existing algorithms and enabling new variants. It proves exponential convergence and provides non-asymptotic error bounds under well-posedness and joint contractivity assumptions. This framework addresses critical problems like training generative models and energy-based models, which often involve intractable gradients. By unifying and extending existing particle-based methods, it could lead to more efficient and theoretically grounded optimization algorithms, impacting machine learning research and applications. The paper introduces mean-field dynamics and its interacting-particle approximations, which contain several existing algorithms as special cases. It illustrates the framework by developing momentum and higher-order Langevin variants, evaluated on maximum marginal-likelihood estimation and energy-based-model training.

rss · arXiv - Data Science & Statistics · Aug 5, 04:00

**Background**: Particle-based optimization methods use a set of interacting particles to explore the loss landscape, often inspired by physical or stochastic processes. Langevin dynamics, a key component, iteratively samples from a distribution using gradient information, and is widely used in machine learning, particularly in diffusion models. Energy-based models (EBMs) are a class of generative models that define an unnormalized probability distribution, and training them often requires sampling from the model distribution, which can be challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mathematical_optimization">Mathematical optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Energy-based_model">Energy-based model - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2101.03288">[2101.03288] How to Train Your Energy-Based Models</a></li>

</ul>
</details>

**Tags**: `#optimization`, `#stochastic methods`, `#particle methods`, `#machine learning`, `#Langevin dynamics`

---

<a id="item-26"></a>
## [Causal Inference for Unstructured Outcomes via Maximally Contrasting Features](https://arxiv.org/abs/2608.03085) ⭐️ 8.0/10

This paper introduces a novel causal query for unstructured outcomes like text and images, proposing the maximally contrasting feature (MCF) to identify the most causally affected aspects. It provides identification conditions, estimation algorithms, and extensions to heterogeneous effects and unstructured treatments. This work addresses a fundamental gap in causal inference, where traditional scalar outcomes are ill-defined for unstructured data. It has high potential impact on fields like healthcare and social science, enabling researchers to ask causal questions about complex outcomes such as clinical notes and survey responses. The MCF is learned by training a feature-scoring function that maps each outcome to a scalar, maximizing the contrast between treated and control potential outcomes. The method also handles settings where both treatment and outcome are unstructured, and empirical studies on text and images demonstrate its effectiveness.

rss · arXiv - Data Science & Statistics · Aug 5, 04:00

**Background**: Traditional causal inference focuses on scalar outcomes, such as recovery status or income, where average treatment effects are well-defined. However, modern studies often involve unstructured outcomes like text or images, where subtraction is meaningless. This paper proposes a new causal query that learns the most affected features, providing a way to define and estimate causal effects in such settings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.03085">Causal Inference with Unstructured Outcomes</a></li>
<li><a href="https://arxiv.org/pdf/2608.03085">Causal Inference with Unstructured Outcomes</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#unstructured data`, `#machine learning`, `#treatment effects`, `#arxiv`

---

<a id="item-27"></a>
## [Minimax-Optimal Policy for Contextual Dynamic Pricing with Multimodal Revenue](https://arxiv.org/abs/2608.03142) ⭐️ 8.0/10

The paper introduces a pilot-corrected layered decision-partitioning policy for contextual dynamic pricing under a semiparametric surplus-index model, achieving minimax-optimal regret up to logarithmic factors. This policy handles arbitrary covariate sequences, bounded nonbinary purchase quantities, and nonconcave, non-unimodal revenue functions. This work resolves a significant open problem in dynamic pricing by providing a policy that achieves minimax optimality under weak assumptions, without requiring concavity or strong unimodality of revenue. It offers a theoretically grounded approach with practical relevance for pricing in complex, multimodal demand settings, likely influencing future research in pricing and online learning. The policy combines directional pilot estimation, local polynomial learning, predictable data assignment, and global action elimination. Pilot correction removes the first-order effect of valuation-parameter error, while permanent labels enable concentration under adaptive sampling; the regret rate matches a lower bound for a constant-context binary-demand subclass.

rss · arXiv - Data Science & Statistics · Aug 5, 04:00

**Background**: Contextual dynamic pricing involves setting prices based on customer features to maximize revenue over time, where demand is unknown and must be learned. The semiparametric surplus-index model assumes a linear valuation parameter and a smooth response function, allowing flexible demand shapes. Minimax optimality refers to achieving the best possible worst-case regret, a key performance measure in online learning.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.03142">[2608.03142] Minimax-Optimal Semiparametric Contextual Dynamic...</a></li>
<li><a href="https://arxiv.org/html/2608.03142v1">Minimax - Optimal Semiparametric Contextual Dynamic Pricing with...</a></li>
<li><a href="https://pubsonline.informs.org/doi/abs/10.1287/opre.2025.1779?journalCode=opre">Minimax Optimality in Contextual Dynamic Pricing with General...</a></li>

</ul>
</details>

**Tags**: `#dynamic pricing`, `#semiparametric estimation`, `#minimax optimality`, `#contextual bandits`, `#machine learning`

---

<a id="item-28"></a>
## [GFlowNets Training via Information Geometry and Natural Gradients](https://arxiv.org/abs/2608.03967) ⭐️ 8.0/10

This paper introduces an information-geometric formulation of forward policy training in GFlowNets, showing that the intrinsic geometry is given by the Fisher-Rao metric and deriving natural gradient updates. It also provides an exact decomposition of the trajectory Fisher information into per-step conditional second moments, leading to three computational regimes for tractable updates. This work bridges GFlowNets with information geometry, offering a principled way to incorporate target structure into optimization geometry, potentially improving convergence and exploration in amortized inference and generative modeling. The decomposition of trajectory Fisher information clarifies when temporal score interactions vanish, guiding practical algorithm design. The paper identifies three computational regimes: exact Fisher information, Monte Carlo estimation, and structure-exploitable approximations using graphical-model tools like belief propagation. Empirical comparisons show convergence and exploration behavior under Riemannian versus Euclidean optimization.

rss · arXiv - Data Science & Statistics · Aug 5, 04:00

**Background**: Generative Flow Networks (GFlowNets) are a framework for amortized inference over discrete and mixed discrete-continuous objects, where an unnormalized target density is specified via a reward. The Fisher information matrix measures the amount of information a random variable carries about an unknown parameter, and natural gradient descent uses it to account for the curvature of the parameter space, often improving convergence. This paper applies these concepts to GFlowNets to derive structure-aware training updates.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fisher_information_matrix">Fisher information matrix</a></li>
<li><a href="https://mj10.github.io/blog/2023/gflownets-scientific-discovery/">GFlowNets and Scientific Discovery | Moksh Jain</a></li>
<li><a href="https://andrewcharlesjones.github.io/journal/natural-gradients.html">Natural gradients</a></li>

</ul>
</details>

**Tags**: `#GFlowNets`, `#information geometry`, `#natural gradient`, `#amortized inference`, `#generative models`

---