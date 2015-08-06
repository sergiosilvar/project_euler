N = 1000
multiples = []
for i in range(N):
    if i%3 == 0 or i%5 == 0:
        multiples.append(i)
    
x = sum(multiples)
print(x)