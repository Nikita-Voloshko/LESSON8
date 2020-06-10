class Compleks():
    number = 0
    def __init__(self, number1, number2):
        self.number1 = int(number1)
        self.number1 = int(number2)
        Compleks.number = complex(int(number1), int(number2))
    def __add__(self):
        i = input('Что вы хотите выполнить? 1(+) 2(-) 3(*) 4(/) ')
        if (i == '1'):
            return Compleks.number + Second.number
        if (i == '2'):
            return Compleks.number - Second.number
        if (i == '3'):
            return Compleks.number * Second.number
        if (i == '4'):
            return Compleks.number / Second.number
        else:
            return "ОШИБКА!!!"
class Second():
    number = 0
    def __init__(self, number1, number2):
        self.number1 = int(number1)
        self.number1 = int(number2)
        Second.number = complex(int(number1), int(number2))

a = Compleks(2, 1)
b = Second(4, 1)
print(a.__add__())