from Rate import *

class MarketSnapshot(object):

	def __init__(self, date):
		self.instruments = {}
		self.date = date


	def addInstrument(self, name, rate):
		self.instruments[name]=rate

	def getRate(self, instrument):
		return self.instruments[instrument]

	def getDate(self):
		return self.date