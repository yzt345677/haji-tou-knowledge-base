#!/usr/bin/env node

/**
 * OpenClaw 内容收集脚本
 * 每 5 分钟收集感兴趣的内容
 * 
 * 工作模式：
 * - --collect: 触发真实的内容收集（通过 OpenClaw message 发送请求）
 * - --report: 生成汇报摘要
 * - 无参数：默认执行收集
 */

const fs = require('fs');
const { execSync } = require('child_process');
const path = require('path');

// 感兴趣的主题
const TOPICS = [
  'AI 人工智能 最新进展',
  '科技 开源项目',
  'NBA 篮球 比赛',
  '编程 开发工具',
  'macOS iOS 技巧',
  'OpenClaw 自动化',
  '加密货币 区块链',
  '太空 科学探索'
];

// 日志文件路径
const LOG_FILE = path.join(__dirname, 'content-log-2026-03-10.md');

// 随机选择一个主题
function getRandomTopic() {
  return TOPICS[Math.floor(Math.random() * TOPICS.length)];
}

// 获取当前时间
function getTime() {
  const now = new Date();
  return now.toLocaleString('zh-CN', { 
    timeZone: 'Asia/Shanghai',
    hour: '2-digit',
    minute: '2-digit'
  });
}

// 读取现有日志
function readLog() {
  try {
    return fs.readFileSync(LOG_FILE, 'utf8');
  } catch (e) {
    return '';
  }
}

// 写入日志
function writeLog(content) {
  fs.writeFileSync(LOG_FILE, content);
}

// 添加记录
function addEntry(topic, type, summary, source) {
  const log = readLog();
  const time = getTime();
  const newRow = `| ${time} | ${topic} | ${type} | ${summary} | ${source} |\n`;
  
  // 在表格部分插入新行
  const updated = log.replace(
    /(\| 时间 \| 主题 \| 类型 \| 摘要 \| 链接\/来源 \|\n\|------\|------\|------\|------\|-----------\|)/,
    `$1\n${newRow}`
  );
  
  writeLog(updated);
  console.log(`✅ 已记录：${topic}`);
}

// 真实内容收集 - 写入队列文件，由 AI 助手在 heartbeat 时处理
function collectContent() {
  const topic = getRandomTopic();
  const queueFile = path.join(__dirname, 'content-queue.json');
  
  console.log(`🔍 收集任务入队：${topic}`);
  
  // 读取现有队列
  let queue = [];
  try {
    queue = JSON.parse(fs.readFileSync(queueFile, 'utf8'));
  } catch (e) {
    // 文件不存在，创建空队列
  }
  
  // 添加新任务
  queue.push({
    topic: topic,
    timestamp: new Date().toISOString(),
    status: 'pending'
  });
  
  // 写回队列（最多保留 10 个待处理任务）
  queue = queue.slice(-10);
  fs.writeFileSync(queueFile, JSON.stringify(queue, null, 2));
  
  console.log(`✅ 任务已入队 (队列长度：${queue.length})`);
  
  // 同时记录到日志（作为降级备份）
  const types = ['文章', '新闻', '项目', '讨论', '教程'];
  const type = types[Math.floor(Math.random() * types.length)];
  addEntry(topic, type, '待 AI 处理真实搜索', 'queue-pending');
}

// 生成汇报
function generateReport() {
  const log = readLog();
  const lines = log.split('\n');
  
  // 统计记录数
  const entries = lines.filter(l => l.startsWith('|') && !l.includes('时间')).length;
  const time = getTime();
  
  // 更新汇报部分
  const report = `### 第 ${Math.ceil(entries / 6)} 次汇报 (${time})
- 收集次数：${entries}
- 内容条数：${entries}
- 备注：自动收集完成

`;
  
  const updated = log.replace(
    /(### 第 \d+ 次汇报.*?备注：.*?\n\n)/s,
    report
  );
  
  writeLog(updated);
  console.log(`📊 汇报已更新 (${time})`);
  
  return { entries, time };
}

// 主函数
function main() {
  const args = process.argv.slice(2);
  
  if (args.includes('--collect')) {
    collectContent();
  } else if (args.includes('--report')) {
    const report = generateReport();
    console.log(`收集了 ${report.entries} 条内容`);
  } else {
    // 默认执行收集
    collectContent();
  }
}

main();
