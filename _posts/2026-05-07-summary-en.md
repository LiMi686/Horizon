---
layout: default
title: "Horizon Summary: 2026-05-07 (EN)"
date: 2026-05-07
lang: en
---

> From 95 items, 36 important content pieces were selected

---

1. [Dirtyfrag: Universal Linux LPE Exploit Released](#item-1) ⭐️ 9.0/10
2. [Anthropic Releases Natural Language Autoencoders for LLM Interpretability](#item-2) ⭐️ 9.0/10
3. [Mozilla Hardens Firefox with Claude Mythos, Fixing 423 Bugs](#item-3) ⭐️ 9.0/10
4. [PyTorch: Foundational Deep Learning Framework](#item-4) ⭐️ 9.0/10
5. [Formally Verified LLM Agent for Autonomous Cyber Defense](#item-5) ⭐️ 9.0/10
6. [Triton v3.7.0 Adds Scaled BMM, FP8 Constants, and New Ops](#item-6) ⭐️ 8.0/10
7. [Agents need control flow, not more prompts](#item-7) ⭐️ 8.0/10
8. [AlphaEvolve: Gemini-powered coding agent scales impact](#item-8) ⭐️ 8.0/10
9. [AI Slop Eroding Trust in Online Communities](#item-9) ⭐️ 8.0/10
10. [DeepSeek 4 Flash Local Inference Engine for Apple Metal](#item-10) ⭐️ 8.0/10
11. [Chrome removes on-device AI privacy claim](#item-11) ⭐️ 8.0/10
12. [Motherboard sales collapse 25% as AI chip production takes priority](#item-12) ⭐️ 8.0/10
13. [Agent Skills: Production-Grade Engineering for AI Coders](#item-13) ⭐️ 8.0/10
14. [TabPFN: Foundation Model for Tabular Data](#item-14) ⭐️ 8.0/10
15. [DocuSeal: Open-Source DocuSign Alternative](#item-15) ⭐️ 8.0/10
16. [Ladybird: A Truly Independent Web Browser in Pre-Alpha](#item-16) ⭐️ 8.0/10
17. [Kronos: Open-Source Foundation Model for Financial Markets](#item-17) ⭐️ 8.0/10
18. [ByteDance Open-Sources DeerFlow 2.0 SuperAgent Framework](#item-18) ⭐️ 8.0/10
19. [CreativityBench: Benchmarking LLM Creative Tool Use via Affordances](#item-19) ⭐️ 8.0/10
20. [Worker-Centered AI Adoption: Bridging Organizational Goals and User Needs](#item-20) ⭐️ 8.0/10
21. [Programmatic Context Augmentation for LLM Symbolic Regression](#item-21) ⭐️ 8.0/10
22. [Learning Correct Behavior from Few Traces](#item-22) ⭐️ 8.0/10
23. [Terminus-4B: Small Model Matches Frontier LLMs in Agentic Tasks](#item-23) ⭐️ 8.0/10
24. [Stop Automating Peer Review Without Rigorous Evaluation](#item-24) ⭐️ 8.0/10
25. [ADAPTS: Agentic LLM Framework for Automated Mental Health Assessment](#item-25) ⭐️ 8.0/10
26. [Scalar-Irreducible Dynamics Enable Endogenous Regime Switching](#item-26) ⭐️ 8.0/10
27. [MetaAdamW: Self-Attention for Adaptive Learning Rates and Weight Decay](#item-27) ⭐️ 8.0/10
28. [Task Encoding in LLMs Is Distributed, Not Localized](#item-28) ⭐️ 8.0/10
29. [LLMs Show Bias in Conflict Monitoring](#item-29) ⭐️ 8.0/10
30. [MedFabric & ETHER: Detecting Word-Level Fabrications in Medical LLMs](#item-30) ⭐️ 8.0/10
31. [Nsanku Benchmarks LLMs for Ghanaian Language Translation](#item-31) ⭐️ 8.0/10
32. [MLLMs Show Large Benchmark-to-Bedside Gap in Dermatology](#item-32) ⭐️ 8.0/10
33. [Deep learning fails on scientific images despite richer data](#item-33) ⭐️ 8.0/10
34. [Entropic RNOT Unifies Regularization and Neural OT on Manifolds](#item-34) ⭐️ 8.0/10
35. [Adam vs SGD: Provable Tradeoffs in Nonstationary Optimization](#item-35) ⭐️ 8.0/10
36. [Perturbation Training Boosts LLM Extrapolation](#item-36) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Dirtyfrag: Universal Linux LPE Exploit Released](https://www.openwall.com/lists/oss-security/2026/05/07/8) ⭐️ 9.0/10

A new Linux local privilege escalation exploit called Dirtyfrag has been publicly released, leveraging a page-cache write vulnerability in the xfrm-ESP subsystem. The exploit is claimed to work universally across all major Linux distributions, and no patches or CVEs exist because the embargo was broken. This vulnerability poses a critical threat to Linux system security, as it allows any local user to gain root privileges without authentication. The broken embargo means systems remain exposed until distributions develop and deploy their own mitigations. The exploit shares the same sink (page-cache write) as the previous Copy Fail vulnerability but reaches it through a different path—xfrm-ESP network sockets instead of AF_ALG. The researcher notes that the root cause similarity to Copy Fail highlights the failure to properly fix the underlying issue.

hackernews · flipped · May 7, 19:21 · [Discussion](https://news.ycombinator.com/item?id=48053623)

**Background**: Local privilege escalation (LPE) vulnerabilities allow an attacker with limited user access to gain full root control of a system. The xfrm-ESP subsystem in the Linux kernel handles IPsec ESP (Encapsulating Security Payload) traffic. A page-cache write vulnerability occurs when the kernel writes data to the page cache without proper validation, potentially enabling out-of-bounds writes. The Copy Fail vulnerability (CVE-2026-31431) was a similar LPE exploit that used the AF_ALG crypto interface.

<details><summary>References</summary>
<ul>
<li><a href="https://copy.fail/">Copy Fail — CVE-2026-31431</a></li>

</ul>
</details>

**Discussion**: Community comments express concern over the broken embargo and lack of patches, with some users noting that the exploit failed to run on a default Ubuntu container. One commenter highlights the similarity to Copy Fail and criticizes the reliance on AI for vulnerability research, arguing it hinders creative exploration. Another points out that the underlying issue in authencesn was not fixed after Copy Fail, leading to this new exploit.

**Tags**: `#Linux`, `#privilege escalation`, `#vulnerability`, `#exploit`, `#security`

---

<a id="item-2"></a>
## [Anthropic Releases Natural Language Autoencoders for LLM Interpretability](https://www.anthropic.com/research/natural-language-autoencoders) ⭐️ 9.0/10

Anthropic has released open-weight Natural Language Autoencoders (NLAs) that can translate internal activations of large language models (including Qwen 2.5 7B, Gemma 3 12B/27B, and Llama 3.3 70B) into human-readable natural language text. This is a major step forward in mechanistic interpretability, allowing researchers to directly read what a model is 'thinking' rather than relying on post-hoc explanations. It also marks Anthropic's deeper engagement with the open-source community by releasing weights on Hugging Face. The NLA consists of a 'verbalizer' that maps activations to text and a 'reconstructor' that inverts the text back to activations, trained end-to-end. Notably, the objective does not enforce human readability, so the verbalizer could theoretically invent its own language, but in practice it produces coherent English.

hackernews · instagraham · May 7, 17:54 · [Discussion](https://news.ycombinator.com/item?id=48052537)

**Background**: Autoencoders are neural networks that learn efficient representations of data by encoding inputs into a latent space and then decoding them back. In mechanistic interpretability, researchers aim to understand the internal computations of LLMs by analyzing their activations—the intermediate vectors produced during inference. Prior work often required complex probes or manual inspection; NLAs offer a more direct and scalable approach.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/research/natural-language-autoencoders">Natural Language Autoencoders: Turning Claude’s thoughts into text</a></li>

</ul>
</details>

**Discussion**: The community is highly enthusiastic, with many praising the open-weight release and the potential for interpretability. Some commenters note that the approach could be used for activation steering, and others recommend reading the detailed Transformer Circuits blog post for deeper understanding. A few express skepticism about whether the generated text truly reflects the model's internal reasoning.

**Tags**: `#interpretability`, `#AI safety`, `#open-source`, `#LLM`, `#Anthropic`

---

<a id="item-3"></a>
## [Mozilla Hardens Firefox with Claude Mythos, Fixing 423 Bugs](https://simonwillison.net/2026/May/7/firefox-claude-mythos/#atom-everything) ⭐️ 9.0/10

Mozilla used the Claude Mythos preview to find and fix hundreds of vulnerabilities in Firefox, with the number of monthly security fixes jumping from around 20-30 to 423 in April 2026. This demonstrates a major leap in AI-assisted security auditing, showing that advanced models combined with improved techniques can transform AI-generated bug reports from 'unwanted slop' into highly effective vulnerability discovery. The bugs found include a 20-year-old XSLT bug and a 15-year-old bug in the <legend> element; many attempts were blocked by Firefox's existing defense-in-depth measures.

rss · Simon Willison · May 7, 17:56

**Background**: Claude Mythos is Anthropic's most advanced large language model, released in preview in 2026 to select companies but not to the public. Mozilla's success came from a combination of more capable models and improved techniques for steering, scaling, and filtering AI-generated security reports.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos_Preview">Claude Mythos Preview</a></li>

</ul>
</details>

**Discussion**: The Lobste.rs discussion highlighted the dramatic shift from AI-generated bug reports being noise to becoming highly valuable, with many commenters impressed by the scale and effectiveness of the approach.

**Tags**: `#AI`, `#security`, `#Firefox`, `#vulnerability`, `#Mozilla`

---

<a id="item-4"></a>
## [PyTorch: Foundational Deep Learning Framework](https://github.com/pytorch/pytorch) ⭐️ 9.0/10

The PyTorch GitHub repository continues to serve as the central hub for the open-source deep learning framework, providing tensor computation with GPU acceleration and dynamic neural networks via a tape-based autograd system. PyTorch is one of the most widely adopted deep learning frameworks, powering countless research projects and production systems. Its continued development and community support are critical for advancing AI and machine learning. PyTorch offers a GPU-ready tensor library, dynamic neural networks built on a tape-based autograd system, and a Python-first design that integrates seamlessly with NumPy, SciPy, and Cython. It supports NVIDIA CUDA, AMD ROCm, and Intel GPU backends.

rss · GitHub Trending - Python · May 7, 23:10

**Background**: PyTorch is an open-source machine learning library developed primarily by Meta AI. Its tape-based autograd system records operations during the forward pass to build a computational graph, enabling automatic differentiation for training neural networks. Tensor computation with GPU acceleration allows efficient processing of large-scale data.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/pytorch/pytorch">GitHub - pytorch/pytorch: Tensors and Dynamic neural networks in Python with strong GPU acceleration · GitHub</a></li>
<li><a href="https://stackoverflow.com/questions/64856195/what-is-tape-based-autograd-in-pytorch">python - What is tape - based autograd in Pytorch? - Stack Overflow</a></li>
<li><a href="https://www.nvidia.com/en-us/data-center/tensor-cores/">NVIDIA Tensor Cores: Versatility for HPC & AI</a></li>

</ul>
</details>

**Tags**: `#deep learning`, `#pytorch`, `#python`, `#gpu`, `#neural networks`

---

<a id="item-5"></a>
## [Formally Verified LLM Agent for Autonomous Cyber Defense](https://arxiv.org/abs/2605.03034) ⭐️ 9.0/10

Researchers propose a tool-mediated LLM architecture for autonomous cyber defense, with formal stability guarantees machine-checked in Lean 4 on 282 real enterprise attack graphs. This work is the first to combine formal verification with LLM agents for high-stakes cybersecurity, offering provable controllability and robustness against adversarial disturbances, which could transform SOC operations and AI safety. The architecture uses deterministic tools (Stackelberg best-response, Bayesian updates, attack-graph primitives) and finite action catalogs enforced at the tool-output interface, with a composite Lyapunov function certifying ISS stability in Lean 4 with zero 'sorry'.

rss · arXiv - AI · May 7, 04:00

**Background**: Input-to-State Stability (ISS) is a control-theoretic property ensuring a system remains bounded under bounded external inputs. Lean 4 is a proof assistant used for formal verification of mathematical theorems and software correctness. Stackelberg games model strategic interactions where a leader (defender) commits to a strategy before a follower (attacker) responds.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Input-to-state_stability">Input - to - state stability - Wikipedia</a></li>
<li><a href="https://onlinelibrary.wiley.com/doi/10.1155/2023/2811038">Stackelberg Security Game for Optimizing Cybersecurity Decisions in Cloud Computing - Ait Temghart - 2023 - Security and Communication Networks - Wiley Online Library</a></li>

</ul>
</details>

**Tags**: `#LLM agents`, `#cyber defense`, `#formal verification`, `#autonomous systems`, `#AI safety`

---

<a id="item-6"></a>
## [Triton v3.7.0 Adds Scaled BMM, FP8 Constants, and New Ops](https://github.com/triton-lang/triton/releases/tag/v3.7.0) ⭐️ 8.0/10

Triton v3.7.0 introduces scaled batched matrix multiply (scaled BMM), direct FP8 constant creation, and new tensor operations like tl.squeeze and tl.unsqueeze. The release also includes significant backend improvements for NVIDIA and AMD GPUs, as well as enhanced profiling and testing infrastructure. Scaled BMM and FP8 support are critical for efficient large language model training and inference, directly addressing the needs of AI practitioners. These features enable higher performance and lower memory usage, making Triton an even more compelling alternative to hand-tuned CUDA kernels. The scaled BMM feature allows scaling factors to be applied per batch, which is useful for quantization-aware training. FP8 constants can now be created directly in Triton kernels without workarounds, supporting both E4M3 and E5M2 formats. The release also includes a non-reordering variant of tl.cat with broadcast support.

github · atalman · May 7, 22:19

**Background**: Triton is an open-source compiler and language for GPU programming, developed by OpenAI, that allows users to write efficient GPU kernels in Python-like syntax. It compiles to optimized code for NVIDIA and AMD GPUs, often matching or exceeding the performance of hand-written CUDA. Scaled batched matrix multiply is a key operation in modern deep learning, especially for transformer models with grouped query attention or quantization. FP8 is a low-precision floating-point format gaining traction for accelerating training and inference while reducing memory footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/triton-lang/triton">GitHub - triton - lang / triton : Development repository for the Triton...</a></li>
<li><a href="https://openai.com/index/triton/">Introducing Triton : Open-source GPU programming for neural... | OpenAI</a></li>
<li><a href="https://rocm.blogs.amd.com/software-tools-optimization/kernel-development-optimizations-with-triton-on-/README.html">Unlock Peak Performance on AMD GPUs with Triton Kernel ...</a></li>

</ul>
</details>

**Tags**: `#triton`, `#gpu`, `#compiler`, `#machine learning`, `#release`

---

<a id="item-7"></a>
## [Agents need control flow, not more prompts](https://bsuh.bearblog.dev/agents-need-control-flow/) ⭐️ 8.0/10

A blog post argues that effective AI agents should rely on structured control flow rather than improved prompts, based on practical experience building a QA agent that processes hundreds of markdown files. This challenges the prevailing focus on prompt engineering and suggests a shift toward deterministic, code-driven agent architectures, which could lead to more reliable and scalable AI systems in production. The author describes a QA agent that must run through 200 markdown files in a browser session, and found that prompt improvements hit a limit, requiring explicit control flow for reliable execution.

hackernews · bsuh · May 7, 16:43 · [Discussion](https://news.ycombinator.com/item?id=48051562)

**Background**: AI agents are software systems that use large language models (LLMs) to perform tasks autonomously. Control flow refers to the structured sequence of steps (e.g., loops, conditionals) that govern an agent's behavior, as opposed to relying solely on natural language prompts to guide the LLM.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PrefectHQ/ControlFlow">GitHub - prefect-archive/ControlFlow: 🦾 Take control of your AI agents</a></li>
<li><a href="https://www.prefect.io/blog/controlflow-intro">Introducing ControlFlow</a></li>
<li><a href="https://ai-sdk.dev/docs/agents/overview">Agents: Overview</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree, with some suggesting that LLMs should be used to write deterministic code at design time rather than at runtime. Others note that the misapplication of LLMs for tasks better suited to traditional software is a core issue.

**Tags**: `#AI agents`, `#control flow`, `#LLM`, `#software engineering`, `#prompt engineering`

---

<a id="item-8"></a>
## [AlphaEvolve: Gemini-powered coding agent scales impact](https://deepmind.google/blog/alphaevolve-impact/) ⭐️ 8.0/10

Google DeepMind unveiled AlphaEvolve in May 2025, an evolutionary coding agent powered by Gemini 2.0 LLMs that autonomously discovers and optimizes algorithms across scientific and algorithmic domains. AlphaEvolve demonstrates AI's ability to improve its own infrastructure, potentially accelerating progress in fields like mathematics, physics, and computer science by automating algorithm design. AlphaEvolve uses an evolutionary approach combined with Gemini LLMs to generate and refine code, achieving state-of-the-art results on benchmark problems including Erdős problems.

hackernews · berlianta · May 7, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48050278)

**Background**: Large language models (LLMs) like Gemini are known to be hit-and-miss at coding. AlphaEvolve leverages an evolutionary loop where the LLM proposes code variations, tests them, and iteratively improves, similar to how AlphaZero mastered games through self-play.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AlphaEvolve">AlphaEvolve - Wikipedia</a></li>
<li><a href="https://www.unite.ai/alphaevolve-google-deepminds-groundbreaking-step-toward-agi/">AlphaEvolve: Google DeepMind’s Groundbreaking Step Toward AGI</a></li>
<li><a href="https://www.technologyreview.com/2025/05/14/1116438/google-deepminds-new-ai-uses-large-language-models-to-crack-real-world-problems/">Google DeepMind’s new AI agent cracks real-world problems better than humans can | MIT Technology Review</a></li>

</ul>
</details>

**Discussion**: Commenters debated the significance, with some comparing it to Antirez's work on Redis optimization and others questioning whether Google employees prefer Gemini over Claude Code or Codex. Some expressed frustration with Gemini API availability and capacity issues.

**Tags**: `#AI`, `#coding agent`, `#optimization`, `#Google DeepMind`, `#LLM`

---

<a id="item-9"></a>
## [AI Slop Eroding Trust in Online Communities](https://rmoff.net/2026/05/06/ai-slop-is-killing-online-communities/) ⭐️ 8.0/10

AI-generated content, often called 'slop,' is increasingly infiltrating online communities, with users reporting that bots can now engage in indistinguishable conversations, leading to a decline in authentic human interaction. This erosion of trust threatens the very foundation of online communities, making it harder for genuine users to connect and share knowledge, and potentially driving people away from digital platforms altogether. One user's experiment showed an AI agent could karma farm and covertly advertise on Reddit without detection, while a community moderator reports banning around 600 AI-generated content creator accounts monthly.

hackernews · thm · May 7, 18:46 · [Discussion](https://news.ycombinator.com/item?id=48053203)

**Background**: Online communities rely on trust and authentic human interaction. AI-generated content, powered by large language models (LLMs), can now mimic human writing so convincingly that it's hard to distinguish from real users, leading to concerns about spam, manipulation, and loss of community value.

**Discussion**: Commenters express a mix of fear and resignation, with some suggesting that the problem may drive humans back to real-world interactions. Others highlight the immense effort required to moderate AI content, fearing the battle is being lost.

**Tags**: `#AI`, `#online communities`, `#content moderation`, `#LLMs`, `#social media`

---

<a id="item-10"></a>
## [DeepSeek 4 Flash Local Inference Engine for Apple Metal](https://github.com/antirez/ds4) ⭐️ 8.0/10

Antirez released ds4, a focused local inference engine for DeepSeek-V4-Flash optimized for Apple Metal on Apple Silicon Macs. The engine achieves full-speed token generation with energy usage peaking at 50W on an M3 Max MacBook. This project demonstrates that large Mixture-of-Experts models like DeepSeek-V4-Flash (284B total parameters) can run efficiently on consumer hardware, potentially enabling privacy-preserving local AI without cloud dependency. It also showcases the value of focused optimization for a single model, which could inspire similar efforts for other open-source models. DeepSeek-V4-Flash is a Mixture-of-Experts model with 284B total parameters and 13B activated, supporting a 1M-token context window. The ds4 engine is optimized for Apple Metal, but the model's enormous size means loading large contexts can take minutes, and the engine currently only supports this specific model.

hackernews · tamnd · May 7, 15:40 · [Discussion](https://news.ycombinator.com/item?id=48050751)

**Background**: DeepSeek-V4-Flash is a preview of the DeepSeek-V4 series, a Mixture-of-Experts (MoE) language model designed for efficient reasoning. Apple Metal is Apple's GPU-accelerated compute framework for Mac, enabling high-performance inference on Apple Silicon. Local inference engines like ds4 allow running large language models entirely on-device, avoiding cloud costs and privacy concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash">DeepSeek V4 Flash - API Pricing & Providers | OpenRouter</a></li>
<li><a href="https://ollama.com/library/deepseek-v4-flash">deepseek-v4-flash</a></li>

</ul>
</details>

**Discussion**: The community expressed excitement about the project, with users noting the impressive energy efficiency (50W peak) and the value of focused optimization. Some pointed out practical limitations: the model is still enormous, and reading large contexts can be slow. Others appreciated the educational simplicity compared to larger frameworks.

**Tags**: `#local-llm`, `#deepseek`, `#apple-silicon`, `#inference-optimization`, `#open-source`

---

<a id="item-11"></a>
## [Chrome removes on-device AI privacy claim](https://old.reddit.com/r/chrome/comments/1t5qayz/chrome_removes_claim_of_ondevice_al_not_sending/) ⭐️ 8.0/10

Google Chrome removed a statement that on-device AI does not send data to Google servers, raising concerns about data collection in AI features. This change affects billions of Chrome users and could undermine trust in on-device AI privacy, especially as Chrome silently downloads large AI models without clear consent. The removal was noticed on Reddit, and recent reports show Chrome downloads a 4GB AI model (Gemini Nano) without user consent, potentially violating EU privacy laws.

hackernews · newsoftheday · May 7, 15:56 · [Discussion](https://news.ycombinator.com/item?id=48050964)

**Background**: On-device AI runs models locally on the user's device to process data without sending it to servers. Google's Gemini Nano is a lightweight model designed for local execution. The controversy involves Chrome silently downloading this model and the removal of privacy assurances.

<details><summary>References</summary>
<ul>
<li><a href="https://support.google.com/chrome/answer/16961953?hl=en">Manage on-device Generative AI models in Chrome - Google Chrome Help</a></li>
<li><a href="https://www.thatprivacyguy.com/blog/chrome-silent-nano-install/">Google Chrome silently installs a 4 GB AI model on your device without consent. At a billion-device scale the climate costs are insane. — That Privacy Guy!</a></li>
<li><a href="https://gizmodo.com/google-chrome-is-downloading-a-4gb-ai-model-onto-your-device-without-consent-researcher-warns-2000755201">Google Chrome Is Downloading a 4GB AI Model Onto Your Device Without Consent, Researcher Warns</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism, with some believing AI features are primarily for data collection. Others suggested the wording change might be innocuous, but noted compliance risks for businesses using Chrome.

**Tags**: `#privacy`, `#Chrome`, `#AI`, `#data collection`, `#browser`

---

<a id="item-12"></a>
## [Motherboard sales collapse 25% as AI chip production takes priority](https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers) ⭐️ 8.0/10

Motherboard sales have collapsed by more than 25% as chipmakers prioritize AI chip production, squeezing the enthusiast PC market. Asus is projected to sell 5 million fewer boards in 2025, with Gigabyte, MSI, and ASRock also expecting reduced sales. This shift highlights how AI demand is cannibalizing consumer PC hardware, potentially leading to higher prices and fewer choices for DIY builders. It also underscores the growing dominance of AI infrastructure investments over traditional PC markets. The shortage has caused prices for many major PC components to rise over the past six months, especially memory modules and storage drives. Despite the sales drop, motherboard makers like Asus, Gigabyte, and ASRock have pivoted to AI server production to capture hyperscaler investments.

hackernews · speckx · May 7, 15:23 · [Discussion](https://news.ycombinator.com/item?id=48050540)

**Background**: Motherboards are the main circuit board of a computer, connecting all components. The enthusiast PC market refers to high-performance custom-built computers favored by gamers and professionals. AI chips, such as GPUs from Nvidia and AMD, are in high demand for training large AI models, leading chipmakers to allocate more wafer capacity to AI products at the expense of consumer PC chips.

<details><summary>References</summary>
<ul>
<li><a href="https://www.tomshardware.com/pc-components/motherboards/motherboard-sales-collapse-by-more-than-25-percent-as-chipmakers-strangle-enthusiast-pc-market-to-build-more-ai-chips-asus-projected-to-sell-5-million-fewer-boards-in-2025-gigabyte-msi-and-asrock-also-expected-to-see-reduced-sales-numbers">Motherboard sales ' collapse ' by more than 25% as... | Tom's Hardw...</a></li>
<li><a href="https://aihaberleri.org/en/news/motherboard-sales-plunge-25percent-in-2026-as-ai-chip-shortages-hit-pc-market">Motherboard Sales Collapse Due to AI Chip Shortages and Failures</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lUaVpPTEVSSEYyc1BTZ0REVmNpZ0FQAQ?hl=en-SG&gl=SG&ceid=SG:en">Google News - Motherboard sales amid AI chip shortage - Overview</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern about the PC being the last major open platform, with some noting a shift toward closed hardware. Others shared personal anecdotes of delaying upgrades due to high prices, while some pointed out that motherboard makers are pivoting to AI servers to offset losses.

**Tags**: `#AI`, `#hardware`, `#PC market`, `#shortages`, `#industry trends`

---

<a id="item-13"></a>
## [Agent Skills: Production-Grade Engineering for AI Coders](https://github.com/addyosmani/agent-skills) ⭐️ 8.0/10

Addy Osmani released an open-source GitHub repository called agent-skills that packages senior engineering workflows into slash commands for AI coding agents, covering the full development lifecycle from idea to ship. This addresses a critical gap where AI coding agents often skip best practices like specs, tests, and security reviews, making it easier for developers to maintain code quality and consistency when using AI assistance. The repository provides 7 slash commands (/spec, /plan, /build, /test, /review, /code-simplify, /ship) that map to development phases, and skills activate automatically based on context (e.g., API design triggers api-and-interface-design).

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: AI coding agents like Claude Code, Cursor, and Gemini CLI can execute commands and follow instructions, but they often default to the shortest path, skipping engineering best practices. Agent Skills encodes the workflows, quality gates, and best practices that senior engineers use, packaging them so AI agents follow them consistently.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/addyosmani/agent-skills">addyosmani/ agent - skills : Production - grade engineering skills for AI ...</a></li>
<li><a href="https://jimmysong.io/ai/addyosmani-agent-skills/">Agent Skills : Production - Grade Engineering Skills for AI Coding...</a></li>
<li><a href="https://skilld.dev/skills/addyosmani/agent-skills/frontend-ui-engineering">Production - grade engineering skills for AI coding agents .</a></li>

</ul>
</details>

**Tags**: `#AI coding agents`, `#software engineering`, `#developer tools`, `#workflow automation`

---

<a id="item-14"></a>
## [TabPFN: Foundation Model for Tabular Data](https://github.com/PriorLabs/TabPFN) ⭐️ 8.0/10

PriorLabs has released TabPFN, a foundation model for tabular data that can perform classification and regression with state-of-the-art accuracy on small to medium datasets. TabPFN represents a paradigm shift in tabular machine learning by providing a single pretrained model that works across diverse datasets, reducing the need for extensive feature engineering and model selection. TabPFN is trained purely on synthetic data and supports datasets up to 10,000 samples and 500 features; it requires a GPU for optimal performance, with at least 8GB VRAM recommended.

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: Tabular data (e.g., spreadsheets, SQL tables) is the most common form of structured data in business and science. Traditional machine learning on tabular data often requires manual feature engineering and model tuning. TabPFN, short for Tabular Prior-data Fitted Network, is a foundation model that learns a prior over datasets, enabling few-shot learning and strong generalization on small data.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/PriorLabs/TabPFN">GitHub - PriorLabs / TabPFN : TabPFN : Foundation Model for Tabular...</a></li>
<li><a href="https://priorlabs.ai/tabpfn">TabPFN | Prior Labs</a></li>

</ul>
</details>

**Tags**: `#machine learning`, `#tabular data`, `#foundation model`, `#open source`

---

<a id="item-15"></a>
## [DocuSeal: Open-Source DocuSign Alternative](https://github.com/docusealco/docuseal) ⭐️ 8.0/10

DocuSeal, an open-source platform for creating, filling, and signing digital documents, has been released as a self-hosted alternative to DocuSign. It offers a live demo and cloud trial, with features including PDF form builder, automated emails, and API integrations. This provides a free, self-hosted option for secure document signing, reducing reliance on proprietary services like DocuSign. It empowers organizations to maintain control over their data and customize workflows. DocuSeal supports 12 field types, multiple submitters, and storage on disk or cloud services like AWS S3. Pro features include white-labeling, SMS verification, and embedded signing forms for React, Vue, and Angular.

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: Digital document signing platforms like DocuSign are widely used but often require subscription fees and data hosted on third-party servers. Open-source alternatives like DocuSeal allow users to self-host the software, ensuring data privacy and reducing costs. DocuSeal is built with a focus on ease of deployment and mobile optimization.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/docusealco/docuseal">GitHub - docusealco/docuseal: Open source DocuSign alternative. Create, fill, and sign digital documents ✍️</a></li>
<li><a href="https://www.docuseal.com/">DocuSeal | Open Source Document Signing</a></li>

</ul>
</details>

**Tags**: `#open-source`, `#document-signing`, `#self-hosted`, `#productivity`

---

<a id="item-16"></a>
## [Ladybird: A Truly Independent Web Browser in Pre-Alpha](https://github.com/LadybirdBrowser/ladybird) ⭐️ 8.0/10

Ladybird, a truly independent web browser built from scratch with a novel engine based on web standards, has been announced as a pre-alpha release suitable only for developers. Ladybird represents a significant effort to increase browser diversity by avoiding code from existing engines like Blink, WebKit, or Gecko, which could reduce the dominance of a few major browsers and promote a more open web. The browser uses a multi-process architecture with sandboxed renderer processes, and currently inherits core libraries from SerenityOS including LibWeb, LibJS, and LibWasm. It runs on Linux, macOS, Windows (with WSL2), and other Unix-like systems.

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: Most modern browsers (Chrome, Firefox, Safari) are based on a few dominant engines: Blink, Gecko, and WebKit. Ladybird aims to create a completely independent alternative by writing its own engine from scratch, initially forked from SerenityOS but now separate. Pre-alpha means the software is not feature-complete and is intended for developers only.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/LadybirdBrowser/ladybird">GitHub - LadybirdBrowser/ladybird: Truly independent web browser · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ladybird_(web_browser)">Ladybird (web browser) - Wikipedia</a></li>
<li><a href="https://ladybird.org/">Ladybird Browser</a></li>

</ul>
</details>

**Tags**: `#web browser`, `#open source`, `#web standards`, `#software engineering`

---

<a id="item-17"></a>
## [Kronos: Open-Source Foundation Model for Financial Markets](https://github.com/shiyu-coder/Kronos) ⭐️ 8.0/10

Kronos, the first open-source foundation model for financial candlesticks (K-lines), has been released and accepted by AAAI 2026. It is trained on data from over 45 global exchanges and features a live demo for BTC/USDT forecasting. Kronos addresses the lack of specialized foundation models for financial time series, potentially enabling more accurate forecasting and quantitative analysis. Its open-source nature and live demo could accelerate research and adoption in the financial AI community. Kronos uses a two-stage framework: a specialized tokenizer that discretizes OHLCV data into hierarchical discrete tokens, followed by a large autoregressive Transformer. The model family includes multiple sizes available on Hugging Face, and fine-tuning scripts have been released.

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: Foundation models are large pre-trained models that can be adapted to various downstream tasks. In finance, K-line (candlestick) charts represent price movements over time, and modeling them is challenging due to high noise and non-stationarity. Kronos is designed specifically for this domain, unlike general-purpose time series foundation models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/shiyu-coder/Kronos">GitHub - shiyu-coder/Kronos: Kronos: A Foundation Model for the Language of Financial Markets · GitHub</a></li>
<li><a href="https://arxiv.org/abs/2508.02739">[2508.02739] Kronos: A Foundation Model for the Language of Financial Markets</a></li>
<li><a href="https://arxiv.org/html/2508.02739v1">Kronos: A Foundation Model for the Language of Financial Markets</a></li>

</ul>
</details>

**Tags**: `#AI/ML`, `#Finance`, `#Foundation Model`, `#GitHub Trending`

---

<a id="item-18"></a>
## [ByteDance Open-Sources DeerFlow 2.0 SuperAgent Framework](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

ByteDance released DeerFlow 2.0, a ground-up rewrite of its open-source long-horizon SuperAgent framework, on GitHub under the MIT license. The framework orchestrates sub-agents, memory, sandboxes, and a message gateway to handle tasks ranging from minutes to hours. DeerFlow 2.0 provides a production-ready, modular architecture for building autonomous AI agents capable of complex, long-horizon tasks, potentially accelerating development in research, coding, and creative domains. Its open-source nature and multi-language support lower barriers for global developers. The framework requires Python 3.12+ and Node.js 22+, and ByteDance recommends using Doubao-Seed-2.0-Code, DeepSeek v3.2, or Kimi 2.5 as the underlying LLM. Version 2.0 is a complete rewrite with no shared code from v1, which remains maintained on a separate branch.

rss · GitHub Trending - Daily (All) · May 7, 23:10

**Background**: SuperAgent frameworks orchestrate multiple AI sub-agents, each specialized for subtasks, to accomplish complex goals. DeerFlow incorporates sandboxes for safe code execution, persistent memory for context retention, and a message gateway for inter-agent communication, enabling long-horizon autonomy.

**Tags**: `#AI Agents`, `#Open Source`, `#ByteDance`, `#Long-Horizon Tasks`, `#SuperAgent`

---

<a id="item-19"></a>
## [CreativityBench: Benchmarking LLM Creative Tool Use via Affordances](https://arxiv.org/abs/2605.02910) ⭐️ 8.0/10

Researchers introduced CreativityBench, a benchmark with 14K grounded tasks and a large-scale affordance knowledge base of 4K entities and 150K+ annotations, to evaluate LLMs' creative tool repurposing through affordance-based reasoning. This benchmark addresses the underexplored dimension of creative reasoning in LLMs, revealing that current models struggle with non-obvious tool use, which is crucial for advancing AI agents that must adapt to novel situations. Evaluations across 10 state-of-the-art LLMs showed that models often select plausible objects but fail to identify correct parts, affordances, and physical mechanisms; scaling and Chain-of-Thought yielded limited gains.

rss · arXiv - AI · May 7, 04:00

**Background**: Creative tool use requires reasoning about an object's affordances—its possible uses beyond its canonical function—rather than relying on typical usage. This capability is essential for intelligent agents that must solve problems in dynamic environments.

**Tags**: `#LLM`, `#benchmark`, `#creative reasoning`, `#affordance`, `#tool use`

---

<a id="item-20"></a>
## [Worker-Centered AI Adoption: Bridging Organizational Goals and User Needs](https://arxiv.org/abs/2605.03078) ⭐️ 8.0/10

A new qualitative study published on arXiv (2605.03078) identifies key barriers to AI adoption, including poor usability, misaligned expectations, limited control, and insufficient communication, based on interviews with workers in healthcare, finance, and management. This research highlights a critical blind spot in AI implementation: the neglect of worker experiences, which often leads to adoption failures. It advocates for worker-centered AI integration, a timely perspective as organizations worldwide struggle to realize AI's promised productivity gains. The study draws on interviews with professionals who interact with AI systems daily, revealing a mismatch between organizational goals and worker needs. It proposes adaptation strategies at individual, task, and organizational levels to better align AI with real-world practices.

rss · arXiv - AI · May 7, 04:00

**Background**: AI adoption in organizations often fails because workers resist or struggle to integrate new systems. This paper argues that workers are frequently invisible in decisions about AI design and deployment, leading to tools that do not fit their workflows. The concept of worker-centered AI has gained traction in recent policy discussions, emphasizing co-design, upskilling, and transparent communication.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.03078">[ 2605 . 03078 ] Making the Invisible Visible: Understanding the Mismatch...</a></li>
<li><a href="https://brownpoliticalreview.org/out-of-office-the-need-for-worker-centered-ai/">Out of Office: The Need for Worker - Centered AI</a></li>
<li><a href="https://gignomist.com/global-leaders-at-wef26-call-for-worker-centric-ai-upskilling-and-inclusion-in-tech-revolution/">WEF26 Panel Urges Worker - Centric AI , Upskilling... | The Gignomist</a></li>

</ul>
</details>

**Tags**: `#AI adoption`, `#human-computer interaction`, `#organizational change`, `#worker experience`, `#qualitative study`

---

<a id="item-21"></a>
## [Programmatic Context Augmentation for LLM Symbolic Regression](https://arxiv.org/abs/2605.03101) ⭐️ 8.0/10

Researchers propose a novel LLM-based evolutionary search framework for symbolic regression that incorporates programmatic context augmentation, enabling code-based data analysis beyond scalar metrics. This approach addresses a key limitation of existing LLM-based symbolic regression methods by leveraging richer feedback from the dataset, potentially improving accuracy and efficiency in scientific discovery. The framework was evaluated on advanced benchmarks like LLM-SRBench, demonstrating superior efficiency and accuracy compared to strong baselines.

rss · arXiv - AI · May 7, 04:00

**Background**: Symbolic regression is a type of regression analysis that searches the space of mathematical expressions to find the model that best fits a given dataset. Traditional methods often rely on genetic algorithms, while recent LLM-based approaches typically use scalar metrics like mean squared error as feedback, missing rich dataset information.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.03101">[2605.03101] Programmatic Context Augmentation for LLM-based...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Symbolic_regression">Symbolic regression</a></li>

</ul>
</details>

**Tags**: `#symbolic regression`, `#large language models`, `#evolutionary search`, `#scientific discovery`, `#AI`

---

<a id="item-22"></a>
## [Learning Correct Behavior from Few Traces](https://arxiv.org/abs/2605.03159) ⭐️ 8.0/10

Researchers propose a novel algorithm that learns correct sequential behavior from just 2-10 execution traces by combining dominator analysis from compiler theory with multimodal LLMs, achieving high accuracy in detecting bugs and false successes. This work addresses a critical challenge in validating autonomous agents' sequential behavior, reducing the need for manual specification or large training datasets, which could significantly improve AI safety and reliability across domains like UI testing, code generation, and robotics. The system constructs a generalized ground truth model using Prefix Tree Acceptors, merges traces through multi-tiered equivalence detection, and validates new executions via topological subsequence matching, providing explainable results with coverage metrics.

rss · arXiv - AI · May 7, 04:00

**Background**: Validating sequential behavior in autonomous agents traditionally requires manual specification, exact sequence matching, or thousands of training examples. Dominator analysis, a technique from compiler theory, identifies essential states in control flow graphs, while multimodal LLMs provide semantic understanding of diverse inputs.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dominator_(graph_theory)">Dominator (graph theory ) - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2605.03159">Learning Correct Behavior from Examples: Validating Sequential...</a></li>

</ul>
</details>

**Tags**: `#autonomous agents`, `#validation`, `#LLM`, `#compiler theory`, `#AI safety`

---

<a id="item-23"></a>
## [Terminus-4B: Small Model Matches Frontier LLMs in Agentic Tasks](https://arxiv.org/abs/2605.03195) ⭐️ 8.0/10

Researchers introduce Terminus-4B, a finetuned 4-billion-parameter model that achieves comparable or superior performance to frontier models like Claude Sonnet and GPT-5.3-Codex on agentic terminal execution tasks, reducing main agent token usage by up to 30%. This demonstrates that specialized small models can replace expensive frontier models for subagent tasks, significantly cutting costs and latency in agentic systems while maintaining performance, which could accelerate the deployment of multi-agent architectures. Terminus-4B is based on Qwen3-4B and trained with supervised finetuning and reinforcement learning using a rubric-based LLM-as-judge reward. It was evaluated on SWE-Bench Pro and an internal C# benchmark, showing improved main agent reliance on subagent outputs.

rss · arXiv - AI · May 7, 04:00

**Background**: Modern coding agents often delegate specialized subtasks to smaller subagents to keep the main agent's context clean. Traditionally, frontier models are used as subagents, which is expensive. This paper explores whether a finetuned small model can match frontier performance in terminal execution tasks.

**Tags**: `#AI Agents`, `#Small Language Models`, `#Reinforcement Learning`, `#Agentic Execution`, `#Model Efficiency`

---

<a id="item-24"></a>
## [Stop Automating Peer Review Without Rigorous Evaluation](https://arxiv.org/abs/2605.03202) ⭐️ 8.0/10

A new position paper empirically demonstrates that LLM-based peer reviewers exhibit a hivemind effect of excessive agreement and are easily gameable through stylistic rewriting, arguing against using current AI systems for paper reviews. This paper highlights critical flaws in AI peer review that threaten research integrity, urging the community to develop a science of peer review automation rather than deploying general-purpose LLMs without rigorous evaluation. The study compared human- versus AI-generated ICLR 2026 reviews and found that AI reviewers show excessive agreement within and across papers, and that prompting an LLM to rewrite a paper can significantly increase AI reviewer scores, demonstrating gaming via stylistic changes.

rss · arXiv - AI · May 7, 04:00

**Background**: Peer review is a cornerstone of scientific publishing but faces a crisis due to increasing submission volumes and reviewer shortages. Large language models (LLMs) have been proposed as a solution to automate parts of the review process, but this paper argues that such automation is premature and dangerous without proper safeguards.

**Tags**: `#AI`, `#peer review`, `#LLM`, `#research integrity`, `#machine learning`

---

<a id="item-25"></a>
## [ADAPTS: Agentic LLM Framework for Automated Mental Health Assessment](https://arxiv.org/abs/2605.03212) ⭐️ 8.0/10

ADAPTS introduces a mixture-of-agents LLM architecture that decomposes clinical interviews into symptom-specific reasoning tasks to automatically rate depression and anxiety severity, achieving expert-level accuracy on high-discrepancy cases. This framework enables objective and scalable psychiatric assessment, potentially improving mental health care access in resource-limited settings by reducing reliance on human raters. On high-discrepancy interviews, ADAPTS achieved an absolute error of 22, outperforming original human ratings (absolute error 26). An extended protocol incorporating clinical conventions reached ICC(2,1) = 0.877, indicating high agreement with expert ratings.

rss · arXiv - AI · May 7, 04:00

**Background**: Affective computing is an interdisciplinary field focused on enabling machines to recognize and respond to human emotions. Traditional mental health assessment relies on clinician-administered interviews and manual rating scales, which are time-consuming and subjective. ADAPTS leverages large language models (LLMs) in a multi-agent setup to automate this process while maintaining temporal and speaker alignment.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Affective_computing">Affective computing</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#affective computing`, `#mental health`, `#clinical AI`, `#multi-agent systems`

---

<a id="item-26"></a>
## [Scalar-Irreducible Dynamics Enable Endogenous Regime Switching](https://arxiv.org/abs/2605.04054) ⭐️ 8.0/10

This paper introduces a classification of learning dynamics into scalar-reducible and scalar-irreducible types, and shows that scalar-irreducible dynamics can produce endogenous regime switching without external scheduling. This work addresses a fundamental challenge in machine learning—autonomous intelligence—by proposing a mechanism for internally organized adaptive behavior, potentially reducing reliance on external scheduling in learning systems. The paper uses a minimal dynamical model to illustrate sustained endogenous regime transitions via feedback between fast dynamical variables and slow structural adaptation, but remains theoretical without empirical validation.

rss · arXiv - Machine Learning · May 7, 04:00

**Background**: Endogenous regime switching refers to a system's ability to autonomously change its behavioral mode without external intervention. Most existing machine learning systems rely on externally imposed schedules or curricula for such transitions. This paper proposes a new dynamical paradigm based on scalar-irreducible dynamics, which cannot be reduced to gradient flows of a scalar objective.

**Tags**: `#machine learning`, `#dynamical systems`, `#autonomous intelligence`, `#regime switching`, `#learning theory`

---

<a id="item-27"></a>
## [MetaAdamW: Self-Attention for Adaptive Learning Rates and Weight Decay](https://arxiv.org/abs/2605.04055) ⭐️ 8.0/10

Researchers propose MetaAdamW, a meta-optimizer that uses a self-attention mechanism to dynamically adjust per-group learning rates and weight decay, outperforming AdamW on five diverse tasks. This addresses a key limitation of AdamW—uniform hyperparameters across parameter groups—by enabling adaptive, group-specific optimization, potentially improving training efficiency and model performance across many deep learning applications. The self-attention module is a lightweight Transformer encoder that processes statistical features like gradient norms and momentum norms from each parameter group, trained via a meta-learning objective with priority-injected homoscedastic uncertainty weighting.

rss · arXiv - Machine Learning · May 7, 04:00

**Background**: Adaptive optimizers like AdamW apply the same learning rate and weight decay to all parameter groups, ignoring that different layers (e.g., embeddings vs. classifiers) may require different hyperparameters. MetaAdamW introduces a meta-learning approach to learn these group-specific adjustments, using self-attention to capture dependencies between groups.

**Tags**: `#optimization`, `#meta-learning`, `#self-attention`, `#deep learning`, `#hyperparameter adaptation`

---

<a id="item-28"></a>
## [Task Encoding in LLMs Is Distributed, Not Localized](https://arxiv.org/abs/2605.04061) ⭐️ 8.0/10

A new paper shows that task identity in large language models is encoded in a distributed manner across demonstration output tokens, not localized to single positions, using causal intervention methods. This challenges prior assumptions about localized task representations in LLMs and reshapes our understanding of how in-context learning operates, with implications for mechanistic interpretability and model editing. Single-position intervention achieved 0% task transfer despite 100% probing accuracy, while multi-position intervention at all demonstration output tokens achieved up to 96% transfer at layer 8 in Llama-3.2-3B. The effect generalizes across four models from three architecture families, with a universal intervention window at ~30% network depth.

rss · arXiv - Machine Learning · May 7, 04:00

**Background**: In-context learning (ICL) allows LLMs to perform tasks from a few examples without parameter updates. Prior work used linear probing to localize task representations, reporting high accuracy at specific layers. This paper reveals a dissociation between probing accuracy and causal importance, showing that task encoding is distributed across demonstration tokens.

**Tags**: `#mechanistic interpretability`, `#in-context learning`, `#large language models`, `#causal intervention`, `#task encoding`

---

<a id="item-29"></a>
## [LLMs Show Bias in Conflict Monitoring](https://arxiv.org/abs/2605.04177) ⭐️ 8.0/10

A new study evaluates four open-weight LLMs and two domain-adapted models on conflict-event classification in West Africa, revealing systematic biases such as False Illegitimation and actor-based selection bias. This research highlights that current LLMs are not ready for unsupervised deployment in conflict monitoring, which is critical for humanitarian accountability and AI safety. Open-weight models like Gemma 3 4B misclassify 18.29% of legitimate battles as civilian-targeted violence, while domain-adapted models reduce but do not eliminate bias, e.g., state actors are legitimized 36.5% more often than non-state actors in Nigeria.

rss · arXiv - NLP · May 7, 04:00

**Background**: Conflict monitoring relies on accurate classification of events like battles and civilian violence. ACLED is a gold-standard dataset with multi-stage verification. LLMs are increasingly used but may introduce biases that distort humanitarian reporting.

**Tags**: `#LLM`, `#bias`, `#conflict monitoring`, `#domain adaptation`, `#AI safety`

---

<a id="item-30"></a>
## [MedFabric & ETHER: Detecting Word-Level Fabrications in Medical LLMs](https://arxiv.org/abs/2605.04180) ⭐️ 8.0/10

Researchers propose MedFabric, a dataset of realistic word-level fabrications in medical LLMs, and ETHER, a modular detector that outperforms state-of-the-art by over 15% on word-level fabrication benchmarks. This addresses a critical safety issue in medical AI by enabling precise detection of subtle factual errors, which is essential for reliable clinical decision support. MedFabric preserves syntactic and stylistic fidelity while introducing subtle factual deviations, and ETHER uses Text2Table Decomposition, Word Masking and Filling, and Hybrid Sentence Pair Evaluation.

rss · arXiv - NLP · May 7, 04:00

**Background**: Large Language Models (LLMs) often generate fluent but factually incorrect statements, known as hallucinations, which are especially dangerous in medical domains. Existing datasets for medical hallucination detection suffer from limited coverage and stylistic mismatches. This work introduces a data-centric pipeline to generate more realistic fabrications.

**Tags**: `#medical LLMs`, `#hallucination detection`, `#data-centric AI`, `#NLP`, `#factuality`

---

<a id="item-31"></a>
## [Nsanku Benchmarks LLMs for Ghanaian Language Translation](https://arxiv.org/abs/2605.04208) ⭐️ 8.0/10

The Nsanku benchmark evaluates zero-shot translation of 19 LLMs across 43 Ghanaian languages, finding gemini-2.5-flash top-performing with an average score of 26.88, but overall low scores indicate models are not yet reliable for these low-resource languages. This work addresses a critical gap in evaluating LLMs for extremely low-resource African languages, highlighting the need for better support and fairness in multilingual AI systems. The benchmark uses 300 sentence pairs per language from the YouVersion Bible platform, with BLEU and chrF metrics, and a consistency analysis showing no model-language pair achieved both high performance and high consistency.

rss · arXiv - NLP · May 7, 04:00

**Background**: Zero-shot machine translation refers to translating between language pairs without explicit training data for that pair. Low-resource languages like those in Ghana often lack large parallel corpora, making LLM evaluation challenging. The chrF metric measures character n-gram overlap, which can be more robust for morphologically rich languages than BLEU.

**Tags**: `#machine translation`, `#low-resource languages`, `#LLM evaluation`, `#African languages`, `#NLP`

---

<a id="item-32"></a>
## [MLLMs Show Large Benchmark-to-Bedside Gap in Dermatology](https://arxiv.org/abs/2605.04098) ⭐️ 8.0/10

A study evaluated four open-weight and one commercial multimodal LLM on real-world dermatology data (5,811 cases), finding top-3 diagnostic accuracy dropped from 42.25% on public benchmarks to 24.65% on real-world images alone for GPT-4.1. This reveals a significant gap between benchmark success and clinical applicability, questioning the readiness of current MLLMs for real-world dermatology and highlighting the need for more realistic evaluation. The study used a multi-site hospital cohort with 46,405 clinical images and evaluated models on differential diagnosis and severity-based triage. Incorporating clinical context improved accuracy but models remained sensitive to incomplete or erroneous context.

rss · arXiv - Computer Vision · May 7, 04:00

**Background**: Multimodal large language models (MLLMs) process both text and images, showing promise on public dermatology benchmarks. However, benchmarks often use curated data that may not reflect real-world variability in image quality, lesion diversity, and clinical context.

**Tags**: `#multimodal LLM`, `#dermatology`, `#clinical evaluation`, `#AI in healthcare`, `#benchmark-to-bedside gap`

---

<a id="item-33"></a>
## [Deep learning fails on scientific images despite richer data](https://arxiv.org/abs/2605.04231) ⭐️ 8.0/10

A new paper shows that deep learning models trained on information-rich infrared (IR) pathology images paradoxically underperform compared to models trained on standard RGB stained tissue images, due to a mismatch between data priors and the simplicity bias of deep learning. This finding highlights a critical failure mode of deep learning in scientific imaging, raising AI safety concerns and undermining the advantages of advanced scientific modalities; it calls for modality-specific algorithm design rather than naive application of generic DL frameworks. The study compares RGB pathology images with quantitative IR imaging data, finding that IR-trained models collapse to one-dimensional predictions, leaving most representational capacity unused; this problem persists even with state-of-the-art robustification strategies designed for RGB imagery.

rss · arXiv - Computer Vision · May 7, 04:00

**Background**: Deep learning excels on everyday RGB images due to their alignment with human perception and natural image priors. Scientific imaging, however, often involves many spectral channels encoding precise physicochemical properties, which can introduce different statistical priors that interact poorly with deep learning's simplicity bias—the tendency to favor low-complexity solutions.

**Tags**: `#deep learning`, `#scientific imaging`, `#failure analysis`, `#pathology`, `#computer vision`

---

<a id="item-34"></a>
## [Entropic RNOT Unifies Regularization and Neural OT on Manifolds](https://arxiv.org/abs/2605.04255) ⭐️ 8.0/10

Entropic RNOT integrates entropic regularization with neural optimal transport for Riemannian manifolds, enabling scalable out-of-sample transport maps. The method learns a single target-side Schrödinger potential via neural pullback parameterization. This framework bridges a gap between discrete entropic OT and amortized neural OT on curved spaces, making optimal transport practical for machine learning problems with non-Euclidean data. It has potential impact on domains like robotics, computer vision, and drug design where data lies on manifolds. The method provides theoretical guarantees: barycentric surrogates converge in L^2, and heat-smoothed surrogates are stable and asymptotically unbiased. Empirically, it matches or improves over Euclidean and tangent-space baselines on benchmarks including S^2, SO(3), SPD(3), SE(3), and H^2.

rss · arXiv - Data Science & Statistics · May 7, 04:00

**Background**: Optimal transport (OT) defines a distance between probability distributions, but on curved spaces (Riemannian manifolds), Euclidean OT distorts geometry. Entropic regularization adds a penalty to make discrete OT computationally cheaper, while neural OT learns amortized maps for new samples. Prior work kept these advantages separate.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/hadamard_manifold">Hadamard manifold</a></li>

</ul>
</details>

**Tags**: `#optimal transport`, `#Riemannian manifolds`, `#machine learning`, `#entropic regularization`, `#neural networks`

---

<a id="item-35"></a>
## [Adam vs SGD: Provable Tradeoffs in Nonstationary Optimization](https://arxiv.org/abs/2605.04269) ⭐️ 8.0/10

This paper provides the first theoretical analysis of Adam optimizer under non-stationary stochastic objectives, deriving finite-time bounds that decompose into initialization, drift, first-moment tracking error, and preconditioner perturbation components. 这项工作揭示了噪声-漂移权衡，解释了Adam何时优于SGD、何时表现更差，为在线学习和强化学习等动态环境中的优化器选择提供了理论指导。 The analysis covers two regimes: Euclidean tracking under adaptive strong monotonicity and high-probability projected stationarity under general L-smooth objectives. The bounds explicitly depend on hyperparameters β1, β2, and ε, characterizing burn-in time and irreducible tracking floor.

rss · arXiv - Data Science & Statistics · May 7, 04:00

**Background**: Adam and SGD are two widely used optimizers in machine learning. Adam adapts learning rates per parameter using first and second moment estimates, while SGD uses a fixed or decaying learning rate. Non-stationary objectives, where the data distribution or loss function changes over time, are common in online learning and reinforcement learning. Prior theoretical work on Adam focused on stationary settings, leaving its behavior under distribution shift poorly understood.

**Tags**: `#optimization`, `#Adam`, `#SGD`, `#non-stationary`, `#theory`

---

<a id="item-36"></a>
## [Perturbation Training Boosts LLM Extrapolation](https://arxiv.org/abs/2605.04344) ⭐️ 8.0/10

Researchers propose a perturbation-based training method for large language models that replaces exact prefix conditioning with a semantically perturbed variant, improving out-of-support prediction while maintaining in-support performance. This work provides a theoretical framework for extrapolation in language models, addressing a key limitation of standard autoregressive models that struggle with sequences outside the training distribution, potentially improving generalization in real-world applications. The method introduces a hierarchical model with a pre-post-additive noise structure, and the paper provides finite-sample performance guarantees on both synthetic and real-world language data.

rss · arXiv - Data Science & Statistics · May 7, 04:00

**Background**: Standard autoregressive language models predict the next token based on an exact prefix, which limits their ability to handle sequences not seen during training. Extrapolation, or out-of-support prediction, is a known challenge in machine learning. This work proposes perturbing the prefix to create semantic neighbors, enabling the model to learn from a broader range of contexts.

**Tags**: `#large language models`, `#training methods`, `#extrapolation`, `#perturbation`, `#NLP`

---