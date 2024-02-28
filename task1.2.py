seat_number = int(input("Введите номер места"))
if seat_number % 2 == 0:
    if seat_number % 4 == 0 or seat_number % 4 == 1:
        print(f"Номер место{seat_number} тип: верхний")
    else:
        print(f"Номер место{seat_number} тип: нижний")
else:
    if seat_number % 4 == 2 or seat_number % 4 == 3:
        print(f"Номер место{seat_number} тип: купе")
    else:
        print(f"Номер место{seat_number} тип: боковой")

