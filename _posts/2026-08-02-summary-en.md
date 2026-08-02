---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 37 items, 6 important content pieces were selected

---

1. [Microsoft-led open letter backs open-weight AI models](#item-1) ⭐️ 8.0/10
2. [GitHub Releases Official Multi-Platform Copilot Agent SDK](#item-2) ⭐️ 8.0/10
3. [Hugging Face Launches Low-Latency Open-Source Speech-to-Speech Library](#item-3) ⭐️ 8.0/10
4. [Microsoft's TRELLIS.2: Compact Structured Latents for Efficient 3D Generation](#item-4) ⭐️ 8.0/10
5. [ByteDance's DeerFlow 2.0: Open-Source Long-Horizon SuperAgent Harness](#item-5) ⭐️ 8.0/10
6. [Karpathy's Autoresearch: Autonomous AI Agents for Overnight LLM Training](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Microsoft-led open letter backs open-weight AI models](https://simonwillison.net/2026/Aug/2/open-letters/#atom-everything) ⭐️ 8.0/10

On July 24, 2026, Microsoft shepherded an open letter titled 'Open Weights and American AI Leadership', signed by 235 AI-adjacent companies including NVIDIA, Amazon, Y Combinator, The Linux Foundation, and later OpenAI, arguing against potential US government restrictions on open-weight models. Notably, Anthropic did not sign and instead published its own position three days later, while a separate letter 'Pacing the Frontier' signed by 1,324 employees of frontier AI companies was published on July 28. This open letter represents a significant industry alignment against potential government restrictions on open-weight AI models, highlighting a major policy debate with broad implications for AI development, competition, and safety. The involvement of major tech companies and the notable absence of Anthropic underscore the strategic divisions within the AI community over how to balance openness and risk. The letter explicitly supports distillation, a technique where models train on outputs from other models, arguing policymakers should not conflate it with misappropriation. Anthropic's response, 'Our position on open-weights models', expressed concerns about authoritarian governments building powerful AI and called for a crackdown on industrial-scale distillation operations, while stating it has never advocated for a ban on open-weights models.

rss · Simon Willison · Aug 2, 04:16

**Background**: Open-weight models are AI models whose core components, including the trained weights, are publicly released, allowing anyone to download and use them. This contrasts with closed models, which are kept proprietary. The debate over open-weight models centers on balancing transparency and innovation against potential misuse and national security risks, especially in the context of US-China competition in AI.

<details><summary>References</summary>
<ul>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>
<li><a href="https://www.nytimes.com/2026/07/28/technology/open-weight-ai.html">What Is Open-Weights A.I.? - The New York Times</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**Tags**: `#AI policy`, `#open source`, `#open-weight models`, `#industry letter`, `#Simon Willison`

---

<a id="item-2"></a>
## [GitHub Releases Official Multi-Platform Copilot Agent SDK](https://github.com/github/copilot-sdk) ⭐️ 8.0/10

GitHub has released an official multi-platform SDK for integrating the GitHub Copilot Agent into applications, now in technical preview. The SDK supports Python, TypeScript, Go, .NET, Java, and Rust, and is available via npm, PyPI, NuGet, Go modules, crates.io, and Maven Central. This SDK lowers the barrier for developers to build Copilot-powered applications by exposing the same production-tested agent runtime behind Copilot CLI. It enables programmatic access to planning, tool invocation, file edits, and command execution, potentially accelerating the adoption of agentic AI in software development. The SDK is available for Node.js/TypeScript, Python, Go, .NET, Rust, and Java, with installation commands such as 'npm install @github/copilot-sdk' and 'pip install github-copilot-sdk'. It includes cookbooks for most languages, and API documentation is provided for Go and Rust. The SDK is currently in technical preview, meaning features may change.

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**Background**: GitHub Copilot is an AI-powered coding assistant that helps developers write code. The Copilot Agent is a more advanced system that can autonomously plan and execute tasks, such as editing files and running commands. Previously, developers had to build their own orchestration to integrate such capabilities, but this SDK provides a ready-made runtime.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/github/copilot-sdk">GitHub - github/copilot-sdk: Multi-platform SDK for ...</a></li>
<li><a href="https://docs.github.com/en/copilot/how-tos/copilot-sdk">Copilot SDK - GitHub Docs</a></li>
<li><a href="https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/">Build an agent into any app with the GitHub Copilot SDK</a></li>

</ul>
</details>

**Tags**: `#GitHub Copilot`, `#SDK`, `#AI`, `#Developer Tools`, `#API`

---

<a id="item-3"></a>
## [Hugging Face Launches Low-Latency Open-Source Speech-to-Speech Library](https://github.com/huggingface/speech-to-speech) ⭐️ 8.0/10

Hugging Face has released a new open-source library called 'speech-to-speech' that enables building local voice agents with a modular pipeline (VAD -> STT -> LLM -> TTS) and an OpenAI Realtime-compatible WebSocket API. The library is currently the #1 trending repository on GitHub today. This release addresses the growing demand for on-device AI and low-latency voice agents, allowing developers to build fully local, open-source voice applications without relying on cloud services. It also provides a flexible, swappable architecture that can integrate with various LLM backends, including hosted providers or local servers, making it a significant tool for the AI developer community. The pipeline includes Voice Activity Detection (VAD), Speech-to-Text (STT), Language Model (LLM), and Text-to-Speech (TTS), with each component swappable. The default setup uses Parakeet TDT for local STT, an OpenAI-compatible LLM, and Qwen3-TTS for local speech output, and it supports CUDA and Apple Silicon. The library is already running in production as the conversation backend for thousands of Reachy Mini robots.

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**Background**: Voice agents typically require a pipeline of components: detecting when a user speaks (VAD), transcribing speech to text (STT), generating a response with a language model (LLM), and converting text back to speech (TTS). Traditionally, these components are often hosted in the cloud, leading to latency and privacy concerns. Hugging Face's library aims to provide a low-latency, fully local alternative by integrating open-source models and an OpenAI Realtime-compatible API, making it easier for developers to build and deploy voice agents on their own hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/huggingface/speech-to-speech">GitHub - huggingface/speech-to-speech: Build local voice agents with...</a></li>
<li><a href="https://www.linkedin.com/posts/andimarafioti_introducing-hugging-faces-speech-to-speech-activity-7231548059388723201-zFfS">Hugging Face 's Speech to Speech library | Andrés... | LinkedIn</a></li>
<li><a href="https://drose.io/aitools/tools/hugging-face-speech-to-speech">Hugging Face Speech - to - Speech | AI Developer Tools Tool</a></li>

</ul>
</details>

**Tags**: `#speech-to-speech`, `#voice agents`, `#open-source`, `#Hugging Face`, `#AI`

---

<a id="item-4"></a>
## [Microsoft's TRELLIS.2: Compact Structured Latents for Efficient 3D Generation](https://github.com/microsoft/TRELLIS.2) ⭐️ 8.0/10

Microsoft released TRELLIS.2, a 4B-parameter large 3D generative model that introduces a novel 'field-free' sparse voxel structure called O-Voxel for high-fidelity image-to-3D generation. The model, code, and demo are open-sourced on GitHub and Hugging Face. TRELLIS.2 significantly advances 3D generation by enabling efficient, high-quality asset creation from a single image, which can lower the barrier for non-experts in fields like game development, product design, and AR/VR. Its open-source release encourages broad adoption and further research. The model uses a Sparse 3D VAE with 16× spatial downsampling to encode assets into a compact latent space, and supports arbitrary topologies like open surfaces and non-manifold geometry. It can generate 512³ resolution in ~3 seconds on an H100 GPU, and models PBR materials including base color, roughness, metallic, and opacity.

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**Background**: TRELLIS.2 builds on the earlier TRELLIS model, which introduced Structured LATents (SLAT) for 3D generation. SLAT represents 3D assets using local latents on active voxels, allowing decoding to different formats like meshes and radiance fields. TRELLIS.2 improves this by using a field-free O-Voxel representation, avoiding lossy conversions and handling complex topologies more robustly.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/TRELLIS.2">GitHub - microsoft/TRELLIS.2: Native and Compact Structured ...</a></li>
<li><a href="https://microsoft.github.io/TRELLIS/">TRELLIS: Structured 3D Latents for Scalable and Versatile 3D ...</a></li>
<li><a href="https://arxiv.org/abs/2412.01506">[2412.01506] Structured 3D Latents for Scalable and Versatile 3D Generation</a></li>

</ul>
</details>

**Tags**: `#3D generation`, `#structured latents`, `#machine learning`, `#computer vision`, `#Microsoft`

---

<a id="item-5"></a>
## [ByteDance's DeerFlow 2.0: Open-Source Long-Horizon SuperAgent Harness](https://github.com/bytedance/deer-flow) ⭐️ 8.0/10

ByteDance released DeerFlow 2.0, a ground-up rewrite of its open-source agent framework, now a long-horizon SuperAgent harness that orchestrates sub-agents, memory, sandboxes, and a message gateway to handle tasks lasting minutes to hours. The project reached #1 on GitHub Trending on February 28, 2026. This release advances autonomous agent development by enabling complex, long-horizon tasks that were previously challenging for AI systems. It provides an open-source alternative for researchers and developers to build sophisticated agents, potentially accelerating innovation in AI automation and software engineering. DeerFlow 2.0 is a complete rewrite with no code shared with v1; the original Deep Research framework is maintained on the 1.x branch. It requires Python 3.12+ and Node.js 22+, is MIT-licensed, and ByteDance recommends using Doubao-Seed-2.0-Code, DeepSeek v3.2, or Kimi 2.5 models.

rss · GitHub Trending - Daily (All) · Aug 2, 22:48

**Background**: Long-horizon agent tasks involve extended sequences of actions over hours or days, requiring sophisticated planning and adaptation. A SuperAgent harness is a framework that orchestrates sub-agents, each with scoped context and tools, to tackle complex tasks. A message gateway provides a governed layer for agent-to-agent communication, handling authentication, logging, and routing.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/bytedance/deer-flow">GitHub - bytedance/deer-flow: An open-source long-horizon ...</a></li>
<li><a href="https://ai-tldr.dev/releases/bytedance-deerflow-2/">DeerFlow 2.0 — open-source SuperAgent harness — ByteDance ...</a></li>
<li><a href="https://www.ibm.com/think/topics/agent-gateway">What is an Agent Gateway? | IBM</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Agent`, `#Open Source`, `#Automation`, `#ByteDance`

---

<a id="item-6"></a>
## [Karpathy's Autoresearch: Autonomous AI Agents for Overnight LLM Training](https://github.com/karpathy/autoresearch) ⭐️ 8.0/10

Andrej Karpathy released 'autoresearch', a GitHub repository that enables AI agents to autonomously run LLM training experiments overnight. The agent modifies training code, runs 5-minute experiments, and iterates to improve a model's validation bits per byte (val_bpb). This project showcases a novel workflow where AI agents take over the iterative research process, potentially accelerating discovery and reducing human workload. It could influence how AI research is conducted, moving toward more autonomous experimentation. The repo is minimal, with three key files: prepare.py (fixed), train.py (agent-edited), and program.md (human-edited). Training runs on a single GPU (tested on H100) with a fixed 5-minute time budget, and the metric is val_bpb, which is vocab-size-independent.

rss · GitHub Trending - Python · Aug 2, 22:48

**Background**: Karpathy's previous project, nanochat, is a minimal single-GPU LLM training harness covering tokenization, pretraining, finetuning, evaluation, and inference. Autoresearch builds on this by adding an autonomous agent layer that can modify the training code and run experiments without human intervention, aiming to create a self-improving research loop.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/karpathy/nanochat">GitHub - karpathy/nanochat: The best ChatGPT that $100 can buy. · GitHub</a></li>
<li><a href="https://trelis.substack.com/p/train-an-llm-from-scratch-with-karpathys">Train an LLM from Scratch with Karpathy's Nanochat</a></li>
<li><a href="https://aiengineering.academy/LLM/ServerLessFinetuning/TrainNanochatModalTutorial/">Training Nanochat on Modal - AI Engineering Academy</a></li>

</ul>
</details>

**Tags**: `#AI agents`, `#LLM training`, `#automation`, `#research`, `#Karpathy`

---