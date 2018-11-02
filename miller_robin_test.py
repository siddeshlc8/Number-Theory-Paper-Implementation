import random
import numpy as np

# This function is called for all k trials. It returns 
# false if n is composite and returns false if n is probably
# prime.  
# d is an odd number such that  d*2^r = n-1 for some r >= 1     
def millerTest(d, n,r):
	# 1) Pick a random number 'a' in range [2, n-2]
	#    Corner cases make sure that n > 4
	if n < 4: 
		if n==3:
			return True
		else:
			return False
	a = random.randrange(2,n-2)


	#print('millerTest1')
	#print(d)
	#print(a)
	# 2) Compute: x = pow(a, d) % n
	x = (np.power(a, d)) % n
	#print(x)
	
	# 3) If x == 1 or x == n-1, return true.
	if x==1:
		return True
		
		
	# Below loop mainly runs 'r-1' times.
	# 4) Do following while d doesn't become n-1.
    #     a) x = (x*x) % n.
    #     b) If (x == 1) return false.
    #     c) If (x == n-1) return true.
	#print(d)
	for i in range(0,r):
		j = np.power(2,i)*r
		x = (np.power(a, j)) % n
		if x==n-1:
			return True
	# while d!=n-1:
	# 	#print(x)
	# 	x = (x*x) % n

	# 	d = d*2
		
	# 	if x==1:
	# 		return False
		
	# 	if x==n-1:
	# 		return True
	
	#print('millerTest2')		
	# 5)Return composite 
	return False; 
		
	
	
     

# It returns false if n is composite and returns true if n
# is probably prime.  k is an input parameter that determines
# accuracy level. Higher value of k indicates more accuracy.
def checkMillerRobinTest(n, k):
	#print('checkMillerRobinTest')
	# 1) Handle base cases for n < 3
	if n==0 or n==1:
		return False
	
	if n==2:
		return True
		
	# 2) If n is even, return false.
	if n%2==0:
		return False
		
	# 3) Find an odd number d such that n-1 can be written as d*2r. 
    #    Note that since n is odd, (n-1) must be even and r must be 
    #    greater than 0.
	d = n-1
	r=0
	while d%2==0:
		d = d/2
		d = int(d)
		r=r+1
		
    # 4) Do following k times
	
	if(millerTest(d, n, r) == False):
		return False
			
	# 5) Return true.
	return True
		
	
		
	
