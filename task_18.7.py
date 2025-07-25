# удаление оценки для ученика по предмету
print('1. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        mark = int(input('Удалите оценку: ')
        class_ = input('Введите предмет: '))
if student in students_marks.keys() and class_ in students_marks[student].keys():
        students_marks[student][class_].remove(mark)
        print(f'Для {student} по предмету {class_} удалена оценка {mark}')
else:
    print('ОШИБКА: неверное имя ученика или название предмета')

# удаление предмета
print('Удалить предмет')
class_ = input('Введите предмет: ')
if class in classes():
        classes.remove(class_)
        for class_ in classes:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Предмет {class_} удален')
                else:
                    print('ОШИБКА: предмета не существует ')
                        
# удаление ученика
print('Удалить ученика')
student = input('Введите имя: ')
if student in students():
        students.remove(student_)
        for student in students:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Ученик {student_} удален')
                else:
                    print('ОШИБКА: неверное имя ученика ')

# редактирование оценки для ученика по предмету
print('1. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
if student in students_marks.keys() and class_ in students_marks[student].keys():
               students_marks[student][class_].edit(mark)
                print(f'Для {student} по предмету {class_} редактирована оценка {mark}')
else:
    print('ОШИБКА: неверное имя ученика или название предмета')

# редактирование предмета
print('Редактировать предмет')
class_ = input('Введите предмет: ')
if class in classes():
        classes.edit(class_)
        for class_ in classes:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Предмет {class_} редактирован')
                else:
                    print('ОШИБКА: предмета не существует ')

# редактирование ученика

print('Редактировать имя ученика')
student = input('Введите имя: ')
if student in students():
        students.edit(student_)
        for student in students:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Имя ученика {student_} редактировано')
                else:
                    print('ОШИБКА: неверное имя ученика ')

#вывод информации по всем оценкам для определенного ученика
 for student in students:
                print(student)
                # цикл по предметам
                for class_ in classes:
                    print(f'\t{class_} - {students_marks[student][class_]}')
                print()

#вывод среднего балла по каждому предмету по определенному ученику
            for student in students:
                print(student)
                # цикл по предметам
                for class_ in classes:
                    # находим сумму оценок по предмету
                    marks_sum = sum(students_marks[student][class_])
                    # находим количество оценок по предмету
                    marks_count = len(students_marks[student][class_])
                    # выводим средний балл по предмету
                    print(f'{class_} - {marks_sum//marks_count}')
                print()


# добавление предмета
print('Добавить предмет')
class_ = input('Введите новый предмет: ')
if class in classes():
        classes.append(class_)
        for class_ in classes:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Новый предмет {class_} добавлен')
                else:
                    print('ОШИБКА: Предмет уже существует ')


# добавление ученика
print('Добавить нового ученика')
student = input('Введите имя: ')
if student in students():
        students.append(student_)
        for student in students:
        marks = [random.randint(a:1, b:5) for i in range(3)]
        students_marks[student][class_] = marks
        print(f' Новый ученик {student_} добавлен')
                else:
                    print('ОШИБКА: имя ученика уже существует ')

