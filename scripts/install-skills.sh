#!/bin/bash

# OpenClaw Skills 批量安装脚本
# 用法：./install-skills.sh

set -e

CLAWHUB_CMD="node /usr/local/lib/node_modules/clawhub/dist/cli.js"

echo "🦞 OpenClaw Skills 批量安装"
echo "================================"
echo ""

# 检查 clawhub
if ! $CLAWHUB_CMD --help &> /dev/null; then
    echo "❌ clawhub 未安装，请先运行：sudo npm install -g clawhub"
    exit 1
fi

echo "✅ clawhub 已安装"
echo ""
echo "📦 开始安装 Skills..."
echo "⚠️  遇到速率限制会自动等待..."
echo ""

# Skills 列表
SKILLS=(
    # 搜索类
    "multi-search-engine"
    "tavily-search"
    "summarize"
    
    # 技能管理
    "skill-creator"
    "skill-vetter"
    "model-usage"
    
    # 文档类
    "pdf"
    "docx"
    "xlsx"
    
    # 知识管理
    "obsidian"
    "apple-notes"
    "apple-reminders"
    
    # 开发工具
    "github"
    
    # 多媒体
    "youtube-watcher"
    "openai-whisper"
    
    # 工具类
    "weather"
    "copywriting"
)

INSTALLED=0
FAILED=0
RETRY_COUNT=0
MAX_RETRIES=5

for skill in "${SKILLS[@]}"; do
    echo "🔧 安装：$skill"
    
    # 尝试安装，遇到速率限制则等待
    while ! $CLAWHUB_CMD install "$skill" 2>&1; do
        echo "⚠️  速率限制，等待 30 秒后重试..."
        sleep 30
        ((RETRY_COUNT++))
        if [ $RETRY_COUNT -ge $MAX_RETRIES ]; then
            echo "❌ $skill 安装失败（超过最大重试次数）"
            ((FAILED++))
            RETRY_COUNT=0
            break
        fi
    done
    
    if [ $RETRY_COUNT -lt $MAX_RETRIES ]; then
        echo "✅ $skill 安装成功"
        ((INSTALLED++))
        RETRY_COUNT=0
    fi
    
    # 每个 skill 之间等待几秒
    sleep 3
done

echo "================================"
echo "🎉 安装完成！"
echo "================================"
echo "成功：$INSTALLED"
echo "失败：$FAILED"
echo ""
echo "查看已安装 skills:"
echo "  openclaw skills"
echo ""
echo "下一步："
echo "  1. 配置 API Keys（如 tavily-search 需要）"
echo "  2. 测试搜索功能"
echo "  3. 恢复内容收集任务"
