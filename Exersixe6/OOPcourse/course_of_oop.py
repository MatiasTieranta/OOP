class Course:
    def __init__(self, id, name, school):
        self.__id = id
        self.__name = name
        self.__school = school

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_school(self):
        return self.__school

    def set_school(self, school):
        self.__school = school

        # The __str__ method returns a string indicating the objects state

    def __str__(self):
        return f'''id: {self.__id}
            \nname: {self.__name}
            \nschool: {self.__school}'''


class Students(Course):

    def __init__(self, id, name, school, isStudent, tasksDone, grade):
        super().__init__(id, name, school)
        self.__isStudent = isStudent
        self.__tasksDone = tasksDone
        self.__grade = grade

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.__isStudent + '\nTasks done' + self.__tasksDone + '\nGrade' + self.__grade


class Teachers(Course):

    def __init__(self, id, name, school, isTeacher, cofeeBreaks, salary):
        super().__init__(id, name, school)
        self.__isTeacher = isTeacher
        self.__cofeeBreaks = cofeeBreaks
        self.__salary = salary

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.__isTeacher + '\nHow many cofee breaks he/she had' + self.__cofeeBreaks+ \
               '\nSalary' + self.__salary


markus = Students(' 1', ' Markus', ' Turun AMK', ' a student', ' 11', ' 5')
jonna = Students('2', 'Jonna', 'Turun AMK', 'is a student', '5', '1')

ossi = Teachers(' 11', ' Ossi', ' Turun AMK', ' a teacher', ' 3', ' 2400e')
jaana = Teachers(' 120', ' Jaana', ' Turun AMK', ' a teacher', ' 11', ' 3400e')


print('Here are our students :')
print(markus)
print()
print(jonna)
print()

print('Here are our teachers :')
print(ossi)
print()
print(jaana)