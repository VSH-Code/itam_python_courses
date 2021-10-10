st = input()
word = []
s = ''
for i in range(len(st)):
    if st[i] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        pass
    else:
        word += [st[i]]
        word += [st[n] for n in range(i + 3, len(st), 3)]
        break
s = s.join(word)
print(s)

