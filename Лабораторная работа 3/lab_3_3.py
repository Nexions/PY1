money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить

traty = spend * 1.05


# TODO Оформить решение
while money_capital > traty:
    money_capital -= traty
    money_capital += salary
    month +=1
print(month)






