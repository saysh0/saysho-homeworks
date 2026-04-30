#task1 Класс Rectangle.
# Создайте класс Rectangle, который описывает прямоугольник.
# У каждого объекта должны быть два поля: width и height.
# Добавьте метод get_area(), который возвращает площадь прямоугольника.
# Создайте объект прямоугольника с произвольными значениями.
# Выведите его площадь.
# Измените ширину и высоту.
# Выведите новую площадь.
# Пример вывода:
# Площадь: 20
# Новая площадь: 35

class Rectangle:
    def __init__(self, width: float, height: float):
        """
        Инициализирует прямоугольник.

        :param width: Ширина (положительное число)
        :param height: Высота (положительное число)
        """
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть больше нуля!")
        self.width = width
        self.height = height

    def get_area(self)-> float:
        """Возвращает площадь прямоугольника."""
        return self.width * self.height

rectangle1 = Rectangle(4, 5)
print(f'Площадь: {rectangle1.get_area()}')
rectangle2 = Rectangle(5, 7)
print(f'Новая площадь: {rectangle2.get_area()}')

# task2 Класс Counter.
# Реализуйте класс Counter, который представляет собой простой счётчик.
# Счётчик должен начинаться с нуля.
# Предусмотрите методы для увеличения и уменьшения значения на единицу, при этом при каждой операции должно отображаться новое значение счётчика.
# Добавьте метод, возвращающий текущий результат.
# Проверьте работу счётчика, выполнив несколько операций.
# Пример вывода:
# Значение увеличено, текущее: 1
# Значение увеличено, текущее: 2
# Значение увеличено, текущее: 3
# Значение уменьшено, текущее: 2
# Текущее значение: 2

class Counter:
    def __init__(self, value: float = 0) -> None:
        """
        Инициализирует счётчик с начальным значением 0.

        :param value: Начальное значение счётчика (по умолчанию 0).
        :raises TypeError: Если передано не число.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Начальное значение счётчика должно быть числом (int или float)")
        self.value = value

    def plus_one(self):
        """
        Увеличивает значение счётчика на 1.

        :return: Строка с уведомлением о новом значении.
        """
        self.value += 1
        return f"Значение увеличено, текущее: {self.value}"

    def min_one(self):
        """
        Уменьшает значение счётчика на 1.

        :return: Строка с уведомлением о новом значении.
        """
        self.value -= 1
        return f"Значение уменьшено, текущее: {self.value}"

    def current_value(self):
        """
        Возвращает текущее состояние счётчика.

        :return: Строка с текущим значением.
        """
        return f"Текущее значение: {self.value}"

counter = Counter()
print(counter.plus_one())
print(counter.plus_one())
print(counter.plus_one())
print(counter.min_one())
print(counter.current_value())
