---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> From 105 items, 8 important content pieces were selected

---

1. [微软将 Rust 提升为一级语言](#item-1) ⭐️ 9.0/10
2. [AI 辅助开发的 WeWorm 零点击蠕虫通过微信通话传播](#item-2) ⭐️ 9.0/10
3. [Shopify 放弃 React Native，转向原生 Swift 和 Kotlin 应用](#item-3) ⭐️ 8.0/10
4. [研究人员质疑 OpenAI 能否被信任接触未发表的数学成果](#item-4) ⭐️ 8.0/10
5. [索尼因数字游戏所有权主张面临诉讼](#item-5) ⭐️ 8.0/10
6. [论文发现 Option-Critic 的终止规则无效且策略会坏死](#item-6) ⭐️ 8.0/10
7. [无透镜视线传感身份泄露率高达 96.7%，研究揭示隐私风险](#item-7) ⭐️ 8.0/10
8. [AI 的电力需求暴露了脆弱的电网架构](#item-8) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [微软将 Rust 提升为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

微软已正式将 Rust 列为一级语言，使其与 C++、C# 和 TypeScript 并列，成为内部开发中支持最完善的语言之一。该消息通过 Rust 基金会网站的一篇客座文章发布，突显了 Rust 在微软核心项目中日益重要的角色。 这一认可标志着 Rust 在系统编程领域的成熟和广泛采用，可能促使其他大型组织效仿。它也凸显了行业向内存安全语言转型以减少安全漏洞的趋势。 微软的目标包括到 2030 年通过自动化工具将 10 亿行代码转换为 Rust，目标是“1 名工程师、1 个月、100 万行代码”。此外，有传言称 MSVC 将与 Rust 集成，DARPA 也在资助 C 到 Rust 的转换工作。

hackernews · mmastrac · Sep 10, 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是一种专注于内存安全和性能的系统编程语言，由 Mozilla 开发，现由 Rust 基金会维护。在微软，一级语言地位意味着它获得一流的工具、文档和支持，与 C++ 和 C# 等成熟语言类似。内存安全问题（如缓冲区溢出）是用 C 和 C++ 编写的软件中的主要安全漏洞来源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier - 1 Language at Microsoft</a></li>
<li><a href="https://news.ycombinator.com/item?id=49643546">Rust Is Tier - 1 Language at Microsoft | Hacker News</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（579 分，317 条评论）显示出浓厚兴趣，用户提到微软雄心勃勃的 10 亿行代码转换目标以及 DARPA 的 C 到 Rust 转换工作。一些评论者强调 Rust 相比 Zig 和 Odin 等新语言更为成熟，而其他人则讨论了内存安全对减少 CVE 的战略好处。一个值得注意的点是用 MSVC 后端替换 LLVM，表明更深入的集成。

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Language Adoption`

---

<a id="item-2"></a>
## [AI 辅助开发的 WeWorm 零点击蠕虫通过微信通话传播](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，称这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，受害者无需接听电话或与手机交互，账号即可被劫持。该团队表示，他们借助 AI 在大约两天内找到漏洞并写出首个远程代码执行（RCE）利用程序，随后又用约一周时间构建出蠕虫。 这展示了漏洞利用开发的范式转变：过去需要大型团队耗时数月才能完成的蠕虫，据称由一个小团队借助 AI 在约十天内完成，可能使超过十亿微信账号面临风险。这为移动安全、漏洞披露实践和 AI 安全提出了紧迫问题，因为 AI 如今能大幅加速关键漏洞的发现与武器化。 据相关报道，该利用程序针对微信 VoIP 通话栈中的内存破坏漏洞，即使电话未接听或接听后无声，也能在数秒内攻陷目标账号，且该漏洞已私下报告给腾讯。该蠕虫目前是演示/概念验证，而非真实在野攻击，研究人员强调人类判断决定了攻击目标的选择和安全测试方式。

rss · Simon Willison · Sep 10, 00:56

**背景**: 零点击利用无需受害者任何操作，因此比需要点击或下载的攻击危险得多。远程代码执行（RCE）指攻击者能通过网络在受害者设备上运行自己的代码，通常利用缓冲区溢出等内存破坏漏洞。蠕虫是能从一台设备自我传播到另一台的恶意软件；将其与零点击 RCE 以及微信（用户超过十亿）这类广泛使用的应用结合，就可能造成快速、大规模的账号劫持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://cybersecuritynews.com/weworm-first-0-click-worm/">WeWorm – First 0-Click Worm Spreading Through WeChat Calls ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Arbitrary_code_execution">Arbitrary code execution - Wikipedia</a></li>

</ul>
</details>

**标签**: `#security`, `#ai`, `#mobile`, `#exploit`, `#worm`

---

<a id="item-3"></a>
## [Shopify 放弃 React Native，转向原生 Swift 和 Kotlin 应用](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify 宣布将其移动应用从 React Native 迁移回完全原生开发，iOS 使用 Swift，Android 使用 Kotlin。该工程博客文章详细说明了公司放弃这一曾大力投入的跨平台框架的决定。 Shopify 的这一逆转是一个重要的行业信号，因为该公司曾是 React Native 的高调采用者，其举动可能影响其他正在评估跨平台与原生策略的大型移动团队。这一决定也加剧了关于 AI 辅助编程是否让维护独立原生代码库变得更可行的广泛争论。 迁移涉及用 Swift 和 Kotlin 重写应用，社区成员报告使用 AI 编程代理在几天内将 React Native 代码移植到原生平台。然而，仍有人担心团队是否具备维护质量所需的原生专业知识，因为 AI 生成的 Swift 或 Kotlin 代码可能会对不熟悉这些语言的开发者隐藏细微的错误。

hackernews · fnthawar2 · Sep 10, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49643982)

**背景**: React Native 是 Meta 推出的开源框架，允许开发者使用 JavaScript 和 React 构建 iOS 和 Android 应用，并在平台间共享大量代码。Swift 是苹果用于 iOS 和 macOS 的编译型语言，而 Kotlin 是 JetBrains 的语言，被谷歌推荐为 Android 开发的首选。Shopify 此前曾是 React Native 的知名用户，因此其回归原生开发标志着移动工程策略的显著转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://en.wikipedia.org/wiki/Swift_(programming_language)">Swift (programming language)</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者意见严重分歧：一些人认为复杂性必须被驯服而非倍增，AI 处理复杂性的能力与人类一样有限；另一些人则分享了使用 AI 代理在几天内将 React Native 移植到原生的积极经验。一个反复出现的担忧是，不懂 Swift 或 Kotlin 的开发者无法发现 AI 生成的垃圾代码，还有人推荐 Kotlin Multiplatform 作为共享业务逻辑同时保留原生 UI 的折中方案。

**标签**: `#react-native`, `#mobile-development`, `#swift`, `#kotlin`, `#ai-assisted-development`

---

<a id="item-4"></a>
## [研究人员质疑 OpenAI 能否被信任接触未发表的数学成果](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

在 OpenAI 宣布利用一个由 1 万个智能体组成的集群解决了一个长期悬而未决的数学难题后，纽约大学数学家 Tristan Buckmaster 公开指控该公司抢先发表了他的研究成果，称 OpenAI 通过协作式 Codex 对话得知了他的研究进展，随后匆忙发表了一份将他的合作者排除在作者之外的证明。OpenAI 研究员 Sébastien Bubeck 否认了这些指控，OpenAI 随后公布了自己的证明手稿和形式化验证代码，但关键通话的完整录音尚未公开。 随着 AI 实验室与学术界的合作日益增多，这场争议引发了关于研究诚信和署名归属的根本性问题，可能会让研究人员不愿再与商业模型分享未发表的想法。它可能重塑 AI 公司如何标注外部贡献以及机密研究对话是否被用于模型训练的规范。 争议的核心在于 OpenAI 的模型是受益于 Buckmaster 的私有 Codex 数据，还是通过在海量算力下对可验证数学问题进行强化学习而独立发现了解决方案。OpenAI 已公布其证明手稿和形式化验证代码，但未公开关键通话的完整录音，使得这些想法的来源仍存争议。

hackernews · pred_ · Sep 10, 06:49 · [社区讨论](https://news.ycombinator.com/item?id=49639408)

**背景**: OpenAI 已向许多研究人员免费开放其模型，包括面向编码和工作场景的 AI 工具 Codex，据报道其内部模型解决开放数学问题的速度惊人。开放问题是研究人员通常需要花费数年时间攻克的未解数学难题，而将新想法输入 AI 对话可能会无意中为模型训练做出贡献。形式化验证是一种由计算机检查证明的过程，正越来越多地被用于验证 AI 生成的数学结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://venturebeat.com/technology/openai-solves-longstanding-math-problem-with-10-000-agent-swarm-but-cant-rule-out-benefitting-from-a-researchers-private-codex-data">OpenAI solves longstanding math problem with 10,000-agent swarm — but can't rule out benefitting from a researcher's private Codex data | VentureBeat</a></li>
<li><a href="https://finance.biggo.com/news/b05bc0db-1896-4282-9106-fb3da78adc03">AI cracks a Millennium Prize-adjacent problem, igniting a credit war: NYU mathematician accuses OpenAI of scooping his work — BigGo Finance</a></li>
<li><a href="https://www.stork.ai/blog/openais-stolen-math-proof">OpenAI Navier-Stokes Controversy: AI Authorship & Ethics | Stork.AI</a></li>

</ul>
</details>

**社区讨论**: 评论者将其类比为人类合作者，认为如果 OpenAI 是一个人，基于协作对话发表成果却不署名将是非常不道德的。一些人建议唯一合乎道德的做法是提供免费额度和工具支持，而不是抢先发表；另一些人则指出两件事可能同时成立：模型可能记住了对话数据，同时也通过强化学习独立发现了超人级的技术。少数人对研究人员的判断力表示怀疑，或对争议漠不关心。

**标签**: `#OpenAI`, `#research ethics`, `#AI collaboration`, `#attribution`, `#mathematics`

---

<a id="item-5"></a>
## [索尼因数字游戏所有权主张面临诉讼](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 8.0/10

针对索尼 PlayStation 商店“购买”按钮的集体诉讼引发关注，索尼在辩护中主张玩家无法真正拥有数字游戏，仅获得许可。一个维基页面汇编了索尼关于所有权的矛盾陈述，在 Hacker News 上引发讨论，获得 347 分和 115 条评论。 此案可能为数字商品的营销和销售方式树立先例，不仅影响游戏玩家，还影响电子书、电影和软件等所有数字内容的消费者。它凸显了消费者对所有权的期望与主导数字分发的许可模式之间日益紧张的关系。 索尼的辩护包括其服务条款第 14 条中的约束性仲裁条款和集体诉讼豁免，要求用户在 30 天内选择退出。该诉讼特别质疑 PlayStation 商店对实际为可撤销许可的数字游戏使用“购买”按钮。

hackernews · haunter · Sep 10, 12:18 · [社区讨论](https://news.ycombinator.com/item?id=49642531)

**背景**: 数字游戏通常作为许可而非实体产品出售，这意味着用户并不拥有游戏本身，而是在特定条件下访问它的权利。当内容被移除或访问被撤销时，这引发了消费者的强烈反对，例如索尼 2024 年合并 Crunchyroll 和 FUNimation 时用户失去了已购买内容的访问权。“停止杀死游戏”运动和日益增加的监管审查是重新定义数字所有权的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/tech/sony-digital-game-ownership-lawsuit/">Sony Digital Game Ownership Fight: You Can’t Own Games, It ...</a></li>
<li><a href="https://openclassactions.com/lawsuits/consumer-protection/sony-playstation-digital-game-license-class-action-lawsuit.php">Do You Own Digital Games You Buy? Sony Lawsuit Explained</a></li>
<li><a href="https://www.ign.com/articles/playstation-claims-digital-games-are-not-really-owned-by-players-in-response-to-class-action-lawsuit">PlayStation's Response to Class-Action Lawsuit Over Digital ...</a></li>

</ul>
</details>

**社区讨论**: 评论者批评约束性仲裁条款不公平，并争论购买书籍与数字游戏的类比，指出实体副本是独立的而数字许可则不是。一些人指出索尼的辩护可能适得其反，暗示如果用户不拥有副本，索尼可能一开始就无权出售它，其他人则因过去的 rootkit 丑闻等事件对索尼持矛盾态度。

**标签**: `#digital-ownership`, `#consumer-rights`, `#legal`, `#gaming`, `#sony`

---

<a id="item-6"></a>
## [论文发现 Option-Critic 的终止规则无效且策略会坏死](https://arxiv.org/abs/2609.05508) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.05508）从理论和实验两方面证明，option-critic 学到的终止规则对性能毫无贡献，并且选项内部的策略存在一种被作者命名为“策略坏死”（policy necrosis）的失效模式。作者报告称，强制每一步都终止并不会改变选项数量与性能的关系曲线，而且在典型选项中大约五分之三的状态是坏死的。 Option-critic 是分层强化学习中的基础性方法，其“增加选项能提升性能”的核心结论影响了研究者设计选项发现方法的思路。如果终止规则是冗余的、且选项内部策略无法有效探索，那么该领域对选项收益的许多假设可能需要重新评估。 当终止测试与选项选择策略读取相同的值时，测试会在每一步触发，使学到的规则等同于始终终止；当策略进行探索而测试不探索时，该规则会阻碍探索，某些情形下会带来 Ω(T) 的遗憾，而始终终止仅为 O(log T)。论文还给出了策略坏死的状态级检测方法，并表明恢复探索可以修复坏死状态，之后单个选项即可解决任务。

rss · arXiv - Machine Learning · Sep 10, 04:00

**背景**: 选项（options）框架由 Sutton、Precup 和 Singh 于 1999 年提出，将时间上延展的动作建模为带有各自终止条件的子策略，从而在强化学习中实现时间抽象。Option-critic 架构（Bacon、Harb 和 Precup，2016）首次通过策略梯度定理端到端地学习选项内部策略、终止函数以及选项选择策略，无需额外奖励或子目标。此类分层强化学习方法旨在通过将任务分解为可复用的技能，把学习扩展到长时程任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/1609.05140">[1609.05140] The Option-Critic Architecture</a></li>
<li><a href="https://campusai.github.io/papers/the-option-critic-architecture">The Option Critic Architecture</a></li>
<li><a href="https://rljclub.github.io/posts/hierarchical-reinforcement-learning/">Hierarchical Reinforcement Learning: From Options to Goal ...</a></li>

</ul>
</details>

**标签**: `#reinforcement learning`, `#hierarchical RL`, `#option-critic`, `#policy necrosis`, `#exploration`

---

<a id="item-7"></a>
## [无透镜视线传感身份泄露率高达 96.7%，研究揭示隐私风险](https://arxiv.org/abs/2609.09188) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.09188）对模拟的无透镜视线传感流程进行了审计，发现在 36 名受试者的闭集识别协议下，视觉上难以理解的编码测量仍能以 96.7%的 top-1 准确率恢复身份，几乎与原始眼部裁剪图像的 97.7%持平。作者表明压缩和降维几乎无法提供保护：8 维 PCA 和匹配的 8 维瓶颈分别保留 93.2%和 91.8%的恢复率，而发布的 128 路视线令牌将单帧恢复率降至 38.1%。 这项工作挑战了人们普遍认为无透镜近眼传感因其原始测量看似噪声而天然保护隐私的假设，对生物特征安全、视线追踪和边缘传感系统中的隐私设计声明具有重要影响。它主张隐私必须在每个披露边界（传感、存储、计算和输出）进行审计，而不能仅凭视觉外观推断。 该审计使用固定且已知的点扩散函数（PSF）以及匹配的线性与 MLP 探针，因此报告的准确率是经验性攻击成功率，并不构成更强攻击者的上界，且未知或变化光学密钥下的隐私不在研究范围内。即使对六维裁剪几何与强度摘要做普通最小二乘残差化后，无透镜恢复率仍达 95.1%；在源帧不相交的分块协议下，T=25 时令牌摘要达到 39.9%。

rss · arXiv - Computer Vision · Sep 10, 04:00

**背景**: 无透镜近眼传感用编码掩模取代镜头，产生的测量看似难以理解的图案，但可通过计算重建；点扩散函数（PSF）描述光学系统如何将一个光点扩散开来。由于这些测量难以被人类解读，常被宣传为隐私友好，但本文把身份隐私视为披露面的系统属性，并用掩码自编码器（MAE）嵌入等学习型攻击者进行测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.09188">[2609.09188] Lensless Gaze Is Not Private by Default ...</a></li>
<li><a href="https://github.com/xoxo121/Lensless-Gaze-Is-Not-Private-by-Default">GitHub - xoxo121/Lensless-Gaze-Is-Not-Private-by-Default</a></li>
<li><a href="https://en.wikipedia.org/wiki/Point_spread_function">Point spread function - Wikipedia</a></li>

</ul>
</details>

**标签**: `#privacy`, `#lensless sensing`, `#gaze tracking`, `#biometric security`, `#adversarial machine learning`

---

<a id="item-8"></a>
## [AI 的电力需求暴露了脆弱的电网架构](https://www.technologyreview.com/2026/09/10/1141649/powering-ai-is-an-architecture-problem/) ⭐️ 8.0/10

2026 年 7 月 22 日，位于弗吉尼亚州阿什本（全球最大的数据中心集群）的一条输电线路发生故障，在几秒钟内使电网损失了超过 3 吉瓦的负载。此前 2024 年曾发生一起单一避雷器故障导致约 60 个弗吉尼亚设施和 1500 兆瓦负载同时脱网的事件，而《麻省理工科技评论》认为这些事件表明，为 AI 供电本质上是一个架构问题。 随着 AI 训练和推理在少数地理枢纽中带来前所未有的功率密度，电网无法承受突然的大规模负载损失，这不仅威胁数据中心的正常运行时间，也威胁更广泛的电网稳定性。这影响到 AI/ML 公司、云服务提供商、电力公司以及共享同一基础设施的数百万电力用户。 2026 年 7 月的故障在几秒内切除了超过 3 吉瓦的负载，而更早的避雷器故障则使约 60 个设施损失了约 1500 兆瓦，说明单个组件故障如何级联为大规模的同时负载损失。这些事件凸显出当前电网架构缺乏足够的冗余、快速故障隔离以及针对集中式 AI 数据中心负载的减载协调能力。

rss · MIT Technology Review · Sep 10, 11:00

**背景**: 弗吉尼亚州阿什本位于华盛顿特区西北约 30 英里处，是全球最大的数据中心和互联网互联枢纽，拥有来自多家运营商的 140 多个设施。输电线路故障是指短路或绝缘失效等可能导致停电的扰动，而避雷器是一种将电压尖峰引开的保护装置；一旦它失效，就可能引发级联停电。由于 AI 工作负载将巨大的电力需求集中在这些枢纽，单条线路或单个保护装置的失效就可能突然切除数吉瓦的负载，给电网频率和稳定性带来压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Ashburn,_Virginia">Ashburn , Virginia - Wikipedia</a></li>
<li><a href="https://www.inmr.com/principal-failure-modes-surge-arresters/">Failure Modes for Surge Arresters -</a></li>
<li><a href="https://ideas.repec.org/a/eee/energy/v355y2026ics0360544226012739.html">Improve MicroGrid connected systems with hybrid Wolf-Bird Optimizer...</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#data centers`, `#power grid`, `#energy systems`, `#architecture`

---