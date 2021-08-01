# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections


def task_section(task):
    print(f'\n{"":-^10} №{task} {"":-^10}')


count_companies = int(input('Введите кол-во компаний: '))

companies = []

for i in range(count_companies):
    title = input('Введите название компании: ')
    profit_q1, profit_q2, profit_q3, profit_q4 = map(int, input('Квартальные прибыли через пробел: ').split(' '))
    company = {
        'title': title,
        'profit_q1': profit_q1,
        'profit_q2': profit_q2,
        'profit_q3': profit_q3,
        'profit_q4': profit_q4,
        'profit_year': profit_q1 + profit_q2 + profit_q3 + profit_q4,
    }

    companies.append(company)

profit_col = collections.Counter()
for company in companies:
    profit_comp = company.copy()
    del profit_comp['title']
    profit_col += collections.Counter(profit_comp)

print()
for company in companies:
    print(company)

average_profit = profit_col['profit_year'] / len(companies)

print('Суммарная прибыль компаний: ', profit_col)
print('Средняя годовая прибыль компаний: ', average_profit)
print('Прибыль выше среднего: ', [x['title'] for x in companies if x['profit_year'] >= average_profit])
print('Прибыль ниже среднего: ', [x['title'] for x in companies if x['profit_year'] < average_profit])
