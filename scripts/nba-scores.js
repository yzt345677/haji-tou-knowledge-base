#!/usr/bin/env node

/**
 * NBA 比分推送脚本 v3
 * 使用 ESPN API (免费、实时 NBA 数据)
 * https://site.web.api.espn.com/
 */

const https = require('https');

// ESPN API endpoint
const API_BASE = 'https://site.web.api.espn.com/apis/site/v2/sports/basketball/nba';

// 获取日期 (YYYYMMDD 格式)
function getDates() {
  const today = new Date();
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  
  return {
    today: formatDate(today),
    yesterday: formatDate(yesterday),
    todayDisplay: formatDateDisplay(today),
    yesterdayDisplay: formatDateDisplay(yesterday)
  };
}

function formatDate(date) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${year}${month}${day}`;
}

function formatDateDisplay(date) {
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  return `${month}-${day}`;
}

// 获取比赛数据
function getGames(dateStr) {
  return new Promise((resolve, reject) => {
    const url = `${API_BASE}/scoreboard?dates=${dateStr}`;
    
    https.get(url, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          const events = json.events || [];
          resolve(events);
        } catch (e) {
          reject(new Error(`解析失败：${e.message}`));
        }
      });
    }).on('error', reject);
  });
}

// 格式化比赛信息
function formatGame(event) {
  const competition = event.competitions?.[0];
  if (!competition) return null;
  
  const homeTeam = competition.competitors?.find(c => c.homeAway === 'home');
  const awayTeam = competition.competitors?.find(c => c.homeAway === 'away');
  
  if (!homeTeam || !awayTeam) return null;
  
  const homeName = homeTeam.team?.displayName || homeTeam.team?.name || 'Unknown';
  const awayName = awayTeam.team?.displayName || awayTeam.team?.name || 'Unknown';
  const homeScore = homeTeam.score || '-';
  const awayScore = awayTeam.score || '-';
  const status = competition.status?.type?.name || competition.status?.type?.description || 'Unknown';
  const detail = competition.status?.detail || '';
  
  // 状态图标
  let statusIcon = '⏰';
  if (status === 'STATUS_FINAL' || status.includes('Final')) {
    statusIcon = '✅';
  } else if (status === 'STATUS_IN_PROGRESS' || status.includes('In Progress')) {
    statusIcon = '🔴';
  }
  
  return {
    text: `${statusIcon} ${awayName} (${awayScore}) @ ${homeName} (${homeScore})\n${detail}`,
    status: status,
    homeScore: parseInt(homeScore) || 0,
    awayScore: parseInt(awayScore) || 0
  };
}

// 生成飞书消息卡片
function createFeishuCard(games, dates) {
  if (games.length === 0) {
    return {
      msg_type: 'text',
      content: {
        text: `🏀 NBA 比分推送 (${dates.todayDisplay})\n\n今天和昨天都没有 NBA 比赛。\n好好休息，明天继续！🏆`
      }
    };
  }
  
  let gameText = `**📅 最近比赛**\n\n`;
  
  games.forEach((game, index) => {
    if (index > 0) gameText += '\n';
    gameText += game.text;
    if (index < games.length - 1) gameText += '\n';
  });
  
  return {
    msg_type: 'interactive',
    card: {
      config: {
        wide_screen_mode: true
      },
      header: {
        template: 'blue',
        title: {
          tag: 'plain_text',
          content: `🏀 NBA 比分 - ${dates.todayDisplay}`
        }
      },
      elements: [
        {
          tag: 'div',
          text: {
            tag: 'lark_md',
            content: gameText
          }
        },
        {
          tag: 'hr'
        },
        {
          tag: 'note',
          elements: [
            {
              tag: 'plain_text',
              content: `数据来自 ESPN · 更新时间：${new Date().toLocaleString('zh-CN', { timeZone: 'Asia/Shanghai' })}`
            }
          ]
        }
      ]
    }
  };
}

// 发送到飞书
async function sendToFeishu(message) {
  const webhookUrl = process.env.FEISHU_WEBHOOK_URL;
  
  if (!webhookUrl) {
    console.error('错误：请设置 FEISHU_WEBHOOK_URL 环境变量');
    process.exit(1);
  }
  
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(message);
    const url = new URL(webhookUrl);
    
    const options = {
      hostname: url.hostname,
      port: 443,
      path: url.pathname + url.search,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': data.length
      }
    };
    
    const req = https.request(options, (res) => {
      let response = '';
      res.on('data', chunk => response += chunk);
      res.on('end', () => {
        console.log('发送成功:', response);
        resolve(response);
      });
    });
    
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

// 主函数
async function main() {
  console.log('🏀 获取 NBA 比赛数据 (ESPN API)...');
  
  try {
    const dates = getDates();
    console.log(`查询日期：${dates.yesterday}, ${dates.today}`);
    
    // 获取今天和昨天的比赛
    const [todayGames, yesterdayGames] = await Promise.all([
      getGames(dates.today),
      getGames(dates.yesterday)
    ]);
    
    console.log(`今天：${todayGames.length} 场，昨天：${yesterdayGames.length} 场`);
    
    // 合并并格式化比赛
    const allGames = [];
    
    yesterdayGames.forEach(game => {
      const formatted = formatGame(game);
      if (formatted) allGames.push(formatted);
    });
    
    todayGames.forEach(game => {
      const formatted = formatGame(game);
      if (formatted) allGames.push(formatted);
    });
    
    console.log(`总计：${allGames.length} 场比赛`);
    
    // 创建消息
    const message = createFeishuCard(allGames, dates);
    
    // 发送
    await sendToFeishu(message);
    
    console.log('✅ NBA 比分推送完成');
  } catch (error) {
    console.error('❌ 错误:', error.message);
    process.exit(1);
  }
}

main();
