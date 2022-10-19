#1
def f(сс, numb):
    res = ''
    while numb > 0:
        ost = numb % cc
        res += str(ost)
        numb //= cc
    return res[::-1]

numb = int(input('Пожалуйста, введите целое десятичное число: '))
cc = int(input('Пожалуйста, введите основание системы (2 или 8): '))
print(f(cc, numb))