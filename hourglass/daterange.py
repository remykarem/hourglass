import datetime
from . import Date


class daterange:

    def __init__(self, start, end, step=1, by="days"):
        if isinstance(start, tuple):
            self.start = Date(*start)
        elif isinstance(start, Date):
            self.start = start
        else:
            raise ValueError("Invalid")
        if isinstance(start, tuple):
            self.end = Date(*end)
        elif isinstance(start, Date):
            self.end = end
        else:
            raise ValueError("Invalid")
        self.step = step
        self.by = by

    def __iter__(self):
        num_days = (self.end - self.start).days
        li = [self.start + f"{i} {self.by}"
              for i in range(num_days)]
        self._it = iter(li)
        return self._it

    def __next__(self):
        return next(self._it)

    def __contains__(self, date):
        return date._date in self._it
