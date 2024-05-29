group1 = ["Иванов", "Петров", "Сидоров", "Козлов", "Смирнов", "Васильев", "Морозов", "Новиков", "Федоров", "Макаров"]
group2 = ["Кузнецов", "Воробьев", "Борисов", "Сергеев", "Попов", "Лебедев", "Козлов", "Никитин", "Соловьев", "Белов"]


sports_team = tuple(group1[:5] + group2[:5])


print("Группа 1:", group1)
print("Группа 2:", group2)
print("Спортивная команда:", sports_team)


print("Длина кортежа:", len(sports_team))


sorted_team = sorted(sports_team)
print("Отсортированная команда:", sorted_team)


ivanov_count = sorted_team.count("Иванов")
print("Студент Иванов входит в команду:", ivanov_count, "раз(а)")