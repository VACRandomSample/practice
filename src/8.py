arr_1 = list(map(int, input().split()))
print('Ваш массив: ',arr_1)
arr_2 = []
m = 0
for j in range(len(arr_1)):
    if arr_1[j] > 0:
        arr_2.append(arr_1[j])
        if arr_1[j] > m:
            m = arr_1[j]
print('Новый массив, состоящий из положительных элементов:', arr_2)
print ('Наибольший элемент массива:', m)
