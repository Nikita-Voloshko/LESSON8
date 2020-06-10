from datetime import datetime
class Data():
    month = ''
    @classmethod
    def __init__(self, month):
        # self.data = datetime.strptime(data, '%d')
        Data.month = month
        # self. year = datetime.strptime(year, '%Y')

    @staticmethod
    def data_number(self):
        try:
            print(datetime.strptime(Data.month, '%d %b %Y'))
        except ValueError:
            print("Неправельная последовательность. Дата, Месяц, Год")

a = Data("25 Jun 2002")
a.data_number(0)
