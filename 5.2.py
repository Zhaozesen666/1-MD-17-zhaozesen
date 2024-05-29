my_list = [5, 2, 7, 3, 5, 8, 2, 9]

duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

if duplicates:
    print("Повторяющиеся элементы в списке:", duplicates)
else:
    print("В списке нет повторяющихся элементов.")