import sys
sys.dont_write_bytecode = True

from fxObjects import Trade
import json
class API:

	def __init__(self):
		self.snapShots = []
		self.positions = {} # dictionary of a list of trades
		self.pnl = 0
		self.stats = []

	def API_newSnapShot(self, snapShot):

		self.snapShots.append(snapShot)

		if len(self.snapShots) > 500:
			self.snapShots.pop(0)


	def API_getRate(self, instrumentName):
		return self.snapShots[-1].getRate(instrumentName)


	def Rate(self, side, rate):
		if side == 'buy':
			return rate.getBid()
		else:
			return rate.getAsk()
			
	def API_postTrade(self, instrumentName, units, side):
		if instrumentName in self.positions:
			curposition = self.positions[instrumentName]
			if curposition[0].side != side:
				diffUnits = curposition[0].units - units #Number of units in trade object subtract number of units selling/buying
				if diffUnits > 0:
					curposition[0].units = diffUnits
					self.pnl += units * (curposition[0].price - self.Rate(side, self.snapShots[-1].getRate(instrumentName)))
				elif diffUnits == 0:
					self.pnl += units * (curposition[0].price - self.Rate(side, self.snapShots[-1].getRate(instrumentName)))
					curposition.pop(0)
					if len(curposition) == 0:
						del self.positions[instrumentName]
				else:
					self.pnl += curposition[0].units * (curposition[0].price - self.Rate(side, self.snapShots[-1].getRate(instrumentName)))
					curposition.pop(0)
					if len(curposition) == 0:
						del self.positions[instrumentName]
					self.API_postTrade(instrumentName, diffUnits * -1, side) 
			else:
				trade = Trade.Trade(0, units, side, instrumentName, self.Rate(side, self.snapShots[-1].getRate(instrumentName)))
				curposition = trade				
				self.positions[instrumentName].append(trade)
		else:
			trade = Trade.Trade(0, units, side, instrumentName, self.Rate(side, self.snapShots[-1].getRate(instrumentName)))
			curposition = trade
			self.positions[instrumentName] = []
			self.positions[instrumentName].append(trade)
			
		return 1.00

	def API_abstractMovingAverage(self, interval, instrumentName):
		if interval > len(self.snapShots):
			self.API_abstractMovingAverage(len(self.snapShots), instrumentName)
		else:
			movingAverage = 0
			for x in range(interval, (len(self.snapShots) - interval)):
				i = -1*x
				movingAverage = movingAverage + self.snapShots[i].getRate(instrumentName).getAvg() 
			return float(movingAverage)/interval

	def API_movingAverage10(self, instrumentName):
		return self.API_abstractMovingAverage(10, instrumentName)

	def API_movingAverage50(self, instrumentName):
		return self.API_abstractMovingAverage(50, instrumentName)

	def API_movingAverage100(self, instrumentName):
		return self.API_abstractMovingAverage(100, instrumentName)

	def API_computeStats(self):
		#self.stats[self.snapShots[-1].getDate()]=self.pnl
		self.stats.append([self.snapShots[-1].getDate(), self.pnl])

	def API_outputStats(self):
		with open('data.txt', 'w') as outfile:
  			json.dump(self.stats, outfile)

  	def API_closeTrade(self, instrumentName):
		if instrumentName in self.positions:
			tradeObject = self.positions[instrumentName]
			totalUnits = 0
			side = ""
			for i in tradeObject:
				totalUnits += i.units
				side = i.side

			if side == "buy":
				side = "sell"
			elif side == "sell":
				side = "buy"

			self.API_postTrade(instrumentName, totalUnits, side);
