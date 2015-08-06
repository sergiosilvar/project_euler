
# Problem 8: https://projecteuler.net/problem=8
# The four adjacent digits in the 1000-digit number that 
# have the greatest product are 9 × 9 × 8 × 9 = 5832.
# Find the thirteen adjacent digits in the 1000-digit number 
# that have the greatest product. 
# What is the value of this product?
from functools import reduce
N = 13
number = ''
with open('assets/p008.txt', 'r') as f:
    number = f.read()
number = number.replace('\n','')
max_str = ''
max_prod = 0
for i in range(0,len(number)-N+1):
    x_str = number[i:i+N]
    if x_str.find('0') > -1: 
        continue
    x_prod = reduce(lambda x,y: int(x)*int(y), list(x_str))
    if x_prod > max_prod:
        max_prod = x_prod
        max_str = x_str
print('The answer is the sequence "{}" which gives the product {}.'.format(max_str, max_prod))