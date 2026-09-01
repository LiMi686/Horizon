---
layout: default
title: "Horizon Summary: 2026-09-01 (EN)"
date: 2026-09-01
lang: en
---

> From 112 items, 23 important content pieces were selected

---

1. [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 with Improved Writing and Science](#item-1) ⭐️ 9.0/10
2. [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](#item-2) ⭐️ 8.0/10
3. [Apple presents forensic evidence in OpenAI trade secret lawsuit](#item-3) ⭐️ 8.0/10
4. [Python 3.15.0 Release Candidate 2 Announced](#item-4) ⭐️ 8.0/10
5. [Heretic: Fully Automatic Censorship Removal for Language Models](#item-5) ⭐️ 8.0/10
6. [Frontier LLMs Share Blind Spots in Oncology Decision-Making](#item-6) ⭐️ 8.0/10
7. [Agentic AI vs. Survey Attention Checks: A New Data Quality Threat](#item-7) ⭐️ 8.0/10
8. [CDPR: Counterfactual Advantage Credit Assignment for Cost-Aware Diagnosis](#item-8) ⭐️ 8.0/10
9. [SHAPE Framework Decodes LLM Math Reasoning via Heuristics](#item-9) ⭐️ 8.0/10
10. [Curvature Cryptanalysis Extracts Hidden Transformer FFN Directions](#item-10) ⭐️ 8.0/10
11. [ESNN: Equivariant Sheaf Neural Networks for Geometric Transport](#item-11) ⭐️ 8.0/10
12. [Halt Vector: Causal Steering to Cut LLM Overthinking](#item-12) ⭐️ 8.0/10
13. [Conservative Hybrid Graph Networks Achieve Zero-Shot Transfer in Process Systems](#item-13) ⭐️ 8.0/10
14. [General Coded Computing: A Learning-Theoretic Framework for Stragglers](#item-14) ⭐️ 8.0/10
15. [SemKV: Quality-Cliff-Aware Mixed-Precision KV Cache Quantization](#item-15) ⭐️ 8.0/10
16. [Parametric Multimodal User Memory: Storing What Captions Cannot Carry](#item-16) ⭐️ 8.0/10
17. [LLM Peer Review Audit Reveals Inflated Scores and Bias](#item-17) ⭐️ 8.0/10
18. [MIRAGE-CAD: Multimodal Generation of Executable CAD Programs](#item-18) ⭐️ 8.0/10
19. [Interaction Growth Complexity Characterizes Discrete Diffusion Sampling](#item-19) ⭐️ 8.0/10
20. [Jigsaw-CRL: Recovering Global Latent Causal Order from Fragmented Multi-Client Interventions](#item-20) ⭐️ 8.0/10
21. [Sharp RIP Threshold for Global Minima of Rank-Restricted Matrix LASSO](#item-21) ⭐️ 8.0/10
22. [Deep Latent Variable Framework Jointly Models Missingness, Error, Heterogeneity](#item-22) ⭐️ 8.0/10
23. [Token Prediction Organizes Representations: A Statistical Framework](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic Releases Claude Fable 5.1 and Mythos 5.1 with Improved Writing and Science](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic has released Claude Fable 5.1 and Claude Mythos 5.1, extending the previous Fable 5 model with improved writing style, stronger science performance, and a reduced cache read price from $1/M to $0.25/M. The models also introduce several additive features including per-message effort control and turn-scoped system messages. This release significantly lowers the cost of using Claude for applications that rely on prompt caching, making it more competitive against other LLM providers. The improvements in writing style and science capabilities could attract more users in creative and research fields, potentially shifting market dynamics. The cache read price reduction from $1/M to $0.25/M makes Fable 5.1's cache reads half the cost of Opus's ($0.5/M). Three breaking changes address security issues related to chain-of-thought disclosure, including preventing forced tool use from exposing raw reasoning and restricting access to thinking blocks.

hackernews · denysvitali · Sep 1, 17:53 · [Discussion](https://news.ycombinator.com/item?id=49525378)

**Background**: Claude Fable 5.1 is a large language model from Anthropic, designed for general-purpose tasks with a focus on writing quality and scientific reasoning. Prompt caching is a technique that stores previously computed tokens to reduce latency and cost for repeated API calls. The new models also include Claude Mythos 5.1, a specialized variant for cybersecurity and biology research, available by invitation only.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/overview">Claude Fable 5.1 - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \ Anthropic \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**Discussion**: Community members praised the improved writing style, with an Anthropic employee noting it sounds more natural and responds better to style instructions. Some users discussed the price reduction, attributing it to lower cache read pricing, and debated whether the model shows real improvements beyond the science benchmark. Others highlighted security patches related to chain-of-thought disclosure.

**Tags**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Machine Learning`

---

<a id="item-2"></a>
## [Small Transformer Trained in 1.5 Hours Beats Many LLMs on ARC](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

A small transformer trained from scratch in just 1.5 hours achieves competitive results on the ARC benchmark, outperforming many large language models. The author, evilmathkid, shared the result on Hacker News, sparking discussion about sample efficiency and training methodology. This challenges the prevailing scaling paradigm that massive models and enormous compute are necessary for complex reasoning tasks. It suggests that efficient architectures and training strategies can achieve strong performance, potentially democratizing AI research and reducing environmental costs. The model is a small autoregressive transformer, not an LLM, and was trained on the ARC benchmark's training set. The author notes that improvements came from modern architecture choices (e.g., SwiGLU, RMSNorm), better data shuffling, and scaling up to 8 layers, but emphasizes that training on eval puzzles is not 'training on test' since labels were not used.

hackernews · porridgeraisin · Sep 1, 09:52 · [Discussion](https://news.ycombinator.com/item?id=49519939)

**Background**: The ARC (Abstraction and Reasoning Corpus) benchmark is designed to measure AI's ability to acquire skills and reason abstractly, with tasks that are easy for humans but hard for AI. Traditionally, only large language models or their fine-tunes have scaled this benchmark, often with enormous training costs. This work demonstrates that a small transformer can achieve competitive results with minimal compute, highlighting the potential of sample-efficient approaches.

<details><summary>References</summary>
<ul>
<li><a href="https://arcprize.org/">ARC Prize</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://lab42.global/arc/">About ARC – Lab42</a></li>

</ul>
</details>

**Discussion**: The author engaged actively, clarifying that the model is not an LLM and defending the training methodology against accusations of 'training on test'. Commenters like usernametaken29 praised the focus on sample efficiency but cautioned against 'squeezing the lemon' as a last resort. Others congratulated the author, noting the achievement's significance and even mentioning the author's personal story of saving his own life.

**Tags**: `#transformer`, `#ARC`, `#efficiency`, `#deep learning`, `#research`

---

<a id="item-3"></a>
## [Apple presents forensic evidence in OpenAI trade secret lawsuit](https://9to5mac.com/2026/08/31/apple-openai-forensic-macbook-evidence/) ⭐️ 8.0/10

Apple has presented forensic evidence in its lawsuit against OpenAI, alleging that a former employee, Mr. Liu, used stolen Apple trade secrets, including a confidential circuit schematic, in his work at OpenAI. The evidence includes his use of the schematic in LTspice simulations and attempts to destroy evidence upon learning of Apple's investigation. This case could set a precedent for how trade secret law applies to AI training and usage, as Apple argues that feeding trade secrets into AI models creates irreversible and propagating uses. The outcome may affect how companies protect proprietary data in the age of AI and how AI developers handle sensitive information. Apple also seeks access to a Mac mini that Liu used, which synced via iCloud to the MacBook he took from Apple. The lawsuit involves io, a company founded by former Apple employees and acquired by OpenAI, which is accused of using Apple's metal-finishing techniques.

hackernews · colinprince · Sep 1, 20:19 · [Discussion](https://news.ycombinator.com/item?id=49527573)

**Background**: Trade secret litigation often relies on digital forensics to uncover evidence of misappropriation, as electronic data leaves traces that can be analyzed. In this case, Apple's forensic evidence includes iCloud sync data and simulation files, highlighting how digital trails can link personal and corporate devices. The legal argument that AI models 'learn' from trade secrets and propagate them is novel and could have broad implications for AI development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cy8w379e091o">Apple sues OpenAI, its employees claiming theft of trade secrets</a></li>
<li><a href="https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/">The wildest allegations in Apple’s trade secrets lawsuit against OpenAI | TechCrunch</a></li>
<li><a href="https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html">Apple sues OpenAI alleging trade secret theft, says scheme was 'at every level'</a></li>

</ul>
</details>

**Discussion**: Commenters discuss the legal and privacy implications, with some noting the high-impact argument about AI learning from trade secrets. Others express curiosity about the privacy implications of iCloud syncing personal data on company devices, and one commenter draws a parallel to the Coca-Cola recipe case, suggesting that companies should act ethically when receiving stolen secrets.

**Tags**: `#Apple`, `#OpenAI`, `#trade secrets`, `#AI`, `#legal`

---

<a id="item-4"></a>
## [Python 3.15.0 Release Candidate 2 Announced](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

Python 3.15.0 release candidate 2 (RC2) has been announced by release manager Hugo van Kemenade, marking the final release candidate before the stable release scheduled for October. Third-party maintainers are strongly encouraged to prepare their projects and publish Python 3.15 wheels on PyPI to ensure compatibility. This release candidate is a critical milestone for the Python ecosystem, as it signals the final phase before a major version release. It gives third-party maintainers a clear call to action to test and build wheels, ensuring a smooth transition for the entire community when Python 3.15 is officially released. During the release candidate phase, only reviewed bug fixes are allowed between RC2 and the final release. Binary wheels built against Python 3.15.0 release candidates will work with future versions of Python 3.15, and the RC is not yet available on GitHub Actions, but can be tested using the allow-prereleases and check-latest flags in actions/setup-python.

rss · Simon Willison · Sep 1, 14:59

**Background**: Python uses a release candidate (RC) phase to stabilize the codebase before the final release, allowing only bug fixes. Wheels are Python's standard binary distribution format, which install without compilation, and ensuring they are built against the RC ensures compatibility with the final release. The release manager's announcement emphasizes the importance of testing during this period to avoid shipping bugs, as seen in a past incident with Python 3.10.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.python.org/2026/09/python-3150-rc2/">Python 3 . 15 .0 candidate 2 is here! | Python Insider</a></li>
<li><a href="https://packaging.python.org/specifications/binary-distribution-format/">Binary distribution format - Python Packaging User Guide</a></li>
<li><a href="https://blog.trailofbits.com/2022/11/15/python-wheels-abi-abi3audit/">ABI compatibility in Python: How hard could it be? - The Trail of Bits Blog</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Release`, `#Software Engineering`, `#Ecosystem`

---

<a id="item-5"></a>
## [Heretic: Fully Automatic Censorship Removal for Language Models](https://github.com/p-e-w/heretic) ⭐️ 8.0/10

Heretic, a new open-source tool by p-e-w, enables fully automatic removal of censorship (safety alignment) from transformer-based language models without expensive post-training. It combines advanced directional ablation (abliteration) with a TPE-based parameter optimizer powered by Optuna, achieving results comparable to manual abliteration by human experts. This project addresses a controversial yet technically significant topic: automatic censorship removal in LLMs. It could democratize the creation of 'uncensored' models, raising important ethical and safety questions about model alignment and potential misuse, while also advancing research in model interpretability and control. Heretic supports most dense models, including multimodal and MoE architectures, and even hybrid models like Qwen3.5, but not pure state-space models. It works by co-minimizing the number of refusals and KL divergence from the original model, preserving intelligence while removing refusals. The tool is designed to be usable by anyone familiar with command-line programs, without deep understanding of transformer internals.

rss · GitHub Trending - Daily (All) · Sep 1, 23:43

**Background**: Language models are often 'aligned' to refuse harmful prompts, a process known as safety alignment. Abliteration is a technique that removes this alignment by modifying model weights, typically done manually by experts. Heretic automates this process using optimization algorithms, making it accessible to a broader audience. The project has gained attention on GitHub Trending and has an official website and community channels.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/p-e-w/heretic">GitHub - p-e-w/heretic: Fully automatic censorship removal for language models · GitHub</a></li>
<li><a href="https://explainx.ai/blog/heretic-llm-abliteration-guide-2026">Heretic: Complete Guide to Automatic LLM Censorship Removal | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-05-29-heretic-new-github-project-aims-for-automated-censorship-removal-in-language-models">Heretic: Automated Censorship Removal for Language Models | AIToolly</a></li>

</ul>
</details>

**Tags**: `#AI`, `#language models`, `#censorship`, `#open source`, `#ethics`

---

<a id="item-6"></a>
## [Frontier LLMs Share Blind Spots in Oncology Decision-Making](https://arxiv.org/abs/2608.28592) ⭐️ 8.0/10

A new study introduces the Oncology Decision Boundary Benchmark (ODBB), comprising 2,005 oncology decision points from NCCN guidelines and colorectal cancer cases, and evaluates nine frontier LLMs released between June 2025 and April 2026. The results show that 42.1% of pooled decisions were answered correctly by none of the models, revealing a collective capability boundary. This finding challenges the assumption that simply combining more models or adding training data can overcome LLM limitations in clinical decision-making. It highlights a fundamental blind spot in clinical meta-judgment that may require architectural changes, impacting the deployment of LLMs in healthcare. The study used a fully deterministic scorer with zero LLM inference, classifying outputs into 14 failure types, validated by two oncologists (Cohen's weighted kappa = 0.939 and 0.790). Notably, two models tuned for decisiveness (GPT-5.5, Gemini 3.1 Pro Preview) made unsafe commitments three to five times more often than the seven cautious models without scoring higher.

rss · arXiv - AI · Sep 1, 04:00

**Background**: Large language models (LLMs) have achieved high scores on medical knowledge exams, but real-world oncology involves sequential decision-making under uncertainty, not just factual recall. Existing benchmarks often measure knowledge recall, leaving a gap in evaluating decision-path capabilities. The ODBB benchmark addresses this by focusing on guideline-conformant decision points, and the study suggests that progress requires architectures that detect when a model reaches its competence boundary and route decisions to clinicians.

<details><summary>References</summary>
<ul>
<li><a href="https://smartchunks.com/frontier-ai-oncology-decision-benchmark-shared-blind-spot/">Frontier AI Models Share The Same Blind Spot In Cancer Decisions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.nccn.org/guidelines/nccn-guidelines">NCCN Guidelines</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#medical AI`, `#oncology`, `#benchmark`, `#decision-making`

---

<a id="item-7"></a>
## [Agentic AI vs. Survey Attention Checks: A New Data Quality Threat](https://arxiv.org/abs/2608.28597) ⭐️ 8.0/10

A new arXiv paper demonstrates that agentic AI systems can exploit structural vulnerabilities in online surveys, such as exposed DOM metadata and predictable option encoding, to pass attention checks without genuine comprehension. The study evaluates a single-agent architecture with multimodal input and tool-based web interaction on a controlled survey sandbox. This research highlights a growing threat to the integrity of online survey data, which underpins research in social sciences, marketing, and public policy. As agentic AI becomes more capable, traditional attention checks may no longer suffice, necessitating new defensive strategies to protect data quality. The paper analyzes both attack and defense perspectives: it shows how agents can resolve attention checks through structured parsing alone, and proposes DOM metadata obfuscation as a mitigation. It evaluates multiple open-source language and multimodal models to assess capability and orchestration effectiveness.

rss · arXiv - AI · Sep 1, 04:00

**Background**: Online surveys often use attention checks to filter out respondents who are not paying attention, ensuring data quality. Agentic AI refers to autonomous systems powered by large language models (LLMs) that can plan and execute tasks using tools. DOM metadata vulnerabilities involve exposed HTML attributes that can leak semantic information, which agents can exploit to infer correct answers.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components">Choose your agentic AI architecture components | Cloud Architecture Center | Google Cloud Documentation</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-architecture">What Is Agentic Architecture? | IBM</a></li>
<li><a href="https://portswigger.net/web-security/dom-based">DOM-based vulnerabilities | Web Security Academy</a></li>

</ul>
</details>

**Tags**: `#agentic AI`, `#data quality`, `#online surveys`, `#LLM`, `#security`

---

<a id="item-8"></a>
## [CDPR: Counterfactual Advantage Credit Assignment for Cost-Aware Diagnosis](https://arxiv.org/abs/2608.28599) ⭐️ 8.0/10

The paper introduces CDPR (Counterfactual Diagnostic Process Reward), a novel reinforcement learning method for cost-aware sequential medical diagnosis that requires no expert labels or learned critic. It integrates CDPR into GRPO and demonstrates improved diagnostic accuracy while reducing the number and cost of examinations on MIMIC-IV, ClinicalBench, and a private hospital dataset. This work addresses a critical gap in medical diagnosis, where most models ignore the trade-off between test value and cost. By enabling efficient credit assignment in long trajectories without expert labels, CDPR could make AI-driven diagnosis more practical and cost-effective in real clinical settings, potentially reducing unnecessary medical expenses. CDPR identifies hesitant states using the uncertainty of the policy's action distribution, then scores actions by their advantage over alternatives via short rollouts under a utility balancing correctness, test count, cost, and infeasible requests. A rollout cache reuses within-batch trajectories to keep computational costs low, and the method is integrated into GRPO for training.

rss · arXiv - AI · Sep 1, 04:00

**Background**: Clinical diagnosis is inherently sequential and cost-aware, but most medical language models treat it as one-pass classification. Reinforcement learning offers a way to model this sequential decision process, but credit assignment is challenging because the only reliable reward comes at the end of a long trajectory. Counterfactual methods estimate the advantage of chosen actions by comparing them with alternative actions, which can reduce variance in policy gradient estimates.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28599">[2608.28599] CDPR : Counterfactual Advantage-based Credit...</a></li>
<li><a href="https://arxiv.org/html/2605.16302v1">Reducing Credit Assignment Variance via Counterfactual Reasoning Paths</a></li>
<li><a href="http://proceedings.mlr.press/v139/mesnard21a/mesnard21a.pdf">Counterfactual Credit Assignment in Model-Free Reinforcement Learning</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#medical diagnosis`, `#credit assignment`, `#cost-aware decision making`, `#arXiv`

---

<a id="item-9"></a>
## [SHAPE Framework Decodes LLM Math Reasoning via Heuristics](https://arxiv.org/abs/2608.28600) ⭐️ 8.0/10

The paper introduces SHAPE, a framework that analyzes Chain-of-Thought (CoT) trajectories in LLMs using semantic spaces and heuristics from mathematics education. It reveals that mathematical heuristics better explain answer correctness than traditional CoT features, and that models concentrate reasoning in few semantic spaces, similar to humans. This work provides a theoretically-grounded diagnostic framework for interpreting LLM reasoning, which is crucial for improving model transparency and reliability in mathematical tasks. It also offers a new path for post-training LLMs by promoting diverse heuristics, potentially enhancing accuracy in math reasoning benchmarks. SHAPE uses two lenses: semantic spaces (e.g., algebraic, geometric) and heuristics (e.g., simplifying, working backward). The study finds that reinforcement learning induces mode-seeking in heuristic usage, and post-training with diverse heuristics improves accuracy. Code is available on GitHub.

rss · arXiv - AI · Sep 1, 04:00

**Background**: Chain-of-Thought (CoT) prompting is a technique that elicits intermediate reasoning steps from large language models (LLMs), significantly improving their performance on complex reasoning tasks. However, the internal reasoning patterns remain largely opaque. SHAPE leverages concepts from mathematics education to analyze these patterns, offering a new interpretability lens.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28600">[2608.28600] SHAPE of Chain - of - Thought in Math Reasoning</a></li>
<li><a href="https://huggingface.co/papers/2608.28600">Paper page - SHAPE of Chain - of - Thought in Math Reasoning</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#Chain-of-Thought`, `#Mathematical Reasoning`, `#Interpretability`, `#arXiv`

---

<a id="item-10"></a>
## [Curvature Cryptanalysis Extracts Hidden Transformer FFN Directions](https://arxiv.org/abs/2608.28843) ⭐️ 8.0/10

The paper introduces a novel model extraction attack that uses curvature (Hessian) information to recover hidden directions in smooth transformer feed-forward networks (FFNs) with only a small number of black-box queries. On CIFAR-10 vision transformers, just 16 projected Hessians (8193 queries) achieve average cosine alignment above 0.94 for GELU and SiLU activations. This work reveals a new security vulnerability in transformer models, showing that hidden internal structure can be extracted from black-box access alone, which has significant implications for model privacy and intellectual property protection. It also provides a new tool for interpretability, as the recovered structure can be used for functional extraction and high-fidelity substitutes. The attack exploits a second-order leakage channel where projected input Hessians form mixtures of hidden symmetric rank-one factors. The method uses vector-output stencil reuse to reduce query cost by a factor of 16, and adapts finite-difference steps to counter output rounding and Gaussian noise, restoring alignment to 0.9603 and 0.9398.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: Model extraction attacks typically rely on input-output behavior to replicate a model's function, but this paper shows that second-order information (curvature) can reveal internal parameter geometry that behavioral fidelity alone cannot. The attack operates under a chosen-input raw-output oracle, meaning the attacker can query the model with arbitrary inputs and receive raw outputs, but has no access to parameters, gradients, or internal activations. The recovered structure supports functional extraction, allowing the attacker to build a substitute model with high agreement.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28843">[2608.28843] Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linear_cryptanalysis">Linear cryptanalysis - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#model extraction`, `#transformer`, `#Hessian`, `#security`, `#deep learning`

---

<a id="item-11"></a>
## [ESNN: Equivariant Sheaf Neural Networks for Geometric Transport](https://arxiv.org/abs/2608.28853) ⭐️ 8.0/10

The paper introduces Equivariant Sheaf Neural Networks (ESNN), which learn directed, matrix-valued transport between neighboring vector features on graphs while preserving exact Euclidean equivariance. It provides a theoretical characterization showing that any linear O(n)-equivariant map decomposes into independent radial and tangential components when relative displacement is the only covariant input. ESNN addresses a key limitation of first-order equivariant graph neural networks by placing additional geometric flexibility in edge transport rather than increasing representation order. This offers a complementary route to expressive equivariant message passing, potentially influencing future geometric deep learning research and improving performance in tasks like particle dynamics and molecular property prediction. The paper also introduces controlled symmetry relaxation for systems with a preferred ambient direction, which can be prescribed or inferred from data while recovering full E(n)-equivariance when the directional pathway is inactive. Experiments show improvements in dynamics prediction, recovery of the gravity axis when symmetry is broken, substantial gains on selected mesh tasks and long-horizon rollouts, and robustness to unseen rotations.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: Equivariant graph neural networks (GNNs) are designed to respect symmetries in data, such as rotations and translations, which is crucial for modeling geometric systems. Traditional first-order architectures often limit how vector information is transformed across edges, and higher-order representations can be computationally expensive. Sheaf neural networks extend GNNs by assigning vector spaces to nodes and edges with linear maps, enabling richer message passing. This paper builds on these concepts to learn matrix-valued transport while maintaining equivariance.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28853">[2608.28853] Equivariant Sheaf Neural Networks : Learning...</a></li>
<li><a href="https://www.emergentmind.com/topics/category-equivariant-neural-networks-cenns.md">emergentmind.com/topics/category- equivariant - neural - networks ...</a></li>
<li><a href="https://arxiv.org/pdf/2601.21207">A Sheaf - Theoretic and Topological Perspective on Complex Network ...</a></li>

</ul>
</details>

**Tags**: `#graph neural networks`, `#equivariance`, `#geometric deep learning`, `#sheaf theory`, `#arXiv`

---

<a id="item-12"></a>
## [Halt Vector: Causal Steering to Cut LLM Overthinking](https://arxiv.org/abs/2608.28859) ⭐️ 8.0/10

Researchers identified a 'halt vector' in DeepSeek-R1-Distill-Qwen-7B that controls reasoning length, and internalized it into the model weights to reduce overthinking. This intervention cut about a quarter of thinking steps across five unseen benchmarks without global penalties. This work addresses the inefficiency of reasoning models that continue thinking after they already know the answer, which wastes computation. By offering a causal, weight-internalized method, it provides a new approach to improve LLM efficiency, potentially benefiting deployment and cost reduction. The halt vector is a difference-of-means direction at layer 18, and simply maximizing projection onto it corrupts off-axis dimensions, making generation longer; instead, reconstructing the whole steered activation with pinned dimensions works. Fit from only 24 problems and no reinforcement learning, the cut tracks each problem's removable slack at 0.70 correlation.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: Reasoning models like DeepSeek-R1-Distill-Qwen-7B generate long chains of thought, often overthinking beyond the point where the answer is determined. Causal analysis and steering vectors are interpretability techniques that manipulate internal representations to control model behavior. This paper builds on these concepts to achieve efficiency gains.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/collections/deepseek-ai/deepseek-r1">DeepSeek - R 1 - a deepseek-ai Collection</a></li>
<li><a href="https://www.emergentmind.com/topics/neural-steering-vector">Neural Steering Vector</a></li>
<li><a href="https://arxiv.org/abs/2410.15319">[2410.15319] Causality for Large Language Models</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#LLM reasoning`, `#efficiency`, `#causal analysis`, `#DeepSeek`

---

<a id="item-13"></a>
## [Conservative Hybrid Graph Networks Achieve Zero-Shot Transfer in Process Systems](https://arxiv.org/abs/2608.28896) ⭐️ 8.0/10

The paper introduces the Conservative Hybrid Graph Network (CHGN), which learns routing, regime assignment, and removal rates as data-driven surrogates and embeds them into a fixed transport equation, ensuring mass balance by construction. CHGN trained on networks of 10-20 nodes transfers zero-shot to unseen graphs of 25-40 nodes, achieving an RMSE of 2.1e-3 compared to 6e-2 to 9e-2 for GNN baselines. This work addresses a critical limitation in modeling industrial process networks, where topology changes dynamically and latent mechanisms are often unobserved. The zero-shot generalization across topologies without retraining could significantly reduce the need for retraining models on every new plant configuration, impacting process systems engineering and physics-informed machine learning. CHGN enforces mass balance by construction, and on a fluid-mixing pilot plant, it improves on a persistence baseline for held-out physical faults but does not predict manual interventions where valve actions are unobserved. The model achieves a gate MAE of 7.9e-3 and regime accuracy of 94.3% on unseen graphs, with 1.2e-2 and 96.4% respectively on the fixed training topology.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: Industrial process networks, such as chemical plants, consist of units connected by streams, but their effective topology changes as streams are throttled or bypassed and units switch between idle, transition, and active regimes. Traditional graph neural networks (GNNs) trained on measured trajectories may fit data without assigning stable physical meaning to routing. Mass balance, a fundamental conservation law, ensures that mass is neither created nor destroyed in a system, and embedding it into a model guarantees physically consistent predictions.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28896">[2608.28896] Conservative Hybrid Graph Networks for Process...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mass_balance">Mass balance - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/mass-balance-equation">Mass Balance Equation - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**Tags**: `#graph neural networks`, `#process systems`, `#zero-shot learning`, `#physics-informed ML`, `#hybrid models`

---

<a id="item-14"></a>
## [General Coded Computing: A Learning-Theoretic Framework for Stragglers](https://arxiv.org/abs/2608.28910) ⭐️ 8.0/10

The paper introduces General Coded Computing (GCC), a novel framework that replaces algebraic tools with an end-to-end mean-squared error loss to handle stragglers in distributed computing. It provides theoretical performance guarantees, showing the loss decays at least at rate O(S^3 N^{-3}) in the worst-case setting and O(log_{1/p}^3(N) N^{-3}) in a probabilistic setting. This work addresses a critical limitation of existing coded computing schemes, which are designed for exact recovery of structured computations and fail to handle modern ML workloads like deep neural networks. By adopting a learning-theoretic perspective, GCC broadens the applicability of coded computing to approximate computations, potentially impacting distributed training and inference systems. The framework restricts the encoder and decoder to a reproducing kernel Hilbert space (RKHS) with mild smoothness constraints, allowing them to be represented as linear combinations of kernel functions with efficiently computable coefficients. The theoretical guarantees cover two straggler regimes: worst-case with at most S stragglers among N workers, and probabilistic where each worker straggles independently with probability p.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: Coded computing is a paradigm that uses coding theory to inject computational redundancy into distributed systems to mitigate stragglers—slow or failed workers. Traditional schemes rely on algebraic structures for exact recovery, which limits their use in machine learning where computations are often non-algebraic and only require approximate results. This paper proposes a learning-based alternative that directly optimizes an end-to-end loss, making it more flexible for modern workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28910">[2608.28910] Learning-Theoretic Foundation for General Coded ...</a></li>
<li><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/cae00f05c4074758a6542823ae7bea99-Paper-Conference.pdf">Coded Computing for Resilient Distributed</a></li>

</ul>
</details>

**Tags**: `#coded computing`, `#distributed systems`, `#machine learning`, `#straggler mitigation`, `#theory`

---

<a id="item-15"></a>
## [SemKV: Quality-Cliff-Aware Mixed-Precision KV Cache Quantization](https://arxiv.org/abs/2608.28911) ⭐️ 8.0/10

SemKV introduces a quality-cliff-aware mixed-precision KV cache quantization method that preserves all tokens and uses model-internal importance scores to assign adjacent above-cliff precisions, achieving a 6.0x storage reduction with no statistically detectable quality loss compared to full KV for Llama-3.1-8B-Instruct. This work addresses the critical memory bottleneck of long-context LLM inference by revealing a quality cliff in uniform KV quantization and demonstrating that mixed-precision can achieve better average precision. It provides a practical recipe for significantly reducing memory usage without sacrificing quality, which could enable longer contexts and more efficient deployment of LLMs. The paper identifies a quality cliff in the bit range (2.0, 2.322] where uniform quantization collapses, and shows that above the cliff, eight model-internal importance indicators are statistically interchangeable. Replacing the affine base with a distortion-optimized quantizer (TurboQuant-MSE) lowers the cliff and raises the no-detectable-loss operating point to 7.9x storage reduction.

rss · arXiv - Machine Learning · Sep 1, 04:00

**Background**: KV cache stores key and value tensors during LLM inference, growing linearly with context length and becoming the dominant memory bottleneck for long-context models. Quantization reduces memory by using fewer bits per value, but uniform quantization can suffer from a 'quality cliff' where performance drops sharply below a certain bit rate. Mixed-precision quantization assigns different bit widths to different parts of the model to balance efficiency and accuracy. SemKV leverages model-internal importance scores to guide precision allocation, preserving all tokens and using adjacent above-cliff precisions to achieve better average precision than uniform quantization.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Progressive_Mixed-Precision_KV_Cache_Quantization">Progressive Mixed-Precision KV Cache Quantization</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**Tags**: `#KV cache`, `#quantization`, `#LLM inference`, `#mixed-precision`, `#long-context`

---

<a id="item-16"></a>
## [Parametric Multimodal User Memory: Storing What Captions Cannot Carry](https://arxiv.org/abs/2608.28609) ⭐️ 8.0/10

The paper introduces a parametric multimodal user memory that stores perceptual identity keys as inline tokens, overcoming the limitations of text-based memory in personalized agents. It decomposes recall into grounding by a vision-language model and identity extraction by a dedicated encoder, achieving near-oracle performance on the PerceptMem benchmark. This work addresses a critical gap in personalized AI agents by enabling them to remember perceptual aspects of users (e.g., voice, face) that text captions cannot capture. It could significantly enhance multimodal AI systems, making them more truly personalized and capable in real-world applications. The recognition core is training-free, reproducing the encoder's recall on any frozen model at O(1) registration cost. On PerceptMem (12 domains, 1,080 tasks), perceptual identity is capacity-limited while exact facts are binding-limited, suggesting identity belongs in a parametric bank and facts in a text store.

rss · arXiv - NLP · Sep 1, 04:00

**Background**: Personalized agents typically rely on text-based user memories, such as transcripts and captions, which fail to capture perceptual information like voice timbre or facial appearance. The proposed method grounds perceptual memory in the model itself, using a vision-language model to locate the referent and a dedicated encoder to extract an identity key, stored as an inline token. This approach avoids external retrieval round-trips and composes with text memory for comprehensive user modeling.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28609">[2608.28609] Parametric Multimodal User Memory : Storing What...</a></li>
<li><a href="https://01.me/research/multimodal-user-memory/">Parametric Multimodal User Memory — Companion site</a></li>
<li><a href="https://aclanthology.org/2022.emnlp-main.375.pdf">MuRAG: Multimodal Retrieval-Augmented Generator</a></li>

</ul>
</details>

**Tags**: `#multimodal`, `#user memory`, `#personalization`, `#vision-language model`, `#AI agents`

---

<a id="item-17"></a>
## [LLM Peer Review Audit Reveals Inflated Scores and Bias](https://arxiv.org/abs/2608.28626) ⭐️ 8.0/10

A new study audited two multimodal LLMs, Qwen2.5-VL-72B and Pixtral-Large-124B, as peer reviewers for ICLR 2026 submissions, finding they assign inflated scores (7.0-8.1 vs human 3.4-6.8) and detect only 12.1% of inserted errors. This matters because LLMs are increasingly used in academic peer review, and the findings highlight serious limitations in their calibration and error detection, potentially undermining the integrity of scientific evaluation if adopted without safeguards. The study used 165 ICLR 2026 submissions, manipulated author identity (blinded, high-prestige, low-prestige), and inserted 145 verifiable errors into 55 manuscripts. A one-sentence verification instruction improved error detection to 22.2%, but 78% of errors remained undetected; providing figures reduced detection while increasing scores.

rss · arXiv - NLP · Sep 1, 04:00

**Background**: Large language models (LLMs) are AI systems trained on vast text data, and multimodal LLMs can also process images. They are increasingly used for tasks like peer review, but their reliability in critical evaluation is questionable. This study tests two such models on conference submissions, comparing their scores and error detection to human reviewers.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Qwen25-VL-72B-Instruct">Qwen2.5-VL-72B-Instruct</a></li>
<li><a href="https://huggingface.co/mistral-community/Pixtral-Large-Instruct-2411">mistral-community/ Pixtral - Large -Instruct-2411 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_LLM">Multimodal LLM</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#peer review`, `#AI bias`, `#multimodal`, `#academic integrity`

---

<a id="item-18"></a>
## [MIRAGE-CAD: Multimodal Generation of Executable CAD Programs](https://arxiv.org/abs/2608.28669) ⭐️ 8.0/10

MIRAGE-CAD introduces a construction-mediated method that generates executable CAD programs from natural language, images, point clouds, and B-Rep geometry, achieving 55.4-70.0% build success and 52.3-66.2% STEP export success on 2,500 held-out queries per modality without retrieval. This work addresses the fundamental ambiguity in recovering parametric CAD programs from observed objects, offering a unified approach across multiple input types. The high success rates and explicit construction-plan interface could significantly advance CAD automation and design workflows, impacting engineers and designers. The system uses a shared construction representation and an explicit construction-plan interface, with Python code executed by an OpenCASCADE kernel to build solids and export as STEP. Controlled comparisons show that a decoder conditioned directly on the continuous representation also reconstructs strongly, while the explicit plan provides a readable and measurable intermediate representation whose agreement with the reference construction predicts downstream execution success.

rss · arXiv - Computer Vision · Sep 1, 04:00

**Background**: CAD (Computer-Aided Design) programs are parametric models that define 3D objects through construction steps. B-Rep (Boundary Representation) describes geometry via its boundaries, and STEP is a standard file format for exchanging 3D CAD data. OpenCASCADE is a widely used open-source CAD kernel that executes modeling operations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/STEP_file_format">STEP file format</a></li>
<li><a href="https://www.shapr3d.com/content-library/what-is-b-rep">Boundary representation ( b - rep ): What it is, and why it’s a problem in...</a></li>

</ul>
</details>

**Tags**: `#CAD`, `#multimodal learning`, `#program generation`, `#computer vision`, `#geometry processing`

---

<a id="item-19"></a>
## [Interaction Growth Complexity Characterizes Discrete Diffusion Sampling](https://arxiv.org/abs/2608.28949) ⭐️ 8.0/10

This paper introduces a novel geometric measure, the interaction growth complexity (IGC), to characterize the sampling performance of product-reference discrete diffusion algorithms. It shows that a bivariate IGC kernel exactly represents KL discretization error and a one-step upper bound, and that optimal stepsize scheduling can reduce iteration complexity. This work provides a theoretical foundation for understanding and optimizing discrete diffusion models, which are increasingly important for generative modeling of discrete data such as text and graphs. The proposed complexity measure could guide the design of more efficient sampling algorithms and improve the practical deployment of these models. The paper shows that samplers using equi-spaced steps in log-squared-reliability-odds have performance depending on aggregate IGC mass, while refined stepsize choices yield lower complexity based on a square-root functional. It also demonstrates that general product reference distributions can reshape the IGC profile and lead to dimension-dependent improvements, and connects aggregate IGC mass to total correlation and dual total correlation.

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**Background**: Discrete diffusion models are a class of generative models that iteratively transform noise into discrete data by reversing a forward corruption process. Product-reference diffusion algorithms use a product distribution as a reference for the forward process, and their sampling performance depends on the path taken in the probability simplex. The interaction growth complexity (IGC) is a new path-based measure that captures the geometric complexity of the data distribution along the diffusion path, providing a unified framework to analyze discretization error and iteration complexity.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28949">The information geometry of product - reference discrete diffusion ...</a></li>

</ul>
</details>

**Tags**: `#diffusion models`, `#discrete sampling`, `#information geometry`, `#sampling complexity`, `#theory`

---

<a id="item-20"></a>
## [Jigsaw-CRL: Recovering Global Latent Causal Order from Fragmented Multi-Client Interventions](https://arxiv.org/abs/2608.28991) ⭐️ 8.0/10

Jigsaw-CRL is a new framework that recovers the global latent causal order from fragmented multi-client interventions, where each client only accesses a subset of latent variables. It leverages low-rank structure in precision matrix differences under soft interventions to assemble client-specific fragments into the global node-level causal order. This work addresses a novel and practical challenge in causal representation learning, relevant to distributed and privacy-preserving settings where data cannot be centralized. It extends causal discovery to scenarios where clients observe only parts of the system, potentially enabling more robust and scalable causal inference in real-world applications. The framework provides identifiability guarantees, develops practical algorithms, and validates them on synthetic data. The code is available at an anonymous repository, and the paper is on arXiv (2608.28991).

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**Background**: Causal representation learning (CRL) aims to recover latent causal variables and their structural relations from high-dimensional observations. Traditional CRL assumes all environments share the same latent variables, but in fragmented multi-client settings, clients intervene on different subsets, causing marginalization to introduce bidirected edges and breaking node-wise latent causal graphs. This paper tackles this by assembling client-specific fragments to recover the global causal order.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Causal_Representation_Learning">Causal Representation Learning</a></li>
<li><a href="https://arxiv.org/abs/2102.11107">[2102.11107] Towards Causal Representation Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Causal_graph">Causal graph - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#causal representation learning`, `#causal discovery`, `#multi-client`, `#latent variables`, `#interventions`

---

<a id="item-21"></a>
## [Sharp RIP Threshold for Global Minima of Rank-Restricted Matrix LASSO](https://arxiv.org/abs/2608.29018) ⭐️ 8.0/10

This paper determines the sharp restricted isometry property (RIP) threshold for recovery at global minima of the rank-restricted matrix LASSO, providing a precise condition on the RIP constant that guarantees accurate recovery. The result also extends to the vector LASSO case. This work provides a fundamental theoretical limit for matrix LASSO recovery, which is crucial for compressed sensing and high-dimensional statistics. The sharp threshold clarifies when recovery is possible and cannot be improved, guiding algorithm design and theoretical analysis in these fields. The sharp threshold is given by δ_sharp(t)=t/(4-t) for 0<t<4/3 and δ_sharp(t)=√((t-1)/t) for t≥4/3, where t=k/r_*. The result holds for all search ranks r≥r_* and the constants are independent of r. The paper also shows the threshold cannot be improved via counterexamples.

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**Background**: The restricted isometry property (RIP) is a key concept in compressed sensing that ensures stable recovery of sparse signals from linear measurements. Matrix LASSO is a nuclear-norm regularized least-squares problem used for low-rank matrix recovery, generalizing the vector LASSO to matrices. The Frobenius norm error measures the recovery accuracy in matrix problems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cs.columbia.edu/~andoni/algoS19/scribes/scribe9.tex">Lecture #9: Compressed Sensing : Restricted Isometry Property</a></li>
<li><a href="https://arxiv.org/html/2404.12828">Low solution rank of the matrix LASSO under RIP with consequences...</a></li>

</ul>
</details>

**Tags**: `#matrix LASSO`, `#restricted isometry property`, `#compressed sensing`, `#high-dimensional statistics`, `#optimization`

---

<a id="item-22"></a>
## [Deep Latent Variable Framework Jointly Models Missingness, Error, Heterogeneity](https://arxiv.org/abs/2608.30040) ⭐️ 8.0/10

This paper introduces a unified probabilistic framework that jointly addresses missing data, measurement error, and population heterogeneity using a hierarchical tree-routed variational autoencoder with reconvergent routing and calibration-based denoising. The framework supports MCAR, MAR, and MNAR missingness mechanisms while learning subgroup-specific and globally shared latent structures. This work is significant because it addresses three common data challenges in a single model, which is more realistic than treating them separately. It could improve the reliability of analyses in healthcare and other high-dimensional applications where data are often noisy and incomplete. The proposed method integrates a pattern-aware latent representation, a hierarchical tree-routed encoder, and a reconvergent branch-sharing architecture. Simulation studies show substantial improvements over existing deep generative imputation approaches under complex heterogeneous missingness and measurement-error settings.

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**Background**: Variational autoencoders (VAEs) are generative models that learn latent representations of data. Hierarchical VAEs, such as TreeVAE, extend this by learning tree-based posterior distributions, which can capture hierarchical structure in data. Missing data mechanisms (MCAR, MAR, MNAR) describe how missingness relates to observed and unobserved data, and measurement error refers to inaccuracies in recorded values. This paper combines these concepts to handle real-world data complexities.

<details><summary>References</summary>
<ul>
<li><a href="https://towardsdatascience.com/difference-between-autoencoder-ae-and-variational-autoencoder-vae-ed7be1c038f2/">towardsdatascience.com/difference-between- autoencoder -ae-and...</a></li>
<li><a href="https://mvandenhi.github.io/publications/manduchi-2023-tree/">Tree Variational Autoencoders | Moritz Vandenhirtz</a></li>
<li><a href="https://arxiv.org/pdf/2608.30040">A Deep Latent Variable Framework for Jointly Modeling Missingness...</a></li>

</ul>
</details>

**Tags**: `#variational autoencoder`, `#missing data`, `#measurement error`, `#heterogeneity`, `#probabilistic modeling`

---

<a id="item-23"></a>
## [Token Prediction Organizes Representations: A Statistical Framework](https://arxiv.org/abs/2608.30072) ⭐️ 8.0/10

This paper introduces a statistical framework showing that token prediction organizes token embeddings and contextual representations according to Hellinger distance between context distributions, with explicit error bounds. It also establishes downstream guarantees for token generation, community recovery, and linear probe classification. This work provides a theoretical foundation for understanding why token prediction, the core pre-training objective of large language models, yields broadly useful representations. It bridges the gap between pre-training loss and downstream performance, potentially guiding more efficient and interpretable model designs. The framework assumes a softmax prediction head and shows that token embeddings are organized by Hellinger distance, with errors depending on prediction accuracy and token frequency. It also introduces a self-consistency principle where repeated applications of a shared representation block refine contextual representations without adding parameters.

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**Background**: Token prediction is the standard pre-training objective for modern language models like GPT and Llama, where the model learns to predict the next token in a sequence. Hellinger distance is a metric that quantifies the similarity between two probability distributions, and it is used here to measure the similarity between context distributions. Representation geometry refers to the spatial arrangement of embeddings in a high-dimensional space, which is believed to capture semantic relationships.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hellinger_distance">Hellinger distance - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2404.19737">Better & Faster Large Language Models via Multi- token Prediction</a></li>
<li><a href="https://avrtt.github.io/research/geometry_estimation/">Geometry estimation, pt. 1 - avrtt.blog</a></li>

</ul>
</details>

**Tags**: `#representation learning`, `#language models`, `#theory`, `#token prediction`, `#statistical learning`

---