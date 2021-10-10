a = [int(n) for n in input().split()]
k_neg, k_even, k_big = 0, 0, 0

for el in a:
    if el < 0: k_neg += 1
    if el > 8: k_big += 1
    if el % 2 == 0: k_even += 1
print(k_neg, k_big, k_even)
    
