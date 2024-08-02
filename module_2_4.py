numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []                 #простые числа
not_primes = []        #непростые числа
for i in range(2,len(numbers) + 1):
    k = 0
    for j in range(1, i + 1):
        if i % j == 0:
            k += 1
            if k > 2:
                break
    if k == 2:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)



