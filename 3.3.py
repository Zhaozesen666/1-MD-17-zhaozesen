def check_rare_word():
    word = input("Введите слово: ")
    if 'ф' in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

check_rare_word()
