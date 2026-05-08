#task1 Класс Person.
# Создайте класс Person, представляющий человека.
# Каждый человек должен иметь имя.
# Добавьте метод introduce(), который выводит приветствие с именем.
from os import name

class Person:
    """
    Класс, представляющий человека.
    """
    def __init__(self, name: str) -> None:
        """
        Инициализирует новый экземпляр человека.
        :param name: Имя человека.
        """
        self.name = name

    def introduce(self):
        return f"Whatsup ma boy {self.name}"

#task2 Класс Student.
# На основе класса Person создайте класс Student.
# Студент должен иметь имя и номер курса.
# Метод introduce() должен сначала выводить базовое приветствие, а затем строку: I'm on course <номер_курса>.
# Пример вывода:

class Person:
    """
    Класс, представляющий человека.
    """
    def __init__(self, name) -> str:
        """
        Инициализирует новый экземпляр человека.
        :param name: Имя человека.
        """
        self.name = name

    def introduce(self) -> str:
        return f'Whatsup ma boy {self.name}'

class Student(Person):
    def __init__(self, name, course_nummer) -> None:
        """
        Инициализирует новый экземпляр студента.
        :param name: Имя человека.
        :param course_nummer: Номер курса.
        """
        super().__init__(name)
        self.course_nummer = course_nummer

    def introduce(self) -> str:
        return f"Whatsup ma boy {self.name}\nI'm on course {self.course_nummer}"

student1 = Student("Nikita", 1)
print(student1.introduce())
student2 = Student("Igor", 2)
print(student2.introduce())
student3 = Student("Vlad", 3)
print(student3.introduce())

#task3 Класс Teacher и список людей.
# На основе класса Person создайте класс Teacher.
# У преподавателя есть имя и предмет.
# Метод introduce() должен выводить имя и предмет.
# Метод introduce() должен выводить строку: Hello, I am professor <имя>. My subject is <предмет>.
# Создайте список, в котором будут Student и Teacher, и вызовите у всех метод introduce().

class Person:
    def __init__(self, name) -> None:
        """
        Инициализирует новый экземпляр человека.
        :param name: Имя человека.
        """
        self.name = name

    def introduce(self) -> str:
        return f'Whatsup ma boy {self.name}'

class Student(Person):
    def __init__(self, name, course_nummer) -> None:
        """
        Инициализирует новый экземпляр студента.
        :param name: Имя человека.
        :param course_nummer: Номер курса.
        """
        super().__init__(name)
        self.course_nummer = course_nummer

    def introduce(self) -> str:
        return f"Whatsup ma boy {self.name}\nI'm on course {self.course_nummer}"

class Teacher(Person):
    def __init__(self, name, subject) -> None:
        """
        Инициализирует новый экземпляр студента.
        :param name: Имя человека.
        :param subject: Название предмета.
        """
        super().__init__(name)
        self.subject = subject

    def introduce(self) -> str:
        return f"Hello, I am professor {self.name}. My subject is{self.subject}."

student1 = Student("Nikita", 1)
student2 = Student("Igor", 2)
teacher1 = Teacher("Oleg", 'Python')
teacher2 = Teacher("Julian", 'SQL')

spisok = []
spisok.append(student1)
spisok.append(student2)
spisok.append(teacher1)
spisok.append(teacher2)
for s in spisok:
    print(s.introduce())


