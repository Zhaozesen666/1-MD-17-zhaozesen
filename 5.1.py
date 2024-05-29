numbers = [3, 8, 15, 22, 42]

user_number = int(input("Введите число: "))

if user_number in numbers:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")

print("Список:", numbers)
print("Ваше число:", user_number)