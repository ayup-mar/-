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
for student in students: # 1 итерация: student = 'Александра'
    students_marks[student] = {} # 1 итерация: students_marks['Александра'] = {}
# цикл по предметам
for class_ in classes: # 1 итерация: class_ = 'Математика'
    marks = [random.randint(1,5) for i in range(3)] # генерируем список из 3х случайных оценок
    students_marks[student][class_] = marks # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
    for student in students:
            print(f'''{student}
            {students_marks[student]}''')
