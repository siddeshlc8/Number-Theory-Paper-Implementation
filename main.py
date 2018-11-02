from random_number import getRandom
from trial_division import checkTrialDivision
from miller_robin_test import checkMillerRobinTest
from generate_k_primes import kPrimes
import timeit
import matplotlib.pyplot as plt
from gcd_finder import computeGCD




# TD-MR Combination(n, k)
#   1) Random Number Generation
#       - Generate an n-bit odd random number r.
#   2) Trial division on r with k primes
#       - Divides r by k small primes.
#       - If r is divided by any prime, go to Step 1.
#   3) Miller-Rabin test on r
#       - Perform Miller-Rabin Test on r.
#       - If r passes, return r as a prime.
#       - Otherwise, go to Step 1.

def combinationPGCD_MR(n, primes):
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
		
		if(computeGCD(r, primes) != 1):
			continue
			
		#print(False)
		#   3) Miller-Rabin test on r
		#       - Perform Miller-Rabin Test on r.
		#       - If r passes, return r as a prime.
		#       - Otherwise, go to Step 1.
		
		if(checkMillerRobinTest(r, 5) == False):
			#print(False)
			continue
			
		return r



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
		#   3) Miller-Rabin test on r
		#       - Perform Miller-Rabin Test on r.
		#       - If r passes, return r as a prime.
		#       - Otherwise, go to Step 1.
		
		if(checkMillerRobinTest(r, 5) == False):
			#print(False)
			continue
			
		return r
		

bits = [4,6,8,10,12,14,16,18,20]
time1 = []
time2 = []

for n in bits:
	primes = kPrimes(n)
	pi_k = 1
	for p in primes:
		pi_k = pi_k * p

	start = timeit.default_timer()
	print(str(combinationTD_MR(n, primes))+ '----------')
	stop = timeit.default_timer()
	print(str(n)+' Time: ', stop - start) 
	time1.append(stop - start)
		

	start = timeit.default_timer()
	print(str(combinationPGCD_MR(n, pi_k))+ '----------')
	stop = timeit.default_timer()
	print(str(n)+' Time: ', stop - start) 
	time2.append(stop - start)

# plotting the points  
plt.plot(bits, time1, label='TD_MR') 
plt.plot(bits, time2, label='PGCD_MR') 
  
# naming the x axis 
plt.xlabel('Bits') 
# naming the y axis 
plt.ylabel('Time') 
  
# giving a title to my graph 
plt.title('Random Prime Generation') 
  
# function to show the plot 
plt.show()