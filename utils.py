import json
import os
from datetime import datetime, date


def get_user_level(level):
    '''Функция принемает уровень сложности, и возвращает словарь слов в соответствующей сложности'''

    with open(os.path.normpath(os.path.abspath("questions/questions.json")), "rt", encoding="utf-8") as file:
        data_json = json.loads(file.read())
        words_easy = data_json[0]["questions"][0]
        words_medium = data_json[0]["questions"][1]
        words_hard = data_json[0]["questions"][2]
        words = {
            1: words_easy,
            2: words_medium,
            3: words_hard
        }
        dict_words = words[int(level)]
    return dict_words


def base_program(dict_words, name):
    '''Функция принемает словарь слов, спрашивает пользователя вопросы по данному словарю,  возвращает ответы с значениями True и Fals а также создает файл с ответами'''
    answer = {}
    for word_eng, word_rus in dict_words.items():
        answer_word = input(f"Введите превод слова {word_eng}, подсказка: слово имеет {len(word_rus)} букв, начинается с буквы '{word_rus[0]}..' :").strip().lower()
        if answer_word == word_rus:
            print(f"Верно, {word_eng.title()} — это {word_rus}.")
            answer[word_eng] = True
        else:
            print(f"Не верно, {word_eng.title()} — это {word_rus}.")
            answer[word_eng] = False
        answer_json = json.dumps(answer)
    with open(os.path.normpath(os.path.abspath(f"answer_{name}_{date.today()}_{datetime.now().strftime("%H-%M-%S")}.json")), "wt", encoding="utf-8") as file:
        file.write(answer_json)
    return answer


def get_result(answer):
    '''Функция получает словарь с ответсами, и возвращает результат прохождения викторины'''
    count = 0
    with open(os.path.normpath(os.path.abspath("questions/questions.json")), "rt", encoding="utf-8") as file:
        data_json = json.loads(file.read())
        levels = data_json[1]["levels"]

    print("Правильно отвечены слова:")
    for word, status in answer.items():
        if status == True:
            count += 1
            print(word)

    print("Неправильно отвечены слова:")
    for word, status in answer.items():
        if status == False:
            print(word)

    print(f"Ваш ранг:\n{levels[str(count)]}")
