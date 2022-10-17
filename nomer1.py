#1
def f(сс):
    res = ''
    while chiclo10 > 0:
        a = chiclo10 % cc
        res += str(a)
        chiclo10 //= cc
        return res[::-1]

chiclo10 = int(input('Пожалуйста, введите целое число: '))
cc = int(input('Пожалуйста, введите основание системы (2 или 8): '))
print(res[::-1])