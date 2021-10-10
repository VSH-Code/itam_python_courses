a = [n for n in input()]
if len(a) >= 6:
    print(a.pop(3), a.pop(4))
else:
    print(a[::-2])
