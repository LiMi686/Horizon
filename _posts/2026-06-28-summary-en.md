---
layout: default
title: "Horizon Summary: 2026-06-28 (EN)"
date: 2026-06-28
lang: en
---

> From 46 items, 7 important content pieces were selected

---

1. [GLM 5.2 Beats Claude in Cybersecurity Benchmarks](#item-1) ⭐️ 8.0/10
2. [Developer Uses Claude Code to Analyze His Own MRI](#item-2) ⭐️ 8.0/10
3. [Jon Udell: Reframe 'Human in the Loop' as 'Agent in the Loop'](#item-3) ⭐️ 8.0/10
4. [SimpleX Chat: Messaging Without Any User Identifiers](#item-4) ⭐️ 8.0/10
5. [Openpilot: Open-Source ADAS for 300+ Cars](#item-5) ⭐️ 8.0/10
6. [Free-for-Dev: Curated List of Free Cloud Tiers](#item-6) ⭐️ 8.0/10
7. [dbt Core v2.0 Alpha: Rust Rewrite for Speed](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [GLM 5.2 Beats Claude in Cybersecurity Benchmarks](https://semgrep.dev/blog/2026/we-have-mythos-at-home-glm-52-beats-claude-in-our-cyber-benchmarks/) ⭐️ 8.0/10

GLM 5.2, a 753-billion-parameter open-source Mixture-of-Experts model, outperforms Claude in Semgrep's cybersecurity vulnerability detection benchmarks, achieving a 38% detection rate at $0.17 per vulnerability found. This demonstrates that open-source models can now compete with proprietary leaders in specialized domains like cybersecurity, potentially lowering costs and increasing accessibility for security teams. GLM 5.2 uses a Mixture-of-Experts architecture with 753B total parameters but activates only a subset per token, making inference efficient. It also features a 1M-token context window and improved speculative decoding.

hackernews · jms703 · Jun 28, 17:50 · [Discussion](https://news.ycombinator.com/item?id=48709670)

**Background**: Large language models are increasingly used for code analysis and vulnerability detection. Semgrep's benchmark tests models on finding real-world security bugs. GLM 5.2 is the latest in the GLM series, fully open-weight and commercially usable.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/zai-org/GLM-5.2">zai-org/GLM-5.2 · Hugging Face</a></li>
<li><a href="https://openlm.ai/glm-5.2/">GLM-5.2 - openlm.ai</a></li>
<li><a href="https://www.mindstudio.ai/blog/what-is-glm-5-2-open-weight-model-3">What Is GLM 5.2? The Open-Weight Model Competing with Claude Opus on Coding | MindStudio</a></li>

</ul>
</details>

**Discussion**: Commenters noted GLM 5.2's strong performance in daily programming tasks, with one user spending only $20 for a two-day coding session. Others questioned the benchmark methodology, pointing out that Claude Code is an agent harness, not a pure LLM. Some expressed surprise at China's rapid progress in open-source AI.

**Tags**: `#LLM`, `#benchmark`, `#cybersecurity`, `#open-source`, `#AI`

---

<a id="item-2"></a>
## [Developer Uses Claude Code to Analyze His Own MRI](https://antoine.fi/mri-analysis-using-claude-code-opus) ⭐️ 8.0/10

A developer used Anthropic's Claude Code, an AI coding assistant, to analyze his own shoulder MRI images and received a second opinion that aligned with his eventual diagnosis. The experiment demonstrates a novel personal application of large language models in medical image interpretation. This case highlights both the potential of AI to empower patients with accessible second opinions and the serious risks of misdiagnosis, trust, and clinical oversight. It sparks debate among radiologists and patients about the role of AI in healthcare, especially as LLMs become more capable. The developer used Claude Code (likely the Opus model) to analyze his MRI without any medical training, and the AI's findings matched his doctor's diagnosis. However, the community notes that AI can make mistakes in describing images and reasoning, even when the final answer is correct, as shown in NIH research.

hackernews · engmarketer · Jun 28, 16:35 · [Discussion](https://news.ycombinator.com/item?id=48708941)

**Background**: Claude Code is a tool built on Anthropic's Claude large language model, which is trained using constitutional AI to improve ethical compliance. AI in healthcare has shown promise but also carries risks of bias, errors, and patient safety concerns, requiring validation and oversight. The developer's experiment is a grassroots example of using LLMs for personal medical analysis, a practice not yet clinically validated.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Code">Claude Code</a></li>
<li><a href="https://aihealthcare360.org/foundations/risks-of-ai-in-healthcare/">Risks of AI in Healthcare: Bias, Errors, and Patient Safety</a></li>
<li><a href="https://www.nih.gov/news-events/news-releases/nih-findings-shed-light-risks-benefits-integrating-ai-into-medical-decision-making">NIH findings shed light on risks and benefits of integrating ...</a></li>

</ul>
</details>

**Discussion**: Community comments reveal a mix of fascination and caution. A radiologist notes the need for full 3D datasets to evaluate AI accuracy, while others share personal misdiagnosis stories and question the deterministic view of diagnosis. Some appreciate the ability to ask AI questions without time pressure, but many emphasize that AI cannot yet be fully trusted for medical decisions.

**Tags**: `#AI in Healthcare`, `#Medical Diagnosis`, `#LLM Applications`, `#Patient Empowerment`, `#Radiology`

---

<a id="item-3"></a>
## [Jon Udell: Reframe 'Human in the Loop' as 'Agent in the Loop'](https://simonwillison.net/2026/Jun/28/jon-udell/#atom-everything) ⭐️ 8.0/10

Jon Udell proposes reframing 'human in the loop' as 'agent in the loop' to emphasize that humans remain in control, inviting AI agents as team members rather than being excluded from the process. This reframing shifts the narrative from human oversight of AI to human-led collaboration with AI agents, which could influence how teams design agentic software development workflows and maintain human agency. Udell specifically warns against agents creating unreviewable pull requests, advocating for transparent, human-invited agent participation rather than black-box feature generation.

rss · Simon Willison · Jun 28, 21:57

**Background**: The traditional 'human in the loop' (HITL) concept places a human as a supervisor or validator of AI actions, often implying the AI drives the process. 'Agent in the loop' flips this by asserting that humans own the workflow and invite AI agents as collaborators. This distinction is increasingly relevant as AI agents become more autonomous in software development, raising concerns about unreviewable code changes.

<details><summary>References</summary>
<ul>
<li><a href="https://community.ibm.com/community/user/blogs/anuj-bahuguna/2025/05/25/ai-in-the-loop-vs-human-in-the-loop">AI in the Loop vs Human in the Loop: A Technical Analysis of ...</a></li>
<li><a href="https://www.trantorinc.com/blog/human-in-the-loop-vs-fully-autonomous-ai-agents">Human-in-the-Loop vs. Fully Autonomous AI Agents: Guide</a></li>
<li><a href="https://www.strata.io/blog/agentic-identity/practicing-the-human-in-the-loop/">A 2026 Guide to Human-in-the-Loop | Strata</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#software development`, `#human-AI collaboration`, `#agentic development`

---

<a id="item-4"></a>
## [SimpleX Chat: Messaging Without Any User Identifiers](https://github.com/simplex-chat/simplex-chat) ⭐️ 8.0/10

SimpleX Chat has released a messaging network that operates without any user identifiers, achieving 100% privacy by design, with apps available for iOS, Android, and desktop. This approach eliminates the possibility of tracking or profiling users based on identifiers, setting a new standard for private communication and potentially influencing the broader messaging ecosystem. Instead of user IDs, SimpleX uses pairwise per-queue identifiers, creating up to n*(n-1) message queues for n users, making network graph observation difficult. It also employs quantum-resistant end-to-end encryption with a double-ratchet protocol.

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**Background**: Traditional messaging apps like WhatsApp or Signal rely on user identifiers (phone numbers, usernames) to route messages, which can be used to track users and build social graphs. SimpleX removes these identifiers entirely, using only temporary queue addresses for each connection. This design is inspired by privacy-by-design principles, aiming to embed privacy into the system architecture from the ground up.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SimpleX_Chat">SimpleX Chat - Wikipedia</a></li>
<li><a href="https://github.com/simplex-chat/simplex-chat">GitHub - simplex-chat/simplex-chat: SimpleX - the first messaging network operating without user identifiers of any kind - 100% private by design! iOS, Android and desktop apps 📱!</a></li>
<li><a href="https://simplex.chat/messaging/">SimpleX Chat: The World's Most Secure Messaging</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#messaging`, `#decentralized`, `#open-source`

---

<a id="item-5"></a>
## [Openpilot: Open-Source ADAS for 300+ Cars](https://github.com/commaai/openpilot) ⭐️ 8.0/10

Openpilot, an open-source operating system for robotics, now upgrades the driver assistance system on over 300 supported car models, with the latest comma four hardware available for $999. This project democratizes advanced driver assistance features, enabling hobbyists and researchers to experiment with autonomous driving technology on production vehicles, potentially accelerating innovation in the field. The comma four hardware is one-fifth the size of its predecessor, the comma 3X, and supports both release and staging software branches for early access to new features.

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**Background**: Openpilot is an open-source driver assistance system developed by comma.ai, founded by George Hotz in 2015. It provides adaptive cruise control and automated lane centering on compatible vehicles using aftermarket hardware like the comma four.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Openpilot">openpilot - Wikipedia</a></li>
<li><a href="https://comma.ai/openpilot">comma.ai — make driving chill</a></li>
<li><a href="https://github.com/commaai/openpilot">GitHub - commaai/openpilot: openpilot is an operating system for robotics. Currently, it upgrades the driver assistance system on 300+ supported cars. · GitHub</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#open source`, `#robotics`, `#driver assistance`

---

<a id="item-6"></a>
## [Free-for-Dev: Curated List of Free Cloud Tiers](https://github.com/ripienaar/free-for-dev) ⭐️ 8.0/10

The ripienaar/free-for-dev GitHub repository continues to be actively maintained by over 1600 contributors, providing a curated list of SaaS, PaaS, and IaaS offerings with free tiers for DevOps and infrastructure developers. This list saves developers significant time and effort in discovering free cloud services, enabling them to build and test projects without upfront costs. It is a trusted resource in the DevOps community due to its community-driven curation and regular updates. The list only includes as-a-Service offerings with a genuine free tier (not just a trial), and the free tier must last at least a year if time-limited. It excludes self-hosted software and services that restrict TLS to paid tiers.

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**Background**: Many cloud services offer free tiers to attract developers, but finding and comparing them is time-consuming. This GitHub repository aggregates such offerings across categories like CI/CD, analytics, and data storage, maintained by community contributions.

**Tags**: `#devops`, `#free-tier`, `#SaaS`, `#PaaS`, `#IaaS`

---

<a id="item-7"></a>
## [dbt Core v2.0 Alpha: Rust Rewrite for Speed](https://github.com/dbt-labs/dbt-core) ⭐️ 8.0/10

dbt Labs has released dbt Core v2.0 in alpha, a ground-up rewrite in Rust that serves as the foundation for the Fusion engine, offering dramatically faster parsing and compilation. This rewrite addresses performance bottlenecks in large dbt projects, enabling faster data transformations and easier installation via a single binary, which could accelerate adoption in data engineering teams. dbt Core v2.0 produces Parquet artifacts for scalable analysis, supports macOS and Linux on both x86-64 and ARM, and Windows on x86-64 only, while maintaining backward compatibility with JSON artifacts.

rss · GitHub Trending - Daily (All) · Jun 28, 22:57

**Background**: dbt (data build tool) is an open-source command-line tool that enables data analysts and engineers to transform data in their warehouse using SQL, following software engineering best practices like version control and testing. The original dbt Core v1 is written in Python, while v2.0 is a Rust rewrite aimed at improving performance and scalability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_build_tool">Data build tool - Wikipedia</a></li>
<li><a href="https://www.getorchestra.io/guides/dbt-core-key-questions-answered">Dbt core : key questions answered | Orchestra</a></li>
<li><a href="https://jakubillner.github.io/2025/01/24/dbt-with-adb.html">Configuring dbt Core with Oracle Autonomous Database</a></li>

</ul>
</details>

**Tags**: `#data engineering`, `#data transformation`, `#SQL`, `#open source`, `#analytics`

---