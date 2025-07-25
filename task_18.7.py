print('1. Удалить оценку ученика по предмету')
        # считываем имя ученика
student = input('Введите имя ученика: ')
        # считываем название предмета
class_ = input('Введите предмет: ')
# если данные введены верно
if student in students_marks.keys() and class_ in students_marks[student].keys():
                # удаляем оценку для ученика по предмету
                students_marks[student][class_].append(mark)
                print(f'Для {student} по предмету {class_} удалена оценка {mark}')
# неверно введены название предмета или имя ученика
else:
    print('ОШИБКА: неверное имя ученика или название предмета')
