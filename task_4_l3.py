# 4. Определить, какое число в массиве встречается чаще всего.

# формируем массив для обработки
from random import random
N = 20
arr = [0] * N
for i in range(N):
    arr[i] = int(random() * 20)
print(arr)

# создаем переменную для записи самого встречаемого элемента массива
num = arr[0]
# создаем переменную для подсчета количества раз встречаемости
max_frq = 1
# в цикле перебераем элементы начиная с первого и сравниваем с предыдущим
for i in range(N-1):
    frq = 1
    for k in range(i+1,N):
        if arr[i] == arr[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = arr[i]

# результат выводим
if max_frq > 1:
    print(max_frq, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
