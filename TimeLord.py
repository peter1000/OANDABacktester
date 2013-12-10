from fxObjects import Rate
from fxObjects import MarketSnapshot
import json

class TimeLord(object):

	def __init__(self):
		self.name = 0
		self.rate1 = Rate.Rate("EUR/USD", "time", "1", "2")
		self.snapShots = []


	def readJSON(self):	

		print "Loading JSON" 
		json_data = json.load(open('json_data.json'))

		instrumentName = json_data['instrument']
		candles = json_data['candles']

		for rate in candles:
			# create snapshot
			snap = MarketSnapshot.MarketSnapshot(rate["time"])
			#create new rate
			tmpRate = Rate.Rate(instrumentName, rate["time"], rate["openBid"], rate["openAsk"])
			# add rate/instrument to snapshot
			snap.addInstrument(instrumentName, tmpRate)
			# add snapshot to snaplist list
			self.snapShots.append(snap)

#		for s in self.snapShots :
#			print s.date
#			print s.instruments

	print "Json Loaded" 

	def mainLoop(self):
		print "Entering Main Loop"

	def initialize(self):
		self.readJSON()


def main():
	 x = TimeLord()
	 x.initialize()
	 x.mainLoop()
	
if  __name__ =='__main__':main()

