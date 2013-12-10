class API:

	def __init__(self):
		self.snapShots = []

	def API_newSnapShot(self, snapshot):
		self.snapShots.append(snapShot)


	def API_getRate(self, instrumentName):
		return snapShots[-1].getRate(instrumentName)


	def API_buy(self, instrumentName, units):
		return 1.00

	def API_sell(self, instrument, units):
		return 1.00

	def API_movingAverage10(self, instrumentName):
		return API_abstractmovingAverage(self, 10, instrumentName)

	def API_movingAverage50(self, instrumentName):
		return API_abstractmovingAverage(self, 50, instrumentName)

	def API_movingAverage100(self, instrumentName):
		return API_abstractmovingAverage(self, 100, instrumentName)

	def API_abstractMovingAverage(self, interval, instrumentName):
		if interval > len(self.snapShots):
			self.API_abstractmovingAverage(self, len(self.snapShots), instrumentName)
		else:
			movingAverage = 0
			for x in range(interval, (len(self.snapShots) - interval)):
				i = -1*x
				movingAverage = movingAverage + self.snapShots[i]
			return float(movingAverage)/interval