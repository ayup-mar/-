print('1. Удалить оценку ученика по предмету')
        # считываем имя ученика
student = input('Введите имя ученика: ')
        # считываем название предмета
class_ = input('Введите предмет: ')
# если данные введены верно
if student in students_marks.keys() and class_ in students_marks[student].keys():
                # удаляем оценку для ученика по предмету
                students_marks[student][class_].remove(mark)
                print(f'Для {student} по предмету {class_} удалена оценка {mark}')
# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')



print('1. Редактировать оценку ученика по предмету')
        # считываем имя ученика
student = input('Введите имя ученика: ')
        # считываем название предмета
class_ = input('Введите предмет: ')
# считываем оценку
mark = int(input('Введите оценку: '))
# если данные введены верно
if student in students_marks.keys() and class_ in students_marks[student].keys():
                # редактируем оценку для ученика по предмету
                students_marks[student][class_].edit(mark)
                print(f'Для {student} по предмету {class_} редактирована оценка {mark}')
# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')
