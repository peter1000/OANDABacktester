import sys
import re
import cgi
sys.dont_write_bytecode = True

from fxObjects import Rate
from fxObjects import MarketSnapshot
import json
import API

class TimeLord(object):

	def __init__(self):
		self.name = 0
		self.rate1 = Rate.Rate("EUR/USD", "time", "1", "2")
		self.snapShots = []
		self.API = API.API()

	def readJSON(self):

		print "Loading JSON"
		json_data = json.load(open('cgi-bin/history/EUR_USD.json'))
		print "got JSON data"
		instrumentName = "EUR/USD"
		candles = json_data

		for rate in candles:
			# create snapshot
			snap = MarketSnapshot.MarketSnapshot(rate["time"])
			#create new rate
			tmpRate = Rate.Rate(instrumentName, rate["time"], rate["openBid"], rate["openAsk"])
			# add rate/instrument to snapshot
			snap.addInstrument(instrumentName, tmpRate)
			# add snapshot to snaplist list
			self.snapShots.append(snap)

		print "Json Loaded"


	def getAlgorithm(self):
		#with open ("input.txt", "r") as inputFile:
		#	algorithm = inputFile.read()

		#print "in getAlgorithm"
		form = cgi.FieldStorage()
		algorithm = form.getvalue("user-script");
		#print algorithm
		algorithm = self.doRegex(algorithm)
		#print algorithm

		with open ("cgi-bin/input.py", "w") as outputFile:
			outputFile.write(algorithm)
			

	def doRegex(self, algorithm):

		#	getRate("EUR/USD")
		#   getRate("EUR/USD").getRate()

		
		return re.sub( r'(getRate|postTrade|movingAverage)', r'self.API.API_\1', algorithm)

		#return re.sub( r'(getRate|postTrade|movingAverage)', r'self.API.API_\1', algorithm) 
		#return re.sub(r'(getRate(.*?))', r'\1.getRate()', algorithm )

	def mainLoop(self):
		print "Entering Main Loop"
		i = 0
		length = len(self.snapShots)
		#print length
		for snap in self.snapShots:
			self.API.API_newSnapShot(snap)

			#print self.API.API_movingAverage10("EUR/USD")
			#else:
			if i == length-1:
				self.API.API_closePositions('EUR/USD')
				self.API.API_computeStats()
			else:
				#execfunc('cgi-bin/input.py')
				if self.API.API_movingAverage10("EUR/USD") < self.API.API_getRate("EUR/USD"):
					self.API.API_postTrade('EUR/USD', 500, 'buy')
				else:
					self.API.API_postTrade('EUR/USD', 500, 'sell')

				if self.API.API_movingAverage50("EUR/USD") > self.API.API_getRate("EUR/USD"):
					self.API.API_postTrade('EUR/USD', 500, 'buy')
				else:
					self.API.API_postTrade('EUR/USD', 500, 'sell')
			if i % 60 == 0:
		#		self.API.API_postTrade('EUR/USD', 1, 'buy')
				self.API.API_computeStats()
			i = i + 1

		self.API.API_outputStats()

			#print self.API.pnl


	def initialize(self):
		self.readJSON()


def main():
	print "Content-type: text/html"
	print
	print "<title>Test CGI</title>"
	x = TimeLord()
	x.getAlgorithm()

	x.initialize()
	x.mainLoop()

if  __name__ =='__main__':main()

