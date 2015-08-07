
# Problem 9: https://projecteuler.net/problem=9
# Find a, b and c that a^2+b^2 = c^2 and a+b+c=1000
import itertools

ab = itertools.combinations(range(1,999), 2)


solution = None
for i in ab:
    a = i[0]
    b = i[1]
    c = 1000-a-b
    if a**2+b**2 == c**2:
        solution = (a,b,c)
        break

print(solution[0]*solution[1]*solution[2])