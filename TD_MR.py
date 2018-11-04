from random_number import getRandom
from trial_division import checkTrialDivision
from miller_robin_test import miller_rabin
from generate_k_primes import kPrimes
import timeit
import matplotlib.pyplot as plt
from gcd_finder import computeGCD, computeGCDMR


# TD-MR Combination(n, k)
#   1) Random Number Generation
#       - Generate an n-bit odd random number r.
#   2) Trial division on r with k primes <= sqrt(n)
#       - Divides r by k small primes.
#       - If r is divided by any prime, go to Step 1.
#   3) Miller-Rabin test on r
#       - Perform Miller-Rabin Test on r.
#       - If r passes, return r as a prime.
#       - Otherwise, go to Step 1.
def combinationTD_MR(n, primes):
	k=100
	while True:
		# 1) Random Number Generation
		#       - Generate an n-bit odd random number r.
	
		r = getRandom(n)
		#print(r)
		#t = r* r * r
		#return r
	
		#   2) Trial division on r with k primes
		#       - Divides r by k small primes.
		#       - If r is divided by any prime, go to Step 1.
		
		if(checkTrialDivision(r, primes) == False):
			continue
			
		#print(False)
		#   3) Miller-Rabin test on r0
		#       - Perform Miller-Rabin Test on r.
		#       - If r passes, return r as a prime.
		#       - Otherwise, go to Step 1.
		
		if(miller_rabin(r) == False):
			#print(False)
			continue
			
		return r