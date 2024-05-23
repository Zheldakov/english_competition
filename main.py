import utils as ut

name = input ("Введите ваше имя: ")
level = input(
    "Введите уровень сложности: 1 - Легкий, 2- Средний, 3 - Сложный, другое - для выхода из программы: ")

if level not in ["1", "2", "3"]:
    print("Вы вышли из программы")
    quit()

dict_words= ut.get_user_level(level)

answer=ut.base_program(dict_words,name)

ut.get_result(answer)