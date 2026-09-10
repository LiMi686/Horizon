---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 105 items, 8 important content pieces were selected

---

1. [Microsoft Elevates Rust to Tier-1 Language Status](#item-1) ⭐️ 9.0/10
2. [AI-Assisted WeWorm Zero-Click Worm Spreads via WeChat Calls](#item-2) ⭐️ 9.0/10
3. [Shopify abandons React Native for native Swift and Kotlin apps](#item-3) ⭐️ 8.0/10
4. [Researchers question whether OpenAI can be trusted with unpublished math](#item-4) ⭐️ 8.0/10
5. [Sony Faces Lawsuit Over Digital Game Ownership Claims](#item-5) ⭐️ 8.0/10
6. [Option-Critic's Termination Rule Is Useless and Policies Necrose, Paper Finds](#item-6) ⭐️ 8.0/10
7. [Lensless Gaze Sensing Leaks Identity at 96.7% Accuracy, Study Finds](#item-7) ⭐️ 8.0/10
8. [AI's Power Demand Exposes Fragile Grid Architecture](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft Elevates Rust to Tier-1 Language Status](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Microsoft has officially designated Rust as a tier-1 language, placing it alongside C++, C#, and TypeScript as one of the best-supported languages for internal development. The announcement was made via a guest post on the Rust Foundation website, highlighting Rust's growing role in Microsoft's core projects. This endorsement signals Rust's maturity and broad adoption in systems programming, potentially influencing other large organizations to follow suit. It also underscores the industry's shift toward memory-safe languages to reduce security vulnerabilities. Microsoft's goal includes converting 1 billion lines of code to Rust by 2030 using automated tooling, aiming for '1 engineer, 1 month, 1 million lines of code.' Additionally, there are rumors of MSVC integration with Rust, and DARPA is funding C-to-Rust conversion efforts.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a systems programming language focused on memory safety and performance, developed by Mozilla and now maintained by the Rust Foundation. Tier-1 language status at Microsoft means it receives first-class tooling, documentation, and support, similar to established languages like C++ and C#. Memory safety issues, such as buffer overflows, are a major source of security vulnerabilities in software written in C and C++.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://news.ycombinator.com/item?id=49643546">Rust Is Tier - 1 Language at Microsoft | Hacker News</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion (579 points, 317 comments) reflects strong interest, with users noting Microsoft's ambitious 1 billion lines of code conversion goal and DARPA's C-to-Rust efforts. Some commenters highlight Rust's maturity compared to newer languages like Zig and Odin, while others discuss the strategic benefits of memory safety for reducing CVEs. A notable point is the replacement of LLVM with MSVC's backend, indicating deeper integration.

**Tags**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Language Adoption`

---

<a id="item-2"></a>
## [AI-Assisted WeWorm Zero-Click Worm Spreads via WeChat Calls](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, described as the first zero-click worm that spreads through WeChat calls on both iOS and Android, hijacking accounts without the victim answering or interacting with their phone. The team says it used AI to find the bug and write the first remote code execution (RCE) exploit in about two days, then built the worm in roughly one more week. This demonstrates a paradigm shift in exploit development: a worm that once required a large team and months of work was reportedly built by a small team with AI assistance in about ten days, putting over a billion WeChat accounts potentially at risk. It raises urgent questions for mobile security, vulnerability disclosure practices, and AI safety, since AI can now dramatically accelerate both finding and weaponizing critical bugs. According to coverage, the exploit targets a memory-corruption flaw in WeChat's VoIP call stack, compromising a target's account in seconds even if the call is missed or answered with silence, and the bug was privately reported to Tencent. The worm is presented as a demo/proof of concept rather than an in-the-wild attack, and the researchers emphasize that human judgment guided what to target and how to test safely.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit requires no action from the victim, making it far more dangerous than attacks that need a click or download. Remote code execution (RCE) means an attacker can run their own code on a victim's device over a network, typically by exploiting a memory-corruption bug such as a buffer overflow. A worm is malware that self-propagates from device to device; combining it with zero-click RCE and a widely used app like WeChat (with over a billion users) creates the potential for rapid, large-scale account hijacking.

<details><summary>References</summary>
<ul>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arbitrary_code_execution">Arbitrary code execution - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#security`, `#ai`, `#mobile`, `#exploit`, `#worm`

---

<a id="item-3"></a>
## [Shopify abandons React Native for native Swift and Kotlin apps](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify announced it is moving its mobile apps away from React Native and back to fully native development using Swift for iOS and Kotlin for Android. The engineering blog post details the company's decision to abandon the cross-platform framework it had previously invested in heavily. Shopify's reversal is a significant industry signal because the company was a high-profile React Native adopter, and its move could influence other large-scale mobile teams evaluating cross-platform versus native strategies. The decision also fuels the broader debate about whether AI-assisted coding makes maintaining separate native codebases more feasible. The migration involves rewriting the app in Swift and Kotlin, and community members report using AI coding agents to port React Native code to native platforms in a matter of days. However, concerns remain about whether teams have the native expertise to maintain quality, since AI-generated Swift or Kotlin code can hide subtle bugs from developers unfamiliar with those languages.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source framework from Meta that lets developers build iOS and Android apps using JavaScript and React, sharing much of the code across platforms. Swift is Apple's compiled language for iOS and macOS, while Kotlin is JetBrains' language that Google endorses as the preferred choice for Android. Shopify had previously been a prominent React Native user, so its return to native development marks a notable shift in mobile engineering strategy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>

</ul>
</details>

**Discussion**: Hacker News commenters are deeply divided: some argue that complexity must be tamed rather than multiplied and that AI struggles with complexity just as humans do, while others share positive experiences porting React Native to native using AI agents in days. A recurring concern is that developers who don't know Swift or Kotlin cannot spot AI-generated garbage code, and some recommend Kotlin Multiplatform as a middle ground for sharing business logic while keeping native UIs.

**Tags**: `#react-native`, `#mobile-development`, `#swift`, `#kotlin`, `#ai-assisted-development`

---

<a id="item-4"></a>
## [Researchers question whether OpenAI can be trusted with unpublished math](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

Following OpenAI's announcement that it solved a longstanding open math problem using a 10,000-agent swarm, NYU mathematician Tristan Buckmaster publicly accused the company of scooping his work, alleging that OpenAI learned of his progress through collaborative Codex chats and then rushed to publish a proof that excluded his collaborator from authorship. OpenAI researcher Sébastien Bubeck denied the allegations, and OpenAI subsequently published its own proof manuscript and formal verification code, but the full recordings of key phone calls have not been released. This dispute raises fundamental questions about research integrity and attribution as AI labs increasingly collaborate with academics, potentially chilling researchers from sharing unpublished ideas with commercial models. It could reshape norms around how AI companies credit external contributions and whether confidential research chats are used in model training. The controversy centers on whether OpenAI's model benefited from Buckmaster's private Codex data or independently discovered the solution through reinforcement learning on verifiable math with massive compute. OpenAI has published its proof manuscript and formal verification code, but has not released the complete recordings of the key phone calls, leaving the provenance of the ideas contested.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: OpenAI has given many researchers free access to its models, including Codex, a coding and work-focused AI harness, and internal models have reportedly been solving open math problems at a surprisingly fast rate. Open problems are unsolved mathematical questions that researchers typically work on for years, and feeding fresh ideas into AI chats may inadvertently contribute to model training. Formal verification is a process where proofs are checked by computer, which is increasingly used to validate AI-generated mathematical results.

<details><summary>References</summary>
<ul>
<li><a href="https://venturebeat.com/technology/openai-solves-longstanding-math-problem-with-10-000-agent-swarm-but-cant-rule-out-benefitting-from-a-researchers-private-codex-data">OpenAI solves longstanding math problem with 10,000-agent swarm — but can't rule out benefitting from a researcher's private Codex data | VentureBeat</a></li>
<li><a href="https://finance.biggo.com/news/b05bc0db-1896-4282-9106-fb3da78adc03">AI cracks a Millennium Prize-adjacent problem, igniting a credit war: NYU mathematician accuses OpenAI of scooping his work — BigGo Finance</a></li>
<li><a href="https://www.stork.ai/blog/openais-stolen-math-proof">OpenAI Navier-Stokes Controversy: AI Authorship & Ethics | Stork.AI</a></li>

</ul>
</details>

**Discussion**: Commenters drew an analogy to a human collaborator, arguing that if OpenAI were a person, publishing work based on collaborative chats without attribution would be highly unethical. Some suggested the only ethical path was to offer free credits and tooling support rather than scooping the researchers, while others noted that both things can be true: models may remember chat data while also independently discovering superhuman techniques through RL. A few expressed skepticism about the researchers' judgment or indifference to the controversy.

**Tags**: `#OpenAI`, `#research ethics`, `#AI collaboration`, `#attribution`, `#mathematics`

---

<a id="item-5"></a>
## [Sony Faces Lawsuit Over Digital Game Ownership Claims](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 8.0/10

A class-action lawsuit against Sony over its PlayStation Store 'Buy' buttons has drawn attention after Sony argued in its defense that players cannot truly own digital games, only licenses. A wiki page compiling references to Sony's contradictory statements on ownership is being discussed on Hacker News, with 347 points and 115 comments. This case could set a precedent for how digital goods are marketed and sold, affecting not just gamers but all consumers of digital content like ebooks, movies, and software. It highlights the growing tension between consumer expectations of ownership and the licensing model that dominates digital distribution. Sony's defense includes a binding arbitration clause and class action waiver in Section 14 of its Terms of Service, requiring users to opt out within 30 days. The lawsuit specifically challenges the use of 'Buy' buttons on the PlayStation Store for digital games that are actually revocable licenses.

hackernews · haunter · Sep 10, 12:18 · [Discussion](https://news.ycombinator.com/item?id=49642531)

**Background**: Digital games are typically sold as licenses rather than physical products, meaning users do not own the game itself but a right to access it under certain conditions. This has led to consumer backlash when content is removed or access is revoked, as seen with Sony's 2024 merger of Crunchyroll and FUNimation where users lost access to purchased titles. The 'Stop Killing Games' movement and increased regulatory scrutiny are part of a broader push to redefine digital ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://cybernews.com/tech/sony-digital-game-ownership-lawsuit/">Sony Digital Game Ownership Fight: You Can’t Own Games, It ...</a></li>
<li><a href="https://openclassactions.com/lawsuits/consumer-protection/sony-playstation-digital-game-license-class-action-lawsuit.php">Do You Own Digital Games You Buy? Sony Lawsuit Explained</a></li>
<li><a href="https://www.ign.com/articles/playstation-claims-digital-games-are-not-really-owned-by-players-in-response-to-class-action-lawsuit">PlayStation's Response to Class-Action Lawsuit Over Digital ...</a></li>

</ul>
</details>

**Discussion**: Commenters criticized binding arbitration clauses as unfair and debated the analogy of buying a book versus a digital game, noting that physical copies are distinct while digital licenses are not. Some pointed out that Sony's defense could backfire by implying that if a user doesn't own a copy, Sony might not have the right to sell it in the first place, and others expressed ambivalence toward Sony due to past incidents like the rootkit scandal.

**Tags**: `#digital-ownership`, `#consumer-rights`, `#legal`, `#gaming`, `#sony`

---

<a id="item-6"></a>
## [Option-Critic's Termination Rule Is Useless and Policies Necrose, Paper Finds](https://arxiv.org/abs/2609.05508) ⭐️ 8.0/10

A new arXiv paper (2609.05508) theoretically and experimentally shows that option-critic's learned termination rule contributes nothing to performance, and that intra-option policies suffer from a newly named failure mode called 'policy necrosis.' The authors report that forcing termination at every step leaves the option-count performance curve intact, and that roughly three fifths of states inside a typical option are necrotic. Option-critic is a foundational method in hierarchical reinforcement learning, and its headline claim that adding options improves performance has shaped how researchers design option-discovery methods. If the termination rule is redundant and intra-option policies fail to explore, much of the field's assumed benefit from options may need to be re-evaluated. When the termination test and the policy-over-options read the same values, the test fires at every step, making the learned rule equivalent to always terminating; when the policy explores but the test does not, the rule can block exploration, with instances showing Ω(T) regret versus O(log T) for always terminating. The paper also gives a state-level test for policy necrosis and shows that restoring exploration repairs necrotic states, after which a single option can solve the task.

rss · arXiv - Machine Learning · Sep 10, 04:00

**Background**: The options framework, introduced by Sutton, Precup and Singh in 1999, models temporally extended actions as sub-policies with their own termination conditions, enabling temporal abstraction in reinforcement learning. The option-critic architecture (Bacon, Harb and Precup, 2016) was the first to learn intra-option policies, termination functions and the policy over options end-to-end via policy gradient theorems, without extra rewards or subgoals. Hierarchical RL methods like these aim to scale learning to long-horizon tasks by decomposing them into reusable skills.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/1609.05140">[1609.05140] The Option-Critic Architecture</a></li>
<li><a href="https://campusai.github.io/papers/the-option-critic-architecture">The Option Critic Architecture</a></li>
<li><a href="https://rljclub.github.io/posts/hierarchical-reinforcement-learning/">Hierarchical Reinforcement Learning: From Options to Goal ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#hierarchical RL`, `#option-critic`, `#policy necrosis`, `#exploration`

---

<a id="item-7"></a>
## [Lensless Gaze Sensing Leaks Identity at 96.7% Accuracy, Study Finds](https://arxiv.org/abs/2609.09188) ⭐️ 8.0/10

A new arXiv paper (2609.09188) audits a simulated lensless gaze pipeline and finds that coded, visually unintelligible measurements still allow identity recovery with 96.7% top-1 accuracy under a 36-subject closed-set protocol, nearly matching the 97.7% achieved from original eye crops. The authors show that compression and dimensionality reduction offer little protection, with 8-D PCA and a matched 8-D bottleneck retaining 93.2% and 91.8% recovery, while a released 128-way gaze token lowers single-frame recovery to 38.1%. This work challenges the common assumption that lensless near-eye sensing is inherently privacy-preserving because its raw measurements look like noise, with implications for privacy-by-design claims in biometric security, gaze tracking, and edge sensing systems. It argues that privacy must be audited at every disclosure boundary—sensing, storage, computation, and output—rather than inferred from visual appearance. The audit uses a fixed, known point spread function (PSF) and matched linear and MLP probes, so the reported accuracies are empirical attack success rates that do not upper-bound stronger adversaries, and privacy from an unknown or varying optical key is out of scope. Even after ordinary least squares residualization against a six-dimensional crop geometry and intensity summary, lensless recovery remains at 95.1%, and under a source-frame-disjoint tiled protocol token summaries reach 39.9% at T=25.

rss · arXiv - Computer Vision · Sep 10, 04:00

**Background**: Lensless near-eye sensing replaces the lens with a coded mask, producing measurements that look like unintelligible patterns but can be computationally reconstructed; the point spread function (PSF) describes how a point of light is spread by the optical system. Because these measurements are hard for humans to interpret, they are often marketed as privacy-friendly, but this paper treats identity privacy as a systems property of disclosure surfaces and tests it with learned adversaries such as masked autoencoder (MAE) embeddings.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.09188">[2609.09188] Lensless Gaze Is Not Private by Default ...</a></li>
<li><a href="https://github.com/xoxo121/Lensless-Gaze-Is-Not-Private-by-Default">GitHub - xoxo121/Lensless-Gaze-Is-Not-Private-by-Default</a></li>
<li><a href="https://en.wikipedia.org/wiki/Point_spread_function">Point spread function - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#lensless sensing`, `#gaze tracking`, `#biometric security`, `#adversarial machine learning`

---

<a id="item-8"></a>
## [AI's Power Demand Exposes Fragile Grid Architecture](https://www.technologyreview.com/2026/09/10/1141649/powering-ai-is-an-architecture-problem/) ⭐️ 8.0/10

On July 22, 2026, a transmission line fault in Ashburn, Virginia—the world's largest data center cluster—knocked more than 3 gigawatts of load off the grid in seconds. This follows a 2024 incident where a single failed surge arrester dropped roughly 60 Virginia facilities and 1,500 megawatts at once, and MIT Technology Review argues these events reveal that powering AI is fundamentally an architecture problem. As AI training and inference drive unprecedented power density in a handful of geographic hubs, the grid's inability to absorb sudden large load losses threatens both data center uptime and broader grid stability. This affects AI/ML companies, cloud providers, utilities, and millions of electricity customers who share the same infrastructure. The July 2026 fault removed over 3 gigawatts in seconds, while the earlier surge arrester failure dropped about 1,500 megawatts across roughly 60 facilities, illustrating how a single component failure can cascade into massive simultaneous load loss. These incidents highlight that current grid architecture lacks sufficient redundancy, fast fault isolation, and load-shedding coordination for concentrated AI data center loads.

rss · MIT Technology Review · Sep 10, 11:00

**Background**: Ashburn, Virginia, about 30 miles northwest of Washington, D.C., is the world's largest data center and internet interconnection hub, hosting over 140 facilities from multiple operators. A transmission line fault is a disruption such as a short circuit or insulation failure that can cause outages, and a surge arrester is a protective device that diverts voltage spikes; when it fails, it can trigger cascading outages. Because AI workloads concentrate enormous power demand in such hubs, the loss of a single line or protective device can suddenly remove gigawatts of load, stressing grid frequency and stability.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ashburn,_Virginia">Ashburn , Virginia - Wikipedia</a></li>
<li><a href="https://www.inmr.com/principal-failure-modes-surge-arresters/">Failure Modes for Surge Arresters -</a></li>
<li><a href="https://ideas.repec.org/a/eee/energy/v355y2026ics0360544226012739.html">Improve MicroGrid connected systems with hybrid Wolf-Bird Optimizer...</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#power grid`, `#energy systems`, `#architecture`

---