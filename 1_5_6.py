revenue = float(input('Введите значение выручки = '))
costs = float(input('Введите значение издержек = '))
if revenue >= costs:
    profit = revenue - costs
    print('Прибыль равна = ', profit)
    profitability = (profit / revenue) * 100
    print('Рентабельность = ', "%.2f" % profitability, '%')
    personal = int(input('Введите численность персонала фирмы = '))
    profit_1 = profit / personal
    print('Прибыль на одного сотрудника равна = ', "%.2f" % profit_1)
else:
    loss = costs - revenue
    print('Убыток равен = ', loss)