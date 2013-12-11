if self.API.API_movingAverage10() < self.API.API_getRate("EUR/USD"):
	self.API.API_postTrade('EUR/USD', 500, 'buy')
else:
	self.API.API_postTrade('EUR/USD', 500, 'sell')
