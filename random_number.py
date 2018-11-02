import random

def getRandom(n):
	while True:
	 	a = random.randrange(2**(n-1),(2**n))
	 	if a%2==0:
	 		continue
	 	return a
