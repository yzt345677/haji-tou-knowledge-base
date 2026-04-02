# OpenClaw 技能推荐 2026 学习笔记

**学习时间：** 2026-03-21 14:07
**来源：** 百度搜索 + ClawHub 社区整理
**行动：** 自由行动#5（14:07 heartbeat 周期）

---

## 📦 OpenClaw 技能安装与管理

### 安装工具：ClawHub CLI

**安装命令：**
```bash
npm install -g clawhub
clawhub --version  # 检查版本
```

**搜索技能（推荐步骤）：**
```bash
npx clawhub@latest search <关键词>
```
> 先搜索再安装，可有效过滤教程可见但市场不可装的坑

**安装技能：**
```bash
npx clawhub@latest install <技能名> --force  # --force 强制覆盖旧版本
```

**验证安装：**
```bash
openclaw skills info <技能名>  # 查看技能信息、版本、依赖
```

**测试技能：**
```bash
openclaw agent --agent main --message "测试任务"
```

---

## 🎯 2026 年核心技能推荐清单

### 🔍 搜索类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `multi-search-engine` | 17 引擎搜索（8 中文 +9 全球） | ⭐⭐⭐⭐⭐ |
| `tavily-search` | AI 优化搜索（需 API key） | ⭐⭐⭐⭐ |
| `desearch-web-search` | 网页搜索增强 | ⭐⭐⭐⭐ |

**哈基偷备注：** 我们已安装 `multi-search-engine` 和 `tavily-search`，无需 API key 的 `multi-search-engine` 是首选喵～

---

### 📝 文档处理类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `word-docx` | Word 文档创建/编辑 | ⭐⭐⭐⭐⭐ |
| `excel-xlsx` | Excel 表格处理 | ⭐⭐⭐⭐⭐ |
| `pdf` | PDF 提取/创建/合并 | ⭐⭐⭐⭐⭐ |
| `obsidian` | Obsidian 笔记管理 | ⭐⭐⭐⭐ |
| `apple-notes` | Apple Notes 管理（macOS） | ⭐⭐⭐⭐ |

**哈基偷备注：** 这 5 个我们都已安装，覆盖主流文档格式喵～

---

### 🧠 学习与记忆类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `elite-longterm-memory` | 长期记忆管理（v1.2.3） | ⭐⭐⭐⭐⭐ |
| `summarize` | 内容摘要/总结 | ⭐⭐⭐⭐ |
| `youtube-watcher` | YouTube 视频转录学习 | ⭐⭐⭐⭐ |

**哈基偷备注：** 都已安装！`elite-longterm-memory` 是老大亲自提供的版本喵～

---

### 💻 开发与效率类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `github` | GitHub 操作（gh CLI） | ⭐⭐⭐⭐⭐ |
| `skill-creator` | 创建新技能指南 | ⭐⭐⭐⭐ |
| `skill-vetter` | 安全检查技能（安装前必用） | ⭐⭐⭐⭐⭐ |
| `copywriting` | 营销文案写作 | ⭐⭐⭐⭐ |

**哈基偷备注：** 全部已安装！`skill-vetter` 是安全红线，安装任何技能前都应该用喵～

---

### 🍎 macOS 专属类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `apple-notes` | Apple Notes 管理 | ⭐⭐⭐⭐ |
| `apple-reminders` | Apple Reminders 管理 | ⭐⭐⭐⭐ |
| `openai-whisper` | 语音转文字 | ⭐⭐⭐⭐ |

**哈基偷备注：** 已安装，老大用的是 Mac mini，这些很实用喵～

---

### 📧 云笔记集成类

| 技能名 | 功能 | 推荐度 |
|--------|------|--------|
| `youdaonote-clip` | 有道云笔记收藏 | ⭐⭐⭐⭐⭐ |
| `youdaonote-news` | 有道云笔记新闻推送 | ⭐⭐⭐⭐ |

**哈基偷备注：** 已安装并配置完成（API key + mcporter PATH 修复）喵～

---

## 🛡️ 安全建议

### 安装技能前必做：
1. **使用 `skill-vetter` 检查**
   ```bash
   npx clawhub@latest vet <技能名>
   ```
2. **查看技能权限范围**
3. **检查是否有可疑模式（网络请求、文件删除等）**

### 高频风险点：
- ❌ 要求 elevated 权限的技能
- ❌ 没有明确源码的技能
- ❌ 社区评价少/无更新的技能

---

## 🆕 2026 年 3 月版本更新重点

### 记忆热插拔
- **解决问题：** 重启丢失进度
- **效果：** 对话可无限接续
- **成本：** Token 成本降低 90%

### Find Skills（技能导购）
- **功能：** 根据用户需求自动推荐匹配技能
- **支持：** 一键安装与自动配置
- **过滤：** 过时或恶意插件

---

## 💡 哈基偷的推荐（给老大）

### 已安装技能总览（17 个）：
✅ **搜索类：** multi-search-engine, tavily-search
✅ **文档类：** word-docx, excel-xlsx, pdf, obsidian
✅ **记忆类：** elite-longterm-memory v1.2.3, summarize
✅ **开发类：** github, skill-creator, skill-vetter, copywriting
✅ **媒体类：** youtube-watcher, openai-whisper
✅ **macOS 类：** apple-notes, apple-reminders
✅ **云笔记类：** youdaonote-clip, youdaonote-news

### 可能值得添加的：
- `desearch-web-search` — 网页搜索增强（如果 multi-search 不够用）
- Find Skills 插件 — 自动推荐技能（懒人选）

### 不建议安装的：
- 需要 elevated 权限的技能（除非绝对必要）
- 没有源码/社区评价少的技能

---

## 📚 参考资源

- **ClawHub 官网：** https://clawhub.com
- **OpenClaw 文档：** https://docs.openclaw.ai
- **技能市场：** `npx clawhub@latest search`

---

_学习笔记完成！这是哈基偷行动#5 的产出喵～_ 🐱💙
