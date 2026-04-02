#!/bin/bash

# OpenClaw Skills 后台批量安装脚本
# 自动处理速率限制，安装完成后通知用户

CLAWHUB_CMD="node /usr/local/lib/node_modules/clawhub/dist/cli.js"
LOG_FILE="/Users/yzt/.openclaw/workspace/scripts/install-skills.log"

echo "🦞 OpenClaw Skills 后台安装启动" | tee -a "$LOG_FILE"
echo "开始时间：$(date)" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"

# Skills 列表
SKILLS=(
    "multi-search-engine"
    "tavily-search"
    "summarize"
    "skill-creator"
    "skill-vetter"
    "model-usage"
    "pdf"
    "docx"
    "xlsx"
    "obsidian"
    "apple-notes"
    "apple-reminders"
    "github"
    "youtube-watcher"
    "openai-whisper"
    "weather"
    "copywriting"
)

INSTALLED=0
FAILED=0

for skill in "${SKILLS[@]}"; do
    echo "" | tee -a "$LOG_FILE"
    echo "🔧 安装：$skill ($(date))" | tee -a "$LOG_FILE"
    
    # 尝试安装，最多重试 5 次
    for i in {1..5}; do
        if $CLAWHUB_CMD install "$skill" 2>&1 | tee -a "$LOG_FILE"; then
            echo "✅ $skill 安装成功" | tee -a "$LOG_FILE"
            ((INSTALLED++))
            break
        else
            if [ $i -lt 5 ]; then
                echo "⚠️  速率限制，等待 45 秒后重试 ($i/5)" | tee -a "$LOG_FILE"
                sleep 45
            else
                echo "❌ $skill 安装失败（超过最大重试次数）" | tee -a "$LOG_FILE"
                ((FAILED++))
            fi
        fi
    done
    
    # 每个 skill 之间等待
    sleep 5
done

echo "" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"
echo "🎉 安装完成！" | tee -a "$LOG_FILE"
echo "成功：$INSTALLED" | tee -a "$LOG_FILE"
echo "失败：$FAILED" | tee -a "$LOG_FILE"
echo "结束时间：$(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 发送通知
if [ $INSTALLED -gt 0 ]; then
    echo "✅ Skills 安装完成！成功：$INSTALLED, 失败：$FAILED"
fi
