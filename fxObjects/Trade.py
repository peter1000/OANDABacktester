class Trade(object):
	id = 0
	units = 0
	side = ""
	instrument = ""
	price = ""

	# The class "constructor"
    def __init__(self, id, units, side, instrument, price):
        self.id = id
        self.units = units
        self.side = side
        self.instrument = instrument
        self.price = price