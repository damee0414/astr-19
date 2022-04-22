import numpy as np
import math
import tabulate
import pandas as pd
import matplotlib.pyplot as plt 

def sin(x):
	return math.sin(x)

def cos(x):
	return math.cos(x)

def main():
	print("x                     sin                   cos")
	for i in np.arange(0,2*math.pi,2*math.pi/1000):
		print(i,sin(i),cos(i))

if __name__=="__main__":
	main()