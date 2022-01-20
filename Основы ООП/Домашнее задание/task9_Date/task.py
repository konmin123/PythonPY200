class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = None
        self.day = self.day_editor(day)
        self.month = None
        self.month = self.month_editor(month)
        self.year = None
        self.year = self.year_editor(year)

    @staticmethod
    def day_editor(day):
        if not isinstance(day, int):
            raise TypeError
        if not 0 < day <= 31:
            raise ValueError
        return f'{day if day > 10 else day:02}'

    @staticmethod
    def month_editor(month):
        if not isinstance(month, int):
            raise TypeError
        if not 0 < month <= 12:
            raise ValueError
        return f'{month if month > 10 else month:02}'

    @staticmethod
    def year_editor(year):
        if not isinstance(year, int):
            raise TypeError
        if not 0 < year:
            raise ValueError
        return year

    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year}"

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


data1 = Date(12, 11, 2015)
print(data1)
