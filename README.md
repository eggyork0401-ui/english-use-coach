# English Use Coach · 英语实用输出教练

**把看得懂的英语，练成能用于邮件、面试与真实沟通的表达。**

面向有基础但输出困难的中文学习者的 Agent Skill。解释用中文，练习用英语；先完成一个具体任务，再通过新的情境检查能否独立表达。也支持编写原创场景学习资料。

这是独立编写的 Skill，不是六个第三方项目的镜像或课程合集；它们作为有出处的资源导航保留。资源核查日期为 2026-10-24。

## 快速体验

将 `skills/english-use-coach/` 完整目录放到支持 SKILL.md 的工具的技能目录，再按工具自身的技能加载方式启用。不同 Agent 的发现与安装方式不同，本仓库不宣称已在所有工具中完成安装测试。

也可以先打开 [SKILL.md](skills/english-use-coach/SKILL.md) 与所需 references，在支持文件读取的对话中明确指定使用它。以下为调用示例：

```text
请用 $english-use-coach 帮我给同事 Alex 写一封英文邮件：
询问演示文稿进展，希望 2026 年 10 月 28 日下午 3 点（新加坡时间）收到。
原因是我要提前检查。先给能发的版本，再指出两处语气选择。
```

```text
请用 $english-use-coach 做一轮英文面试练习。
我没有正式工作经历，可以讲课程项目。每轮只问我一个问题，等我答完再反馈。
```

```text
请用 $english-use-coach 制作“礼貌催进度”学习单元，
包含替换字段、完整示例、语气对比和答案分开的两道练习。
```

无需 GitHub、Anki 或其他六个项目的账号就能使用核心文字功能。Skill 本身不调用模型 API，不需要另外配置 API key；运行它的 Agent 需要自身可用的模型环境。

## 能交付什么

| 模式 | 交付 |
| --- | --- |
| 急用 | 能复制的英文稿、必要字段、少量关键解释 |
| 训练 | 用户先答、针对性纠错、示范、新情境复测 |
| 复习 | 自用表达卡片、可选 Anki 文本导出 |
| 资料生产 | 场景、结构、模板、完整示例、语气对照、练习和答案 |

目前覆盖请求、确认、跟进、汇报、延期、协商、会议、面试及日常口语。只提供文字时不会评价用户实际发音或听力；不承诺固定天数流利或固定分数提升。

## 内容与来源

- [技能入口](skills/english-use-coach/SKILL.md)：模式选择与执行规则。
- [原创场景模板](skills/english-use-coach/references/scenarios.md)：可直接参考的表达。
- [练习与卡片规范](skills/english-use-coach/references/practice.md)：如何训练、复测与导出。
- [资料生产规范](skills/english-use-coach/references/product-design.md)：如何制作可用的原创单元。
- [六项目功能与许可核查](skills/english-use-coach/references/resources.md)：学习资源选择与复用边界。
- [可追溯文件记录](docs/source-audit.json)：所读文件的 blob SHA，不是整个仓库的 commit SHA。
- [完整演示单元](examples/follow-up-unit.md)：买家可理解的交付样例。
- [行为验收场景](evals/behavior-cases.md)：实测时检查 Skill 有没有做到要求。

## Anki 导出（可选）

Python 3.10+，无第三方依赖：

```text
python skills/english-use-coach/scripts/export_anki.py skills/english-use-coach/assets/sample-cards.json my-practice.tsv
```

生成 UTF-8、三列（Front / Back / Tags）的 Anki 导入文本。使用 Basic 笔记类型并检查预览；详见练习规范。脚本不自动连接或导入 Anki，不设置提醒，不生成 .apkg。

本地检查：

```text
python -m unittest discover -s tests -v
```

发布包经过格式与导出脚本检查。真实 Agent 的行为、跨工具兼容性、学习效果和销售转化需要分别测试；行为验收文件列的是验收方案，不代表已通过真实模型评测。

## 发布到自己的 GitHub

项目仓库：[eggyork0401-ui/english-use-coach](https://github.com/eggyork0401-ui/english-use-coach)。可以下载或克隆后使用；复制到自己的账号及后续维护方法见 [发布说明](docs/PUBLISH.md)。

## 许可证与商业资料

本仓库原创内容按 [MIT](LICENSE) 开放，允许依条款商业使用与再分发。第三方项目及其内容不由本仓库重新授权。公开 Skill 适合展示方法与示例；如果计划出售行业资料包或人工反馈服务，可另行制作和交付相应内容，不必把完整付费资料放进公开仓库。公开的 MIT 内容不能同时宣称付费独占。

欢迎提交真实场景、自然表达改进或可复现的问题；请用虚构姓名替换私人信息，不上传公司内部资料。
