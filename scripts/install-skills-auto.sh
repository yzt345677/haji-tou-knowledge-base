#!/bin/bash

# Skills 后台自动安装脚本（增强版）
# 自动处理速率限制，安装完成后记录日志

CLAWHUB_CMD="node /usr/local/lib/node_modules/clawhub/dist/cli.js"
LOG_FILE="/Users/yzt/.openclaw/workspace/scripts/skills-install.log"
cd /Users/yzt/.openclaw/workspace

echo "🦞 Skills 后台自动安装启动" | tee -a "$LOG_FILE"
echo "开始时间：$(date)" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"

# 剩余 Skills 列表
SKILLS=(
    "pdf"
    "docx"
    "xlsx"
    "youtube-watcher"
    "copywriting"
    "obsidian"
    "apple-notes"
    "apple-reminders"
    "model-usage"
    "skill-vetter"
)

INSTALLED=0
FAILED=0

for skill in "${SKILLS[@]}"; do
    echo "" | tee -a "$LOG_FILE"
    echo "🔧 安装：$skill ($(date))" | tee -a "$LOG_FILE"
    
    # 尝试安装，最多重试 10 次（应对速率限制）
    for i in {1..10}; do
        # 检查是否需要 --force（可疑 skill）
        if [[ "$skill" == "pdf" || "$skill" == "docx" || "$skill" == "xlsx" ]]; then
            RESULT=$($CLAWHUB_CMD install "$skill" --force 2>&1)
        else
            RESULT=$($CLAWHUB_CMD install "$skill" 2>&1)
        fi
        
        if echo "$RESULT" | grep -q "OK. Installed"; then
            echo "✅ $skill 安装成功" | tee -a "$LOG_FILE"
            ((INSTALLED++))
            break
        elif echo "$RESULT" | grep -q "Rate limit"; then
            if [ $i -lt 10 ]; then
                WAIT_TIME=$((60 + RANDOM % 60))  # 60-120 秒随机等待
                echo "⚠️  速率限制，等待 ${WAIT_TIME}秒后重试 ($i/10)" | tee -a "$LOG_FILE"
                sleep $WAIT_TIME
            else
                echo "❌ $skill 安装失败（超过最大重试次数）" | tee -a "$LOG_FILE"
                ((FAILED++))
            fi
        else
            echo "❌ $skill 安装失败：$RESULT" | tee -a "$LOG_FILE"
            ((FAILED++))
            break
        fi
    done
    
    # 每个 skill 之间额外等待
    sleep 30
done

echo "" | tee -a "$LOG_FILE"
echo "================================" | tee -a "$LOG_FILE"
echo "🎉 安装完成！" | tee -a "$LOG_FILE"
echo "成功：$INSTALLED" | tee -a "$LOG_FILE"
echo "失败：$FAILED" | tee -a "$LOG_FILE"
echo "结束时间：$(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

# 显示最终列表
echo "已安装 skills:" | tee -a "$LOG_FILE"
$CLAWHUB_CMD list 2>&1 | tee -a "$LOG_FILE"

# 发送通知
if [ $INSTALLED -gt 0 ]; then
    echo "" | tee -a "$LOG_FILE"
    echo "✅ Skills 安装完成！成功：$INSTALLED, 失败：$FAILED" | tee -a "$LOG_FILE"
fi
