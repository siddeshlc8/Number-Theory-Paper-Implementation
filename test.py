# TD-MR Combination(n, k)
#	1) Random Number Generation
#		- Generate an n-bit odd random number r.
#	2) GCD test
#		- Find GCD of  r and k small primes.
#		- If GCD is not 1 with any prime, go to Step 1.
#	3) Miller-Rabin test on r
#		- Perform Miller-Rabin Test on r.
#		- If r passes, return r as a prime.
#		- Otherwise, go to Step 1.