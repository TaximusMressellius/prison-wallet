"""Exchange objectt"""

class Exchange(object):

	"""Constructor
	type eing gdax, binance, etc.
	"""
	def __init__(self, type):
		self.type = type

	"""gets balances of each currency type on exchange
	return dict mapping currency type to amount
	"""
	def get_balances():
		pass

	"""get price of each currency type on exchange
	return dict mapping currency tyupe to price
	"""
	def get_prices():
		pass

	"""place buy order
	return True if successful, false otherwise
	"""
	def buy(currency_type, quantity, price):
		pass

	"""place sell order
	return True if successful, false otherwise
	"""
	def sell(currency_type, quantity, price):
		pass

	"""transfer funds to address"""
	def transfer(currency_type, quantity, destination):
		pass

	"""calculates and returns total fee"""
	def get_fee(currency_type):
		pass