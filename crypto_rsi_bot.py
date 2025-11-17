#!/usr/bin/env python3
import ccxt
import time
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(message)s',
    handlers=[logging.FileHandler("rsi_bot.log"), logging.StreamHandler()]
)

class RSITradingBot:
    def __init__(self, api_key, api_secret, symbol='BTC/USDT', timeframe='15m', rsi_period=14):
        self.exchange = ccxt.binance({
            'apiKey': api_key,
            'secret': api_secret,
            'enableRateLimit': True,
        })
        self.symbol = symbol
        self.timeframe = timeframe
        self.rsi_period = rsi_period
        self.overbought = 70
        self.oversold = 30

    def fetch_ohlcv(self):
        return self.exchange.fetch_ohlcv(self.symbol, self.timeframe, limit=self.rsi_period + 1)

    def calculate_rsi(self, prices):
        import numpy as np
        deltas = np.diff(prices)
        up = deltas.clip(min=0)
        down = abs(deltas.clip(max=0))
        ma_up = np.mean(up[-self.rsi_period:])
        ma_down = np.mean(down[-self.rsi_period:])
        rs = ma_up / ma_down if ma_down != 0 else float('inf')
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def run(self):
        logging.info("RSI бот запущен для %s", self.symbol)
        while True:
            try:
                bars = self.fetch_ohlcv()
                closes = [x[4] for x in bars]
                current_price = closes[-1]
                rsi = self.calculate_rsi(closes)

                logging.info(f"Цена: {current_price:.2f} | RSI: {rsi:.2f}")

                if rsi < self.oversold:
                    logging.info("ОВЕРСОЛД! Пора покупать?")
                elif rsi > self.overbought:
                    logging.info("ОВЕРБАУТ! Пора фиксировать?")

                time.sleep(60)  # проверка каждую минуту
            except Exception as e:
                logging.error(f"Ошибка: {e}")
                time.sleep(30)

if __name__ == "__main__":
    # ВНИМАНИЕ: не коммить реальные ключи!
    API_KEY = 'YOUR_API_KEY'
    API_SECRET = 'YOUR_API_SECRET'

    bot = RSITradingBot(API_KEY, API_SECRET)
    bot.run()
