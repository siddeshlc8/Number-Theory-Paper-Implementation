from generate_k_primes import kPrimes, k_Primes
import timeit
import matplotlib.pyplot as plt
from TD_MR import combinationTD_MR
from GCD_MR import combinationGCD_MR
from PGCD_MR import combinationPGCD_MR

	

bits = [4,8,16,32, 64 ,128 ,256 ,512 ,1024]
bits2 = [32, 64, 128, 256, 512, 1024, 2048, 4096]
time1 = [0,0,0,0,0,0,0,0,0]
time2 = [0,0,0,0,0,0,0,0,0]
time3 = [0,0,0,0,0,0,0,0,0]
k_primes = [9, 15, 25, 43, 74, 131, 232, 417]
time = [0,0,0]

for i in range(0,10):
	j=0
	print(i)
	for n in bits[:-1]:
		primes = k_Primes(n)
		pi_k = 1
		for p in primes:
			pi_k = pi_k * p

		start = timeit.default_timer()
		combinationTD_MR(n, primes)
		stop = timeit.default_timer()
		#print(str(n)+' Time: ' + str(stop - start) + '----------') 
		time1[j] = time1[j] + (stop - start)
		time[0] = time[0] + (stop - start)


		start = timeit.default_timer()
		combinationPGCD_MR(n, pi_k)
		stop = timeit.default_timer()
		#print(str(n)+' Time: ' + str(stop - start) + '----------') 
		time2[j] = time2[j] + (stop - start)
		time[1] = time[1] + (stop - start)


		start = timeit.default_timer()
		combinationGCD_MR(n, primes)
		stop = timeit.default_timer()
		#print(str(n)+' Time: ' + str(stop - start) + '----------') 
		time3[j] = time3[j] + (stop - start)
		time[2] = time[2] + (stop - start)

		j = j + 1

		
for i in range(0,8):
	time1[i] = time1[i] / 10
	time2[i] = time2[i] / 10
	time3[i] = time3[i] / 10
	
time[0] = time[0]/10
time[1] = time[1]/10
time[2] = time[2]/10

# plotting the points 
plt.semilogx(bits[:-1],time1[:-1], label='TD_MR')
plt.semilogx(bits[:-1],time2[:-1], label='PGCD_MR')
plt.semilogx(bits[:-1],time3[:-1], label='GCD_MR')
plt.xticks([4,8,16,32, 64 ,128 ,256 ,512], (4,8,16,32, 64 ,128 ,256 ,512))
#plt.xticks([32, 64, 128, 256, 512, 1024, 2048, 4096], (32, 64, 128, 256, 512, 1024, 2048, 4096))
# naming the x axis 
plt.xlabel('Number of bits in generated prime') 
# naming the y axis 
plt.ylabel('Time in sec') 
# giving a title to my graph 
plt.title('Comparison of Running time of TD-MR, GCD-MR and PGCD-MR') 
plt.legend()
  
# function to show the plot 
plt.show()

plt.title('Comparison of Running time of TD-MR, GCD-MR and PGCD-MR in generating 4,8,16,32,64,128,256,512 bit primes numbers') 
plt.ylabel('Time in sec') 
plt.bar([0,1,2], time)
plt.xticks([0,1,2], ('TD-MR','PGCD-MR','GCD-MR'))
plt.show()