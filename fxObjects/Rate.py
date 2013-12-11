class Rate(object):
	instrument = ""
	time = ""
	bid = 0
	ask = 0

	# The class "constructor" - It's actually an initializer 
	def __init__(self, instrument, time, bid, ask):
		self.instrument = instrument
		self.time = time
		self.bid = bid
		self.ask = ask

	def getTime(self):
		return self.time
		
	def getAsk(self):
		return self.ask		
		
	def getBid(self):
		return self.bid

	def getMid(self):
		return (self.bid + self.ask) / 2