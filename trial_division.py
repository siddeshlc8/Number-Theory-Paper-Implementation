

def checkTrialDivision(n, primes):
	if n in primes:
		return True
	for number in primes:
		if(n % number == 0):
			return False
			
	return True
