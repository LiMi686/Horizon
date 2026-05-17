---
layout: default
title: "Horizon Summary: 2026-05-17 (EN)"
date: 2026-05-17
lang: en
---

> From 27 items, 6 important content pieces were selected

---

1. [SGLang v0.5.12 Adds Full Inference Support for DeepSeek V4](#item-1) ⭐️ 9.0/10
2. [Bun: All-in-One JavaScript Runtime, Bundler, and Package Manager](#item-2) ⭐️ 9.0/10
3. [Supertonic: Fast On-Device Multilingual TTS via ONNX](#item-3) ⭐️ 8.0/10
4. [RuView Turns WiFi Signals into Privacy-Preserving Spatial Intelligence](#item-4) ⭐️ 8.0/10
5. [CodeGraph: Pre-indexed knowledge graph slashes Claude Code tool calls by 94%](#item-5) ⭐️ 8.0/10
6. [CLI-Anything: Making All Software Agent-Native](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.12 Adds Full Inference Support for DeepSeek V4](https://github.com/sgl-project/sglang/releases/tag/v0.5.12) ⭐️ 9.0/10

SGLang v0.5.12 introduces comprehensive inference support for DeepSeek V4, including tensor, expert, context, and data parallel attention, along with optimized DeepGemm and FlashMLA kernels for the MegaMoE architecture. The release also adds support for multiple new models like Intern-S2-Preview and MiniCPM-V 4.6, and matures speculative decoding with EAGLE-3. This release enables efficient serving of DeepSeek V4, a 1.6-trillion-parameter MoE model, on a wide range of hardware including NVIDIA B300/B200 and AMD MI35X, significantly lowering the barrier for deploying cutting-edge large language models. The advanced parallelism and kernel optimizations set a new standard for inference performance in open-source serving frameworks. Key features include HiSparse for offloading inactive KV cache to CPU memory, W4A4 MegaMoE kernels for faster speed with negligible accuracy drop, and a unified Docker tag for all NVIDIA GPUs. The release also migrates DeepEP to the official CUDA 13-compatible fork and adds TokenSpeed MLA attention backend for Blackwell GPUs.

github · Fridge003 · May 16, 18:23

**Background**: SGLang is an open-source framework for high-performance inference of large language models and multimodal models, designed for low-latency and high-throughput serving. DeepSeek V4 is a Mixture-of-Experts (MoE) model with up to 1.6 trillion total parameters, requiring advanced parallelism and kernel optimizations for efficient deployment. MegaMoE is a specialized architecture that scales expert parallelism across many GPUs.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/sgl-project/sglang">GitHub - sgl-project/sglang: SGLang is a high-performance serving ...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro">deepseek-ai/DeepSeek-V4-Pro · Hugging Face</a></li>
<li><a href="https://api-docs.deepseek.com/news/news260424">DeepSeek V4 Preview Release | DeepSeek API Docs</a></li>

</ul>
</details>

**Tags**: `#DeepSeek V4`, `#inference`, `#SGLang`, `#parallelism`, `#kernels`

---

<a id="item-2"></a>
## [Bun: All-in-One JavaScript Runtime, Bundler, and Package Manager](https://github.com/oven-sh/bun) ⭐️ 9.0/10

Bun is a new all-in-one JavaScript runtime, bundler, test runner, and package manager that aims to replace Node.js and multiple separate tools. It is written in Zig and uses JavaScriptCore for significantly faster startup and lower memory usage. Bun simplifies the JavaScript development toolchain by replacing multiple tools (Node.js, webpack, Jest, npm) with a single executable, drastically improving performance and developer experience. Its speed and all-in-one design could shift the JavaScript ecosystem toward more integrated tooling. Bun supports TypeScript and JSX out of the box, and is compatible with existing Node.js projects with minimal changes. It runs on Linux, macOS, and Windows, and can be installed via curl, npm, Homebrew, or Docker.

rss · GitHub Trending - Daily (All) · May 17, 13:26

**Background**: JavaScript developers traditionally rely on separate tools for runtime (Node.js), bundling (webpack), testing (Jest), and package management (npm). Bun consolidates these into one tool, built on the fast JavaScriptCore engine (used by Safari) instead of V8 (used by Chrome/Node.js), and written in Zig for low-level performance.

<details><summary>References</summary>
<ul>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>
<li><a href="https://www.linode.com/docs/guides/introduction-to-bun/">Introduction to the Bun JavaScript Runtime | Linode Docs</a></li>

</ul>
</details>

**Discussion**: The community has shown strong interest, with the GitHub repository accumulating over 70,000 stars. Discussions highlight excitement about Bun's speed and simplicity, though some users express caution about its maturity and compatibility with existing Node.js packages.

**Tags**: `#JavaScript`, `#runtime`, `#tooling`, `#performance`, `#open-source`

---

<a id="item-3"></a>
## [Supertonic: Fast On-Device Multilingual TTS via ONNX](https://github.com/supertone-inc/supertonic) ⭐️ 8.0/10

Supertone Inc. released Supertonic, an open-source, on-device multilingual text-to-speech system that runs natively via ONNX Runtime, supporting 31 languages with a 99M-parameter model. Supertonic enables high-quality, low-latency TTS on edge devices without cloud dependency, preserving privacy and reducing costs, which is significant for applications in accessibility, education, and IoT. The model outputs 44.1kHz 16-bit WAV audio directly, includes 10 expression tags for natural speech, and provides SDKs for multiple runtimes including Python, Node.js, and WebGPU.

rss · GitHub Trending - Daily (All) · May 17, 13:26

**Background**: ONNX Runtime is a cross-platform inference accelerator for machine learning models, supporting various frameworks and hardware. Traditional TTS systems often rely on cloud APIs, introducing latency and privacy concerns. Supertonic leverages ONNX to run entirely on-device, offering a compact 99M-parameter model that is much smaller than typical 0.7B-2B parameter models.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/microsoft/onnxruntime">GitHub - microsoft/onnxruntime: ONNX Runtime: cross-platform, high ...</a></li>
<li><a href="https://elevenlabs.io/blog/multilingual-text-to-speech-reaching-a-global-audience-with-ai-voices">Multilingual TTs: Reaching a Global Audience with AI Voices</a></li>

</ul>
</details>

**Tags**: `#TTS`, `#ONNX`, `#open-source`, `#multilingual`, `#on-device`

---

<a id="item-4"></a>
## [RuView Turns WiFi Signals into Privacy-Preserving Spatial Intelligence](https://github.com/ruvnet/RuView) ⭐️ 8.0/10

RuView is an open-source platform that uses commodity WiFi signals and Channel State Information (CSI) from low-cost ESP32 sensors to detect presence, monitor vital signs, and estimate human pose without any cameras. This technology enables privacy-preserving sensing for smart homes, healthcare, and security, operating through walls and in darkness without requiring wearables or cloud connectivity. RuView supports pose estimation with 17 COCO keypoints using the WiFlow architecture, but current camera-free accuracy is limited (PCK@20 ≈ 2.5%), with a planned camera-supervised training target of 35%+ PCK@20. The system uses spiking neural networks that adapt in under 30 seconds and cryptographically attests measurements via an Ed25519 witness chain.

rss · GitHub Trending - Daily (All) · May 17, 13:26

**Background**: WiFi sensing leverages Channel State Information (CSI) to detect changes in radio wave reflections caused by human movement and breathing. Unlike traditional camera-based or wearable sensors, WiFi sensing is non-intrusive and can operate through walls. RuView builds on prior research like DensePose From WiFi from Carnegie Mellon University and uses ESP32 microcontrollers as low-cost sensor nodes.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/espressif/esp-csi">GitHub - espressif/esp-csi: Applications based on Wi-Fi CSI (Channel state information), such as indoor positioning, human detection · GitHub</a></li>
<li><a href="https://info.support.huawei.com/info-finder/encyclopedia/en/CSI+Sensing.html">What Is CSI Sensing? - Huawei</a></li>

</ul>
</details>

**Tags**: `#WiFi sensing`, `#spatial intelligence`, `#vital signs`, `#privacy`, `#IoT`

---

<a id="item-5"></a>
## [CodeGraph: Pre-indexed knowledge graph slashes Claude Code tool calls by 94%](https://github.com/colbymchenry/codegraph) ⭐️ 8.0/10

CodeGraph is a pre-indexed code knowledge graph for Claude Code that reduces tool calls by up to 94% and exploration time by up to 77%, running entirely locally. It provides instant querying of symbol relationships, call graphs, and code structure instead of relying on file scanning. This dramatically reduces token consumption and latency for AI-assisted code exploration, making Claude Code more efficient and cost-effective for developers working on large codebases. It represents a practical application of knowledge graphs to improve AI agent performance without sacrificing privacy or requiring cloud dependencies. Benchmarks across six real-world codebases (VS Code, Excalidraw, Claude Code, Alamofire, Swift Compiler) show an average of 92% fewer tool calls and 71% faster exploration. CodeGraph uses tree-sitter for parsing and exposes the graph via the Model Context Protocol (MCP).

rss · GitHub Trending - Daily (All) · May 17, 13:26

**Background**: Claude Code's Explore agents traditionally scan files using grep, glob, and Read operations, consuming tokens on every tool call. A code knowledge graph pre-indexes symbol relationships, call graphs, and structure, allowing agents to query instantly instead of scanning. This approach was pioneered by projects like GraphGen4Code and popularized by CodeGraph for AI coding assistants.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/colbymchenry/codegraph">GitHub - colbymchenry/codegraph: Pre-indexed code knowledge graph for Claude Code — fewer tokens, fewer tool calls, 100% local</a></li>
<li><a href="https://github.com/wala/graph4code">GitHub - wala/graph4code: GraphGen4Code: a toolkit for ...</a></li>
<li><a href="https://www.grahambrooks.com/post/building-a-code-knowledge-graph-for-ai-agents/">Building a Code Knowledge Graph for Ai Agents | Coding Architect</a></li>

</ul>
</details>

**Tags**: `#AI`, `#developer-tools`, `#code-intelligence`, `#Claude-Code`

---

<a id="item-6"></a>
## [CLI-Anything: Making All Software Agent-Native](https://github.com/HKUDS/CLI-Anything) ⭐️ 8.0/10

HKUDS released CLI-Anything, a framework and hub that creates CLI wrappers for any software, enabling AI agents to interact with them natively. The project includes a CLI-Hub for community-contributed wrappers and supports agents like Claude Code, Cursor, and OpenClaw. This project bridges the gap between AI agents and existing software, potentially transforming how agents interact with tools. It could accelerate the adoption of agent-native architectures by making any software accessible via CLI. The generated CLIs are standard Python packages installable via pip, output both JSON and human-readable text, and have passed over 2,200 tests. The CLI-Hub allows users to browse, install, and manage community-built CLIs with a single command.

rss · GitHub Trending - Python · May 17, 13:26

**Background**: AI agents often struggle to interact with software that lacks a command-line interface or API. CLI-Anything addresses this by creating lightweight CLI wrappers that expose software functionality in a structured, agent-friendly way. The concept of 'agent-native' software means applications are designed to be controlled by AI agents, not just humans.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/HKUDS/CLI-Anything">GitHub - HKUDS/CLI-Anything: "CLI-Anything: Making ALL ...</a></li>
<li><a href="https://clianything.org/">CLI Anything</a></li>
<li><a href="https://dev.to/clawgear/the-5-principles-behind-agent-native-software-architecture-5d0e">The 5 Principles Behind Agent-Native Software Architecture</a></li>

</ul>
</details>

**Tags**: `#AI Agents`, `#CLI`, `#Software Engineering`, `#Tooling`, `#Open Source`

---