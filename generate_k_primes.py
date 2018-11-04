from math import sqrt

def kPrimes(k):
	primes =[]
	count = 0
	number = 2
	while True:
		m=0
		for i in range(2,number):
			if(number % i) == 0:
				m=1
				break;
		if m==0:
			primes.append(number)
			count = count + 1
			
		if count >= k:
			break

		number = number + 1

	return primes


def k_Primes(k):
	primes =[]
	count = 0
	number = 2
	while True:
		m=0
		for i in range(2,number):
			if(number % i) == 0:
				m=1
				break;
		if m==0:
			primes.append(number)
			count = count + 1
			
		if number >= sqrt(k):
			break

		number = number + 1

	return primes