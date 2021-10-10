def debug_control(*args, **let_me_die):
    types = {str : 0, int: 0, float: 0}
    for arg in args:
        try:
            arg = int(arg)
        except:
            try:
                arg = float(arg)
            except:
                pass
        types[type(arg)] += 1
    for key, kwarg in let_me_die.items():
        types[type(kwarg)] += 1
    return types

print(debug_control(*(input().split()), name = "Абоба Гуль Бебрович", age = 1000-7))


