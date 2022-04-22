import numpy as np

def f(x):
	return x**3+8

def main():
	x = 9
	ans = f(x)
	print(ans)
	if ans > 27:
		print("YAY!")

if __name__=="__main__":
	main()