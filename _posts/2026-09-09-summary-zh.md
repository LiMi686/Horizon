---
layout: default
title: "Horizon Summary: 2026-09-09 (ZH)"
date: 2026-09-09
lang: zh
---

> From 59 items, 13 important content pieces were selected

---

1. [OpenAI 声称解决纳维-斯托克斯问题，但遭不当行为指控](#item-1) ⭐️ 10.0/10
2. [vLLM v0.29.0：Model Runner V2 成为默认，新增模型与性能提升](#item-2) ⭐️ 8.0/10
3. [苹果发布首款折叠屏手机 iPhone Duo](#item-3) ⭐️ 8.0/10
4. [Shopify 收购 Tailwind CSS 开发商 Tailwind Labs](#item-4) ⭐️ 8.0/10
5. [GPT-6 Astra、循环 Transformer 与隐藏推理](#item-5) ⭐️ 8.0/10
6. [Qwen 3.8 可能使用了 GPT-5.5 的推理轨迹进行训练](#item-6) ⭐️ 8.0/10
7. [GNU Radio 现可通过 WebAssembly 在浏览器中运行](#item-7) ⭐️ 8.0/10
8. [恶意软件如何在 Google Ads 上做广告](#item-8) ⭐️ 8.0/10
9. [讽刺网站揭露 Claude 过度工程化的循环](#item-9) ⭐️ 8.0/10
10. [陶哲轩警告：AI 正耗尽开放数学问题](#item-10) ⭐️ 8.0/10
11. [Browser-use：让 AI 代理操控网页浏览器](#item-11) ⭐️ 8.0/10
12. [TradingAgents：用于金融交易的多智能体 LLM 框架](#item-12) ⭐️ 8.0/10
13. [HexStrike AI：MCP 服务器通过 150 多种工具自动化渗透测试](#item-13) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 声称解决纳维-斯托克斯问题，但遭不当行为指控](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 10.0/10

2026 年 9 月 8 日，OpenAI 宣布其未发布的模型，利用约一万个 AI 代理的集群，解决了千禧年七大难题之一的纳维-斯托克斯存在性与光滑性问题。该公告伴随着纽约大学数学家 Tristan Buckmaster 的指控，他声称 OpenAI 利用了其与 Levent Alpöge 未发表的工作。 如果得到验证，这将是首个由人工智能解决的千禧年难题，标志着数学和人工智能领域的范式转变。这一争议引发了关于研究伦理、知识产权以及 AI 公司在科学发现中竞争动态的关键问题。 OpenAI 表示，在所有尝试的问题中，代理发送了 490 万条消息，使用了约 3000 亿个输出 token，其中仅纳维-斯托克斯问题就消耗了 1300 亿个 token。该结果已在 Lean 证明助手中形式化，但尚未经过外部数学家或克莱数学研究所的验证，OpenAI 也表示不会领取 100 万美元的奖金。

rss · Simon Willison · Sep 8, 23:55

**背景**: 纳维-斯托克斯存在性与光滑性问题询问描述流体运动的纳维-斯托克斯方程在三维空间中是否总是存在光滑解。这是克莱数学研究所在 2000 年设立的七个千禧年难题之一，每个难题奖金为 100 万美元。该问题与理解湍流密切相关，而湍流是物理学和工程学中一个重大的未解挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>
<li><a href="https://techcrunch.com/2026/09/08/openai-fought-dirty-on-career-making-math-problem-says-nyu-mathematician/">OpenAI fought dirty on career-making math problem, says NYU mathematician | TechCrunch</a></li>

</ul>
</details>

**社区讨论**: 社区讨论既对技术成就表示惊叹，也对伦理问题深感担忧。许多评论者支持 Buckmaster，批评 OpenAI 涉嫌在未适当归属的情况下使用其他团队未发表的工作。其他人则讨论这对数学研究未来的影响，质疑 AI 驱动的发现是否会受到类似争议的困扰。

**标签**: `#AI`, `#Mathematics`, `#OpenAI`, `#Millennium Prize`, `#Navier-Stokes`

---

<a id="item-2"></a>
## [vLLM v0.29.0：Model Runner V2 成为默认，新增模型与性能提升](https://github.com/vllm-project/vllm/releases/tag/v0.29.0) ⭐️ 8.0/10

vLLM v0.29.0 已发布，包含来自 277 位贡献者的 594 次提交。Model Runner V2 现已成为所有模型的默认运行器，并新增了对 Hy4-preview、Qwen3.8-Flash-Next、GraniteSWA 和 Kimi K3 NVFP4 检查点等模型的支持。 此次发布标志着 vLLM 的一个重要架构里程碑，Model Runner V2 成为默认运行器，有望带来更好的性能和可维护性。新增模型支持以及对 Kimi-K3 和 DeepSeek V4 的优化，巩固了 vLLM 作为领先 LLM 推理引擎的地位。 关键技术细节包括：为 KV 缓存自动调整大小而引入的 CUDA graph 内存分析、减少每步 logits 内存的批量分片采样，以及新的默认设置，例如 TP CUDA 组默认启用 FlashInfer all-reduce。破坏性变更包括移除了十个已弃用的模型架构，并弃用了 Python 模块入口点，推荐使用 'vllm serve'。

github · khluu · Sep 9, 08:54

**背景**: vLLM 是一个开源 LLM 推理引擎，以其高吞吐量和灵活性著称。Model Runner V2 是重新设计的执行引擎，旨在提升性能和模块化程度，并逐步取代原有的 Model Runner。多 token 预测（MTP）是一种让模型预测多个未来 token 的技术，常用于通过投机解码加速推理。DeepSeek 稀疏注意力（DSA）是一种学习型稀疏注意力机制，用于 DeepSeek V4 等模型以高效处理长上下文。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vllm-project/vllm/releases">Releases · vllm -project/ vllm</a></li>
<li><a href="https://effloow.com/articles/vllm-production-inference-guide-2026">vLLM in Production: Open-Source LLM Inference Engine... — Effloow</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/mtp/">Multi-Token Prediction (MTP) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#release`, `#Model Runner V2`, `#performance`

---

<a id="item-3"></a>
## [苹果发布首款折叠屏手机 iPhone Duo](https://www.apple.com/iphone-duo/) ⭐️ 8.0/10

苹果在 Apple Park 的九月发布会上推出了其首款折叠屏智能手机 iPhone Duo。该设备配备 7.6 英寸内屏、钛金属框架，256GB 版本起售价为 1,999 美元，将于 10 月 23 日开售。 这标志着苹果进入折叠屏手机市场，比三星首款 Galaxy Fold 晚了七年，预示着行业的重大转变。这可能推动折叠屏设备的更广泛普及，并加剧智能手机制造商之间的竞争。 iPhone Duo 展开后是史上最薄的 iPhone，采用纳米纹理涂层以减少眩光。耐用性是重点，配备钛金属框架和 Ceramic Shield 玻璃，并提供星光白和夜空蓝两种颜色。

hackernews · thecosmicfrog · Sep 9, 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 折叠屏手机利用柔性显示屏，使设备可以展开成更大的屏幕，在便携尺寸中提供类似平板的使用面积。苹果的加入结束了多年的猜测和研发，而三星和华为等竞争对手已在此细分市场立足。iPhone Duo 的大屏幕旨在满足内容观看、游戏和多任务处理需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.apple.com/iphone-duo/">iPhone Duo - Apple</a></li>
<li><a href="https://www.apple.com/newsroom/2026/09/apple-unveils-iphone-duo/">Apple unveils iPhone Duo</a></li>
<li><a href="https://www.wired.com/story/apple-debuts-the-iphone-duo-its-first-folding-iphone/">Apple Debuts the iPhone Duo , Its First Folding iPhone | WIRED</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一。一些人称赞其设计且无明显折痕，另一些人则批评演示风格和手机越来越大的趋势，部分用户希望有更小的设备。此外，也有人对 John Ternus 领导下的变革充满期待。

**标签**: `#Apple`, `#iPhone`, `#folding phone`, `#product launch`, `#mobile technology`

---

<a id="item-4"></a>
## [Shopify 收购 Tailwind CSS 开发商 Tailwind Labs](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购 Tailwind Labs，即广受欢迎的开源 CSS 框架 Tailwind CSS 背后的公司，这一消息在 Tailwind 博客上宣布。此次收购旨在确保 Tailwind 在 MIT 许可下的未来，团队将加入 Shopify。 此次收购意义重大，因为 Tailwind CSS 是最广泛使用的 CSS 框架之一，Shopify 的接管可能影响前端开发工具的未来。同时，它也凸显了 AI 对开发者工具商业模式的日益影响，因为 Tailwind 的模板业务因 AI 生成的代码而受到冲击。 此次收购于 2025 年 2 月 12 日宣布，Tailwind CSS 将继续在 MIT 许可下保持开源。Tailwind Labs 的工程团队将加入 Shopify，但该公司将不再销售其高级 UI 模板，而这是其主要的收入来源。

hackernews · EdwinHoksberg · Sep 9, 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 是一个实用优先的 CSS 框架，允许开发者直接在 HTML 中使用预定义类来设计网站。它因其灵活性和速度而广受欢迎，但其商业模式严重依赖销售高级模板和文档。AI 编码工具的兴起减少了其文档流量和模板需求，导致裁员并最终被收购。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://seekingalpha.com/news/4641301-shopify-acquires-tailwind-labs">Shopify acquires Tailwind Labs (SHOP:NASDAQ) | Seeking Alpha</a></li>
<li><a href="https://betakit.com/tailwind-finds-stable-long-term-home-with-shopify-acquisition/">Tailwind finds “stable, long-term home” with Shopify acquisition | BetaKit</a></li>
<li><a href="https://github.com/tailwindlabs/tailwindcss">GitHub - tailwindlabs/tailwindcss: A utility-first CSS framework for rapid...</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了复杂的情绪：有人对 Tailwind 模板业务的结束表示遗憾，也有人质疑在 AI 驱动的开发时代是否还需要 Tailwind。还有人猜测 Shopify 是在收购团队和品牌，一些评论者称赞 Tailwind 提升了他们的 CSS 技能。

**标签**: `#acquisition`, `#Tailwind CSS`, `#Shopify`, `#AI impact`, `#open source`

---

<a id="item-5"></a>
## [GPT-6 Astra、循环 Transformer 与隐藏推理](https://magazine.sebastianraschka.com/p/gpt-6-astra-looped-transformers-and) ⭐️ 8.0/10

文章讨论了 OpenAI 发布的 GPT-6 Astra，并深入探讨了循环 Transformer 和隐藏推理等先进 AI 概念。文章强调这些话题正在引发社区的高度关注和讨论。 这些主题代表了 AI 领域的前沿发展，可能影响未来的模型架构和推理能力。对于希望保持在 AI 创新前沿的研究人员和从业者来说，理解这些内容至关重要。 GPT-6 Astra 于 2026 年 9 月 3 日发布，次日全面可用。文章还引用了关于思维链和通用 Transformer 的学术研究，将循环 Transformer 与隐藏推理联系起来。

hackernews · ModelForge · Sep 9, 14:37 · [社区讨论](https://news.ycombinator.com/item?id=49627370)

**背景**: 循环 Transformer，也称为循环深度或循环深度共享，通过迭代复用相同的 Transformer 层，在不增加参数数量的情况下实现更深层次的推理。隐藏推理指的是模型输出中未明确显示的内部计算，例如未显式表达的思维链痕迹。GPT-6 Astra 是 OpenAI 最新的大型语言模型，展示了在复杂任务中的先进能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GPT-6_Astra">GPT-6 Astra</a></li>
<li><a href="https://www.emergentmind.com/topics/looped-transformer-architectures">Looped Transformer Architectures</a></li>
<li><a href="https://www.alignmentforum.org/posts/ZrgFfeWuckpwK5Lyi/hidden-reasoning-in-llms-a-taxonomy">Hidden Reasoning in LLMs: A Taxonomy</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂的情绪：一些人对 GPT-6 Astra 的能力印象深刻，而另一些人则指出其性能不稳定。此外，还有关于循环 Transformer 和隐藏推理的理论意义的讨论，并引用了学术论文。

**标签**: `#GPT-6`, `#looped transformers`, `#hidden reasoning`, `#AI research`, `#chain-of-thought`

---

<a id="item-6"></a>
## [Qwen 3.8 可能使用了 GPT-5.5 的推理轨迹进行训练](https://gist.github.com/wsxiaoys/e0286dc6bb624ff5fdf49e7f4c528ba3) ⭐️ 8.0/10

一项分析表明，Qwen 3.8 可能使用了 OpenAI GPT-5.5 的推理轨迹进行训练，因为观察到思维链模式存在重叠。这引发了对潜在蒸馏和基准测试污染的担忧。 如果得到证实，这将表明一个主要的开源模型可能使用了专有推理轨迹进行训练，引发关于模型透明度和公平竞争的伦理与法律问题。这也凸显了人工智能行业中检测和防止蒸馏的日益严峻的挑战。 该分析据称使用了一种技术来恢复 OpenAI 模型的可读思维链，然后将 GPT-5.5 推理的初始部分与 Qwen 3.8 的输出进行比较。值得注意的是，Qwen 3.8（版本 0902）是在一篇详细介绍恢复方法的论文发布后训练的，这可能解释了重叠现象。

hackernews · wsxiaoys · Sep 9, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=49630026)

**背景**: 知识蒸馏是一种技术，较小的模型通过训练于较大“教师”模型的输出来学习。推理轨迹是模型在生成最终答案之前产生的思维链步骤。基准测试污染是指模型的训练数据包含用于评估其性能的基准测试中的示例，从而使结果不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/reasoning-model">What Is a Reasoning Model? | IBM</a></li>
<li><a href="https://www.deeplearning.ai/the-batch/the-problem-with-benchmark-contamination-in-ai/">The Problem with Benchmark Contamination in AI</a></li>

</ul>
</details>

**社区讨论**: 社区评论对方法论进行了辩论，一些人指出唯一可访问的 GPT-5.5 思维来自一篇“窃取思维”的论文，而 Qwen 3.8 是在该论文发布后训练的。其他人质疑重叠是否可能源于两个模型都在相同的基准测试解决方案上训练，而非直接蒸馏。

**标签**: `#AI`, `#LLM`, `#distillation`, `#reasoning`, `#safety`

---

<a id="item-7"></a>
## [GNU Radio 现可通过 WebAssembly 在浏览器中运行](https://gnuradioworld.com/) ⭐️ 8.0/10

GNU Radio，一个流行的开源软件定义无线电（SDR）和数字信号处理（DSP）工具包，现在通过 WebAssembly（WASM）编译可直接在网页浏览器中使用。用户无需安装原生软件即可构建和运行信号处理流程图。 这一进展大大降低了 SDR 和 DSP 教育与实验的门槛，因为用户现在只需一个网页浏览器即可尝试 GNU Radio。这可能会扩大社区，让学生、爱好者和专业人士更容易进行动手信号处理实践。 浏览器版本利用 WebAssembly 在沙盒环境中运行 GNU Radio 的核心处理，并可通过 WebUSB 与 USRP B200 等硬件交互。一些用户报告了可用性问题，例如描述不清晰和演示中缺乏音频输出，但该项目在交互式学习方面显示出潜力。

hackernews · kristianpaul · Sep 9, 15:53 · [社区讨论](https://news.ycombinator.com/item?id=49628576)

**背景**: GNU Radio 是一个免费的软件开发工具包，提供信号处理模块来实现软件定义无线电。传统上，它需要在 Linux、macOS 或 Windows 上进行原生安装。WebAssembly 是一种二进制指令格式，允许用 C++ 等语言编写的高性能代码在网页浏览器中运行，这使得将 GNU Radio 等复杂应用移植到网页成为可能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Software-defined_radio">Software-defined radio - Wikipedia</a></li>
<li><a href="https://webassembly.org/features/">Feature Status - WebAssembly</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区总体反应积极，用户对该项目表示兴奋，并分享了相关实验，例如在浏览器中运行的宽带射频扫描仪和 AX.25 解码器。一些用户指出了可用性问题，包括描述不清晰和缺乏音频输出，一位之前觉得 GNU Radio 难以理解的用户表示有兴趣再试一次。

**标签**: `#GNU Radio`, `#WebAssembly`, `#SDR`, `#DSP`, `#Browser`

---

<a id="item-8"></a>
## [恶意软件如何在 Google Ads 上做广告](https://xlii.space/eng/malicious-software-on-google-ads/) ⭐️ 8.0/10

文章详细介绍了绕过 Google Ads 自动审核流程分发恶意软件的方法，暴露了内容审核的系统性缺陷。作者的账户曾被暂时封禁，但在公开投诉后恢复。 作者使用伪装和混淆等技术来逃避检测，并指出 Google 的自动化系统在许多情况下缺乏人工审核。该账户仅在问题在 Hacker News 上引起关注后才被恢复。

hackernews · xlii · Sep 9, 11:43 · [社区讨论](https://news.ycombinator.com/item?id=49624856)

**背景**: 恶意广告（malvertising）涉及利用在线广告分发恶意软件，通常通过诱骗用户点击恶意链接。Google 等平台通常使用自动化内容审核系统大规模审查广告，但复杂的攻击者可以绕过这些系统。伪装（cloaking）等技术，即广告对审核者显示良性内容而对用户显示恶意内容，在网络安全社区中广为人知。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybersecuritynews.com/malvertising-is-moving-from-deceptive-content-to-weaponized-infrastructure/">Malvertising Is Moving From Deceptive Content to Weaponized Infrastructure</a></li>
<li><a href="https://attack.mitre.org/techniques/T1583/008/">Acquire Infrastructure: Malvertising, Sub-technique T1583.008 - Enterprise | MITRE ATT&CK®</a></li>
<li><a href="https://getstream.io/blog/moderation-circumvention-tactics/">Moderation Evasion Tactics: Algospeak, Obfuscation & More</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Google 的自动化系统表示不满，分享了不公平拒绝和诈骗广告的个人经历。一些人指出，Google 缺乏人工监督是更广泛的企业趋势，而作者的更新表明，公开施压是解决问题的必要条件。

**标签**: `#cybersecurity`, `#google ads`, `#malvertising`, `#online safety`, `#automated moderation`

---

<a id="item-9"></a>
## [讽刺网站揭露 Claude 过度工程化的循环](https://opusfived.dev/) ⭐️ 8.0/10

一个讽刺网站 opusfived.dev 幽默地描绘了用户在使用像 Claude 这样的 AI 编程助手时遇到的令人沮丧的循环，例如反复要求更改按钮颜色。该网站在 Hacker News 上引发了病毒式讨论，获得了 959 分和 386 条评论。 这一讽刺作品凸显了开发者与 AI 交互中的真实痛点，引发了关于 AI 编程助手实际效用和可靠性的讨论。它强调了这些日益流行的工具在用户体验和可预测行为方面需要改进。 该网站是一个可选的游戏，用户可以关闭，但许多人觉得它真实得令人恼火。评论者指出，虽然某些循环有所减少，但模型现在倾向于“过度热心”，常常过度设计解决方案或提出过多的澄清问题。

hackernews · matthieu_bl · Sep 9, 09:39 · [社区讨论](https://news.ycombinator.com/item?id=49623754)

**背景**: 像 Claude 这样的 AI 编程助手使用大型语言模型根据自然语言提示生成代码。虽然它们功能强大，但有时会误解指令或陷入迭代循环，导致用户沮丧。这一讽刺作品之所以引起共鸣，是因为它夸张了常见体验，例如助手反复要求确认或进行不必要的更改。

**社区讨论**: 评论者分享了不同的体验：有些人认为这一讽刺作品很准确，而另一些人则报告说使用 Codex 等工具时循环较少。一个关键观点是，AI 交互遵循“可变奖励计划”，类似于赌博，尽管偶尔失败，仍能让用户保持参与。

**标签**: `#AI coding assistants`, `#Claude`, `#satire`, `#developer experience`, `#LLM behavior`

---

<a id="item-10"></a>
## [陶哲轩警告：AI 正耗尽开放数学问题](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 8.0/10

著名数学家陶哲轩公开警告，AI 驱动的努力正不可持续地开采数量有限的、富有成果的开放数学问题，可能在新的问题被发现之前就将它们耗尽。他还提醒，担心 AI 抢先完成研究可能会使数学家不愿分享有前景的研究方向，从而逆转数百年来的开放科学传统。 这一警告凸显了学术界一个关键的新问题：AI 可能耗尽共享的研究问题并抑制合作，从而破坏开放科学的基础。这对 AI 伦理、研究激励以及数学发现的未来速度具有重大影响，影响研究人员、资助机构以及更广泛的科学界。 陶哲轩指出，即使有人正在研究某个问题的传闻，也可能引发大规模的 AI 驱动努力，在原始研究者充分发挥潜力之前就将其“攻克”。他认为，好的开放问题稀缺且更替缓慢，当被 AI 不加区分地开采时，它们就成为一种不可再生资源。

rss · Simon Willison · Sep 9, 00:20

**背景**: 数学中的开放问题是指尚未解决的难题，它们引导研究并激发新理论。传统上，数学家公开分享这些问题以促进合作和加速进展。然而，随着能够解决复杂数学任务的强大 AI 系统的兴起，人们越来越担心这些共享问题可能被 AI 迅速解决，从而减少人类研究者的机会，并抑制公开分享。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://panews.io/articles/01a083c5-6d5a-7384-be70-d9eee539859c">Terence Tao Warns: AI Is Unsustainably 'Mining' Open Mathematical Problems | PANews English</a></li>
<li><a href="https://ai-tldr.dev/releases/terry-tao-mined-open-problems-sep8/">Terence Tao — good open math problems are a… | AI/TLDR</a></li>
<li><a href="https://decrypt.co/377818/ai-math-best-problems-terence-tao">AI Is Solving Math's Best Problems Faster Than They Can Be Replaced, Terence Tao Warns - Decrypt</a></li>

</ul>
</details>

**标签**: `#AI ethics`, `#open science`, `#mathematics`, `#research incentives`

---

<a id="item-11"></a>
## [Browser-use：让 AI 代理操控网页浏览器](https://github.com/browser-use/browser-use) ⭐️ 8.0/10

Browser-use 是一个热门的 GitHub 项目，它让 AI 代理能够像人类一样操作网页浏览器，执行填写表单、点击按钮和提取数据等任务。它提供开源库和云服务，云服务包含托管代理（V4），并为符合条件的新用户提供 15 美元积分。 该项目代表了 AI 驱动的网页自动化的重要一步，可能改变开发者构建网页抓取、测试和个人助理工具的方式。它在 GitHub 上的热度表明社区兴趣浓厚，可能加速代理式 AI 在日常网页任务中的应用。 该仓库包含示例代码，如填写工作申请和将关注者数据导出为 CSV。它还提供带有托管代理的云服务，并且积极开发基于 Rust 的核心以提升性能。

rss · GitHub Trending - Daily (All) · Sep 9, 23:44

**背景**: 传统的浏览器自动化依赖于像 Selenium 这样的脚本工具，但 browser-use 利用大型语言模型（LLM）来理解自然语言指令并动态执行操作。这种方法通常被称为“代理式 AI”，它允许更灵活和自适应的自动化，而无需预定义脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/browser-use/browser-use">GitHub - browser - use / browser - use : Make websites accessible...</a></li>
<li><a href="https://github.com/browser-use/awesome-projects">GitHub - browser - use /awesome- projects : List of Open Source...</a></li>
<li><a href="https://www.arnlweb.com/browser-use-github-repository/">Browser Use GitHub Repository: Complete Guide</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#browser automation`, `#web scraping`, `#LLM`, `#GitHub trending`

---

<a id="item-12"></a>
## [TradingAgents：用于金融交易的多智能体 LLM 框架](https://github.com/TauricResearch/TradingAgents) ⭐️ 8.0/10

TradingAgents，一个用于金融交易的多智能体 LLM 框架，已发布并在 GitHub 上流行，附有 arXiv 论文（2412.20138）。该框架通过专业智能体模拟专业交易公司，用于分析、交易和风险管理。 该框架代表了多智能体 LLM 系统在金融领域的新应用，可能使复杂的交易策略大众化，并影响 AI 驱动的金融。其在 GitHub 上的流行表明社区对基于 AI 的交易解决方案有浓厚兴趣。 该框架包括基本面分析师、情绪分析师、技术分析师、研究员、交易员和风险经理等角色，模拟真实交易公司。最新版本（v0.4.0）增加了前瞻/时点修复、GPT-5.6 和 GLM-5.3 等新模型，并支持多个数据供应商和提供商。

rss · GitHub Trending - Python · Sep 9, 23:44

**背景**: 多智能体 LLM 框架涉及多个具有专业角色的 AI 智能体协作解决复杂任务。在交易中，这些智能体可以分析不同类型的数据、辩论投资论点并管理风险，旨在比单智能体系统更好地改进决策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/TauricResearch/TradingAgents">TauricResearch/ TradingAgents : TradingAgents : Multi - Agents LLM ...</a></li>
<li><a href="https://arxiv.org/abs/2412.20138">[ 2412 . 20138 ] TradingAgents: Multi-Agents LLM Financial Trading...</a></li>
<li><a href="https://tradingagents-ai.github.io/">TradingAgents : Multi - Agents LLM Financial Trading Framework</a></li>

</ul>
</details>

**标签**: `#LLM`, `#multi-agent`, `#finance`, `#trading`, `#GitHub`

---

<a id="item-13"></a>
## [HexStrike AI：MCP 服务器通过 150 多种工具自动化渗透测试](https://github.com/0x4m4/hexstrike-ai) ⭐️ 8.0/10

HexStrike AI MCP Agents v6.0 已发布，引入了一个 MCP 服务器，使 Claude、GPT 和 Copilot 等 AI 代理能够自主运行 150 多种网络安全工具，用于自动化渗透测试、漏洞发现和漏洞赏金自动化。该平台包含 12 个以上的自主 AI 代理，由 OTT Cybersecurity LLC 开发。 该项目弥合了 AI 代理与现实世界进攻性安全之间的差距，可能自动化重复的渗透测试任务并加速漏洞发现。它可能通过使高级安全测试更易用和高效，对网络安全行业产生重大影响，但也引发了关于滥用和人类渗透测试人员角色的担忧。 该平台支持 Python 3.8+，采用 MIT 许可证，并与 MCP 兼容，可与 Claude 和 ChatGPT 等客户端集成。它采用多代理架构，具备智能决策和漏洞情报功能，可在 GitHub 上获取，并有专门网站 hexstrike.com。

rss · GitHub Trending - Python · Sep 9, 23:44

**背景**: MCP（模型上下文协议）是一种开放协议，允许 Claude 和 ChatGPT 等 AI 助手与外部软件系统连接，使其能够访问工具和数据。自动化渗透测试使用软件模拟黑客攻击并识别漏洞，补充手动测试。HexStrike AI 利用 MCP 让 AI 代理自主编排这些安全工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modelcontextprotocol.io/">What is the Model Context Protocol ( MCP )? - Model Context Protocol</a></li>
<li><a href="https://www.getastra.com/blog/penetration-testing/automated/">Automated Penetration testing 101 ( How It Works + ROI You Can...)</a></li>

</ul>
</details>

**标签**: `#AI`, `#Cybersecurity`, `#MCP`, `#Automation`, `#Pentesting`

---