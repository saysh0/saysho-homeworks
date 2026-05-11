#task1 Банковский счёт.
# Создайте класс BankAccount, описывающий банковский счёт.
# Объект должен хранить имя владельца и текущий баланс.
# Реализуйте методы:
# пополнение счёта
# снятие средств
# отображение баланса
# При попытке снять больше, чем есть на счёте, операция не должна выполняться.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.

#task2 История операций.
# Доработайте класс BankAccount.
# Каждая операция пополнения и снятия должна сохраняться в историю.
# История должна быть доступна через property history только для чтения.
# История представляется в виде списка строк ("Deposit: 150", "Withdraw: 100" и т.д.).

class BankAccount:
    """
    Класс для управления банковским счетом пользователя.
    """

    def __init__(self, user_name: str, balance: float) -> None:
        """
        Инициализация объекта банковского счета.

        :param user_name: Имя владельца счета.
        :param balance: Начальная сумма на счету.
        """
        self.__user_name = user_name
        self.__balance = balance
        self.__history = []

    @property
    def history(self) -> list[str]:
        """
        Возвращает историю всех успешно завершенных транзакций.

        :return: Список строковых записей о депозитах и снятиях.
        :raise AttributeError: Если доступ к истории ограничен (опционально для документации).
        """
        return self.__history

    def info(self) -> float:
        """
        Получение текущего остатка средств.

        :return: Текущий баланс.
        """
        return self.__balance

    def top_up_balance(self, amount: float) -> str:
        """
        Метод для пополнения баланса.

        :param amount: Сумма, на которую увеличивается баланс.
        :return: Статус выполнения операции.
        """
        self.__balance += amount
        self.__history.append(f'Deposit: {amount}')
        return 'Баланс успешно пополнен!'

    def top_down_balance(self, amount: float) -> str:
        """
        Метод для снятия средств с баланса.

        :param amount: Сумма, которую необходимо снять.
        :return: Статус выполнения операции.
        :raise ValueError: Если сумма снятия больше текущего баланса.
        """
        if amount > self.__balance:
            raise ValueError('Средств на балансе меньше, чем вы пытаетесь снять.')
        self.__balance -= amount
        self.__history.append(f'Withdraw: {amount}')
        return 'Деньги были успешно сняты с баланса!'


usr1 = BankAccount('Nikita', 100)
print(f"Текущий баланс: {usr1.info()}")
print(usr1.top_up_balance(100))
print(f"Текущий баланс: {usr1.info()}")
print(usr1.top_down_balance(100))
print(f"Текущий баланс: {usr1.info()}")
try:
    usr1.top_down_balance(200)
except ValueError as e:
    print(e)
print(f"Текущий баланс: {usr1.info()}")
print(f'Operation history:')
for i in usr1.history:
    print(f"\t\t{i}")