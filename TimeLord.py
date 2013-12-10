from fxObjects import Rate
class TimeLord(object):

	def __init__(self):
		self.name = 0
		self.rate1 = Rate.Rate("EUR/USD", "time", "1", "2");


	def initialize(self):
		rate1 = Rate.Rate("EUR/USD", "time", "1", "2");
		# read in tick data into object.

	def mainLoop(self):
		print self.rate1.instrument
		print self.rate1.time
		print self.rate1.bid
		print self.rate1.ask

def main():
	 x = TimeLord()
	 x.initialize()
	 x.mainLoop()
	
if  __name__ =='__main__':main()

