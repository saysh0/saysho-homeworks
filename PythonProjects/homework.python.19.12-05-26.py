#task1 Класс Door.
# Создайте класс Door, представляющий электронную дверь.
# ● При создании передаётся первоначальный код доступа.
# ● Есть метод unlock(code), который разрешает доступ при правильном коде.
# ● При неверном коде доступ отклоняется.
# Продумайте, какие поля и методы следует скрыть от внешнего доступа, а какие оставить открытыми.
# Пример вывода:
# Access denied.
# Access granted.
import time

from win32trace import blockingread


#task2 Смена кода.
# Доработайте класс Door.
# ● Добавьте метод для смены кода.
# ● Новый код можно установить только после проверки текущего кода.
# ● Логика проверки корректности кода должна не должна дублироваться.
# Пример вывода:
# Access denied. Code not changed.
# Code changed.
# Access denied.
# Access granted.

#task3 Блокировка двери.
# Доработайте класс Door.
# ● При создании можно указать:
# ○ максимальное количество попыток (по
# умолчанию 3)
# ○ время блокировки в минутах (по умолчанию 15)
# ● Если попытки исчерпаны, дверь блокируется на
# указанное время.
# ● Пока дверь заблокирована — сменить код или
# открыть нельзя.
# ● Неверные попытки входа или смены кода
# учитываются общим счётчиком.
# ● При блокировке должно выводиться сообщение с
# указанием оставшегося времени ожидания.
# Пример вывода:
# Access denied.
# Access denied. Code not changed.
# Too many failed attempts. Door is blocked. Try again in 0 min 2 sec.
# Door is blocked. Try again in 0 min 2 sec.
# Access granted.

class Door:
    def __init__(self, pass_key: float, unlock_trys: int = 3, block_time: float = 15):
        self.__pass_key = pass_key
        self.unlock_trys = unlock_trys
        self.block_time = block_time
        self.__try = 0
        self.blocked_time = None
        self.door_status_global = True


    def door_status(self):
        from datetime import datetime
        time_now = round(datetime.now().timestamp())
        if self.__try == self.unlock_trys and ((time_now - int(self.blocked_time)) / 60) < self.block_time:
            self.door_status_global = False
            return f'Door is blocked. Try again in {(self.block_time - ((time_now - int(self.blocked_time)) / 60))}'
        else:
            self.__try = 0
            self.door_status_global = True
            self.blocked_time = None
            return f'Door is unlocked'

    def unlock(self, user_key: float):
        unlock = 'Не открыл'
        from datetime import datetime
        if not self.door_status_global:
            return f'Door is locked!'

        if user_key != self.__pass_key:
            self.__try += 1
        else:
            unlock = 'Открыл'
            self.__try = 0

        if self.__try == 3:
            self.blocked_time = round(datetime.now().timestamp())
            self.door_status()
        return unlock


    @property
    def interaction_with_key(self):
        return self.__pass_key

    @interaction_with_key.setter
    def interaction_with_key(self, codes: list[float]):
        from datetime import datetime
        old_code, new_code = codes[0], codes[1]
        if self.__pass_key != old_code:
            self.__try += 1
        else:
            self.__pass_key = new_code

        if self.__try == 3:
            self.blocked_time = int(round(datetime.now().timestamp()))
            time.sleep(self.block_time * 60)

door1 = Door(1234,3, 15)
print(door1.unlock(1234))
print(door1.unlock(1235))
print(door1.unlock(1235))
print(door1.unlock(1235))
print(door1.door_status())
time.sleep(60)
print(door1.unlock(1235))
print(door1.door_status())