from Rate import *
class test(object):

    # The class "constructor" - It's actually an initializer 
	def __init__(self):
		self.name = 0
		

	def main():
		print "hello"
		rate = Rate("instrument", "time", "1", "2");
		print rate.instrument
		
	if  __name__ =='__main__':main()