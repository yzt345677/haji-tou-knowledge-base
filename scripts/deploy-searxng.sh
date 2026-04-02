#!/bin/bash

# SearXNG 一键部署脚本 for OpenClaw
# 用法：./deploy-searxng.sh

set -e

echo "🚀 开始部署 SearXNG..."

# 检查 Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker 未安装"
    echo "请先安装 Docker Desktop: https://desktop.docker.com/mac/main/arm64/Docker.dmg"
    echo "或者安装 Colima:"
    echo "  brew install colima docker"
    echo "  colima start"
    exit 1
fi

echo "✅ Docker 已安装：$(docker --version)"

# 克隆 SearXNG
DEPLOY_DIR="/usr/local/searxng-docker"
if [ -d "$DEPLOY_DIR" ]; then
    echo "⚠️  $DEPLOY_DIR 已存在，跳过克隆"
else
    echo "📦 克隆 SearXNG..."
    sudo git clone https://github.com/searxng/searxng-docker.git "$DEPLOY_DIR"
fi

cd "$DEPLOY_DIR"

# 生成密钥
echo "🔑 生成密钥..."
if grep -q "ultrasecretkey" searxng/settings.yml; then
    sed -i '' "s|ultrasecretkey|$(openssl rand -hex 32)|g" searxng/settings.yml
    echo "✅ 密钥已生成"
else
    echo "⚠️  密钥已存在，跳过"
fi

# 修改配置文件
echo "⚙️  修改 SearXNG 配置..."

# 启用 Baidu 和 Bing 引擎
if grep -q "disabled: true" searxng/settings.yml; then
    # 启用 baidu
    sed -i '' '/- name : baidu/,/disabled: true/{s/disabled: true/disabled: false/}' searxng/settings.yml
    # 启用 bing
    sed -i '' '/- name : bing/,/disabled: true/{s/disabled: true/disabled: false/}' searxng/settings.yml
    echo "✅ 已启用 Baidu 和 Bing 引擎"
fi

# 添加 JSON 格式支持
if ! grep -q "json" searxng/settings.yml; then
    sed -i '' '/^html:/a\\n  - json' searxng/settings.yml
    echo "✅ 已添加 JSON 格式支持"
fi

# 启动 Docker
echo "🐳 启动 SearXNG..."
docker compose up -d

# 等待启动
echo "⏳ 等待服务启动..."
sleep 10

# 检查状态
if docker compose ps | grep -q "Up"; then
    echo "✅ SearXNG 启动成功！"
    echo ""
    echo "📍 本地访问地址：http://localhost:8080"
    echo "🔍 测试搜索：http://localhost:8080/search?q=SearXNG&format=json"
    echo ""
    echo "⚠️  下一步：配置内网穿透（让 OpenClaw 可以访问）"
    echo ""
    echo "选项 A - Cloudflare Tunnel（需要域名）:"
    echo "  brew install cloudflared"
    echo "  cloudflared tunnel --url http://localhost:8080"
    echo ""
    echo "选项 B - ngrok（无需域名）:"
    echo "  brew install ngrok"
    echo "  ngrok http 8080"
    echo ""
else
    echo "❌ SearXNG 启动失败，请检查日志："
    docker compose logs
    exit 1
fi

echo ""
echo "🎉 部署完成！"
