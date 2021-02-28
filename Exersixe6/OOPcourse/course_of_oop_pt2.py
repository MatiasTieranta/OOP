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

    def __init__(self, id, name, school, is_student, tasks_done, grade):
        super().__init__(id, name, school)
        self.__isStudent = is_student
        self.__tasksDone = tasks_done
        self.__grade = grade

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.__isStudent + '\nTasks done' + self.__tasksDone + '\nGrade' + self.__grade

    def get_is_student(self):
        return self.__isStudent

    def set_is_student(self, is_student):
        self.__isStudent = is_student

    def get_tasks_done(self):
        return self.__tasksDone

    def set_tasks_done(self, tasks_done):
        self.__tasksDone = tasks_done

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade


class DomesticAnimal(Students):

    def __init__(self, id, name, school, is_student, tasks_done, grade, domestic, name_of_domestic):
        super().__init__(id, name, school, is_student, tasks_done, grade)
        self.__isDomestic = domestic
        self.__nameOfDomestic = name_of_domestic

    def get_domestic(self):
        return self.__isDomestic

    def set_domestic(self, domestic):
        self.__isDomestic = domestic

    def get_name_of_domestic(self):
        return self.__nameOfDomestic

    def set_name_of_domestic(self):
        return self.__nameOfDomestic

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.get_is_student() + '\nTasks done' + self.get_tasks_done() + '\nGrade' + self.get_grade() \
               + '\nAnimal is ' + self.__isDomestic + '\nAnimal name is ' + self.__nameOfDomestic


class WildAnimal(DomesticAnimal):
    def __init__(self, id, name, school, is_student, tasks_done, grade, domestic, name_of_domestic, wild, name_of_wild):
        super().__init__(id, name, school, is_student, tasks_done, grade, domestic, name_of_domestic)
        self.__isWild = wild
        self.__nameOfWild = name_of_wild

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.get_is_student() + '\nTasks done' + self.get_tasks_done() + '\nGrade' + self.get_grade() \
               + '\nAnimal is ' + self.get_domestic() + '\nAnimal name is ' + self.get_name_of_domestic() + \
               '\nAnimal is' + self.__isWild + '\nName of wild animal is ' + self.__nameOfWild


class Teachers(Course):

    def __init__(self, id, name, school, is_teacher, cofee_breaks, salary):
        super().__init__(id, name, school)
        self.__isTeacher = is_teacher
        self.__cofeeBreaks = cofee_breaks
        self.__salary = salary

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.__isTeacher + '\nHow many cofee breaks he/she had' + self.__cofeeBreaks + \
               '\nSalary' + self.__salary

    def get_is_teacher(self):
        return self.__isTeacher

    def set_is_teacher(self, is_teacher):
        self.__isTeacher = is_teacher

    def get_cofee_breaks(self):
        return self.__cofeeBreaks

    def set_cofee_breaks(self, cofee_breaks):
        self.__cofeeBreaks = cofee_breaks

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary


class DomesticAnimalOfTeachers(Teachers):

    def __init__(self, id, name, school, is_teacher, cofee_breaks, salary, domestic, name_of_domestic_of_teacher):
        super().__init__(self, id, name, school, is_teacher, cofee_breaks, salary)
        self.__isDomestic = domestic
        self.__nameOfDomestic = name_of_domestic_of_teacher

    def get_domestic(self):
        return self.__isDomestic

    def set_domestic(self, domestic):
        self.__isDomestic = domestic

    def get_name_of_domestic(self):
        return self.__nameOfDomestic

    def set_name_of_domestic(self):
        return self.__nameOfDomestic

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.get_is_teacher() + '\nCofee breaks' + self.get_cofee_breaks() + '\nSalary' + self.get_salary() \
               + '\nAnimal is ' + self.__isDomestic + '\nAnimal name is ' + self.__nameOfDomestic


class WildAnimalOfTeachers(DomesticAnimalOfTeachers):
    def __init__(self, id, name, school, is_teacher, cofee_breaks, salary, domestic, name_of_domestic_of_teacher, wild,
                 name_of_wild):
        super().__init__(self, id, name, school, is_teacher, cofee_breaks, salary, domestic, name_of_domestic_of_teacher)
        self.__isWild = wild
        self.__nameOfWild = name_of_wild

    def __str__(self):
        return 'id' + self.get_id() + '\nname' + self.get_name() + \
               '\nSchool' + self.get_school() + '\nPerson is' + \
               self.get_is_teacher() + '\nCofee breaks' + self.get_cofee_breaks() + '\nSalary' + self.get_salary() \
               + '\nAnimal is ' + self.get_domestic() + '\nAnimal name is ' + self.get_name_of_domestic() + \
               '\nAnimal is' + self.__isWild + '\nAnimal name is' + self.__nameOfWild


markus = WildAnimal(' 1', ' Markus', ' Turun AMK', ' a student', ' 11', ' 5', 'Domestic', 'Cat', ' Wild animal',
                    ' Rhino')

ossi = WildAnimalOfTeachers(' 1', ' Markus', ' Turun AMK', ' a student', ' 11', ' 5', 'Domestic', 'Cat' 'asda', 'asdasd')

print(ossi)
