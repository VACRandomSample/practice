from random import randint
dct = {}
while True:
    group = randint(1, 100000)
    fio = str(input('Введите фамилию студента или 0 для завершения ввода '))
    if fio == '0': break
    dct[group] = fio
print(dct)
dct_s = sorted(dct.items(), key=lambda x: x[0])
print(dct_s)