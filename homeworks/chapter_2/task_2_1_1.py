def greetings(s):
    a, b = s.split()
    return f'Доброго времени суток, {a} "Человек" {b}!'
    
s = input()
print(greetings(s))
