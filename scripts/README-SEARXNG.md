# SearXNG 部署指南

## 🚀 一键部署（推荐）

你回来后，**只需执行一个命令**：

```bash
cd /Users/yzt/.openclaw/workspace/scripts
./searxng-all-in-one.sh
```

脚本会自动：
1. ✅ 检查并安装依赖
2. ✅ 部署 SearXNG Docker
3. ✅ 配置内网穿透（ngrok/Cloudflare）
4. ✅ 配置 OpenClaw 集成

---

## 📋 分步部署（可选）

如果想手动控制每一步：

### 1. 安装 Docker

**选项 A: Docker Desktop**
```bash
open "https://desktop.docker.com/mac/main/arm64/Docker.dmg"
# 拖动到 Applications，启动
```

**选项 B: Colima（轻量）**
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install colima docker
colima start
```

### 2. 部署 SearXNG
```bash
./deploy-searxng.sh
```

### 3. 配置内网穿透
```bash
./setup-tunnel.sh
# 复制 ngrok 提供的 HTTPS URL
```

### 4. 配置 OpenClaw
```bash
./configure-openclaw-searxng.sh https://你的-url.ngrok.io
```

---

## 🧪 测试

```bash
# 测试搜索
./searxng-search.sh "AI 人工智能"

# 或直接访问
open http://localhost:8080/search?q=SearXNG&format=json
```

---

## 🔧 常用命令

```bash
# 查看 SearXNG 状态
docker compose -C /usr/local/searxng-docker ps

# 查看日志
docker compose -C /usr/local/searxng-docker logs -f

# 重启
docker compose -C /usr/local/searxng-docker restart

# 停止
docker compose -C /usr/local/searxng-docker down
```

---

## 📖 配置说明

### 修改搜索引擎
编辑 `/usr/local/searxng-docker/searxng/settings.yml`
- 行 340 左右：启用/禁用特定引擎
- 已默认启用：Baidu, Bing

### 修改端口
编辑 `/usr/local/searxng-docker/docker-compose.yml`
```yaml
ports:
  - "8080:8080"  # 修改左边的端口
```

---

## 🆘 故障排查

### Docker 无法启动
```bash
# Mac 重启 Docker Desktop
# 或 Colima: colima restart
```

### 无法访问本地端口
OpenClaw 的 web_fetch 不能访问 localhost，必须配置内网穿透。

### ngrok 连接断开
重新运行 `./setup-tunnel.sh`

---

## 📚 参考资料

- SearXNG 官方文档：https://docs.searxng.org/
- SearXNG Docker: https://github.com/searxng/searxng-docker
- 公共实例：https://searx.space/
- 原博客教程：https://www.aldyh.top/cn/Openclaw-Search/
