

class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

        self.is_valid_date(self.day, self.month, self.year)

    @ staticmethod
    def is_leap_year(year: int) -> bool:
        """Проверяет, является ли год високосным"""
        return year % 4 == 0

    @staticmethod
    def get_max_day(month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if Date.is_leap_year(year) is True:
            return Date.DAY_OF_MONTH[1][month-1]
        else:
            return Date.DAY_OF_MONTH[0][month-1]

    def is_valid_date(self, day: int, month: int, year: int) -> None:
        """Проверяет, является ли дата корректной"""
        if not isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            raise TypeError()
        if not 0 <= day <= 31 and 0 < month <= 12 and 0 < year:
            raise ValueError()
        if day > self.get_max_day(month, year):
            raise ValueError()

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day: int):
        if not isinstance(day, int):
            raise TypeError()
        if not 0 < day <= 31:
            raise ValueError()
        self._day = day

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError()
        if not 0 < month <= 12:
            raise ValueError()
        self._month = month

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError()
        if year < 0:
            raise ValueError
        self._year = year


if __name__ == "__main__":
    dr = Date(4, 3, 1987)
