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
