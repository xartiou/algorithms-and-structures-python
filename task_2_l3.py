# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# Создаем счетчик элементов для второго массива.
from random import randint
N = 5
arr_1 = [0] * N
even_2 = []
# В цикле перебираем все элементы первого массива.
# Если элемент четный, то
# заносим его индекс в очередную ячейку второго массива,
# увеличиваем на 1 значение счетчика элементов второго массива.
for i in range(N):
    arr_1[i] = randint(1, 19)
    if arr_1[i] % 2 == 0:
        even_2.append(i)
# Выводим на экран элементы второго массива от первого до последнего,
# на индекс которого указывает счетчик элементов второго массива.
print(arr_1)
print('Индексы четных элементов: ', even_2)