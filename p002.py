N = 4000000
s = 0
a = 1
b = 2
even_sum = 2

while True:
    s = a + b
    if s<N:
        if s%2==0:
            even_sum += s
        a = b
        b = s
    else:
        break
print(even_sum)

