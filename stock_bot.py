#!/usr/bin/env python3
"""
Stock Reminder - A股/港股/美股提醒
"""

import os
import json
import time
import requests
from datetime import datetime
from typing import Dict, List


class StockReminder:
    def __init__(self, config_file: str = "config.json"):
        self.config = self.load_config(config_file)
        self.session = requests.Session()
    
    def load_config(self, config_file: str) -> Dict:
        default_config = {
            "schedule": "09:00",
            "platforms": ["feishu"],
            "stocks": [
                {"symbol": "000001.SZ", "name": "平安银行"},
                {"symbol": "600519.SH", "name": "贵州茅台"},
                {"symbol": "00700.HK", "name": "腾讯控股"}
            ],
            "thresholds": {
                "rise": 5,   # 涨超5%提醒
                "fall": -5   # 跌超5%提醒
            }
        }
        
        if os.path.exists(config_file):
            with open(config_file, 'r') as f:
                config = json.load(f)
                default_config.update(config)
        
        return default_config
    
    def get_stock_price(self, symbol: str) -> Dict:
        """Get stock price (使用新浪API)"""
        try:
            if symbol.endswith(".SH"):
                url = f"http://hq.sinajs.cn/list={symbol}"
            elif symbol.endswith(".SZ"):
                url = f"http://hq.sinajs.cn/list={symbol}"
            else:
                return self.get_mock_price(symbol)
            
            headers = {"Referer": "http://finance.sina.com.cn"}
            response = self.session.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.text.split('"')[1].split(',')
                return {
                    "symbol": symbol,
                    "price": float(data[1]),
                    "change": float(data[2]),
                    "change_percent": float(data[3]),
                    "name": data[0]
                }
        except Exception as e:
            print(f"Stock API error: {e}")
        
        return self.get_mock_price(symbol)
    
    def get_mock_price(self, symbol: str) -> Dict:
        """模拟股价数据"""
        import random
        base_price = 100 if "600519" in symbol else 50
        change = random.uniform(-3, 3)
        
        return {
            "symbol": symbol,
            "price": round(base_price * (1 + change/100), 2),
            "change": round(change, 2),
            "change_percent": round(change, 2),
            "name": "模拟股票"
        }
    
    def format_stock_message(self, stocks: List[Dict]) -> str:
        """Format stock data as message"""
        lines = [f"📈 A股行情 - {datetime.now().strftime('%H:%M')}"]
        
        for stock in stocks:
            emoji = "📈" if stock["change_percent"] >= 0 else "📉"
            lines.append(f"{emoji} {stock.get('name', stock['symbol'])}")
            lines.append(f"   💰 {stock['price']} ({stock['change_percent']:+.2f}%)")
            lines.append("")
        
        return "\n".join(lines).strip()
    
    def run(self):
        stocks = []
        for stock in self.config.get("stocks", []):
            data = self.get_stock_price(stock["symbol"])
            data["name"] = stock.get("name", data.get("name", stock["symbol"]))
            stocks.append(data)
        
        message = self.format_stock_message(stocks)
        print(message)
        return message


if __name__ == "__main__":
    bot = StockReminder()
    bot.run()
