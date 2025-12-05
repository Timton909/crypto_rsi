# RSI Crypto Bot

Простой RSI-бот для Binance. Торгует только глазами — сам ничего не покупает/продаёт, просто орёт в лог когда RSI в экстремальной зоне.


## Зачем
Хотелось лёгкий скрипт, который можно запустить на VPS и смотреть логи. Без вебхуков, без телеграм-ботов, без понтов.

## Установка
```bash
git clone https://github.com/Tinkard1/rsi-crypto-bot.git
cd rsi-crypto-bot
pip install ccxt numpy
Настройка

Создай API-ключ на Binance (только чтение, без вывода!)
Открой crypto_rsi_bot.py
Замени YOUR_API_KEY и YOUR_API_SECRET на свои
По желанию поменяй пару, таймфрейм, уровни RSI

Запуск
bashpython3 crypto_rsi_bot.py
Логи пишутся в rsi_bot.log и в консоль.
