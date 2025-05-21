def gen_func(x):
    print('입력값')
    yield x

    print('입력값 + 1')
    x += 1
    yield x

    print('입력값 + 2')
    x += 1
    yield x

gen_func(1)

for i in gen_func(1):
    print(i)