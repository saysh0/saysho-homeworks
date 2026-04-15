#task1 Фильтрация по ключевому слову.
# Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и сохраняет их в новый файл.
# Имя нового файла формируется как <keyword>_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Если совпадения не найдены, новый файл не создаётся.
# Используйте файл system_log.txt.
# Пример ввода:
# Введите имя файла для поиска: system_log.txt
# Введите ключевое слово: error
# Пример вывода:
# Строки, содержащие 'error', сохранены в error_system_log.txt.

target_file_user = input('Введите имя файла для поиска: ')
target_word_user = input('Введите ключевое слово: ')
def filter_by_key_word(target_file: str, target_word: str) -> str:
    '''
    Функция принимает относительный или полный путь к файлу, а также ключевое слово для поиска в файле. После обрабатывает линии файла и ищет в них указанное слово,
    а затем создает новый файл называя его <ключевое слово>_<название файла> и передавая в него линии где встретилось указанное слово.)
    :param target_file: Принимает относительный или полный путь к файлу.
    :param target_word: Принимает ключевое слово для поиска в файле.
    :return: Строку со статусом выполнения функции(файл был создан или нет).
    '''
    name_to_create_file = f'{target_word}_{target_file}'
    target_lines = []
    with open(target_file, mode='r', encoding="utf-8") as f:
        for line in f:
            words = line.lower().split()
            clean_words = [clean_words.strip(':,.-!?') for clean_words in words]
            if target_word.lower() in clean_words:
                target_lines.append(line)
    if target_lines:
        with open(name_to_create_file, mode='w', encoding="utf-8") as fa:
            fa.writelines(target_lines)
        return f'Строки, содержащие "{target_word}", сохранены в {name_to_create_file}.'
    else:
        return f'Нет строк, содержащих "{target_word}" в файле {target_file}, файл не был создан.'

try:
    print(filter_by_key_word(target_file_user, target_word_user))
except FileNotFoundError:
    print('Файл не существует')

#task2 Поиск и удаление дубликатов.
# Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
# Имя нового файла формируется как unique_<original_filename>.
# Если файл не существует, программа должна вывести ошибку.
# Исходный порядок строк должен сохраниться.
# Если в файле нет дубликатов, создаётся точная копия файла.
# Используйте файл movies_to_watch.txt.
# Пример ввода:
# Введите имя файла: movies_to_watch.txt
# Пример вывода:
# Дубликаты удалены. Уникальные строки сохранены в unique_movies_to_watch.txt.

target_file_user = input("Введите имя файла: ")
def duplicate_finder_and_remover(target_file: str) -> str:
    with open(target_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    unique_lines_set = set()
    unique_lines = []
    for line in lines:
        if line not in unique_lines_set:
            unique_lines.append(line)
            unique_lines_set.add(line)
    if len(unique_lines) == len(lines):
        new_filename = f"unique_{target_file}"
        with open(new_filename, 'w', encoding='utf-8') as fi:
            fi.writelines(lines)
        return f"Дубликатов не обнаружено. Создана точная копия {new_filename}."
    else:
        new_filename = f"unique_{target_file}"
        with open(new_filename, 'w', encoding='utf-8') as fi:
            fi.writelines(unique_lines)
        return f"Дубликаты удалены. Уникальные строки сохранены в {new_filename}."

try:
    print(duplicate_finder_and_remover(target_file_user))
except FileNotFoundError:
    print('Ошибка: Файл не существует')


