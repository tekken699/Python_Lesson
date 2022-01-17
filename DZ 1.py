class Error(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date(object):
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        is_date = cls.is_date_valid(date_as_string)
        try:
            if is_date == False:
                raise Error("Wrong date!")
        except Error as err:
            print(err)
            return

        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


date2 = Date.from_string('11-10-2012')

try:
    print(date2.day, date2.month, date2.year)
except:
    print('OOps. Something wrong')