from math import sqrt

def checkTrialDivision(n, primes):
	for number in primes:
		if number < n:
			if(n % number == 0):
				return False
			
	return True
