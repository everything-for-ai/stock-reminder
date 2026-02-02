# Stock Reminder / 股票提醒机器人

[English](#english) | [中文](#中文)

---

## English

📈 **Stock Reminder** - Real-time A-share/ETF monitoring with alerts

### Features

- 📊 **Real-time Quotes** - Tencent Finance API (free, no API key)
- ⏰ **Scheduled Push** - Auto push at 10:00 / 16:00 daily
- 📝 **Change Analysis** - Automatic trend analysis
- ⚠️ **Price Alerts** - Trigger when change > ±3%
- 📱 **Multi-platform** - Feishu, WeCom, Telegram

### Supported Stocks

| Code | Name | Type |
|------|------|------|
| 159941 | Nasdaq 100 LOF | ETF |
| 513100 | Nasdaq 100 | ETF |
| 600519 | Kweichow Moutai | A-share |
| 000001 | Ping An Bank | A-share |
| 513050 | China Internet | ETF |

### Quick Start

```bash
cd stock-reminder
pip install -r requirements.txt
python stock_bot.py
```

### Configuration

Edit `config.json`:
```json
{
    "schedule": ["10:00", "16:00"],
    "stocks": [
        {"code": "159941", "name": "Nasdaq 100 LOF", "type": "etf"}
    ]
}
```

---

## 中文

📈 **股票提醒机器人** - A股/ETF 实时行情监控与提醒

### 功能特点

- 📊 **实时行情** - 腾讯财经接口，无需 API Key
- ⏰ **定时推送** - 每天 10:00 / 16:00 自动推送
- 📝 **涨跌分析** - 自动分析涨跌幅度
- ⚠️ **价格预警** - 涨跌超过 ±3% 时触发预警
- 📱 **多平台支持** - 飞书、企业微信、Telegram

### 支持的股票

| 代码 | 名称 | 类型 |
|------|------|------|
| 159941 | 纳指100LOF | ETF |
| 513100 | 纳指100 | ETF (深基) |
| 600519 | 贵州茅台 | A 股 |
| 000001 | 平安银行 | A 股 |
| 513050 | 中概互联网 | ETF |

### 快速开始

```bash
cd stock-reminder
pip install -r requirements.txt
python stock_bot.py
```

### 配置说明

编辑 `config.json`：
```json
{
    "schedule": ["10:00", "16:00"],
    "stocks": [
        {"code": "159941", "name": "纳指100LOF", "type": "etf"}
    ]
}
```

---

## Project Structure / 项目结构

```
stock-reminder/
├── stock_bot.py      # Main program / 主程序
├── stock_api.py      # Stock API / 股票接口
├── config.json       # Configuration / 配置
├── requirements.txt  # Dependencies / 依赖
└── README.md         # This file / 本文档
```

## Data Source / 数据来源

- Tencent Finance (http://qt.gtimg.cn)
- Free API, no API key required

---

*README generated for everything-for-ai project*
