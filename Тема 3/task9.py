salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев
month_list = (list(range(1, months+1)))
counter = 0
for i in month_list:
    cap_per_month = spend * ((1 + increase) ** counter) - salary
    money_capital += cap_per_month
    counter += 1
# TODO Оформить решение

print(round(money_capital))
