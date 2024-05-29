def join_words():
    result = ""
    word = input("Введите слово (для завершения введите 'stop'): ")

    while word.lower() != "stop":
        result += word + " "
        word = input("Введите следующее слово (для завершения введите 'stop'): ")

    result = result.strip()

    print("Результат:", result)

join_words()