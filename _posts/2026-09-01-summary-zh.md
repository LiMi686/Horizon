---
layout: default
title: "Horizon Summary: 2026-09-01 (ZH)"
date: 2026-09-01
lang: zh
---

> From 112 items, 23 important content pieces were selected

---

1. [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1，提升写作与科学能力](#item-1) ⭐️ 9.0/10
2. [1.5 小时训练的小型 Transformer 在 ARC 上超越众多 LLM](#item-2) ⭐️ 8.0/10
3. [苹果在 OpenAI 商业秘密诉讼中出示取证证据](#item-3) ⭐️ 8.0/10
4. [Python 3.15.0 候选版本 2 发布](#item-4) ⭐️ 8.0/10
5. [Heretic：语言模型的全自动去审查工具](#item-5) ⭐️ 8.0/10
6. [前沿大语言模型在肿瘤决策中存在共同盲区](#item-6) ⭐️ 8.0/10
7. [智能体 AI 与调查注意力检查：新的数据质量威胁](#item-7) ⭐️ 8.0/10
8. [CDPR：用于成本感知诊断的反事实优势信用分配](#item-8) ⭐️ 8.0/10
9. [SHAPE 框架通过启发式解码 LLM 数学推理](#item-9) ⭐️ 8.0/10
10. [曲率密码分析提取 Transformer 前馈网络隐藏方向](#item-10) ⭐️ 8.0/10
11. [ESNN：用于几何传输的等变层状神经网络](#item-11) ⭐️ 8.0/10
12. [停止向量：通过因果引导减少大模型过度思考](#item-12) ⭐️ 8.0/10
13. [保守混合图网络实现过程系统零样本迁移](#item-13) ⭐️ 8.0/10
14. [通用编码计算：面向掉队者的学习理论框架](#item-14) ⭐️ 8.0/10
15. [SemKV：基于质量悬崖的混合精度 KV 缓存量化方法](#item-15) ⭐️ 8.0/10
16. [参数化多模态用户记忆：存储字幕无法承载的信息](#item-16) ⭐️ 8.0/10
17. [LLM 同行评审审计揭示评分虚高与偏见](#item-17) ⭐️ 8.0/10
18. [MIRAGE-CAD：多模态生成可执行 CAD 程序](#item-18) ⭐️ 8.0/10
19. [交互增长复杂度刻画离散扩散采样](#item-19) ⭐️ 8.0/10
20. [Jigsaw-CRL：从碎片化多客户端干预中恢复全局潜在因果顺序](#item-20) ⭐️ 8.0/10
21. [秩受限矩阵 LASSO 全局最小值的尖锐 RIP 阈值](#item-21) ⭐️ 8.0/10
22. [深度潜变量框架联合建模缺失、误差与异质性](#item-22) ⭐️ 8.0/10
23. [令牌预测组织表示：一个统计框架](#item-23) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Fable 5.1 和 Mythos 5.1，提升写作与科学能力](https://www.anthropic.com/claude-fable-and-mythos-5-1) ⭐️ 9.0/10

Anthropic 发布了 Claude Fable 5.1 和 Claude Mythos 5.1，在原有 Fable 5 的基础上提升了写作风格、增强了科学性能，并将缓存读取价格从每百万 token 1 美元降至 0.25 美元。新模型还引入了多项新增功能，包括按消息控制推理努力和回合级系统消息。 此次发布大幅降低了依赖提示缓存的 Claude 应用成本，使其在与其他 LLM 提供商的竞争中更具优势。写作风格和科学能力的提升可能吸引更多创意和研究领域的用户，从而可能改变市场格局。 缓存读取价格从每百万 token 1 美元降至 0.25 美元，使 Fable 5.1 的缓存读取成本仅为 Opus（每百万 token 0.5 美元）的一半。三项破坏性变更修复了与思维链泄露相关的安全问题，包括阻止强制工具使用暴露原始推理，并限制对思考块的访问。

hackernews · denysvitali · Sep 1, 17:53 · [社区讨论](https://news.ycombinator.com/item?id=49525378)

**背景**: Claude Fable 5.1 是 Anthropic 推出的大型语言模型，专注于写作质量和科学推理等通用任务。提示缓存是一种存储先前计算过的 token 以减少重复 API 调用延迟和成本的技术。新模型还包括 Claude Mythos 5.1，这是专为网络安全和生物学研究设计的变体，仅限受邀用户使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/models/fable-5-1/overview">Claude Fable 5.1 - Claude Platform Docs</a></li>
<li><a href="https://www.anthropic.com/claude-fable-and-mythos-5-1">Introducing Claude Fable 5.1 and Claude Mythos 5.1 \ Anthropic \ Anthropic</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区成员对改进的写作风格表示赞赏，一位 Anthropic 员工称其听起来更自然，对风格指令的响应也更好。一些用户讨论了价格下调，将其归因于缓存读取价格的降低，并争论模型在科学基准之外是否真正有所改进。其他人则强调了与思维链泄露相关的安全补丁。

**标签**: `#AI`, `#Anthropic`, `#Claude`, `#LLM`, `#Machine Learning`

---

<a id="item-2"></a>
## [1.5 小时训练的小型 Transformer 在 ARC 上超越众多 LLM](https://mvakde.github.io/blog/44-on-arc-1/) ⭐️ 8.0/10

一个从头开始训练仅 1.5 小时的小型 Transformer 在 ARC 基准上取得了有竞争力的结果，超越了众多大型语言模型。作者 evilmathkid 在 Hacker News 上分享了这一结果，引发了关于样本效率和训练方法的讨论。 这挑战了普遍认为复杂推理任务需要大规模模型和巨大计算资源的扩展范式。它表明高效的架构和训练策略也能取得强大性能，可能使 AI 研究民主化并降低环境成本。 该模型是一个小型自回归 Transformer，而非 LLM，并在 ARC 基准的训练集上进行了训练。作者指出，性能提升来自现代架构选择（如 SwiGlu、RMSNorm）、更好的数据洗牌以及扩展到 8 层，但强调在评估谜题上训练并非“测试训练”，因为未使用标签。

hackernews · porridgeraisin · Sep 1, 09:52 · [社区讨论](https://news.ycombinator.com/item?id=49519939)

**背景**: ARC（抽象与推理语料库）基准旨在衡量 AI 获取技能和抽象推理的能力，其任务对人类容易但对 AI 困难。传统上，只有大型语言模型或其微调版本才能扩展此基准，且通常需要巨大的训练成本。这项工作表明，小型 Transformer 可以用最少的计算量取得有竞争力的结果，凸显了样本高效方法的潜力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arcprize.org/">ARC Prize</a></li>
<li><a href="https://arcprize.org/arc-agi">ARC Prize - What is ARC-AGI?</a></li>
<li><a href="https://lab42.global/arc/">About ARC – Lab42</a></li>

</ul>
</details>

**社区讨论**: 作者积极参与讨论，澄清该模型不是 LLM，并针对“测试训练”的指责为训练方法辩护。评论者如 usernametaken29 称赞了对样本效率的关注，但警告不要将“挤柠檬”作为最后手段。其他人祝贺作者，指出这一成就的重要性，甚至提到作者自救的个人故事。

**标签**: `#transformer`, `#ARC`, `#efficiency`, `#deep learning`, `#research`

---

<a id="item-3"></a>
## [苹果在 OpenAI 商业秘密诉讼中出示取证证据](https://9to5mac.com/2026/08/31/apple-openai-forensic-macbook-evidence/) ⭐️ 8.0/10

苹果在其对 OpenAI 的诉讼中出示了取证证据，指控前员工刘先生将在苹果窃取的商业秘密（包括一份机密电路原理图）用于其在 OpenAI 的工作。证据包括他在 LTspice 模拟中使用该原理图，以及在得知苹果调查后试图销毁证据的行为。 此案可能为商业秘密法如何适用于 AI 训练和使用开创先例，因为苹果主张将商业秘密输入 AI 模型会产生不可逆转且持续传播的使用。结果可能影响企业在 AI 时代如何保护专有数据，以及 AI 开发者如何处理敏感信息。 苹果还要求访问刘先生使用过的一台 Mac mini，该设备通过 iCloud 同步到了他从苹果带走的 MacBook 上。诉讼还涉及 io 公司，该公司由前苹果员工创立并被 OpenAI 收购，被指控使用了苹果的金属表面处理技术。

hackernews · colinprince · Sep 1, 20:19 · [社区讨论](https://news.ycombinator.com/item?id=49527573)

**背景**: 商业秘密诉讼通常依赖数字取证来发现盗用证据，因为电子数据会留下可分析的痕迹。在此案中，苹果的取证证据包括 iCloud 同步数据和模拟文件，凸显了数字痕迹如何将个人和企业设备联系起来。关于 AI 模型从商业秘密中“学习”并传播它们的法律论点具有新颖性，可能对 AI 发展产生广泛影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/cy8w379e091o">Apple sues OpenAI, its employees claiming theft of trade secrets</a></li>
<li><a href="https://techcrunch.com/2026/07/13/the-wildest-allegations-in-apples-trade-secrets-lawsuit-against-openai/">The wildest allegations in Apple’s trade secrets lawsuit against OpenAI | TechCrunch</a></li>
<li><a href="https://www.cnbc.com/2026/07/10/apple-openai-lawsuit-trade-secrets.html">Apple sues OpenAI alleging trade secret theft, says scheme was 'at every level'</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了法律和隐私影响，有人指出关于 AI 从商业秘密中学习的论点具有重大影响。其他人对公司设备上 iCloud 同步个人数据的隐私影响表示好奇，还有评论者将其与可口可乐配方案相提并论，建议公司在收到被盗秘密时应采取道德行为。

**标签**: `#Apple`, `#OpenAI`, `#trade secrets`, `#AI`, `#legal`

---

<a id="item-4"></a>
## [Python 3.15.0 候选版本 2 发布](https://simonwillison.net/2026/Sep/1/python-315-rc-2/) ⭐️ 8.0/10

Python 3.15.0 候选版本 2 (RC2) 已由发布经理 Hugo van Kemenade 宣布，这是 10 月稳定版发布前的最终候选版本。强烈鼓励第三方维护者准备其项目并在 PyPI 上发布 Python 3.15 的 wheel 包以确保兼容性。 此候选版本是 Python 生态系统的关键里程碑，标志着主要版本发布前的最后阶段。它向第三方维护者发出了明确的行动号召，要求他们进行测试并构建 wheel 包，以确保 Python 3.15 正式发布时整个社区能够平稳过渡。 在候选版本阶段，从 RC2 到最终版本之间只允许经过审查的错误修复。针对 Python 3.15.0 候选版本构建的二进制 wheel 包将与 Python 3.15 的未来版本兼容，并且该 RC 版本尚不可用于 GitHub Actions，但可以通过在 actions/setup-python 中使用 allow-prereleases 和 check-latest 标志进行测试。

rss · Simon Willison · Sep 1, 14:59

**背景**: Python 在最终发布前使用候选版本 (RC) 阶段来稳定代码库，此阶段只允许错误修复。Wheel 是 Python 的标准二进制分发格式，无需编译即可安装，确保针对 RC 构建的 wheel 包与最终版本兼容。发布经理的公告强调了在此期间进行测试的重要性，以避免发布错误，如过去 Python 3.10 中的事件所示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.python.org/2026/09/python-3150-rc2/">Python 3 . 15 .0 candidate 2 is here! | Python Insider</a></li>
<li><a href="https://packaging.python.org/specifications/binary-distribution-format/">Binary distribution format - Python Packaging User Guide</a></li>
<li><a href="https://blog.trailofbits.com/2022/11/15/python-wheels-abi-abi3audit/">ABI compatibility in Python: How hard could it be? - The Trail of Bits Blog</a></li>

</ul>
</details>

**标签**: `#Python`, `#Release`, `#Software Engineering`, `#Ecosystem`

---

<a id="item-5"></a>
## [Heretic：语言模型的全自动去审查工具](https://github.com/p-e-w/heretic) ⭐️ 8.0/10

Heretic 是 p-e-w 开发的新开源工具，能够全自动地从基于 Transformer 的语言模型中移除审查（即安全对齐），无需昂贵的后训练。它结合了先进的定向消融（abliteration）技术和基于 Optuna 的 TPE 参数优化器，达到了与人类专家手动 abliteration 相当的效果。 该项目涉及一个具有争议但技术意义重大的话题：LLM 的自动去审查。它可能使“未审查”模型的创建变得大众化，引发关于模型对齐和潜在滥用的重要伦理与安全问题，同时也推动了模型可解释性和控制方面的研究。 Heretic 支持大多数稠密模型，包括多模态和 MoE 架构，甚至支持像 Qwen3.5 这样的混合模型，但不支持纯状态空间模型。它通过同时最小化拒绝次数和与原始模型的 KL 散度来工作，在去除拒绝的同时保留智能。该工具设计为任何熟悉命令行程序的人都能使用，无需深入了解 Transformer 内部结构。

rss · GitHub Trending - Daily (All) · Sep 1, 23:43

**背景**: 语言模型通常经过“对齐”处理，以拒绝有害提示，这一过程称为安全对齐。Abliteration 是一种通过修改模型权重来移除这种对齐的技术，通常由专家手动完成。Heretic 利用优化算法自动化了这一过程，使其对更广泛的用户群体可用。该项目在 GitHub Trending 上受到关注，并拥有官方网站和社区渠道。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/p-e-w/heretic">GitHub - p-e-w/heretic: Fully automatic censorship removal for language models · GitHub</a></li>
<li><a href="https://explainx.ai/blog/heretic-llm-abliteration-guide-2026">Heretic: Complete Guide to Automatic LLM Censorship Removal | explainx.ai Blog | explainx.ai</a></li>
<li><a href="https://aitoolly.com/ai-news/article/2026-05-29-heretic-new-github-project-aims-for-automated-censorship-removal-in-language-models">Heretic: Automated Censorship Removal for Language Models | AIToolly</a></li>

</ul>
</details>

**标签**: `#AI`, `#language models`, `#censorship`, `#open source`, `#ethics`

---

<a id="item-6"></a>
## [前沿大语言模型在肿瘤决策中存在共同盲区](https://arxiv.org/abs/2608.28592) ⭐️ 8.0/10

一项新研究引入了肿瘤决策边界基准（ODBB），包含来自 NCCN 指南和结直肠癌病例的 2005 个肿瘤决策点，并评估了 2025 年 6 月至 2026 年 4 月间发布的九个前沿大语言模型。结果显示，42.1%的汇总决策没有任何模型能正确回答，揭示了一个集体能力边界。 这一发现挑战了仅仅通过组合更多模型或增加训练数据就能克服 LLM 在临床决策中局限性的假设。它揭示了临床元判断中的一个根本性盲区，可能需要架构上的改变，从而影响 LLM 在医疗领域的部署。 该研究使用了完全确定性的评分器，不涉及 LLM 推理，将输出分类为 14 种失败类型，并由两位肿瘤学家独立验证（Cohen 加权 kappa 分别为 0.939 和 0.790）。值得注意的是，两个为果断性调优的模型（GPT-5.5、Gemini 3.1 Pro Preview）做出不安全承诺的频率是七个谨慎模型的 3 到 5 倍，但得分并未更高。

rss · arXiv - AI · Sep 1, 04:00

**背景**: 大语言模型（LLM）在医学知识考试中取得了高分，但现实世界的肿瘤学涉及在不确定性下的序列决策，而不仅仅是事实回忆。现有基准通常衡量知识回忆，在评估决策路径能力方面存在空白。ODBB 基准通过关注符合指南的决策点来弥补这一空白，研究建议进步需要能够检测模型何时达到能力边界并将决策路由给临床医生的架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smartchunks.com/frontier-ai-oncology-decision-benchmark-shared-blind-spot/">Frontier AI Models Share The Same Blind Spot In Cancer Decisions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Large_language_model">Large language model - Wikipedia</a></li>
<li><a href="https://www.nccn.org/guidelines/nccn-guidelines">NCCN Guidelines</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#medical AI`, `#oncology`, `#benchmark`, `#decision-making`

---

<a id="item-7"></a>
## [智能体 AI 与调查注意力检查：新的数据质量威胁](https://arxiv.org/abs/2608.28597) ⭐️ 8.0/10

一篇新的 arXiv 论文表明，智能体 AI 系统可以利用在线调查中的结构性漏洞（如暴露的 DOM 元数据和可预测的选项编码）来通过注意力检查，而无需真正理解内容。该研究在受控的调查沙盒中评估了具有多模态输入和基于工具的网络交互的单智能体架构。 这项研究凸显了在线调查数据完整性面临的日益严重的威胁，而在线调查数据是社会科学、市场营销和公共政策研究的基础。随着智能体 AI 能力的增强，传统的注意力检查可能不再足够，需要新的防御策略来保护数据质量。 该论文从攻击和防御两个角度进行分析：展示了智能体如何仅通过结构化解析就能解决注意力检查，并提出了 DOM 元数据混淆作为缓解措施。它评估了多个开源语言和多模态模型，以评估能力和编排效果。

rss · arXiv - AI · Sep 1, 04:00

**背景**: 在线调查通常使用注意力检查来筛选未认真参与的受访者，以确保数据质量。智能体 AI 是指由大型语言模型（LLM）驱动的自主系统，能够使用工具规划和执行任务。DOM 元数据漏洞涉及暴露的 HTML 属性，这些属性可能泄露语义信息，智能体可利用这些信息推断正确答案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.cloud.google.com/architecture/choose-agentic-ai-architecture-components">Choose your agentic AI architecture components | Cloud Architecture Center | Google Cloud Documentation</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-architecture">What Is Agentic Architecture? | IBM</a></li>
<li><a href="https://portswigger.net/web-security/dom-based">DOM-based vulnerabilities | Web Security Academy</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#data quality`, `#online surveys`, `#LLM`, `#security`

---

<a id="item-8"></a>
## [CDPR：用于成本感知诊断的反事实优势信用分配](https://arxiv.org/abs/2608.28599) ⭐️ 8.0/10

该论文提出了 CDPR（反事实诊断过程奖励），一种用于成本感知的序贯医学诊断的新型强化学习方法，无需专家标签或学习到的评论者。它将 CDPR 集成到 GRPO 中，并在 MIMIC-IV、ClinicalBench 和私有医院数据集上展示了诊断准确率的提高，同时减少了检查次数和成本。 这项工作解决了医学诊断中的一个关键差距，即大多数模型忽略了测试价值与成本之间的权衡。通过在长轨迹中实现无需专家标签的高效信用分配，CDPR 可以使 AI 驱动的诊断在实际临床环境中更加实用和经济高效，可能减少不必要的医疗支出。 CDPR 利用策略动作分布的不确定性来识别犹豫状态，然后通过在平衡正确性、测试数量、成本和不可行请求的效用下进行短滚动，对所选动作相对于替代方案的优势进行评分。滚动缓存重用批内轨迹以保持较低的计算成本，并将该方法集成到 GRPO 中进行训练。

rss · arXiv - AI · Sep 1, 04:00

**背景**: 临床诊断本质上是序贯且成本感知的，但大多数医学语言模型将其视为一次性分类任务。强化学习提供了一种建模这种序贯决策过程的方法，但信用分配具有挑战性，因为唯一可靠的奖励出现在长轨迹的末端。反事实方法通过将所选动作与替代动作进行比较来估计其优势，这可以减少策略梯度估计中的方差。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28599">[2608.28599] CDPR : Counterfactual Advantage-based Credit...</a></li>
<li><a href="https://arxiv.org/html/2605.16302v1">Reducing Credit Assignment Variance via Counterfactual Reasoning Paths</a></li>
<li><a href="http://proceedings.mlr.press/v139/mesnard21a/mesnard21a.pdf">Counterfactual Credit Assignment in Model-Free Reinforcement Learning</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#medical diagnosis`, `#credit assignment`, `#cost-aware decision making`, `#arXiv`

---

<a id="item-9"></a>
## [SHAPE 框架通过启发式解码 LLM 数学推理](https://arxiv.org/abs/2608.28600) ⭐️ 8.0/10

该论文引入了 SHAPE 框架，利用数学教育中的语义空间和启发式来分析 LLM 的思维链（CoT）轨迹。研究发现，数学启发式比传统的 CoT 特征更能解释答案的正确性，并且模型倾向于将推理集中在少数语义空间中，这与人类行为相似。 这项工作为解释 LLM 推理提供了一个有理论基础的诊断框架，对于提高模型在数学任务中的透明度和可靠性至关重要。它还通过促进多样化的启发式，为 LLM 的后训练提供了新途径，可能提高数学推理基准的准确性。 SHAPE 使用两个视角：语义空间（如代数、几何）和启发式（如简化、倒推）。研究发现，强化学习会导致启发式使用的模式寻求，而通过多样化启发式进行后训练可以提高准确性。代码已在 GitHub 上提供。

rss · arXiv - AI · Sep 1, 04:00

**背景**: 思维链（CoT）提示是一种从大型语言模型（LLM）中引出中间推理步骤的技术，显著提高了它们在复杂推理任务上的表现。然而，其内部推理模式在很大程度上仍不透明。SHAPE 利用数学教育中的概念来分析这些模式，提供了一种新的可解释性视角。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28600">[2608.28600] SHAPE of Chain - of - Thought in Math Reasoning</a></li>
<li><a href="https://huggingface.co/papers/2608.28600">Paper page - SHAPE of Chain - of - Thought in Math Reasoning</a></li>
<li><a href="https://www.promptingguide.ai/techniques/cot">Chain - of - Thought Prompting | Prompt Engineering Guide</a></li>

</ul>
</details>

**标签**: `#LLM`, `#Chain-of-Thought`, `#Mathematical Reasoning`, `#Interpretability`, `#arXiv`

---

<a id="item-10"></a>
## [曲率密码分析提取 Transformer 前馈网络隐藏方向](https://arxiv.org/abs/2608.28843) ⭐️ 8.0/10

该论文提出了一种新颖的模型提取攻击，利用曲率（Hessian）信息仅通过少量黑盒查询即可恢复平滑 Transformer 前馈网络（FFN）中的隐藏方向。在 CIFAR-10 视觉 Transformer 上，仅需 16 个投影 Hessian（8193 次查询）即可对 GELU 和 SiLU 激活实现平均余弦对齐超过 0.94。 这项工作揭示了 Transformer 模型中的新安全漏洞，表明仅通过黑盒访问即可提取隐藏的内部结构，这对模型隐私和知识产权保护具有重大影响。同时，它为可解释性提供了新工具，因为恢复的结构可用于功能提取和高保真替代模型。 该攻击利用二阶泄漏通道，其中投影输入 Hessian 形成隐藏对称秩一因子的混合。该方法使用向量输出模板重用将查询成本降低 16 倍，并通过调整有限差分步长来对抗输出舍入和高斯噪声，将对齐恢复到 0.9603 和 0.9398。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: 模型提取攻击通常依赖输入输出行为来复制模型的功能，但本文表明二阶信息（曲率）可以揭示仅靠行为保真度无法获得的内部参数几何。该攻击在选定输入原始输出预言机下运行，意味着攻击者可以用任意输入查询模型并获得原始输出，但无法访问参数、梯度或内部激活。恢复的结构支持功能提取，使攻击者能够构建具有高度一致性的替代模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28843">[2608.28843] Curvature Cryptanalysis of Smooth Transformer Feed-Forward Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Linear_cryptanalysis">Linear cryptanalysis - Wikipedia</a></li>

</ul>
</details>

**标签**: `#model extraction`, `#transformer`, `#Hessian`, `#security`, `#deep learning`

---

<a id="item-11"></a>
## [ESNN：用于几何传输的等变层状神经网络](https://arxiv.org/abs/2608.28853) ⭐️ 8.0/10

该论文提出了等变层状神经网络（ESNN），它在保持精确欧几里得等变性的同时，学习图上相邻向量特征之间的有向矩阵值传输。它提供了理论表征，表明当相对位移是唯一的协变输入时，任何线性 O(n)-等变映射都可以分解为独立的径向和切向分量。 ESNN 通过将额外的几何灵活性置于边传输中，而不是增加表示阶数，解决了第一阶等变图神经网络的一个关键限制。这为表达性等变消息传递提供了一条补充途径，可能影响未来的几何深度学习研究，并在粒子动力学和分子性质预测等任务中提高性能。 该论文还引入了针对具有优先环境方向的系统的受控对称性松弛，该方向可以预先指定或从数据中推断，同时当方向通路不活跃时恢复完全的 E(n)-等变性。实验表明，在动力学预测、对称性破坏时重力轴的恢复、选定网格任务和长时程推演上的显著改进，以及对未见旋转的鲁棒性。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: 等变图神经网络（GNN）旨在尊重数据中的对称性，如旋转和平移，这对于建模几何系统至关重要。传统的一阶架构通常限制向量信息在边上的变换方式，而高阶表示可能计算成本高昂。层状神经网络通过为节点和边分配带有线性映射的向量空间来扩展 GNN，从而实现更丰富的消息传递。本文基于这些概念，在学习矩阵值传输的同时保持等变性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28853">[2608.28853] Equivariant Sheaf Neural Networks : Learning...</a></li>
<li><a href="https://www.emergentmind.com/topics/category-equivariant-neural-networks-cenns.md">emergentmind.com/topics/category- equivariant - neural - networks ...</a></li>
<li><a href="https://arxiv.org/pdf/2601.21207">A Sheaf - Theoretic and Topological Perspective on Complex Network ...</a></li>

</ul>
</details>

**标签**: `#graph neural networks`, `#equivariance`, `#geometric deep learning`, `#sheaf theory`, `#arXiv`

---

<a id="item-12"></a>
## [停止向量：通过因果引导减少大模型过度思考](https://arxiv.org/abs/2608.28859) ⭐️ 8.0/10

研究人员在 DeepSeek-R1-Distill-Qwen-7B 中发现了一个能控制推理长度的“停止向量”，并将其内化到模型权重中以减少过度思考。该干预在五个未见基准上将思考步骤减少了约四分之一，且无需全局惩罚。 这项工作解决了推理模型在已知答案后仍继续思考而浪费计算资源的问题。通过提供一种因果的、权重内化的方法，它为提升大模型效率提供了新途径，可能有助于部署和降低成本。 停止向量是第 18 层的一个均值差方向，简单地最大化投影会破坏离轴维度，导致生成变长；相反，重建整个受引导激活并固定这些维度才有效。仅从 24 个问题拟合且无需强化学习，削减与每个问题的可移除冗余的相关性为 0.70。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: 像 DeepSeek-R1-Distill-Qwen-7B 这样的推理模型会生成很长的思维链，常常在答案已确定后仍过度思考。因果分析和引导向量是可解释性技术，通过操纵内部表示来控制模型行为。本文基于这些概念实现了效率提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/collections/deepseek-ai/deepseek-r1">DeepSeek - R 1 - a deepseek-ai Collection</a></li>
<li><a href="https://www.emergentmind.com/topics/neural-steering-vector">Neural Steering Vector</a></li>
<li><a href="https://arxiv.org/abs/2410.15319">[2410.15319] Causality for Large Language Models</a></li>

</ul>
</details>

**标签**: `#interpretability`, `#LLM reasoning`, `#efficiency`, `#causal analysis`, `#DeepSeek`

---

<a id="item-13"></a>
## [保守混合图网络实现过程系统零样本迁移](https://arxiv.org/abs/2608.28896) ⭐️ 8.0/10

该论文提出了保守混合图网络（CHGN），它将路由、工况分配和移除率作为数据驱动的替代模型学习，并嵌入到固定的输运方程中，从而在构造上保证质量平衡。在 10-20 个节点的网络上训练的 CHGN 可以零样本迁移到 25-40 个节点的未见图，RMSE 达到 2.1e-3，而 GNN 基线为 6e-2 至 9e-2。 这项工作解决了工业过程网络建模中的一个关键限制，即拓扑动态变化且潜在机制往往不可观测。无需重新训练即可跨拓扑进行零样本泛化，可显著减少针对每个新工厂配置重新训练模型的需求，对过程系统工程和物理信息机器学习产生影响。 CHGN 在构造上强制质量平衡，在流体混合中试装置上，对于留出的物理故障，它优于持久性基线，但无法预测未观测到阀门动作的人工干预。在未见图上，门控 MAE 为 7.9e-3，工况准确率为 94.3%；在固定训练拓扑上分别为 1.2e-2 和 96.4%。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: 工业过程网络（如化工厂）由通过流股连接的单元组成，但随着流股被节流或旁路以及单元在空闲、过渡和活跃工况之间切换，其有效拓扑会发生变化。在测量轨迹上训练的传统图神经网络（GNN）可能拟合数据，但不会为路由赋予稳定的物理意义。质量平衡是基本的守恒定律，确保系统中质量既不会产生也不会消失，将其嵌入模型可保证预测的物理一致性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28896">[2608.28896] Conservative Hybrid Graph Networks for Process...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Mass_balance">Mass balance - Wikipedia</a></li>
<li><a href="https://www.sciencedirect.com/topics/engineering/mass-balance-equation">Mass Balance Equation - an overview | ScienceDirect Topics</a></li>

</ul>
</details>

**标签**: `#graph neural networks`, `#process systems`, `#zero-shot learning`, `#physics-informed ML`, `#hybrid models`

---

<a id="item-14"></a>
## [通用编码计算：面向掉队者的学习理论框架](https://arxiv.org/abs/2608.28910) ⭐️ 8.0/10

该论文提出了通用编码计算（GCC），一种用端到端均方误差损失替代代数工具来处理分布式计算中掉队者的新框架。它提供了理论性能保证，在最坏情况下损失至少以 O(S^3 N^{-3}) 的速率衰减，在概率设置下以 O(log_{1/p}^3(N) N^{-3}) 的速率衰减。 这项工作解决了现有编码计算方案的关键局限性，这些方案专为结构化计算的精确恢复而设计，无法处理深度神经网络等现代机器学习工作负载。通过采用学习理论视角，GCC 将编码计算的适用性扩展到近似计算，可能影响分布式训练和推理系统。 该框架将编码器和解码器限制在具有温和平滑约束的再生核希尔伯特空间（RKHS）中，使其能够表示为核函数的线性组合，且系数可高效计算。理论保证涵盖两种掉队者场景：最坏情况下 N 个工作者中最多 S 个掉队者，以及概率设置下每个工作者独立以概率 p 掉队。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: 编码计算是一种利用编码理论向分布式系统注入计算冗余以缓解掉队者（缓慢或失败的工作者）影响的范式。传统方案依赖代数结构进行精确恢复，这限制了它们在机器学习中的应用，因为机器学习中的计算通常是非代数的且只需要近似结果。本文提出了一种基于学习的替代方案，直接优化端到端损失，使其对现代工作负载更加灵活。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28910">[2608.28910] Learning-Theoretic Foundation for General Coded ...</a></li>
<li><a href="https://proceedings.neurips.cc/paper_files/paper/2024/file/cae00f05c4074758a6542823ae7bea99-Paper-Conference.pdf">Coded Computing for Resilient Distributed</a></li>

</ul>
</details>

**标签**: `#coded computing`, `#distributed systems`, `#machine learning`, `#straggler mitigation`, `#theory`

---

<a id="item-15"></a>
## [SemKV：基于质量悬崖的混合精度 KV 缓存量化方法](https://arxiv.org/abs/2608.28911) ⭐️ 8.0/10

SemKV 提出了一种感知质量悬崖的混合精度 KV 缓存量化方法，该方法保留所有 token，并使用模型内部的重要性分数来分配相邻的悬崖以上精度，在 Llama-3.1-8B-Instruct 上实现了 6.0 倍的存储缩减，且与完整 KV 相比没有统计上可检测的质量损失。 这项工作通过揭示均匀 KV 量化中的质量悬崖，并证明混合精度可以实现更好的平均精度，解决了长上下文 LLM 推理中的关键内存瓶颈。它提供了一种实用的方法，在不牺牲质量的情况下大幅减少内存使用，这可能支持更长的上下文和更高效的 LLM 部署。 论文识别出在比特范围(2.0, 2.322]内存在质量悬崖，均匀量化在此处崩溃，并表明在悬崖以上，八种模型内部重要性指标在统计上可互换。将仿射基替换为失真优化量化器(TurboQuant-MSE)可降低悬崖，并将无可检测损失的工作点提高到 7.9 倍存储缩减。

rss · arXiv - Machine Learning · Sep 1, 04:00

**背景**: KV 缓存在大语言模型推理期间存储键和值张量，随上下文长度线性增长，成为长上下文模型的主要内存瓶颈。量化通过减少每个值的位数来降低内存，但均匀量化可能遭遇“质量悬崖”，即低于某个比特率时性能急剧下降。混合精度量化为模型的不同部分分配不同的位宽，以平衡效率和准确性。SemKV 利用模型内部的重要性分数来指导精度分配，保留所有 token，并使用相邻的悬崖以上精度，从而实现比均匀量化更好的平均精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Progressive_Mixed-Precision_KV_Cache_Quantization">Progressive Mixed-Precision KV Cache Quantization</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>
<li><a href="https://docs.vllm.ai/en/stable/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM</a></li>

</ul>
</details>

**标签**: `#KV cache`, `#quantization`, `#LLM inference`, `#mixed-precision`, `#long-context`

---

<a id="item-16"></a>
## [参数化多模态用户记忆：存储字幕无法承载的信息](https://arxiv.org/abs/2608.28609) ⭐️ 8.0/10

该论文提出了一种参数化多模态用户记忆，将感知身份键存储为内联令牌，克服了基于文本的记忆在个性化代理中的局限性。它将回忆分解为视觉语言模型的接地和专用编码器的身份提取，在 PerceptMem 基准上达到了接近完美的性能。 这项工作解决了个性化 AI 代理中的一个关键缺口，使它们能够记住文本字幕无法捕捉的用户感知方面（如声音、面部）。它可能显著增强多模态 AI 系统，使其在现实应用中更加个性化和有能力。 识别核心是无需训练的，可以在任何冻结模型上以 O(1)注册成本复现编码器的召回率。在 PerceptMem（12 个领域，1,080 个任务）上，感知身份受容量限制，而精确事实受绑定限制，表明身份应存储在参数化库中，事实应存储在文本库中。

rss · arXiv - NLP · Sep 1, 04:00

**背景**: 个性化代理通常依赖基于文本的用户记忆，如转录和字幕，这些无法捕捉声音音色或面部外观等感知信息。所提出的方法将感知记忆接地在模型本身，使用视觉语言模型定位指代对象，并使用专用编码器提取身份键，存储为内联令牌。这种方法避免了外部检索往返，并与文本记忆组合，实现全面的用户建模。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2608.28609">[2608.28609] Parametric Multimodal User Memory : Storing What...</a></li>
<li><a href="https://01.me/research/multimodal-user-memory/">Parametric Multimodal User Memory — Companion site</a></li>
<li><a href="https://aclanthology.org/2022.emnlp-main.375.pdf">MuRAG: Multimodal Retrieval-Augmented Generator</a></li>

</ul>
</details>

**标签**: `#multimodal`, `#user memory`, `#personalization`, `#vision-language model`, `#AI agents`

---

<a id="item-17"></a>
## [LLM 同行评审审计揭示评分虚高与偏见](https://arxiv.org/abs/2608.28626) ⭐️ 8.0/10

一项新研究审计了两个多模态 LLM（Qwen2.5-VL-72B 和 Pixtral-Large-124B）作为 ICLR 2026 投稿的同行评审员，发现它们给出的分数虚高（7.0-8.1，而人类为 3.4-6.8），且仅检测出 12.1%的插入错误。 这很重要，因为 LLM 越来越多地被用于学术同行评审，而研究结果凸显了它们在评分校准和错误检测方面的严重局限性，如果在没有保障措施的情况下采用，可能会损害科学评估的完整性。 该研究使用了 165 篇 ICLR 2026 投稿，操纵了作者身份（盲审、高威望、低威望），并在 55 篇稿件中插入了 145 个可验证错误。一句验证指令将错误检测率提高到 22.2%，但仍有 78%的错误未被发现；提供图表反而降低了检测率并提高了分数。

rss · arXiv - NLP · Sep 1, 04:00

**背景**: 大型语言模型（LLM）是在海量文本数据上训练的 AI 系统，多模态 LLM 还能处理图像。它们越来越多地被用于同行评审等任务，但其在关键评估中的可靠性存疑。本研究在会议投稿上测试了两种此类模型，将其评分和错误检测与人类评审员进行了比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Qwen25-VL-72B-Instruct">Qwen2.5-VL-72B-Instruct</a></li>
<li><a href="https://huggingface.co/mistral-community/Pixtral-Large-Instruct-2411">mistral-community/ Pixtral - Large -Instruct-2411 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_LLM">Multimodal LLM</a></li>

</ul>
</details>

**标签**: `#LLM evaluation`, `#peer review`, `#AI bias`, `#multimodal`, `#academic integrity`

---

<a id="item-18"></a>
## [MIRAGE-CAD：多模态生成可执行 CAD 程序](https://arxiv.org/abs/2608.28669) ⭐️ 8.0/10

MIRAGE-CAD 提出了一种通过构造中介的方法，从自然语言、图像、点云和 B-Rep 几何生成可执行的 CAD 程序，在每种模态的 2500 个保留查询上，无需检索即可实现 55.4%-70.0%的构建成功率和 52.3%-66.2%的 STEP 导出成功率。 这项工作解决了从观察对象恢复参数化 CAD 程序时的基本歧义问题，提供了一种跨多种输入类型的统一方法。高成功率和显式的构造计划接口可能显著推进 CAD 自动化和设计工作流程，影响工程师和设计师。 该系统使用共享的构造表示和显式的构造计划接口，生成的 Python 代码由 OpenCASCADE 内核执行以构建实体并导出为 STEP。对照实验表明，直接基于连续表示的解码器也能很好地重建，而显式计划提供了可读且可测量的中间表示，其与参考构造的一致性可预测下游执行的成功率。

rss · arXiv - Computer Vision · Sep 1, 04:00

**背景**: CAD（计算机辅助设计）程序是通过构造步骤定义 3D 对象的参数化模型。B-Rep（边界表示）通过边界描述几何形状，STEP 是用于交换 3D CAD 数据的标准文件格式。OpenCASCADE 是一个广泛使用的开源 CAD 内核，用于执行建模操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/STEP_file_format">STEP file format</a></li>
<li><a href="https://www.shapr3d.com/content-library/what-is-b-rep">Boundary representation ( b - rep ): What it is, and why it’s a problem in...</a></li>

</ul>
</details>

**标签**: `#CAD`, `#multimodal learning`, `#program generation`, `#computer vision`, `#geometry processing`

---

<a id="item-19"></a>
## [交互增长复杂度刻画离散扩散采样](https://arxiv.org/abs/2608.28949) ⭐️ 8.0/10

本文提出了一种新的几何度量——交互增长复杂度（IGC），用于刻画乘积参考离散扩散算法的采样性能。研究表明，双变量 IGC 核能精确表示 KL 离散化误差和一步上界，并且最优步长调度可以降低迭代复杂度。 该工作为理解和优化离散扩散模型提供了理论基础，这类模型在文本、图等离散数据的生成建模中日益重要。所提出的复杂度度量可指导更高效采样算法的设计，并改善这些模型的实际部署。 论文表明，在对数平方可靠性优势中等距步长的采样器，其性能取决于总 IGC 质量，而精细步长选择可基于平方根泛函获得更低复杂度。研究还证明，一般乘积参考分布能重塑 IGC 轮廓并带来维度相关的改进，并将总 IGC 质量与总相关和双总相关联系起来。

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**背景**: 离散扩散模型是一类生成模型，通过逆转前向破坏过程，迭代地将噪声转化为离散数据。乘积参考扩散算法使用乘积分布作为前向过程的参考，其采样性能取决于概率单纯形中的路径。交互增长复杂度（IGC）是一种新的基于路径的度量，用于捕捉扩散路径上数据分布的几何复杂度，为分析离散化误差和迭代复杂度提供了统一框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2608.28949">The information geometry of product - reference discrete diffusion ...</a></li>

</ul>
</details>

**标签**: `#diffusion models`, `#discrete sampling`, `#information geometry`, `#sampling complexity`, `#theory`

---

<a id="item-20"></a>
## [Jigsaw-CRL：从碎片化多客户端干预中恢复全局潜在因果顺序](https://arxiv.org/abs/2608.28991) ⭐️ 8.0/10

Jigsaw-CRL 是一个新框架，能从碎片化的多客户端干预中恢复全局潜在因果顺序，其中每个客户端仅访问潜在变量的子集。它利用软干预下精度矩阵差异的低秩结构，将客户端特定的碎片组装成全局节点级因果顺序。 这项工作解决了因果表示学习中一个新颖且实际的挑战，适用于数据无法集中的分布式和隐私保护场景。它将因果发现扩展到客户端仅观察系统部分的情况，可能使现实应用中的因果推断更加稳健和可扩展。 该框架提供了可辨识性保证，开发了实用算法，并在合成数据上进行了验证。代码可在匿名仓库获取，论文见 arXiv（2608.28991）。

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**背景**: 因果表示学习（CRL）旨在从高维观测中恢复潜在因果变量及其结构关系。传统 CRL 假设所有环境共享相同的潜在变量，但在碎片化多客户端设置中，客户端干预不同的子集，导致边缘化引入双向边并破坏节点级潜在因果图。本文通过组装客户端特定的碎片来恢复全局因果顺序。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Causal_Representation_Learning">Causal Representation Learning</a></li>
<li><a href="https://arxiv.org/abs/2102.11107">[2102.11107] Towards Causal Representation Learning</a></li>
<li><a href="https://en.wikipedia.org/wiki/Causal_graph">Causal graph - Wikipedia</a></li>

</ul>
</details>

**标签**: `#causal representation learning`, `#causal discovery`, `#multi-client`, `#latent variables`, `#interventions`

---

<a id="item-21"></a>
## [秩受限矩阵 LASSO 全局最小值的尖锐 RIP 阈值](https://arxiv.org/abs/2608.29018) ⭐️ 8.0/10

本文确定了秩受限矩阵 LASSO 全局最小值恢复的尖锐受限等距性质（RIP）阈值，给出了保证精确恢复的 RIP 常数的精确条件。该结果也推广到向量 LASSO 情形。 该工作为矩阵 LASSO 恢复提供了基本的理论极限，对压缩感知和高维统计至关重要。尖锐阈值明确了何时可以恢复且无法改进，为这些领域的算法设计和理论分析提供了指导。 尖锐阈值由δ_sharp(t)=t/(4-t)（0<t<4/3）和δ_sharp(t)=√((t-1)/t)（t≥4/3）给出，其中 t=k/r_*。该结果对所有搜索秩 r≥r_*成立，且常数与 r 无关。论文还通过反例表明该阈值无法改进。

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**背景**: 受限等距性质（RIP）是压缩感知中的关键概念，确保从线性测量中稳定恢复稀疏信号。矩阵 LASSO 是用于低秩矩阵恢复的核范数正则化最小二乘问题，将向量 LASSO 推广到矩阵情形。Frobenius 范数误差用于衡量矩阵问题中的恢复精度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cs.columbia.edu/~andoni/algoS19/scribes/scribe9.tex">Lecture #9: Compressed Sensing : Restricted Isometry Property</a></li>
<li><a href="https://arxiv.org/html/2404.12828">Low solution rank of the matrix LASSO under RIP with consequences...</a></li>

</ul>
</details>

**标签**: `#matrix LASSO`, `#restricted isometry property`, `#compressed sensing`, `#high-dimensional statistics`, `#optimization`

---

<a id="item-22"></a>
## [深度潜变量框架联合建模缺失、误差与异质性](https://arxiv.org/abs/2608.30040) ⭐️ 8.0/10

本文提出一个统一的概率框架，利用具有再收敛路由和基于校准的去噪的分层树路由变分自编码器，联合处理缺失数据、测量误差和总体异质性。该框架支持 MCAR、MAR 和 MNAR 缺失机制，同时学习子组特定和全局共享的潜在结构。 这项工作意义重大，因为它在单一模型中解决了三个常见的数据挑战，这比单独处理它们更符合实际。它可能提高医疗保健和其他高维应用中分析的可靠性，这些应用中的数据通常嘈杂且不完整。 所提出的方法集成了模式感知的潜在表示、分层树路由编码器和再收敛分支共享架构。模拟研究表明，在复杂的异质性缺失和测量误差设置下，与现有的深度生成插补方法相比，该方法有显著改进。

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**背景**: 变分自编码器（VAE）是学习数据潜在表示的生成模型。分层 VAE，如 TreeVAE，通过学习基于树的先验分布来扩展这一点，从而捕捉数据中的层次结构。缺失数据机制（MCAR、MAR、MNAR）描述了缺失性与观测和未观测数据的关系，测量误差指记录值的不准确性。本文结合这些概念来处理现实世界数据的复杂性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://towardsdatascience.com/difference-between-autoencoder-ae-and-variational-autoencoder-vae-ed7be1c038f2/">towardsdatascience.com/difference-between- autoencoder -ae-and...</a></li>
<li><a href="https://mvandenhi.github.io/publications/manduchi-2023-tree/">Tree Variational Autoencoders | Moritz Vandenhirtz</a></li>
<li><a href="https://arxiv.org/pdf/2608.30040">A Deep Latent Variable Framework for Jointly Modeling Missingness...</a></li>

</ul>
</details>

**标签**: `#variational autoencoder`, `#missing data`, `#measurement error`, `#heterogeneity`, `#probabilistic modeling`

---

<a id="item-23"></a>
## [令牌预测组织表示：一个统计框架](https://arxiv.org/abs/2608.30072) ⭐️ 8.0/10

本文提出了一个统计框架，表明令牌预测根据上下文分布之间的 Hellinger 距离组织令牌嵌入和上下文表示，并给出了显式的误差界。它还建立了令牌生成、社区恢复和线性探针分类的下游保证。 这项工作为理解为什么令牌预测（大型语言模型的核心预训练目标）能产生广泛有用的表示提供了理论基础。它弥合了预训练损失与下游性能之间的差距，可能指导更高效和可解释的模型设计。 该框架假设 softmax 预测头，并表明令牌嵌入按 Hellinger 距离组织，误差取决于预测准确性和令牌频率。它还引入了一个自洽原则，即共享表示块的重复应用可以在不增加参数的情况下细化上下文表示。

rss · arXiv - Data Science & Statistics · Sep 1, 04:00

**背景**: 令牌预测是现代语言模型（如 GPT 和 Llama）的标准预训练目标，模型学习预测序列中的下一个令牌。Hellinger 距离是一种量化两个概率分布相似度的度量，本文用它来衡量上下文分布的相似性。表示几何指的是嵌入在高维空间中的空间排列，被认为能捕捉语义关系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hellinger_distance">Hellinger distance - Wikipedia</a></li>
<li><a href="https://arxiv.org/pdf/2404.19737">Better & Faster Large Language Models via Multi- token Prediction</a></li>
<li><a href="https://avrtt.github.io/research/geometry_estimation/">Geometry estimation, pt. 1 - avrtt.blog</a></li>

</ul>
</details>

**标签**: `#representation learning`, `#language models`, `#theory`, `#token prediction`, `#statistical learning`

---