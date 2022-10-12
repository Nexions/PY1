salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
bank = 0
rost = 0
need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months > 0:
    if months == 10:
        bank += salary
        bank -=spend
        rost += spend
        months -= 1
    else:
        bank += salary
        rost *= 1.03
        bank -= rost
        months -=1
need_money = -bank
# TODO Оформить решение

print(round(need_money))
