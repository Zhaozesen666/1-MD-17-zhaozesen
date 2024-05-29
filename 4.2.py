def divide_300_by_input():
    try:
        user_input = input("ведите число: ")
        number = float(user_input)
        result = 300 / number
        print(f"300 делить{number}равно:{result}")
    except ZeroDivisionError:
        print("Error:не ведите 0")
    except ValueError:
        print("Error: ведите число")

divide_300_by_input()
