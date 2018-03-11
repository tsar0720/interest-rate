import account

rate = int(input("Введите процентную ставку: "))
money = int(input("Введите сумму: "))
period = int(input("Введите период ведения счета в месяцах: "))

result = account.calculate_income(rate, money, period)
print("Параметры счета:\n", "Сумма: ", money, "\n", "Ставка: ", rate, "\n",
        "Период: ", period, "\n", "Сумма на счете в конце периода: ", result)
