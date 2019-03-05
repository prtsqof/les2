import math


#Task 1

class Figure ():
    def __init__(self, a_a, a_b, b_a, b_b, c_a, c_b):
        self.a_a = a_a
        self.a_b = a_b
        self.b_a = b_a
        self.b_b = b_b
        self.c_a = c_a
        self.c_b = c_b
        self.AB = round(math.sqrt(int(math.fabs(((b_b - a_b) ** 2) + ((b_a - a_a) ** 2)))), 2)
        self.BC = round(math.sqrt(int(math.fabs(((c_b - b_b) ** 2) + ((c_a - b_a) ** 2)))), 2)
        self.CA = round(math.sqrt(int(math.fabs(((a_b - c_b) ** 2) + ((a_a - c_a) ** 2)))), 2)


    def per(self):
        self.per = (self.AB + self.BC + self.CA)
        return (self.per)

    def plo(self):
        self.per /=2
        self.plo =  round(math.sqrt(self.per*(self.per - self.AB)*(self.per - self.BC)* (self.per - self.CA)),2)
        return (self.plo)

    def hig(self):
        self.plo *=2
        self.hig =  round((self.plo / self.CA),2)
        return (self.hig)


possible = Figure(2,2,5,8,7,4)


print('side length АВ = {}, ВС = {}, СА = {}'.format(possible.AB, possible.BC, possible.CA))
print('perimeter of a triangle АВС {}'.format(possible.per()))
print('area of triangle {}'.format(possible.plo()))
print('higth of a triangle from corner АВС {}'.format(possible.hig()))



#Task 2

import math


class Trapeze:
    def __init__(self, a, b, c, d):
 
        try:
            self.AB = round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2), 2)
            self.CD = round(math.sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2), 2)
            self.DA = round(math.sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2), 2)
        except TypeError:
            print('Параметры заданы неправильно')

    def isosceles(self):
        return self.AB == self.CD

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA, 2)

    def area(self):
        if self.isosceles():
            h = math.sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            return round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.perimeter() / 2
            return round((self.BC + self.DA)/abs(self.DA - self.BC) *
                         math.sqrt((p-self.DA)*(p-self.BC) *
                                   (p-self.DA-self.AB) *
                                   (p-self.DA-self.CD)), 2)


trap = Trapeze((-4, 1), (-2, 3), (3, 3), (5, 2))

print('DA and BC\n являетс: {0}\n'
      'с S {1} P {2} '
      'см'.format(trap.isosceles(), trap.area(), trap.perimeter()))


#Normal 
class School:
    def __init__(self, school_name, school_adress, teachers, students):
        self._school_name = school_name
        self._school_adress = school_adress
        self._teachers = teachers
        self._students = students

    def get_all_classes(self):
        classes = set([student.get_class_room for student in self._students])
        return list(sorted(classes, key=lambda x: int(x[:-1])))

    def get_students(self, class_room):
        return [student.get_short_name for student in self._students if
                class_room == student.get_class_room]

    def get_teachers(self, class_room):
        return [teacher.get_short_name for teacher in self._teachers if
                class_room in teacher.get_classes]

    def find_student(self, student_full_name):
        for person in self._students:
            if student_full_name == person.get_full_name:
                teachers = [teachers.get_short_name for teachers in
                            self._teachers if person.get_class_room in
                            teachers.get_classes]
                lessons = [teachers.get_courses for teachers in
                           self._teachers if person.get_class_room in
                           teachers.get_classes]
                parents = person.get_parents

                return {
                    'full_name': student_full_name,
                    'class_room': person.get_class_room,
                    'teachers': teachers,
                    'lessons': lessons,
                    'parents': parents
                    }

    @property
    def name(self):
        return 'Муниципальное образовательное учреждение ' \
               '"{}"'.format(self._school_name)

    @property
    def adress(self):
        return '{}'.format(self._school_adress)


class People:
    def __init__(self, last_name, first_name, middle_name):
        self._last_name = last_name
        self._first_name = first_name
        self._middle_name = middle_name

    @property
    def get_full_name(self):
        return '{0} {1} {2}'.format(self._last_name,
                                    self._first_name,
                                    self._middle_name)

    @property
    def get_short_name(self):
        return '{0} {1}.{2}.'.format(self._last_name,
                                     self._first_name[:1],
                                     self._middle_name[:1])


class Student(People):
    def __init__(self, last_name, first_name, middle_name,
                 class_room, mather, father):
        People.__init__(self, last_name, first_name, middle_name)
        self._class_room = class_room
        self._parents = {
            'mather': mather,
            'father': father
            }

    @property
    def get_class_room(self):
        return self._class_room

    @property
    def get_parents(self):
        return self._parents


class Teacher(People):
    def __init__(self, last_name, first_name, middle_name,
                 courses, classes):
        People.__init__(self, last_name, first_name, middle_name)
        self._courses = courses
        self._classes = classes

    @property
    def get_courses(self):
        return self._courses

    @property
    def get_classes(self):
        return self._classes


teachers = [
    Teacher('Жукова', 'Людмила', 'Александровна', 'Математика',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Белик', 'Вячеслав', 'Валерьевич', 'Информатика',
            ['10А', '10Б', '11А', '11Б']),
    Teacher('Лакина', 'Надежда', 'Фёдоровна', 'История',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Мордвинова', 'Татьяна', 'Владимировна', 'Литература',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б', '10А', '10Б', '11А', '11Б']),
    Teacher('Лагута', 'Татьяна', 'Ивановна', 'География',
            ['7А', '7Б', '8А', '8Б', '9А', '9Б'])
    ]

students = [
    Student('Юрин', 'Александр', 'Александрович', '10Б',
            'Юрина О. А.', 'Юрин А. В.'),
    Student('Пантелеев', 'Евгений', 'Алексеевич', '11А',
            'Пантелеева Т.В.', 'Пантелеев А.В.'),
    Student('Мотовилов', 'Константин', 'Сергеевич', '11Б',
            'Мотовилова А.Д.', 'Мотовилов С.А.'),
    Student('Патосин', 'Виталий', 'Николаевич', '10А',
            'Патосина А.К.', 'Патосин Н.В.'),
    Student('Бочкин', 'Артём', 'Александрович', '9Б',
            'Бочкина В.А.', 'Бочкин А.Т'),
    Student('Никитин', 'Никита', 'Никитыч', '9А',
            'Никитина Н.А.', 'Никитин Н.С.'),
    Student('Ягодина', 'Дарья', 'Александровна', '8Б',
            'Ягодина А.В.', 'Ягодин А.С.'),
    Student('Панфилов', 'Андрей', 'Васильевич', '8А',
            'Панфилова Е.В.', 'Панфилов В.С.'),
    Student('Андреева', 'Анна', 'Владимировна', '7Б',
            'Андреева А.Д.', 'Андреев В.А.'),
    Student('Сливкин', 'Михаил', 'Аркадьевич', '7А',
            'Сливкина А.Г.', 'Сливкин А.С.'),
    Student('Циганков', 'Александр', 'Сергеевич', '10Б',
            'Цыгакова О. А.', 'Циганков С. В.'),
    Student('Цыганков', 'Алексей', 'Сергеевич', '11А',
            'Цыгакова О. А.', 'Циганков С. В..'),
    Student('Макарова', 'Ирина', 'Александровна', '11Б',
            'Макарова А.Д.', 'Макаров А.А.'),
    Student('Кравченко', 'Александр', 'Владимирович', '10А',
            'Кравченко Е.К.', 'Кравченко В.В.'),
    Student('Беляева', 'Мария', 'Вячеславовна', '9Б',
            'Беляева В.А.', 'Беляев В.Т'),
    Student('Рыбакова', 'Лидия', 'Константиновна', '9А',
            'Рыбакова Н.А.', 'Рыбаков К.С.'),
    Student('Абрамкин', 'Ярослав', 'Александрович', '8Б',
            'Абрамкина А.В.', 'Абрамкин А.С.'),
    Student('Стенькина', 'Анжелла', 'Васильевна', '8А',
            'Стенькина Е.В.', 'Стенькин В.С.'),
    Student('Садыкова', 'Лилия', 'Владимировна', '7Б',
            'Садыкова А.Д.', 'Садыков В.А.'),
    Student('Андросова', 'Анна', 'Сергеевна', '7А',
            'Андросова А.Г.', 'Андросов С.С.'),
    ]


school = School('Гимназия №8', '630068, г.Новосибирск, '
                'ул.Ученическая 8', teachers, students)

print(school.name)
print(school.adress)

print('\nСписок классов школы:')
print(', '.join(school.get_all_classes()))

print('\nСписок "10Б" класса:')
print('\n'.join(school.get_students('10Б')))

student = school.find_student('Юрин Александр Александрович')
print('\nУченик: {0}\nУчебный класс: "{1}"\n'
      'Учителя: {2}\nПредметы: {3}'.format(student['full_name'],
                                           student['class_room'],
                                           ', '.join(student['teachers']),
                                           ', '.join(student['lessons'])))

print('Родители: {0}, {1}'.format(student['parents']['mather'],
                                   student['parents']['father']))

print('\nКласс: "8А"\nПреподаватели: '
      '{0}'.format(', '.join(school.get_teachers('8А'))))

#da