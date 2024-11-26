salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0  # Требуемая подушка безопасности
current_spend = spend  # Траты текущего месяца

for _ in range(months):
    deficit = current_spend - salary  # Нехватка средств в текущем месяце
    if deficit > 0:
        money_capital += deficit  # Добавляем нехватку к подушке
    current_spend *= (1 + increase)  # Увеличиваем расходы на следующий месяц

money_capital = round(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)

