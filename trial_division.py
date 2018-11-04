

def checkTrialDivision(n, primes):
	for number in primes:
		if(n % number == 0):
			return False
			
	return True
