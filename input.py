if self.API.API_movingAverage10("EUR/USD") < self.API.API_getRate("EUR/USD").getRate():
	self.API.API_postTrade('EUR/USD', 500, 'buy')
else:
	self.API.API_postTrade('EUR/USD', 500, 'sell')

if self.API.API_movingAverage50("EUR/USD") > self.API.API_getRate("EUR/USD").getRate():
	self.API.API_postTrade('EUR/USD', 500, 'buy')
else:
	self.API.API_postTrade('EUR/USD', 500, 'sell')