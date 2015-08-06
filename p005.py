
# Problem 5: https://projecteuler.net/problem=5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from numpy import array, where, in1d
from p003 import primes
from functools import reduce

numbers = array(range(2,20+1))
myprimes = primes(20)
factors = []

for prime in myprimes:
    had_division = True
    while had_division:
        remainders = numbers%prime
        ix = in1d(remainders, 0)
        had_division = ix.sum() > 0
        if had_division:
            factors.append(prime)
            numbers[where(ix)] = numbers[where(ix)]/prime
print(reduce(lambda x,y: x*y, factors))