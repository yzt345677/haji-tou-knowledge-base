# Skills 安装记录

**日期:** 2026-03-11  
**状态:** ⏳ 等待用户执行  
**来源:** 飞书文档 Skills 推荐清单

---

## 📦 待安装 Skills（19 个）

### 🔎 搜索类（3 个）
- `multi-search-engine` - 聚合 17 个搜索引擎，零配置
- `tavily-search` - AI 优化搜索（需要 API Key）
- `summarize` - URL/PDF/音频/视频摘要

### 🔍 技能管理（3 个）
- `skill-creator` - 创建自定义技能
- `skill-vetter` - 安全审查
- `model-usage` - 追踪 token 消耗

### 📄 文档类（3 个）
- `pdf` - PDF 处理
- `docx` - Word 文档
- `xlsx` - Excel 表格

### 🧠 知识管理（3 个）
- `obsidian` - 本地 Markdown 笔记
- `apple-notes` - Apple 备忘录
- `apple-reminders` - Apple 提醒事项

### 💻 开发工具（1 个）
- `github` - GitHub 集成

### 🎙️ 多媒体（2 个）
- `youtube-watcher` - YouTube 字幕抓取
- `openai-whisper` - 本地语音转文字

### 🛠️ 工具类（2 个）
- `weather` - 天气查询
- `copywriting` - 文案优化

---

## 🚀 安装命令

```bash
cd /Users/yzt/.openclaw/workspace/scripts
./install-skills.sh
```

脚本会自动：
1. 安装 clawhub（如果未安装）
2. 批量安装上述 19 个 skills
3. 显示安装结果

---

## 📋 安装后配置

### 需要 API Key 的 Skills
| Skill | 配置方法 |
|-------|----------|
| tavily-search | `openclaw configure --section web` |

### 零配置的 Skills
- multi-search-engine ✅
- weather ✅
- apple-* ✅
- github（需登录 GitHub）✅

---

## 🎯 优先级

### 立即配置（核心功能）
1. `multi-search-engine` - 免费搜索，替代 Brave
2. `clawhub` - 技能市场入口

### 后续配置
3. 文档类（pdf/docx/xlsx）
4. 知识管理类
5. 多媒体类

---

## 🔗 与 SearXNG 的关系

- 如果 `multi-search-engine` 好用 → 可能不需要 SearXNG
- 如果要更隐私/完全自控 → 继续部署 SearXNG
- 两者可以共存，按需使用

---

*等待用户执行安装*
