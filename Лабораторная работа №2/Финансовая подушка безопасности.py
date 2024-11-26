
money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0  # Счетчик месяцев
current_budget = money_capital  # Текущие сбережения

while current_budget + salary >= spend:
    current_budget = current_budget + salary - spend  # Обновляем бюджет
    spend *= (1 + increase)  # Увеличиваем траты
    months += 1  # Увеличиваем счетчик месяцев

print("Количество месяцев, которое можно протянуть без долгов:", months)