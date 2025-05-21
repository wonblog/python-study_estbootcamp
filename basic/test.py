def get_lengths(lst):
    result = []
    for item in lst:
        if type(item) == str:   
            result.append(len(item))  
    return result
li = ['apple', 'banana', 3, ['cherry', 'kiwi'], 'strawberry']
print(get_lengths(li))

ct = 5
for i in range(1, ct + 1):
    sp = ct - i
    st = 2 * i - 1
    print(" " * sp + "*" * st)




year = int(input("연도를 입력하세요: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print('윤년')
else:
    print('평년')


def dict_to_list(d):
    return list(d.items())
dic = {'a': 1, 'b': 2, 'c': 3}
print(dict_to_list(dic))

def lens(lst):
    result = []
    for item in lst:
        if type(item) == str:   
            result.append(len(item))  
    return result
li = ['apple', 'banana', 3, ['cherry', 'kiwi'], 'strawberry']
print(lens(li))
