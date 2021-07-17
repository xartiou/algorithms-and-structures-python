# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# - просим пользователя ввести целое трехзначное число
three_digit = int(input('Введите целое трехзначное число: '))

# - выделяем цифры из числа
one_d = three_digit // 100
two_d = (three_digit % 100) // 10
three_d = three_digit % 10

# - сумма цифр числа
sum_of_digits = one_d + two_d + three_d
# - произведение цифр числа
comp_of_digits = one_d * two_d * three_d

# - выводим результат
print(f'Для числа {three_digit} сумма цифр = {sum_of_digits}\nпроизведение цифр = {comp_of_digits}')
