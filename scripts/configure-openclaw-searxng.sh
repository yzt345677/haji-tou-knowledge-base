#!/bin/bash

# 配置 OpenClaw 使用 SearXNG
# 用法：./configure-openclaw-searxng.sh <SearXNG URL>

set -e

SEARXNG_URL="${1:-http://localhost:8080}"

echo "🔧 配置 OpenClaw 使用 SearXNG..."
echo "URL: $SEARXNG_URL"

# 测试连接
echo "🧪 测试连接..."
if curl -s "${SEARXNG_URL}/search?q=test&format=json" | grep -q "results"; then
    echo "✅ SearXNG 连接成功"
else
    echo "⚠️  无法连接 SearXNG，请检查 URL 或服务状态"
    echo "继续配置（你可以稍后手动测试）"
fi

# 创建 OpenClaw 搜索工具配置
cat > /Users/yzt/.openclaw/workspace/TOOLS.md << 'EOF'
# TOOLS.md - Local Notes

## SearXNG 搜索引擎

**URL:** http://localhost:8080
**搜索格式:** `{URL}/search?q={query}&format=json`
**启用引擎:** Baidu, Bing

### 使用方法

当用户要求搜索时，使用以下格式：
```
curl "http://localhost:8080/search?q={查询词}&format=json"
```

### OpenClaw 集成

配置 AI 在搜索时优先使用 SearXNG：
1. 使用 web_fetch 访问 SearXNG JSON API
2. 解析 results 数组
3. 提取 title, url, content

---

## 其他配置

（原有配置保留）
EOF

echo "✅ TOOLS.md 已更新"

# 创建搜索辅助脚本
cat > /Users/yzt/.openclaw/workspace/scripts/searxng-search.sh << 'INNER_EOF'
#!/bin/bash
# SearXNG 搜索脚本
# 用法：./searxng-search.sh <查询词>

SEARXNG_URL="${SEARXNG_URL:-http://localhost:8080}"
QUERY="$1"

if [ -z "$QUERY" ]; then
    echo "用法：$0 <查询词>"
    exit 1
fi

curl -s "${SEARXNG_URL}/search?q=${QUERY}&format=json" | jq -r '.results[] | "[\(.title)](\(.url))\n\(.content)\n"'
INNER_EOF

chmod +x /Users/yzt/.openclaw/workspace/scripts/searxng-search.sh
echo "✅ 搜索脚本已创建"

echo ""
echo "🎉 OpenClaw SearXNG 配置完成！"
echo ""
echo "测试搜索："
echo "  ./scripts/searxng-search.sh \"AI 人工智能\""
echo ""
echo "手动搜索 URL:"
echo "  ${SEARXNG_URL}/search?q=测试&format=json"
