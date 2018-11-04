from random_number import getRandom
from trial_division import checkTrialDivision
from miller_robin_test import miller_rabin
from generate_k_primes import kPrimes
import timeit
import matplotlib.pyplot as plt
from gcd_finder import computeGCD, computeGCDMR

# PGCD-MR Combination(n, k)
#	1) Random Number Generation
#		- Generate an n-bit odd random number r.
#	2) GCD test on r and Πk
#		- Computes GCD(r, Πk)
#		- If the result is not 1, go to Step 1.
#	3) Miller-Rabin test on r
#		- Perform Miller-Rabin Test on r.
#		- If r passes, return r as a prime.
#		- Otherwise, go to Step 1.
def combinationPGCD_MR(n, primes):
	k=100
	while True:
		# 1) Random Number Generation
		#       - Generate an n-bit odd random number r.
	
		r = getRandom(n)
		#print(r)
		#t = r* r * r
		#return r
	
		#	2) GCD test on r and Πk
		#		- Computes GCD(r, Πk)
		#		- If the result is not 1, go to Step 1.
		
		if(computeGCD(r, primes) != 1):
			continue
			
		#print(False)
		#   3) Miller-Rabin test on r
		#       - Perform Miller-Rabin Test on r.
		#       - If r passes, return r as a prime.
		#       - Otherwise, go to Step 1.
		
		if(miller_rabin(r) == False):
			#print(False)
			continue
			
		return r