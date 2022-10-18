#1
def f(сс, numb):
    res = ''
    while numb > 0:
        a = numb % cc
        res += str(a)
        numb //= cc
    return res[::-1]

numb = int(input('Пожалуйста, введите целое число: '))
cc = int(input('Пожалуйста, введите основание системы (2 или 8): '))
print(f(cc, numb))