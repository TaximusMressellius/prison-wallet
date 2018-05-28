from enum import Enum

from exchange import Exchange

# List of Exchange objects
EXCHANGES = []

PROFIT_MARGIN = 0.1
TRADE_QUANTITY = 10

class CurrencyType(Enum):
	BTC = "Bitcoin"
	LTC = "Litecoin"

class ExchangeType(Enum):
	GDAX = "GDAX"
	BINANCE = "Binance"

def populate_exchanges():
	gdax = Exchange(ExchangeType.GDAX)
	EXCHANGES.append(gdax)

	binance = Exchange(ExchangeType.BINANCE)
	EXCHANGES.append(binance)

def balance(exchange):
	balance = exchange.get_balance


def main():
	populate_exchanges()
	max_prices = {} #key: currency_type, value: max_price, exchange
	min_prices = {}
    for exchange in EXCHANGES:
    	prices = exchange.get_prices()
    	for currency, price in prices.items():
    		# figure out max and min prices for each currency
    		# place into respective dicts
    		pass
    for currency in max_prices:
    	max = max_prices[currency][0]
    	max_exchange = max_prices[currency][1]

    	min = min_prices[currency][0]
    	min_exchange = min_prices[currency][1]

    	buy_price = 1.1 * min 
    	sell_price = 0.9 * max
    	ratio = (sell_price - buy_price)/buy_price 

    	fees = max_exchange.get_fee(currency) + min_exchange.get_fee(currency)

    	if ratio > PROFIT_MARGIN - fees:
    		min_exchange.buy(currency, TRADE_QUANTITY, buy_price)
    		max_exchange.sell(currency, TRADE_QUANTITY, sell_price)
    		balance(min_exchange)

if __name__ == '__main__':
    main()