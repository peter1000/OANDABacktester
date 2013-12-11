if self.API.API_movingAverage10("EUR/USD") < self.API.API_getRate("EUR/USD").getRate().getAsk():
	self.API.API_postTrade('EUR/USD', 500, 'buy')
elifself.API.API_movingAverage10("EUR/USD") < self.API.API_getRate("EUR/USD").getRate().getBid():
	self.API.API_postTrade('EUR/USD', 500, 'sell')