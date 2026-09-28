# Create a prime_finder() function that takes in a number, n, 
# and returns all the prime numbers from 1 to n (inclusive). 
# As a reminder, a prime number is a number that is only divisible by 1 and itself.
# Challenge described by Codecademy 
# Completed by Mara Brandsen from scratch, no AI usage

import time

start = time.time()

def prime_test(k):
  candiv = []
  cannot = []
  
  for i in range(2, k + 1):
    if k % i == 0:
      candiv.append(i)
    else:
      cannot.append(i)

  if len(candiv) == 1:
    return True
  else:
    return False

  

def prime_finder(n):
  primes = []
  
  for i in range(1, n+1):
    if prime_test(i) == True:
      primes.append(i)
  
  return primes

 
print(prime_finder(11901))

end = time.time()
print(f'Elapsed: {end - start:.2f} seconds')
