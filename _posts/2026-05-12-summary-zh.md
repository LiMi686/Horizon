---
layout: default
title: "Horizon Summary: 2026-05-12 (ZH)"
date: 2026-05-12
lang: zh
---

> From 92 items, 39 important content pieces were selected

---

1. [TanStack NPM 供应链攻击事后分析](#item-1) ⭐️ 9.0/10
2. [UCLA 发现首款修复脑损伤的中风康复药物](#item-2) ⭐️ 9.0/10
3. [AUTOMATIC1111 的 Stable Diffusion WebUI：首选界面](#item-3) ⭐️ 9.0/10
4. [实时多模态 Transformer 微轮交互模型](#item-4) ⭐️ 8.0/10
5. [GitLab 裁员并放弃 CREDIT 价值观，启动‘第二幕’战略转型](#item-5) ⭐️ 8.0/10
6. [AI 编码代理必须按比例降低维护成本](#item-6) ⭐️ 8.0/10
7. [AI 写作催生‘僵尸互联网’](#item-7) ⭐️ 8.0/10
8. [Shopify 的 River：公开编码代理作为教学工坊](#item-8) ⭐️ 8.0/10
9. [字节跳动开源多模态 AI 智能体栈 TARS](#item-9) ⭐️ 8.0/10
10. [CloakBrowser：通过所有机器人检测的隐身 Chromium 浏览器](#item-10) ⭐️ 8.0/10
11. [用 PyTorch 从零构建类 ChatGPT 的大语言模型](#item-11) ⭐️ 8.0/10
12. [Agentmemory：AI 编码代理的持久记忆](#item-12) ⭐️ 8.0/10
13. [微信 4.x 数据库解密工具从内存提取密钥](#item-13) ⭐️ 8.0/10
14. [VLM 可靠性探针挑战注意力-置信度假设](#item-14) ⭐️ 8.0/10
15. [自动评分标准作为奖励：显式多模态生成准则](#item-15) ⭐️ 8.0/10
16. [面向偏好而非语义的嵌入](#item-16) ⭐️ 8.0/10
17. [自由能框架区分能力激发与能力创造](#item-17) ⭐️ 8.0/10
18. [MemQ：将 Q 学习与资格迹结合，实现自演化记忆智能体](#item-18) ⭐️ 8.0/10
19. [SkillLens：面向 LLM 智能体的分层技能复用框架](#item-19) ⭐️ 8.0/10
20. [LLM 通过双重机制进行上下文学习](#item-20) ⭐️ 8.0/10
21. [BaLoRA：贝叶斯低秩自适应提升准确率与不确定性估计](#item-21) ⭐️ 8.0/10
22. [KV 缓存量化方案的统计分析](#item-22) ⭐️ 8.0/10
23. [长文本幻觉检测的合理性检验](#item-23) ⭐️ 8.0/10
24. [研究发现语言模型电路并非任务特化](#item-24) ⭐️ 8.0/10
25. [冻结塔组合实现高效多模态嵌入](#item-25) ⭐️ 8.0/10
26. [基于 LLM 的模型将解释转化为行动计划](#item-26) ⭐️ 8.0/10
27. [Sem-ECE：面向开放式问答的新校准评估指标](#item-27) ⭐️ 8.0/10
28. [自描述方法提升视觉语言模型的鲁棒性](#item-28) ⭐️ 8.0/10
29. [VT-Bench：首个视觉-表格多模态学习统一基准](#item-29) ⭐️ 8.0/10
30. [HY-Himmel：通过分层运动编码实现高效长视频理解](#item-30) ⭐️ 8.0/10
31. [WATCH 框架实现月度级考古遗址变化检测](#item-31) ⭐️ 8.0/10
32. [MULTITEXTEDIT：跨语言图像文本编辑基准](#item-32) ⭐️ 8.0/10
33. [Sinkhorn 处理效应：因果最优传输度量](#item-33) ⭐️ 8.0/10
34. [平均场理论揭示多分量 ICA 中的相变](#item-34) ⭐️ 8.0/10
35. [CONTRA：利用归一化流进行共形预测](#item-35) ⭐️ 8.0/10
36. [用于去中心化不动点问题的核心-晕分解方法](#item-36) ⭐️ 8.0/10
37. [基于扩散的新方法测量高维模态分离](#item-37) ⭐️ 8.0/10
38. [通过 Softmax 单位划分证明 Transformer 的逼近能力](#item-38) ⭐️ 8.0/10
39. [无噪声逆优化的紧泛化界](#item-39) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [TanStack NPM 供应链攻击事后分析](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem) ⭐️ 9.0/10

TanStack Router 的 NPM 包通过 CI 管道攻击被攻陷，攻击者获取了 GitHub Actions 缓存并窃取了发布令牌，导致恶意负载包含一个死亡开关，如果令牌被撤销，则会擦除用户的主目录。 此事件凸显了 CI/CD 安全中的关键漏洞以及使用长期令牌发布包的风险，影响了整个 npm 生态系统以及依赖 TanStack 库的数千名开发者。 攻击利用了 GitHub Actions 缓存投毒和 postinstall 脚本执行负载，该负载安装了 systemd 服务或 LaunchAgent 来监控被盗令牌的有效性，并在令牌被撤销时触发数据销毁。

hackernews · varunsharma07 · May 11, 21:08 · [社区讨论](https://news.ycombinator.com/item?id=48100706)

**背景**: 供应链攻击针对软件开发管道，将恶意代码注入受信任的包中。NPM 包通常使用 postinstall 等生命周期脚本，在安装时自动运行，使其成为常见攻击向量。具有缓存依赖项和长期令牌的 CI/CD 管道是攻击者的诱人目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cyberpress.org/84-tanstack-npm-packages-compromised-in-ongoing-supply-chain-attack-targeting-ci-credentials/">84 TanStack npm Packages Compromised in Ongoing Supply-Chain Attack Targeting CI Credentials</a></li>
<li><a href="https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem">TeamPCP's Mini Shai-Hulud Is Back: A Self-Spreading Supply Chain Attack Compromises TanStack npm Packages - StepSecurity</a></li>
<li><a href="https://cyberpress.org/dead-mans-switch-widespread-npm-supply-chain-attack-driving-malware-attacks/">Dead Man’s Switch: Widespread npm Supply Chain Attack Driving ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论警告死亡开关会在令牌撤销时删除主目录，并讨论了可能导致缓存投毒的 CI 管道 YAML 配置的复杂性。一些人认为仅靠 Trusted Publishing 是不够的，并强调 postinstall 脚本很危险，推荐使用 pnpm 作为更安全的替代方案。

**标签**: `#supply-chain security`, `#npm`, `#CI/CD`, `#open-source`, `#incident response`

---

<a id="item-2"></a>
## [UCLA 发现首款修复脑损伤的中风康复药物](https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage) ⭐️ 9.0/10

UCLA 研究人员发现了首个针对中风康复的药物候选物，该药物靶向远离中风病灶的脑细胞连接中断，恢复存活网络中的连接和功能。该化合物是一种小清蛋白神经元调节剂，已在小鼠实验中显示出运动与认知功能的显著恢复。 中风是成人残疾的主要原因，目前尚无针对中风康复的药物，仅依靠物理康复。这一突破可能通过药物修复脑连接来改变中风治疗，有望改善全球数百万患者的预后。 该药物特异性靶向小清蛋白神经元，这类神经元对维持中风后的脑节律和连接至关重要。研究已发表在同行评审期刊上，该化合物被认为是潜在的首创中风康复药物，但目前仅在小鼠中进行了测试。

hackernews · bookofjoe · May 11, 17:53 · [社区讨论](https://news.ycombinator.com/item?id=48098261)

**背景**: 中风发生时，大脑某部分的血液供应中断，导致受影响区域的脑细胞死亡。然而，存活的脑细胞可能会“挫伤”，并失去与远处网络的连接，导致持续性残疾。此前，尚无药物能够修复这些丢失的连接，康复依赖于物理治疗和神经可塑性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stemcell.ucla.edu/news/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain-damage">UCLA discovers first stroke rehabilitation drug to repair brain damage</a></li>
<li><a href="https://www.uclahealth.org/news/release/ucla-discovers-first-stroke-rehabilitation-drug-repair-brain">UCLA discovers first stroke rehabilitation drug to repair brain damage in mice | UCLA Health</a></li>
<li><a href="https://newsroom.ucla.edu/releases/ucla-discovers-first-stroke-rehabilitation-drug-to-reestablish-brain-connections-in-mice">UCLA discovers first stroke rehabilitation drug to reestablish brain connections in mice | UCLA</a></li>

</ul>
</details>

**社区讨论**: 评论者澄清，该药物针对的是存活脑细胞的连接中断，而非中风核心区域的细胞死亡——后者仍不可逆。有人对治疗阿尔茨海默病的潜力表示兴奋，也有人引用特德·姜的科幻小说《领悟》来强调其戏剧性影响。

**标签**: `#neuroscience`, `#stroke`, `#drug discovery`, `#brain repair`, `#medical breakthrough`

---

<a id="item-3"></a>
## [AUTOMATIC1111 的 Stable Diffusion WebUI：首选界面](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ⭐️ 9.0/10

AUTOMATIC1111/stable-diffusion-webui 仓库提供了一个基于 Gradio 的全面 Web 界面，用于 Stable Diffusion，具有 txt2img、img2img、inpainting、outpainting 以及注意力控制、文本反转和放大等许多高级选项。 该 Web UI 已成为与 Stable Diffusion 交互的事实标准，使 AI 图像生成对艺术家、爱好者和研究人员变得普及。其丰富的功能集和活跃的开发塑造了 AI 艺术社区的工作流程。 该 UI 支持 4GB VRAM（据报道 2GB 也可用），包含一键安装脚本，并将生成参数保存在 PNG/EXIF 元数据中。它还提供负面提示、样式、X/Y/Z 图和低 VRAM 占用的实时预览。

rss · GitHub Trending - Daily (All) · May 12, 14:31

**背景**: Stable Diffusion 是一种潜在文本到图像扩散模型，可根据文本描述生成图像。Gradio 是一个开源 Python 库，用于快速为机器学习模型创建 Web UI。该 Web UI 将这些技术打包成一个易于使用的工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gradio.app/">Gradio</a></li>
<li><a href="https://stable-diffusion-art.com/outpainting/">How to use outpainting to extend images - Stable Diffusion Art</a></li>

</ul>
</details>

**标签**: `#stable-diffusion`, `#AI-art`, `#image-generation`, `#machine-learning`, `#open-source`

---

<a id="item-4"></a>
## [实时多模态 Transformer 微轮交互模型](https://thinkingmachines.ai/blog/interaction-models/) ⭐️ 8.0/10

Thinking Machines AI 发布了一篇博客文章和演示，展示了一个基于 Transformer 的模型，该模型通过 200 毫秒的时间对齐微轮，近乎实时地处理文本、图像和音频输入，并生成文本和音频输出。 这种新颖的交互模型实现了输入和输出的连续交错，使人机对话更加自然和响应迅速，可能改变虚拟助手、客户服务和无障碍工具等应用。 该架构是一个多模态 Transformer，在文本、图像和音频上联合训练，以 200 毫秒输入处理和 200 毫秒输出生成的微轮方式运行，实现近乎实时的交互。

hackernews · smhx · May 11, 20:53 · [社区讨论](https://news.ycombinator.com/item?id=48100524)

**背景**: 传统 AI 模型在处理完整输入（如整句话）后才生成响应，导致延迟。该模型使用时间对齐的微轮，连续交错输入和输出的小块，类似于人类在对话中停顿和反应的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_learning">Multimodal learning - Wikipedia</a></li>
<li><a href="https://www.emergentmind.com/topics/multimodal-transformer-models">Multimodal Transformer Models</a></li>

</ul>
</details>

**社区讨论**: 评论者对自然的停顿和实时行为印象深刻，有人称其为交互式 AI 的突破。但也有人担心可能被滥用于监控，部分人认为演示显得刻意，缺乏明确的商业应用场景。

**标签**: `#AI`, `#machine learning`, `#real-time interaction`, `#transformer`, `#multimodal`

---

<a id="item-5"></a>
## [GitLab 裁员并放弃 CREDIT 价值观，启动‘第二幕’战略转型](https://about.gitlab.com/blog/gitlab-act-2/) ⭐️ 8.0/10

GitLab 宣布裁员并废除其 CREDIT 价值观框架，将此举定位为抓住软件开发‘智能体时代’机遇的战略转型。 此举标志着这家领先的 DevOps 公司发生重大转变，可能影响数千名开发者和整个 DevSecOps 生态系统，同时引发对 AI 驱动企业重组背后真实动机的质疑。 GitLab 股价在过去一年下跌 50%，从约 52 美元降至 26 美元；公司作为‘GitLab 第二幕’的一部分，废除了 CREDIT 价值观（协作、结果、效率、多样性、迭代、透明度）。

hackernews · AnonGitLabEmpl · May 11, 20:51 · [社区讨论](https://news.ycombinator.com/item?id=48100500)

**背景**: GitLab 是一个用于软件开发、CI/CD 和安全的主要 DevOps 平台。其 CREDIT 价值观曾是公司文化的核心部分，指导团队运作方式。‘智能体时代’指 AI 智能体自主执行任务的趋势，GitLab 声称这将增加对软件的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.gitlab.com/blog/gitlab-act-2/">GitLab Act 2</a></li>
<li><a href="https://news.ycombinator.com/item?id=48100500">GitLab Announces Workforce Reduction and End of Their CREDIT Values | Hacker News</a></li>
<li><a href="https://docs.gitlab.com/subscriptions/gitlab_credits/">GitLab Credits and usage billing | GitLab Docs</a></li>

</ul>
</details>

**社区讨论**: 社区评论持怀疑态度：一位用户指出 GitLab 股价 12 个月内下跌 50%，暗示 AI 转型可能是对投资者压力的回应。另一位质疑减少资源如何与声称的‘史上最大机遇’相符。其他人则批评 GitLab 的产品路线图和长期未解决的问题。

**标签**: `#GitLab`, `#layoffs`, `#AI strategy`, `#DevOps`, `#corporate culture`

---

<a id="item-6"></a>
## [AI 编码代理必须按比例降低维护成本](https://simonwillison.net/2026/May/11/james-shore/#atom-everything) ⭐️ 8.0/10

James Shore 认为，AI 编码代理必须按比例降低维护成本，否则团队将面临不可持续的技术债务。他提出了一个数学模型，表明在不将维护成本减半的情况下将代码输出加倍，会使总维护负担增加四倍。 这一见解揭示了 AI 辅助编码热潮中的一个关键盲点：更快的代码生成如果没有相应的维护成本降低，会导致债务呈指数级增长。它迫使团队和工具供应商在追求原始生产力的同时，优先考虑可维护性。 Shore 的论点以数学框架呈现：如果生产力倍数为 P，维护成本倍数为 M，则总维护负担为 P × M。要保持负担不变，M 必须等于 1/P。他警告说，如果没有这样的降低，团队就会用暂时的速度换取永久的束缚。

rss · Simon Willison · May 11, 19:48

**背景**: AI 编码代理是使用大型语言模型（LLM）帮助开发者编写、调试和优化代码的工具。技术债务是指由于短期权宜之计而导致的未来系统维护成本。Shore 的论点将这些概念联系起来，警告说如果不解决维护成本问题，AI 生成的代码可能比传统代码更快地积累债务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Technical_debt">Technical debt - Wikipedia</a></li>
<li><a href="https://github.com/resources/articles/what-are-ai-agents">What are AI agents ? · GitHub</a></li>

</ul>
</details>

**标签**: `#AI-assisted coding`, `#software maintenance`, `#productivity`, `#technical debt`

---

<a id="item-7"></a>
## [AI 写作催生‘僵尸互联网’](https://simonwillison.net/2026/May/11/zombie-internet/#atom-everything) ⭐️ 8.0/10

Jason Koebler 发表了一篇愤怒但精彩的文章，提出了‘僵尸互联网’这一术语，用以描述 AI 生成的内容如何污染互联网并扭曲人类的写作风格。 这很重要，因为它揭示了过滤 AI 内容带来的日益严重的精神疲惫，并警告 AI 不仅是在增加噪音，还在积极重塑人类在线写作的方式，威胁到真实的交流。 Koebler 将‘僵尸互联网’与‘死互联网’理论区分开来：前者涉及人与机器人及 AI 代理的互动，而不仅仅是机器人与机器人对话。他列举了 AI 网红、自动化 YouTube 频道以及被当作真书出售的 AI 摘要等例子。

rss · Simon Willison · May 11, 19:21

**背景**: ‘死互联网’理论是一种阴谋论，声称自 2016 年左右以来，互联网上的大部分内容和互动都是由机器人和算法生成的。Koebler 的‘僵尸互联网’概念针对 AI 时代进行了更新，描述了一种更隐蔽的人机混合活动，人们有意使用 AI 创建内容并与他人互动，模糊了真实与合成之间的界限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dead_Internet_theory">Dead Internet theory</a></li>
<li><a href="https://www.fastcompany.com/91489308/zombie-internet-devastating-consequences-advertising-social-media-human-web-dead-internet-moltbook-ai-tbpn">The ‘ zombie internet ’ has arrived—and it has... - Fast Company</a></li>

</ul>
</details>

**标签**: `#AI`, `#internet culture`, `#content quality`, `#ethics`, `#writing`

---

<a id="item-8"></a>
## [Shopify 的 River：公开编码代理作为教学工坊](https://simonwillison.net/2026/May/11/learning-on-the-shop-floor/#atom-everything) ⭐️ 8.0/10

Shopify CEO Tobias Lütke 透露，其内部编码代理 River 完全在公开的 Slack 频道中运行，拒绝私信并鼓励开放协作。这种方法将每次编码会话转变为所有员工透明、可搜索且具有教育意义的体验。 这种模式将 AI 辅助开发从私人生产力工具转变为共享学习平台，可能加速整个组织的知识传递和入职培训。它也为公司如何设计 AI 工具以促进透明度和集体技能建设树立了先例。 River 在像#tobi_river 这样的公开频道中运行，超过 100 人可以观察、反应和贡献。Lütke 将其描述为“Lehrwerkstatt”（教学工坊），实现无需正式课程或培训计划的“渗透式学习”。

rss · Simon Willison · May 11, 15:46

**背景**: 像 Claude Code 和 Jules 这样的 AI 编码代理通常由个人开发者私下使用。Shopify 的方法与之相反，使代理的工作完全可见，其灵感来源于 Midjourney 早期的公开 Discord 频道，用户在那里分享提示并集体学习。德语概念“Lehrwerkstatt”指的是通过实践、独立于生产的学习来传授实用技能的工坊。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wirtschaftslexikon.gabler.de/definition/lehrwerkstatt-38603">Lehrwerkstatt • Definition | Gabler Wirtschaftslexikon</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#software engineering`, `#team collaboration`, `#knowledge sharing`, `#Shopify`

---

<a id="item-9"></a>
## [字节跳动开源多模态 AI 智能体栈 TARS](https://github.com/bytedance/UI-TARS-desktop) ⭐️ 8.0/10

字节跳动发布了一个名为 TARS 的开源多模态 AI 智能体栈，包含两个组件：Agent TARS，一个提供 CLI 和 Web UI 的通用多模态 AI 智能体；以及 UI-TARS Desktop，一个基于 UI-TARS 视觉语言模型的原生 GUI 智能体桌面应用。 字节跳动作为一家大型科技公司发布此项目，大大降低了开发者和研究人员构建和部署多模态 AI 智能体的门槛，这些智能体可以通过自然语言控制计算机和浏览器，从而加速 GUI 自动化和基于智能体的系统的创新。 Agent TARS 集成了 MCP 工具，并通过多模态大语言模型支持类人任务完成；UI-TARS Desktop 则提供本地和远程的计算机及浏览器操作功能。该栈完全开源，可在 GitHub 上获取。

rss · GitHub Trending - Daily (All) · May 12, 14:31

**背景**: 多模态 AI 智能体能够处理并基于多种数据类型（如文本、图像和 GUI 截图）自主执行任务。基于智能体的模型通过模拟自主智能体的交互来理解复杂系统。字节跳动的 TARS 栈将这些概念结合成一个实用的开源工具包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/bytedance/UI-TARS-desktop">Agent TARS UI-TARS-desktop - GitHub</a></li>
<li><a href="https://agent-tars.com/">Agent TARS - Open-source Multimodal AI Agent Stack</a></li>
<li><a href="https://ui-tarsai.com/">Bytedance UI - TARS AI Desktop : AI Agent for Computer Control</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，许多人称赞字节跳动开源了如此实用的工具。一些讨论聚焦于本地 AI 智能体替代云端依赖解决方案的潜力，另一些人则指出需要更多文档和示例。

**标签**: `#AI`, `#open-source`, `#multimodal`, `#agent`, `#ByteDance`

---

<a id="item-10"></a>
## [CloakBrowser：通过所有机器人检测的隐身 Chromium 浏览器](https://github.com/CloakHQ/CloakBrowser) ⭐️ 8.0/10

CloakBrowser 是一款新的开源隐身 Chromium 浏览器，通过 49 个 C++源码级指纹补丁，在 30/30 的机器人检测测试中全部通过，包括 Cloudflare Turnstile 和 reCAPTCHA v3。它可作为 Playwright 和 Puppeteer 的直接替代品，只需更改导入语句即可。 该工具解决了网页抓取和自动化中的一个主要痛点，提供了一种绕过高级机器人检测系统的可靠方法，可能为开发者节省大量时间和资源。其开源特性和零配置设置降低了需要不可检测浏览器自动化的门槛。 这些补丁在 C++源码级别修改指纹，涵盖 canvas、WebGL、音频、字体、GPU、屏幕、WebRTC、网络时序、自动化信号和 CDP 输入行为。它还包含一个 humanize=True 标志，可模拟类人鼠标轨迹、键盘时序和滚动模式，达到 0.9 的 reCAPTCHA v3 评分。

rss · GitHub Trending - Daily (All) · May 12, 14:31

**背景**: 网站使用 Cloudflare Turnstile 和 reCAPTCHA 等机器人检测系统来区分自动化浏览器和人类用户。传统的自动化工具如 Playwright 和 Puppeteer 常常因为留下可识别的浏览器环境指纹而被检测到。CloakBrowser 直接修改 Chromium 源码以移除这些指纹，使浏览器看起来与普通用户的浏览器无异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/CloakHQ/CloakBrowser">GitHub - CloakHQ/CloakBrowser: Stealth Chromium that passes every bot detection test. Drop-in Playwright replacement with source-level fingerprint patches. 30/30 tests passed. · GitHub</a></li>
<li><a href="https://cloakbrowser.dev/">CloakBrowser — Stealth Chromium for Browser Automation</a></li>

</ul>
</details>

**标签**: `#web scraping`, `#browser automation`, `#anti-detection`, `#chromium`, `#playwright`

---

<a id="item-11"></a>
## [用 PyTorch 从零构建类 ChatGPT 的大语言模型](https://github.com/rasbt/LLMs-from-scratch) ⭐️ 8.0/10

Sebastian Raschka 发布了一个全面的 GitHub 仓库及配套书籍，教授如何使用 PyTorch 从零构建类似 GPT 的大语言模型，涵盖开发、预训练和微调。 该资源为 AI 从业者和研究人员提供了一条易于理解的逐步路径，以深入理解大语言模型的内部机制，弥合理论与实践之间的差距。它还包含加载更大预训练模型进行微调的代码，使其在实际应用中具有实用性。 该仓库是书籍《Build a Large Language Model (From Scratch)》（ISBN 9781633437166）的官方代码，包含目录、设置指南以及针对 Linux 和 Windows 的持续集成测试。其方法模仿了创建像 ChatGPT 这样的大规模基础模型所使用的途径。

rss · GitHub Trending - Daily (All) · May 12, 14:31

**背景**: 像 GPT 这样的大语言模型是在海量文本数据上训练的深度神经网络，能够生成类似人类的文本。从零构建一个这样的模型需要理解 Transformer 架构、注意力机制和训练流程。该仓库为教育目的简化了这一过程。

**标签**: `#LLM`, `#PyTorch`, `#GPT`, `#deep learning`, `#tutorial`

---

<a id="item-12"></a>
## [Agentmemory：AI 编码代理的持久记忆](https://github.com/rohitg00/agentmemory) ⭐️ 8.0/10

Agentmemory 是一个新的开源库，为 Claude Code、Cursor 和 Gemini CLI 等 AI 编码代理提供持久记忆，基于 iii 引擎构建，并扩展了 Karpathy 的 LLM Wiki 模式，增加了置信度评分、生命周期管理、知识图谱和混合搜索。 这解决了使用 AI 编码代理的开发者的一个主要痛点——他们经常需要在不同会话中重新解释上下文。通过让代理记住过去的交互，agentmemory 可以显著提高生产力，并将令牌使用量减少高达 92%。 Agentmemory 在 R@5 上实现了 95.2% 的检索召回率，提供 51 个 MCP 工具和 12 个自动钩子，无需外部数据库，并通过了 827 项测试。它适用于任何 MCP 客户端，并可在 npm 上获取。

rss · GitHub Trending - Daily (All) · May 12, 14:31

**背景**: 像 Claude Code 和 Cursor 这样的 AI 编码代理通过编写代码来帮助开发者，但它们缺乏持久记忆，因此会在会话之间忘记上下文。模型上下文协议（MCP）是一个开放标准，用于连接 AI 代理与数据源。Karpathy 的 LLM Wiki 模式使用结构化 Markdown 文件作为 LLM 的知识库，agentmemory 通过高级功能对其进行了扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/rohitg00/agentmemory">GitHub - rohitg00/agentmemory: #1 Persistent memory for AI coding agents based on real-world benchmarks · GitHub</a></li>
<li><a href="https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f">llm-wiki · GitHub</a></li>
<li><a href="https://www.anthropic.com/news/model-context-protocol">Introducing the Model Context Protocol \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI coding agents`, `#persistent memory`, `#MCP`, `#developer tools`, `#LLM`

---

<a id="item-13"></a>
## [微信 4.x 数据库解密工具从内存提取密钥](https://github.com/ylytdeng/wechat-decrypt) ⭐️ 8.0/10

一款新的开源工具 wechat-decrypt 能够从正在运行的微信 4.x 进程内存中提取加密密钥，并在 Windows、macOS 和 Linux 上解密所有本地 SQLCipher 4 数据库。它还提供实时消息监听和富媒体解析，最近的更新增加了表情包内联显示、隐藏消息检测和改进的 Web UI。 该工具大幅降低了安全研究人员和取证分析师访问微信加密本地数据的门槛，能够深入调查消息历史记录和用户活动。它还展示了一种针对广泛使用应用的实用内存提取技术，突显了对数百万用户潜在的隐私和安全影响。 该工具通过扫描进程内存中特定模式（格式为 x'<64hex_enc_key><32hex_salt>' 的原始密钥）来工作，然后通过第 1 页的 HMAC 校验确认密钥正确性。它需要管理员/root 权限，支持 Python 3.10+；macOS 还需要 ad-hoc 重签名和 Xcode Command Line Tools。

rss · GitHub Trending - Python · May 12, 14:31

**背景**: 微信 4.x 使用 SQLCipher 4 加密本地数据库，采用 AES-256-CBC 和 HMAC-SHA512，PBKDF2-HMAC-SHA512 密钥派生（256,000 次迭代），页面大小为 4096 字节。加密密钥由微信的 WCDB 封装缓存在进程内存中，因此可以通过内存扫描提取。SQLCipher 是一种广泛使用的 SQLite 扩展，提供透明的全数据库加密。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.zetetic.net/sqlcipher/">SQLCipher - Full Database Encryption for SQLite | Zetetic</a></li>
<li><a href="https://github.com/sqlcipher/sqlcipher">GitHub - sqlcipher/sqlcipher: SQLCipher is a standalone fork ... SQLCipher: AES 256 Bit - SQLite3 Multiple Ciphers sqlcipher/sqlcipher | DeepWiki SQLCipher - Download - Softpedia SQLCipher API - Full Database Encryption PRAGMAs, Functions ... Releases · sqlcipher/sqlcipher - GitHub</a></li>
<li><a href="https://aibit.im/blog/post/wechat-4-x-decryptor-extract-keys-decrypt-dbs">WeChat 4.x Decryptor: Extract Keys & Decrypt DBs | AIBit</a></li>

</ul>
</details>

**社区讨论**: 该项目在 GitHub 上获得了显著关注，拥有 1.9k 星和 1.3k 分支，并设有活跃的 Telegram 群组提供支持。社区讨论可能集中在工具的有效性、跨平台兼容性以及未经授权访问微信数据的潜在伦理问题上。

**标签**: `#security`, `#forensics`, `#reverse engineering`, `#wechat`, `#python`

---

<a id="item-14"></a>
## [VLM 可靠性探针挑战注意力-置信度假设](https://arxiv.org/abs/2605.08200) ⭐️ 8.0/10

研究人员引入了 VLM 可靠性探针（VRP），这是一个机制性分析管道，用于分析三个 VLM 系列（LLaVA-1.5、PaliGemma、Qwen2-VL）中的注意力、隐藏状态和因果回路。他们发现注意力结构对正确性的预测能力几乎为零（R_pb=0.001），这与常见的“注意力集中意味着可靠性”的信念相矛盾。 这项研究挑战了视觉语言模型可解释性中一个普遍存在的直觉，表明注意力图在评估可信度方面具有误导性。这些发现对构建更可靠的 VLM 和设计更好的监控工具具有直接影响，尤其是在高风险应用中。 VRP 揭示了可靠性在计算后期才变得可读：对于三个系列中的两个，单个隐藏状态线性探针在 POPE 上达到了 AUROC>0.95。此外，因果神经元级消融暴露了明显的架构差异：晚期融合的 LLaVA 将可靠性集中在脆弱的晚期瓶颈中，而早期融合的 PaliGemma 和 Qwen2-VL 则广泛分布可靠性。

rss · arXiv - AI · May 12, 04:00

**背景**: 视觉语言模型（VLM）结合视觉和文本信息来回答关于图像的问题。机制性可解释性旨在通过追踪因果回路和分析隐藏状态来理解神经网络的内部计算。注意力-置信度假设认为，当模型的注意力图尖锐地集中在相关图像区域时，模型更可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/itsloganmann/VLM-Reliability-Probe">GitHub - itsloganmann/VLM-Reliability-Probe</a></li>
<li><a href="https://arxiv.org/pdf/2605.08200">Where Reliability Lives in Vision–Language Models: A ...</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#mechanistic interpretability`, `#reliability`, `#attention`, `#causal circuits`

---

<a id="item-15"></a>
## [自动评分标准作为奖励：显式多模态生成准则](https://arxiv.org/abs/2605.08354) ⭐️ 8.0/10

Auto-Rubric as Reward (ARR) 是一个新框架，它将视觉语言模型（VLM）的隐式偏好转化为显式的、针对提示的评分标准用于奖励建模，并引入 Rubric Policy Optimization (RPO) 将这些评分标准蒸馏为稳健的二元奖励，用于多模态生成对齐。 该方法通过将偏好外化为可检查的准则，解决了多模态模型 RLHF 中的关键限制，如奖励黑客和缺乏可解释性，有望在文本到图像生成和图像编辑中实现更可靠、数据高效的 alignment。 ARR 在任何成对比较之前将 VLM 内化的偏好知识外化为针对提示的评分标准，抑制了位置偏差等评估偏差。RPO 随后利用这些评分标准来条件化偏好决策，取代不透明的标量回归并稳定策略梯度。

rss · arXiv - AI · May 12, 04:00

**背景**: 基于人类反馈的强化学习（RLHF）将生成模型与人类偏好对齐，但常将复杂判断简化为标量或成对标签，导致奖励黑客。Rubrics-as-Reward (RaR) 方法尝试使用显式准则，但可扩展地生成可靠评分标准仍有挑战。ARR 在 RaR 基础上，从 VLM 的隐式知识中自动生成评分标准。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2507.17746">[2507.17746] Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains</a></li>
<li><a href="https://arxiv.org/abs/2510.17314">[2510.17314] Auto-Rubric: Learning to Extract Generalizable Criteria for Reward Modeling</a></li>
<li><a href="https://arxiv.org/html/2510.14738">AutoRubric: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning</a></li>

</ul>
</details>

**标签**: `#RLHF`, `#multimodal alignment`, `#reward modeling`, `#generative AI`, `#VLM`

---

<a id="item-16"></a>
## [面向偏好而非语义的嵌入](https://arxiv.org/abs/2605.08360) ⭐️ 8.0/10

一篇新论文正式提出，标准文本嵌入衡量的是语义相似性，而非集体决策中设施选址和公平聚类所需的偏好相似性，并提出了合成训练数据来打破偏好相关信号与语义干扰之间的相关性。 这项工作解决了语义嵌入与基于偏好的决策之间的根本性不匹配，通过实现真正捕捉参与者偏好的嵌入，可能显著改善 AI 驱动的集体决策和公平聚类。 论文形式化了一个不变性问题：文本嵌入模型同时编码偏好相关信号（立场和价值观）和语义干扰（风格和措辞），两者在观测上相关，因此依赖干扰的几何结构可能看起来是偏好正确的，而实际上并非如此。

rss · arXiv - AI · May 12, 04:00

**背景**: 设施选址问题和公平聚类是数学框架，用于找到代表点或划分，使参与者距离最小化。标准文本嵌入（如 BERT 或 GPT）基于语义相似性将文本映射到向量，但在集体决策中，距离应反映偏好一致性而非语义接近性。本文指出，现成的嵌入仅通过相关性捕获粗略的偏好信号，当相关性被打破时就会失效。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08360">[2605.08360] Embeddings for Preferences, Not Semantics</a></li>
<li><a href="https://aidailypost.com/news/new-embeddings-prioritize-preferential-similarity-over-semantics">New embeddings prioritize preferential similarity over...</a></li>

</ul>
</details>

**标签**: `#embeddings`, `#collective decision-making`, `#fair clustering`, `#preference learning`, `#NLP`

---

<a id="item-17"></a>
## [自由能框架区分能力激发与能力创造](https://arxiv.org/abs/2605.08368) ⭐️ 8.0/10

一篇新的 arXiv 论文提出了基于自由能的框架，通过可访问支持的概念，将 LLM 后训练中的能力激发与能力创造区分开来。 这一区分澄清了后训练是仅仅重新加权现有行为，还是扩展了模型可达到的行为空间，对 AI 对齐和训练方法具有重要意义。 论文将可访问支持定义为模型在有限预算下实际能产生的行为集合；在此支持内重新加权是激发，而改变支持则是创造。SFT 和 RL 都被视为用不同外部信号对预训练参考分布进行重新加权。

rss · arXiv - AI · May 12, 04:00

**背景**: 自由能原理最初来自神经科学，认为系统通过最小化变分自由能来维持自身存在。在 LLM 后训练中，争论常将 SFT 视为模仿、RL 视为发现，但本文认为需要基于训练是否改变模型可达到的行为空间进行更细致的区分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08368">[2605.08368] On Distinguishing Capability Elicitation from Capability Creation in Post-Training: A Free-Energy Perspective</a></li>
<li><a href="https://en.wikipedia.org/wiki/Free_energy_principle">Free energy principle - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#post-training`, `#capability elicitation`, `#free-energy`, `#AI alignment`

---

<a id="item-18"></a>
## [MemQ：将 Q 学习与资格迹结合，实现自演化记忆智能体](https://arxiv.org/abs/2605.08374) ⭐️ 8.0/10

MemQ 提出了一种新方法，将 TD(λ)资格迹应用于 LLM 智能体的记忆 Q 值，通过溯源 DAG 反向传播信用，实现自演化记忆。该方法在六个不同基准测试（包括操作系统交互、函数调用和代码生成）中均取得了最先进的结果。 该工作解决了当前记忆系统将每条记忆独立处理的局限，通过依赖链传播信用。它有望显著提升 LLM 智能体在多步骤任务上的表现，推动更自主、更自适应的 AI 智能体发展。 MemQ 将问题形式化为外生上下文 MDP（EC-MDP），其中任务流是外生的，记忆存储是内生的。信用权重按(γλ)^d 随 DAG 深度 d 衰减，用结构接近度替代时间距离，该方法在多步骤任务上提升最大（高达+5.7 个百分点），在单步分类上提升最小（+0.77 个百分点）。

rss · arXiv - AI · May 12, 04:00

**背景**: LLM 智能体中的情景记忆允许它们存储和检索过去的经验，但当前方法独立评估每条记忆，忽略了记忆如何促成未来记忆。TD(λ)资格迹是一种强化学习技术，根据近因和频率为状态分配信用；溯源 DAG 记录了记忆之间的依赖关系。外生上下文 MDP 框架将外部任务流与智能体的内部记忆分离，实现了更规范的信用分配。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuglr.medium.com/eligibility-trace-in-temporal-difference-learning-391aa94ba091">Eligibility trace in Temporal difference learning | by Guilin Zhu | Medium</a></li>
<li><a href="https://arxiv.org/abs/2207.06272">Hindsight Learning for MDPs with Exogenous Inputs Hindsight Learning for MDPs with Exogenous Inputs (PDF) Hindsight Learning for MDPs with Exogenous Inputs Learning a Fast Mixing Exogenous Block MDP using a Single ... Contextual Markov Decision Processes - arXiv.org Learning a Fast Mixing Exogenous Block MDP using a Single ... Learning Efficiently Function Approximation for Contextual MDP</a></li>

</ul>
</details>

**标签**: `#LLM Agents`, `#Reinforcement Learning`, `#Memory Systems`, `#Provenance DAG`, `#Q-Learning`

---

<a id="item-19"></a>
## [SkillLens：面向 LLM 智能体的分层技能复用框架](https://arxiv.org/abs/2605.08386) ⭐️ 8.0/10

SkillLens 提出了一个四层分层技能图（策略、战略、程序、原语）和自适应检索机制，实现了 LLM 智能体的混合粒度技能复用，在 bug 定位上准确率提升最多 6.31 个百分点，在 ALFWorld 上将成功率从 45.00%提高到 51.31%。 这项工作解决了 LLM 智能体技能复用中相关性与成本之间的关键矛盾，有望使它们在复杂、长周期任务中更高效、更适应。分层方法可能影响未来的智能体架构并降低运营成本。 SkillLens 使用度校正随机游走扩展技能种子，并通过验证器决定对每个访问单元是接受、分解、重写还是跳过。理论分析表明，在稀疏不匹配假设下成本为次线性，且验证目标单调改进直至局部最优。

rss · arXiv - AI · May 12, 04:00

**背景**: LLM 智能体通常从扁平库中复用技能，但粗粒度技能可能引入无关上下文，而重写整个技能成本高昂。SkillLens 将技能分层组织，允许细粒度复用，从而降低成本并提高相关性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08386">SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost ...</a></li>
<li><a href="https://aipulselab.tech/news/skilllens-adaptive-multi-granularity-skill-reuse-for-cost-efficient-llm-agents-e9f6c1">SkillLens: Adaptive Multi-Granularity Skill Reuse for Cost ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#skill reuse`, `#hierarchical framework`, `#cost efficiency`, `#graph-based retrieval`

---

<a id="item-20"></a>
## [LLM 通过双重机制进行上下文学习](https://arxiv.org/abs/2605.08405) ⭐️ 8.0/10

一篇新论文通过图随机游走任务以及 PCA、激活修补和引导等技术，提供了因果证据，表明 LLM 在上下文学习中同时使用模式匹配和潜在结构推断。 这项研究澄清了 LLM 可解释性中的一个基本争论，表明上下文学习不仅仅是记忆，还涉及真正的推理，这对模型理解和安全性具有重要意义。 该研究使用了一个包含两种竞争图结构的玩具图随机游走任务，并通过 PCA 发现，在中间混合比例下，两种拓扑结构被编码在正交子空间中，这与纯粹的模式匹配解释相矛盾。

rss · arXiv - AI · May 12, 04:00

**背景**: 上下文学习（ICL）允许 LLM 根据提示中的示例执行任务，而无需更新权重。两种相互竞争的理论解释了 ICL：模式匹配（复制局部转换）和潜在结构推断（构建全局模型）。本文提供了因果证据，表明这两种机制共存。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.stanford.edu/blog/understanding-incontext/">How does in-context learning work? A framework for ...</a></li>
<li><a href="https://arxiv.org/abs/2507.16003">[2507.16003] Learning without training: The implicit dynamics ...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#in-context learning`, `#interpretability`, `#causal inference`

---

<a id="item-21"></a>
## [BaLoRA：贝叶斯低秩自适应提升准确率与不确定性估计](https://arxiv.org/abs/2605.08110) ⭐️ 8.0/10

BaLoRA 将贝叶斯推理扩展到 LoRA，引入了一种输入自适应的贝叶斯参数化方法，仅增加极少的参数和计算量，从而提升了准确率并提供了校准良好的不确定性估计。 这缩小了 LoRA 与全微调之间的准确率差距，同时增加了不确定性量化，使微调后的模型在药物发现或自动驾驶等安全关键应用中更加可靠。 BaLoRA 所基于的自适应噪声注入不仅产生了不确定性估计，还显著提升了自然语言推理和视觉任务的预测准确率；在金属有机框架带隙预测中，BaLoRA 的零样本不确定性估计与模型误差的相关性比训练好的 LoRA 集成模型更强。

rss · arXiv - Machine Learning · May 12, 04:00

**背景**: LoRA（低秩自适应）是一种参数高效的微调方法，它冻结预训练权重并注入可训练的低秩矩阵，从而减少内存和计算量。然而，LoRA 产生点估计，缺乏不确定性量化，限制了其在可靠性关键领域的应用。贝叶斯神经网络通过学习权重的分布来提供概率预测，但通常计算成本高昂。BaLoRA 结合了 LoRA 的高效性和贝叶斯原理，以解决这些局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2106.09685">LoRA: Low-Rank Adaptation of Large Language Models</a></li>
<li><a href="https://arxiv.org/abs/2302.13425">[2302.13425] A Survey on Uncertainty Quantification Methods for Deep Learning</a></li>

</ul>
</details>

**标签**: `#Bayesian methods`, `#Low-Rank Adaptation`, `#fine-tuning`, `#large language models`, `#uncertainty quantification`

---

<a id="item-22"></a>
## [KV 缓存量化方案的统计分析](https://arxiv.org/abs/2605.08114) ⭐️ 8.0/10

本文在公平比特预算下对三种 KV 缓存量化方案（KV、KQV、QKQV）进行了严格的统计分析，揭示了 KQV 在所有预算和分布下在 KL 散度上优于 QKQV，并在几何 K 重建中存在预算依赖的交叉现象。 这项工作提供了关于 K-V 不对称性和预算依赖交叉的新见解，对于优化大语言模型推理效率、在不牺牲质量的情况下减少内存占用至关重要。 论文指出，在 n=4（实际主导预算）时，KQV 在所有指标上获胜，而 QKQV 在 n∈{2,3,5}时几何 K 重建更好。这种交叉归因于 softmax 放大的 Jensen 机制。

rss · arXiv - Machine Learning · May 12, 04:00

**背景**: KV 缓存量化通过压缩自回归解码中使用的键值缓存来减少大语言模型的内存使用。常见技术包括标量量化、Walsh-Hadamard 变换（WHT）和四元数 Johnson-Lindenstrauss（QJL）变换。本文比较了三种方案：标量 MSE 基线（KV）、在 K 上使用 WHT+MSE 并在 V 上使用 WHT+MSE+QJL 的混合方案（KQV），以及全 QJL 方案（QKQV）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2406.03482">[2406.03482] QJL: 1-Bit Quantized JL Transform for KV Cache Quantization with Zero Overhead</a></li>
<li><a href="https://arxiv.org/html/2603.20397v1">KV Cache Optimization Strategies for Scalable and Efficient LLM Inference</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>

</ul>
</details>

**标签**: `#KV cache`, `#quantization`, `#LLM inference`, `#statistical inference`, `#machine learning`

---

<a id="item-23"></a>
## [长文本幻觉检测的合理性检验](https://arxiv.org/abs/2605.08346) ⭐️ 8.0/10

该论文提出了一种受控不变性方法，包含两个预言测试（Force 和 Remove），用于区分幻觉检测方法是在评估推理过程还是利用答案层面的伪影。同时，论文介绍了 TRACT，一种轻量级词汇评分器，通过使用诸如模糊趋势和步骤长度动态等轨迹特征，实现了强鲁棒性。 这项工作揭示了 LLM 评估中的一个关键缺口：许多幻觉检测器可能依赖于答案伪影而非真正的推理评估来取得成功。研究结果表明，核心挑战在于从端点线索中分离出轨迹级信号，这有助于提高思维链推理评估的可靠性。 Force 预言测试在保留推理轨迹的同时，将最终答案替换为真实答案；Remove 预言测试则去除答案声明步骤。TRACT 使用词汇轨迹特征，包括模糊趋势、步骤长度动态和跨响应词汇收敛性，在未扰动的轨迹上保持竞争力或优于现有基线。

rss · arXiv - NLP · May 12, 04:00

**背景**: 大型语言模型（LLM）中的幻觉检测旨在识别生成内容何时在事实上不正确或缺乏依据。近期方法通过分析思维链推理轨迹来检测幻觉，但尚不清楚它们是在评估推理质量还是仅仅利用最终答案的表面模式。所提出的预言测试提供了一种合理性检验，以区分这些因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08346v1">Sanity Checks for Long-Form Hallucination Detection - arXiv.org</a></li>
<li><a href="https://arxiv.org/html/2605.07209">Hallucination Detection via Activations of Open-Weight Proxy Analyzers</a></li>
<li><a href="https://arxiv.org/html/2508.18473">Principled Detection of Hallucinations in Large Language Models via Multiple Testing</a></li>

</ul>
</details>

**标签**: `#hallucination detection`, `#large language models`, `#chain-of-thought`, `#evaluation methodology`

---

<a id="item-24"></a>
## [研究发现语言模型电路并非任务特化](https://arxiv.org/abs/2605.08348) ⭐️ 8.0/10

一篇新论文系统性地测量了语言模型电路在六个任务和七个模型上的一致性和特异性，发现任务内复用率高，但由于跨任务重叠严重，任务特异性低。 这挑战了电路是任务特化的常见假设，对电路能在多大程度上支持对模型行为进行针对性理解和干预提出了疑问。 通过使用边归因修补（edge attribution patching），作者发现消融一个任务的电路对另一个任务性能的损害程度与该任务自身电路相当，表明存在大量重叠。

rss · arXiv - NLP · May 12, 04:00

**背景**: 机制可解释性旨在通过识别负责特定行为的稀疏子图（电路）来逆向工程神经网络。电路框架通常通过测量必要性和充分性来评估电路。本文引入了两个较少研究的属性：一致性（组件在任务内的重复出现）和特异性（对任务的唯一性）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability - Wikipedia</a></li>
<li><a href="https://arxiv.org/abs/2310.10348">[2310.10348] Attribution Patching Outperforms Automated Circuit Discovery</a></li>

</ul>
</details>

**标签**: `#mechanistic interpretability`, `#language models`, `#circuits`, `#interpretability`, `#deep learning`

---

<a id="item-25"></a>
## [冻结塔组合实现高效多模态嵌入](https://arxiv.org/abs/2605.08384) ⭐️ 8.0/10

研究人员推出了 jina-embeddings-v5-omni，这是一对多模态嵌入模型，通过冻结编码器组合将文本、图像、音频和视频编码到统一的语义空间中，仅训练了总权重的 0.35%。 这种方法大幅降低了训练成本，同时保留了文本嵌入的几何结构，使得无需完整模型重训练即可实现高效的多模态检索与分析。 该模型分别使用来自 Qwen3.5 和 Qwen2.5-Omni 的冻结图像和音频编码器，仅训练轻量级连接组件，实现了与更大规模多模态模型相竞争的性能。

rss · arXiv - NLP · May 12, 04:00

**背景**: 多模态嵌入模型旨在将不同类型的数据（文本、图像、音频、视频）表示到共享的向量空间中。传统方法通常需要对大型模型进行完整微调，计算成本高昂。冻结编码器组合是一种参数高效的迁移学习方法，它保持预训练编码器冻结，仅训练小型适配器，从而显著降低训练开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2605.08384v1">jina - embeddings - v 5 - omni : Text-Geometry-Preserving Multimodal...</a></li>
<li><a href="https://www.elastic.co/search-labs/blog/jina-embeddings-v5-omni-all-media-one-index">jina - embeddings - v 5 - omni for text, images, video... - Elasticsearch Labs</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_learning">Multimodal learning - Wikipedia</a></li>

</ul>
</details>

**标签**: `#multimodal embeddings`, `#frozen-encoder composition`, `#VLM architecture`, `#efficient training`, `#AI/ML research`

---

<a id="item-26"></a>
## [基于 LLM 的模型将解释转化为行动计划](https://arxiv.org/abs/2605.08406) ⭐️ 8.0/10

研究人员提出了一种计算模型，利用大型语言模型将自然语言解释转化为类似程序的指导（策略先验和价值地图），然后由规划代理在部分可观测性下执行。该模型根据生成路径的效率和可靠性对解释进行评分，并通过四项预注册实验（涉及 24 张地图上的 1200 条解释）进行了验证。 这项工作弥合了解释生成与不确定性下的规划之间的鸿沟，为评估和生成导航任务中有帮助的解释提供了一种原则性方法。它对需要有效传达指令的 AI 系统（如自主代理或辅助技术）具有重要意义。 该模型使用 LLM 从解释中生成策略先验和价值地图，然后规划器在部分可观测性下执行，并对重新规划进行惩罚。在人类实验中，得分更高的解释被认为更有帮助，并改善了导航性能。

rss · arXiv - NLP · May 12, 04:00

**背景**: 不确定性下的规划是指代理在环境信息不完整时做出决策。策略先验指导考虑哪些动作，而价值地图估计状态的可取性。该模型将这些概念与基于 LLM 的解释生成相结合，以模拟听者如何将语言转化为行动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC12633763/">Between planning and map-building: prioritizing replay when future goals are uncertain - PMC</a></li>
<li><a href="https://www.geeksforgeeks.org/artificial-intelligence/fully-observable-vs-partially-observable-environment-in-ai/">Fully Observable vs. Partially Observable Environment in AI</a></li>

</ul>
</details>

**标签**: `#explanation generation`, `#planning under uncertainty`, `#large language models`, `#cognitive science`, `#AI`

---

<a id="item-27"></a>
## [Sem-ECE：面向开放式问答的新校准评估指标](https://arxiv.org/abs/2605.08432) ⭐️ 8.0/10

研究人员提出了 Sem-ECE，这是一个用于开放式问答的校准评估框架，它通过语义采样将模型输出分组为语义类别，并将得到的频率作为置信度估计。 这填补了 LLM 在真实开放式问答场景中校准评估的关键空白，而开放式问答是现代 LLM 最常见的部署场景，对于在医疗和法律等高风险领域的安全部署至关重要。 Sem-ECE 包含两个估计量：Sem1-ECE（同一样本自一致性）和 Sem2-ECE（留出变体），两者都被证明是渐近无偏的，其中 Sem2 在难题上实现了严格更小的校准误差。

rss · arXiv - NLP · May 12, 04:00

**背景**: 校准衡量模型预测的置信度是否与其实际准确率一致。期望校准误差（ECE）是分类任务的标准指标，但开放式问答缺乏可靠的校准评估方法，因为基于 logit 和口头置信度的方法存在局限性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08432v1">A Semantic-Sampling Framework for Evaluating Calibration in ...</a></li>
<li><a href="https://towardsdatascience.com/expected-calibration-error-ece-a-step-by-step-visual-explanation-with-python-code-c3e9aa12937d/">Expected Calibration Error (ECE): A Step-by-Step Visual Explanation | Towards Data Science</a></li>

</ul>
</details>

**标签**: `#LLM calibration`, `#open-ended QA`, `#AI safety`, `#evaluation framework`

---

<a id="item-28"></a>
## [自描述方法提升视觉语言模型的鲁棒性](https://arxiv.org/abs/2605.08145) ⭐️ 8.0/10

研究人员提出了一种带有“多模态交互门”的自描述工作流，将独特交互转化为冗余交互，在视觉语言模型中将视觉引发的错误减少 38.3%，并将一致性提升 16.8%。 这项工作直接解决了视觉语言模型中的幻觉和鲁棒性关键问题，对于在自动驾驶和医学影像等实际应用中可靠部署至关重要。 该方法放大了多模态冗余交互（视觉与语言之间的共享信息），以补偿受损或模糊的模态，弥补了当前指令数据集通常消除冗余的不足。

rss · arXiv - Computer Vision · May 12, 04:00

**背景**: 视觉语言模型（VLM）结合视觉和文本信息执行图像描述和视觉问答等任务。它们常常出现幻觉（生成虚假细节）并在某一模态受损时缺乏鲁棒性。多模态交互可分为冗余（共享）、独特（独占）和协同（涌现）信息。本文提出放大冗余交互以提高可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2409.07402">[2409.07402] What to align in multimodal contrastive learning?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multimodal_interaction">Multimodal interaction - Wikipedia</a></li>

</ul>
</details>

**标签**: `#vision-language models`, `#multimodal learning`, `#robustness`, `#hallucination`, `#redundancy`

---

<a id="item-29"></a>
## [VT-Bench：首个视觉-表格多模态学习统一基准](https://arxiv.org/abs/2605.08146) ⭐️ 8.0/10

研究人员推出了 VT-Bench，这是首个用于视觉-表格多模态学习的统一基准，汇集了来自 9 个领域的 14 个数据集，包含超过 75.6 万个样本，并评估了 23 个代表性模型。 该基准填补了多模态学习中一个未被充分探索的领域，该领域对医疗和工业等高利害领域至关重要，通过标准化评估推动视觉-表格基础模型的发展。 VT-Bench 涵盖判别性预测和生成式推理任务，评估的模型包括单模态专家、专用视觉-表格模型以及通用视觉语言模型（VLM）。

rss · arXiv - Computer Vision · May 12, 04:00

**背景**: 多模态学习通常结合文本、图像或音频，但视觉-表格数据（图像与结构化表格配对）尽管在医学影像和工业检测中很重要，却研究较少。现有基准多聚焦于视觉-文本任务，缺乏对视觉-表格模型的标准化评估。VT-Bench 通过提供包含多样化数据集和模型评估的统一平台填补了这一空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08146">VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal ...</a></li>

</ul>
</details>

**标签**: `#multi-modal learning`, `#benchmark`, `#visual-tabular`, `#machine learning`, `#healthcare`

---

<a id="item-30"></a>
## [HY-Himmel：通过分层运动编码实现高效长视频理解](https://arxiv.org/abs/2605.08158) ⭐️ 8.0/10

HY-Himmel 提出了一种分层视频-语言框架，通过稀疏锚点 I 帧和轻量级压缩域三流适配器分离语义与运动处理，实现运动编码。 该方法解决了长视频理解中的关键瓶颈——高解码成本、令牌增长和运动感知弱——以更少的令牌实现了更优性能，有望推动更高效的多模态 AI 系统。 在 Video-MME 上，HY-Himmel 比密集的 32 帧基线提升了 2.3 个百分点（从 61.2% 到 63.5%），同时使用的上下文令牌减少了 3.6 倍。

rss · arXiv - Computer Vision · May 12, 04:00

**背景**: 多模态语言模型理解长视频通常需要将所有帧解码为 RGB，计算成本高昂。稀疏关键帧采样降低了成本但丢失了运动信息。HY-Himmel 利用视频编解码器中的压缩域数据（运动矢量、残差）来高效捕获运动，无需完全解码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0925231224001607">Action recognition in compressed domains: A survey</a></li>
<li><a href="https://ieeexplore.ieee.org/document/10262342">Compressed Video Action Recognition With Dual-Stream and Dual ...</a></li>
<li><a href="https://ottverse.com/i-p-b-frames-idr-keyframes-differences-usecases/">I, P, and B-frames – Differences and Use Cases Made Easy</a></li>

</ul>
</details>

**标签**: `#video understanding`, `#multimodal language models`, `#motion encoding`, `#compressed domain`, `#hierarchical framework`

---

<a id="item-31"></a>
## [WATCH 框架实现月度级考古遗址变化检测](https://arxiv.org/abs/2605.08160) ⭐️ 8.0/10

研究人员提出了 WATCH 框架，利用 PlanetScope 卫星影像和三种评分方法（时间嵌入距离、自监督变化检测和弱监督定位），在 2017 年至 2024 年间以月度分辨率检测考古遗址的变化。 这项工作实现了对文化遗产遗址的可扩展自动化监测，解决了考古学中人工检查不切实际的关键需求。该框架在三个月容差内的高召回率（92.5%）使其对遗产保护具有决策意义。 基准测试包括阿富汗的 1,943 个考古遗址，并测试了六个基础模型（CLIP、GeoRSCLIP、SatMAE、Prithvi-EO-2.0、DINOv3、Satlas-Pretrain）。无监督方法（TED、SSCD）始终优于弱监督方法，其中 TED+SatMAE 实现了 55%的精确月度召回率。

rss · arXiv - Computer Vision · May 12, 04:00

**背景**: 基于卫星的变化检测通常依赖于有标签数据的监督学习，而考古遗址的标签数据稀缺。WATCH 结合了无需训练和自监督方法来克服这一限制。PlanetScope 提供 4.7 米/像素分辨率的高频（每日）影像，支持月度镶嵌图。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.planet.com/products/mosaics/">Planet Mosaics : Comprehensive, High-Frequency Mosaics for Analysis</a></li>
<li><a href="https://docs.sentinel-hub.com/api/latest/data/planet/planet-scope/">PlanetScope</a></li>

</ul>
</details>

**标签**: `#remote sensing`, `#change detection`, `#archaeology`, `#machine learning`, `#satellite imagery`

---

<a id="item-32"></a>
## [MULTITEXTEDIT：跨语言图像文本编辑基准](https://arxiv.org/abs/2605.08163) ⭐️ 8.0/10

研究人员推出了 MULTITEXTEDIT 基准，包含 12 种语言、5 个视觉领域和 7 种编辑操作的 3600 个实例，并引入新的语言保真度指标（LSF）来评估图像文本编辑中的跨语言退化。 该基准填补了多语言图像文本编辑评估的关键空白，揭示了所有测试模型都存在跨语言退化，尤其是在阿拉伯语和希伯来语等文字上，这对开发公平的多语言 AI 系统至关重要。 LSF 指标采用两阶段 LVM 协议检测脚本级错误，如缺失变音符号和反向 RTL 顺序，与人类标注者相比达到 0.76 的二次加权 kappa。基准还发现语义正确性与像素级保真度之间存在普遍不匹配。

rss · arXiv - Computer Vision · May 12, 04:00

**背景**: 图像文本编辑是指在保留背景和视觉风格的同时修改图像中的文本。现有基准大多以英语为中心，未能评估不同语言和文字上的性能，导致 AI 系统存在偏见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/nameoffly/MultiTextEdit">GitHub - nameoffly/MultiTextEdit</a></li>
<li><a href="https://arxiv.org/pdf/2605.08163">MULTITEXTEDIT: Benchmarking Cross-Lingual Degradation in Text ...</a></li>

</ul>
</details>

**标签**: `#benchmark`, `#text-in-image editing`, `#multilingual`, `#AI evaluation`, `#computer vision`

---

<a id="item-33"></a>
## [Sinkhorn 处理效应：因果最优传输度量](https://arxiv.org/abs/2605.08485) ⭐️ 8.0/10

该论文提出了 Sinkhorn 处理效应，一种基于熵正则化最优传输的度量，用于量化整个反事实分布之间的差异，并提供了去偏估计量和渐近有效的假设检验方法。 这项工作将因果推断从平均处理效应扩展到分布差异的捕捉，能够更细致地分析处理对整个群体的影响，并提供了严格的统计保证。 Sinkhorn 处理效应被表示为反事实均值嵌入的光滑变换，具有一阶和二阶路径可微性。为解决检验功效对熵正则化参数的依赖，论文还提出了跨正则化参数网格的聚合检验。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 最优传输度量将一个概率分布转换为另一个概率分布的成本。熵正则化最优传输通过添加正则化项提高计算效率。反事实均值嵌入将分布表示为再生核希尔伯特空间中的元素，支持非参数因果推断。Sinkhorn 处理效应结合了这些思想来比较反事实分布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08485">[2605.08485] Sinkhorn Treatment Effects: A Causal Optimal ...</a></li>
<li><a href="https://icml.cc/virtual/2026/poster/65027">ICML Poster Sinkhorn Treatment Effects</a></li>

</ul>
</details>

**标签**: `#causal inference`, `#optimal transport`, `#treatment effects`, `#statistical theory`, `#hypothesis testing`

---

<a id="item-34"></a>
## [平均场理论揭示多分量 ICA 中的相变](https://arxiv.org/abs/2605.08552) ⭐️ 8.0/10

一篇新论文为高维多分量在线 ICA 开发了渐近精确的平均场理论，揭示了由初始化驱动的解耦与竞争学习阶段之间的相变。 这项工作将 ICA 理论扩展到单分量恢复之外，提供了一个统一框架来理解集体学习动态和相行为，可能影响无监督表示学习和高维统计。 该理论为学习方向与真实分量之间的重叠矩阵导出了一个封闭的 ODE 系统，并预测了阶梯现象，其中可恢复分量的数量随学习率离散变化。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 独立分量分析（ICA）是一种将多变量信号分离为加性独立分量的方法，常用于盲源分离。传统的高维 ICA 理论专注于恢复单个分量，但实际应用通常需要同时恢复多个分量，这引入了耦合效应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/pdf/2605.08552">Learnability and Competition in High-Dimensional Multi ...</a></li>

</ul>
</details>

**标签**: `#ICA`, `#high-dimensional statistics`, `#mean-field theory`, `#unsupervised learning`, `#representation learning`

---

<a id="item-35"></a>
## [CONTRA：利用归一化流进行共形预测](https://arxiv.org/abs/2605.08561) ⭐️ 8.0/10

CONTRA 提出了一种方法，利用归一化流定义共形预测的非一致性分数，从而为多维输出生成精确的预测区域。它还通过训练残差的归一化流，扩展以增强任何预测模型。 这解决了共形预测在多维场景中的一个关键限制，传统方法会产生过于保守的区域。它改进了机器学习中的不确定性量化，有利于自动驾驶和医疗诊断等应用。 CONTRA 将潜在空间中的高密度区域映射到输出空间中的精确预测区域，优于超矩形或椭圆形共形区域。其扩展通过在残差上训练简单的归一化流，为任何模型添加可靠的预测区域。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 共形预测是一种无分布方法，能生成具有保证覆盖率的预测集，但由于依赖一维非一致性分数，在处理多维输出时存在困难。归一化流是一种生成模型，通过可逆映射将简单分布转化为复杂分布，实现可处理的密度估计。CONTRA 结合了这些思想，创建了更具表达力的预测区域。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Conformal_prediction">Conformal prediction</a></li>
<li><a href="https://en.wikipedia.org/wiki/Normalizing_flows">Normalizing flows</a></li>
<li><a href="https://arxiv.org/abs/1908.09257">[1908.09257] Normalizing Flows: An Introduction and Review of ... Introduction to Normalizing Flows - Towards Data Science Normalizing Flow Models - GitHub Pages 15 Normalizing Flows – Machine Learning for Mechanical ... Normalizing Flows for Probabilistic Modeling and Inference Normalizing Flows: An Introduction and Review of Current Methods</a></li>

</ul>
</details>

**标签**: `#conformal prediction`, `#normalizing flows`, `#uncertainty quantification`, `#density estimation`, `#machine learning`

---

<a id="item-36"></a>
## [用于去中心化不动点问题的核心-晕分解方法](https://arxiv.org/abs/2605.08681) ⭐️ 8.0/10

研究人员提出了核心-晕分解方法，该方法将写所有权与只读评估上下文分离，从而在去中心化多智能体系统中忠实地实现大规模不动点问题。 这解决了严格分解中固有的结构性偏差，在保持并行性优势的同时实现接近集中式的性能，对去中心化优化和多智能体系统具有潜在影响。 该方法使分解与算子的块依赖结构对齐，论文还刻画了严格分解的 Bellman 闭包条件和逐块偏差下界。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 形如 x* = F(x*) 的不动点问题在优化和控制中很常见。在去中心化设置中，严格分解为每个智能体分配不相交的变量块，但许多算子具有跨块依赖关系，截断后会产生结构性偏差。核心-晕分解允许重叠的只读晕来保留原始算子。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08681">[2605.08681] Core-Halo Decomposition: Decentralizing Large ...</a></li>
<li><a href="https://arxiv.org/pdf/2605.08681">Core-Halo Decomposition: Decentralizing Large-Scale Fixed ...</a></li>

</ul>
</details>

**标签**: `#decentralized optimization`, `#fixed-point problems`, `#multi-agent systems`, `#decomposition methods`

---

<a id="item-37"></a>
## [基于扩散的新方法测量高维模态分离](https://arxiv.org/abs/2605.08777) ⭐️ 8.0/10

该论文提出了一种基于扩散的框架，通过自协方差分析测量高维密度中的模态分离，并提出了两个指标：SSA（平方自相关和）和 DA（主导自相关方向）。 这为量化高维数据中的聚类结构提供了一种原则性方法，对于聚类、生成建模和分子动力学等领域至关重要，而传统方法如 PCA 和熵无法捕捉屏障分隔的聚类。 该方法使用以目标密度为平稳分布的可逆扩散，并从自协方差矩阵中提取 SSA 和 DA；它仅需要样本和得分函数，并通过 Tweedie 恒等式利用预训练的基于得分的模型进行扩展。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 模态分离指的是分布被低密度屏障分隔成聚类的尖锐程度，是高维统计学中的一个关键几何属性。现有的度量如熵和 PCA 捕捉分散性但不捕捉碎片化，而互信息需要已知的混合成分。该论文利用可逆扩散过程的自协方差（与密度的亚稳定性相关）来量化分离。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08777">[2605.08777] Measuring and Decomposing Mode Separation via the...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Reversible_diffusion">Reversible diffusion - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Autocovariance">Autocovariance - Wikipedia</a></li>

</ul>
</details>

**标签**: `#mode separation`, `#diffusion processes`, `#high-dimensional statistics`, `#density estimation`

---

<a id="item-38"></a>
## [通过 Softmax 单位划分证明 Transformer 的逼近能力](https://arxiv.org/abs/2605.08811) ⭐️ 8.0/10

一篇新论文证明，通过 softmax 单位划分的局部到全局构造，一个两块的 Transformer 可以以最优参数效率一致逼近 Hölder 连续函数。 这提供了首个严格的理论框架，表明浅层 Transformer 可以实现接近极小极大最优的泛化，弥合了基于注意力模型的实践与理论之间的差距。 该 Transformer 仅使用两个编码器块和单隐藏层前馈网络，在[0,1]^d 和流形上对α-Hölder 函数实现ε逼近，参数数量为 O(ε^{-d/α})。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: Transformer 是使用注意力机制处理序列数据的深度学习模型。Softmax 函数归一化注意力权重，单位划分是一组和为 1 的函数，实现局部到全局的逼近。Hölder 连续性衡量函数光滑度，指数α在(0,1]之间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Partition_of_unity">Partition of unity - Wikipedia</a></li>

</ul>
</details>

**标签**: `#transformers`, `#approximation theory`, `#deep learning theory`, `#attention mechanism`, `#function approximation`

---

<a id="item-39"></a>
## [无噪声逆优化的紧泛化界](https://arxiv.org/abs/2605.08866) ⭐️ 8.0/10

本文为无噪声逆优化建立了紧的 O(d/T) 高概率泛化界，匹配下界，并表明随机设置实际上是对抗性的。 这些结果显著推进了逆优化的理论基础，将其与赌博机文献联系起来，并提供紧的遗憾保证，影响从专家演示中学习。 这些界对诱导动作集成立，并在唯一性条件下得到加强，匹配最佳臂识别速率；还提出了一种每轮迭代复杂度更低的免参数算法。

rss · arXiv - Data Science & Statistics · May 12, 04:00

**背景**: 逆优化从观察到的上下文-动作数据中推断决策者目标的参数。泛化界量化了学习模型在未见数据上的表现，而最佳臂识别是一个赌博机问题，目标是高效找到最佳动作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2109.03920">[2109.03920] Inverse Optimization: Theory and Applications Inverse Optimization: Theory and Applications | Operations ... Inverse optimization for multi-objective linear programming - PMC Inverse Optimization | Springer Nature Link Inverse Optimization - MOOSE Introduction to inverse optimization - jsaezgallego.com Inverse Optimization: Theory and Applications - PubsOnLine</a></li>
<li><a href="https://en.wikipedia.org/wiki/Best_arm_identification">Best arm identification</a></li>

</ul>
</details>

**标签**: `#inverse optimization`, `#generalization bounds`, `#learning theory`, `#bandit algorithms`

---