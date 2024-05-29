def is_lucky_ticket(number):
    if len(number) % 2 != 0:
        return False

    first_half_sum = sum(map(int, number[:len(number) // 2]))

    second_half_sum = sum(map(int, number[len(number) // 2:]))

    return first_half_sum == second_half_sum

print(is_lucky_ticket("545621"))
print(is_lucky_ticket("213321"))