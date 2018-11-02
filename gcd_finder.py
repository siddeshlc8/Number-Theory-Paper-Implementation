# Python code to demonstrate naive 
# method to compute gcd ( Euclidean algo ) 
  
  
def computeGCD(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x 
  