class Account(object):
	id = 0
	balance = 0
	positionList = []

	# The class "constructor"
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance