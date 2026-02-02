# Stock Reminder / 股票提醒机器人

<div class="tabs">
<details>
<summary><span>🇺🇸 English</span></summary>

## 📈 Stock Reminder

Real-time A-share/ETF monitoring with alerts

### Features
- 📊 Real-time quotes (Tencent Finance, free)
- ⏰ Scheduled push (10:00 / 16:00 daily)
- 📝 Automatic trend analysis
- ⚠️ Price alerts (> ±3%)

### Supported Stocks
| Code | Name | Type |
|------|------|------|
| 159941 | Nasdaq 100 LOF | ETF |
| 513100 | Nasdaq 100 | ETF |
| 600519 | Kweichow Moutai | A-share |

### Quick Start
```bash
cd stock-reminder
pip install -r requirements.txt
python stock_bot.py
```

</details>
<details>
<summary><span>🇨🇳 中文</span></summary>

## 📈 股票提醒机器人

A股/ETF 实时行情监控与提醒

### 功能特点
- 📊 实时行情（腾讯财经，免费）
- ⏰ 定时推送（每天 10:00 / 16:00）
- 📝 自动涨跌分析
- ⚠️ 价格预警（涨跌 ±3%）

### 支持的股票
| 代码 | 名称 | 类型 |
|------|------|------|
| 159941 | 纳指100LOF | ETF |
| 513100 | 纳指100 | ETF |
| 600519 | 贵州茅台 | A 股 |

### 快速开始
```bash
cd stock-reminder
pip install -r requirements.txt
python stock_bot.py
```

</details>
</div>

---

## Project Structure

```
stock-reminder/
├── stock_bot.py      # Main program
├── stock_api.py      # Stock API
├── config.json       # Configuration
└── requirements.txt  # Dependencies
```

## License

MIT
