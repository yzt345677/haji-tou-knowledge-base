#!/usr/bin/env python3
"""
stock-announcements: A 股公告监控工具
数据源：东方财富 API

使用方法:
    uv run python announcements.py --stock 600519.SS --days 7
    uv run python announcements.py --stocks 600519.SS,300750.SZ --days 30
"""

import argparse
import json
import requests
from datetime import datetime, timedelta
from typing import Optional


# 东方财富公告 API
EASTMONEY_ANNOUNCEMENT_URL = "https://datacenter-web.eastmoney.com/api/data/v1/get"


def parse_stock_code(stock: str) -> tuple[str, str]:
    """
    解析股票代码
    600519.SS → ("SH600519", "上交所")
    300750.SZ → ("SZ300750", "深交所")
    """
    if "." in stock:
        code, exchange = stock.split(".")
        if exchange == "SS":
            return f"SH{code}", "上交所"
        elif exchange == "SZ":
            return f"SZ{code}", "深交所"
    raise ValueError(f"无效的股票代码格式：{stock}")


def get_announcements(stock: str, days: int = 7, announcement_type: str = "all") -> list[dict]:
    """
    获取股票公告
    
    Args:
        stock: 股票代码 (如 600519.SS)
        days: 近 N 天公告
        announcement_type: 公告类型 (all/financial/major/business/risk)
    """
    secid, exchange = parse_stock_code(stock)
    
    # 计算日期范围
    start_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    
    # 公告类型映射
    type_map = {
        "all": "",
        "financial": "年度报告，半年度报告，季度报告，业绩预告，业绩快报",
        "major": "重大资产重组，收购，出售资产，股份变动，股东减持",
        "business": "重大合同，中标，项目进展，对外投资",
        "risk": "退市风险，其他风险警示，行政处罚，立案调查"
    }
    
    params = {
        "sortColumns": "ANNOUNCEMENT_DATE",
        "sortTypes": "-1",
        "pageSize": "100",
        "pageNum": "1",
        "reportName": "RPT_PUBLIC_OP_NEWPUBLISH",
        "columns": "ALL",
        "source": "HSFSPAGE",
        "client": "WEB",
        "filter": f"""(SECUCODE="{secid}")(ANNOUNCEMENT_DATE>='{start_date}')(ANNOUNCEMENT_DATE<='{end_date}')"""
    }
    
    # 添加类型过滤
    if announcement_type != "all" and announcement_type in type_map:
        type_filter = type_map[announcement_type]
        params["filter"] += f"""(ANNOUNCEMENT_TYPE_NAME in ("{type_filter.replace(',', '","')}"))"""
    
    try:
        response = requests.get(EASTMONEY_ANNOUNCEMENT_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        announcements = []
        if data.get("result") and data["result"].get("data"):
            for item in data["result"]["data"]:
                announcements.append({
                    "title": item.get("ANNOUNCEMENT_TITLE", ""),
                    "type": item.get("ANNOUNCEMENT_TYPE_NAME", "未知"),
                    "date": item.get("ANNOUNCEMENT_DATE", "")[:10],
                    "url": f"http://data.eastmoney.com/notices/detail/{item.get('SECUCODE', '')}/{item.get('ANNOUNCEMENT_ID', '')}.html",
                    "summary": item.get("ANNOUNCEMENT_CONTENT", "")[:200] + "..." if item.get("ANNOUNCEMENT_CONTENT") else "",
                })
        
        return announcements
    except Exception as e:
        return [{"error": f"获取公告失败：{str(e)}"}]


def format_announcements(stock: str, announcements: list[dict], days: int) -> str:
    """
    格式化输出公告列表
    """
    output = f"\n{'='*60}\n"
    output += f"📢 {stock} 近{days}天公告\n"
    output += f"查询时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    output += f"{'='*60}\n"
    
    if not announcements:
        output += "\n暂无公告\n"
    else:
        output += f"\n共 {len(announcements)} 条公告:\n\n"
        for i, ann in enumerate(announcements, 1):
            if "error" in ann:
                output += f"  ❌ {ann['error']}\n"
            else:
                output += f"  [{i}] {ann['title']}\n"
                output += f"      类型：{ann['type']} | 日期：{ann['date']}\n"
                output += f"      链接：{ann['url']}\n"
                if ann.get('summary'):
                    output += f"      摘要：{ann['summary']}\n"
                output += "\n"
    
    output += f"{'='*60}\n"
    return output


def main():
    parser = argparse.ArgumentParser(description="A 股公告监控工具")
    parser.add_argument("--stock", type=str, help="股票代码 (如：600519.SS)")
    parser.add_argument("--stocks", type=str, help="多只股票，逗号分隔")
    parser.add_argument("--days", type=int, default=7, help="近 N 天公告 (默认 7)")
    parser.add_argument("--type", type=str, default="all", 
                       choices=["all", "financial", "major", "business", "risk"],
                       help="公告类型 (默认 all)")
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
    
    # 查询并输出
    for stock in stocks:
        try:
            announcements = get_announcements(stock.strip(), args.days, args.type)
            if args.json:
                result = {
                    "stock": stock.strip(),
                    "days": args.days,
                    "type": args.type,
                    "announcements": announcements
                }
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                print(format_announcements(stock.strip(), announcements, args.days))
        except Exception as e:
            print(f"❌ 处理 {stock} 失败：{str(e)}")


if __name__ == "__main__":
    main()
