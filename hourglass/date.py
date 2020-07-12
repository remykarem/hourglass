import datetime
import calendar
from dateutil.relativedelta import relativedelta


class Date:

    def __init__(self, *args):
        if isinstance(args[0], datetime.date):
            self._date = args[0]
        else:
            self._date = datetime.date(*args)
        self.is_holiday = None

    def __repr__(self):
        return str(self._date)

    def __add__(self, rhs):
        if isinstance(rhs, int):
            duration, duration_type = rhs, "days"
        elif isinstance(rhs, str):
            duration, duration_type = rhs.split()
        else:
            raise ValueError("Invalid")

        return Date(self._date + relativedelta(**{duration_type: int(duration)}))

    def __radd__(self, lhs):
        return self.__add__(lhs)

    def __sub__(self, rhs: str):
        if isinstance(rhs, str):
            duration, duration_type = rhs.split()
        elif isinstance(rhs, int):
            duration, duration_type = rhs, "days"
        elif isinstance(rhs, Date):
            return self._date - rhs._date
        else:
            raise ValueError("Invalid")

        return Date(self._date - relativedelta(**{duration_type: int(duration)}))

    def __gt__(self, rhs):
        return self._date > rhs._date

    def __ge__(self, rhs):
        return self._date >= rhs._date

    def __lt__(self, rhs):
        return self._date < rhs._date

    def __le__(self, rhs):
        return self._date <= rhs._date

    @property
    def day_of_week(self):
        return self._date.weekday()

    @property
    def day_name(self):
        return self._date.strftime("%A")

    @property
    def is_weekday(self):
        if self._date.weekday() < 5:
            return True
        else:
            return False

    @property
    def is_weekend(self):
        return not self.is_weekday

    @property
    def is_leap(self):
        return calendar.isleap(self._date.year)

    @property
    def month_days(self):
        return calendar.monthrange(self._date.year, self._date.month)[1]

    def format_as(self, *args, **kwargs):
        return self._date.strftime(*args, **kwargs)


def today():
    return Date(datetime.date.today())


def yesterday():
    return Date(datetime.date.today()) - 1


def tomorrow():
    return Date(datetime.date.today()) + 1
