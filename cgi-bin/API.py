import sys
sys.dont_write_bytecode = True

from fxObjects import Trade
import json
class API:

	def __init__(self):
		self.snapShots = []
		self.positions = {} # dictionary of a list of trades
		self.pnl = 0
		self.cash = 0
		self.unrealized = 0
		self.stats = []

	def API_newSnapShot(self, snapShot):

		self.snapShots.append(snapShot)

		if len(self.snapShots) > 500:
			self.snapShots.pop(0)


	def API_getRate(self, instrumentName):
		return self.snapShots[-1].getRate(instrumentName).getMid()

	def getRate_ABI(self, instrumentName):
		return self.snapShots[-1].getRate(instrumentName)


	def Rate(self, side, rate):
		if side == 'buy':
			return rate.getAsk()
		else:
			return rate.getBid()

	def API_postTrade(self, instrumentName, units, side):
		curRate = self.Rate(side, self.snapShots[-1].getRate(instrumentName))
		if instrumentName in self.positions: #if there is a trade existing
			curposition = self.positions[instrumentName]
			if curposition[0].side != side: #if the side we are trading does not match the side of the trade that exists
				diffUnits = curposition[0].units - units #Number of units in trade object subtract number of units selling/buying
				if diffUnits > 0:
					curposition[0].units = diffUnits
					self.pnl += units * (curposition[0].price - curRate)
					self.cash += units*self.Rate(side, self.snapShots[-1].getRate(instrumentName))
				elif diffUnits == 0:
					self.pnl += units * (curposition[0].price - curRate)
					self.cash += units*self.Rate(side, self.snapShots[-1].getRate(instrumentName))
					curposition.pop(0)
					if len(curposition) == 0:
						del self.positions[instrumentName]
				else:
					self.pnl += curposition[0].units * (curposition[0].price - curRate)
					self.cash += units * self.Rate(side, self.snapShots[-1].getRate(instrumentName))
					curposition.pop(0)
					if len(curposition) == 0:
						del self.positions[instrumentName]
					self.API_postTrade(instrumentName, diffUnits * -1, side)
			else:
				trade = Trade.Trade(0, units, side, instrumentName, curRate)
				curposition = trade
				self.cash -= trade.units*trade.price
				self.positions[instrumentName].append(trade)
		else: #no trade exists
			trade = Trade.Trade(0, units, side, instrumentName, curRate)
			curposition = trade
			self.positions[instrumentName] = []
			self.cash -= trade.units*trade.price
			self.positions[instrumentName].append(trade)

		return 1.00

	def API_abstractMovingAverage(self, interval, instrumentName):
		#print interval
		if interval > len(self.snapShots):
			movingAverage = self.API_abstractMovingAverage(len(self.snapShots), instrumentName)
			return movingAverage
		else:
			movingAverage = 0
			for x in range((len(self.snapShots) - interval), len(self.snapShots)):
				i = x
				movingAverage = (movingAverage + self.snapShots[i].getRate(instrumentName))
			return float(movingAverage)/interval

	def API_movingAverage10(self, instrumentName):
		return self.API_abstractMovingAverage(10, instrumentName)

	def API_movingAverage50(self, instrumentName):
		return self.API_abstractMovingAverage(50, instrumentName)

	def API_movingAverage100(self, instrumentName):
		return self.API_abstractMovingAverage(100, instrumentName)

	def API_computeStats(self):
		#self.stats[self.snapShots[-1].getDate()]=self.pnl
		self.stats.append([self.snapShots[-1].getDate(), -1*self.pnl, self.cash, self.unrealized, self.unrealized-self.pnl])

	def API_outputStats(self):
		with open('data.txt', 'w') as outfile:
  			json.dump({"data":self.stats}, outfile)

  	def API_closePositions(self, instrumentName):
		print "closing positions"
		if instrumentName in self.positions:
			tradeObjects = self.positions[instrumentName]
			totalUnits = 0
			side = ""
			i = len(tradeObjects)
			while(i > 0):
				i = i - 1
				#totalUnits += trade.units
				trade = tradeObjects[0]
				side = trade.side
				if side == "buy":
					side = "sell"
				elif side == "sell":
					side = "buy"
				self.API_postTrade(instrumentName, trade.units, side);
		self.unrealized = 0
				
  	def API_unRealized(self, instrumentName):
		if instrumentName in self.positions:
			tradeObjects = self.positions[instrumentName]
			totalUnits = 0
			side = ""
			i = len(tradeObjects)
			while(i > 0):
				i = i - 1
				#totalUnits += trade.units
				trade = tradeObjects[0]
				side = trade.side
				if side == "buy":
					self.unrealized = self.unrealized + (trade.units*self.Rate(side, self.snapShots[-1].getRate(instrumentName))-(trade.price * trade.units))
				elif side == "sell":
					self.unrealized = self.unrealized - (trade.units*self.Rate(side, self.snapShots[-1].getRate(instrumentName)) -(trade.price * trade.units))
		print "unrealized" + str(self.unrealized)
