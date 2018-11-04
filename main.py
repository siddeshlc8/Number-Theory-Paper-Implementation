from random_number import getRandom
from trial_division import checkTrialDivision
from miller_robin_test import miller_rabin
from generate_k_primes import kPrimes
import timeit
import matplotlib.pyplot as plt
from gcd_finder import computeGCD



# MGCD-MR Combination(n, k)
#	1) Random Number Generation
#		- Generate an n-bit odd random number r.
#	2) GCD test on r and Πkj
#		- Divide Πk into the proper length of Πkj
#		- Computes GCD(r, Πkj ) sequentially
#		- If any result is not 1, go to Step 1.
#	3) Miller-Rabin test on r
#		- Perform Miller-Rabin Test on r.
#		- If r passes, return r as a prime.
#		- Otherwise, go to Step 1.




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
		

bits = [4,8,16,32, 64 ,128 ,256 ,512 ,1024 ,2048 ,4096]
time1 = []
time2 = []
k_primes = [9, 15, 25, 43, 74, 131, 232, 417]
#k_primes = list(range(10,500, 10))

for n in bits:
	primes = kPrimes(n)
	pi_k = 1
	for p in primes:
		pi_k = pi_k * p

	start = timeit.default_timer()
	print(str(combinationTD_MR(n, primes)))
	stop = timeit.default_timer()
	print(str(n)+' Time: ' + str(stop - start) + '----------') 
	time1.append(stop - start)
		

	start = timeit.default_timer()
	print(str(combinationPGCD_MR(n, pi_k)))
	stop = timeit.default_timer()
	print(str(n)+' Time: ' + str(stop - start) + '----------') 
	time2.append(stop - start)


# plotting the points  
plt.semilogx(bits, time1, label='TD_MR') 
plt.semilogx(bits, time2, label='PGCD_MR') 
plt.xticks([4,8,16,32, 64 ,128 ,256 ,512 ,1024 ,2048 ,4096], (4,8,16,32, 64 ,128 ,256 ,512 ,1024 ,2048 ,4096))
# naming the x axis 
plt.xlabel('Number of Bits in Generated prime') 
# naming the y axis 
plt.ylabel('Time in sec') 
  
# giving a title to my graph 
plt.title('Fig. 1. Comparison of Running time of Trial Division(TD MR) and PGCD') 
plt.legend()
  
# function to show the plot 
plt.show()