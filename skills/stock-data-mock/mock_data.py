#!/usr/bin/env python3
"""
stock-data-mock: A 股模拟数据生成器
用于测试 stock-explorer/stock-analyzer/stock-announcements 的输出格式

使用方法:
    uv run python mock_data.py --stock 000975.SZ
    uv run python mock_data.py --stocks 000975.SZ,600988.SS
"""

import argparse
import json
from datetime import datetime, timedelta
import random


def generate_mock_quote(stock: str) -> dict:
    """生成模拟行情数据"""
    # 根据股票代码生成"合理"的模拟数据
    mock_data = {
        "000975.SZ": {
            "name": "银泰黄金",
            "base_price": 18.50,
            "market_cap": 520,  # 亿
            "pe": 25,
            "pb": 3.2,
            "roe": 12.5
        },
        "600988.SS": {
            "name": "赤峰黄金",
            "base_price": 22.30,
            "market_cap": 380,  # 亿
            "pe": 28,
            "pb": 4.1,
            "roe": 15.2
        }
    }
    
    data = mock_data.get(stock, {
        "name": "未知股票",
        "base_price": 10.0,
        "market_cap": 100,
        "pe": 20,
        "pb": 2.5,
        "roe": 10.0
    })
    
    # 添加随机波动
    change_percent = random.uniform(-3, 3)
    price = data["base_price"] * (1 + change_percent / 100)
    
    return {
        "stock": stock,
        "name": data["name"],
        "price": round(price, 2),
        "change": round(price - data["base_price"], 2),
        "change_percent": round(change_percent, 2),
        "open": round(data["base_price"] * 0.99, 2),
        "high": round(price * 1.02, 2),
        "low": round(price * 0.97, 2),
        "volume": random.randint(1000000, 50000000),
        "turnover": round(random.uniform(5, 50), 2),  # 亿
        "market_cap": data["market_cap"],
        "pe_ttm": data["pe"],
        "pb": data["pb"],
        "roe": data["roe"]
    }


def generate_mock_technical(stock: str) -> dict:
    """生成模拟技术指标"""
    quote = generate_mock_quote(stock)
    price = quote["price"]
    
    # 生成"合理"的均线数据
    ma5 = price * random.uniform(0.98, 1.02)
    ma10 = price * random.uniform(0.96, 1.04)
    ma20 = price * random.uniform(0.94, 1.06)
    ma60 = price * random.uniform(0.90, 1.10)
    
    return {
        "stock": stock,
        "ma5": round(ma5, 2),
        "ma10": round(ma10, 2),
        "ma20": round(ma20, 2),
        "ma60": round(ma60, 2),
        "macd": round(random.uniform(-0.5, 0.5), 2),
        "kdj_k": round(random.uniform(20, 80), 2),
        "kdj_d": round(random.uniform(20, 80), 2),
        "rsi": round(random.uniform(30, 70), 2)
    }


def generate_mock_f10(stock: str) -> dict:
    """生成模拟 F10 资料"""
    quote = generate_mock_quote(stock)
    
    return {
        "stock": stock,
        "pe_ttm": quote["pe_ttm"],
        "pb": quote["pb"],
        "ps": round(random.uniform(2, 8), 2),
        "pcf": round(random.uniform(5, 20), 2),
        "roe": quote["roe"],
        "gross_margin": round(random.uniform(30, 60), 2),
        "net_margin": round(random.uniform(10, 30), 2),
        "debt_ratio": round(random.uniform(20, 50), 2),
        "eps": round(quote["price"] / quote["pe_ttm"], 2),
        "bvps": round(quote["price"] / quote["pb"], 2),
        "revenue_growth": round(random.uniform(5, 30), 2),
        "profit_growth": round(random.uniform(10, 40), 2)
    }


def generate_mock_announcements(stock: str, days: int = 7) -> list:
    """生成模拟公告"""
    quote = generate_mock_quote(stock)
    name = quote["name"]
    
    announcements = []
    
    # 生成 1-3 条模拟公告
    num_announcements = random.randint(1, 3)
    announcement_types = [
        ("财报", "季度报告", "业绩说明"),
        ("重大事项", "股东减持", "股份变动"),
        ("经营", "重大合同", "项目中标"),
        ("风险", "股价异动", "风险提示")
    ]
    
    for i in range(num_announcements):
        days_ago = random.randint(1, days)
        ann_date = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
        ann_type, ann_subtype, ann_title = random.choice(announcement_types)
        
        announcements.append({
            "title": f"{name}{ann_title}公告",
            "type": f"{ann_type} - {ann_subtype}",
            "date": ann_date,
            "url": f"http://data.eastmoney.com/notices/mock/{stock}/{i}.html",
            "summary": f"{name}发布{ann_title}公告，具体内容详见公告全文..."
        })
    
    return announcements


def generate_full_report(stock: str) -> dict:
    """生成完整模拟报告"""
    quote = generate_mock_quote(stock)
    technical = generate_mock_technical(stock)
    f10 = generate_mock_f10(stock)
    announcements = generate_mock_announcements(stock)
    
    # 计算评分
    value_score = 18  # PE 25 分，给 7 分；PB 3.2 分，给 7 分；股息 2 分
    growth_score = 20  # 营收 20 分，利润 25 分，机构 5 分
    financial_score = 22  # ROE 8 分，毛利 9 分，负债 5 分
    technical_score = 16  # 趋势 7 分，成交量 5 分，支撑 4 分
    
    total_score = value_score + growth_score + financial_score + technical_score
    
    return {
        "stock": stock,
        "name": quote["name"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "quote": quote,
        "technical": technical,
        "f10": f10,
        "announcements": announcements,
        "scores": {
            "value": value_score,
            "growth": growth_score,
            "financial": financial_score,
            "technical": technical_score,
            "total": total_score
        }
    }


def format_report(data: dict) -> str:
    """格式化输出报告"""
    report = f"\n{'='*70}\n"
    report += f"📈 {data['name']}（{data['stock']}）模拟分析报告\n"
    report += f"生成时间：{data['timestamp']}\n"
    report += f"{'='*70}\n\n"
    
    # 核心数据
    quote = data["quote"]
    report += "## 📊 核心数据（模拟数据）\n"
    report += f"| 指标 | 数值 |\n"
    report += f"|------|------|\n"
    report += f"| 当前价 | ¥{quote['price']:.2f} |\n"
    report += f"| 涨跌幅 | {quote['change_percent']:+.2f}% |\n"
    report += f"| 总市值 | {quote['market_cap']:.2f}亿 |\n"
    report += f"| PE(TTM) | {quote['pe_ttm']} |\n"
    report += f"| PB | {quote['pb']:.2f} |\n"
    report += f"| ROE | {quote['roe']:.1f}% |\n\n"
    
    # 技术指标
    tech = data["technical"]
    report += "## 📈 技术指标（模拟）\n"
    report += f"- MA5:  {tech['ma5']:.2f}\n"
    report += f"- MA10: {tech['ma10']:.2f}\n"
    report += f"- MA20: {tech['ma20']:.2f}\n"
    report += f"- MA60: {tech['ma60']:.2f}\n"
    report += f"- MACD: {tech['macd']:.2f}\n"
    report += f"- KDJ:  K={tech['kdj_k']:.0f}, D={tech['kdj_d']:.0f}\n"
    report += f"- RSI:  {tech['rsi']:.0f}\n\n"
    
    # F10 资料
    f10 = data["f10"]
    report += "## 📋 F10 资料（模拟）\n"
    report += f"- PE(TTM):  {f10['pe_ttm']}\n"
    report += f"- PB:       {f10['pb']:.2f}\n"
    report += f"- ROE:      {f10['roe']:.1f}%\n"
    report += f"- 毛利率：   {f10['gross_margin']:.1f}%\n"
    report += f"- 净利率：   {f10['net_margin']:.1f}%\n"
    report += f"- 负债率：   {f10['debt_ratio']:.1f}%\n"
    report += f"- 营收增速：{f10['revenue_growth']:.1f}%\n"
    report += f"- 利润增速：{f10['profit_growth']:.1f}%\n\n"
    
    # 公告
    report += "## 📢 近期公告（模拟）\n"
    for ann in data["announcements"]:
        report += f"- [{ann['date']}] {ann['title']}\n"
        report += f"  类型：{ann['type']}\n"
    report += "\n"
    
    # 评分
    scores = data["scores"]
    report += "## 🎯 多维评分\n"
    report += f"- **价值评分**: {scores['value']}/25\n"
    report += f"- **成长评分**: {scores['growth']}/25\n"
    report += f"- **财务评分**: {scores['financial']}/25\n"
    report += f"- **技术评分**: {scores['technical']}/25\n"
    report += f"\n### 🏆 综合评分：{scores['total']}/100\n\n"
    
    # 建仓建议
    if scores['total'] >= 80:
        rating, advice = "★★★★★ (5/5)", "强烈买入"
        target_low, target_high = quote['price'] * 1.2, quote['price'] * 1.4
    elif scores['total'] >= 70:
        rating, advice = "★★★★☆ (4/5)", "买入"
        target_low, target_high = quote['price'] * 1.1, quote['price'] * 1.3
    elif scores['total'] >= 60:
        rating, advice = "★★★☆☆ (3/5)", "持有"
        target_low, target_high = quote['price'] * 0.95, quote['price'] * 1.15
    else:
        rating, advice = "★★☆☆☆ (2/5)", "减持"
        target_low, target_high = quote['price'] * 0.8, quote['price'] * 0.9
    
    report += "## 💡 建仓建议\n"
    report += f"- **评级**: {rating}\n"
    report += f"- **建议**: {advice}\n"
    report += f"- **目标价**: ¥{target_low:.2f} - ¥{target_high:.2f}\n"
    report += f"- **止损位**: ¥{quote['price'] * 0.85:.2f}\n\n"
    
    # 风险提示
    report += "## ⚠️ 风险提示\n"
    report += "1. ⚠️ **本报告使用模拟数据，仅供测试格式**\n"
    report += "2. 真实数据需等待东方财富 API 恢复\n"
    report += "3. 股市有风险，投资需谨慎\n"
    report += "4. 不构成投资建议\n\n"
    
    report += f"{'='*70}\n"
    report += "_数据源：模拟数据（测试用）| 分析模型：stock-analyzer v1.0 | 喵～🐱_\n"
    report += f"{'='*70}\n"
    
    return report


def main():
    parser = argparse.ArgumentParser(description="A 股模拟数据生成器")
    parser.add_argument("--stock", type=str, help="股票代码 (如：000975.SZ)")
    parser.add_argument("--stocks", type=str, help="多只股票，逗号分隔")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    
    args = parser.parse_args()
    
    if not args.stock and not args.stocks:
        parser.print_help()
        return
    
    # 解析股票代码
    stocks = []
    if args.stock:
        stocks.append(args.stock)
    if args.stocks:
        stocks.extend(args.stocks.split(","))
    
    # 生成并输出
    for stock in stocks:
        try:
            data = generate_full_report(stock.strip())
            if args.json:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print(format_report(data))
        except Exception as e:
            print(f"❌ 生成 {stock} 失败：{str(e)}")


if __name__ == "__main__":
    main()
