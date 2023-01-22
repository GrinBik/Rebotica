# Класс для хранения выбранного ученика и предмета
class Student:
    def __init__(self):
        self.surname = None
        self.subject = None

# Ведомость учеников
dict = {"surname_1" : {'subject_1' : [1 ,2, 3, 4, 5], 'subject_2' : [1, 2, 3, 4, 5],
                        'subject_3': [1, 2, 3, 4, 5], 'subject_4': [1, 2, 3, 4, 5]},
        "surname_2" : {'subject_1' : [1 ,2, 3, 4, 5], 'subject_2' : [1, 2, 3, 4, 5],
                        'subject_3': [1, 2, 3, 4, 5], 'subject_4': [1, 2, 3, 4, 5]},
        "surname_3" : {'subject_1' : [1 ,2, 3, 4, 5], 'subject_2' : [1, 2, 3, 4, 5],
                        'subject_3': [1, 2, 3, 4, 5], 'subject_4': [1, 2, 3, 4, 5]}}

# Функция для получения всего списка оценок или средней по выбранному предмету
def grades(surname, subject, dict, oper):
    if dict.get(surname) is None:
        print(f'{surname} - нет такого ученика в ведомости!')
        return
    if dict[surname].get(subject) is None:
        print(f'{subject} - нет такого предмета в ведомости!')
        return
    if oper == 1:
        print(f"Список оценок {surname} ученика по {subject} предмету: {dict[surname][subject]}")
    elif oper == 2:
        ball = sum(dict[surname][subject]) / len(dict[surname][subject])
        print(f"Средняя оценка у {surname} ученика по {subject} предмету: {ball}")
    else:
        print('Команда не найдена! Повторите, пожалуйста, попытку...')


if __name__ == '__main__':
    student = Student()
    close_prog = 'нет'
    flag = 'нет'

    while True:

        while flag != 'да':
            flag = input('Хотите посмотреть ведомость ученика? ').lower()
            if flag == 'нет':
                close_prog = input("Завершить программу? ").lower()
            if close_prog == 'да':
                break
        if close_prog == 'да':
            break

        flag = 'нет'
        student.surname = input("Ведомость какого ученика Вы хотите посмотреть? ").lower()
        student.subject = input("По какому предмету Вас интересуют оценки? ").lower()

        while True:
            print("1 - все оценки, 2 - средняя оценка, 3 главное меню.")
            try:
                oper = int(input("Что выполнить? "))
            except TypeError:
                print('Команда не найдена! Повторите, пожалуйста, попытку...')
                continue
            else:
                if oper == 3:
                    break
                else:
                    grades(student.surname, student.subject, dict, oper)
