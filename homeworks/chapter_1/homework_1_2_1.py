N = int(input())
ochno, zaochno = 0, 0
for a in range(N):
    a = input().split()
    if a[3] == 'True': ochno += 1
    else: zaochno += 1
print(ochno, zaochno)
    
