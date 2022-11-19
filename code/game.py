# Импортируем модуль рандом для работы с функцией change_word(word)
import random


def load_words(filename):
    """Загружает слово из файла"""
    new_lines = []
    # Открываем файл на чтение с учетом языка(кодировка)
    with open(filename, "r", encoding="utf-8") as f:
        # Считываем построчно
        for line in f.readlines():
            # Добавляем в новый список строчку, удаляя символ новой строки, если он есть
            new_lines.append(line.strip("\n"))
    return new_lines


def change_word(word):
    """Меняет буквы в словах"""
    # Привели word к типу list, чтобы работать с random.shuffle
    word = list(word)
    random.shuffle(word)
    # Объединение, чтобы снова была строчка
    return "".join(word)


def write_history(filename, user_name, points):
    """Запись в файл имя пользователя и очков"""
    with open(filename, "a", encoding="utf-8") as f:
        # Добавление символа новой строки \n
        f.write(f"{user_name} {points}\n")


def read_history(filename):
    """Определяет колличество игр и максимальный рекорд"""
    # Максимальный рекорд
    max = 0
    # Колличество игр
    games = 0
    with open(filename, "r", encoding="utf-8") as f:
        # Считываем файл построчно
        for line in f.readlines():
            games += 1
            # Вычисление максимального колличества очков записанных в файле
            # Делим строчку по пробелу line.split(" ") и берем второй элемент
            # Переводим тип строки к типу int
            points = int(line.split(" ")[1])
            if points > max:
                max = points
    return f"Всего игр сыграно: {games}\n" \
           f"Максимальный рекорд: {max}"


# Названия файлов с которыми будем работать
words_txt = "words.txt"
history_txt = "history.txt"

# Ввод данных от пользователя
user_name = input("Введите ваше имя: ")

# Загрузка слов в переменную words
words = load_words(words_txt)

# Колличество очков
points = 0

# Цикл прохода по словам
for word in words:
    # Вывод перемешанного рандомного слова
    print(change_word(word))
    user_answer = input("Угадайте слово: ")
    # Сравнение ответа пользователя с  word, с учетом регистра и пробелов
    if user_answer.lower().strip(" ") == word:
        points += 10
        print("Верно! Вы получаете 10 очков.")
    else:
        print(f"Неверно! Верный ответ – {word}.")

# Вывод результатов
write_history(history_txt, user_name, points)
print(read_history(history_txt))
