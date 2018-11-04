# Number Theory And Cryptography (CO313): Paper-Implementation

## **Members:**

Siddesh LC (16CO144) - <siddeshlc8@gmail.com>

Shreyas Pandith (16CO142) - <shreyaspandith98@gmail.com>

## **Paper Selected For Implementation:**

Fast prime generation algorithms using proposed GCD test on mobile smart devices.

## **Abstract:**

As mobile smart devices are widely used, mobile security becomes more and more important. However, the performance of these devices are not powerful enough to use the
same security algorithms as PC’s. Public key cryptosystem such as RSA needs big primes to enhance the security, however, a generating big primes takes a substantial time even on a PC.
In this paper, we proposed two prime generation algorithms for mobile smart devices using GCD primality test. We analyzed and compared the running times of our algorithm with the widely
used TD-MR combination on Samsung Galaxy Tab 10.1. The experimental results showed only a 2% error and our algorithm is about 20% faster than the TD-MR combination.

##  Algorithms:


The procedure of TD-MR combination is as follows :

TD-MR Combination(n, k)
1) Random Number Generation
- Generate an n-bit odd random number r.
2) Trial division on r with k primes
- Divides r by k small primes.
- If r is divided by any prime, go to Step 1.
3) Miller-Rabin test on r
- Perform Miller-Rabin Test on r.
- If r passes, return r as a prime.
- Otherwise, go to Step 1.

The procedure of PGCD-MR combination is as follows :

PGCD-MR Combination(n, k)
1) Random Number Generation
- Generate an n-bit odd random number r.
2) GCD test on r and Πk
- Computes GCD(r, Πk)
- If the result is not 1, go to Step 1.
3) Miller-Rabin test on r
- Perform Miller-Rabin Test on r.
- If r passes, return r as a p


The procedure of MGCD-MR combination is as follows :

MGCD-MR Combination(n, k)
1) Random Number Generation
- Generate an n-bit odd random number r.
2) GCD test on r and Πkj
- Divide Πk into the proper length of Πkj
- Computes GCD(r, Πkj ) sequentially
- If any result is not 1, go to Step 1.
3) Miller-Rabin test on r
- Perform Miller-Rabin Test on r.
- If r passes, return r as a prime.
- Otherwise, go to Step 1.
## **Objectives:**

- Implementing The Improved Algorithms proposed.

- Comparing the Algorithms Proposed by Author.


**References:**

- [Fast Prime Generation Algorithms using proposed GCD test on Mobile Smart Devices](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7425951&tag=1)

## **File Structure**

