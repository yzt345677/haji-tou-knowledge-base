#!/bin/bash

# 安装剩余的 Skills
# 由于速率限制，建议逐个安装，每个之间等待 60 秒

CLAWHUB_CMD="node /usr/local/lib/node_modules/clawhub/dist/cli.js"
cd /Users/yzt/.openclaw/workspace

echo "🦞 安装剩余 Skills"
echo "================================"
echo ""

# 剩余 Skills 列表
SKILLS=(
    "youtube-watcher"
    "openai-whisper"
    "copywriting"
    "obsidian"
    "apple-notes"
    "apple-reminders"
    "pdf"
    "docx"
    "xlsx"
    "model-usage"
    "skill-vetter"
)

for skill in "${SKILLS[@]}"; do
    echo "🔧 安装：$skill"
    $CLAWHUB_CMD install "$skill" --force 2>&1
    
    if [ $? -eq 0 ]; then
        echo "✅ $skill 安装成功"
    else
        echo "⚠️  $skill 安装失败（可能速率限制或不存在）"
    fi
    
    echo ""
    echo "⏳ 等待 180 秒避免速率限制..."
    sleep 180
done

echo "================================"
echo "🎉 完成！"
echo "查看已安装：node /usr/local/lib/node_modules/clawhub/dist/cli.js list"
