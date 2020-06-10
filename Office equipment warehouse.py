from abc import abstractmethod
class equipment():
    printer = 0
    scanner = 0
    copier = 0

    def __init__(self, printer, scanner, copier):
        equipment.printer = int(printer)
        equipment.scanner = int(scanner)
        equipment.copier = int(copier)
    def quantity(self):
        print(f"Количество техники на = {equipment.printer + equipment.scanner + equipment.copier}")



class printer():
    @staticmethod
    def quantity_printer(self):
        print(f"Количество принтеровна = {equipment.printer}")
class scanner():
    @staticmethod
    def quantity_scanner(self):
        print(f"Количество сканеров = {equipment.scanner}")
class copier():
    @staticmethod
    def quantity_copier(self):
        print(f"Количество ксероксов = {equipment.copier}")
class Warehouse():
    @property
    def import_(self):
        printer_result = {'on the': 0}
        scanner_result = {'on the': 0}
        copier_result = {'on the': 0}
        n = 0
        while n != '2':
            try:
                print()
                i = int(input("Что вы хотите передать на склад? 1(Принтер) 2(Сканер) 3 (Ксерокс) "))
                if (i == 1):
                    user = int(input(f"Сколько принтеров вы хотите передать из {equipment.printer}? "))
                    if (user <= equipment.printer):
                        printer_result['on the'] += user
                        equipment.printer -= user
                    else:
                        print()
                        print(f"В наличии принетро: {equipment.printer}.")
                        print()
                elif (i == 2):
                    user = int(input(f"Сколько сканеров вы хотите передать из {equipment.scanner}? "))
                    if (user <= equipment.scanner):
                        scanner_result['on the'] += user
                        equipment.scanner -= user
                    else:
                        print()
                        print(f"В наличии сканеров: {equipment.scanner}.")
                        print()
                elif (i == 3):
                    user = int(input(f"Сколько сканеров вы хотите передать из {equipment.printer}? "))
                    if (user <= equipment.copier):
                        copier_result['on the'] += user
                        equipment.copier -= user
                    else:
                        print()
                        print(f"В наличии ксероксов: {equipment.copier}.")
                        print()
                else:
                    print()
                    print("Ошибка, неверное число!")
            except ValueError:
                print("Ошибка! Введите число")
            finally:
                n = input("Хотите продолжить? 1(Да) 2(Нет) ")
        print()
        print(f"На скаладе принтеров: {printer_result['on the']}")
        print(f"Сканеров: {scanner_result['on the']} ")
        print(f"Ксероксов: {copier_result['on the']}")



a = equipment(3, 6, 3)
a.quantity()
printer.quantity_printer(0)
scanner.quantity_scanner(0)
copier.quantity_copier(0)
b = Warehouse()
b.import_