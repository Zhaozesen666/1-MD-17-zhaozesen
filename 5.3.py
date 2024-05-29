days_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')

num_weekends = int(input("Сколько выходных дней на неделе вы хотите? "))

last_index = len(days_of_week) - 1

weekends = days_of_week[last_index - num_weekends + 1:]

workdays = days_of_week[:last_index - num_weekends + 1]

print("Ваши выходные дни:", ", ".join(weekends))
print("Ваши рабочие дни:", ", ".join(workdays))