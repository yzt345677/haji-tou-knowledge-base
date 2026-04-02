#!/bin/bash

# 内网穿透脚本（使用 ngrok）
# 用法：./setup-tunnel.sh

set -e

echo "🌐 开始配置内网穿透..."

# 检查 ngrok
if ! command -v ngrok &> /dev/null; then
    echo "⚠️  ngrok 未安装，尝试自动安装..."
    if command -v brew &> /dev/null; then
        brew install ngrok
    else
        echo "❌ 请先安装 Homebrew 或手动安装 ngrok"
        echo "https://ngrok.com/download"
        exit 1
    fi
fi

echo "✅ ngrok 已安装：$(ngrok --version | head -1)"

# 启动 ngrok tunnel
echo "🔗 启动 ngrok tunnel..."
echo "按 Ctrl+C 停止"
echo ""

# 后台启动 ngrok
ngrok http 8080 --log=stdout &
NGROK_PID=$!

# 等待获取 URL
sleep 5

echo ""
echo "✅ Tunnel 已启动！"
echo "PID: $NGROK_PID"
echo ""
echo "📋 查看 ngrok 状态：http://localhost:4040"
echo "🔍 获取的公网 URL 在上方日志中"
echo ""
echo "复制 ngrok 提供的 https://xxx.ngrok.io 地址，然后运行："
echo "  ./configure-openclaw-searxng.sh <你的 ngrok URL>"
