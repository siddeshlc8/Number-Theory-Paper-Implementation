from TD_MR import combinationTD_MR
from generate_k_primes import k_Primes
n = input('Enter the Number of Bits to be present in Genererated Random Prime Number')
n = int(n)
primes = k_Primes(n)
pi_k = 1
for p in primes:
	pi_k = pi_k * p
print(combinationTD_MR(n, primes))
