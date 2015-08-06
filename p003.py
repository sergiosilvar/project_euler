
# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

N = 600851475143

def primes(n):
    '''
    Prime numbers up to n generator.
    Source: http://programmingpraxis.com/programming-with-prime-numbers-source-code-in-python/
    '''
    if type(n) != int:
        raise TypeError('must be integer')
    if n < 2:
        raise ValueError('must be greater than one')
    m = (n-1) // 2
    b = [True] * m
    i, p, ps = 0, 3, [2]
    while p*p < n:
        if b[i]:
            ps.append(p)
            j = 2*i*i + 6*i + 3
            while j < m:
                b[j] = False
                j = j + 2*i + 3
        i += 1; p += 2
    while i < m:
        if b[i]:
            ps.append(p)
        i += 1; p += 2
    return ps

if __name__ == '__main__':
    myprimes = primes(int(sqrt(N)))

    for i in myprimes:
        if N%i == 0:
            print(i)