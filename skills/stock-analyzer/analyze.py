#!/usr/bin/env python3
"""
stock-analyzer: A 股深度分析工具
生成价值 + 技术 + 成长 + 财务多维评分报告

使用方法:
    uv run python analyze.py --stock 600519.SS
    uv run python analyze.py --stocks 600519.SS,300750.SZ
"""

import argparse
import json
import sys
import time
from datetime import datetime
from typing import Optional

# 导入 stock-explorer 的函数
sys.path.insert(0, '/Users/yzt/.openclaw/workspace-stock/skills/stock-explorer')
from quote import get_stock_info


# ============= 重试装饰器 =============

def retry(max_attempts=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if i == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator


# ============= 评分函数 =============

def score_value(quote: dict, f10: dict) -> tuple[int, dict]:
    """价值评分（25 分）- 基于 PE/PB 计算"""
    score = 0
    details = {}
    
    # PE 评分（10 分）- 越低越好
    pe = safe_float(f10.get('pe_ttm'), 0)
    if pe > 0:
        if pe < 15:
            pe_score = 10
        elif pe < 25:
            pe_score = 7
        elif pe < 35:
            pe_score = 4
        else:
            pe_score = 2
    else:
        pe_score = 5  # 无数据给中等
    score += pe_score
    details['pe_score'] = pe_score
    
    # PB 评分（10 分）- 越低越好
    pb = safe_float(f10.get('pb'), 0)
    if pb > 0:
        if pb < 2:
            pb_score = 10
        elif pb < 4:
            pb_score = 7
        elif pb < 6:
            pb_score = 4
        else:
            pb_score = 2
    else:
        pb_score = 5
    score += pb_score
    details['pb_score'] = pb_score
    
    # 市值评分（5 分）- 适中最好
    market_cap = safe_float(f10.get('market_cap'), 0)
    if market_cap > 0:
        if 100 < market_cap < 1000:  # 中型市值
            cap_score = 5
        elif market_cap >= 1000:  # 大型市值
            cap_score = 4
        else:  # 小型市值
            cap_score = 3
    else:
        cap_score = 3
    score += cap_score
    details['cap_score'] = cap_score
    
    return score, details


def score_growth(quote: dict, f10: dict) -> tuple[int, dict]:
    """成长评分（25 分）"""
    details = {'revenue_score': 5, 'profit_score': 5, 'analyst_score': 2}
    return 12, details  # 默认平均分


def score_financial(quote: dict, f10: dict) -> tuple[int, dict]:
    """财务评分（25 分）- 基于 ROE/毛利率/负债率"""
    score = 0
    details = {}
    
    # ROE 评分（10 分）- 越高越好
    roe = safe_float(f10.get('roe'), 0)
    if roe > 0:
        if roe > 20:
            roe_score = 10
        elif roe > 15:
            roe_score = 8
        elif roe > 10:
            roe_score = 6
        elif roe > 5:
            roe_score = 4
        else:
            roe_score = 2
    else:
        roe_score = 5
    score += roe_score
    details['roe_score'] = roe_score
    
    # 毛利率评分（10 分）- 越高越好
    gross_margin = safe_float(f10.get('gross_margin'), 0)
    if gross_margin > 0:
        if gross_margin > 50:
            gm_score = 10
        elif gross_margin > 30:
            gm_score = 7
        elif gross_margin > 20:
            gm_score = 5
        else:
            gm_score = 3
    else:
        gm_score = 5
    score += gm_score
    details['gross_margin_score'] = gm_score
    
    # 负债率评分（5 分）- 越低越好
    debt_ratio = safe_float(f10.get('debt_ratio'), 0)
    if debt_ratio > 0:
        if debt_ratio < 30:
            debt_score = 5
        elif debt_ratio < 50:
            debt_score = 4
        elif debt_ratio < 70:
            debt_score = 2
        else:
            debt_score = 1
    else:
        debt_score = 3
    score += debt_score
    details['debt_score'] = debt_score
    
    return score, details


def score_technical(quote: dict, technical: dict) -> tuple[int, dict]:
    """技术评分（25 分）"""
    details = {'trend_score': 5, 'volume_score': 5, 'support_score': 2}
    return 12, details  # 默认平均分


# ============= 分析报告生成 =============

def generate_rating(total_score: int) -> tuple[str, str]:
    """根据总分生成评级"""
    if total_score >= 80:
        return "★★★★★ (5/5)", "强烈买入"
    elif total_score >= 70:
        return "★★★★☆ (4/5)", "买入"
    elif total_score >= 60:
        return "★★★☆☆ (3/5)", "持有"
    elif total_score >= 50:
        return "★★☆☆☆ (2/5)", "减持"
    else:
        return "★☆☆☆☆ (1/5)", "卖出"


def safe_float(value, default=0):
    """安全转换为 float"""
    try:
        return float(value) if value else default
    except (ValueError, TypeError):
        return default


def generate_report(stock: str, data: dict) -> str:
    """生成深度分析报告"""
    quote = data.get('quote', {})
    technical = data.get('technical', {})
    f10 = data.get('f10', {})
    
    # 检查是否有错误
    has_error = any('error' in x for x in [quote, technical, f10] if isinstance(x, dict))
    
    # 计算各项评分
    value_score, value_details = score_value(quote, f10)
    growth_score, growth_details = score_growth(quote, f10)
    financial_score, financial_details = score_financial(quote, f10)
    technical_score, technical_details = score_technical(quote, technical)
    
    total_score = value_score + growth_score + financial_score + technical_score
    rating, rating_text = generate_rating(total_score)
    
    # 生成报告
    report = f"\n{'='*70}\n"
    report += f"📈 {data.get('stock', stock)} 深度分析报告\n"
    report += f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    report += f"{'='*70}\n\n"
    
    if has_error:
        report += "⚠️ **数据获取失败，使用默认评分**\n"
        report += "东方财富 API 连接不稳定，请稍后重试或检查网络连接。\n\n"
    
    # 核心数据
    report += "## 📊 核心数据\n"
    report += f"| 指标 | 数值 |\n"
    report += f"|------|------|\n"
    
    if isinstance(quote, dict) and 'error' not in quote:
        price = safe_float(quote.get('price', 0))
        report += f"| 当前价 | ¥{price:.2f} |\n"
        report += f"| 涨跌幅 | {safe_float(quote.get('change_percent'), 0):+.2f}% |\n"
        report += f"| 总市值 | {safe_float(quote.get('market_cap'), 0):.2f}亿 |\n"
    else:
        report += f"| 当前价 | N/A (数据获取失败) |\n"
        report += f"| 涨跌幅 | N/A |\n"
        report += f"| 总市值 | N/A |\n"
    
    if isinstance(f10, dict) and 'error' not in f10:
        report += f"| PE(TTM) | {safe_float(f10.get('pe_ttm'), 'N/A')} |\n"
        report += f"| PB | {safe_float(f10.get('pb'), 'N/A')} |\n"
        report += f"| ROE | {safe_float(f10.get('roe'), 'N/A')}% |\n"
    else:
        report += f"| PE(TTM) | N/A |\n"
        report += f"| PB | N/A |\n"
        report += f"| ROE | N/A |\n"
    
    report += "\n"
    
    # 多维评分
    report += "## 🎯 多维评分\n"
    report += f"- **价值评分**: {value_score}/25\n"
    report += f"- **成长评分**: {growth_score}/25\n"
    report += f"- **财务评分**: {financial_score}/25\n"
    report += f"- **技术评分**: {technical_score}/25\n"
    report += f"\n### 🏆 综合评分：{total_score}/100\n\n"
    
    # 建仓建议
    report += "## 💡 建仓建议\n"
    report += f"- **评级**: {rating}\n"
    report += f"- **建议**: {rating_text}\n"
    
    # 目标价估算
    price = safe_float(quote.get('price', 0) if isinstance(quote, dict) else 0)
    if price > 0:
        if total_score >= 80:
            target_low, target_high = price * 1.2, price * 1.4
        elif total_score >= 70:
            target_low, target_high = price * 1.1, price * 1.3
        elif total_score >= 60:
            target_low, target_high = price * 0.95, price * 1.15
        else:
            target_low, target_high = price * 0.8, price * 0.9
        
        report += f"- **目标价**: ¥{target_low:.2f} - ¥{target_high:.2f}\n"
        report += f"- **止损位**: ¥{price * 0.85:.2f}\n\n"
    else:
        report += "- **目标价**: 数据获取失败，无法计算\n"
        report += "- **止损位**: N/A\n\n"
    
    # 风险提示
    report += "## ⚠️ 风险提示\n"
    report += "1. 本报告仅供参考，不构成投资建议\n"
    report += "2. 数据来源于公开信息，可能存在延迟\n"
    report += "3. 股市有风险，投资需谨慎\n"
    report += "4. 评分模型简化处理，实际分析需结合更多信息\n\n"
    
    report += f"{'='*70}\n"
    report += "_数据来源：东方财富 | 分析模型：stock-analyzer v1.0 | 喵～🐱_\n"
    report += f"{'='*70}\n"
    
    return report


def analyze_stock(stock: str, retry_count: int = 3) -> dict:
    """分析单只股票（带重试）"""
    for i in range(retry_count):
        try:
            data = get_stock_info(stock, fields=['quote', 'technical', 'f10'])
            return data
        except Exception as e:
            if i == retry_count - 1:
                return {
                    'stock': stock,
                    'quote': {'error': str(e)},
                    'technical': {'error': str(e)},
                    'f10': {'error': str(e)}
                }
            time.sleep(1)


def main():
    parser = argparse.ArgumentParser(description="A 股深度分析工具")
    parser.add_argument("--stock", type=str, help="股票代码 (如：600519.SS)")
    parser.add_argument("--stocks", type=str, help="多只股票，逗号分隔")
    parser.add_argument("--json", action="store_true", help="输出 JSON 格式")
    parser.add_argument("--retry", type=int, default=3, help="重试次数 (默认 3)")
    
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
    
    # 分析并输出
    for stock in stocks:
        try:
            data = analyze_stock(stock.strip(), retry_count=args.retry)
            if args.json:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                report = generate_report(stock.strip(), data)
                print(report)
        except Exception as e:
            print(f"❌ 分析 {stock} 失败：{str(e)}")


if __name__ == "__main__":
    main()
