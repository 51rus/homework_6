"""После этого программа выбирает первое слово из списка, перемешивает буквы и
предлагает пользователю его отгадать."""

def load_words(filename):
    lines = ""
    with open(filename, "r", encoding="etf-8") as f:
        lines = f.readlines()
    print(lines)
