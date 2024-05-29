students_languages = {'Анна': {'Английский', 'Французский', 'Немецкий'}, 'Петр': {'Китайский', 'Английский'},
                      'Мария': {'Испанский', 'Французский'}, 'Иван': {'Китайский', 'Английский', 'Испанский'},
                      'Елена': {'Английский', 'Итальянский'}}

all_languages = {language for languages in students_languages.values() for language in languages}

sorted_languages = sorted(all_languages)
print("Sorted list of all languages:")
print(sorted_languages)

chinese_speakers = [student for student, languages in students_languages.items() if 'Китайский' in languages]
print("\nStudents who know Chinese:")
print(chinese_speakers)
