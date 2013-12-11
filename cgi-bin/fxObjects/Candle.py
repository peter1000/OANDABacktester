class Candle(object):
	time = 0
	openMid = 0
	highMid = 0
	lowMid = 0
	closeMid = 0
	volume = 0

	# The class "constructor"
    def __init__(self, time, openMid, highMid, lowMid, closeMid, volume):
        self.time = time
        self.openMid = openMid
        self.highMid = highMid
        self.lowMid = lowMid
        self.closeMid = closeMid
        self.volume = volume