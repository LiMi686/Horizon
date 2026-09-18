---
layout: default
title: "Horizon Summary: 2026-09-18 (ZH)"
date: 2026-09-18
lang: zh
---

> From 110 items, 16 important content pieces were selected

---

1. [Android 17 新增 API 仅限 Pixel，未发布至 AOSP](#item-1) ⭐️ 8.0/10
2. [Cactus Needle 3：8-29MB 模型媲美 DeepSeek V4 Flash](#item-2) ⭐️ 8.0/10
3. [ZCode 被曝静默将用户完整 Git 历史上传至云端](#item-3) ⭐️ 8.0/10
4. [Dan Abramov 用 AI“凭感觉”证明 Conway 猜想](#item-4) ⭐️ 8.0/10
5. [韩国将数据泄露罚款上限提高至营收的 10%](#item-5) ⭐️ 8.0/10
6. [Rust 团队警告维护者遭定向社工攻击](#item-6) ⭐️ 8.0/10
7. [Anthropic 的 Claude Code 登上 GitHub 趋势榜，成为终端智能体编程工具](#item-7) ⭐️ 8.0/10
8. [NSA 的开源逆向工程框架 Ghidra](#item-8) ⭐️ 8.0/10
9. [Colibri：纯 C 引擎从磁盘流式加载前沿 MoE 模型](#item-9) ⭐️ 8.0/10
10. [谷歌研究发布 TimesFM 3.0 时间序列基础模型](#item-10) ⭐️ 8.0/10
11. [首个对话式 LLM 智能体网络搜索端到端研究](#item-11) ⭐️ 8.0/10
12. [AutoTuring 测试 AI 智能体是否真正理解计算机体系结构](#item-12) ⭐️ 8.0/10
13. [MAGS：多智能体框架为 LLM 生成代码提供形式化安全保证](#item-13) ⭐️ 8.0/10
14. [射频卷积神经网络利用无线硬件实现边缘 AI 推理](#item-14) ⭐️ 8.0/10
15. [SonoBase：基于 45.6 万张图像训练的开源超声基础模型](#item-15) ⭐️ 8.0/10
16. [逃过程序性死亡的细胞能重建受损组织](#item-16) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Android 17 新增 API 仅限 Pixel，未发布至 AOSP](https://grapheneos.social/@GrapheneOS/117282080803799576) ⭐️ 8.0/10

GrapheneOS 报告称，Android 17 QPR1 引入了新的应用开发者 API，这些 API 仅在 Pixel 设备上可用，并未发布到 Android 开源项目（AOSP）。这是自 Android 3.x 以来首次出现新增 API 而未同步发布到 AOSP 的情况。 这一变化削弱了 Android 的开放性，可能导致生态系统碎片化，使 GrapheneOS 等替代操作系统更难保持兼容性和安全性。它还引发了人们对 Google 对 AOSP 长期承诺的质疑，并可能影响依赖及时源代码发布的其他 OEM 和开发者。 根据社区讨论，问题可能不在于新 API 本身是 Pixel 独占，而在于每年第一和第三季度的发布补丁是 Pixel 独占的，导致 AOSP 更新延迟。Google 仍向受信任的 OEM 提供每月安全补丁回溯，但公开的 AOSP 源代码滞后。

hackernews · theanonymousone · Sep 18, 19:03 · [社区讨论](https://news.ycombinator.com/item?id=49758736)

**背景**: AOSP 是 Google 维护并发布的 Android 开源代码库；设备制造商和 GrapheneOS 等自定义 ROM 项目都基于它构建。历史上，Google 会将新的 Android 版本及其 API 发布到 AOSP，让社区能够适配。GrapheneOS 是一个专注于安全和隐私的 Android 分支，依赖及时的 AOSP 发布来集成补丁并保持与 Pixel 设备的兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://alternativeto.net/news/2026/9/grapheneos-claims-android-17-qpr1-apis-remain-exclusive-to-pixel-devices/">GrapheneOS claims Android 17 QPR1 APIs remain exclusive to Pixel devices | AlternativeTo</a></li>
<li><a href="https://source.android.com/">Android Open Source Project</a></li>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍批评 Google，用户对 GrapheneOS 面临的障碍表示不满，并指责 Google 后悔 Android 开源。一些人澄清真正的问题是 Pixel 独占的季度补丁，而不仅仅是新 API，另一些人则赞扬 GrapheneOS 并希望它能生存下去。

**标签**: `#Android`, `#AOSP`, `#GrapheneOS`, `#Open Source`, `#Google`

---

<a id="item-2"></a>
## [Cactus Needle 3：8-29MB 模型媲美 DeepSeek V4 Flash](https://cactuscompute.com/needle) ⭐️ 8.0/10

Cactus 发布了 Needle 3 系列超小型自动化模型（8-29MB，2-bit 量化下 25-121M 参数），专注于工具调用和结构化 JSON 输出，在窄任务上达到或超越 DeepSeek V4 Flash。模型采用新颖的 Monarch Hadamard MLP 架构和智能阶梯技术，可在从树莓派 5 到 WebAssembly 的多种平台上运行。 这表明极小的压缩模型能够处理以前需要大得多的模型才能完成的自动化任务，从而在手机、汽车和工业控制器等低功耗设备上实现强大的边缘 AI。这可以显著降低工具调用应用的成本和延迟，同时保持数据本地化。 20 层模型在 2-bit 下于 Mobile Actions 上达到 86.0 分，超过 LFM2.5 1.2B（82.4）和 Qwen3.5 0.8B（76.0）；支持 7 种语言、微调、正则触发器以及校准置信度分数。但设计上不支持聊天，且如社区测试所示，可能在间接或模糊指令上失败。

hackernews · HenryNdubuaku · Sep 18, 00:11 · [社区讨论](https://news.ycombinator.com/item?id=49748553)

**背景**: 小型语言模型旨在通过量化（如 2-bit）和高效架构大幅减小体积，从而在边缘设备上运行。工具调用和结构化 JSON 输出对自动化至关重要，使模型能够触发开灯等操作。Cactus Needle 3 基于此前 Needle 2 的反馈，提升了性能和可用性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49748553">Show HN: Cactus Needle 3: 8-29MB automation models... | Hacker News</a></li>
<li><a href="https://kerneldigest.dev/glosario/dsa/hadamard-mlp">Hadamard MLP — KernelDigest</a></li>
<li><a href="https://github.com/HarryR/z80ai">GitHub - HarryR/z80ai: Z80-μLM is a 2 - bit quantized language model ...</a></li>

</ul>
</details>

**社区讨论**: 社区成员测试了演示，发现对于“打开/关闭所有灯”等直接指令有效，但对“我需要小便”或“太冷了”等间接表达则表现不佳，有时会产生错误操作。一些人指出错误响应的置信度分数较低，建议添加阈值；另一些人则称赞其与语音模型结合后在低功耗实际应用中的潜力。

**标签**: `#small language models`, `#tool calls`, `#structured output`, `#edge AI`, `#model compression`

---

<a id="item-3"></a>
## [ZCode 被曝静默将用户完整 Git 历史上传至云端](https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/) ⭐️ 8.0/10

博客 blog.ferstar.org 上发布的一项取证调查显示，z.ai 旗下的 AI 编程工具 ZCode 会在用户登录状态下，静默地将整个工作区打包——包括完整的 .git 历史、LFS 资源缓存、reflog 以及全局应用配置——加密后上传至阿里云 OSS。该文章通过本地取证与逆向工程还原了完整的上传流程和加密方案，并指出解密密钥仅由服务端持有，用户既无法解密也无法审计被上传的内容。 这对开发者而言是一个严重的隐私与安全问题，因为 Git 历史中往往包含密钥、凭证、专有代码以及本不应离开本机的内部提交信息。此事也引发了对 AI 编程代理更广泛的信任质疑——这类工具通常拥有较宽的文件系统权限，用户很难对其进行审计。 据调查，只要应用处于登录状态，上传就会静默发生，目标为阿里云 OSS 对象存储，且解密密钥仅由服务端持有；文章将该行为与 ZCode 的“代码库索引”功能联系起来，z.ai 随后在官方声明中为此致歉。社区成员还指出同类风险也存在于其他代理工具中，有评论者观察到 GLM 和 DeepSeek 模型“喜欢尝试读取 dotfiles 以及 .gitignore 中列出的任何文件”。

hackernews · csmantle · Sep 18, 06:11 · [社区讨论](https://news.ycombinator.com/item?id=49750694)

**背景**: ZCode 是中国初创公司 z.ai 于 2026 年 7 月推出的免费 AI 编程工具，基于其 GLM 系列模型，定位为 Cursor、Claude Code 和 GitHub Copilot 的低价挑战者。AI 编程代理通常需要读取项目文件才能给出有用的建议，许多工具提供“代码库索引”功能来构建可搜索的仓库表示——通常在本机完成，但有时会涉及云服务。Git 历史是仓库中每一次提交的完整记录，因此上传它可能暴露已删除的文件、旧凭证以及当前工作区中已不可见的敏感提交信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/">Inside ZCode: Silently Uploading Your Entire Git History to the Cloud</a></li>
<li><a href="https://tokenstead.ai/guides/zcode-silent-git-history-upload">ZCode uploads your git history ; Z.ai holds the only key</a></li>
<li><a href="https://venturebeat.com/technology/z-ai-launches-zcode-to-challenge-cursor-claude-code-and-github-copilot-in-ai-coding">Z.ai launches ZCode to challenge Cursor, Claude Code and GitHub Copilot in AI coding | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（243 分、89 条评论）总体持批评和怀疑态度：评论者质疑“假设代理不会访问磁盘上任何内容”是否过于天真，指出自动模式下的权限分类器不过是模型在猜测，并认为当代理绕过沙箱时沙箱就形同虚设。多位用户表示正是这类事件让他们坚持使用 OpenCode 等替代方案，还有评论者称 Windows Defender 反复请求上传 Codex 工作文件进行分析，而他选择阻止。

**标签**: `#privacy`, `#security`, `#AI coding tools`, `#Git`, `#cloud upload`

---

<a id="item-4"></a>
## [Dan Abramov 用 AI“凭感觉”证明 Conway 猜想](https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/) ⭐️ 8.0/10

Dan Abramov 发布了一篇博客文章和 GitHub 仓库（gaearon/conway-refinement），描述了他如何使用大语言模型辅助证明 Conway 猜想——这是 John Conway 关于其“外观数列”的最后一个尚未被证明的猜想。文章包含一个名为“为什么我认为它正确”的部分，解释了 AI 辅助证明背后的推理。 如果该证明成立，将有力地展示大语言模型能够对原创数学研究做出贡献，可能改变数学家解决开放问题的方式以及学术界的贡献认定。这也将“凭感觉编程”（vibe coding）——即不经过完整验证就接受 AI 生成结果——的争论延伸到了形式化证明领域。 该证明发布在一个 GitHub 仓库中，并附有明确论证其正确性的章节，但尚未经过形式化验证或同行评审。作者是一位软件工程师（Redux 的创造者），而非受过专业训练的数学家，其方法依赖于对 AI 生成论证的迭代提示和简化。

hackernews · m-hodges · Sep 18, 14:36 · [社区讨论](https://news.ycombinator.com/item?id=49755024)

**背景**: Conway 猜想涉及“外观数列”（look-and-say sequence），其中每一项描述前一项（例如“1, 11, 21, 1211……”）。John Conway 证明了相邻项之比收敛于一个常数（现称 Conway 常数），并猜想该数列的其他某些性质也成立；这一猜想一直悬而未决。“凭感觉编程”（vibe coding）是 Andrej Karpathy 于 2025 年 2 月创造的术语，指开发者根据结果而非逐行审查来接受 AI 生成代码的编程方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://overreacted.io/how-i-vibed-a-proof-of-conways-conjecture/">How I Vibed a Proof of Conway ’ s Conjecture — overreacted</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dan_Abramov">Dan Abramov</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上印象深刻但持谨慎态度：一位受过专业训练的数学家称赞了这一方向，同时建议进一步简化并检查证明的某些部分是否已在别处出现；另一位评论者将 AI 比作无限猴子定理中的猴子，认为有限数量的大语言模型智能体在足够多的 token 预算下最终能找到所有定理。一位更为怀疑的评论者则认为，如果该证明有效，将对学术界造成冲击，并打破现有的知识等级和奖励体系。

**标签**: `#AI`, `#mathematics`, `#proof`, `#LLM`, `#Conway's conjecture`

---

<a id="item-5"></a>
## [韩国将数据泄露罚款上限提高至营收的 10%](https://www.koreajoongangdaily.com/business/korea-raises-data-breach-fines-to-10-of-revenue/12869899) ⭐️ 8.0/10

韩国修订了《个人信息保护法》（PIPA），将数据泄露的最高罚款从企业总营收的 3%提高至 10%，该修正案于 2026 年 3 月 10 日颁布，并将于 2026 年 9 月 11 日生效。此次修订还引入了对首席执行官在数据保护失职方面的个人问责制。 此举可能为全球更严格的数据保护执法树立先例，推动世界各地的企业将安全投资置于削减成本之上。它可能影响其他国家采用类似的基于营收的罚款，从而重塑企业在数据隐私方面的激励。 罚款仅适用于存在故意或重大过失的情况，一些观察人士认为这一门槛较高，可能限制实际执法。该法律还要求 CEO 承担个人责任，但批评者担心对三星等大型企业集团的执法力度，以及通过空壳公司规避责任的可能性。

hackernews · throw7 · Sep 18, 20:02 · [社区讨论](https://news.ycombinator.com/item?id=49759466)

**背景**: 韩国的《个人信息保护法》（PIPA）是该国主要的数据保护法律，此前将罚款上限设定为营收的 3%。此次修订大幅提高处罚力度以威慑数据泄露，与欧盟《通用数据保护条例》（GDPR）等全球趋势保持一致。该法律将于 2026 年 9 月生效，为企业留出合规时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://databreaches.net/2026/09/10/korea-raises-data-breach-fines-to-10-of-revenue/">Korea raises data breach fines to 10 % of revenue - DataBreaches .Net</a></li>
<li><a href="https://www.techtimes.com/articles/321115/20260720/south-koreas-diplomatic-roster-exposed-zero-day-nearly-ten-months.htm">South Korea 's Diplomatic Roster Exposed by Zero-Day for Nearly Ten...</a></li>
<li><a href="https://news.ycombinator.com/item?id=49759466">Korea raises data breach fines to 10 % of revenue | Hacker News</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎此举，认为这是让企业重视安全的必要步骤，但一些人对执法表示怀疑，指出'故意或重大过失'的高门槛以及政府自身的虚伪（如柏林数据泄露事件）。还有人提到企业通过空壳公司规避责任的策略。

**标签**: `#data-privacy`, `#regulation`, `#security`, `#policy`, `#korea`

---

<a id="item-6"></a>
## [Rust 团队警告维护者遭定向社工攻击](https://simonwillison.net/2026/Sep/17/targeted-attacks-on-rustaceans/) ⭐️ 8.0/10

2026 年 9 月 17 日，Adam Harvey 与 crates 安全团队发布警告称，一场持续进行的攻击活动正针对 rust-lang 成员及热门 crate 的所有者，攻击者以虚假的视频面试或合同机会为诱饵，诱骗目标安装恶意软件或执行剪贴板中的命令。该警告发布前，2026 年 8 月已发生一起已确认的供应链攻击，导致 arrayref 及另外两个相关 crate 被投毒。 这是针对 Rust 供应链中“人”这一环节的活跃定向威胁；由于几乎所有软件都依赖开源，一名维护者被攻陷就可能把恶意代码推送给数百万下游用户。8 月的攻击已波及下载量约 2.45 亿次的 crate，显示出此类攻击活动的真实影响范围。 攻击者以“正面机会”为名安排视频通话，进而诱导目标安装某样东西（例如所谓缺失的音频编解码器）或执行命令，比如把命令放到剪贴板中让目标粘贴运行。在 8 月的事件中，恶意版本 arrayref 0.3.10、internment 0.8.7 和 append-only-vec 0.1.9 引入了一个仿冒名称的构建期依赖 proc-macro1，其构建脚本会在 cargo build 期间下载并运行远程二进制文件；相关 crate 已被移除、账号被锁定，研究人员还指出该事件与朝鲜相关攻击活动存在显著重叠。

rss · Simon Willison · Sep 17, 23:59

**背景**: Rust 的包注册中心 crates.io 托管着可复用的库（即 crate），而 crate 的维护者拥有发布权限，可以向所有依赖它的用户发布新版本。供应链攻击正是滥用这种信任：攻陷维护者的账号或电脑后发布恶意代码，这些代码随后会在下游项目中运行。社会工程学指的是利用心理操纵而非技术漏洞，诱使某人执行操作或泄露信息。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://www.wiz.io/blog/rust-supply-chain-attack-on-arrayref-significant-overlap-with-dprk-campaigns">Rust Supply Chain Attack on arrayref: Significant Overlap with DPRK Campaigns | Wiz Blog</a></li>

</ul>
</details>

**社区讨论**: 文章作者 Simon Willison 认为，任何依赖开源的软件背后都有一张由人组成的网络，而这些人都是潜在的攻击入口；他建议采用“依赖冷却期”（dependency cooldowns），即在新版本发布后先等几天再升级，寄希望于其他人先发现攻击。

**标签**: `#security`, `#supply-chain`, `#rust`, `#open-source`, `#social-engineering`

---

<a id="item-7"></a>
## [Anthropic 的 Claude Code 登上 GitHub 趋势榜，成为终端智能体编程工具](https://github.com/anthropics/claude-code) ⭐️ 8.0/10

Anthropic 的 Claude Code 是一款运行在终端中的智能体编程工具，目前登上了 GitHub 趋势榜。它能够理解代码库，通过自然语言命令自动执行日常任务、解释复杂代码并处理 git 工作流，同时也可在 IDE 中使用，或在 GitHub 上通过 @claude 调用。 Claude Code 是向智能体编程（agentic coding）迈进的重要一步，AI 智能体不再只是补全代码行，而是自主处理多步骤开发任务。其终端优先的设计以及登上 GitHub 趋势榜的表现，说明开发者兴趣浓厚，可能重塑工程师的日常工作流程。 通过 npm 安装的方式现已被弃用；Anthropic 推荐在 macOS/Linux 上使用 curl 安装脚本或 Homebrew cask，在 Windows 上使用 PowerShell 脚本或 WinGet。该仓库还提供插件，可通过自定义命令和智能体扩展功能，同时 Claude Code 会收集代码采纳或拒绝等使用数据以及对话数据。

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**背景**: 智能体编程（agentic coding）是指利用由大语言模型驱动的 AI 智能体，在软件开发生命周期中自主完成从代码生成到调试、测试等任务。Claude Code 是 Anthropic 对这一理念的实现，把 AI 智能体直接放进开发者的终端，使其能够读取项目、运行命令并编辑文件。自然语言的代码库理解意味着开发者可以用日常语言询问不熟悉的代码，而不必手动逐文件追踪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal , IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/Agentic_coding">Agentic coding</a></li>
<li><a href="https://www.datacamp.com/tutorial/claude-code">Claude Code Tutorial: Setup and Refactoring in Practice | DataCamp</a></li>

</ul>
</details>

**标签**: `#AI`, `#developer-tools`, `#agentic-coding`, `#terminal`, `#Anthropic`

---

<a id="item-8"></a>
## [NSA 的开源逆向工程框架 Ghidra](https://github.com/NationalSecurityAgency/ghidra) ⭐️ 8.0/10

Ghidra 是由美国国家安全局（NSA）研究局开发的一款免费、开源的软件逆向工程（SRE）框架，提供反汇编、反编译、图形化和脚本等功能，支持 Windows、macOS 和 Linux 平台。它支持多种处理器指令集和可执行文件格式，并可通过 Java 或 Python 脚本进行扩展。 Ghidra 为 IDA Pro 等商业工具提供了一个强大的免费替代方案，显著降低了安全研究人员、恶意软件分析师和学生进入逆向工程领域的门槛。其开源特性和 NSA 的支持使其成为逆向工程社区广泛采用的标准工具。 运行 Ghidra 需要 JDK 25 64 位版本，其反编译器组件用 C++ 编写，其余部分基于 Java。该项目警告某些版本存在已知安全漏洞，因此用户在使用前应查看安全公告。

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**背景**: 软件逆向工程是分析已编译二进制文件以理解其结构和行为的过程，常用于安全研究、恶意软件分析和漏洞发现。Ghidra 由 NSA 于 2019 年 3 月在 RSA 大会上发布，一个月后在 GitHub 上公开了源代码。它主要用 Java 编写，并包含一个反编译器，可将机器码转换回可读的高级表示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/NationalSecurityAgency/ghidra">GitHub - NationalSecurityAgency/ ghidra : Ghidra is a software reverse...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ghidra_(software)">Ghidra (software)</a></li>

</ul>
</details>

**标签**: `#reverse-engineering`, `#security`, `#NSA`, `#open-source`, `#disassembly`

---

<a id="item-9"></a>
## [Colibri：纯 C 引擎从磁盘流式加载前沿 MoE 模型](https://github.com/JustVugg/colibri) ⭐️ 8.0/10

JustVugg 发布了 Colibri v1.11.0，这是一个纯 C、零依赖的推理引擎，通过从磁盘流式加载路由专家，让 744B 至 2.8T 参数的前沿混合专家（MoE）模型能在消费级硬件上运行。它目前支持九个模型家族，包括 GLM-5.2/5.3（744B）、Kimi K3（2.8T）、DeepSeek V4 Flash（284B）和 Qwen3.6（35B-A3B），每个模型都以单个 C 文件实现，并共用统一的 `coli chat` / `coli serve` / `coli web` 前端。 这种方法大幅降低了运行前沿规模 MoE 模型的硬件门槛，有望让缺乏数据中心 GPU 的研究者和开发者也能使用大模型推理。通过将存储、内存和显存视为统一的推理层级，它指向了一个模型能力不再那么依赖稀缺昂贵硬件的未来。 Colibri 将注意力、共享专家和嵌入等稠密部分常驻内存（约 17B 参数、9.9 GB），同时把 21,504 个路由专家（约 370 GB）全部存放在磁盘上并按需流式加载。该项目明确不承诺速度 SLA，但硬性保证语义：默认策略绝不悄悄改变模型精度或路由语义；演示显示 744B 模型在 6 张 RTX 5090 上达到 4 tok/s、首 token 延迟 1.6 秒。

rss · GitHub Trending - Daily (All) · Sep 18, 23:47

**背景**: 混合专家（MoE）模型将大型网络拆分为许多专门的“专家”子网络，每个输入 token 只激活其中一小部分，因此能以远低于稠密模型的单 token 计算量扩展到极大的参数量。由于任一时刻只需要少数专家，未被激活的专家可以存放在更慢、更便宜的存储上并按需加载——这就是所谓的磁盘流式加载。Colibri 正是利用这种稀疏性，把显存、内存和磁盘视为一个统一的内存层级，其思路与 llama.cpp 普及零依赖量化推理有相似之处。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pasqualepillitteri.it/en/news/15985/disk-streaming-moe-models-laptop">Run 744B MoE models on a laptop with disk streaming, no GPU ...</a></li>
<li><a href="https://ai-beat.github.io/news/2026/07/colibri-moe-disk-streaming/">Streaming 744 Billion Parameters from Disk · AI Beat</a></li>
<li><a href="https://www.aitoolnet.com/JustVugg-colibri">Colibri - Tiny C Engine Runs 744B MoE Model on... - Aitoolnet</a></li>

</ul>
</details>

**标签**: `#MoE`, `#inference`, `#C`, `#edge-computing`, `#LLM`

---

<a id="item-10"></a>
## [谷歌研究发布 TimesFM 3.0 时间序列基础模型](https://github.com/google-research/timesfm) ⭐️ 8.0/10

谷歌研究发布了 TimesFM 3.0，这是其预训练的仅解码器时间序列预测基础模型的新检查点，已在 Hugging Face 上以 google/timesfm-3.0-pytorch 提供。3.0 版本新增了原生多变量预测、灵活的仅过去及过去加未来协变量支持，并声称在 fev-bench、TIME Benchmark 和 GIFT-Eval 上排名第一。 TimesFM 3.0 将基础模型式的零样本预测带入了多变量且协变量丰富的现实问题，可能减少为每个预测任务训练定制模型的需求。它与 BigQuery ML、Google Sheets 和 Vertex Model Garden 的集成表明，谷歌正将时间序列基础模型推向主流企业分析领域。 源代码仍采用 Apache-2.0 许可，2.5 及之前版本的权重也保持 Apache-2.0，但 TimesFM 3.0 预训练权重采用单独的 timesfm-non-commercial-license-v1.0 许可，仅限非商业、非生产用途。较旧的 1.0 和 2.0 检查点归档在 v1 子目录下，可通过 pip install timesfm==1.3.0 加载。

rss · GitHub Trending - Python · Sep 18, 23:47

**背景**: TimesFM（时间序列基础模型）是谷歌研究开发的预训练模型，发表于 ICML 2024，能够对从未见过的时间序列进行预测而无需针对特定任务训练，类似于大语言模型预测下一个词的方式。它采用带输入分块的仅解码器注意力架构，在约 1000 亿个真实世界时间点的大型语料库上预训练。时间序列预测在商业中广泛用于预测库存需求、能源消耗等。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/google-research/timesfm">GitHub - google-research/ timesfm : TimesFM ( Time Series Foundation...</a></li>
<li><a href="https://arxiv.org/abs/2310.10688">[2310.10688] A decoder-only foundation model for time-series forecasting</a></li>
<li><a href="https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/">A decoder-only foundation model for time-series forecasting</a></li>

</ul>
</details>

**标签**: `#time-series`, `#foundation-model`, `#forecasting`, `#google-research`, `#machine-learning`

---

<a id="item-11"></a>
## [首个对话式 LLM 智能体网络搜索端到端研究](https://arxiv.org/abs/2609.19244) ⭐️ 8.0/10

一篇新的 arXiv 论文（2609.19244）首次对 ChatGPT、Claude、Grok 和 DeepSeek 四大主流对话平台的网络搜索行为进行了端到端刻画。该研究结合真实用户交互（in vivo）与基于 API 的受控实验（in vitro），分析了智能体何时决定搜索、如何构造查询、其搜索引擎偏好哪些域名，以及如何将搜索结果转化为有依据的回答。 随着对话式智能体越来越依赖网络搜索来回答问题，理解其搜索决策与依据生成行为对可靠性和归因至关重要。研究发现更频繁的搜索未必带来更好的回答质量，且部分论断依赖未引用的搜索结果，这对未来 AI 智能体和搜索工具的设计具有直接影响。 研究发现，是否调用网络搜索的决策在不同平台和模型间差异显著，且各智能体采用不同的复杂查询策略。平台专属搜索引擎倾向于返回其偏好域名的结果；尽管回答大体基于搜索结果，但部分论断依赖未引用的结果，引发了对归因和可靠性的担忧。

rss · arXiv - AI · Sep 18, 04:00

**背景**: 对话式 LLM 智能体是能够自主决定调用网络搜索等工具来回答用户问题的 AI 系统，这种模式常被称为智能体搜索（agentic search）或检索增强生成（RAG）。in vivo 实验观察真实用户交互，而 in vitro 实验通过受控 API 调用隔离模型行为。本文首次结合两种方法，刻画多个商业平台上完整的搜索生命周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.14253">[2510.14253] Towards Agentic Self-Learning LLMs in Search ... Agentic Retrieval Overview - Azure AI Search | Microsoft Learn Agentic search | OpenSearch Documentation GitHub - YunjiaXi/Awesome-Search-Agent-Papers LLM Agent Benchmarks (September 2026): 26 Agentic Evals ... Best LLMs for Agentic — September 2026 Leaderboard Awesome RL-based Agentic Search Papers - GitHub</a></li>
<li><a href="https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview">Agentic Retrieval Overview - Azure AI Search | Microsoft Learn</a></li>
<li><a href="https://www.firecrawl.dev/glossary/web-search-apis/reduce-hallucinations-search-grounded-llm-responses">How do I reduce hallucinations when using search - grounded LLM ...</a></li>

</ul>
</details>

**标签**: `#LLM agents`, `#web search`, `#conversational AI`, `#agentic search`, `#empirical study`

---

<a id="item-12"></a>
## [AutoTuring 测试 AI 智能体是否真正理解计算机体系结构](https://arxiv.org/abs/2609.19387) ⭐️ 8.0/10

AutoTuring 提出了一项受控实验：同一个 AI 智能体两次优化同一个 15 维加速器设计空间，一次以带模拟器计数器的具名架构旋钮形式呈现，一次以 [0,1] 区间上的匿名变量形式呈现，而评估器、合法空间和可达最优解保持完全相同。在九个内核的 FP16 GEMM 测试集上，架构智能体平均比建模的 H200 高出 5.4%，比其盲测对照高出 12.3%，同时模拟器调用次数减少 70.1%。 该方法能够区分 AI 智能体究竟是在真正推理计算机体系结构，还是仅仅在匿名变量上进行搜索，而这一区别决定了它们的技能能否迁移到下一个架构。它为智能体推理中的“意义”提供了一种干净的度量方式，可能重塑 AI-for-systems 和硬件设计智能体的评估方法。 该论文报告的是初步发现，每个条件仅在单个建模加速器上运行了五到六次；论文还指出，评论者循环（critic loop）能为盲测智能体挽回大部分差距，却对架构智能体毫无帮助，这表明架构知识与结构化批评之间是替代关系而非互补关系。作者明确将比较本身而非加速器视为其贡献。

rss · arXiv - AI · Sep 18, 04:00

**背景**: AI 智能体正越来越多地被用于设计硬件加速器，但设计改进的报告无法解释改进的原因。智能体可能是在对机器进行推理，也可能只是在其从未理解其含义的旋钮上进行有效搜索，而只有第一种情况才能迁移到新架构。现有评估无法区分这两种情况，因为它们改变的是智能体而保持问题框架不变；AutoTuring 则相反，只改变语义框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.19387v1">Do AI Agents Understand Computer Architecture? - arXiv.org</a></li>
<li><a href="https://arxiv.org/pdf/2510.19577">gem5 Co-Pilot: AI Assistant Agent for Architectural Design ...</a></li>
<li><a href="https://arxiv.org/html/2601.01743v1">AI Agent Systems: Architectures, Applications, and Evaluation</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#computer architecture`, `#hardware design`, `#evaluation methodology`, `#AutoML`

---

<a id="item-13"></a>
## [MAGS：多智能体框架为 LLM 生成代码提供形式化安全保证](https://arxiv.org/abs/2609.19391) ⭐️ 8.0/10

研究人员提出了 MAGS，这是一个统一的多智能体框架，通过将 Dafny 作为可验证的中间表示，生成具有形式化安全保证的可执行程序。MAGS 会冻结经人工审核的 API 和安全需求，将 LLM 生成的代码翻译为 Dafny，利用验证器反馈修复违规，并将验证通过的程序编译回可执行代码，在涵盖 100 个 CUDA 内核、100 个终端脚本和 20 个机械臂任务的 220 个示例中实现了 100%的成功率。 随着 LLM 编程智能体以人类难以全面审查的规模生成日益复杂的程序，MAGS 通过提供机器可检查的保证，而非依赖模糊测试或 LLM-as-a-Verifier 等概率性检测方法，填补了一个关键的安全缺口。这种方法可能对 AI 安全和软件工程产生重大影响，使智能体代码生成能够在安全关键领域实现可信部署。 该框架在全部 220 个示例中针对冻结的规范实现了非平凡的安全保证，但独立评估显示，当自动形式化的语义未能完全捕捉目标行为时会出现失败。这一局限性凸显了确保形式化规范准确反映现实需求的持续挑战。

rss · arXiv - AI · Sep 18, 04:00

**背景**: Dafny 是一种可验证的编程语言，原生支持规范记录，并配备静态程序验证器，可持续检查代码是否符合其规范。形式化验证针对指定属性提供机器可检查的保证，但传统上需要大量的人工规范和证明工程。近期研究提出将 Dafny 用作 LLM 代码生成的可验证中间语言，即让 LLM 首先生成可自动验证的 Dafny 代码，然后再编译为目标语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dafny.org/">Dafny</a></li>
<li><a href="https://arxiv.org/abs/2501.06283">[2501.06283] Dafny as Verification-Aware Intermediate ...</a></li>
<li><a href="https://arxiv.org/abs/2607.05391">[2607.05391] LLM-as-a-Verifier: A General-Purpose ...</a></li>

</ul>
</details>

**标签**: `#formal-verification`, `#multi-agent-systems`, `#LLM-code-generation`, `#AI-safety`, `#Dafny`

---

<a id="item-14"></a>
## [射频卷积神经网络利用无线硬件实现边缘 AI 推理](https://arxiv.org/abs/2609.19279) ⭐️ 8.0/10

研究人员提出了射频卷积神经网络（RF-CNN），利用每个无线电台中已有的频率混频器来执行 CNN 推理。他们实验演示了多达 2640 万参数、九层的深度 CNN，在无线信号分类、图像分类和可控图像生成任务上达到了接近全精度的性能。 这种方法可能消除对专用边缘 AI 加速器的需求，因为这类加速器会增加本已受限的智能手机、可穿戴设备和无人机等设备的尺寸、重量、功耗和成本（SWaP-C）。通过利用已部署的无线基础设施，它有望为数十亿联网设备带来高效、最先进的 AI 推理能力。 该系统将多通道卷积映射到频率音调上，由无源混频器在一次通过中执行，权重通过空中传输，模拟硬件与通信共享。能耗降至每次乘累加 0.72 飞焦耳，比附加的数字处理器低两个数量级，边缘设备仅在数据准备和读出上消耗能量。

rss · arXiv - Machine Learning · Sep 18, 04:00

**背景**: 边缘设备通常缺乏运行现代神经网络所需的计算能力，而添加加速器会增加 SWaP-C 限制。频率混频器是无线电台中的标准组件，它在时域上对信号进行乘法运算，这在数学上相当于在频域执行卷积。RF-CNN 利用这一特性，直接在现有通信硬件上运行 CNN 推理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2609.19279">[2609.19279] Radio-Frequency Convolutional Neural Networks</a></li>
<li><a href="https://arxiv.org/html/2609.19279">Radio-Frequency Convolutional Neural Networks</a></li>

</ul>
</details>

**标签**: `#edge-ai`, `#hardware-acceleration`, `#rf-computing`, `#neural-networks`, `#signal-processing`

---

<a id="item-15"></a>
## [SonoBase：基于 45.6 万张图像训练的开源超声基础模型](https://arxiv.org/abs/2609.19230) ⭐️ 8.0/10

研究人员发布了 SonoCorpus——一个包含 456,963 张图像和 1,626,085 个专家标注掩码的开源超声数据集，数据来自 17 个国家、24 个临床应用领域的 53 个公开数据集，并同时发布了在其上预训练的交互式分割基础模型 SonoBase。SonoBase 在涵盖新器官、新设备、新操作者和新地域的 15 个评测数据集上全部优于 SAM2、MedSAM2 和 MedSAM3，并达到与在同一数据上训练的逐数据集专用模型相当的水平。 超声是全球部署最广泛的影像模态，但临床 AI 一直碎片化为狭窄的单任务模型，一旦设备、操作者或解剖部位发生变化就会失效。一个稳健的开源基础模型有望在低中收入国家由训练有限的操作者使用手持探头时，仍能可靠完成射血分数、胎儿头围等临床测量。 基于 SonoBase 分割结果计算的射血分数误差为 6.63%，落在观察者间变异范围内，且在除颤器适应症阈值处的误分类率低于可提示基线（13%对 18–42%）；胎儿头围误差 1.81 毫米、孕龄误差 1.2 天，也均低于观察者间变异。在基线完全失败的测试案例中（占四分之一），SonoBase 在 81%的情况下恢复了可用分割，且仅需五个标注样本即可适应新场景；研究还公开了全部检查点、优化器状态、数据划分索引、去重哈希和入门代码。

rss · arXiv - Computer Vision · Sep 18, 04:00

**背景**: 基础模型是在广泛数据上预训练的大型神经网络，可适配多种下游任务；在医学影像中，通常通过将 SAM2（Segment Anything Model 2）等分割架构适配到临床数据来构建。超声图像因探头类型、操作者手法和患者解剖结构差异极大，域偏移严重，对这类模型尤为困难。此前的 MedSAM2、MedSAM3 等医学变体虽加入了医学数据，但在完全外部的超声数据上仍表现不佳，这正是 SonoBase 试图填补的空白。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/AlfredQin/sonobase">GitHub - AlfredQin/sonobase: SonoBase: interactive ultrasound segmentation foundation model, pretrained on SonoCorpus · GitHub</a></li>
<li><a href="https://arxiv.org/html/2509.11752">A Fully Open and Generalizable Foundation Model for Ultrasound ...</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-3-658-51100-5_8">Foundation Models in Medical Image Segmentation | Springer Nature...</a></li>

</ul>
</details>

**标签**: `#medical-imaging`, `#foundation-models`, `#ultrasound`, `#segmentation`, `#domain-adaptation`

---

<a id="item-16"></a>
## [逃过程序性死亡的细胞能重建受损组织](https://www.sciencedaily.com/releases/2026/09/260917003722.htm) ⭐️ 8.0/10

科学家发现了一类特殊的细胞群体，它们能够启动程序性细胞死亡（凋亡）过程，却能在这一过程中存活下来，随后迅速重建受损组织。这些细胞的后代对后续损伤表现出明显更强的抵抗力，揭示了一种对组织修复和癌症复发都具有双重意义的机制。 这一发现可能重塑再生医学的思路，说明人体或许可以被引导加速愈合，同时也为肿瘤治疗后复发提供了新的解释。它提示，帮助组织修复的同一套“存活并产生抗性”的程序，可能被癌细胞劫持以逃避治疗。 这些细胞在通常被认为不可逆的细胞自杀过程中存活下来，其后代还继承了更强的抗损伤能力。这种双重特性意味着，任何针对这类细胞的疗法都必须在促进组织修复与避免催生耐药癌症之间取得平衡。

rss · ScienceDaily Health · Sep 18, 12:30

**背景**: 凋亡（程序性细胞死亡）是一种受到严格调控的自毁机制，用于清除受损或多余的细胞，通常被认为一旦启动便不可逆转。癌症治疗后的复发往往涉及一小群存活下来并产生耐药性的细胞，这一现象与肿瘤异质性以及 YAP1 等标志物有关。这项发现将这两个领域联系起来，表明凋亡过程中的存活可以产生一种具备修复能力且抗损伤的细胞谱系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sciencealert.com/APOPTOSIS-PROGRAMMED-CELL-DEATH-MECHANISM-TRIGGER-WAVE">Scientists Have Just Measured The 'Speed of Death ' of a Cell And...</a></li>
<li><a href="https://medicalxpress.com/news/2026-05-biomarker-chemotherapy-resistance-relapsed-lung.html">Researchers find biomarker of chemotherapy resistance in relapsed ...</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9558974/">Current Landscape of Therapeutic Resistance in Lung Cancer and...</a></li>

</ul>
</details>

**标签**: `#cell biology`, `#regenerative medicine`, `#cancer research`, `#apoptosis`, `#tissue repair`

---