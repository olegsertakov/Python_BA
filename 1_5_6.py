revenue = float(input('Введите значение выручки = '))
costs = float(input('Введите значение издержек = '))
if revenue >= costs:
    profit = revenue - costs
    print('Прибыль равна = ', profit)
    rentabel = profit / revenue
    personal = int(input('Введите численность персонала фирмы = '))
    profit_1 = profit / personal
    print('Прибыль на одного сотрудника равна = ', "%.2f" % profit_1)
else:
    loss = costs - revenue
    print('Убыток равен = ', loss)