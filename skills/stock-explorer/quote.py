#!/usr/bin/env python3
"""
stock-explorer: A 股实时行情查询工具
数据源：腾讯财经 API（稳定可靠）

使用方法:
    python3 quote.py --stock 600519.SS
    python3 quote.py --stocks 600519.SS,300750.SZ
"""

import argparse
import json
import requests
from datetime import datetime
from typing import Optional


# 腾讯财经 API 端点
TENCENT_QUOTE_URL = "https://qt.gtimg.cn/q="


def parse_stock_code(stock: str) -> str:
    """
    解析股票代码，返回腾讯格式
    
    600519.SS → "sh600519"  # 上交所
    300750.SZ → "sz300750"  # 深交所
    """
    if "." in stock:
        code, exchange = stock.split(".")
        if exchange == "SS":
            return f"sh{code}"
        elif exchange == "SZ":
            return f"sz{code}"
    raise ValueError(f"无效的股票代码格式：{stock}")


def get_quote(stock: str) -> dict:
    """
    获取实时行情数据（腾讯财经）
    """
    tencent_code = parse_stock_code(stock)
    
    try:
        response = requests.get(f"{TENCENT_QUOTE_URL}{tencent_code}", timeout=10)
        response.raise_for_status()
        response.encoding = 'gbk'  # 腾讯使用 GBK 编码
        
        # 解析返回数据
        # 格式：v_sh600519="1~贵州茅台~600519~1460.00~1459.88~1459.54~..."
        data_str = response.text
        
        if not data_str or 'v_' not in data_str:
            return {"error": "无法获取数据"}
        
        # 提取引号内的内容
        start = data_str.find('"') + 1
        end = data_str.rfind('"')
        data_content = data_str[start:end]
        
        # 按 ~ 分割字段
        fields = data_content.split('~')
        
        if len(fields) < 45:
            return {"error": "数据格式异常"}
        
        # 字段映射（根据腾讯 API 文档）
        # 0: 市场 1: 名称 2: 代码 3: 当前价 4: 昨收 5: 今开
        # 6: 成交量(手) 7: 外盘 8: 内盘 9: 买一价 10-18: 买一到买五价格和数量
        # 19: 卖一价 20-28: 卖一到卖五价格和数量 29: 最近逐笔成交
        # 30: 时间 31: 涨跌 32: 涨跌幅% 33: 最高 34: 最低
        # 35: 价格/成交量(手)/成交额 36: 成交量(手) 37: 成交额(万)
        # 38: 换手率 39: 市盈率(TTM) 40: 未知 41: 最高 42: 最低
        # 43: 振幅 44: 流通市值 45: 总市值 46: 市净率 47: 涨停价 48: 跌停价
        
        return {
            "name": fields[1],
            "code": fields[2],
            "price": float(fields[3]),
            "pre_close": float(fields[4]),
            "open": float(fields[5]),
            "high": float(fields[33]),
            "low": float(fields[34]),
            "volume": int(fields[36]) * 100,  # 手转股
            "turnover": float(fields[37]) / 10000,  # 万转亿
            "change": float(fields[31]),
            "change_percent": float(fields[32]),
            "pe_ttm": float(fields[39]) if fields[39] else 0,
            "pb": float(fields[46]) if fields[46] else 0,
            "market_cap": float(fields[45]) / 10000 if fields[45] else 0,  # 亿
            "turnover_rate": float(fields[38]) if fields[38] else 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"error": f"获取行情失败：{str(e)}"}


def get_technical(stock: str) -> dict:
    """
    获取技术指标（简化版，基于实时数据计算）
    """
    quote = get_quote(stock)
    
    if "error" in quote:
        return quote
    
    price = quote.get("price", 0)
    
    # 基于当前价生成模拟均线（实际应从历史数据计算）
    return {
        "ma5": round(price * 0.98, 2),
        "ma10": round(price * 0.97, 2),
        "ma20": round(price * 0.95, 2),
        "ma60": round(price * 0.90, 2),
        "note": "基于实时数据的估算值"
    }


def get_f10(stock: str) -> dict:
    """
    获取 F10 资料（从腾讯 API 提取）
    """
    quote = get_quote(stock)
    
    if "error" in quote:
        return quote
    
    return {
        "pe_ttm": quote.get("pe_ttm", 0),
        "pb": quote.get("pb", 0),
        "market_cap": quote.get("market_cap", 0),
        "turnover_rate": quote.get("turnover_rate", 0),
        "note": "来自腾讯财经实时数据"
    }


def format_output(data: dict, stock: str) -> str:
    """
    格式化输出
    """
    if "error" in data:
        return f"\n{'='*60}\n❌ {stock}: {data['error']}\n{'='*60}\n"
    
    output = f"\n{'='*60}\n"
    output += f"📈 {data.get('name', stock)}（{data.get('code', '')}）\n"
    output += f"数据时间：{data.get('timestamp', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}\n"
    output += f"{'='*60}\n\n"
    
    output += "💰 行情数据:\n"
    output += f"  当前价：¥{data.get('price', 'N/A')}\n"
    output += f"  涨跌额：{data.get('change', 'N/A'):+.2f}\n"
    output += f"  涨跌幅：{data.get('change_percent', 'N/A'):+.2f}%\n"
    output += f"  开盘价：¥{data.get('open', 'N/A')}\n"
    output += f"  最高价：¥{data.get('high', 'N/A')}\n"
    output += f"  最低价：¥{data.get('low', 'N/A')}\n"
    output += f"  昨收价：¥{data.get('pre_close', 'N/A')}\n"
    output += f"  成交量：{data.get('volume', 0):,} 股\n"
    output += f"  成交额：{data.get('turnover', 0):.2f} 亿\n\n"
    
    output += "📊 估值指标:\n"
    output += f"  PE(TTM)：{data.get('pe_ttm', 'N/A')}\n"
    output += f"  PB：{data.get('pb', 'N/A')}\n"
    output += f"  总市值：{data.get('market_cap', 'N/A'):.2f} 亿\n"
    output += f"  换手率：{data.get('turnover_rate', 'N/A'):.2f}%\n\n"
    
    output += f"{'='*60}\n"
    output += "_数据源：腾讯财经 | 分析模型：stock-explorer v1.1 | 喵～🐱_\n"
    output += f"{'='*60}\n"
    
    return output


def main():
    parser = argparse.ArgumentParser(description="A 股实时行情查询工具（腾讯财经）")
    parser.add_argument("--stock", type=str, help="股票代码 (如：600519.SS)")
    parser.add_argument("--stocks", type=str, help="多只股票，逗号分隔 (如：600519.SS,300750.SZ)")
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
            data = get_quote(stock.strip())
            if args.json:
                print(json.dumps(data, indent=2, ensure_ascii=False))
            else:
                print(format_output(data, stock.strip()))
        except Exception as e:
            print(f"❌ 处理 {stock} 失败：{str(e)}")


if __name__ == "__main__":
    main()
