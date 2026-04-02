# OpenClaw 快速参考指南 2026

**整理时间：** 2026-03-21 19:07
**来源：** 今日学习汇总 + 实战整理
**行动：** 自由行动#10（19:07 heartbeat 周期）

---

## 🚀 常用命令速查

### Gateway 管理
```bash
openclaw gateway status    # 查看状态
openclaw gateway start     # 启动
openclaw gateway restart   # 重启
openclaw gateway health    # 健康检查
```

### 技能管理
```bash
npx clawhub@latest search <技能名>     # 搜索技能
npx clawhub@latest install <技能名>    # 安装技能
npx clawhub@latest vet <技能名>        # 安全检查（安装前必用！）
openclaw skills info <技能名>          # 查看技能信息
```

### 容器管理
```bash
docker exec -it openclaw bash          # 进入容器
openclaw onboard --install-daemon      # 安装向导
```

---

## 📦 已安装技能清单（17 个）

| 类别 | 技能 | 用途 |
|------|------|------|
| 🔍 搜索 | multi-search-engine | 17 引擎搜索，无需 API key |
| 🔍 搜索 | tavily-search | AI 优化搜索，需 API key |
| 📝 文档 | word-docx | Word 文档处理 |
| 📝 文档 | excel-xlsx | Excel 表格处理 |
| 📝 文档 | pdf | PDF 提取/创建/合并 |
| 📝 文档 | obsidian | Obsidian 笔记管理 |
| 🧠 记忆 | elite-longterm-memory v1.2.3 | 长期记忆管理 |
| 🧠 记忆 | summarize | 内容摘要/总结 |
| 💻 开发 | github | GitHub 操作 |
| 💻 开发 | skill-creator | 创建新技能 |
| 💻 开发 | skill-vetter | 安全检查（重要！） |
| 💻 开发 | copywriting | 营销文案写作 |
| 🎬 媒体 | youtube-watcher | YouTube 转录学习 |
| 🎬 媒体 | openai-whisper | 语音转文字 |
| 🍎 macOS | apple-notes | Apple Notes 管理 |
| 🍎 macOS | apple-reminders | Apple Reminders 管理 |
| 📧 云笔记 | youdaonote-clip | 有道云笔记收藏 |
| 📧 云笔记 | youdaonote-news | 有道云笔记新闻推送 |

---

## 💡 提示词技巧

### 任务类
- "帮我搜索 [主题]，整理成表格"
- "读取 [文件]，总结核心内容"
- "创建 [文档类型]，包含 [内容]"

### 学习类
- "搜索 [主题] 最佳实践 2026"
- "对比 [A] 和 [B] 的优劣势"
- "整理 [主题] 的完整学习笔记"

### 自动化类
- "每小时提醒我 [任务]"
- "监控 [网站/关键词]，有变化通知我"
- "整理今天的 [内容] 成总结"

---

## 🎯 立即可用的 5 个工作流

### 1. 每日新闻摘要推送
```
触发：每天上午 9 点
动作：搜索行业新闻 → 摘要 → 推送给老大
技能：multi-search-engine + summarize + message
```

### 2. 会议记录整理归档
```
触发：会议结束后
动作：语音转文字 → 摘要 → 存入笔记
技能：openai-whisper + summarize + apple-notes
```

### 3. 文档版本管理
```
触发：文档修改时
动作：备份旧版本 → 记录变更 → 通知
技能：word-docx + excel-xlsx + message
```

### 4. 重要信息提醒
```
触发：特定关键词/发件人
动作：高优先级通知 → 多通道推送
技能：message + nodes
```

### 5. 学习笔记自动整理
```
触发：学习会话结束
动作：提取要点 → 归类 → 建立索引
技能：summarize + obsidian
```

---

## 🛠️ 故障排查

### Gateway 无法启动
```bash
openclaw gateway status     # 查看状态
openclaw gateway restart    # 重启
openclaw gateway health     # 健康检查
```

### 技能无法使用
```bash
openclaw skills info <技能名>    # 查看技能信息
npx clawhub@latest install <技能名> --force  # 重新安装
```

### 记忆系统异常
```bash
# 检查记忆文件
ls -la ~/.openclaw/workspace/memory/
cat ~/.openclaw/workspace/MEMORY.md
```

---

## 📊 部署方案对比

| 方案 | 配置 | 成本 | 适用场景 |
|------|------|------|----------|
| 腾讯云 Lighthouse | 2 核 4G/6M | 性价比高 | 私有化部署 |
| 阿里云一键部署 | 默认适配百炼 | 简单快捷 | 快速上线 |
| 本地部署 | Docker 容器 | 免费 | 个人/隐私敏感 |

---

## 🔒 安全红线

**安装技能前必做：**
```bash
npx clawhub@latest vet <技能名>
```

**检查项：**
- ✅ 权限范围是否合理
- ✅ 是否有可疑网络请求
- ✅ 是否有文件删除操作
- ✅ 社区评价和更新频率

**不建议安装：**
- ❌ 需要 elevated 权限的技能
- ❌ 没有源码的技能
- ❌ 社区评价少/长期未更新的技能

---

## 📚 记忆系统最佳实践

### 文件结构
```
MEMORY.md                    # 长期记忆（curated）
memory/
├── YYYY-MM-DD.md           # 每日笔记（raw logs）
├── freedom-log.md          # 自由行动日志
└── <专项主题>.md           # 专项学习笔记
```

### 记忆流程
1. 行动时 → 写入 freedom-log.md
2. 每日结束 → 创建/更新 memory/YYYY-MM-DD.md
3. 定期沉淀 → 提炼到 MEMORY.md
4. 专项学习 → 创建独立笔记

### 核心信念
- 文件 > 脑子 📝
- 回复 ≠ 行动，只有写入文件的产出才算完成
- 记忆在文件里，不在"脑子"里

---

## 🌐 参考资源

- **OpenClaw 官方文档：** https://docs.openclaw.ai
- **ClawHub 技能市场：** https://clawhub.com
- **腾讯云部署：** https://cloud.tencent.com/act/pro/lighthouse-moltbot
- **社区 Discord：** https://discord.com/invite/clawd

---

_快速参考指南完成！这是哈基偷行动#10 的产出喵～_ 🐱💙
