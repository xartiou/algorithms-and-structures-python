N = 10
rand_numbers = [0]*N
for i in range(N):
    rand_numbers[i] = int(random()*100)
    print(rand_numbers[i],end=' ')
print()
# перебераем элементы и проверяем меньше он или больше предыдущего
min = 0
mx = 0
for i in range(N):
    if rand_numbers[i] < rand_numbers[min]:
        min = i
    elif rand_numbers[i] > rand_numbers[mx]:
        mx = i
# выводим минимальный и выводим максимальный
print('rand_numbers[%d]=%d rand_numbers[%d]=%d' % (min+1, rand_numbers[min], mx+1, rand_numbers[mx]))
# записываем по индексу максимума значение, хранимое в буферной переменной.
b = rand_numbers[min]
rand_numbers[min] = rand_numbers[mx]
rand_numbers[mx] = b
# выводим поменяв местами
for i in range(10):
    print(rand_numbers[i],end=' ')
print()
