# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algo ) 
import math
  
def computeGCD(x, y): 
   return math.gcd(x,y)
  
def computeGCDMR(n, primes):
	for a in primes:
		if math.gcd(a,n) != 1:
			return False
	return True