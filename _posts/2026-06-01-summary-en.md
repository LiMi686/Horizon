---
layout: default
title: "Horizon Summary: 2026-06-01 (EN)"
date: 2026-06-01
lang: en
---

> From 108 items, 35 important content pieces were selected

---

1. [Hackers Exploit Meta AI Bot to Hijack Instagram Accounts](#item-1) ⭐️ 9.0/10
2. [ComfyUI: Modular Node-Based AI Engine for Creators](#item-2) ⭐️ 9.0/10
3. [China Approves World's First Invasive BCI Chip](#item-3) ⭐️ 9.0/10
4. [Daily Pill Doubles Survival for Pancreatic Cancer](#item-4) ⭐️ 9.0/10
5. [Stanford CS336: Build LLMs from Scratch](#item-5) ⭐️ 8.0/10
6. [Nvidia Unveils RTX Spark Arm Chip for Windows PCs](#item-6) ⭐️ 8.0/10
7. [Anthropic Files Confidentially for IPO](#item-7) ⭐️ 8.0/10
8. [Malicious npm Packages Found in Red Hat Cloud Services](#item-8) ⭐️ 8.0/10
9. [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](#item-9) ⭐️ 8.0/10
10. [Anthropic Launches Claude Code: Agentic Coding in Terminal](#item-10) ⭐️ 8.0/10
11. [Build Your Own X: Master Tech by Recreating](#item-11) ⭐️ 8.0/10
12. [Kronos: First Open-Source Foundation Model for Financial Markets](#item-12) ⭐️ 8.0/10
13. [PhyDrawGen: Neuro-Symbolic Pipeline for Physics Diagrams](#item-13) ⭐️ 8.0/10
14. [Query-Conditioned World Models for Embodied AI](#item-14) ⭐️ 8.0/10
15. [Harness Updating vs. Benefit in Self-Evolving LLM Agents](#item-15) ⭐️ 8.0/10
16. [EHRBench: Automated Benchmark for LLM Clinical Decisions](#item-16) ⭐️ 8.0/10
17. [Healthcare Mechanism Design via Policy-as-Code Search](#item-17) ⭐️ 8.0/10
18. [Unicorn: Universal Correlation Network for Time Series](#item-18) ⭐️ 8.0/10
19. [Linear Probes Detect LLM Deception with Near-Perfect Accuracy](#item-19) ⭐️ 8.0/10
20. [NumLeak Reveals LLMs Memorize Public Numeric Benchmarks](#item-20) ⭐️ 8.0/10
21. [LongDS-Bench Reveals AI Agents' Failure in Long Data Analysis](#item-21) ⭐️ 8.0/10
22. [Calibrated Preference Learning: Label Ranking Framework](#item-22) ⭐️ 8.0/10
23. [Autonomous Agentic Data Engineering Boosts LLM Specialization by 57%](#item-23) ⭐️ 8.0/10
24. [Cross-Lingual Steering for Figurative Language Generation](#item-24) ⭐️ 8.0/10
25. [First Bias Study of Multimodal Speech Models](#item-25) ⭐️ 8.0/10
26. [English Prompts Cause Global Narrative Dominance in LLMs](#item-26) ⭐️ 8.0/10
27. [Configurable Reward Model for Balanced Safety Alignment](#item-27) ⭐️ 8.0/10
28. [SANA-Streaming: Real-Time Video Editing on Consumer GPUs](#item-28) ⭐️ 8.0/10
29. [Dex2HOI: Unified Diffusion Model for Bimanual Two-Object Interaction](#item-29) ⭐️ 8.0/10
30. [VLMs Fail to Know When Not to Answer Spatial Questions](#item-30) ⭐️ 8.0/10
31. [Theoretical Analysis of Reward Learning from Best-of-N Data](#item-31) ⭐️ 8.0/10
32. [Last-Layer Linearization Matches Full-Network UQ Performance](#item-32) ⭐️ 8.0/10
33. [Weak Monotonicity Boosts Few-Shot Learning](#item-33) ⭐️ 8.0/10
34. [Bayesian Filtering Unifies Sub-Quadratic Sequence Models](#item-34) ⭐️ 8.0/10
35. [Anytime-Valid Inference Fixes Split Selection in Online Decision Trees](#item-35) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Hackers Exploit Meta AI Bot to Hijack Instagram Accounts](https://simonwillison.net/2026/Jun/1/hackers-simply-asked-meta-ai/#atom-everything) ⭐️ 9.0/10

Hackers have exploited Meta's AI-powered support chatbot to take over high-profile Instagram accounts by simply asking the bot to change the linked email address, bypassing normal account recovery procedures. This vulnerability highlights a critical design flaw in AI support systems, where granting an AI bot privileged access to account recovery tools can lead to severe security breaches, affecting millions of users and undermining trust in AI-driven customer support. The attack involved using a VPN with an IP near the target's location, requesting a password reset, and then chatting with Meta's AI bot to link a new email, after which the bot sent a one-time code allowing a password reset. The exploit did not require sophisticated prompt injection; it was a straightforward request.

rss · Simon Willison · Jun 1, 21:14

**Background**: Prompt injection is a security vulnerability where an attacker manipulates an AI chatbot's behavior by providing malicious input that overrides its intended instructions. In this case, Meta's AI support bot had the ability to change account email and disable 2FA, which are typically high-security actions reserved for verified support staff. The bot's lack of proper authentication and authorization checks allowed the exploit.

<details><summary>References</summary>
<ul>
<li><a href="https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/">Hackers Used Meta’s AI Support Bot to Seize Instagram Accounts</a></li>
<li><a href="https://www.engadget.com/2185225/meta-ai-support-chatbot-made-it-ridiculously-easy-for-hackers-to-take-over-instagram-accounts/">Meta's AI support chatbot made it ridiculously easy for hackers to take over Instagram accounts - Engadget</a></li>
<li><a href="https://gbhackers.com/meta-ai-vulnerability/">Meta AI Vulnerability Allegedly Enables Instagram Password Resets</a></li>

</ul>
</details>

**Discussion**: Commenters expressed shock at Meta's negligence, noting that support requests have always been a weak link in security. Some questioned whether this was an AI-specific issue or just poor design, while others pointed out that the AI should never have been given the ability to remove 2FA or send emails to arbitrary addresses. A user shared a personal experience of having their username stolen via outsourced support, highlighting a recurring pattern.

**Tags**: `#security`, `#AI safety`, `#Meta`, `#Instagram`, `#vulnerability`

---

<a id="item-2"></a>
## [ComfyUI: Modular Node-Based AI Engine for Creators](https://github.com/Comfy-Org/ComfyUI) ⭐️ 9.0/10

ComfyUI has been released as a powerful and modular AI engine for content creation, featuring a graph/nodes interface that supports diffusion models for generating images, videos, 3D models, and audio. ComfyUI democratizes advanced AI content creation by providing a flexible, open-source tool that gives creators full control over models and parameters, enabling sophisticated workflows that can be integrated into production pipelines. ComfyUI natively supports the latest open-source state-of-the-art models and provides API nodes for closed-source models like Nano Banana and Seedance. It is available on Windows, Linux, and macOS via desktop app, portable install, or cloud service.

rss · GitHub Trending - Python · Jun 1, 23:22

**Background**: Diffusion models are a class of generative AI that create data by starting from random noise and gradually refining it into meaningful output. They are widely used for image and video generation, with popular examples including Stable Diffusion and DALL-E. ComfyUI provides a node-based graphical interface that allows users to visually design and connect different model components, making complex AI workflows more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Diffusion_model">Diffusion model</a></li>

</ul>
</details>

**Tags**: `#AI`, `#diffusion models`, `#GUI`, `#content creation`, `#open source`

---

<a id="item-3"></a>
## [China Approves World's First Invasive BCI Chip](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/) ⭐️ 9.0/10

In March 2026, China's National Medical Products Administration (NMPA) approved the Neural Electronic Opportunity (NEO) brain-computer interface developed by Neuracle Medical Technology, making it the first invasive BCI product in the world to be approved for commercial use beyond clinical trials. This milestone marks a significant leap in neurotechnology, potentially transforming treatment for paralysis and other neurological disorders, and positions China as a leader in the global BCI race against rivals like Neuralink. The NEO device is less invasive than Neuralink's implant, as it is not inserted into brain tissue but placed on the brain's surface, and it has already helped a paralyzed patient named Dong Hui regain some mobility, such as holding a pen to write.

rss · MIT Technology Review · Jun 1, 09:09

**Background**: A brain-computer interface (BCI) is a system that reads neural signals to control external devices. Invasive BCIs require surgery to implant electrodes directly on or in the brain, offering higher signal quality than non-invasive methods. China's approval of the NEO device follows years of research and clinical trials, including a study published in January 2023 showing no serious adverse events in patients using a similar stent-electrode array.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/">China has approved the world’s first invasive brain-computer chip—here’s what’s next | MIT Technology Review</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-03-13/china-approves-first-brain-implant-for-commercial-use">China Approves First Brain Implant for Commercial Use - Bloomberg</a></li>
<li><a href="https://en.people.cn/n3/2026/0421/c98649-20448814.html">China approves world's first implantable brain-computer interface for medical use - People's Daily Online</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#neurotechnology`, `#medical device`, `#China`, `#regulatory approval`

---

<a id="item-4"></a>
## [Daily Pill Doubles Survival for Pancreatic Cancer](https://www.bbc.com/news/articles/cy82l435171o?at_medium=RSS&at_campaign=rss) ⭐️ 9.0/10

A daily pill called daraxonrasib has been shown to double survival time for pancreatic cancer patients, marking a major breakthrough in treating this deadly disease. Pancreatic cancer has one of the lowest survival rates among major cancers, with a five-year survival rate of only 13%. This new oral therapy could significantly improve outcomes for patients who currently have few effective treatment options. Daraxonrasib (RMC-6236) is an orally active, multi-selective RAS inhibitor that targets the active, GTP-bound form of RAS proteins, including both mutant and wild-type forms. It uses a tri-complex mechanism to overcome resistance seen with other KRAS inhibitors.

rss · BBC Health · Jun 1, 02:50

**Background**: Pancreatic cancer is notoriously difficult to treat, with most patients diagnosed at an advanced stage when surgery is not possible. The five-year survival rate for stage IV pancreatic cancer is only about 1%, and average survival after diagnosis is around one year. RAS mutations, particularly KRAS, are found in over 90% of pancreatic cancers, making them a key therapeutic target.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Daraxonrasib">Daraxonrasib - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/org/science/article/pii/S1520480425002959">Discovery of Daraxonrasib (RMC-6236), a Potent and Orally ...</a></li>
<li><a href="https://www.cancer.org/cancer/types/pancreatic-cancer/detection-diagnosis-staging/survival-rates.html">Survival Rates for Pancreatic Cancer - American Cancer Society</a></li>

</ul>
</details>

**Tags**: `#cancer`, `#pharmaceuticals`, `#breakthrough`, `#health`, `#pancreatic cancer`

---

<a id="item-5"></a>
## [Stanford CS336: Build LLMs from Scratch](https://cs336.stanford.edu/) ⭐️ 8.0/10

Stanford's CS336 course offers a rigorous, from-scratch implementation of language models, covering the full pipeline from data preprocessing to training and evaluation, with all assignments available online. This course fills a critical gap in practical LLM education by providing hands-on experience with the core components of modern language models, making it valuable for researchers and engineers seeking deep understanding. The course requires significant GPU compute (e.g., B200 at $4.99/hour) and a strong foundation in machine learning (e.g., CS229 or equivalent). Community feedback indicates the first two assignments are particularly challenging and time-consuming.

hackernews · kristianpaul · Jun 1, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48357075)

**Background**: Language models like GPT-4 are typically built using deep learning frameworks (e.g., PyTorch) and trained on massive GPU clusters. CS336 strips away abstractions, requiring students to implement key components—such as attention mechanisms and training loops—from scratch using only basic libraries, mirroring the approach used in early transformer research.

**Discussion**: Community comments are highly positive, with users praising the course's depth and rigor. One user shared that completing the 2025 version took several months of after-work effort, while another debated GPU requirements, noting a 4090 on Vast.ai suffices for early stages. A user also asked about implementation-heavy prerequisites, indicating interest from self-learners.

**Tags**: `#LLM`, `#deep learning`, `#NLP`, `#education`, `#Stanford`

---

<a id="item-6"></a>
## [Nvidia Unveils RTX Spark Arm Chip for Windows PCs](https://www.nvidia.com/en-us/products/rtx-spark/) ⭐️ 8.0/10

Nvidia has announced the RTX Spark, a new Arm-based processor for Windows laptops and desktops, developed in partnership with MediaTek. The chip is set to debut in devices from Microsoft, Dell, HP, ASUS, Lenovo, and MSI. This marks Nvidia's entry into the Windows-on-ARM PC market, directly challenging Intel, AMD, and Apple's M-series chips. The RTX Spark combines Nvidia's GPU and AI capabilities with Arm CPU cores, potentially reshaping the PC landscape. The RTX Spark is a 1-petaflop superchip that supports the full CUDA and RTX ecosystem, and over 100 software providers including Adobe, Blender, and game developers like Riot Games have committed to native Arm versions. However, concerns remain about compatibility, performance, and power consumption.

hackernews · shenli3514 · Jun 1, 05:24 · [Discussion](https://news.ycombinator.com/item?id=48352939)

**Background**: Windows on ARM has historically struggled with software compatibility and performance compared to x86 systems. Apple's successful transition to its own Arm-based M-series chips demonstrated the potential of custom silicon, but Windows on ARM has yet to achieve similar traction. Nvidia's RTX Spark aims to change that by leveraging its GPU and AI expertise.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/05/31/nvidias-new-chip-to-power-fresh-line-of-windows-laptops-by-dell-hp.html">Nvidia jumps into PCs with new Arm-based chip debuting in laptops from Microsoft, Dell, HP</a></li>
<li><a href="https://www.pcmag.com/news/nvidia-rtx-spark-reinvent-pc-computex-2026">Nvidia Unveils RTX Spark, an Arm-Based Superchip for Windows PCs | PCMag</a></li>
<li><a href="https://www.mediatek.com/products/personal-computing/nvidia-rtx-spark">MediaTek | RTX Spark | Next Era of Windows PCs</a></li>

</ul>
</details>

**Discussion**: Community comments express both excitement and skepticism. Some users praise Nvidia's ability to secure native Arm ports for major games and creative apps, while others highlight sharp edges like compatibility issues, overstated performance, and heat generation. There is also curiosity about Linux support.

**Tags**: `#Nvidia`, `#RTX Spark`, `#Arm`, `#Windows on Arm`, `#hardware`

---

<a id="item-7"></a>
## [Anthropic Files Confidentially for IPO](https://www.anthropic.com/news/confidential-draft-s1-sec) ⭐️ 8.0/10

Anthropic has confidentially submitted a draft S-1 registration statement to the U.S. Securities and Exchange Commission (SEC), taking a major step toward an initial public offering (IPO). This move signals Anthropic's maturation as a leading AI company and will subject it to public market scrutiny, potentially impacting the broader AI industry and retail investors. The IPO could also accelerate competition among frontier AI labs. The confidential filing allows Anthropic to keep its financial details private until closer to the IPO date, as permitted under the JOBS Act. The company has not yet disclosed the number of shares or price range.

hackernews · surprisetalk · Jun 1, 16:00 · [Discussion](https://news.ycombinator.com/item?id=48358646)

**Background**: An S-1 is a registration statement required by the SEC for companies planning to go public, containing detailed financial and business information. A confidential filing allows emerging growth companies to initially submit their S-1 privately, reducing market speculation and allowing them to refine the document before public disclosure.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Form_S-1">Form S-1 - Wikipedia</a></li>
<li><a href="https://www.investopedia.com/terms/s/sec-form-s-1.asp">What Is SEC Form S-1? Filing Steps & Amendment Guidelines</a></li>
<li><a href="https://www.dfinsolutions.com/knowledge-hub/thought-leadership/knowledge-resources/confidential-ipo-filings">Confidential IPO Filings | DFIN</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concerns about the timing and potential risks, noting that the IPO rush may be driven by favorable current financials and a desire to go public before market conditions worsen. Some worry that quarterly earnings pressure could challenge AI companies' long-term ethos and lead to anti-competitive behavior.

**Tags**: `#Anthropic`, `#IPO`, `#AI industry`, `#finance`, `#regulation`

---

<a id="item-8"></a>
## [Malicious npm Packages Found in Red Hat Cloud Services](https://github.com/RedHatInsights/javascript-clients/issues/492) ⭐️ 8.0/10

Multiple npm packages in the @redhat-cloud-services scope were found to contain malicious payloads that execute via a preinstall hook, stealing cloud credentials and secrets across AWS, Azure, GCP, and other platforms. This real-world supply chain attack on Red Hat's official packages highlights the ongoing threat to the npm ecosystem and underscores the urgent need for stronger defenses like dependency cooldowns and MFA. The malicious packages deploy a multi-stage credential stealer targeting AWS access keys, GCP service accounts, Azure tokens, Kubernetes secrets, and more. Affected versions span multiple packages in the RedHat Cloud Services frontend ecosystem.

hackernews · kurmiashish · Jun 1, 13:30 · [Discussion](https://news.ycombinator.com/item?id=48356625)

**Background**: Supply chain attacks on npm occur when attackers compromise legitimate packages to inject malicious code, often executed during installation. Dependency cooldowns (delaying installation of new packages by 1-3 days) and MFA for publishing are recommended mitigations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.stepsecurity.io/blog/multiple-redhat-cloud-services-npm-packages-compromised">Multiple redhat-cloud-services npm Packages compromised - StepSecurity</a></li>
<li><a href="https://cybersecuritynews.com/red-hat-cloud-services-npm-packages/">Multiple Red Hat Cloud Services npm Packages Compromised to Deploy Credential-Stealing Malware</a></li>
<li><a href="https://www.mend.io/blog/redhat-cloud-services-packages-drop-multi-cloud-credential-stealer/">Miasma: Red Hat Cloud Services npm Packages Hit by a Mini Shai-Hulud-Style Campaign</a></li>

</ul>
</details>

**Discussion**: Community comments emphasize the effectiveness of dependency cooldowns and MFA, with some noting that tools like yarn 4 already offer cooldown options. Others point out that many attacks are caught within 1-3 days, making cooldowns a practical defense.

**Tags**: `#npm`, `#supply chain security`, `#Red Hat`, `#open source`, `#dependency management`

---

<a id="item-9"></a>
## [OpenBMB Releases VoxCPM2: Tokenizer-Free TTS Model](https://github.com/OpenBMB/VoxCPM) ⭐️ 8.0/10

OpenBMB has released VoxCPM2, a 2-billion-parameter tokenizer-free text-to-speech model trained on over 2 million hours of multilingual speech data, supporting 30 languages, voice design, and voice cloning. VoxCPM2 advances open-source TTS by eliminating discrete tokenization, enabling more natural and expressive speech synthesis, and offering creative voice design from text descriptions alone. The model uses a diffusion autoregressive architecture built on a MiniCPM-4 backbone and outputs 48kHz studio-quality audio. It supports controllable voice cloning with optional style guidance and ultimate cloning that preserves all vocal nuances.

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**Background**: Traditional TTS systems often use discrete tokenizers (e.g., audio codecs) to convert speech into tokens, which can lose prosodic and emotional nuances. Tokenizer-free models like VoxCPM2 directly generate continuous speech representations, preserving naturalness. OpenBMB is known for open-source large language models like MiniCPM.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/OpenBMB/VoxCPM/">GitHub - OpenBMB/VoxCPM: VoxCPM2: Tokenizer-Free TTS for ...</a></li>
<li><a href="https://medium.com/data-science-in-your-pocket/voxcpm-1-5-tokenizer-free-tts-with-voice-cloning-c63059b85882">VoxCPM 1.5: Tokenizer-Free TTS with Voice Cloning | by Mehul Gupta | Data Science in Your Pocket | Medium</a></li>
<li><a href="https://deepwiki.com/OpenBMB/VoxCPM/5.2-voxcpmmodel-and-voxcpm2model">VoxCPMModel and VoxCPM2Model | OpenBMB/VoxCPM | DeepWiki</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#speech generation`, `#voice cloning`, `#multilingual`, `#open-source`

---

<a id="item-10"></a>
## [Anthropic Launches Claude Code: Agentic Coding in Terminal](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic has released Claude Code, an agentic coding tool that operates directly in the terminal, understands entire codebases, and automates tasks like code editing, git workflows, and complex code explanation through natural language commands. Claude Code brings powerful AI assistance directly into the developer's terminal environment, reducing context switching and enabling faster, more intuitive coding workflows. It competes with other agentic coding tools like Cursor and Cline, potentially reshaping how developers interact with AI in daily development. Claude Code supports installation via curl, Homebrew, WinGet, and npm (deprecated), and requires Node.js 18+. It also offers plugins for extended functionality and integrates with GitHub via @claude mentions.

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**Background**: Agentic coding tools are AI-powered assistants that can autonomously perform coding tasks within a developer's environment, such as editing files, running commands, and managing version control. Unlike traditional code completion tools, they understand the full context of a project and can execute multi-step workflows based on natural language instructions.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/anthropics/claude-code">GitHub - anthropics/claude-code: Claude Code is an agentic ...</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://claude.com/blog/introduction-to-agentic-coding">Introduction to agentic coding | Claude</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer-tools`, `#coding-assistant`, `#Anthropic`, `#CLI`

---

<a id="item-11"></a>
## [Build Your Own X: Master Tech by Recreating](https://github.com/codecrafters-io/build-your-own-x) ⭐️ 8.0/10

The 'build-your-own-x' repository on GitHub curates step-by-step guides for recreating over 20 popular technologies from scratch, including databases, Git, Docker, and programming languages. This resource promotes deep learning by encouraging developers to build technologies themselves, which is more effective than passive consumption. It has become a widely referenced compilation in the developer community for hands-on learning. The repository covers topics like 3D renderers, blockchain, emulators, neural networks, operating systems, and search engines. Each guide is well-written and step-by-step, suitable for intermediate to advanced programmers.

rss · GitHub Trending - Daily (All) · Jun 1, 23:22

**Background**: The repository is inspired by Richard Feynman's quote, 'What I cannot create, I do not understand.' It aligns with the learning-by-building approach, which is a proven method for mastering complex systems. The project is maintained by CodeCrafters, a platform that offers interactive coding challenges.

**Tags**: `#learning`, `#programming`, `#tutorials`, `#open-source`, `#curriculum`

---

<a id="item-12"></a>
## [Kronos: First Open-Source Foundation Model for Financial Markets](https://github.com/shiyu-coder/Kronos) ⭐️ 8.0/10

Kronos, the first open-source foundation model for financial candlesticks (K-lines), has been released, trained on data from over 45 global exchanges. It was accepted by AAAI 2026 and a live demo is available. Kronos addresses the gap in applying foundation models to financial time series, offering a unified model for tasks like price forecasting and volatility prediction. This could democratize access to advanced quantitative finance tools. Kronos uses a two-stage framework: a specialized tokenizer discretizes OHLCV data into hierarchical tokens, then an autoregressive Transformer is pre-trained on them. The model family includes variants like Kronos-mini (4M parameters).

rss · GitHub Trending - Python · Jun 1, 23:22

**Background**: Foundation models are large pre-trained models that can be adapted to various downstream tasks. While successful in NLP and general time series, their application to financial K-line data—which captures open, high, low, close prices and volume—has been limited due to high noise and unique patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2508.02739">Kronos: A Foundation Model for the Language of Financial Markets GitHub - shiyu-coder/Kronos: Kronos: A Foundation Model for ... Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the Language of Financial Markets Kronos: A Foundation Model for the Language of Financial Markets NeurIPS Kronos: A Foundation Model for the Language of ... Kronos Live Forecast | BTC/USDT</a></li>
<li><a href="https://github.com/shiyu-coder/Kronos">GitHub - shiyu-coder/Kronos: Kronos: A Foundation Model for ...</a></li>
<li><a href="https://ojs.aaai.org/index.php/AAAI/article/download/39730/43691">Kronos: A Foundation Model for the Language of Financial Markets</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Finance`, `#Foundation Model`, `#LLM`

---

<a id="item-13"></a>
## [PhyDrawGen: Neuro-Symbolic Pipeline for Physics Diagrams](https://arxiv.org/abs/2605.30512) ⭐️ 8.0/10

PhyDrawGen is a neuro-symbolic pipeline that generates physically accurate diagrams from natural language by combining LLM-based scene graph extraction with deterministic constraint solving and iterative visual verification. This addresses a critical limitation of current generative models that hallucinate force vectors and violate physical laws, with potential impact on AI/ML and physics education. The pipeline first extracts a typed scene graph using an LLM, then converts it into a Planar Straight-Line Graph (PSLG) via a deterministic solver, and finally uses a fine-tuned Qwen-VL model in a propose-verify loop to correct violations. It outperforms GPT-5-image, Gemini 2.5 Flash, and Gemini 3 Pro on a benchmark of 1,449 problems across mechanics, optics, and electromagnetism.

rss · arXiv - AI · Jun 1, 04:00

**Background**: Current generative models like GPT-5 and Gemini produce visually plausible images but often violate physical constraints such as force balance and conservation laws. Neuro-symbolic AI combines neural networks with symbolic reasoning to reduce hallucinations. A Planar Straight-Line Graph (PSLG) is a graph embedded in the plane with straight edges, used here to encode geometric constraints precisely.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Neuro-symbolic_AI">Neuro-symbolic AI - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Planar_straight-line_graph">Planar straight - line graph - Wikipedia</a></li>
<li><a href="https://medium.com/@sebuzdugan/how-to-build-a-propose-verify-loop-for-reliable-llm-reasoning-in-production-f85d246fd0c1">How to build a propose - verify loop for reliable LLM... | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#diagram generation`, `#physics`, `#neuro-symbolic`, `#NLP`

---

<a id="item-14"></a>
## [Query-Conditioned World Models for Embodied AI](https://arxiv.org/abs/2605.30542) ⭐️ 8.0/10

This paper argues that embodied AI requires physically viable world models that answer intervention queries by identifying the simplest physical abstraction, rather than merely predicting observations. This work exposes a fundamental structural failure in current observation-predictive world models, which can produce physically wrong rollouts and recommend unsafe actions. It provides a design principle for building interpretable, verifiable, and auditable world models, with potential impact on robotics and AI safety. The paper introduces controlled benchmarks that fix the visible scene while varying latent physics to expose failures. It proposes a modular architecture with an autonomous orchestrator that selects the simplest physical abstraction sufficient for a given intervention query.

rss · arXiv - AI · Jun 1, 04:00

**Background**: World models in embodied AI are internal simulators that predict how actions affect future states. Current models often predict future observations (e.g., video frames) but fail to capture latent physics, leading to visually plausible but physically incorrect rollouts. Intervention queries ask what would happen if a specific action were taken, requiring causal understanding of the environment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.16732">A Comprehensive Survey on World Models for Embodied AI A Survey of Embodied World Models GitHub - Li-Zn-H/AwesomeWorldModels: A Comprehensive Survey ... Frontiers | A review of embodied intelligence systems: a ... Embodied AI: From LLMs to World Models [Feature] | IEEE ... World Action Models: The Next Frontier in Embodied AI ‘World models’ are AI’s latest sensation: what are they and ...</a></li>
<li><a href="https://fi.ee.tsinghua.edu.cn/public/publications/0940dda4-af15-11f0-9d60-0242ac120002.pdf">A Survey of Embodied World Models</a></li>

</ul>
</details>

**Tags**: `#embodied AI`, `#world models`, `#physics`, `#robotics`, `#AI safety`

---

<a id="item-15"></a>
## [Harness Updating vs. Benefit in Self-Evolving LLM Agents](https://arxiv.org/abs/2605.30621) ⭐️ 8.0/10

This paper disentangles two distinct capabilities in self-evolving LLM agents: harness-updating (producing useful harness updates) and harness-benefit (benefiting from updated harnesses), revealing that harness-updating is surprisingly flat across model capability tiers. These findings challenge common assumptions about model capability tiers and suggest that investing in the task-solving agent rather than the evolver may be more effective, with implications for designing and evaluating agent systems. Weak-tier models fail to activate or follow harness artifacts, mid-tier models benefit most, and strong-tier models benefit less than mid-tier; Qwen3.5-9B's updates yield gains comparable to Claude Opus 4.6.

rss · arXiv - AI · Jun 1, 04:00

**Background**: LLM agents use external harnesses (prompts, skills, memories, tools) to shape task execution without changing model parameters. Harness self-evolution adapts these agents by updating harnesses from execution evidence, but it was unclear how base capability relates to evolution capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://www.langchain.com/blog/the-anatomy-of-an-agent-harness">The Anatomy of an Agent Harness - langchain.com</a></li>
<li><a href="https://parallel.ai/articles/what-is-an-agent-harness">What is an agent harness in the context of large-language ...</a></li>
<li><a href="https://harness-engineering.ai/blog/agent-harness-complete-guide/">The Complete Guide to Agent Harness: What It Is and Why It ...</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#self-evolution`, `#harness`, `#capability analysis`, `#AI research`

---

<a id="item-16"></a>
## [EHRBench: Automated Benchmark for LLM Clinical Decisions](https://arxiv.org/abs/2605.30637) ⭐️ 8.0/10

Researchers introduced EHRBench, an automated and reliable benchmark grounded in electronic health records (EHRs) for evaluating LLMs on clinical decision-making tasks, including diagnosis, treatment, and prognosis. EHRBench addresses a critical gap in evaluating LLMs for real-world clinical decision-making, providing a scalable and reliable pipeline that can help improve the safety and trustworthiness of AI in healthcare. The benchmark was constructed using an EHR-LLM-KB interaction pipeline, generating nearly 1 million QA items across three core tasks, and was used to evaluate over 30 representative LLMs, revealing consistent capability trends and actionable gaps.

rss · arXiv - AI · Jun 1, 04:00

**Background**: Clinical decision-making (CDM) involves inferring diagnoses, selecting treatments, or predicting outcomes under incomplete evidence. LLMs are increasingly used to support CDM due to their language capabilities and biomedical knowledge, but their reliability on real-world tasks is not well understood. Existing benchmarks often lack automation, scalability, or grounding in real patient data.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30637">[2605.30637] EHRBench : An Automated and Reliable EHR -based...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#clinical decision-making`, `#benchmark`, `#EHR`, `#healthcare AI`

---

<a id="item-17"></a>
## [Healthcare Mechanism Design via Policy-as-Code Search](https://arxiv.org/abs/2605.30680) ⭐️ 8.0/10

This paper recasts hospital mechanism design as program synthesis for language models, using a multi-agent simulator (Medi-Sim) to evaluate strategic provider responses and synthesize inspectable rule programs. This approach enables evaluation of healthcare policies by the equilibrium they produce, rather than assuming fixed provider behavior, which could lead to more robust and effective healthcare AI and policy design. The simulator includes five strategic provider channels (coding, selection, delay, effort, triage) and an LLM-guided evolutionary code search synthesizes a mixed-objective program that eliminates up-coding, halves rejection, and retains most profit-oriented baseline funds.

rss · arXiv - AI · Jun 1, 04:00

**Background**: Policy-as-code is the practice of expressing organizational policies as executable, version-controlled code that enforces rules automatically. Goodhart's law states that when a measure becomes a target, it ceases to be a good measure. This paper applies these concepts to healthcare mechanism design, using program synthesis with large language models to generate inspectable policies.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Goodhart's_law">Goodhart ' s law - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2108.07732">[2108.07732] Program Synthesis with Large Language Models</a></li>

</ul>
</details>

**Tags**: `#healthcare AI`, `#mechanism design`, `#program synthesis`, `#multi-agent simulation`, `#policy-as-code`

---

<a id="item-18"></a>
## [Unicorn: Universal Correlation Network for Time Series](https://arxiv.org/abs/2605.30376) ⭐️ 8.0/10

Unicorn introduces a latent prototype codebook that decouples correlation modeling from specific channel identities, enabling scalable multi-dataset pretraining for high-dimensional time series forecasting. This approach bridges the gap between channel-independent and channel-dependent models, achieving state-of-the-art performance especially in few-shot transfer scenarios, paving the way for multivariate time series foundation models. Unicorn learns identity-agnostic, reusable interaction patterns across heterogeneous datasets with varying dimensionalities and semantics, significantly outperforming existing architectures in few-shot settings.

rss · arXiv - Machine Learning · Jun 1, 04:00

**Background**: Time series forecasting models face a trade-off: channel-independent models scale well but ignore inter-channel dependencies, while channel-dependent models capture dependencies but struggle to generalize across datasets. Unicorn uses a latent prototype codebook to learn universal correlation patterns, enabling transfer across domains.

**Tags**: `#time series forecasting`, `#deep learning`, `#transfer learning`, `#high-dimensional data`, `#correlation modeling`

---

<a id="item-19"></a>
## [Linear Probes Detect LLM Deception with Near-Perfect Accuracy](https://arxiv.org/abs/2605.30381) ⭐️ 8.0/10

A multi-model study shows that linear probes can detect synthetic dishonesty in LLMs with near-perfect AUC (≥0.99) from early layers across five transformer architectures, supporting the Linear Representation Hypothesis. This work provides a robust, domain-invariant method for detecting deception in LLMs, which is crucial for AI safety and alignment research, especially for monitoring models in high-stakes applications. Logistic regression probes consistently matched or outperformed MLP probes, and probes trained on TruthfulQA generalized with near-zero loss to held-out MMLU subjects. Late-layer representations showed strong robustness to Gaussian noise, with Gemma-2 models exhibiting exceptional stability.

rss · arXiv - Machine Learning · Jun 1, 04:00

**Background**: The Linear Representation Hypothesis posits that high-level concepts are represented linearly as directions in a model's representation space. Synthetic dishonesty is induced via direct optimization on incorrect answers, providing a controlled testbed for studying learned deception. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that introduces small trainable matrices, allowing efficient adaptation of large models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30381">[2605.30381] When LLMs Learn to Be Consistently Wrong: A ...</a></li>
<li><a href="https://arxiv.org/abs/2311.03658">[2311.03658] The Linear Representation Hypothesis and the ...</a></li>
<li><a href="https://github.com/vzm1399/llm-dishonesty-representations/blob/main/README.md">llm-dishonesty-representations/README.md at main - GitHub</a></li>

</ul>
</details>

**Tags**: `#AI safety`, `#deceptive alignment`, `#LLM interpretability`, `#probing`, `#representation learning`

---

<a id="item-20"></a>
## [NumLeak Reveals LLMs Memorize Public Numeric Benchmarks](https://arxiv.org/abs/2605.30393) ⭐️ 8.0/10

NumLeak, a new measurement framework, demonstrates that top-tier LLMs like GPT-4 and Claude memorize public numeric benchmarks such as Fama-French market excess returns with near-perfect correlation (r=0.97-0.99), undermining the validity of out-of-sample evaluations. This research exposes a critical flaw in LLM evaluation methodology: many benchmarks thought to measure reasoning or skill may actually be measuring memorization, which could lead to overestimated model capabilities and misguide AI safety assessments. The framework combines API-boundary probes on production models with white-box validation on an open causal LM, and shows that a one-line system-prompt defense blocks 99.8% of non-adaptive suffix attacks with near-zero utility cost.

rss · arXiv - Machine Learning · Jun 1, 04:00

**Background**: Benchmark contamination occurs when evaluation data appears in a model's training set, making it hard to tell if the model is recalling memorized answers or demonstrating genuine skill. The Fama-French factors are widely used financial models that explain stock returns using market, size, and value factors. NumLeak specifically tests whether LLMs recall exact historical numeric values from these and other public datasets.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.30393">[2605.30393] NumLeak: Public Numeric Benchmarks as Latent ...</a></li>
<li><a href="https://github.com/akotawala10/NumLeak_ICML2026">akotawala10/NumLeak_ICML2026 - GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#memorization`, `#benchmark contamination`, `#evaluation`, `#AI safety`

---

<a id="item-21"></a>
## [LongDS-Bench Reveals AI Agents' Failure in Long Data Analysis](https://arxiv.org/abs/2605.30434) ⭐️ 8.0/10

Researchers introduced LongDS-Bench, a benchmark of 68 tasks from real Kaggle notebooks with 2,225 turns across six domains, to evaluate AI agents on long-horizon, multi-turn data analysis. The best model achieved only 48.45% accuracy, with performance dropping nearly 47 points from early to late turns. This benchmark highlights a critical gap in current AI agents: they struggle to maintain and compose analytical state over long interactions, which is essential for real-world iterative data analysis. The findings suggest that improving state tracking, rather than increasing interaction steps, is key to advancing agentic reasoning. Tasks are designed around state-evolution patterns like counterfactual perturbation, rollback, and multi-state composition, with an average dependency span of 11.3 turns. Long-horizon errors account for 52%–69% of failures, and additional agent steps do not necessarily improve performance.

rss · arXiv - Machine Learning · Jun 1, 04:00

**Background**: Real-world data analysis is often iterative, requiring agents to track evolving context across multiple steps. Existing benchmarks mostly evaluate isolated or short interactive tasks, failing to test long-horizon reasoning. LongDS fills this gap by focusing on maintaining and composing analytical state over many turns.

<details><summary>References</summary>
<ul>
<li><a href="https://llm-stats.com/benchmarks/longbench-v2">LongBench v2 Benchmark Leaderboard</a></li>
<li><a href="https://arxiv.org/html/2601.02872v1">LongBench Pro: A More Realistic and Comprehensive Bilingual Long-Context Evaluation Benchmark</a></li>

</ul>
</details>

**Tags**: `#benchmark`, `#data analysis`, `#AI agents`, `#long-horizon reasoning`, `#evaluation`

---

<a id="item-22"></a>
## [Calibrated Preference Learning: Label Ranking Framework](https://arxiv.org/abs/2605.30447) ⭐️ 8.0/10

This paper formalizes calibration for probabilistic label ranking, introducing a hierarchy of calibration notions including full, sub-ranking, and top-k calibration, and proves their relationships. It empirically shows that popular label ranking models, including RLHF reward models, are often poorly calibrated. This work bridges a gap in calibration research by extending it to label ranking, which is crucial for reliable decision-making in preference learning. The findings have direct implications for improving the trustworthiness of RLHF reward models used in aligning large language models. The paper proves that full-rank calibration implies sub-ranking and top-k calibration, but not vice versa, and that sub-ranking and top-k calibration are incomparable. Experiments reveal that calibration correlates strongly but not perfectly with benchmark accuracy in RLHF reward models, indicating it captures a distinct quality dimension.

rss · arXiv - Machine Learning · Jun 1, 04:00

**Background**: Calibration measures how well predicted probabilities match actual outcomes, and is well-studied for classification and regression. Probabilistic label ranking (ProLR) models a distribution over all possible orderings of labels, which is more structured than multi-class classification. RLHF reward models assign scores to responses to align LLMs with human preferences, and their calibration is important for reliable training.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30447">Calibrated Preference Learning: The Case of Label Ranking</a></li>
<li><a href="https://arxiv.org/abs/2410.09724">Taming Overconfidence in LLMs: Reward Calibration in RLHF Images TAMING OVERCONFIDENCE IN LLMS: REWARD CALIBRATION IN RLHF Reward Calibration for Continual Reinforcement Learning from ... Calibration of Reward Models - apxml.com Reward models: 8 calibration steps that reduce overconfidence Taming Overconfidence in LLMs: Reward Calibration in RLHF GitHub - SeanLeng1/Reward-Calibration</a></li>

</ul>
</details>

**Tags**: `#calibration`, `#label ranking`, `#RLHF`, `#machine learning`, `#probability`

---

<a id="item-23"></a>
## [Autonomous Agentic Data Engineering Boosts LLM Specialization by 57%](https://arxiv.org/abs/2605.30407) ⭐️ 8.0/10

Researchers propose Autonomous Agentic Data Engineering, where LLMs autonomously plan, generate, and iteratively optimize training data for model specialization, achieving a 57.29% improvement on a student model using GPT-5.2. This work demonstrates that LLMs can autonomously drive the entire data engineering pipeline for model specialization, potentially reducing human effort and enabling more efficient adaptation to specialized domains. The paper formalizes a new task called Autonomous Agentic Data Engineering and shows that iterative, agent-driven data adaptation yields substantial gains. The code will be released on GitHub.

rss · arXiv - NLP · Jun 1, 04:00

**Background**: Large Language Models (LLMs) often struggle in specialized domains due to lack of high-quality domain-specific data. Traditional data curation methods rely on human-designed workflows, while this work explores fully autonomous data engineering by LLM agents.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30407">Exploring Autonomous Agentic Data Engineering for Model ...</a></li>
<li><a href="https://www.linkedin.com/pulse/agentic-ai-data-engineering-autonomous-pipeline-ashutosh-sharma-jxwrc">Agentic AI in Data Engineering: The Autonomous Data Pipeline ...</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/three-step-design-pattern-for-specializing-llms/">A three-step design pattern for specializing LLMs | Google ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#data engineering`, `#model specialization`, `#autonomous agents`, `#AI`

---

<a id="item-24"></a>
## [Cross-Lingual Steering for Figurative Language Generation](https://arxiv.org/abs/2605.30443) ⭐️ 8.0/10

Researchers demonstrate that activation steering directions for figurative language learned in one language can transfer to others, sometimes matching or surpassing native directions. This finding provides direct evidence of reusable cross-lingual signals for figurative generation, potentially enabling more efficient multilingual LLM control and improving interpretability. The study tested five figurative categories, six languages, and four multilingual LLMs, finding that German was among the most receptive target languages for cross-lingual transfer.

rss · arXiv - NLP · Jun 1, 04:00

**Background**: Activation steering is an inference-time method that modifies a model's internal representations to guide its behavior. Figurative language generation (FLG) involves reformulating text to include figures of speech like metaphor or simile. This work probes whether internal signals for figurative language are language-specific or reusable across languages.

<details><summary>References</summary>
<ul>
<li><a href="https://sidn.baulab.info/steering/">The Development of Activation Steering - sidn.baulab.info</a></li>
<li><a href="https://dl.acm.org/doi/full/10.1145/3654795">A Survey on Automatic Generation of Figurative Language : From...</a></li>

</ul>
</details>

**Tags**: `#multilingual LLMs`, `#figurative language`, `#activation steering`, `#NLP`, `#interpretability`

---

<a id="item-25"></a>
## [First Bias Study of Multimodal Speech Models](https://arxiv.org/abs/2605.30472) ⭐️ 8.0/10

Researchers conducted the first bias evaluation of multimodal speech recognition models, finding that pairing different faces with the same audio causes transcription accuracy drops of up to 4.05 WER points across gender and ethnicity. This reveals that adding visual modalities can introduce demographic biases, contradicting the assumption that more data always improves fairness, and highlights the need for bias evaluation in multimodal AI systems. The study evaluated mWhisper-Flamingo and Gemini models, measuring word error rate (WER) changes when faces of different self-declared genders and ethnicities were paired with identical audio clips.

rss · arXiv - NLP · Jun 1, 04:00

**Background**: Multimodal speech recognition combines audio with visual cues like lip movements to improve accuracy in noisy environments. Word error rate (WER) measures the percentage of incorrectly transcribed words. Prior bias research focused on single-modality systems, leaving multimodal models unexamined.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.01547v1">mWhisper- Flamingo for Multilingual Audio-Visual Noise-Robust...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Word_error_rate">Word error rate - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#bias`, `#multimodal`, `#speech recognition`, `#fairness`, `#AI ethics`

---

<a id="item-26"></a>
## [English Prompts Cause Global Narrative Dominance in LLMs](https://arxiv.org/abs/2605.30481) ⭐️ 8.0/10

A new paper introduces CulturalNB, a dataset of 717 Bengali cultural instances, and evaluates nine LLMs to reveal that asking questions in English systematically increases global narrative dominance and reduces local perspective coverage. This research highlights a critical flaw in LLMs used as cross-lingual knowledge interfaces: they propagate globally dominant narratives at the expense of local cultural knowledge, which can lead to cultural erasure and bias in AI systems. The study used question-only and evidence-based prompting with human and LLM judges, measuring cross-lingual consistency, language anchoring, global substitution, institutional bias, and epistemic perspective coverage.

rss · arXiv - NLP · Jun 1, 04:00

**Background**: Large language models (LLMs) are increasingly used as cross-lingual knowledge interfaces, but they often reflect globally dominant narratives rather than local cultural contexts. This paper focuses on Bangla, a low-resource language, to study this phenomenon, termed 'global narrative dominance.' The CulturalNB dataset provides parallel Bangla-English question-answer pairs with sociocultural annotations to enable systematic evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2604.22749">Representational Harms in LLM-Generated Narratives Against ...</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/3774904.3793008">From Words to Worlds: Measuring Cultural Narrative Bias in ...</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#cross-lingual`, `#cultural bias`, `#NLP`, `#dataset`

---

<a id="item-27"></a>
## [Configurable Reward Model for Balanced Safety Alignment](https://arxiv.org/abs/2605.30487) ⭐️ 8.0/10

Researchers propose the Configurable Safety Reward Model (CSRM), which adapts to varying safety specifications and achieves state-of-the-art performance on configurable safety benchmarks like CoSApien (94.6% F1) and DynaBench (75.8% F1) without additional human annotation. This work addresses a critical challenge in AI safety by enabling LLMs to flexibly adhere to heterogeneous and evolving safety requirements, improving the helpfulness-safety tradeoff. It provides a practical solution for deploying LLMs in diverse real-world contexts with varying safety standards. CSRM is jointly optimized for calibrated safety compliance and reward modeling, using configuration-targeted data augmentation that enforces instruction adherence while preserving relative severity structure. It achieves strong generalization to unseen safety configurations.

rss · arXiv - NLP · Jun 1, 04:00

**Background**: Large language models (LLMs) are often aligned to safety requirements via instruction tuning or reward models, but these methods struggle to generalize to new or diverse safety configurations. Configurable safety benchmarks like CoSApien and DynaBench evaluate models' ability to follow varying safety policies. CSRM builds on prior work in controllable safety alignment, such as the CoSAlign model and dataset from Microsoft.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.30487v1">Configurable Reward Model for Balanced Safety Alignment</a></li>
<li><a href="https://huggingface.co/datasets/microsoft/CoSApien/blob/main/README.md">README.md · microsoft/CoSApien at main - Hugging Face</a></li>
<li><a href="https://github.com/microsoft/controllable-safety-alignment">Controllable Safety Alignment - GitHub</a></li>

</ul>
</details>

**Tags**: `#LLM alignment`, `#reward model`, `#AI safety`, `#configurable safety`

---

<a id="item-28"></a>
## [SANA-Streaming: Real-Time Video Editing on Consumer GPUs](https://arxiv.org/abs/2605.30409) ⭐️ 8.0/10

SANA-Streaming introduces a hybrid diffusion transformer and system co-design that achieves real-time 1280x704 resolution video-to-video editing at 24 FPS on a single RTX 5090 GPU. This work enables real-time, high-resolution streaming video editing on consumer hardware, which is critical for interactive applications like live broadcasting and gaming, and significantly outperforms existing state-of-the-art methods in both temporal coherence and throughput. The framework combines a Hybrid Diffusion Transformer with softmax attention in some blocks for better local modeling, a Cycle-Reverse Regularization training strategy for temporal consistency without paired long videos, and a system co-design with fused GDN kernels and Mixed-Precision Quantization optimized for NVIDIA Blackwell architecture.

rss · arXiv - Computer Vision · Jun 1, 04:00

**Background**: Video-to-video editing requires maintaining temporal consistency across frames while achieving high throughput for real-time applications. Diffusion transformers have shown promise but suffer from quadratic attention complexity, making real-time high-resolution editing challenging. Hybrid attention mechanisms that combine softmax and linear attention aim to balance quality and efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.30409">SANA-Streaming: Real-time Streaming Video Editing with Hybrid...</a></li>

</ul>
</details>

**Tags**: `#video editing`, `#diffusion transformer`, `#real-time`, `#system co-design`, `#AI/ML`

---

<a id="item-29"></a>
## [Dex2HOI: Unified Diffusion Model for Bimanual Two-Object Interaction](https://arxiv.org/abs/2605.30444) ⭐️ 8.0/10

Dex2HOI introduces a unified diffusion model that generates dexterous bimanual interactions with two objects from text descriptions, using a dual-stream diffusion approach and a motion fusion network. This work addresses the underexplored problem of bimanual two-object interaction generation, moving beyond single-object HOI synthesis and enabling more realistic human motion for robotics, animation, and VR applications. The model achieves up to 540x inference speed-up over prior methods by sampling autoregressively over prefix-conditioned windows, eliminating test-time optimization. It also incorporates hand-relative object representations and contact-aware conditioning.

rss · arXiv - Computer Vision · Jun 1, 04:00

**Background**: Human-object interaction (HOI) generation aims to synthesize realistic human motion interacting with objects. Prior work mainly focused on single-object scenarios, but real human behavior often involves both hands manipulating multiple objects simultaneously. Diffusion models have become a leading approach for motion generation due to their ability to model complex distributions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.27607">Dual-Stream Diffusion for World-Model Augmented Vision ... Dual-Stream Diffusion for World-Model Augmented Vision ... DiffuFuse: Diffusion-Driven Dual-Stream Fusion Framework for ... Dual-Stream Diffusion for World-Model Augmented Vision ... Dual-Stream Diffusion for World-Model Augmented Vision ... MMFace-DiT: Dual-Stream Diffusion Transformer DiffuFuse:Diffusion-Driven Dual-Stream Fusion Framework for ...</a></li>
<li><a href="https://arxiv.org/abs/2409.16855">[2409.16855] A Versatile and Differentiable Hand-Object ... Images A Versatile and Differentiable Hand-Object Interaction ... A Versatile and Differentiable Hand-Object Interaction ... Symbolic representation of objects relative poses for robotic ... GitHub Pages - HandyPriors The real-time hand and object recognition for virtual ... A Versatile and Differentiable Hand-Object Interaction ...</a></li>

</ul>
</details>

**Tags**: `#human-object interaction`, `#diffusion models`, `#motion generation`, `#bimanual manipulation`, `#4D synthesis`

---

<a id="item-30"></a>
## [VLMs Fail to Know When Not to Answer Spatial Questions](https://arxiv.org/abs/2605.30557) ⭐️ 8.0/10

Researchers propose SpatialUncertain, a framework that evaluates whether vision-language models (VLMs) can recognize when spatial questions are unanswerable due to occlusion or perspective ambiguity, rather than just producing correct answers. This work challenges the assumption in existing spatial reasoning benchmarks that observations are always sufficient, revealing that VLMs often overconfidently answer unanswerable questions, which is critical for safe real-world deployment. Under occlusion, average accuracy drops to around 30%, and under perspective ambiguity, it falls below 10%. Even when additional views are available, some models perform near random chance in identifying which view provides reliable evidence.

rss · arXiv - Computer Vision · Jun 1, 04:00

**Background**: Vision-language models (VLMs) combine visual and textual understanding to answer questions about images. Spatial reasoning benchmarks typically test whether models can answer questions about object locations or relationships, but they assume the image contains all necessary information. In reality, occlusion and perspective can make some questions unanswerable, and models should abstain rather than guess.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.30557">Seeing Isn’t Knowing: Do VLMs Know When Not to Answer Spatial ...</a></li>
<li><a href="https://arxiv.org/abs/2401.12168">SpatialVLM: Endowing Vision-Language Models with Spatial ...</a></li>

</ul>
</details>

**Tags**: `#vision-language models`, `#spatial reasoning`, `#benchmark`, `#AI safety`, `#computer vision`

---

<a id="item-31"></a>
## [Theoretical Analysis of Reward Learning from Best-of-N Data](https://arxiv.org/abs/2605.30619) ⭐️ 8.0/10

This paper provides a theoretical analysis of Bradley-Terry reward learning from Best-of-N preference data, deriving closed-form reward targets for independent-reference variants and showing that coupled variants like Best-vs-Random and Best-vs-Worst only approximate these targets as N grows. This work clarifies the theoretical underpinnings of a widely used but poorly understood data collection method in RLHF, offering design principles for choosing N and the base distribution that can improve reward model training efficiency and alignment quality. The analysis reveals a trade-off between margin and connectivity: larger N widens pairwise margins but reduces connectivity, which affects sample efficiency. The paper recommends using larger N when preference labels are the bottleneck and smaller N when generation is the bottleneck.

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**Background**: Best-of-N sampling is an inference-time alignment technique where N candidate responses are generated from a base model and the one with the highest reward score is selected. The Bradley-Terry model is a common approach for learning a reward function from pairwise preference data, but its behavior under Best-of-N sampling was not well understood theoretically.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2505.03156">[2505.03156] Soft Best-of-n Sampling for Model Alignment Best-of-N Sampling: AI Inference-Time Alignment | Inference ... Best-of-N sampling — Grokipedia Regularized Best-of-N Sampling with Minimum Bayes Risk ... Best of N sampling: Alternative ways to get better model ... Soft Best-of-$n$ Sampling for Model Alignment - IEEE Xplore GitHub - saschaschramm/best-of-n-sampling: Toy example for ...</a></li>
<li><a href="https://inferensys.com/glossary/agentic-cognitive-architectures/reinforcement-learning-from-ai-feedback/best-of-n-sampling">Best-of-N Sampling: AI Inference-Time Alignment | Inference ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning from human feedback`, `#reward learning`, `#preference data`, `#Bradley-Terry model`, `#Best-of-N sampling`

---

<a id="item-32"></a>
## [Last-Layer Linearization Matches Full-Network UQ Performance](https://arxiv.org/abs/2605.30741) ⭐️ 8.0/10

A new paper (arXiv:2605.30741) theoretically and empirically demonstrates that last-layer linearization for epistemic uncertainty quantification in deep neural networks achieves comparable performance to full-network linearization, while being far more computationally efficient. This finding challenges the common belief that full-network linearization is necessary for high-quality uncertainty quantification, which is critical for safe AI deployment in mission-critical applications. It enables practitioners to use cheaper last-layer approximations without sacrificing UQ quality. The theoretical analysis uses random matrix theory to compare the predictive posterior distributions of both linearization approaches, revealing no meaningful improvement from full linearization. Large-scale experiments across modern machine learning tasks confirm the equivalence.

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**Background**: Epistemic uncertainty quantification (UQ) measures what a model does not know due to limited data, which is crucial for safe AI. Bayesian Generalized Linear Models (GLMs) linearize neural networks to approximate the posterior distribution, but full-network linearization is computationally expensive. Last-layer linearization is a cheaper approximation often assumed to degrade UQ performance.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/epistemic-uncertainty-quantification">Epistemic Uncertainty Quantification</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bayesian_linear_regression">Bayesian linear regression - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#uncertainty quantification`, `#deep learning`, `#Bayesian neural networks`, `#random matrix theory`, `#epistemic uncertainty`

---

<a id="item-33"></a>
## [Weak Monotonicity Boosts Few-Shot Learning](https://arxiv.org/abs/2605.30997) ⭐️ 8.0/10

A new paper proposes using weak monotonicity across benchmarks to improve few-shot learning, providing theoretical guarantees and practical hedging algorithms. This work offers a principled way to leverage public benchmark evaluations for new tasks with few samples, potentially improving transfer learning and model selection in AI/ML research. The paper explores weak monotonicity in two paradigms: transfer learning and model selection aggregation, and shows that hedging on the frontier can adapt to the geometry of trade-offs.

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**Background**: Few-shot learning aims to learn new tasks from only a few labeled examples. Weak monotonicity is a property where if a model outperforms another on many benchmarks, it tends to also outperform on a new task. This paper leverages that property to prune model classes and improve learning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.machinebrief.com/news/cracking-the-code-task-relatedness-in-few-shot-learning-qju8">Cracking the Code: Task Relatedness in Few-Shot Learning</a></li>
<li><a href="https://arxiv.org/html/2305.00799">How to Address Monotonicity for Model Risk Management?</a></li>
<li><a href="https://arxiv.org/abs/2205.06743">[2205.06743] A Comprehensive Survey of Few-shot Learning ...</a></li>

</ul>
</details>

**Tags**: `#few-shot learning`, `#transfer learning`, `#model selection`, `#statistical learning theory`

---

<a id="item-34"></a>
## [Bayesian Filtering Unifies Sub-Quadratic Sequence Models](https://arxiv.org/abs/2605.31163) ⭐️ 8.0/10

A new paper introduces the design-model framework, which derives efficient recurrent sequence maps from Bayesian filtering assumptions, unifying linear attention, GLA, Mamba-2, and DeltaNet under a probabilistic memory model. This framework provides a principled design principle for efficient sequence models, potentially guiding the development of more robust and interpretable sub-quadratic architectures for long-context tasks. The Bayesian Layer propagates both mean and covariance, tracking uncertainty over stored associations and steering writes toward uncertain directions. Distilling Bayesian Layers into a pretrained 340M Gated DeltaNet improves RULER long-context retrieval at matched compute.

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**Background**: Many modern sequence models like linear attention and Mamba-2 achieve sub-quadratic complexity by using recurrent formulations, but they often lack a unified theoretical foundation. Bayesian filtering is a recursive estimation technique that updates beliefs about hidden states as new observations arrive. This paper bridges the gap by showing that several popular architectures are exact Bayesian filters under specific design models.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.22791">[2605.22791] Gated DeltaNet-2: Decoupling Erase and Write in ...</a></li>
<li><a href="https://sustcsonglin.github.io/blog/2024/deltanet-3/">DeltaNet Explained (Part III) | Songlin Yang</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#recurrent neural networks`, `#Bayesian filtering`, `#sequence modeling`, `#attention`

---

<a id="item-35"></a>
## [Anytime-Valid Inference Fixes Split Selection in Online Decision Trees](https://arxiv.org/abs/2605.31239) ⭐️ 8.0/10

This paper introduces an anytime-valid inference method to correct split selection in online decision trees, providing valid statistical guarantees and finite commitment time under arbitrary data streams. This addresses a fundamental flaw in widely-used Hoeffding Trees, where fixed-sample concentration bounds invalidate guarantees due to data-dependent stopping. The new method improves performance and produces smaller trees, benefiting data stream learning applications. The method provides anytime-valid control of false splits under non-stationary streams, finite commitment time under predictive advantage, and strictly decreasing risk under stationary i.i.d. data. Empirical evaluation on non-stationary streams shows improved performance with substantially smaller trees.

rss · arXiv - Data Science & Statistics · Jun 1, 04:00

**Background**: Online decision trees, such as Hoeffding Trees, grow incrementally by testing splits using concentration inequalities. However, these tests rely on fixed-sample bounds while decisions are made with data-dependent stopping, invalidating statistical guarantees. Anytime-valid inference provides valid sequential testing that controls error rates at all stopping times.

<details><summary>References</summary>
<ul>
<li><a href="https://www.emergentmind.com/topics/any-time-inference">Any - Time Inference</a></li>
<li><a href="https://medium.com/@techynilesh/the-hoeffding-tree-classifier-for-real-time-data-mining-09b117486a95">The Hoeffding Tree Classifier for Real-Time Data Mining | Medium</a></li>
<li><a href="https://www.activeloop.ai/resources/glossary/hoeffding-trees/">What is Hoeffding Trees ? | Activeloop Glossary</a></li>

</ul>
</details>

**Tags**: `#online learning`, `#decision trees`, `#anytime-valid inference`, `#data streams`, `#statistical guarantees`

---