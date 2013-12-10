from Rate import *

class MarketSnapshot(object):

	def __init__(self):
		self.rate1 = Rate.Rate("EUR/USD", "time", "1", "2");
		self.instruemnts = dict("EUR/USD" = self.rate1)


	
		
