t = 'true'
f = 'false'
ochno, zaochno, hz = 0, 0, 0
N = int(input())
for str in range(N):
    str = input().lower().split()
    if (str.count(t) + str.count(f)) == 1:
        if str[3] == t: ochno += 1
        else: zaochno += 1
    else:
        if (str[3] == t) or (str[3] == f):
            if str[3] == t: ochno += 1
            else: zaochno += 1
        else: hz += 1
print(ochno, zaochno, hz)
    
