# 六个项目的资源导航与核查记录

核查日期：2026-10-24（Asia/Shanghai）。这是对 README 与许可文件的定向核查，不是完整代码审计或教学效果实验。所读文件的 blob SHA 见仓库根目录 `docs/source-audit.json`。本文件的简介独立撰写，不转载原项目正文、单词表、课程、截图或音频。

## 功能地图

| 项目与一手入口 | 本次确认的类型和功能 | 适用卡点 | 如何接入本 Skill | 不据此推断 |
| --- | --- | --- | --- | --- |
| [byoungd/up](https://github.com/byoungd/up) | 当前 README 为《人生进阶指南》，涵盖英语等终身学习主题；英语仍有独立入口 | 不知从何开始 | 按需推荐英语章节与自学资源；Skill 自行给当前任务 | 不能继续把当前仓库描述成仅有英语内容的旧版指南 |
| [Everyone Can Use English](https://github.com/ZuodaoTech/everyone-can-use-english) | 既有《人人都能用英语》book 目录，也介绍 Enjoy 产品 | 想从“学英语”转到实际使用 | 推荐阅读或原站工具；Skill 独立生成使用任务 | 不把书稿等同 Agent Skill，不把产品宣传当效果证据 |
| [Qwerty Learner](https://github.com/RealKai42/qwerty-learner) | 单词记忆、键盘输入练习、发音与默写等功能 | 英文拼写、输入不熟 | 用户可在原工具练输入，再回到新句造句任务 | 打字速度、拼写正确率不能证明会话或综合英语能力 |
| [Earthworm](https://github.com/cuixueshe/earthworm) | README 介绍连词构句；提供应用本地运行文档 | 知道单词但组织句子慢 | 作为构句练习候选；Skill 用自编情境检验迁移 | 没有核验游戏机制全貌，不保证刷题可迁移到真实对话 |
| [技术词发音清单](https://github.com/shimohq/chinese-programmer-wrong-pronunciation) | 技术词、音标、发音链接与提示 | 需要核对技术词读法 | 先查线索，再以可靠词典/项目官方读法交叉核验 | 列表不是唯一标准；地区、词义或品牌可能有多种读法 |
| [Anki](https://github.com/ankitects/anki) | 桌面记忆软件，使用间隔重复 | 学后容易忘，难主动调取 | 用本项目脚本导出自编卡片，再由用户导入 | 不等于整套英语课程，不保证只背卡片就能自由表达 |

这些仓库的主要交付形式是指南、书籍、清单或软件，不应在没有读取具体 SKILL.md 的情况下称为“六个现成 Agent Skill”。本次没有把它们作为依赖安装，也没有把原项目代码合并。

## 选择资源的简单规则

优先让学习者完成一个任务，不要求同时注册或安装六个工具。输入困难时推荐 Qwerty Learner；构句练习不足时考虑 Earthworm；主动回忆不足时考虑 Anki；技术词不确定时查发音清单并核验。想建立自学方向时再推荐指南和书籍。无外部工具也能完成本 Skill 的文字任务与练习。

## 本次许可核查

以下仅描述实际查看的文件与本项目采用的处理方式，不是对仓库内所有资产的权利判断。

| 项目 | 查阅文件与所见 | 本项目处理 |
| --- | --- | --- |
| byoungd/up | [LICENSE.md](https://github.com/byoungd/up/blob/main/LICENSE.md) 明确正文为 CC BY-NC 4.0，代码为 MIT，另有第三方材料例外 | 仅独立简介和外链，不复制或改编其正文/工作表用于付费资料 |
| Everyone Can Use English | 根 [LICENSE](https://github.com/ZuodaoTech/everyone-can-use-english/blob/main/LICENSE) 为 GPLv3 文本；另读 book/README.md，未独立确认每章与媒体授权 | 不作“全书可闭源转售”等推断，不收录书稿 |
| Qwerty Learner | 根 [LICENSE](https://github.com/RealKai42/qwerty-learner/blob/master/LICENSE) 为 GPLv3 文本 | 不复制代码或词库，词库与音频需单独核实 |
| Earthworm | 根 [LICENSE](https://github.com/cuixueshe/earthworm/blob/main/LICENSE) 为 AGPLv3 文本 | 不复制代码、课程或音频 |
| 技术词发音清单 | 根路径 LICENSE、LICENSE.md 本次均返回 404 | 只提供外链与独立简介；不据此断言所有路径都无授权，也不批量复用词表 |
| Anki | 根 [LICENSE](https://github.com/ankitects/anki/blob/main/LICENSE) 写明 AGPLv3 或更高版本及部分资产例外 | 不捆绑软件、logo 或第三方牌组；只按官方导入说明导出自编文本 |

需要再利用具体资产时，应重新核验该资产的许可与来源。仓库公开可访问不等于所有材料都能作为自有内容出售。

## 与本项目的边界

本项目使用“任务表达、分轮反馈、换条件复测、主动回忆”等通用训练设计，例句与模块独立编写。六项目链接用于资源导航，不暗示联合出品、作者背书或官方集成。没有证明本 Skill 在学习效果上优于上述项目；可比较的新增交付是可执行的 Agent 指令与原创场景模板。
