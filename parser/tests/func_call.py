class a:
	def __init__(self):
		print "Started"
	def _a(self,x):
		print x
	def _b(self,y):
		print y
if __name__ == "__main__":
	x = a()
	x._a('hello')
