#task1 Реализуйте класс Email, который представляет электронное письмо. Каждое письмо должно содержать:
# sender — адрес отправителя
# recipient — адрес получателя
# subject — тема письма
# body — текст письма
# date — дата отправки
# Класс должен поддерживать:
# Сравнение писем по дате
# Преобразование письма в строку
# Получение длины текста письма
# Проверку на наличие текста в письме или не состоит ли текст только из пробелов
# Пример использования:
# e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
# e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
# print(e1)
# print(e1)
# print(e2)
# print("Length:", len(e1))
# print("Has text:", bool(e1))
# print("Is newer:", e2 > e1)
# Пример вывода:
# From: alice@example.com
# To: bob@example.com
# Subject: Meeting
# - Let's meet at 10am -
# From: bob@example.com
# From: bob@example.com
# To: alice@example.com
# Subject: Report
# -  -
# Length: 18
# Length: 18
# Has text: True
# Is newer: True

from datetime import datetime
class Email:
    """
    Класс для представления электронного письма.
    """
    from datetime import datetime
    from typing import Any

    def __init__(self, sender: str, recipient: str, subject: str, body: Any, date: datetime) -> None:
        """
        Инициализирует объект Email.

        :param sender: Адрес отправителя.
        :param recipient: Адрес получателя.
        :param subject: Тема письма.
        :param body: Тело письма.
        :param date: Дата и время отправки.
        """
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        self.body = body
        self.date = date

    def __str__(self) -> str:
        """
        Возвращает строковое представление письма.

        :return: Строка с данными о письме.
        """
        return f'From: {self.sender},\nTo: {self.recipient},\nSubject: {self.subject}\n- {self.body if self.body else "-"}'

    def __len__(self) -> int:
        """
        Возвращает длину тела письма.

        :return: Количество символов в теле письма.
        """
        return len(self.body)

    def __bool__(self) -> bool:
        """
        Проверяет, содержит ли тело письма текст (исключая пробелы).

        :return: True, если текст есть, иначе False.
        """
        return bool(self.body.strip())

    def __gt__(self, other) -> bool:
        """
        Сравнивает два письма по дате отправки.

        :param other: Другой объект для сравнения.
        :return: True, если текущее письмо отправлено позже, иначе False.
        :raises TypeError: Если объект 'other' не является экземпляром класса Email.
        """
        if not isinstance(other, Email):
            raise TypeError(f"Сравнение '>' не поддерживается между экземплярами '{type(self).__name__}' и '{type(other).__name__}'")
        return self.date > other.date

e1 = Email("alice@example.com", "bob@example.com", "Meeting", "Let's meet at 10am", datetime(2024, 6, 10))
e2 = Email("bob@example.com", "alice@example.com", "Report", "", datetime(2024, 6, 11))
print(e1)
print(e1)
print(e2)
print("Length:", len(e1))
print("Has text:", bool(e1))
print("Is newer:", e2 > e1)


# task2 Класс для работы с деньгами.
# Создайте класс Money, в котором можно:
# складывать и вычитать объекты через операторы + и - выводить объект как строку в виде "$<amount>" при сложении и вычитании возвращается новый объект если вычитание приводит к отрицательному значению — вернуть 0
# Пример использования:
# money1 = Money(100)
# money2 = Money(50)
# print(money1 + money2)
# print(money1 + money2)
# print(money1 - money2)
# print(money2 - money1)
# Пример вывода:
# $150
# $50
# $0

class Money:
    """Класс для работы с деньгами."""

    def __init__(self, money: int) -> None:
        """Инициализирует объект Money.

        Args:
            money (int): Сумма денег.
        """
        self.money = money

    def __add__(self, other: "Money") -> "Money":
        """Складывает два объекта Money.

        Args:
            other (Money): Второй объект Money.

        Returns:
            Money: Новый объект Money.

        Raises:
            TypeError: Если у `other` отсутствует атрибут `money`.
        """
        if not isinstance(other, Money):
            raise TypeError(f"Невозможно сложить Money и {type(other).__name__}")
        return Money(self.money + other.money)

    def __sub__(self, other: "Money") -> "Money":
        """Вычитает один объект Money из другого.

        Args:
            other (Money): Вычитаемый объект Money.

        Returns:
            Money: Новый объект Money или Money(0), если результат отрицательный.

        Raises:
            TypeError: Если у `other` отсутствует атрибут `money`.
        """
        if not isinstance(other, Money):
            raise TypeError(f"Невозможно вычесть Money и {type(other).__name__}")
        if self.money - other.money < 0:
            return Money(0)
        return Money(self.money - other.money)

    def __str__(self) -> str:
        """Возвращает строковое представление объекта.

        Returns:
            str: Строка в виде "$<amount>".
        """
        return f"${self.money}"


money1 = Money(100)
money2 = Money(50)
print(money1 + money2)
print(money1 - money2)
print(money2 - money1)
