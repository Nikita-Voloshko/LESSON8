class Dev_Error(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


number1 = int(input('Введите делимое '))
number2 = int(input('Введите делитель '))
try:
    if (number2 == 0):
        raise Dev_Error("Ошибка деления на 0")
except ValueError:
    print("Error type of value!")
else:
    print(f"Все правельно! Частное = {number1 / number2}")
finally:
    print(" Конец программы.")

