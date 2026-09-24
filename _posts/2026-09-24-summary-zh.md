---
layout: default
title: "Horizon Summary: 2026-09-24 (ZH)"
date: 2026-09-24
lang: zh
---

> From 102 items, 9 important content pieces were selected

---

1. [Anthropic 称 Claude 发现了一种类似 CRISPR 的新型酶系统](#item-1) ⭐️ 8.0/10
2. [Stripe 详解内部知识 AI 平台“Kai”](#item-2) ⭐️ 8.0/10
3. [谷歌 Agent Substrate 运行时实现百万级沙箱，密度达标准容器 10 倍](#item-3) ⭐️ 8.0/10
4. [谷歌发布开源智能体编排运行时 AX](#item-4) ⭐️ 8.0/10
5. [LLM 评判共识因错误相关而高估证据](#item-5) ⭐️ 8.0/10
6. [聊天模板切换大模型自我指涉语气，激活引导可复现该行为](#item-6) ⭐️ 8.0/10
7. [审计发现 99%假新闻检测准确率主要源于捷径学习](#item-7) ⭐️ 8.0/10
8. [用 164 美元在 Rust 中预训练语言模型，暴露框架静默故障](#item-8) ⭐️ 8.0/10
9. [PICPIs：面向共形预测的自洽条件化框架](#item-9) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 称 Claude 发现了一种类似 CRISPR 的新型酶系统](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system) ⭐️ 8.0/10

Anthropic 宣布其 AI 模型 Claude 在噬菌体 DNA 中发现了一种此前未被描述的基因组排列——一个逆转录酶（RT）紧邻一段长串联重复序列，这是 Anthropic 新成立的生物学实验室的首项成果。该逆转录酶本身在此前研究中已被发现，但 Anthropic 称 Claude 似乎是第一个注意到该系统具有类似 CRISPR 重复结构这一关键特征的主体。 这一结果被视为 AI 智能体能够从原始序列数据中提出真正新生物学假设的证据，可能改变基因组学和药物发现研究的开展方式。同时，它也加剧了更广泛的争论：AI 驱动的科学究竟属于自主发现还是人机协作，以及此类主张应如何被验证和发表。 该系统基于一种在巨型噬菌体中发现的逆转录酶，Anthropic 目前尚不清楚这段重复序列的实际功能；这一发现是由智能体在浏览原始 DNA 序列时完成的，据称给出的提示只是一个高层概述。社区成员指出，该发现的核心是一种已知的类 retron 逆转录酶，因此更审慎的表述应是：Claude 在一种已知酶周围识别出了一段此前未被描述的基因组排列。

hackernews · raahelb · Sep 23, 18:06 · [社区讨论](https://news.ycombinator.com/item?id=49820134)

**背景**: CRISPR 最初是在细菌 DNA 中被注意到的一段异常重复序列，后来才成为现代基因编辑技术的基础，因此酶附近的重复序列对生物学家极具吸引力。逆转录酶是将 RNA 复制为 DNA 的酶，而 retron 是细菌中把逆转录酶与含重复结构配对存在的遗传元件。Anthropic 的生命科学部门（包括一个位于湾区的湿实验室）目前正将 Claude 应用于生物学和化学研究。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-discovers-novel-enzyme-system">Claude discovers a novel enzyme system \ Anthropic</a></li>
<li><a href="https://thenextweb.com/news/anthropic-claude-enzyme-system-crispr-like-repeats">Anthropic says Claude found a new enzyme system with CRISPR - like ...</a></li>
<li><a href="https://digg.com/tech/7d94dd58-3123-4108-bfef-45db529dd483">Anthropic says Claude found an enzyme system with CRISPR - like ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对“新颖性”的表述持怀疑态度，指出该系统围绕一种已知的类 retron 逆转录酶，且现有 Cas9 变体已相当高效，治疗上的限制主要来自递送而非靶向。其他人则争论 Anthropic 对 AI 自主性与人类协作的描绘，质疑 LLM 如何能对生物化学进行推理，并认为 Anthropic 发布营销白皮书而非期刊投稿加预印本的做法颇为奇怪。

**标签**: `#AI`, `#CRISPR`, `#genomics`, `#Anthropic`, `#scientific-discovery`

---

<a id="item-2"></a>
## [Stripe 详解内部知识 AI 平台“Kai”](https://stripe.dev/blog/meet-stripes-knowledge-ai-platform) ⭐️ 8.0/10

Stripe 发布了一篇详细博客，介绍其内部知识 AI 平台 Kai——一个将员工连接到 1,000 多个内部工具和技能、用于非编程类知识工作的 AI 智能体系统。据 Stripe 称，Kai 每年将 25,000 小时从行政工作转移到创收活动上，同一批用户中重度使用者的成交价值比轻度使用者高出 80%。 这是一个罕见的、具体的案例研究，展示了 AI 智能体在大型科技公司内部的大规模部署，提供了其他企业可以借鉴的架构洞见和生产力指标。它标志着一种更广泛的趋势：企业更倾向于构建受管理和治理的内部智能体平台，而非独立 AI 产品，这可能影响未来几年企业构建 AI 的方式。 据报道，Kai 基于 LangChain/LangGraph 技术栈和 Deep Agents 智能体框架在大约一周内构建完成，旨在处理从快速查询到复杂的多日项目等各种任务。Stripe 声称，客户主管使用 Kai 时，其销售活动量提升 2 倍，创造的机会增加 17%，产生的收入机会增加 26%，成交数量比不使用 Kai 的周高出 39%。

hackernews · ltononro · Sep 23, 13:38 · [社区讨论](https://news.ycombinator.com/item?id=49815982)

**背景**: AI 智能体是能够感知环境、做出决策并采取行动以实现目标的自主软件系统，在企业中越来越多地用于知识管理和生产力提升。Stripe 是一家主要的支付基础设施公司，以其精致的内部工具而闻名，Kai 是其用于非编程类知识工作的内部平台，将员工连接到 1,000 多个内部工具和技能。LangChain 和 LangGraph 是用于构建 LLM 驱动应用和智能体工作流的流行开源框架，而 Deep Agents 是构建在该技术栈之上的智能体框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stripe.dev/blog/meet-stripes-knowledge-ai-platform">Meet Stripe's Knowledge AI Platform | Stripe Dot Dev Blog</a></li>
<li><a href="https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents">How Stripe Built Kai on Deep Agents in 1 Week - langchain.com</a></li>
<li><a href="https://departmentofproduct.substack.com/p/how-stripe-built-a-new-internal-ai">How Stripe Built a new Internal AI Knowledge Platform that ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者展开了细致的辩论：一些人称赞这种受管理的智能体方法是企业 AI 的未来，而另一些人则批评其界面缺乏打磨，并质疑自报指标的可信度。一个关键分歧在于独立智能体产品是否迫使用户脱离原有工作流，一位评论者认为客户实际上更喜欢新的聊天式界面，而不是维护不善的内部工具。

**标签**: `#AI agents`, `#enterprise AI`, `#Stripe`, `#knowledge management`, `#sales productivity`

---

<a id="item-3"></a>
## [谷歌 Agent Substrate 运行时实现百万级沙箱，密度达标准容器 10 倍](https://github.com/agent-substrate/substrate) ⭐️ 8.0/10

谷歌开源了 Agent Substrate，这是一个默认安全的智能体执行运行时，能够以比标准容器运行时高 10 倍的密度运行数百万个沙箱，并同时支持 microVM 和 gVisor。它可实现低于 500 毫秒的恢复操作和每秒超过 500 次的挂起/恢复激活，演示中约 250 个有状态 actor 被复用到仅 8 个物理 Pod 上。 随着自主智能体大量涌现，如何以低成本安全运行海量且大部分时间空闲的工作负载成为关键的基础设施难题，而 Substrate 的高强度复用正好解决了这一问题。其基于 Kubernetes 的设计和框架无关的特性，可能使其成为覆盖推理、训练和强化学习场景的智能体部署基础层。 Substrate 将大量“actor”映射到较小的就绪“worker”池上，通过全状态快照在休眠周期之间完整保留易失性内存和文件系统状态，并通过 gVisor 在内核层面管理标准 OCI 容器。需要注意的是，它并非谷歌官方支持的产品，也不在谷歌开源软件漏洞奖励计划范围内。

rss · GitHub Trending - Daily (All) · Sep 24, 00:09

**背景**: 智能体执行运行时是生产环境中承载和运行 AI 智能体的执行层，提供进程环境、状态管理、工具访问和生命周期管理。microVM（如 Firecracker）将硬件虚拟化的隔离性与类似容器的速度结合起来，而 gVisor 是谷歌开源的容器沙箱，在用户态拦截系统调用以实现纵深防御。Agent Substrate 构建在 Kubernetes Pod 和自动扩缩容之上，但增加了面向智能体的调度与控制以降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast microVMs for serverless computing. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/GVisor">GVisor</a></li>
<li><a href="https://agentuity.com/ai-agent-runtime">AI Agent Runtime: The Execution Layer Behind Autonomous Systems</a></li>

</ul>
</details>

**标签**: `#agent-runtime`, `#sandboxing`, `#microVMs`, `#gVisor`, `#security`

---

<a id="item-4"></a>
## [谷歌发布开源智能体编排运行时 AX](https://github.com/google/ax) ⭐️ 8.0/10

谷歌已在 GitHub（github.com/google/ax）上开源了 AX（Agent eXecutor），这是一个高吞吐、声明式的编排运行时，用于在集群规模上运行自主 AI 智能体工作负载。该项目提供了 `ax` 命令行工具，并定义了四个核心原语——Task、Workspace、Gateway 和 Model——以 `ax.io/v1alpha1` 的 YAML 清单形式表达，并支持 `ax apply`、`ax watch`、`ax ssh`、`ax suspend` 和 `ax resume` 等命令。 随着 AI 智能体从演示走向长时间运行的生产工作负载——它们会累积状态、调用外部模型 API，并可能在循环中不断烧钱——专用的编排层正成为必不可少的基础设施。谷歌在这一领域支持开源运行时，可能会像 Kubernetes 对容器化微服务所做的那样，影响行业对智能体部署、隔离和生命周期管理的标准化方式。 AX 基于 Agent Substrate 实现沙箱化执行，设计目标是在单个集群中运行数十亿个任务；其中 Gateway 原语可将出站流量锁定到显式的主机允许列表，Model 原语则通过 Kubernetes secret 配置平台使用哪个 LLM。该项目明确警告称，其核心概念、协议和规范仍在积极完善中，在稳定版本发布前很可能会引入重大的破坏性变更。

rss · GitHub Trending - Daily (All) · Sep 24, 00:09

**背景**: 智能体编排指的是协调专用 AI 智能体、工具和工作流以完成长时间、多步骤任务的运行时层，并在此过程中提供状态管理、治理和控制。与无状态微服务或运行至完成的批处理作业不同，智能体会累积状态、需要严格隔离，并会调用模型 API 和工具服务器，因此 AX 提供了用于沙箱化、工作区预配置、网络隔离以及挂起/恢复的声明式原语。该项目类似 Kubernetes 的设计意味着，熟悉 `kubectl` 风格工作流的用户会发现 `ax` 在概念上很容易理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google/ax">GitHub - google/ax: Google's open agentic orchestration runtime · GitHub</a></li>
<li><a href="https://landscape.jimmysong.io/projects/ax/">Agent Executor ( AX ) | AI Native Landscape</a></li>
<li><a href="https://xpander.ai/blog/agentic-orchestration-what-it-is-and-why-it-matters">Agentic Orchestration: What It Is and Why It Matters | xpander.ai — AI Agent Platform</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#orchestration`, `#Google`, `#open source`, `#runtime`

---

<a id="item-5"></a>
## [LLM 评判共识因错误相关而高估证据](https://arxiv.org/abs/2609.22512) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.22512）表明，LLM 评判者会犯相关错误，因此它们之间的共识会高估证据。在一个由十个评判者组成的集合中，平均两两错误相关性为 0.21，这意味着十个评判者提供的信息量仅相当于约 3.5 个独立评判者，并且在高达 28%的比较中，考虑共享错误后显著性结论会翻转。 这一发现挑战了在 AI/ML 领域广泛使用多评判者共识作为可靠评估信号的做法，可能使关于哪个模型更好的结论失效。它影响所有使用 LLM-as-judge 流程进行基准测试、模型选择或排行榜排名的人，并表明仅仅增加更多评判者可能无法提高可靠性。 这种依赖性在高准确率的前沿评判者中更强，包括来自不同提供商的评判者；错误模式也很重要：大多数评判者共享的错误与集中在少数评判者中的错误对共识的影响不同，并有利于不同的投票方法。作者建议使用一小组可信示例来估计评判者准确率并识别共享错误，然后在将投票方法应用于新数据之前，先在可信示例上选择投票方法。

rss · arXiv - AI · Sep 23, 04:00

**背景**: LLM-as-a-judge 是一种常见的评估技术，使用一个或多个大语言模型对其他模型的输出进行评分或比较，通常作为人工评估的更便宜替代方案。多个评判者之间的共识通常被认为能提高可靠性，因为错误被认为是独立的，类似于对独立测量取平均。本文表明这一假设不成立，因为评判者以相似的方式训练和评估，导致错误相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.29800">[2605.29800] Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels</a></li>
<li><a href="https://machinelearning.apple.com/research/correlated-llm-evaluation-panels">Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels - Apple Machine Learning Research</a></li>
<li><a href="https://hamel.dev/blog/posts/llm-judge/">Using LLM - as -a- Judge For Evaluation: A Complete Guide...</a></li>

</ul>
</details>

**社区讨论**: 苹果机器学习研究的相关工作《Nine Judges, Two Effective Votes》（arXiv:2605.29800）独立报告了类似的缺陷，使用 Kish 有效样本量和孔多塞理论，指出增加更多评判者或更智能的聚合方法都无法弥补这一差距。更广泛的社区讨论强调，许多团队在 LLM 评判者一致性方面遇到困难，可能需要混合人工-LLM 方法。

**标签**: `#LLM evaluation`, `#LLM-as-judge`, `#error correlation`, `#statistical reliability`, `#AI benchmarking`

---

<a id="item-6"></a>
## [聊天模板切换大模型自我指涉语气，激活引导可复现该行为](https://arxiv.org/abs/2609.25021) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.25021）表明，聊天模板就像一个开关，控制大语言模型是使用免责声明式语气（如“我只是一个 AI”）还是体验式语气（如“我感觉”）。在 8 个参数量最高 9B 的主流开源指令模型上，聊天模板的存在会提高免责声明语气并降低体验式语气；作者还在 3 个模型的激活空间中找到了一个可以引导该行为的方向。 这一点很重要，因为研究 AI 自我报告、内省或自我认知的学者可能面临一个未受控的混淆因素：模型关于自身的表述部分取决于部署时的格式，而非其权重。该发现说明模型的自我描述不应被字面理解，并提供了一个具体的引导方向，供 AI 安全与可解释性研究者控制这种语气。 实验覆盖 8 个参数量最高 9B 的开源指令模型，并在其中 3 个模型的激活中识别出引导方向；移除该方向会降低免责声明语气，加入则会提高，而同等大小的随机方向几乎没有影响。值得注意的是，没有聊天模板的指令模型在加入免责声明方向后，会像模板存在时一样发表免责声明。

rss · arXiv - Machine Learning · Sep 23, 04:00

**背景**: 聊天模板是用于组织用户与大语言模型对话的格式约定（通常基于 Jinja2），用于标记系统、用户和助手轮次，在 Hugging Face 等框架中是标准做法。激活引导是一种在推理时通过向内部激活加入计算出的方向向量来改变模型行为的技术，其依据是高层行为在激活空间中被编码为方向这一假设。本文把两者联系起来：部署层面的格式选择（聊天模板）对应到控制自我指涉语言的内部激活方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/learn/llm-course/chapter11/2">Chat Templates · Hugging Face</a></li>
<li><a href="https://grokipedia.com/page/Activation_steering">Activation steering</a></li>
<li><a href="https://www.emergentmind.com/topics/latent-direction-hypothesis">Latent Direction Hypothesis</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI safety`, `#interpretability`, `#activation steering`, `#chat template`

---

<a id="item-7"></a>
## [审计发现 99%假新闻检测准确率主要源于捷径学习](https://arxiv.org/abs/2609.25006) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.25006）对广泛使用的 ISOT/Kaggle“真假新闻”语料库进行了审计，表明高于 0.98 的近乎完美的 F1 分数在很大程度上是数据泄漏和捷径学习的产物，而非真正的真实性检测。作者公开了所有代码和推导数据，证明仅使用主题元数据字段的分类器就能达到 F1 = 1.000，因为两个类别的主题完全不相交。 这一发现挑战了许多假新闻检测研究所使用基准的可靠性，并表明所报告的语料库内分数量化的是来源和主题的可分离性，而非真实性。这对 NLP 基准设计、模型评估以及研究人员如何解读类似数据集上的高准确率具有广泛影响。 移除三个泄漏渠道——元数据、99.2%真实文章中存在的新闻通讯社来源标签，以及污染了 19.4%朴素测试集的 6,251 份重复文档——仅使 F1 下降 1.21 个点（从 0.9935 降至 0.9814），且残余信号是弥散的编辑风格，因为删除权重最高的 1,000 个一元词后 F1 仍为 0.926。在主题不相交协议下，平均精度从 0.9995 降至 0.9475，部署 F1 从 0.9905 降至 0.8067，而微调后的 DistilBERT 退化更严重（损失 12.9 个 AP 点，线性模型仅损失 5.2 个），所有模型在独立的 LIAR 基准上均降至接近随机水平（ROC-AUC 0.54–0.57）。

rss · arXiv - NLP · Sep 23, 04:00

**背景**: ISOT/Kaggle“真假新闻”语料库是一个流行的基准，包含数千篇标记为真实或虚假的文章，广泛用于训练假新闻检测的文本分类器。捷径学习是指模型利用虚假关联或数据集伪影，这些在分布内测试数据上表现良好，但在分布偏移下失效；而数据泄漏是指训练数据中存在预测时不可用的信息，从而虚高模型性能。本文使用透明的 TF-IDF 和线性分类器流程作为测量工具，沿泄漏渠道和分布偏移协议对语料库进行审计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2208.11857">[2208.11857] Shortcut Learning of Large Language Models in Natural Language Understanding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Leakage_(machine_learning)">Leakage ( machine learning ) - Wikipedia</a></li>
<li><a href="https://www.kaggle.com/datasets/rahulogoel/isot-fake-news-dataset">ISOT Fake News Dataset | Kaggle</a></li>

</ul>
</details>

**标签**: `#fake news detection`, `#shortcut learning`, `#data leakage`, `#benchmark audit`, `#NLP`

---

<a id="item-8"></a>
## [用 164 美元在 Rust 中预训练语言模型，暴露框架静默故障](https://arxiv.org/abs/2609.25008) ⭐️ 8.0/10

一篇经验报告（arXiv:2609.25008）记录了完全用纯 Rust 端到端预训练一个约 0.4B 参数、以孟加拉语优先的语言模型，租用 GPU 成本仅 164 美元，训练路径中不含 PyTorch 或 Python。作者记录了 Candle 的五个缺陷（包括融合内核静默地不产生任何梯度）和 Burn 的三个缺陷（包括反向传播仅达到理论 GPU 吞吐量约 3%，以及内核融合路径在数十亿参数规模下训练中途发生段错误），而这些问题都能通过常规的损失曲线检查。 这是首批有记录的纯 Rust 端到端语言模型预训练之一，其经过实测的故障分类表明，Rust 机器学习框架目前还不是训练大模型的有竞争力选择，尽管它们在端侧推理服务方面仍有吸引力。作者提出的梯度流仲裁器——一种断言每个可训练参数都收到有限且非零梯度的测试——是一种可复用的验证技术，任何框架都可以采用它来捕获静默的训练故障。 训练后的模型在孟加拉语上每 token 负对数似然为 0.93，而随机初始化的对照模型为 12.60，但在英语常识选择题上仅达到随机水平，这反映了刻意较小的预算：约 20 亿 token、54.6 小时、单张租用的 H100。报告还记录了孟加拉文脚本中的分词器生育率陷阱：朴素的字节级分词将孟加拉语压缩到约每 token 1.4 个字符，而英语为 3.9 个字符，静默地反转了语料库的语言平衡；修复后达到约 4.1。

rss · arXiv - NLP · Sep 23, 04:00

**背景**: Candle 是 Hugging Face 推出的极简 Rust 机器学习框架，面向轻量级部署并让生产工作负载摆脱 Python；Burn 则是新一代 Rust 张量库和深度学习框架，针对训练和推理都做了优化。两者都比 PyTorch 年轻得多，生态系统的集体调试经验也少得多，这使得训练后端中的静默故障尤其危险。梯度流仲裁器是一种验证测试，它运行一次前向/反向传播，检查每个可训练参数是否都收到有限且非零的梯度，可推广到任何框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/huggingface/candle">GitHub - huggingface/ candle : Minimalist ML framework for Rust</a></li>
<li><a href="https://github.com/tracel-ai/burn">tracel-ai/ burn : Burn is a next generation tensor library and Deep ...</a></li>
<li><a href="https://github.com/Adiuk24/gradient-flow-arbiter">GitHub - Adiuk24/ gradient - flow - arbiter : Verification tooling that...</a></li>

</ul>
</details>

**标签**: `#Rust`, `#Machine Learning`, `#ML Frameworks`, `#Training`, `#Experience Report`

---

<a id="item-9"></a>
## [PICPIs：面向共形预测的自洽条件化框架](https://arxiv.org/abs/2609.25388) ⭐️ 8.0/10

一篇新的 arXiv 论文（arXiv:2609.25388）由包括 Guido Imbens 和 Michael I. Jordan 在内的研究者提出“预测区间条件预测区间”（PICPIs），这是一种共形预测的条件化框架，要求区间 I 满足自洽条件 E[Y | p(X) ∈ I] ∈ I。作者给出了实用的构造算法，推导了概率预测和多分类任务下的推断程序及理论保证，并证明所得区间能覆盖除任意小比例之外的所有预测值，其宽度以 n^{-1/3} 的速率收缩（忽略对数因子和预测误差）。 标准共形预测只提供边际有效性，在决策所依据的具体预测值上分辨率有限，而关于协变量的完全条件保证已被证明无法实现。PICPIs 提供了一种有理论支撑的折中方案，在不改变原始点预测的前提下生成数据自适应的分层，有望改善统计学和机器学习中的下游决策。 该自洽条件同时定义了预测值的分层，并证明该分层内的平均结果落在同一区间内，且构造过程不修改原始预测模型 p。覆盖率和宽度保证在预测分布满足正则性条件下成立，忽略对数因子和预测误差；论文还给出了与现有基于区间的基线方法的实证比较。

rss · arXiv - Data Science & Statistics · Sep 23, 04:00

**背景**: 共形预测是一种无分布假设的技术，只要数据满足可交换性，就能为任意底层点预测器生成统计上有效的预测集合或区间；其做法是在已标注数据上计算非一致性分数，并据此为新样本构建预测集合。预测区间估计的是未来观测值以给定概率落入的范围，这与针对总体参数的置信区间不同。条件期望（条件均值）是随机变量在给定条件概率分布下的期望值，而 PICPIs 要求这一量落在所构造的区间之内。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prediction_interval">Prediction interval</a></li>
<li><a href="https://en.wikipedia.org/wiki/Conditional_expectation">Conditional expectation - Wikipedia</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#uncertainty quantification`, `#statistical inference`, `#prediction intervals`, `#machine learning`

---