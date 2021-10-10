a = [int(n) for n in input().split()]
minn = float("inf")
maxx = 0
for n in a:
    if n >= maxx:
        maxx = n
    if n <= minn:
        minn = n
print(maxx, minn)
