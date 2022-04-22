import numpy as np

class animal:
	def __init__(self,armlen,leglen,eye,tail,furry):
		self.armlen = armlen
		self.leglen = leglen
		self.eye = eye
		self.tail = tail
		self.furry = furry

	def print(self,armlen,leglen,eye,tail,furry):
		print("length of the arms : ", armlen)
		print("length of the legs : ", leglen)
		print("number of eyes : ", eye)
		print("does it have a tail? : ",tail)
		print("is it furry? : ",furry)



def main():
	#a = animal(0.9,0.9,2,True,True)
	a.print(0.9,0.9,2,True,True)
	
if __name__=="__main__":
	main()