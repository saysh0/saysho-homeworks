#task1 Фигуры и площади.
# Создайте абстрактный класс Shape.
# В классе должен быть метод area(), который возвращает площадь фигуры.
# Реализуйте два класса:
# Circle, который принимает радиус.
# Rectangle, который принимает ширину и высоту.
#task2 Проверка размеров фигур.
# Доработайте фигуры:
# Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
# Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение InvalidSizeError.

class InvalidSizeError(ValueError):
    pass

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self) -> float:
        pass

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        if length <= 0 or width <= 0:
            raise InvalidSizeError('Число должно быть больше 0!')
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0:
            raise InvalidSizeError('Число должно быть больше 0!')
        self.radius = radius

    def area(self) -> float:
        from math import pi
        return pow(self.radius, 2) * pi

shapes = [Circle(3), Rectangle(4, 5)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")

try:
    shapes = [Circle(0), Rectangle(4, 5)]
    for shape in shapes:
        print(f"Area: {shape.area():.2f}")
except:
    pass
