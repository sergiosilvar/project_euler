
# Problem 7: https://projecteuler.net/problem=7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
#  we can see that the 6th prime is 13.
# What is the 10 001st prime number?
from p003 import primes
from math import log
n_th = 10001

def pi(x):
    '''
    Estimate the number os primes under x.
    Source: https://primes.utm.edu/howmany.html
    '''
    return int(x/(log(x)-1))


N = 120000
print('Numbers os primes under {} is {}.'.format(N, pi(N)))
myprimes = primes(N)

print('The {} prime is {}.'.format(n_th, myprimes[n_th-1]))