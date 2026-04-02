#!/bin/bash

# SearXNG + OpenClaw 一键部署脚本
# 用法：./searxng-all-in-one.sh

set -e

echo "🦞 SearXNG + OpenClaw 一键部署"
echo "================================"
echo ""

# 步骤 1: 部署 SearXNG
echo "📦 步骤 1/3: 部署 SearXNG"
echo ""
bash /Users/yzt/.openclaw/workspace/scripts/deploy-searxng.sh

echo ""
echo "按回车继续配置内网穿透，或 Ctrl+C 稍后手动配置..."
read

# 步骤 2: 配置内网穿透
echo ""
echo "🌐 步骤 2/3: 配置内网穿透"
echo ""
echo "选择内网穿透方式:"
echo "  1) ngrok (简单，随机域名)"
echo "  2) Cloudflare Tunnel (需要域名)"
echo "  3) 跳过（仅本地使用）"
echo ""
read -p "选择 [1/2/3]: " TUNNEL_CHOICE

case $TUNNEL_CHOICE in
    1)
        echo ""
        echo "启动 ngrok..."
        bash /Users/yzt/.openclaw/workspace/scripts/setup-tunnel.sh
        echo ""
        read -p "输入 ngrok 提供的 HTTPS URL: " SEARXNG_URL
        ;;
    2)
        echo ""
        echo "启动 Cloudflare Tunnel..."
        if ! command -v cloudflared &> /dev/null; then
            echo "安装 cloudflared..."
            brew install cloudflared
        fi
        cloudflared tunnel --url http://localhost:8080 &
        sleep 5
        echo ""
        read -p "输入 Cloudflare 提供的 HTTPS URL: " SEARXNG_URL
        ;;
    3)
        SEARXNG_URL="http://localhost:8080"
        echo "使用本地 URL: $SEARXNG_URL"
        ;;
    *)
        echo "无效选择，使用本地 URL"
        SEARXNG_URL="http://localhost:8080"
        ;;
esac

# 步骤 3: 配置 OpenClaw
echo ""
echo "🔧 步骤 3/3: 配置 OpenClaw"
echo ""
bash /Users/yzt/.openclaw/workspace/scripts/configure-openclaw-searxng.sh "$SEARXNG_URL"

echo ""
echo "================================"
echo "🎉 全部完成！"
echo "================================"
echo ""
echo "SearXNG URL: $SEARXNG_URL"
echo ""
echo "测试搜索："
echo "  ./scripts/searxng-search.sh \"AI 人工智能\""
echo ""
echo "在 OpenClaw 中，告诉我：\"用 SearXNG 搜索 XXX\""
