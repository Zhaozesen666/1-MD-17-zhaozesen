def is_magic_date(date):
    day, month, year = map(int, date.split('.'))
    if day * month == year % 100:
        return True
    else:
        return False


user_date = input("ведите дата (dd.mm.yyyy) : ")
if is_magic_date(user_date):
    print("Магической считается дата")
else:
    print("Не магической считается дата")
