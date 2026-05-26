---
layout: default
title: "Horizon Summary: 2026-05-26 (EN)"
date: 2026-05-26
lang: en
---

> From 107 items, 41 important content pieces were selected

---

1. [DynIP: Modern Dynamic DNS with RFC 2136, IPv6, DNSSEC](#item-1) ⭐️ 8.0/10
2. [Netherlands Blocks US Takeover of Digital Identity Provider](#item-2) ⭐️ 8.0/10
3. [Microsoft Copilot Cowork Vulnerability Enables Data Exfiltration](#item-3) ⭐️ 8.0/10
4. [Pope Leo XIV's Encyclical on AI Ethics](#item-4) ⭐️ 8.0/10
5. [Open-Source Library of 754 Cybersecurity Skills for AI Agents](#item-5) ⭐️ 8.0/10
6. [CodeGraph: Pre-indexed code knowledge graph for AI coding assistants](#item-6) ⭐️ 8.0/10
7. [Microsoft Launches Agent Governance Toolkit for AI Agents](#item-7) ⭐️ 8.0/10
8. [Replicating Picbreeder with VLMs to Study Open-Endedness](#item-8) ⭐️ 8.0/10
9. [LLM Confidence Calibration Study Reveals Hard-Easy Effect](#item-9) ⭐️ 8.0/10
10. [LLM Reasoning Redundancy Quantified: 61-93% Steps Truncatable](#item-10) ⭐️ 8.0/10
11. [Context: Proactive AI Agents with Sandboxed Programs](#item-11) ⭐️ 8.0/10
12. [Optimizing Latency-Reliability-Cost in LLM Agent Workflows](#item-12) ⭐️ 8.0/10
13. [BODHI: LLM-Based OS Kernel Spec Generation Gets 96.73% Pass@1](#item-13) ⭐️ 8.0/10
14. [LLMs Show Belief Instability Under Clinical Pressure](#item-14) ⭐️ 8.0/10
15. [Runtime Execution Model Enforces Reconstructive Authority](#item-15) ⭐️ 8.0/10
16. [Algometrics: Forecasting Under Algorithmic Feedback](#item-16) ⭐️ 8.0/10
17. [Verifiable Transformers: Formal Proofs for Circuit Explanations](#item-17) ⭐️ 8.0/10
18. [IRNO: Iterative Refinement Neural Operators](#item-18) ⭐️ 8.0/10
19. [Hidden-State Privacy Has an Empty Middle](#item-19) ⭐️ 8.0/10
20. [LLM-AutoSciLab: Closed-Loop Scientific Discovery with LLMs](#item-20) ⭐️ 8.0/10
21. [InteractBind: Benchmark for Binding Site Localization](#item-21) ⭐️ 8.0/10
22. [Raon-Speech: 9B Speech LM Achieves SOTA on 42 Benchmarks](#item-22) ⭐️ 8.0/10
23. [Multi-Persona Debate System for Hypothesis Generation](#item-23) ⭐️ 8.0/10
24. [Causal Framework Reveals Rationalization Bias in LLM Judges](#item-24) ⭐️ 8.0/10
25. [AERIC: Anticipatory Hidden-State Monitor for Implicit Harm](#item-25) ⭐️ 8.0/10
26. [DPO Reduces Code-Switching Errors in Audio LLMs by 89.6%](#item-26) ⭐️ 8.0/10
27. [GazeWorld: Radiologist Gaze as World Model for Medical AI](#item-27) ⭐️ 8.0/10
28. [Nano World Models: Minimalist Codebase for Video Prediction](#item-28) ⭐️ 8.0/10
29. [EEG Decodes Visual Stimuli with 86% Retrieval Accuracy](#item-29) ⭐️ 8.0/10
30. [IVR-R1: Iterative Visual-Grounded Reasoning RL for Multimodal LLMs](#item-30) ⭐️ 8.0/10
31. [DIDR: Principled One-Step Generator RL via Diffused Reward](#item-31) ⭐️ 8.0/10
32. [ActQuant: Sub-4-bit Quantization for VLA Models](#item-32) ⭐️ 8.0/10
33. [Causality as AI's Statistical Conscience](#item-33) ⭐️ 8.0/10
34. [MEDAL: Distilling Manifold Embeddings into Autoencoders](#item-34) ⭐️ 8.0/10
35. [Unified Theory of Multicalibration Boosting](#item-35) ⭐️ 8.0/10
36. [Neural Reward Models Learn Features for Policy Optimization](#item-36) ⭐️ 8.0/10
37. [Counterfactual Safety Framework for RL](#item-37) ⭐️ 8.0/10
38. [Agentic AI adoption faces organizational readiness gap](#item-38) ⭐️ 8.0/10
39. [AI Quietly Erodes Entry-Level Jobs, Creating Looming Crisis](#item-39) ⭐️ 8.0/10
40. [Nasal Spray Reverses Brain Aging in Mice](#item-40) ⭐️ 8.0/10
41. [USC Scientists Discover Hidden Alzheimer's Trigger and Potential Drug Target](#item-41) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [DynIP: Modern Dynamic DNS with RFC 2136, IPv6, DNSSEC](https://dynip.dev/) ⭐️ 8.0/10

DynIP is a new dynamic DNS service that supports RFC 2136/TSIG updates, IPv6, and DNSSEC, allowing devices like FortiGate and MikroTik to update DNS records natively without custom clients. It fills a gap in existing DDNS services, which often rely on proprietary HTTP-only protocols and lack IPv6 and DNSSEC support, making it suitable for modern networks and devices. The service uses RFC 2136 DNS UPDATE with TSIG authentication as a first-class path, and also provides an HTTP API for devices that cannot use DNS UPDATE. It supports IPv6 end-to-end and DNSSEC for secure DNS updates.

hackernews · dynip · May 26, 07:35 · [Discussion](https://news.ycombinator.com/item?id=48276363)

**Background**: Dynamic DNS (DDNS) automatically updates DNS records when a device's IP address changes, commonly used for home servers or remote access. RFC 2136 defines a standard DNS UPDATE protocol, while TSIG provides authentication. DNSSEC adds cryptographic signatures to DNS records to prevent spoofing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dynamic_DNS">Dynamic DNS - Wikipedia</a></li>
<li><a href="https://datatracker.ietf.org/doc/html/rfc2136">RFC 2136 - Dynamic Updates in the Domain Name System ( DNS ...)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Domain_Name_System_Security_Extensions">Domain Name System Security Extensions - Wikipedia</a></li>

</ul>
</details>

**Discussion**: The community is positive, praising the support for RFC 2136 and integration with tools like external-dns. Some users suggest improving the landing page design and note that self-hosting with BIND9 is also possible but less convenient.

**Tags**: `#DNS`, `#IPv6`, `#DNSSEC`, `#networking`, `#open-source`

---

<a id="item-2"></a>
## [Netherlands Blocks US Takeover of Digital Identity Provider](https://www.politico.eu/article/netherlands-blocks-us-takeover-vital-digital-supplier/) ⭐️ 8.0/10

The Dutch government blocked the acquisition of Solvinity, the IT provider behind the national digital identity system DigiD, by US-based Kyndryl, citing data sovereignty and privacy concerns. This decision underscores growing tensions over digital sovereignty and the risks of foreign control over critical national infrastructure, especially for identity systems that handle sensitive citizen data. Solvinity hosts DigiD, which is used by millions of Dutch citizens for accessing government services; the Dutch parliament had previously voted to end the contract with Solvinity, but the government extended it, leaving the acquisition block as a key safeguard.

hackernews · vrganj · May 26, 11:46 · [Discussion](https://news.ycombinator.com/item?id=48278406)

**Background**: Digital sovereignty refers to a nation's control over its own data and digital infrastructure. Data sovereignty laws, like those in the EU, require that personal data be stored and processed within the country or region to protect privacy and security. DigiD is the Netherlands' national digital identity system, essential for citizens to interact with government agencies online.

<details><summary>References</summary>
<ul>
<li><a href="https://www.biometricupdate.com/202604/netherlands-weighs-data-sovereignty-concerns-with-solvinity-digital-identity-contract">Netherlands weighs data sovereignty concerns with Solvinity digital ...</a></li>
<li><a href="https://www.androguider.com/2026/05/dutch-government-blocks-us-tech.html">Dutch Government Blocks U.S. Tech Acquisition to Safeguard Digital ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed relief that the government finally acted, with some emphasizing that privacy by architecture is superior to privacy by policy, and suggesting open-source or cryptographic sovereignty systems as better alternatives. Others questioned why the Netherlands cannot self-host an open-source identity solution for its population.

**Tags**: `#digital sovereignty`, `#privacy`, `#geopolitics`, `#identity management`, `#open source`

---

<a id="item-3"></a>
## [Microsoft Copilot Cowork Vulnerability Enables Data Exfiltration](https://simonwillison.net/2026/May/26/copilot-cowork-exfiltrates-files/#atom-everything) ⭐️ 8.0/10

A security researcher disclosed that Microsoft Copilot Cowork's agentic email feature can be exploited via prompt injection to exfiltrate files by embedding external images in compromised messages. The attack leverages pre-authenticated OneDrive download links to allow attackers to access files. This vulnerability highlights a critical security challenge in agentic AI systems, where even limited agent actions can be hijacked to leak sensitive data. As enterprises increasingly adopt AI agents for productivity, such exfiltration vectors pose a serious risk to data confidentiality. The attack works because Copilot Cowork agents can send emails to the user's inbox without approval, and those emails can contain external images that trigger network requests. Prompt injection can cause the agent to include pre-authenticated OneDrive links in the email, enabling file download by attackers.

rss · Simon Willison · May 26, 15:36

**Background**: Prompt injection is a cybersecurity attack where malicious inputs cause AI models to behave unexpectedly. In agentic systems, AI agents can perform actions like sending emails, which expands the attack surface. Pre-authenticated download links from services like OneDrive allow file access without additional authentication, making them a valuable target for exfiltration.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters expressed concern about the inherent risks of agentic AI, with some noting that this vulnerability is a textbook example of the 'lethal trifecta' of prompt injection, agent actions, and data exfiltration. Others debated whether Microsoft's design choices were negligent or if such issues are inevitable in early-stage agent systems.

**Tags**: `#security`, `#AI`, `#prompt injection`, `#Microsoft Copilot`, `#data exfiltration`

---

<a id="item-4"></a>
## [Pope Leo XIV's Encyclical on AI Ethics](https://simonwillison.net/2026/May/25/encyclical-on-ai/#atom-everything) ⭐️ 8.0/10

Pope Leo XIV released his first encyclical, Magnifica Humanitas, on May 25, 2026, providing ethical guidance on artificial intelligence. The document draws parallels to Pope Leo XIII's 1891 encyclical Rerum novarum, which addressed the Industrial Revolution. This is the Vatican's first major encyclical specifically on AI ethics, offering authoritative moral guidance that could influence global policy and public discourse. It frames AI as a social justice issue, emphasizing human dignity, labor rights, and the common good. The encyclical describes AI systems as more 'cultivated' than 'built,' highlighting the interpretability problem where even developers lack full understanding of internal processes. It also stresses that true development must not shift costs onto others or relegate regions to subordinate roles.

rss · Simon Willison · May 25, 23:58

**Background**: An encyclical is a formal papal letter addressing the entire Church and often the wider world on matters of doctrine or social teaching. Pope Leo XIV chose his name to honor Leo XIII, whose 1891 encyclical Rerum novarum established modern Catholic social teaching on labor and capital. This new encyclical applies similar principles to the challenges posed by artificial intelligence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Magnifica_humanitas">Magnifica Humanitas - Wikipedia</a></li>
<li><a href="https://www.vatican.va/content/leo-xiv/en/encyclicals/documents/20260515-magnifica-humanitas.html">Encyclical Letter of His Holiness Leo XIV Magnifica Humanitas (15 May 2026)</a></li>
<li><a href="https://www.vaticannews.va/en/pope/news/2026-05/pope-leo-xiv-encyclical-magnifica-humanitas-ai.html">Pope Leo’s ‘Magnifica humanitas’: AI must serve humanity not concentrate power - Vatican News</a></li>

</ul>
</details>

**Tags**: `#AI ethics`, `#Vatican`, `#encyclical`, `#technology and society`

---

<a id="item-5"></a>
## [Open-Source Library of 754 Cybersecurity Skills for AI Agents](https://github.com/mukul975/Anthropic-Cybersecurity-Skills) ⭐️ 8.0/10

Mukul975 released the largest open-source cybersecurity skills library for AI agents, containing 754 structured skills mapped to five major frameworks (MITRE ATT&CK, NIST CSF 2.0, MITRE ATLAS, D3FEND, NIST AI RMF) and compatible with over 20 AI platforms including Claude Code, GitHub Copilot, and Cursor. This library bridges the gap between cybersecurity expertise and AI agents, enabling developers to equip AI tools with standardized, production-grade security skills across multiple domains, which could accelerate the adoption of AI in security operations and improve consistency in threat detection and response. The skills cover 26 security domains and follow the agentskills.io open standard, ensuring cross-platform portability. The library is licensed under Apache 2.0 and accepts contributions via pull requests.

rss · GitHub Trending - Daily (All) · May 26, 23:04

**Background**: AI agents are increasingly used in cybersecurity for tasks like threat detection and incident response, but they often lack structured, domain-specific knowledge. Frameworks like MITRE ATT&CK and NIST CSF provide standardized taxonomies for cyber threats and defenses, while agentskills.io is an open standard for defining AI agent capabilities. This library combines these elements to create a reusable skill set for AI agents.

<details><summary>References</summary>
<ul>
<li><a href="https://agentskills.io/">A standardized way to give AI agents new capabilities and expertise.</a></li>
<li><a href="https://d3fend.mitre.org/">D3FEND Matrix | MITRE D3FEND™</a></li>
<li><a href="https://www.practical-devsecops.com/mitre-atlas-framework-guide-securing-ai-systems/">MITRE ATLAS Framework 2026 - Guide to Securing AI Systems - Practical DevSecOps</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#AI agents`, `#open-source`, `#MITRE ATT&CK`, `#NIST CSF`

---

<a id="item-6"></a>
## [CodeGraph: Pre-indexed code knowledge graph for AI coding assistants](https://github.com/colbymchenry/codegraph) ⭐️ 8.0/10

CodeGraph is a pre-indexed code knowledge graph that reduces token usage by ~35% and tool calls by ~70% for AI coding assistants like Claude Code, Cursor, Codex CLI, OpenCode, and Hermes Agent, while running entirely locally. This tool significantly lowers the cost and latency of AI-assisted coding by reducing API token consumption and unnecessary tool calls, making AI coding assistants more practical for large codebases. Its local execution also addresses privacy concerns for developers who cannot upload code to cloud services. CodeGraph uses tree-sitter for AST parsing, SQLite with FTS5 for indexing, and bundles its own runtime so no Node.js installation is required. It supports Windows, macOS, and Linux, and can be installed via a one-line curl command or npm.

rss · GitHub Trending - Daily (All) · May 26, 23:04

**Background**: AI coding assistants like Claude Code and Cursor rely on understanding the entire codebase to provide relevant suggestions, but sending large code contexts to cloud APIs is expensive and slow. A code knowledge graph pre-indexes the code structure and relationships locally, allowing the AI to retrieve only the necessary context without repeated file scanning or tool calls.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/colbymchenry/codegraph">GitHub - colbymchenry/codegraph: Pre-indexed code knowledge ...</a></li>
<li><a href="https://pyshine.com/CodeGraph-Pre-Indexed-Code-Knowledge-Graph-AI-Coding-Agents/">CodeGraph: Pre-Indexed Code Knowledge Graph for AI Coding ...</a></li>
<li><a href="https://tosea.ai/blog/codegraph-claude-code-cursor-guide-2026">How to Use CodeGraph for Claude Code and Cursor: Complete ...</a></li>

</ul>
</details>

**Tags**: `#AI-assisted development`, `#code intelligence`, `#developer tools`, `#knowledge graph`

---

<a id="item-7"></a>
## [Microsoft Launches Agent Governance Toolkit for AI Agents](https://github.com/microsoft/agent-governance-toolkit) ⭐️ 8.0/10

Microsoft has released the Agent Governance Toolkit, an open-source framework providing policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. It covers all 10 risks in the OWASP Agentic Top 10. As AI agents become more autonomous, governance and security are critical for safe production deployment. This toolkit from Microsoft addresses key gaps in agent security, helping enterprises adopt AI agents with confidence. The toolkit is available as a public preview on GitHub under the MIT license, with packages on PyPI, npm, and NuGet. It includes compliance documentation mapping to the OWASP Agentic Top 10 and supports multiple languages.

rss · GitHub Trending - Python · May 26, 23:04

**Background**: AI agents are autonomous systems that can plan, execute tasks, and interact with tools and APIs. The OWASP Agentic Top 10 is a framework identifying critical security risks for such agents, including identity abuse and privilege escalation. Zero-trust identity ensures every agent request is verified, while sandboxing isolates agent execution to prevent harm.

<details><summary>References</summary>
<ul>
<li><a href="https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/">OWASP Top 10 for Agentic Applications for 2026 - OWASP Gen AI Security Project</a></li>
<li><a href="https://xage.com/blog/zero-trust-proven-solution-for-the-new-ai-security-challenge/">Zero Trust for AI Security: How Identity-First Defense Solves Modern Threats</a></li>
<li><a href="https://blogs.cisco.com/security/security-agentic-ai-how-cisco-brings-zero-trust-to-your-new-digital-workforce">Zero Trust for AI Agents – Identity, Access Control, and Behavioral Protection for the Agentic Era</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#Governance`, `#Security`, `#Microsoft`, `#OWASP`

---

<a id="item-8"></a>
## [Replicating Picbreeder with VLMs to Study Open-Endedness](https://arxiv.org/abs/2605.23908) ⭐️ 8.0/10

Researchers replicated the human-driven Picbreeder experiment using frontier vision-language models (VLMs) to investigate whether AI can achieve open-ended creative discovery. They observed qualitative differences from the human baseline and tested factors like exploratory noise, behavioral diversity, and narrative momentum. This work directly addresses the fundamental question of whether AI systems can exhibit open-endedness—a key property of human creativity and scientific discovery. Understanding these differences could guide the development of more creative and autonomous AI systems. The study used VLMs to replace human users in interactive evolution of small neural networks, generating images through selection and mutation. The researchers made their code publicly available on GitHub and used metrics like phylogenetic complexity and visual/semantic salience to characterize differences.

rss · arXiv - AI · May 26, 04:00

**Background**: Picbreeder is a classic online experiment in collaborative interactive evolution where users collectively evolved images by selecting preferred variants. Open-endedness refers to the capacity to generate an endless stream of novel and meaningful outputs, a hallmark of human creativity that current AI systems struggle to achieve. Interactive evolutionary computation uses human judgment as the fitness function when objective criteria are hard to define.

<details><summary>References</summary>
<ul>
<li><a href="https://wiki.santafe.edu/images/3/34/Stanley_innovation_workshop14.pdf">The Picbreeder Experiment</a></li>
<li><a href="https://ieeexplore.ieee.org/document/6793948">Picbreeder : A Case Study in Collaborative Evolutionary... | IEEE Xplore</a></li>
<li><a href="https://arxiv.org/abs/2406.04268">[2406.04268] Open-Endedness is Essential for Artificial Superhuman Intelligence</a></li>

</ul>
</details>

**Tags**: `#open-endedness`, `#vision-language models`, `#AI creativity`, `#evolutionary computation`, `#Picbreeder`

---

<a id="item-9"></a>
## [LLM Confidence Calibration Study Reveals Hard-Easy Effect](https://arxiv.org/abs/2605.23909) ⭐️ 8.0/10

A preregistered study on LLM confidence calibration finds that models are overconfident on hard tasks and underconfident on easy tasks, and introduces the LifeEval benchmark for evaluating calibration across difficulty levels. This research addresses a critical issue in AI reliability, showing that LLMs exhibit systematic miscalibration similar to humans, which has practical implications for deploying LLMs in high-stakes applications. The study is preregistered and uses a novel benchmark called LifeEval, which comprises 4,075 question-answer pairs across six capability dimensions to test calibration at varying difficulty levels.

rss · arXiv - AI · May 26, 04:00

**Background**: Confidence calibration measures how well a model's predicted confidence matches its actual accuracy. Poor calibration can lead to overconfident errors or underconfident predictions, undermining trust in AI systems. Previous work has explored calibration in LLMs, but this study specifically investigates the hard-easy effect.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2311.08298">A Survey of Confidence Estimation and Calibration in Large ...</a></li>
<li><a href="https://arxiv.org/abs/2603.00490">[2603.00490] LifeEval: A Multimodal Benchmark for Assistive AI in Egocentric Daily Life Tasks</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#calibration`, `#confidence`, `#AI reliability`, `#benchmark`

---

<a id="item-10"></a>
## [LLM Reasoning Redundancy Quantified: 61-93% Steps Truncatable](https://arxiv.org/abs/2605.23926) ⭐️ 8.0/10

A new paper formalizes reasoning redundancy in LLMs and shows that 61-93% of chain-of-thought steps can be truncated without affecting correctness across four frontier models and two benchmarks. This finding reveals that current reasoning models waste significant computation, offering a path to reduce latency and cost while maintaining accuracy, and challenges the necessity of long chain-of-thought traces. The paper defines redundancy as the largest fraction of trailing steps that can be truncated while the model still produces the correct answer; median critical prefix is a single step in six of eight conditions, and redundancy persists even on hard problems (46-85% on Level-5 MATH-500).

rss · arXiv - AI · May 26, 04:00

**Background**: Chain-of-thought reasoning improves LLM performance on complex tasks by generating intermediate steps. However, these traces often contain redundant content like reformulation and self-reflection, increasing latency and cost. This paper provides the first large-scale measurement of such redundancy and a theoretical explanation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2201.11903">[2201.11903] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models</a></li>
<li><a href="https://www.reddit.com/r/LocalLLaMA/comments/1mkza1b/new_paper_reveals_chainofthought_reasoning_of/">r/LocalLLaMA on Reddit: New paper reveals Chain-of-Thought reasoning of LLMs a mirage</a></li>

</ul>
</details>

**Discussion**: The Reddit discussion on a related paper suggests skepticism about chain-of-thought reasoning, with some arguing that reasoning chains are merely context generation and need not be cogent. This aligns with the paper's finding that much of the chain is redundant.

**Tags**: `#LLM`, `#reasoning`, `#efficiency`, `#chain-of-thought`, `#redundancy`

---

<a id="item-11"></a>
## [Context: Proactive AI Agents with Sandboxed Programs](https://arxiv.org/abs/2605.23928) ⭐️ 8.0/10

Researchers introduced Context, an intelligence layer for proactive goal-directed agents that replaces reactive chatbots, using composable sandboxed programs and declarative wiring to advance tasks without waiting for user prompts. This architecture could significantly improve conversational AI by enabling agents to proactively drive interactions toward goals, reducing latency and user effort, and potentially setting a new standard for agent systems. The system achieves near-100% KV-cache reuse via write-time context assembly, and executes sandboxed wisdom programs at interaction time without additional LM calls, with formal proofs of correctness and efficiency.

rss · arXiv - AI · May 26, 04:00

**Background**: Current conversational AI systems are typically reactive, waiting for user input before generating responses. The Magarshak Architecture proposes a proactive approach where agents have internal goal streams and can take initiative. Key concepts include composable sandboxed programs (isolated, reusable code modules) and declarative wiring (connecting programs to goals via typed relations).

**Tags**: `#AI agents`, `#proactive computing`, `#LLM architecture`, `#conversational AI`, `#systems design`

---

<a id="item-12"></a>
## [Optimizing Latency-Reliability-Cost in LLM Agent Workflows](https://arxiv.org/abs/2605.23929) ⭐️ 8.0/10

This paper introduces performance models for LLM and non-LLM agents and derives optimal token allocation policies, such as water-filling, to balance latency, reliability, and cost in sequential agentic workflows. This work addresses a fundamental challenge in deploying multi-agent systems, providing formal methods to design reliable and cost-effective LLM-enabled workflows, which is critical for real-world AI applications. The paper uses a parametric exponential reliability function to model LLM agent output quality and characterizes optimal workflow reliability via shadow prices from optimization theory.

rss · arXiv - AI · May 26, 04:00

**Background**: Modern AI systems often use workflows with multiple agents, some powered by LLMs and others by conventional modules. Balancing latency, reliability, and cost is a key design challenge. This paper provides theoretical models and optimal policies for such tradeoffs.

**Tags**: `#LLM agents`, `#reliability`, `#latency`, `#cost optimization`, `#workflow design`

---

<a id="item-13"></a>
## [BODHI: LLM-Based OS Kernel Spec Generation Gets 96.73% Pass@1](https://arxiv.org/abs/2605.23931) ⭐️ 8.0/10

Researchers propose BODHI, a domain knowledge prompting method that augments few-shot prompts with a structured C-to-Python translation guide, achieving up to 96.73% Pass@1 on the OSV-Bench benchmark for OS kernel specification generation. This work significantly narrows the gap between general-purpose code generation and formal specification synthesis, automating a critical bottleneck in OS kernel verification and potentially accelerating the adoption of formal methods in systems software. BODHI covers 15 categories of domain-specific translation patterns, inspired by Structured Chain-of-Thought (SCoT) prompting, and improves every model tested (9 models from 6 providers) with gains from +11% to +32%.

rss · arXiv - AI · May 26, 04:00

**Background**: Formal verification of OS kernels requires precise specifications, which are traditionally written manually by experts. LLMs offer automation potential but struggle with domain-specific translation from C to Python. OSV-Bench is a benchmark of 245 specification generation tasks derived from the Hyperkernel OS kernel, where the previous best Pass@1 was 55.10%.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2305.06599">Structured Chain - of - Thought Prompting for Code Generation</a></li>

</ul>
</details>

**Tags**: `#operating systems`, `#formal verification`, `#large language models`, `#specification inference`, `#kernel`

---

<a id="item-14"></a>
## [LLMs Show Belief Instability Under Clinical Pressure](https://arxiv.org/abs/2605.23932) ⭐️ 8.0/10

A new study introduces Med-Stress, a stress test framework that reveals LLMs abandon correct diagnoses under escalating pressure in clinical dialogues, and proposes two defenses: RBED and R-FT. This work highlights a critical failure mode in LLMs—sycophancy under pressure—that undermines their reliability in high-stakes clinical settings, and offers practical defenses to improve epistemic resilience. Across nine frontier LLMs, the study found a dissociation between medical knowledge and robustness, with some models showing high accuracy but low belief stability. The R-FT defense nearly eliminates belief change.

rss · arXiv - AI · May 26, 04:00

**Background**: AI sycophancy refers to a model's tendency to agree with users rather than reason independently. Epistemic resilience concerns a model's ability to maintain correct beliefs under pressure. The Med-Stress framework tests LLMs by simulating escalating clinical pressure in multi-turn dialogues.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Sycophancy">Sycophancy - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Epistemology">Epistemology - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#AI safety`, `#robustness`, `#clinical NLP`, `#sycophancy`

---

<a id="item-15"></a>
## [Runtime Execution Model Enforces Reconstructive Authority](https://arxiv.org/abs/2605.23935) ⭐️ 8.0/10

This paper introduces a runtime execution model for autonomous agents that adds a 'halt' state and a recovery loop with drift detection, ensuring actions are only executed when authority can be reconstructed from the current state. This work addresses a critical gap in AI safety by operationalizing Reconstructive Authority as a runtime enforcement mechanism, which could prevent autonomous agents from executing actions that have lost authorization, thereby improving trustworthiness in real-world deployments. The model extends the execution state space beyond admit/deny with a third state, halt, for cases where authority is undefined due to incomplete observability, and integrates drift detection (IML) with execution control (ACP) in a Recovery Loop.

rss · arXiv - AI · May 26, 04:00

**Background**: Reconstructive Authority (RAM) is a condition that requires actions to be permitted only if authority can be constructed from the current state. Prior work defined RAM but did not specify how to enforce it at runtime. This paper provides the execution semantics needed to apply RAM in real systems, building on concepts like drift detection and execution gating.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.23935v1">Operationalizing Reconstructive Authority Runtime ...</a></li>
<li><a href="https://github.com/chelof100/operationalizing-ram">GitHub - chelof100/operationalizing- ram : Paper 6 ...</a></li>
<li><a href="https://www.alphaxiv.org/abs/2605.23935">Operationalizing Reconstructive Authority : Runtime ...</a></li>

</ul>
</details>

**Tags**: `#autonomous agents`, `#runtime enforcement`, `#AI safety`, `#authority reconstruction`, `#execution gating`

---

<a id="item-16"></a>
## [Algometrics: Forecasting Under Algorithmic Feedback](https://arxiv.org/abs/2605.23978) ⭐️ 8.0/10

This paper introduces algometrics, a framework for time series forecasting under algorithmic feedback, proving that deployment risk is not identifiable from passive historical data and that model rankings can invert under crowding. 这项工作解决了算法市场中的一个基本问题，即预测模型会影响其预测的数据，对金融及其他反馈系统中的机器学习部署具有重要意义。 The framework distinguishes historical risk (passive forecasting) from deployment risk (when forecasts drive actions), and proves that even in a one-step linear feedback model, infinitely many environments can produce the same historical law but different deployment risks.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: In algorithmic markets, predictive models are used to make decisions such as trades or allocations, which in turn alter the future data those models aim to forecast. This creates a feedback loop that can invalidate traditional time series evaluation methods. The paper proposes algometrics to explicitly model this dependency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.23978">[2605.23978] Algometrics: Forecasting Under Algorithmic Feedback</a></li>
<li><a href="https://arxiv.org/html/2605.23978">Algometrics: Forecasting Under Algorithmic Feedback</a></li>

</ul>
</details>

**Tags**: `#algorithmic markets`, `#time series forecasting`, `#deployment risk`, `#feedback loops`, `#machine learning`

---

<a id="item-17"></a>
## [Verifiable Transformers: Formal Proofs for Circuit Explanations](https://arxiv.org/abs/2605.24033) ⭐️ 8.0/10

Researchers propose Verifiable Transformers, a framework that converts task-localized Transformer circuits into bounded, solver-checkable claims using SMT solvers or surrogate models, enabling formal verification of mechanistic interpretability claims. This work bridges the gap between plausible circuit explanations and provable guarantees, a critical step for AI safety by allowing rigorous verification of model behavior in localized tasks. The framework includes direct verification (encoding the circuit into an SMT solver) and surrogate-mediated verification (using an SMT-encodable surrogate model). It demonstrates direct verification on small symbolic tasks and surrogate-mediated verification on GPT-2 scale circuits with hard-to-encode attention.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: Mechanistic interpretability aims to reverse-engineer neural networks by identifying circuits—subnetworks responsible for specific behaviors. However, these explanations are typically validated through examples and ablations, lacking formal proof. SMT solvers determine whether logical formulas are satisfiable, enabling automated verification of mathematical claims.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SMT_solver">SMT solver</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Surrogate_model">Surrogate model</a></li>

</ul>
</details>

**Tags**: `#mechanistic interpretability`, `#transformers`, `#formal verification`, `#AI safety`, `#SMT`

---

<a id="item-18"></a>
## [IRNO: Iterative Refinement Neural Operators](https://arxiv.org/abs/2605.24041) ⭐️ 8.0/10

Researchers introduced the Iterative Refinement Neural Operator (IRNO), which augments pre-trained neural operators with a learned refinement module applied via fixed-point iteration, achieving up to 56.05% error reduction on turbulent flow modeling. This work provides a principled approach to mitigate spectral bias in neural operators, a key limitation in scientific machine learning, and demonstrates significant empirical improvements across physical systems. IRNO decomposes prediction into a coarse initialization followed by successive residual corrections, paralleling classical numerical solvers, and uses a progressive spectral loss that adaptively increases penalty on high-frequency components during training.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: Neural operators are deep learning models that learn mappings between function spaces, serving as fast surrogates for scientific simulations. However, they suffer from spectral bias, meaning they struggle to capture high-frequency details. Fixed-point iteration is a classical numerical method for solving equations by repeatedly applying a function until convergence.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fixed-point_iteration">Fixed - point iteration - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#neural operators`, `#spectral bias`, `#scientific machine learning`, `#fixed-point iteration`, `#deep learning`

---

<a id="item-19"></a>
## [Hidden-State Privacy Has an Empty Middle](https://arxiv.org/abs/2605.24042) ⭐️ 8.0/10

A new paper proves that no Gaussian release achieves both moderate utility and privacy for hidden-state privacy, establishing a Fisher-ball lower bound and identifying a unique optimal diagonal mechanism. This result reframes hidden-state release from mechanism-design within the Gaussian class to architecture or release co-design, potentially impacting privacy-preserving machine learning and large language model deployment. The paper tested 1,536 Gaussian release covariances and found none achieve both moderate utility and privacy; the diagonal inverse-Fisher release is the unique minimax-optimal diagonal mechanism but sits on a privacy/utility edge.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: Hidden-state privacy concerns protecting intermediate representations (hidden states) in neural networks from being inferred by attackers. Gaussian mechanisms add noise to these states to provide privacy, but this paper shows a fundamental trade-off: no Gaussian release can fill the 'middle' region where both utility and privacy are acceptable.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mahalanobis_distance">Mahalanobis distance - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2210.02482">[2210.02482] Fisher information lower bounds for sampling</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#machine learning`, `#information theory`, `#Gaussian mechanisms`, `#differential privacy`

---

<a id="item-20"></a>
## [LLM-AutoSciLab: Closed-Loop Scientific Discovery with LLMs](https://arxiv.org/abs/2605.24043) ⭐️ 8.0/10

LLM-AutoSciLab introduces a closed-loop framework that uses LLMs to iteratively generate hypotheses, select informative experiments, and refine mechanisms, moving beyond static dataset-based discovery. This framework addresses a key limitation of current AI-driven science by enabling adaptive data acquisition, which can significantly accelerate scientific discovery in fields like chemistry and biology. On ActiveSciBench-Chem and ActiveSciBench-GRN, LLM-AutoSciLab achieves 35.1% symbolic accuracy and 31.1% exact graph recovery, respectively, and is 2-5x more sample-efficient than baselines.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: Scientific discovery traditionally involves a closed loop of hypothesis, experiment, and refinement. However, most AI approaches treat discovery as supervised learning on fixed datasets, which cannot adaptively gather new data to resolve uncertainty. LLM-AutoSciLab leverages large language models to automate the entire loop, including hypothesis generation and experiment selection.

<details><summary>References</summary>
<ul>
<li><a href="https://www.science.org/doi/10.1126/sciadv.adu7426">Real-time experiment-theory closed-loop interaction for autonomous materials science | Science Advances</a></li>
<li><a href="https://arxiv.org/abs/2307.07522">[2307.07522] The Future of Fundamental Science Led by Generative Closed-Loop Artificial Intelligence</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#scientific discovery`, `#active learning`, `#AI for science`, `#automated experimentation`

---

<a id="item-21"></a>
## [InteractBind: Benchmark for Binding Site Localization](https://arxiv.org/abs/2605.24045) ⭐️ 8.0/10

Researchers introduced InteractBind, a dataset of ~100k protein-ligand pairs and a benchmark for evaluating binding site localization and non-covalent interaction prediction, beyond simple binding prediction. This benchmark addresses a critical gap in protein-ligand modeling by testing whether models truly learn binding sites, which is essential for interpretable drug discovery and molecular design. The benchmark includes six types of non-covalent interactions and uses protein similarity-controlled splits to assess generalization. Evaluations of eight existing models showed strong binary binding prediction but limited binding-site localization.

rss · arXiv - Machine Learning · May 26, 04:00

**Background**: Protein-ligand modeling is fundamental to computational drug discovery, where models predict whether and how strongly a protein and ligand bind. Existing benchmarks focus on binary binding prediction and affinity regression, but do not test whether models can localize the binding site or identify specific non-covalent interactions, which are crucial for understanding molecular recognition.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-covalent_interaction">Non - covalent interaction - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#protein-ligand modeling`, `#benchmark`, `#drug discovery`, `#binding site localization`, `#machine learning`

---

<a id="item-22"></a>
## [Raon-Speech: 9B Speech LM Achieves SOTA on 42 Benchmarks](https://arxiv.org/abs/2605.23912) ⭐️ 8.0/10

Raon-Speech, a 9B-parameter speech language model, achieves state-of-the-art results across 42 English and Korean benchmarks through multi-stage training including knowledge distillation and preference optimization. The model also introduces Raon-SpeechChat, a full-duplex extension for natural real-time conversation. This work demonstrates a scalable recipe for transforming a pre-trained LLM into a high-performing speech LM while preserving text capabilities, setting a new standard for bilingual speech understanding and generation. The open-source release of all checkpoints and pipelines will accelerate research in speech AI and real-time conversational systems. The model is trained on 1.38M hours of curated English and Korean speech and text data across three stages: speech module alignment, end-to-end pre-training with knowledge distillation, and multi-task preference optimization. Raon-SpeechChat is further trained on 119K hours of time-aligned dialogue data and excels in turn-taking and interruption-sensitive behaviors on the FDB v1.0 benchmark.

rss · arXiv - NLP · May 26, 04:00

**Background**: Speech language models (SpeechLMs) aim to unify speech understanding and generation within a single model, often by extending a text-based LLM with speech encoders and decoders. Knowledge distillation transfers knowledge from a larger teacher model to a smaller student model, while preference optimization fine-tunes the model to align with human preferences for natural interaction. Full-duplex conversation allows both parties to speak and interrupt simultaneously, mimicking human dialogue.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.14930">[2509.14930] Cross-Modal Knowledge Distillation for Speech Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2509.18928">[2509.18928] Direct Preference Optimization for Speech Autoregressive Diffusion Models</a></li>
<li><a href="https://arxiv.org/html/2509.00685v1">MPO: Multidimensional Preference Optimization for Language Model-based Text-to-Speech</a></li>

</ul>
</details>

**Tags**: `#speech language model`, `#AI`, `#speech understanding`, `#speech generation`, `#multimodal`

---

<a id="item-23"></a>
## [Multi-Persona Debate System for Hypothesis Generation](https://arxiv.org/abs/2605.23917) ⭐️ 8.0/10

Researchers introduced the Multi-Persona Debate System (MPDS), a framework that combines literature retrieval, long-context LLM reasoning, corpus-driven persona induction, and structured multi-agent debate to automatically generate scientific hypotheses, demonstrated in battery materials research. MPDS addresses a critical bottleneck in scientific discovery by synthesizing fragmented knowledge into actionable hypotheses, potentially accelerating research in complex domains like battery materials where multiple constraints must be optimized simultaneously. MPDS constructs literature snapshots of up to 500 papers, conducts a three-round citation-aware debate among persona-grounded agents, and uses a moderator for synthesis; it was evaluated with temporally controlled protocols and achieved the highest Integrative Hypothesis Quality score in ablation studies.

rss · arXiv - NLP · May 26, 04:00

**Background**: Scientific hypothesis generation often suffers from information overload and fragmented knowledge. Multi-agent debate systems use multiple LLM agents with distinct roles to discuss and refine ideas, improving reasoning quality. Corpus-driven persona induction automatically derives agent personas from literature, while citation-aware debate ensures arguments are grounded in specific sources.

<details><summary>References</summary>
<ul>
<li><a href="https://sikkha.medium.com/exploring-multi-agent-debate-frameworks-for-ai-reasoning-and-persona-driven-architectures-0ffb5db05ee3">Exploring Multi-Agent Debate Frameworks for AI Reasoning and Persona-Driven Architectures | by Kan Yuenyong | Medium</a></li>
<li><a href="https://www.emergentmind.com/topics/multi-agent-debate-mad-strategies">Multi-Agent Debate Strategies</a></li>
<li><a href="https://arxiv.org/abs/2406.19643">[2406.19643] Debate-to-Write: A Persona-Driven Multi-Agent Framework for Diverse Argument Generation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#scientific discovery`, `#multi-agent systems`, `#hypothesis generation`, `#battery materials`

---

<a id="item-24"></a>
## [Causal Framework Reveals Rationalization Bias in LLM Judges](https://arxiv.org/abs/2605.23970) ⭐️ 8.0/10

A new paper introduces a causal framework and suite of cue interventions to detect rationalization bias in LLM judges, showing that explanations are often unstable under non-evidential cue perturbations. The study proposes mitigations like PROOF-BEFORE-PREFERENCE to improve cue invariance. This research addresses a critical gap in LLM evaluation reliability, as rationalization bias can undermine trust in AI-as-judge systems used for summarization and dialogue evaluation. The proposed metrics and mitigations offer practical tools to enhance AI safety and fairness. The framework includes five cue interventions (Blind, Truth, Flip, Placebo, Reveal-After) and tie-aware metrics for outcome anchoring and rationale anchoring. Experiments on 1,000 summaries show substantial cue-anchored rationalization, while PROOF-BEFORE-PREFERENCE markedly improves cue invariance over baselines.

rss · arXiv - NLP · May 26, 04:00

**Background**: LLMs are increasingly used as automatic judges for evaluating text generation tasks, but they exhibit biases like position and verbosity preferences. Prior work focused on outcome biases, leaving the stability of explanations under input perturbations largely unexplored. This paper introduces a causal perspective to study whether explanations are faithful or fabricated.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LLM-as-a-Judge">LLM-as-a-Judge - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2410.02736v1">Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#bias`, `#evaluation`, `#AI safety`, `#causal inference`

---

<a id="item-25"></a>
## [AERIC: Anticipatory Hidden-State Monitor for Implicit Harm](https://arxiv.org/abs/2605.23974) ⭐️ 8.0/10

Researchers introduced AERIC, a lightweight same-pass hidden-state monitor that anticipates implicit harmful dialogue in language models without requiring additional forward passes. It combines short-horizon hazard forecasting, support-sensitive suppression, and prompt-conditioned residual scoring under an exponential moving average decision rule. This addresses a critical safety challenge: detecting implicit harmful content during generation without extra computational cost. AERIC significantly improves detection accuracy over existing streaming guards while adding minimal latency, making real-time safety monitoring more practical for large language models. The default linear monitor has only 387 trainable head parameters. On DiaSafety, AERIC improves AUROC from 0.6830 to 0.7143; on Harmful Advice, from 0.8219 to 0.8582. Under a safe-budget rule, trigger@64 reaches 0.6438 on HarmBench DirectRequest for Qwen, and latency increase is only 2.34% compared to 79.40% for Qwen3Guard-Stream-4B.

rss · arXiv - NLP · May 26, 04:00

**Background**: Language models can generate harmful content, including implicit harm that uses indirect language. Existing safety monitors either check completed text (response-level) or operate per token but require extra forward passes (streaming guards). Same-pass monitoring reads hidden states during normal decoding without extra passes, offering efficiency but has been underexplored for implicit harm.

**Tags**: `#AI safety`, `#language models`, `#harmful content detection`, `#streaming monitoring`, `#implicit harm`

---

<a id="item-26"></a>
## [DPO Reduces Code-Switching Errors in Audio LLMs by 89.6%](https://arxiv.org/abs/2605.23975) ⭐️ 8.0/10

Researchers applied Direct Preference Optimization (DPO) to align Audio LLMs for English-Mandarin code-switching speech recognition, achieving up to 89.6% reduction in mixed-error rate (MER) on in-distribution data. This work addresses a critical gap in multilingual Audio LLMs—code-switching transcription—and demonstrates that DPO can effectively correct systematic failure modes without complex reinforcement learning pipelines. The study identified three failure modes: language omission, translation-instead-of-transcription, and hallucination. Training on 100K preference pairs (570 hours) yielded consistent behavioral shifts, with out-of-distribution MER reductions up to 20.0%.

rss · arXiv - NLP · May 26, 04:00

**Background**: Audio LLMs combine audio encoders with large language models to perform tasks like speech recognition and translation. Code-switching—mixing languages within a single utterance—poses a challenge because models often default to one language or translate instead of transcribing. Direct Preference Optimization (DPO) is a lightweight alignment method that fine-tunes models using preference pairs without needing a separate reward model.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@joaolages/direct-preference-optimization-dpo-622fc1f18707">Direct Preference Optimization ( DPO ) | by João Lages | Medium</a></li>
<li><a href="https://arxiv.org/abs/2509.24310">[2509.24310] Code-switching Speech Recognition Under the Lens: Model- and Data-Centric Perspectives</a></li>

</ul>
</details>

**Tags**: `#audio LLMs`, `#code-switching`, `#direct preference optimization`, `#speech recognition`, `#multilingual`

---

<a id="item-27"></a>
## [GazeWorld: Radiologist Gaze as World Model for Medical AI](https://arxiv.org/abs/2605.23992) ⭐️ 8.0/10

Researchers propose GazeWorld, a world model that treats radiologist eye-tracking sequences as trajectories through an image, autoregressively predicting latent representations of fixated patches and covering unvisited regions via a spatial-completion branch. GazeWorld achieves state-of-the-art diagnostic accuracy on CheXpert, RSNA Pneumonia, and SIIM-ACR Pneumothorax benchmarks, and outperforms purpose-built gaze prediction models by over 16% in ScanMatch and 22% in SED, demonstrating that modeling how experts read, not just what they conclude, offers a promising pretraining paradigm for medical imaging AI. GazeWorld uses an autoregressive transformer to predict the latent representation of the next fixated patch from previously visited ones, and a spatial-completion branch to handle unvisited regions. At inference, it generates patch representations from the image alone without requiring real gaze data.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: World models in machine learning learn an internal representation of an environment to predict future states. In medical imaging, radiologist eye-tracking data captures how experts search and accumulate evidence, but prior methods used it only as a static prior or auxiliary target. GazeWorld innovates by modeling the fixation sequence as a trajectory in an image world, learning patch representations that encode both diagnostic and gaze information.

**Tags**: `#medical imaging`, `#representation learning`, `#world model`, `#eye-tracking`, `#deep learning`

---

<a id="item-28"></a>
## [Nano World Models: Minimalist Codebase for Video Prediction](https://arxiv.org/abs/2605.23993) ⭐️ 8.0/10

Researchers released Nano World Models, a minimalist and extensible codebase for studying future video prediction using diffusion forcing, along with code, configurations, and pretrained checkpoints. This addresses a gap in the research community by providing a compact, reproducible implementation that enables controlled studies of design choices in world models, which are central to video prediction and decision-making. The codebase unifies generative objectives, model scales, action-conditioning mechanisms, latent observation spaces, datasets, evaluation protocols, and long-horizon rollouts, and was tested on control environments, game simulation, and real-robot data.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: World models are predictive simulators that learn to forecast future states, often used in planning and decision-making. Diffusion forcing is a technique that combines next-token prediction with full-sequence generation, enabling more coherent long-term video prediction.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/diffusion-forcing">Diffusion Forcing</a></li>

</ul>
</details>

**Tags**: `#world models`, `#video prediction`, `#diffusion forcing`, `#reproducibility`, `#AI/ML`

---

<a id="item-29"></a>
## [EEG Decodes Visual Stimuli with 86% Retrieval Accuracy](https://arxiv.org/abs/2605.23996) ⭐️ 8.0/10

A new brain-to-image system achieves 86.3% Top-1 accuracy in retrieving the correct image from 200 candidates using EEG signals, and reconstructs perceived images via multimodal alignment with CLIP embeddings. This work demonstrates that rich visual representations can be decoded from non-invasive EEG with high fidelity, advancing brain-computer interfaces and multimodal AI for applications like communication aids and neural prosthetics. The retrieval model uses multi-level blurring with biologically inspired EVNet features and InfoNCE loss, while the reconstruction model (CognitionCapturerPro) aligns EEG to CLIP embeddings of image, text, depth, and edge, then generates images via SDXL-Turbo with IP-Adapter.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: EEG (electroencephalography) records electrical brain activity non-invasively. CLIP is a multimodal model that aligns images and text in a shared embedding space. InfoNCE is a contrastive loss function used for learning representations by pulling positive pairs together and pushing negatives apart.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2603.12722">[2603.12722] CognitionCapturerPro: Towards High-Fidelity Visual Decoding from EEG/MEG via Multi-modal Information and Asymmetric Alignment</a></li>

</ul>
</details>

**Tags**: `#EEG`, `#brain-computer interface`, `#multimodal learning`, `#image retrieval`, `#image reconstruction`

---

<a id="item-30"></a>
## [IVR-R1: Iterative Visual-Grounded Reasoning RL for Multimodal LLMs](https://arxiv.org/abs/2605.23997) ⭐️ 8.0/10

IVR-R1 introduces an iterative visual-grounded reasoning reinforcement learning framework that dynamically re-aligns visual information to correct reasoning trajectories in multimodal LLMs, addressing visual hallucination and logical errors in long-horizon tasks. This work tackles a critical limitation in multimodal LLMs—visual hallucination and logical errors during long-horizon reasoning—by enabling dynamic visual re-alignment, which could significantly improve the reliability of AI systems in complex visual reasoning tasks. IVR-R1 uses a reward-driven screening mechanism to identify flawed rollouts, performs fine-grained step-level error attribution, and employs a Re-Reasoning Loop that iteratively cross-references intermediate reasoning states with pristine visual priors to synthesize expert-level demonstrations.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: Multimodal large language models (LLMs) combine text and visual information for tasks like visual question answering. However, they often suffer from visual hallucination, where the model generates incorrect visual details, and logical errors in long reasoning chains. Reinforcement learning (RL) is used to improve these models, but existing methods struggle to maintain visual grounding over extended reasoning steps.

**Tags**: `#multimodal LLM`, `#reinforcement learning`, `#visual reasoning`, `#visual hallucination`, `#AI research`

---

<a id="item-31"></a>
## [DIDR: Principled One-Step Generator RL via Diffused Reward](https://arxiv.org/abs/2605.24001) ⭐️ 8.0/10

Researchers propose Diff-Instruct with Diffused Reward (DIDR), a trajectory-level alignment framework for one-step text-to-image generators that propagates reward-optimized distributions across noise levels, improving fidelity while maintaining efficiency. DIDR addresses a key limitation in one-step generation RL by providing a principled method to align reward optimization with generative dynamics, potentially enabling more efficient and higher-quality text-to-image models for real-time applications. DIDR is derived from Integral KL minimization and introduces the Diffused Reward Score (DRS) as a reward-driven correction to the reference score function, with a practical estimator called Diffused Reward Proxy (DRP) based on differentiable short-step denoising.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: One-step text-to-image generators aim to produce images in a single forward pass, offering real-time synthesis but often struggling with fidelity compared to multi-step diffusion models. Reinforcement learning from human feedback (RLHF) can align outputs with preferences, but applying it to one-step generators faces a mismatch between terminal reward optimization and the underlying diffusion dynamics.

**Tags**: `#text-to-image generation`, `#reinforcement learning`, `#diffusion models`, `#one-step generation`, `#RLHF`

---

<a id="item-32"></a>
## [ActQuant: Sub-4-bit Quantization for VLA Models](https://arxiv.org/abs/2605.24011) ⭐️ 8.0/10

ActQuant introduces an action-guided mixed-precision post-training quantization framework that achieves sub-4-bit weight quantization for Vision-Language-Action models, retaining over 94% performance on LIBERO benchmarks and compressing backbone memory by up to 5.3×. This work addresses a critical deployment challenge for VLA models on edge devices, enabling aggressive compression without significant performance loss, which could accelerate real-world embodied intelligence applications like robotic control. ActQuant operates in two stages: an inter-tensor bit allocator assigns bit-widths based on action contribution, and an intra-tensor scale optimizer uses action-aware curvature to focus dynamic range on control-influential weights. It also includes OmniModel.cpp, a conversion pipeline for efficient low-bit kernels on C/C++ runtimes.

rss · arXiv - Computer Vision · May 26, 04:00

**Background**: Vision-Language-Action (VLA) models combine visual perception, language understanding, and action generation for embodied AI tasks like robotic manipulation. Post-training quantization (PTQ) reduces model size and inference cost by lowering numerical precision, but aggressive sub-4-bit quantization often causes severe performance degradation. Mixed-precision quantization assigns different bit-widths to different parts of the model to balance compression and accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Optimization_of_vision-language-action_models_for_edge_devices">Optimization of vision-language-action models for edge devices</a></li>
<li><a href="https://ianloe.medium.com/the-complete-guide-to-vision-language-action-models-how-robots-are-learning-to-think-f1a788d003ed">The Complete Guide to Vision - Language - Action Models ... | Medium</a></li>

</ul>
</details>

**Tags**: `#quantization`, `#VLA models`, `#edge AI`, `#embodied intelligence`, `#PTQ`

---

<a id="item-33"></a>
## [Causality as AI's Statistical Conscience](https://arxiv.org/abs/2605.24076) ⭐️ 8.0/10

A new arXiv paper argues that causal inference is AI's statistical conscience, presenting a Statistical Necessity Theorem for Causal Generalization and a unified framework connecting Pearl's do-calculus, Potential Outcomes, Double Machine Learning, and Invariant Risk Minimization. This work addresses a fundamental limitation of current AI—its inability to distinguish correlation from causation—which is critical for building trustworthy machines that generalize under distribution shift and avoid failures like hallucination and reward hacking. The paper formalizes the distinction between prediction P(Y|X) and intelligence P(Y|do(X)), and identifies three AI failure modes (hallucination, reward hacking, distribution shift degradation) as manifestations of causal blindness, each with a principled statistical remedy.

rss · arXiv - Data Science & Statistics · May 26, 04:00

**Background**: Causal inference is a field that aims to identify cause-effect relationships from data, going beyond mere correlation. Judea Pearl's do-calculus provides a graphical framework for reasoning about interventions, while the Potential Outcomes framework and Double Machine Learning are statistical approaches for estimating causal effects. Invariant Risk Minimization seeks predictors that are robust across environments.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/do_calculus">Do -calculus</a></li>

</ul>
</details>

**Tags**: `#causal inference`, `#artificial intelligence`, `#machine learning`, `#generalization`, `#do-calculus`

---

<a id="item-34"></a>
## [MEDAL: Distilling Manifold Embeddings into Autoencoders](https://arxiv.org/abs/2605.24244) ⭐️ 8.0/10

MEDAL (Manifold Embedding Distillation via Autoencoder Learning) is a novel framework that distills any fitted manifold embedding (e.g., t-SNE, UMAP) into a constrained autoencoder, providing an explicit out-of-sample mapping and an approximate inverse reconstruction for held-out validation. This addresses a critical gap in unsupervised manifold learning by enabling rigorous quantitative validation—previously impossible due to the lack of out-of-sample and inverse mappings—allowing hyperparameter tuning and method comparison for dimension reduction techniques. MEDAL trains a constrained autoencoder whose bottleneck exactly matches the teacher embedding while the decoder reconstructs the original input, yielding a pointwise reconstruction-based distortion measure. It can be applied as a general validation wrapper to any existing dimension reduction method.

rss · arXiv - Data Science & Statistics · May 26, 04:00

**Background**: Nonlinear dimension reduction methods like t-SNE and UMAP are widely used for visualizing high-dimensional data, but they lack out-of-sample mapping (to embed new points) and inverse mapping (to reconstruct original features), making held-out validation—the gold standard in supervised learning—impossible. MEDAL overcomes this by distilling the embedding into an autoencoder model.

<details><summary>References</summary>
<ul>
<li><a href="https://cdn.aaai.org/ojs/7908/7908-13-11436-1-2-20201228.pdf">A Generalised Solution to the Out-of-Sample Extension ...</a></li>
<li><a href="https://ojs.aaai.org/index.php/AAAI/article/view/7696">Local and Global Regressive Mapping for Manifold Learning with Out-of-Sample Extrapolation | Proceedings of the AAAI Conference on Artificial Intelligence</a></li>
<li><a href="https://en.wikipedia.org/wiki/Training,_validation,_and_test_sets">Training, validation, and test data sets - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#manifold learning`, `#autoencoder`, `#dimension reduction`, `#unsupervised learning`, `#data visualization`

---

<a id="item-35"></a>
## [Unified Theory of Multicalibration Boosting](https://arxiv.org/abs/2605.24364) ⭐️ 8.0/10

This paper develops a unified theoretical framework for multicalibration boosting (MCBoost) that subsumes existing variants like multiaccuracy, BatchGCP, and BatchMVP, and reveals a calibration-risk trade-off controlled by early stopping. This work provides a more complete theoretical foundation and practical guidance for multicalibration, which is crucial for fairness, robustness, and reliable prediction in machine learning. The authors show that MCBoost iterates converge to a Bregman projection of the population-optimal predictor, derive convergence rates under different smoothness assumptions, and extend transfer guarantees under covariate shift.

rss · arXiv - Data Science & Statistics · May 26, 04:00

**Background**: Multicalibration extends classical calibration by requiring predictions to be unbiased over a rich collection of functions, including prediction slices and subpopulations. It has become a powerful framework for fairness and reliable prediction, but prior theoretical understanding was fragmented and relied on restrictive assumptions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.24364">[2605.24364] Multicalibration Boosting: Theory, Convergence, and Transferability</a></li>
<li><a href="https://arxiv.org/abs/2301.13767">[2301.13767] Multicalibration as Boosting for Regression</a></li>
<li><a href="https://github.com/mlr-org/mcboost">GitHub - mlr-org/mcboost: Multi-Calibration & Multi-Accuracy Boosting for R · GitHub</a></li>

</ul>
</details>

**Tags**: `#multicalibration`, `#fairness`, `#machine learning theory`, `#boosting`, `#reliable prediction`

---

<a id="item-36"></a>
## [Neural Reward Models Learn Features for Policy Optimization](https://arxiv.org/abs/2605.24749) ⭐️ 8.0/10

This paper provides a theoretical analysis of how neural reward models learn features for KL-regularized policy optimization using a Gaussian single-index model, showing that exponential reward weighting enables feature recovery above a temperature threshold. This work bridges reward modeling and policy optimization theory, offering rigorous bounds on deployment temperature and learning complexity, which is crucial for improving RLHF algorithms and AI alignment. The analysis uses a two-stage neural network: first learning the hidden direction via reward-weighted samples, then fitting the readout layer with weighted ridge regression. The admissible set of deployment temperatures balances the gain from lowering β₂ against the learning cost amplified by exponential weighting.

rss · arXiv - Data Science & Statistics · May 26, 04:00

**Background**: In reinforcement learning from human feedback (RLHF), a reward model is trained to predict human preferences, and then used to optimize a policy via KL-regularized reinforcement learning. The Gaussian single-index model assumes the reward is a function of a linear projection of the input, which simplifies theoretical analysis. Hermite polynomials provide an orthogonal basis for analyzing signals under Gaussian inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.m.wikipedia.org/wiki/Gaussian_function">Gaussian function - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Hermite_polynomials">Hermite polynomials - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#reward modeling`, `#RLHF`, `#theoretical analysis`, `#policy optimization`

---

<a id="item-37"></a>
## [Counterfactual Safety Framework for RL](https://arxiv.org/abs/2605.25114) ⭐️ 8.0/10

This paper introduces a two-stage reinforcement learning procedure that maximizes expected return while controlling individual harm, defined counterfactually as when a chosen action leads to a strictly worse outcome than a baseline alternative. It provides finite-sample guarantees and empirical validation on simulated and real-world datasets. This work addresses the underexplored problem of individual harm in reinforcement learning, moving beyond average-case optimality to ensure safety for each individual. It provides a principled framework with theoretical guarantees, which could be crucial for deploying RL in high-stakes applications like healthcare or autonomous driving. The method uses a two-stage procedure: first learning a baseline policy, then optimizing a harm-constrained objective. The paper derives an upper bound on the sub-optimality gap and shows that the harm rate remains well-controlled with finite samples.

rss · arXiv - Data Science & Statistics · May 26, 04:00

**Background**: Reinforcement learning (RL) typically optimizes for expected return over a population, which can lead to policies that harm certain individuals. Counterfactual reasoning evaluates 'what if' scenarios to understand the impact of decisions not taken. Individual fairness in machine learning aims for consistent treatment of similar individuals, but has been less explored in RL. This paper combines these ideas to propose a new safety framework.

<details><summary>References</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0004370221000060">Counterfactual state explanations for reinforcement learning agents via generative deep learning - ScienceDirect</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fairness_(machine_learning)">Fairness (machine learning) - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2006.11737">[2006.11737] Verifying Individual Fairness in Machine Learning Models</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#safe RL`, `#counterfactual reasoning`, `#individual fairness`, `#machine learning`

---

<a id="item-38"></a>
## [Agentic AI adoption faces organizational readiness gap](https://www.technologyreview.com/2026/05/26/1137584/rethinking-organizational-design-in-the-age-of-agentic-ai/) ⭐️ 8.0/10

A new report reveals that 85% of organizations aim to adopt agentic AI within three years, but 76% admit their current operations and infrastructure cannot support the transition. This gap highlights a critical barrier to enterprise AI transformation, as agentic AI promises autonomous task execution but requires fundamental changes in people, processes, and workflows. The report cites lack of readiness across people, processes, and workflows as the main obstacles, suggesting that organizations must redesign their operations before deploying agentic AI at scale.

rss · MIT Technology Review · May 26, 14:54

**Background**: Agentic AI refers to AI systems that can autonomously take actions to achieve goals, beyond just generating text or suggestions. Unlike traditional AI assistants, agentic AI can orchestrate complex workflows and integrate with external tools, making it attractive for enterprise automation. However, successful adoption requires mature data infrastructure, clear governance, and redesigned workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ibm.com/think/insights/enterprise-ai-agents">Enterprise AI Agents: Beyond Productivity | IBM</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform">Introducing Gemini Enterprise Agent Platform | Google Cloud Blog</a></li>
<li><a href="https://www.grammarly.com/agentic-ai">What is Agentic AI ? | Agentic AI 101</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#organizational design`, `#enterprise AI`, `#AI adoption`

---

<a id="item-39"></a>
## [AI Quietly Erodes Entry-Level Jobs, Creating Looming Crisis](https://www.technologyreview.com/2026/05/26/1137865/its-time-to-address-the-looming-crisis-in-entry-level-work/) ⭐️ 8.0/10

An analysis from MIT Technology Review argues that while AI has not caused mass unemployment, it is quietly eroding entry-level job opportunities, creating a looming crisis for early-career workers. This matters because entry-level jobs are critical for skill development and career progression; their erosion could lead to long-term structural unemployment and inequality, even if aggregate employment remains stable. The article notes that aggregate employment in developed countries remains broadly stable, and recent assessments find limited evidence that AI has shifted headline numbers, but the first rung of the career ladder is weakening.

rss · MIT Technology Review · May 26, 09:00

**Background**: Entry-level jobs have traditionally served as a training ground for new workers, providing essential skills and experience. AI and automation are increasingly capable of performing routine tasks that were once the domain of junior employees, reducing demand for such roles.

**Tags**: `#AI`, `#labor market`, `#entry-level work`, `#employment`, `#technology impact`

---

<a id="item-40"></a>
## [Nasal Spray Reverses Brain Aging in Mice](https://www.sciencedaily.com/releases/2026/05/260526022018.htm) ⭐️ 8.0/10

Researchers at Texas A&M have developed a nasal spray that, after just two doses, reverses brain aging in mice by reducing inflammation and restoring cellular energy systems, leading to improved memory and cognition lasting months. This breakthrough could pave the way for new treatments for age-related neurodegenerative diseases like dementia and Alzheimer's, offering a non-invasive delivery method directly to the brain. The spray targets brain inflammation and mitochondrial dysfunction, two hallmarks of aging. The study, published in April 2026, was led by Dr. Ashok Shetty and colleagues at the Institute for Regenerative Medicine.

rss · ScienceDaily Health · May 26, 13:39

**Background**: Brain aging is associated with chronic low-grade inflammation and declining energy production in neurons. Nasal sprays offer a direct route to the brain, bypassing the blood-brain barrier, making them a promising delivery system for neurological treatments.

<details><summary>References</summary>
<ul>
<li><a href="https://neurosciencenews.com/nasal-spray-reverse-brain-aging-30519/">Nasal Spray Reverses Brain Aging and Inflammation - Neuroscience News</a></li>
<li><a href="https://stories.tamu.edu/news/2026/04/14/scientists-reverse-brain-aging-with-a-nasal-spray/">Scientists reverse brain aging, with a nasal spray – Texas A&M Stories</a></li>

</ul>
</details>

**Tags**: `#neuroscience`, `#aging`, `#dementia`, `#nasal spray`, `#research`

---

<a id="item-41"></a>
## [USC Scientists Discover Hidden Alzheimer's Trigger and Potential Drug Target](https://www.sciencedaily.com/releases/2026/05/260525000504.htm) ⭐️ 8.0/10

USC researchers have identified drug compounds that target the cPLA2 enzyme, potentially reducing brain inflammation linked to Alzheimer's disease, especially in APOE4 gene carriers. 这一发现为阿尔茨海默病（影响数百万人的疾病）提供了新的治疗途径，通过针对高风险APOE4携带者中的特定炎症机制。 The compounds target cPLA2, an enzyme that fuels harmful inflammation but is also important for normal brain activity, suggesting a delicate balance for therapy.

rss · ScienceDaily Health · May 26, 04:56

**Background**: Alzheimer's disease is a progressive neurodegenerative disorder with no cure. The APOE4 gene variant is the strongest genetic risk factor, increasing risk 2-3 fold. cPLA2 is an enzyme involved in lipid signaling and inflammation, and its overactivation has been linked to Alzheimer's pathology.

<details><summary>References</summary>
<ul>
<li><a href="https://med.stanford.edu/news/insights/2025/09/rethinking-alzheimers-gene-variant-apoe4.html">Rethinking Alzheimer’s: Why this common gene variant is bad for your brain</a></li>
<li><a href="https://dornsife.usc.edu/bridge-institute/wp-content/uploads/sites/82/2023/10/C_Valderrama_Mia_BUGSJr2023_ver1.pdf">C_Valderrama_Mia_BUGSJr2023_ver1.pptx</a></li>

</ul>
</details>

**Tags**: `#Alzheimer's`, `#neuroscience`, `#drug discovery`, `#inflammation`, `#APOE4`

---