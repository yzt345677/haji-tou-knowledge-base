# stock-explorer v1.0.0

A 股实时行情查询工具，基于东方财富 API。

## 功能

- ✅ 实时股价/涨跌幅/成交量
- ✅ 技术指标（MA5/MA10/MA20/MA60）
- ✅ F10 资料（财务/股东/机构评级）
- ✅ 支持上交所（.SS）和深交所（.SZ）

## 使用方法

```bash
# 单只股票
uv run python quote.py --stock 600519.SS

# 多只股票
uv run python quote.py --stocks 600519.SS,300750.SZ,000858.SZ

# 带参数
uv run python quote.py --stock 600519.SS --fields quote,technical,f10
```

## 数据源

- 实时行情：东方财富 Push2 API
- F10 资料：东方财富 EMWeb API
- 技术指标：实时计算

## 输出格式

```json
{
  "stock": "600519.SS",
  "name": "贵州茅台",
  "quote": {
    "price": 1780.50,
    "change": "+1.2%",
    "volume": 1234567,
    "turnover": 21.98 亿
  },
  "technical": {
    "ma5": 1765.20,
    "ma10": 1750.80,
    "ma20": 1720.50,
    "ma60": 1680.30
  },
  "f10": {
    "marketCap": 22365 亿，
    "pe": 35.2,
    "pb": 8.5,
    "roe": 28.5%
  }
}
```

## 依赖

- Python 3.10+
- requests
- uv (已 bundled with OpenClaw)

## 限制

- 仅支持 A 股（上交所/深交所）
- 行情数据有 15 分钟延迟（非实时）
- 不建议用于高频交易
