a = 100
b = 3
p1 = p2 = 1
for i in range(1,a+1):
    p1 = p1 * i
for j in range(1,a+1-b):
    p2 = p2 * j
print ('Количество перестановок: ', p1/p2)
print ('Шанс угадать выигрышный лотерейный билет: ', 1 / (p1 / p2))