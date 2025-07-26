import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удалить оценки ученика по предмету
        5. Удалить предмет
        6. Удалить ученика
        7. Редактировать оценку ученика по предмету
        8. Редактировать предмет
        9. Редактировать имя ученика
        10. Добавить предмет
        11. Добавить нового ученика
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].remove(mark)
            print(f'Для {student} по предмету {class_} удалена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 5:
        print('5. Удалить предмет')
        for class_ in classes:
            classes.remove(class_)
            print(f' Предмет {class_} удален')
        else:
            print('ОШИБКА: предмета не существует ')
    elif command == 6:
        print('6. Удалить ученика ')
        if student in students:
            students.remove(student)
        print(f' Ученик {student} удален')
    else:
            print('ОШИБКА: неверное имя ученика ')

    elif command = 7:
        print('7. Редактировать оценку ученика по предмету')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].edit(mark)
        print(f'Для {student} по предмету {class_} редактирована оценка {mark}')
    else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command = 8:
        print('8. Редактировать предмет')
        if class in classes():
            classes.edit(class_)
        print(f' Предмет {class_} редактирован')
    else:
            print('ОШИБКА: предмета не существует ')

    elif command == 9:
        print('9. Редактировать имя ученика')
        if student in students():
            students.edit(student_)
        print(f' Имя ученика {student_} редактировано')
    else:
            print('ОШИБКА: неверное имя ученика ')

    elif command == 10:
        print('10. Добавить предмет')
        if class in classes():
            classes.append(class_)
        print(f' Новый предмет {class_} добавлен')
        else:
                print('ОШИБКА: Предмет уже существует ')

    elif command == 11:
        print('11. Добавить нового ученика')
        student = input('Введите имя: ')
        if student in students():
            students.append(student_)
        print(f' Новый ученик {student_} добавлен')
    else:
        print('ОШИБКА: имя ученика уже существует ')

    elif command == 12:
        print('12. Выход из программы')
        break
