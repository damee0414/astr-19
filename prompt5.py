import numpy as np
import math
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt 

def main():
	x = np.arange(0,2*math.pi,2*math.pi/1000)
	for i in range(0,len(x),1):
		print("x : ",x[i])
		print("sin(x) : ", math.sin(x[i]))
		print("\n")

if __name__=="__main__":
	main()