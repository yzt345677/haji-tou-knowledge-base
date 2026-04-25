# stock-announcements v1.0.0

A 股公告监控工具，从东方财富获取实时公告。

## 功能

- ✅ 财报公告（年报/季报/业绩预告）
- ✅ 重大事项（重组/收购/减持）
- ✅ 经营公告（合同中标/项目进展）
- ✅ 风险提示（ST/*ST/退市风险）
- ✅ 时间过滤（近 7 天/30 天/自定义）

## 使用方法

```bash
# 单只股票近 7 天公告
uv run python announcements.py --stock 600519.SS --days 7

# 单只股票近 30 天公告
uv run python announcements.py --stock 600519.SS --days 30

# 指定公告类型
uv run python announcements.py --stock 600519.SS --type financial

# 多只股票批量查询
uv run python announcements.py --stocks 600519.SS,300750.SZ --days 7
```

## 公告类型

| 类型 | 参数 | 说明 |
|------|------|------|
| 全部 | `all` | 所有公告（默认） |
| 财报 | `financial` | 年报/季报/业绩预告 |
| 重大事项 | `major` | 重组/收购/增减持 |
| 经营 | `business` | 合同/项目/中标 |
| 风险 | `risk` | ST/退市/处罚 |

## 数据源

- 东方财富公告 API
- 上交所/深交所官方公告
- 更新频率：实时

## 输出格式

```json
{
  "stock": "600519.SS",
  "announcements": [
    {
      "title": "贵州茅台 2025 年年度报告",
      "type": "财报",
      "date": "2026-03-28",
      "url": "http://www.cninfo.com.cn/xxx",
      "summary": "2025 年营收 XXX 亿，净利润 XXX 亿..."
    }
  ]
}
```

## 限制

- 仅支持 A 股公告
- 历史公告最多获取 100 条
