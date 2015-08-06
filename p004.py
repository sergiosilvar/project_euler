
# Problem 4: https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
import itertools

def is_palindrome(number):
    number = str(number)
    n = len(number)
    j = int(n/2)
    for i in range(j):
        left = number[i]
        right = number[-1*(i+1)]
        if left != right: 
            return False
    return True    


numbers = [i[0]*i[1] for i in itertools.combinations(range(100,999), 2)]
numbers = sorted(numbers, reverse=True)
for i in numbers:
    if is_palindrome(i):
        print(i)
        break