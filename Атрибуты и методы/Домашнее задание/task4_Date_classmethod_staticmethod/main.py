class Date:
    """Класс для работы с датами"""

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    def is_leap_year(self):
        """Проверяет, является ли год високосным"""
        if self.year % 4 == 0:
            index = 1
        else:
            index = 0
        return index

    def get_max_day(self):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        day_of_month = (
            (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
            (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
        )
        if self.year % 4 == 0:
            return day_of_month[1][self.month - 1]
        else:
            return day_of_month[0][self.month - 1]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not (isinstance(day, int) and isinstance(month, int) and isinstance(year, int)):
            raise TypeError()
        if not (1 <= day <= 31 and 1 <= month <= 12 and 0 < year):
            raise ValueError()


if __name__ == "__main__":
    date1 = Date(12, 2, 2020)
    print(date1.is_leap_year())
    print(date1.get_max_day())
    pass
