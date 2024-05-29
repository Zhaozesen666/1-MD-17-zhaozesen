def check_divisibility_by_7(number):
    if number % 7 == 0:
        return True
    else:
        return False


num = int(input("ведите число:"))
if check_divisibility_by_7(num):
    print(f"{num}введенное число на 7")
else:
    print(f"{num}не введенное число на 7")
