
# What is the largest prime factor of the number 600851475143 ?
from numpy import array
from math import sqrt


N = 600851475143
# https://primes.utm.edu/lists/small/100000.txt
with open('assets/100000.txt', 'r') as f:
    text = f.read()
x = 'see http://primes.utm.edu/\n\n\n\n   '
text = text[text.find(x)+len(x):]
text = text.replace('\n\n', '')
primes = array([int(i.strip()) for i in text.split(' ') if i.strip() != ''])
primes = primes[primes < sqrt(N)]
    
primes = primes[::-1]
for i in primes:
    if N%i == 0:
        print(i)
        break