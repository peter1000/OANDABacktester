class Position(object):
	instrument = ""
	tradeList = []

	# The class "constructor"
    def __init__(self, instrument):
        self.instrument = instrument