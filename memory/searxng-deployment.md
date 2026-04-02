# SearXNG 部署记录

**日期:** 2026-03-11  
**状态:** ⏳ 等待用户执行  
**部署方式:** 一键脚本

---

## 📦 已准备的文件

| 文件 | 作用 |
|------|------|
| `scripts/searxng-all-in-one.sh` | 一键部署脚本 |
| `scripts/deploy-searxng.sh` | SearXNG Docker 部署 |
| `scripts/setup-tunnel.sh` | 内网穿透配置（ngrok） |
| `scripts/configure-openclaw-searxng.sh` | OpenClaw 集成配置 |
| `scripts/searxng-search.sh` | 搜索测试脚本 |
| `scripts/README-SEARXNG.md` | 详细文档 |

---

## 🚀 用户回来后执行

```bash
cd /Users/yzt/.openclaw/workspace/scripts
./searxng-all-in-one.sh
```

---

## ⚙️ 配置详情

### SearXNG 配置
- **部署目录:** `/usr/local/searxng-docker`
- **本地端口:** 8080
- **启用引擎:** Baidu, Bing
- **输出格式:** JSON（供 AI 使用）

### OpenClaw 集成
- 使用 `web_fetch` 访问 SearXNG JSON API
- 解析 `results` 数组获取搜索结果
- 替代 Brave Search API（免费）

---

## 📝 待办事项

- [ ] 用户执行一键部署脚本
- [ ] 选择内网穿透方式（ngrok/Cloudflare/本地）
- [ ] 测试搜索功能
- [ ] 更新 TOOLS.md 中的 SearXNG URL
- [ ] 配置 AI 优先使用 SearXNG 搜索

---

## 🎯 预期效果

配置完成后，用户说"搜索 XXX"时：
1. AI 使用 `web_fetch` 访问 SearXNG
2. 获取真实搜索结果
3. 整理后返回给用户
4. 无需 Brave API Key

---

*等待用户执行*
