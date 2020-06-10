class Only_Numbers(Exception):
    def __init__(self, text):
        self.text = text
user_list = []
i = ''
while i != "stop":
    user = input('Введите число в список.')
    try:
        if user.isdecimal() != True:
            raise Only_Numbers('Только числа.')
    except Only_Numbers:
        print("Ошибка. Это не число")
    else:
        user_list.append(user)
    finally:
        i = input('Для выхода ведите "stop".')
print(user_list)
