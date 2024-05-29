def join_words():
    words = input("Введите слова через пробел: ")
    result = " ".join(words.split())
    print("Результат:", result)

join_words()