---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 122 items, 28 important content pieces were selected

---

1. [PyTorch: Leading Deep Learning Framework on GitHub](#item-1) ⭐️ 9.0/10
2. [Unified Theory of Deep Learning from Approximation to Emergence](#item-2) ⭐️ 9.0/10
3. [BPE Tokenization Creates Exploitable Gaps in LLM Safety Alignment](#item-3) ⭐️ 9.0/10
4. [Pegasus Spyware Hits EU Parliament Spy Probe Member](#item-4) ⭐️ 8.0/10
5. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-5) ⭐️ 8.0/10
6. [Current AI Launches Open Source AI Gap Map](#item-6) ⭐️ 8.0/10
7. [Chrome DevTools MCP Server for AI Coding Agents](#item-7) ⭐️ 8.0/10
8. [Harvard Releases Open-Source Book on ML Systems](#item-8) ⭐️ 8.0/10
9. [Open WebUI: A Self-Hosted AI Platform with Strong Community Traction](#item-9) ⭐️ 8.0/10
10. [Black: The Uncompromising Python Code Formatter](#item-10) ⭐️ 8.0/10
11. [Auto-FL-Research: LLM Agents Automate Federated Learning Algorithm Search](#item-11) ⭐️ 8.0/10
12. [Wiola: A Novel SLM Architecture with Five Original Components](#item-12) ⭐️ 8.0/10
13. [CreativityNeuro: Boosting LLM Divergent Thinking via Weight Steering](#item-13) ⭐️ 8.0/10
14. [Diffusion Language Models Match AR in Radiology Drafting](#item-14) ⭐️ 8.0/10
15. [RLVR Boosts LLM Tool-Use in Enterprise Workflows](#item-15) ⭐️ 8.0/10
16. [Procedural Memory Distillation Boosts Self-Improving LLMs](#item-16) ⭐️ 8.0/10
17. [Grid-Based ANN Scaling Laws Reveal Dimensional Crossover Advantage](#item-17) ⭐️ 8.0/10
18. [NightVision Attack Recovers LLM Architecture via Restrictive API](#item-18) ⭐️ 8.0/10
19. [ProvenanceGuard: Detecting LLM Agent Misalignment via Provenance Analysis](#item-19) ⭐️ 8.0/10
20. [Kara: Sliding-Window KV Cache Compression for Efficient LLM Serving](#item-20) ⭐️ 8.0/10
21. [Prompt Framing Inflates LLM Error Detection F1 Scores](#item-21) ⭐️ 8.0/10
22. [First Benchmark for LLM Office File Comprehension](#item-22) ⭐️ 8.0/10
23. [MapDreamer: Aerial Imagery to Lane-Level Maps via Diffusion](#item-23) ⭐️ 8.0/10
24. [G-CBM: Unsupervised Concept-Graph for Visual Explanations](#item-24) ⭐️ 8.0/10
25. [LF-IBIS: Full Bayesian RL Without Likelihood](#item-25) ⭐️ 8.0/10
26. [Shallow NNs Reformulated as Well-Posed Continuum Problem](#item-26) ⭐️ 8.0/10
27. [New Framework Links Conformal Prediction to Counterfactual Decisions](#item-27) ⭐️ 8.0/10
28. [Device Revives Donor Eyes, Paving Way for Transplants](#item-28) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [PyTorch: Leading Deep Learning Framework on GitHub](https://github.com/pytorch/pytorch) ⭐️ 9.0/10

The PyTorch repository on GitHub continues to be the primary source for the library, offering tensor computation with GPU acceleration and dynamic neural networks via autograd. This trending status reflects ongoing community interest and development activity. PyTorch is a foundational tool in AI/ML research and industry, enabling rapid prototyping and production deployment. Its popularity on GitHub indicates strong community support and continuous improvement, which benefits millions of developers worldwide. PyTorch provides two high-level features: tensor computation with GPU acceleration (similar to NumPy) and deep neural networks built on a tape-based autograd system. It supports integration with Python packages like NumPy, SciPy, and Cython, and offers binaries for NVIDIA Jetson platforms as well as source builds for CUDA, ROCm, and Intel GPU support.

rss · GitHub Trending - Daily (All) · Jul 3, 22:57

**Background**: PyTorch is an open-source machine learning framework developed primarily by Meta AI. It is widely used for deep learning research and production due to its dynamic computation graph and Python-first design. The repository includes the core library, installation instructions, and continuous integration status.

**Tags**: `#deep learning`, `#PyTorch`, `#GPU acceleration`, `#neural networks`, `#tensor computation`

---

<a id="item-2"></a>
## [Unified Theory of Deep Learning from Approximation to Emergence](https://arxiv.org/abs/2607.01311) ⭐️ 9.0/10

A comprehensive monograph titled 'From Approximation to Emergence: A Theory of Deep Learning' has been published on arXiv, presenting a unified, proof-oriented account of deep learning theory spanning from classical foundations to modern phenomena like emergence and alignment. This work organizes a broad literature into a coherent narrative, offering a rigorous map of deep learning theory that is likely to become a key reference for researchers and practitioners, helping to guide future research and understanding of how learned mechanisms arise from scale, data, architecture, and training. The monograph covers topics including overparameterization, robustness, generative modeling, transformers, in-context learning, scaling laws, interpretability, alignment, and emergence, examining each theory through the object it controls, its assumptions, and unexplained phenomena.

rss · arXiv - Data Science & Statistics · Jul 3, 04:00

**Background**: Deep learning theory has traditionally been fragmented, with separate results for approximation, optimization, and generalization. In recent years, phenomena like in-context learning (where models adapt to tasks from examples in prompts) and scaling laws (empirical power-law relations between model size, data, and performance) have emerged, challenging existing theories. This monograph aims to unify these diverse strands into a single coherent framework.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/In-context_learning">In-context learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#deep learning theory`, `#emergence`, `#transformers`, `#scaling laws`, `#alignment`

---

<a id="item-3"></a>
## [BPE Tokenization Creates Exploitable Gaps in LLM Safety Alignment](https://arxiv.org/abs/2607.01239) ⭐️ 9.0/10

A new paper reveals that BPE tokenization fragments safety-critical words, allowing character-level perturbations to bypass LLM safety alignment with 80-100% success in flipping refusal triggers across five model families. This identifies a fundamental structural vulnerability in current LLM safety alignment, as alignment datasets contain no intentionally fragmented inputs, meaning models are not robust to even simple character-level attacks. The attack achieves 48% genuinely harmful outputs per-model (29-65%), and activation patching localizes the disrupted signal to the last ~30% of layers; DPO training fails to close the attack success rate across 55 checkpoints.

rss · arXiv - NLP · Jul 3, 04:00

**Background**: BPE (Byte Pair Encoding) tokenization splits text into subword units based on frequency, which can break safety-related words (e.g., 'harmful') into pieces like 'harm' and 'ful', making them harder for the model to recognize as refusal triggers. Alignment datasets like HarmBench are used to train models to refuse harmful requests, but they contain only naturally tokenized inputs, not adversarially fragmented ones.

<details><summary>References</summary>
<ul>
<li><a href="https://machinelearningplus.com/gen-ai/build-bpe-tokenizer/">How LLM Tokenization Works: Build a BPE Tokenizer</a></li>
<li><a href="https://huggingface.co/datasets/walledai/HarmBench">walledai/HarmBench · Datasets at Hugging Face</a></li>
<li><a href="https://www.aussieai.com/research/activation-patching">Activation Patching</a></li>

</ul>
</details>

**Tags**: `#LLM safety`, `#tokenization`, `#adversarial attacks`, `#AI alignment`, `#BPE`

---

<a id="item-4"></a>
## [Pegasus Spyware Hits EU Parliament Spy Probe Member](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab confirmed with high confidence that the iPhone of European Parliament member Stelios Kouloglou was infected with NSO Group's Pegasus spyware on multiple occasions in 2022 and 2023. Kouloglou was a member of the European Parliament's committee investigating the use of spyware like Pegasus. This incident highlights the risk that even those investigating state-sponsored spyware can be targeted, undermining democratic oversight. It also raises urgent questions about device security policies for EU officials and the accountability of spyware vendors. The infections occurred on or around October 21, 2022, and March 6–7, 2023, according to forensic analysis of artifacts from Kouloglou's iPhone. The attacks potentially compromised both personal medical information and confidential government documents stored on the same device.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a powerful spyware developed by Israeli firm NSO Group, capable of remotely compromising iOS and Android devices, often via zero-click exploits. Citizen Lab is a University of Toronto research lab that investigates digital threats to human rights and has exposed numerous Pegasus abuses globally.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Citizen_Lab">Citizen Lab</a></li>
<li><a href="https://us.norton.com/blog/emerging-threats/pegasus-spyware">What is Pegasus spyware, and how to detect and remove it</a></li>

</ul>
</details>

**Discussion**: Commenters debated whether EU Parliament should enforce separation of work and personal devices, and noted that Greece and other EU states have been implicated in Pegasus abuse. Some argued that using GrapheneOS or enabling lockdown mode could have prevented the infection, while others criticized Apple and Google for making essential hardening features hard to use.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#surveillance`, `#EU politics`

---

<a id="item-5"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 8.0/10

Marijn Haverbeke, the creator of ProseMirror, has released Wordgard 0.1.0, a new in-browser rich-text editor that offers a simplified yet powerful approach to document editing. Wordgard introduces a simpler change representation inspired by CodeMirror, potentially lowering the learning curve for developers while maintaining high performance, and could become a strong alternative to ProseMirror for new projects. Wordgard shares many concepts with ProseMirror but has no direct upgrade path; switching requires significant rework. The editor features improved design and documentation, and its change system is based on a delta format similar to ShareJS.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a widely-used open-source library for building rich-text editors with custom document schemas and collaborative editing support. It has a steep learning curve due to its modular and functional design. Wordgard aims to address this by offering a more intuitive API while retaining the power of ProseMirror.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.prosemirror.net/t/wordgard-0-1-0/9035">Wordgard 0.1.0 - Announce - discuss.ProseMirror</a></li>
<li><a href="https://marijnhaverbeke.nl/blog/wordgard-0.1.html">Wordgard Release 0.1</a></li>

</ul>
</details>

**Discussion**: The community is excited about Wordgard, with many praising its design and documentation. Users are discussing the differences from ProseMirror, noting the lack of an upgrade path and the effort required to switch. Some express interest in using Wordgard for new projects, while others appreciate the improved developer experience.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`

---

<a id="item-6"></a>
## [Current AI Launches Open Source AI Gap Map](https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/#atom-everything) ⭐️ 8.0/10

Current AI, a non-profit founded at the AI Action Summit in Paris in February 2025, launched the Open Source AI Gap Map v0.1, indexing 421 products across the open source AI stack, including 266 software tools, 85 models, 50 datasets, and 20 hardware projects. This map provides a comprehensive, structured view of the open source AI ecosystem, helping identify gaps and opportunities for investment and development, which is crucial for guiding the direction of open source AI efforts. The underlying data is released under an MIT license on GitHub, containing 1,184 YAML files and scripts, and can be explored via Datasette Lite. The map also tracks 16,185 GitHub repos as part of the long tail of uncategorized artifacts.

rss · Simon Willison · Jul 3, 22:04

**Background**: Current AI is a global non-profit partnership backed by $400 million in committed capital, aiming to build a public option for AI. The Gap Map builds on work from experts at Columbia Convening, MOF, Hugging Face, and others, and visualizes over 24,600 AI projects across the open source stack.

<details><summary>References</summary>
<ul>
<li><a href="https://map.currentai.org/">Current AI – Open Source AI Gap Map</a></li>
<li><a href="https://www.currentai.org/blogs/introducing-the-gap-map-v0-1">Introducing the Gap Map v0.1 - currentai.org</a></li>
<li><a href="https://simonwillison.net/2026/Jul/3/open-source-ai-gap-map/">Open Source AI Gap Map - simonwillison.net</a></li>

</ul>
</details>

**Tags**: `#open source`, `#AI`, `#ecosystem`, `#mapping`, `#non-profit`

---

<a id="item-7"></a>
## [Chrome DevTools MCP Server for AI Coding Agents](https://github.com/ChromeDevTools/chrome-devtools-mcp) ⭐️ 8.0/10

Google has released an official MCP server, chrome-devtools-mcp, that allows AI coding agents to control and inspect live Chrome browsers using the full power of Chrome DevTools. This bridges the gap between AI coding agents and real browser debugging, enabling agents to perform reliable automation, in-depth debugging, and performance analysis directly in a live browser, which significantly enhances their capabilities for web development tasks. The server uses Puppeteer for automation and Chrome DevTools for tracing and performance insights. It collects usage statistics by default but allows opt-out via the --no-usage-statistics flag, and performance tools may send trace URLs to the Google CrUX API unless disabled with --no-performance-crux.

rss · GitHub Trending - Daily (All) · Jul 3, 22:57

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 that standardizes how AI applications connect to external tools and data sources. Chrome DevTools Protocol (CDP) is the underlying protocol that allows tools to instrument, inspect, debug, and profile Chromium-based browsers. This MCP server combines both, giving AI agents a standardized interface to leverage CDP's capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://chromedevtools.github.io/devtools-protocol/">Chrome DevTools Protocol - GitHub Pages</a></li>

</ul>
</details>

**Tags**: `#Chrome DevTools`, `#MCP`, `#AI agents`, `#debugging`, `#automation`

---

<a id="item-8"></a>
## [Harvard Releases Open-Source Book on ML Systems](https://github.com/harvard-edge/cs249r_book) ⭐️ 8.0/10

Harvard University has released an open-source book titled 'Machine Learning Systems: Principles and Practices of Engineering Artificially Intelligent Systems' on GitHub, covering the engineering of AI systems from a systems perspective. This resource fills a gap in ML education by focusing on systems engineering rather than just algorithms, making it valuable for software engineers and AI practitioners. Its open-source nature and multi-language translations enable broad global access. The repository includes not only the book but also labs, slides, a simulator (MLSys·im), and a TinyTorch implementation, all with CI validation. The book is licensed under CC-BY-NC-SA 4.0.

rss · GitHub Trending - Python · Jul 3, 22:57

**Background**: Machine learning systems engineering involves designing and deploying ML models in production, covering data pipelines, model serving, monitoring, and hardware optimization. This book aims to teach these principles through a hands-on, project-based approach, complementing traditional ML theory courses.

**Tags**: `#machine learning`, `#systems`, `#education`, `#open-source`, `#AI engineering`

---

<a id="item-9"></a>
## [Open WebUI: A Self-Hosted AI Platform with Strong Community Traction](https://github.com/open-webui/open-webui) ⭐️ 8.0/10

Open WebUI is an open-source, user-friendly AI interface that supports multiple backends including Ollama and OpenAI-compatible APIs, with built-in RAG inference engine and offline operation capability. It addresses the need for a unified, self-hosted interface for various AI models, reducing dependency on cloud services and giving users full control over their data and models. The project has gained high community traction with many GitHub stars, forks, and an active Discord server. It offers easy installation via pip, Docker, or Kubernetes, and provides enterprise plans with custom theming and SLA support.

rss · GitHub Trending - Python · Jul 3, 22:57

**Background**: Ollama is a popular tool for running large language models locally, while OpenAI provides cloud-based AI APIs. Open WebUI acts as a frontend that can connect to both, allowing users to switch between local and cloud models seamlessly.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/open-webui/open-webui">GitHub - open-webui/open-webui: User-friendly AI Interface (Supports Ollama, OpenAI API, ...) · GitHub</a></li>
<li><a href="https://docs.openwebui.com/features/">Features / Open WebUI</a></li>
<li><a href="https://ollama.com/">Ollama</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Open Source`, `#WebUI`, `#Ollama`, `#OpenAI`

---

<a id="item-10"></a>
## [Black: The Uncompromising Python Code Formatter](https://github.com/psf/black) ⭐️ 8.0/10

Black is a widely adopted Python code formatter that automatically enforces consistent code style, reducing formatting debates and improving code review efficiency. By automating formatting decisions, Black saves developers time and mental energy, making codebases more uniform and reviews faster. Its adoption by major projects and the Python Software Foundation underscores its industry impact. Black requires Python 3.10+ and can be installed via pip. It supports Jupyter Notebooks with the 'black[jupyter]' extra and offers standalone executables for users without Python.

rss · GitHub Trending - Python · Jul 3, 22:57

**Background**: Python code formatters automatically adjust code layout to follow style guidelines, reducing human effort and inconsistency. Black is known for its 'uncompromising' approach, offering minimal configuration and deterministic output.

**Tags**: `#Python`, `#code formatter`, `#developer tools`, `#open source`

---

<a id="item-11"></a>
## [Auto-FL-Research: LLM Agents Automate Federated Learning Algorithm Search](https://arxiv.org/abs/2607.01366) ⭐️ 8.0/10

Auto-FL-Research (AFR) introduces a constrained coding-agent workflow that uses LLM agents to automatically propose and implement federated learning algorithm variants, including server aggregation rules, client update schedules, and local objectives. The system was evaluated on five healthcare FLamby tasks and six LEAF datasets, showing gains on most tasks while also revealing seed-sensitive and search-selected failure cases. This work addresses a significant pain point in federated learning research by automating the expensive and difficult manual exploration of algorithmic choices. It could accelerate FL experimentation and enable more systematic discovery of effective training recipes, particularly in privacy-sensitive domains like healthcare. AFR uses task profiles to fix the mutation surface, compute budget, communication contract, and final model evaluation, ensuring fair comparisons. The paper reports mixed outcomes: some gains come from FL-recipe changes, while others are due to fixed-surface tuning or are not reproducible under repeat or held-out evaluation.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Federated learning (FL) is a machine learning paradigm where multiple clients collaboratively train a model without sharing raw data, often used in healthcare for privacy reasons. FL research involves many algorithmic choices (e.g., optimizer variants, aggregation rules) that are expensive to explore manually. LLM agents are AI systems that can reason, plan, and use tools like code compilers to solve complex tasks. FLamby is a benchmark suite of healthcare datasets with natural splits for cross-silo FL evaluation.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2210.04620">[2210.04620] FLamby: Datasets and Benchmarks for Cross-Silo ... GitHub - owkin/FLamby: Cross-silo Federated Learning ... Welcome to FLamby’s documentation! — FLamby 0.0.1 documentation FLamby/README.md at main · owkin/FLamby · GitHub FLamby: Datasets and Benchmarks for Cross-Silo Federated ... FENDA-FL: Personalized Federated Learning on Heterogeneous ... Bridging federated learning theory and practice with real ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Federated_learning">Federated learning - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2412.13667v2">Exploring Multi-Modal Data with Tool-Augmented LLM Agents for ...</a></li>

</ul>
</details>

**Tags**: `#federated learning`, `#automated machine learning`, `#LLM agents`, `#healthcare AI`, `#algorithm search`

---

<a id="item-12"></a>
## [Wiola: A Novel SLM Architecture with Five Original Components](https://arxiv.org/abs/2607.01394) ⭐️ 8.0/10

Wiola introduces a fully original Small Language Model architecture with five novel components: Spiral Rotary Positional Encoding, Gated Cross-Layer Attention, Adaptive Token Merging, Dual Stream Feed-Forward, and WiolaRMSNorm. The model is released in four sizes (120M to 1.5B parameters) and is compatible with HuggingFace Transformers. This work represents a significant departure from dominant model families like GPT and LLaMA, potentially opening new directions for efficient language model design. The five independently novel components could inspire future research in attention mechanisms, positional encoding, and token reduction. The paper provides complete mathematical derivations, architectural block diagrams, complexity analyses, and systematic comparisons against GPT-2, LLaMA-2, and Mistral. All 22 architectural unit tests pass, and the model is fully compatible with the HuggingFace Transformers ecosystem.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Small Language Models (SLMs) are language models with fewer parameters (typically under 2B), designed for efficiency and deployment on resource-constrained devices. Most current SLMs are derived from larger architectures like GPT or LLaMA, often using techniques like knowledge distillation. Wiola aims to build an SLM from first principles without borrowing from existing model families.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2602.03227">[2602.03227] Spiral RoPE: Rotate Your Rotary Positional Embeddings in the 2D Plane</a></li>
<li><a href="https://arxiv.org/abs/2509.09955">[2509.09955] Adaptive Token Merging for Efficient Transformer ...</a></li>
<li><a href="https://arxiv.org/abs/2605.27465">[2605.27465] AdaMerge: Salience-Aware Adaptive Token Merging ...</a></li>

</ul>
</details>

**Tags**: `#SLM`, `#architecture`, `#efficiency`, `#attention`, `#positional encoding`

---

<a id="item-13"></a>
## [CreativityNeuro: Boosting LLM Divergent Thinking via Weight Steering](https://arxiv.org/abs/2607.01433) ⭐️ 8.0/10

Researchers introduced CreativityNeuro, a data-free contrastive weight steering method that improves divergent thinking in large language models by up to 14 human percentile points on the Divergent Association Task and significantly reduces mode collapse, as validated by a human evaluation (N=720). This work addresses the critical issue of mode collapse in LLMs, where models generate repetitive responses, and offers a practical, data-free solution that enhances creativity without retraining, potentially benefiting creative AI applications like story generation and brainstorming tools. CreativityNeuro operates in weight space rather than activation space, and while activation steering matched its performance on the DAT, only weight-space steering transferred to the Alternative Uses Test and Task Task, demonstrating better generalization to unseen tasks.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Divergent thinking is the ability to generate many creative ideas from a single prompt, but LLMs often suffer from mode collapse, producing similar outputs. Contrastive weight steering is a post-training technique that edits model weights using arithmetic operations on fine-tuned checkpoints to induce desired behaviors without gradient-based fine-tuning.

<details><summary>References</summary>
<ul>
<li><a href="https://www.alignmentforum.org/posts/HYTbakdHpxfaCowYp/steering-language-models-with-weight-arithmetic">Steering Language Models with Weight Arithmetic</a></li>
<li><a href="https://arxiv.org/abs/2511.05408">[2511.05408] Steering Language Models with Weight Arithmetic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mode_collapse">Mode collapse - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#creativity`, `#divergent thinking`, `#mode collapse`, `#weight steering`

---

<a id="item-14"></a>
## [Diffusion Language Models Match AR in Radiology Drafting](https://arxiv.org/abs/2607.01436) ⭐️ 8.0/10

Researchers adapted DiffusionGemma-26B, a mixture-of-experts diffusion language model, and showed it matches or exceeds autoregressive Gemma-4-26B on medical VQA tasks, while enabling any-order infill for interactive radiology report drafting with 3.5-4.4x faster decoding. This work demonstrates that diffusion language models can achieve parity with autoregressive models in a high-stakes medical domain, offering a novel interactive drafting capability that autoregressive models lack, which could improve clinical workflow efficiency and report consistency. The finetuned model has only 3.8B active parameters due to the mixture-of-experts architecture, yet it is competitive with frontier vision-language models. The any-order infill capability is inherent to diffusion models because they denoise a token canvas bidirectionally, unlike left-to-right autoregressive generation.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Diffusion language models generate text by iteratively denoising a sequence of tokens, allowing bidirectional context, while autoregressive models generate tokens left to right. Mixture-of-experts (MoE) architectures use multiple specialized subnetworks to increase model capacity without proportional compute cost. LoRA (Low-Rank Adaptation) is a parameter-efficient fine-tuning method that updates only a small set of weights.

<details><summary>References</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10909201/">Diffusion models in text generation: a survey - PMC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#diffusion language models`, `#medical AI`, `#radiology`, `#interactive drafting`, `#efficient decoding`

---

<a id="item-15"></a>
## [RLVR Boosts LLM Tool-Use in Enterprise Workflows](https://arxiv.org/abs/2607.01465) ⭐️ 8.0/10

Researchers propose Reinforcement Learning with Verifiable Rewards (RLVR) to improve LLM tool-use in enterprise SaaS workflows, demonstrating on synthetic Jira and Confluence environments that RLVR lifts average reward from 0.35-0.92 to 0.95-1.00 for small models like Qwen3-1.7B and Qwen3.5-4B. This work addresses a critical limitation of LLMs in enterprise tool-use—the objective mismatch between next-token prediction and successful API execution—without requiring human labels or live APIs, potentially enabling more reliable automation of niche enterprise workflows. The study uses GRPO training with rewards computed entirely from tool-call traces, and finds that one of five scenarios (ticket-transition) already saturates with the prompted baseline, while Confluence page creation sees the largest gain from 0.35 to 1.00. Limitations include the scalability of hand-crafting verifiable rewards beyond a few endpoints.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Large language models are trained to predict the next token, but enterprise SaaS workflows require precise API calls with correct arguments and order. RLVR (Reinforcement Learning with Verifiable Rewards) uses objective, externally verifiable signals (e.g., unit tests) as rewards, avoiding the need for human labels or learned judges. GRPO is a reinforcement learning algorithm used to optimize policies from such rewards.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2506.14245">[2506.14245] Reinforcement Learning with Verifiable Rewards ...</a></li>
<li><a href="https://labelstud.io/blog/reinforcement-learning-from-verifiable-rewards/">Reinforcement Learning from Verifiable Rewards - Label Studio</a></li>
<li><a href="https://github.com/opendilab/awesome-RLVR">Awesome RLVR — Reinforcement Learning with - GitHub</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#LLM agents`, `#tool-use`, `#enterprise SaaS`, `#RLVR`

---

<a id="item-16"></a>
## [Procedural Memory Distillation Boosts Self-Improving LLMs](https://arxiv.org/abs/2607.01480) ⭐️ 8.0/10

Researchers propose Procedural Memory Distillation (PMD), a method that converts cross-episode reinforcement learning signals into reusable procedural memory and distills it into a language model's weights during training, enabling self-improvement without external memory at inference. PMD addresses a key limitation of existing RLVR and self-distillation methods that only use episode-local updates, capturing richer cross-episode patterns. This could significantly enhance the reasoning and coding abilities of large language models, as shown by improvements of 3.8-13.6% on benchmarks. PMD organizes memory at three abstraction levels: raw trajectories, self-reflected strategies and lessons, and higher-level behavioral patterns. A memory-conditioned self-teacher supervises the student on its own rollouts, enabling progressive internalization of procedural knowledge.

rss · arXiv - AI · Jul 3, 04:00

**Background**: Reinforcement Learning with Verifiable Rewards (RLVR) uses deterministic verification functions (e.g., unit tests) to provide binary reward signals for training language models. Self-Distilled Policy Optimization (SDPO) extends this by using the model itself as a teacher to reflect on its own attempts. However, both methods only leverage signals from individual episodes, missing cross-episode patterns that could improve learning efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.01480">[2607.01480] Procedural Memory Distillation: Online ...</a></li>
<li><a href="https://self-evolving-agents.salesforceresearch.ai/papers/pmd/index.html">Procedural Memory Distillation - Self-Evolving Agents</a></li>
<li><a href="https://github.com/lasgroup/SDPO">GitHub - lasgroup/ SDPO : Reinforcement Learning via Self - Distillation ...</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#language models`, `#self-improvement`, `#distillation`, `#RLVR`

---

<a id="item-17"></a>
## [Grid-Based ANN Scaling Laws Reveal Dimensional Crossover Advantage](https://arxiv.org/abs/2607.01283) ⭐️ 8.0/10

A new study systematically characterizes a multiprobe grid algorithm for approximate nearest neighbor (ANN) search, revealing a dimensional scaling crossover on GloVe embeddings where grid search maintains constant scaling while graph/tree methods degrade. This work fills a gap in modern ANN scaling analyses and suggests grid-based methods could be competitive in high-dimensional or rebuild-heavy settings, with implications for efficient transformer architectures where self-attention is formalized as ANN. The multiprobe grid algorithm shows near-linear query scaling in dataset size N and lower indexing cost compared to graph-, tree-, and partitioning-based methods. The code is available at https://github.com/weiz345/MultiProbeANN.

rss · arXiv - Machine Learning · Jul 3, 04:00

**Background**: Approximate nearest neighbor (ANN) search is a fundamental problem in high-dimensional data analysis, with applications in information retrieval, machine learning, and natural language processing. Traditional methods include graph-based, tree-based, and partitioning-based approaches, but grid-based methods have been largely absent from modern scaling studies. The GloVe embedding family is a widely used set of word vectors that serve as a benchmark for high-dimensional search.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.01283">Scaling Laws for Grid-Based Approximate Nearest Neighbor ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/GloVe">GloVe - Wikipedia</a></li>
<li><a href="https://nlp.stanford.edu/projects/glove/">GloVe: Global Vectors for Word Representation</a></li>

</ul>
</details>

**Tags**: `#approximate nearest neighbor`, `#high-dimensional search`, `#scaling laws`, `#grid search`, `#ANN`

---

<a id="item-18"></a>
## [NightVision Attack Recovers LLM Architecture via Restrictive API](https://arxiv.org/abs/2607.01313) ⭐️ 8.0/10

Researchers introduced NightVision, an attack that infers hidden dimension, depth, and parameter count of LLMs using only a single logit per token and time-to-first-token measurements, without requiring logit bias or top-k logits. This work exposes that current restrictive LLM APIs are insufficient to hide architectural details, raising serious security and privacy concerns for model providers and users. NightVision uses a novel common set prompting technique and spectral analysis to estimate hidden dimension with 23% average relative error (9% for MoE models), and estimates depth and parameter count within 53% for models over 3 billion parameters.

rss · arXiv - Machine Learning · Jul 3, 04:00

**Background**: Commercial LLM providers typically do not disclose architectural details. Prior work could recover hidden dimension using top-k logits or logit bias, but many providers have since restricted APIs to a single logit per token and removed logit bias. NightVision overcomes these restrictions by leveraging common set prompting and timing measurements.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.01313">[2607.01313] Black-Box Inference of LLM Architectural ...</a></li>
<li><a href="https://medium.com/@serhatcck/token-level-control-in-openai-models-a-developers-guide-to-logit-bias-6fcc04a8a41f">Understanding Logit Bias in LLMs | Medium</a></li>
<li><a href="https://www.vellum.ai/llm-parameters/logit-bias">Logit Bias - LLM Parameter Guide - Vellum</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#security`, `#model extraction`, `#API`, `#privacy`

---

<a id="item-19"></a>
## [ProvenanceGuard: Detecting LLM Agent Misalignment via Provenance Analysis](https://arxiv.org/abs/2607.01236) ⭐️ 8.0/10

Researchers introduced ProvenanceGuard, a multi-stage pipeline that uses provenance analysis to detect misalignment in LLM agent tool invocations before execution, reducing error rates from 42.9% to 1.8% on Agent-SafetyBench. This work addresses a critical safety issue in LLM agents by providing a systematic, auditable framework for detecting misalignment, outperforming existing LLM-as-a-judge methods and reducing unnecessary interventions. ProvenanceGuard formalizes misalignment detection as checking whether a tool call is supported by traceable evidence in the agent's context, and it evaluates three types of misalignment across 10 backbone LLMs on two benchmarks.

rss · arXiv - NLP · Jul 3, 04:00

**Background**: LLM agents are AI systems that can invoke external tools to perform tasks, but their actions may deviate from user intent, a phenomenon called misalignment. Existing runtime guardrails often rely on an LLM-as-a-judge approach, which lacks systematic reasoning and can produce inconsistent judgments. Provenance analysis, originally used in data management, traces the origin and derivation of information to verify its authenticity and support.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2407.11843v4">Preemptive Detection and Correction of Misaligned Actions in LLM ...</a></li>
<li><a href="https://leanware.co/insights/llm-guardrails">LLM Guardrails: Strategies & Best Practices in 2025</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#AI safety`, `#alignment`, `#provenance analysis`, `#runtime guardrails`

---

<a id="item-20"></a>
## [Kara: Sliding-Window KV Cache Compression for Efficient LLM Serving](https://arxiv.org/abs/2607.01237) ⭐️ 8.0/10

Kara introduces a sliding-window KV cache compression method that compresses only the recently generated context during decoding, using bidirectional attention to score and select informative KV pairs, and a Token2Chunk module to expand selected pairs into flexible chunks. This addresses a critical bottleneck in serving reasoning LLMs that generate long chain-of-thought sequences, where the KV cache grows large and causes high latency and low throughput. By reducing memory usage and improving throughput, Kara enables more efficient deployment of reasoning models. Kara adapts to PagedAttention and is built upon vLLM as the KvLLM inference framework. It overcomes limitations of existing threshold-triggered compression policies that may reduce throughput or lose information, and rigid chunk boundaries that fail to preserve flexible-sized chunks.

rss · arXiv - NLP · Jul 3, 04:00

**Background**: Large language models (LLMs) use a key-value (KV) cache to avoid recomputing attention states during token generation, but the cache grows linearly with sequence length. Reasoning models that generate long chain-of-thought (CoT) sequences accumulate massive KV caches, leading to high decoding latency and limited throughput. Existing KV cache compression methods use threshold-triggered policies or fixed-size chunks, which can be inefficient or lose important information.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2607.01237v1">Kara: Efficient Reasoning LLM Serving via Sliding-Window KV ...</a></li>
<li><a href="https://arxiv.org/abs/2405.06219">[2405.06219] SKVQ: Sliding-window Key and Value Cache ...</a></li>
<li><a href="https://arxiv.org/pdf/2603.01426">Understanding the Physics of Key-Value Cache Compression for...</a></li>

</ul>
</details>

**Tags**: `#LLM serving`, `#KV cache compression`, `#efficiency`, `#reasoning models`

---

<a id="item-21"></a>
## [Prompt Framing Inflates LLM Error Detection F1 Scores](https://arxiv.org/abs/2607.01240) ⭐️ 8.0/10

A new paper reveals that count-based F1 scores for LLM error detection can be artificially inflated by prompt framing without improving actual span localization, and introduces ErrorBench, a stress-test protocol to measure this distortion. This finding undermines the reliability of count-based F1 as a standalone metric for LLM error detection, urging the NLP community to adopt span-aware metrics and avoid pre-populated error counts in evaluations. Using ErrorBench on six LLMs with 4,290 responses from CoNLL-2014, anchored prompts caused up to 0.79 F1 inflation under M2 scoring and 0.96 under strict matching; a 100-passage replication with ERRANT 3.0.0 showed a +0.21 Count-F1 increase but only +0.04 multi-reference ERRANT F0.5 increase.

rss · arXiv - NLP · Jul 3, 04:00

**Background**: Count-based F1 is commonly used to evaluate LLM error detection, but it only measures the number of correctly identified errors, not their exact locations. Prompt framing, such as providing an expected error count (numeric anchoring), can bias LLMs to output more errors, inflating F1 without improving localization. ErrorBench is a controlled protocol designed to isolate this inflation effect.

<details><summary>References</summary>
<ul>
<li><a href="https://aipulselab.tech/news/prompt-framing-distorts-count-based-evaluation-of-llm-error-detection-evidence-from-numeric-anchoring-2641b4">Prompt Framing Distorts Count-Based Evaluation of LLM Error ...</a></li>
<li><a href="https://nlptoolbox.cl.cam.ac.uk/errant/">ERRANT - University of Cambridge</a></li>

</ul>
</details>

**Tags**: `#LLM evaluation`, `#error detection`, `#prompt engineering`, `#NLP benchmarking`, `#F1 inflation`

---

<a id="item-22"></a>
## [First Benchmark for LLM Office File Comprehension](https://arxiv.org/abs/2607.01245) ⭐️ 8.0/10

Researchers introduced Office Comprehension Bench (OCB), the first public benchmark to evaluate LLM comprehension of native Office file formats (.docx, .xlsx, .pptx) across Word, Excel, and PowerPoint. Even the strongest frontier model achieves only about 59.3% accuracy on the Domain Q&A track. This benchmark addresses a critical gap in evaluating real-world document understanding, as LLMs are increasingly used to process office documents. The low accuracy highlights significant limitations in current models, driving improvements for enterprise AI applications. OCB includes two tracks: File Fidelity Q&A tests structural and visual perception of office artifacts, while Domain Q&A tests expert-level reasoning across 12 professional domains. Reference answers are decomposed into atomic claims, and an ensemble of LLM judges scores responses independently.

rss · arXiv - NLP · Jul 3, 04:00

**Background**: LLMs have been evaluated on various benchmarks for text comprehension, but few test understanding of native Office file formats, which contain complex structures like tables, charts, and embedded objects. OCB fills this gap by providing a standardized evaluation across Word, Excel, and PowerPoint documents. The benchmark uses atomic claim decomposition and LLM judge ensembles to ensure reliable scoring.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.01245">[2607.01245] Office Comprehension Benchmark - arXiv.org</a></li>
<li><a href="https://github.com/microsoft/OfficeComprehensionBench">GitHub - microsoft/OfficeComprehensionBench</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#benchmark`, `#office documents`, `#AI evaluation`, `#document understanding`

---

<a id="item-23"></a>
## [MapDreamer: Aerial Imagery to Lane-Level Maps via Diffusion](https://arxiv.org/abs/2607.01370) ⭐️ 8.0/10

MapDreamer introduces a latent diffusion model conditioned on aerial imagery to generate lane-level vector maps with explicit topology for autonomous driving, outperforming non-generative baselines on the UrbanLaneGraph dataset. This work addresses the labor-intensive process of high-definition map generation, which is critical for autonomous driving, by enabling automatic synthesis of lane-level maps from single aerial images, potentially reducing cost and scaling map coverage. The model uses a variational autoencoder to learn a compact latent representation of lane centerlines and topology, a transformer-based latent diffusion model for graph prediction, and introduces ghost lane latents to handle variable lane counts and sliding-window aggregation for city-scale mapping.

rss · arXiv - Computer Vision · Jul 3, 04:00

**Background**: High-definition (HD) maps are essential for autonomous driving but are costly to create manually. Lane-level vector maps represent road geometry and connectivity precisely. Latent diffusion models (LDMs) are generative models that denoise in a compressed latent space, enabling high-quality image synthesis. MapDreamer adapts LDMs to structured graph generation for lane maps.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Latent_diffusion_model">Latent diffusion model</a></li>
<li><a href="https://arxiv.org/pdf/2406.14255">DuMapNet: An End-to-End Vectorization System for City-Scale ...</a></li>

</ul>
</details>

**Tags**: `#autonomous driving`, `#diffusion models`, `#map generation`, `#computer vision`, `#deep learning`

---

<a id="item-24"></a>
## [G-CBM: Unsupervised Concept-Graph for Visual Explanations](https://arxiv.org/abs/2607.01416) ⭐️ 8.0/10

Researchers propose G-CBM, an intrinsically interpretable framework that uses Non-negative Matrix Factorization (NMF) for unsupervised concept discovery and Graph Attention Networks (GAT) for concept-level reasoning, achieving an average relative AUC improvement of 3.7% over ResNet-50 on multiple benchmarks. This work addresses key limitations of existing Concept Bottleneck Models (CBMs), such as reliance on predefined concepts and lack of spatial reasoning, making interpretable AI more practical for high-stakes domains like medical imaging. G-CBM introduces a tunable concept filtering threshold τ to suppress weak region-level features, and uses per-image concept-graphs to capture spatial recurrence and inter-concept dependencies. On dermoscopy benchmarks, it achieves competitive performance with supervised approaches without requiring external annotations.

rss · arXiv - Computer Vision · Jul 3, 04:00

**Background**: Concept Bottleneck Models (CBMs) are a class of interpretable models that first predict human-understandable concepts and then use those concepts to make final predictions. However, traditional CBMs often require predefined concept vocabularies or supervised annotations, and they typically summarize each concept with a single image-level score, ignoring spatial patterns. Non-negative Matrix Factorization (NMF) is an unsupervised method that factorizes a matrix into non-negative components, useful for discovering latent features. Graph Attention Networks (GATs) are neural networks that operate on graph-structured data, learning to weigh the importance of neighboring nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Non-negative_matrix_factorization">Non-negative matrix factorization - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2607.01416v1">Beyond Heatmaps: Unsupervised Concept-Graph Reasoning for ...</a></li>
<li><a href="https://www.mdpi.com/1999-5903/16/9/318">Graph Attention Networks: A Comprehensive Review of Methods ...</a></li>

</ul>
</details>

**Tags**: `#interpretability`, `#concept bottleneck model`, `#graph neural network`, `#unsupervised learning`, `#computer vision`

---

<a id="item-25"></a>
## [LF-IBIS: Full Bayesian RL Without Likelihood](https://arxiv.org/abs/2607.01741) ⭐️ 8.0/10

Researchers propose LF-IBIS, a novel algorithm that combines Approximate Bayesian Computation with Iterated Batch Importance Sampling to perform full Bayesian reinforcement learning in environments without explicit likelihood functions. This work addresses a key limitation of Bayesian RL by enabling likelihood-free inference, making it applicable to real-world problems where environment dynamics are intractable or unknown. It also provides uncertainty quantification over policies, aiding exploration-exploitation trade-offs. LF-IBIS updates beliefs online as new interactions occur, yielding approximate posterior distributions over both environment parameters and optimal policies. The method was validated on a clinical trial simulation where closed-form posteriors exist, and on settings with no closed-form posteriors.

rss · arXiv - Data Science & Statistics · Jul 3, 04:00

**Background**: Bayesian Reinforcement Learning (BRL) uses prior knowledge and sequential belief updates to handle data scarcity, but most BRL methods require an explicit likelihood function, which is often unavailable in practice. Approximate Bayesian Computation (ABC) bypasses likelihood evaluation by comparing simulated data to observed data, while Iterated Batch Importance Sampling (IBIS) sequentially updates posterior distributions over parameters. LF-IBIS merges these techniques to enable BRL without likelihoods.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Approximate_Bayesian_computation">Approximate Bayesian computation</a></li>
<li><a href="https://arxiv.org/abs/1101.1528">[1101.1528] SMC^2: an efficient algorithm for sequential ... SMC2: an efficient algorithm for sequential analysis of state ... Full Bayesian Reinforcement Learning via LF-IBIS - arXiv.org Iterated and Sequential Importance Sampling - Springer R: Logistic regression iterated batch importance sampling SMC2: an efficient algorithm for sequential analysis of state ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-1-4757-4145-2_14">Iterated and Sequential Importance Sampling - Springer</a></li>

</ul>
</details>

**Tags**: `#reinforcement learning`, `#bayesian inference`, `#likelihood-free`, `#approximate bayesian computation`, `#importance sampling`

---

<a id="item-26"></a>
## [Shallow NNs Reformulated as Well-Posed Continuum Problem](https://arxiv.org/abs/2607.02003) ⭐️ 8.0/10

This paper introduces a variational formulation for shallow neural networks that replaces the discrete training problem with a well-posed continuum problem over parameter densities in weighted Sobolev spaces, proving global well-posedness, stability, and almost C^3 regularity. This work could fundamentally change how shallow neural networks are optimized by enabling direct solution via a single linear system, bypassing iterative stochastic methods, and it bridges the gap between NTK and feature-learning regimes with rigorous generalization guarantees. The paper identifies a family of λ-convex functionals over parameter densities and proves that the optimal density can be obtained by solving a single linear system, with generalization error controlled at a rate of 1/α and finite-width networks of size N achieving the continuum optimum at O(1/N) rate.

rss · arXiv - Data Science & Statistics · Jul 3, 04:00

**Background**: Traditional neural network training involves optimizing a non-convex loss landscape using stochastic gradient descent, which lacks theoretical guarantees. Variational methods and mean-field approaches have been explored but often face regularity and discretization issues. This work leverages weighted Sobolev spaces and elliptic regularity to provide a well-posed continuum surrogate.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_function">Convex function - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/math/0703725">Weighted Sobolev spaces and embedding theorems</a></li>
<li><a href="https://en.wikipedia.org/wiki/Elliptic_operator">Elliptic operator - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#neural networks`, `#variational methods`, `#optimization theory`, `#deep learning theory`

---

<a id="item-27"></a>
## [New Framework Links Conformal Prediction to Counterfactual Decisions](https://arxiv.org/abs/2607.02206) ⭐️ 8.0/10

A new arXiv paper introduces policy-coupled coverage, a decision-theoretic concept that bridges conformal prediction and counterfactual decision-making, and proposes a two-stage procedure called PC-RACP that approximates optimal prediction sets with finite-sample guarantees. This work addresses a critical gap between uncertainty quantification and decision optimality in high-stakes settings like treatment selection and policy-making, where the outcome depends on the action taken. The proposed framework ensures both statistical validity and utility, potentially improving reliability of AI-driven decisions. The paper shows that optimizing prediction sets under policy-coupled coverage is equivalent to both universal-coverage formulation and direct risk-averse optimization over policies. The PC-RACP procedure is validated through simulations and a real email-marketing experiment, demonstrating higher utility than existing methods while maintaining valid coverage.

rss · arXiv - Data Science & Statistics · Jul 3, 04:00

**Background**: Conformal prediction is a distribution-free method for uncertainty quantification that produces prediction sets with guaranteed coverage under exchangeability. Counterfactual decisions involve choosing actions whose outcomes depend on the action itself, creating a feedback loop between uncertainty and decision rules. The paper introduces policy-coupled coverage to capture this interdependence.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.02206">Prediction Sets for Counterfactual Decisions: Coverage ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>

</ul>
</details>

**Tags**: `#conformal prediction`, `#counterfactual decisions`, `#uncertainty quantification`, `#decision theory`, `#causal inference`

---

<a id="item-28"></a>
## [Device Revives Donor Eyes, Paving Way for Transplants](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) ⭐️ 8.0/10

Researchers have developed a portable device called eye-ECMO that pumps oxygenated blood mixed with a unique solution into donor eyes to keep them viable after removal, potentially enabling successful whole-eye transplants. Whole-eye transplantation has been a long-standing challenge due to rapid degeneration of donor eyes; this device could restore sight to blind individuals by preserving the eye's function until transplantation. The eye-ECMO device was developed by University of Miami researchers and is designed to be portable. It addresses the critical issue of donor eye viability, which previously limited whole-eye transplant success.

rss · MIT Technology Review · Jul 3, 17:34

**Background**: Whole-eye transplantation involves transplanting an entire donor eye, including the optic nerve, into a recipient. Previous attempts failed because donor eyes degenerate quickly after removal, and the optic nerve must be regenerated for vision. The eye-ECMO device keeps the eye alive ex vivo, similar to how ECMO supports heart and lung function.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/">A device that revives eyeballs from dead donors could make ...</a></li>
<li><a href="https://news.med.miami.edu/paving-the-way-for-human-eye-transplants/">Paving the Way for Human Eye Transplants - InventUM</a></li>
<li><a href="https://superinnovators.com/2025/08/paving-the-way-for-human-eye-transplants/">Paving the way for human eye transplants - Super Innovators</a></li>

</ul>
</details>

**Tags**: `#biotechnology`, `#organ transplantation`, `#medical device`, `#ophthalmology`

---