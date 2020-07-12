import datetime
from dateutil.relativedelta import relativedelta
import time


class Datetime:
    """
    This is a location-aware Datetime object.
    Treat this as if time were frozen and you can teleport
    to any other locations. You cannot replace a timezone.
    To do that, instantiate another Datetime object.

    By default, you will be located at GMT +0.
    """

    def __init__(self, *args, gmt=0):
        self._datetime = datetime.datetime(*args)
        self.gmt = gmt

    def __repr__(self):
        if self.gmt >= 0:
            return f"{self._datetime} GMT +{self.gmt:.0f}"
        else:
            return f"{self._datetime} GMT {self.gmt:.0f}"

    def switch_to_utc(self):
        return from_datetime(self._datetime - relativedelta(hours=self.gmt), gmt=self.gmt)

    def switch_to(self, gmt):
        if gmt == 0:
            return self.switch_to_utc()
        else:
            return from_datetime(self._datetime + relativedelta(hours=-self.gmt+gmt), gmt=gmt)

    def to_epoch(self):
        """
        Note this means a UNIX/POSIX representation of time
        by switching to GMT +0
        """
        return self._datetime.timestamp()

    def __add__(self, rhs):
        if isinstance(rhs, str):
            duration, duration_type = rhs.split()
        else:
            raise ValueError("Invalid")

        return from_datetime(self._datetime + relativedelta(**{duration_type: int(duration)}), gmt=self.gmt)

    def __sub__(self, rhs: str):
        if isinstance(rhs, int):
            duration, duration_type = rhs, "days"
        elif isinstance(rhs, Datetime):
            if self.gmt != rhs.gmt:
                raise ValueError("Cannot subtract from different timezones!")
            else:
                return self._datetime - rhs._datetime
        else:
            raise ValueError("Invalid")

        return from_datetime(self._datetime - relativedelta(**{duration_type: int(duration)}))

    def __gt__(self, rhs):
        return self._datetime > rhs._datetime

    def __ge__(self, rhs):
        return self._datetime >= rhs._datetime

    def __lt__(self, rhs):
        return self._datetime < rhs._datetime

    def __le__(self, rhs):
        return self._datetime <= rhs._datetime

    def __getattr__(self, key):
        allowed = ["year", "month", "day", "hour", "minute",
                   "second", "microsecond"]
        if key in allowed:
            return getattr(self._datetime, key)
        else:
            raise ValueError

    def __or__(self, gmt):
        return self.switch_to(gmt)


def from_datetime(dt, gmt):
    return Datetime(dt.year, dt.month, dt.day, dt.hour,
                       dt.minute, dt.second,
                       gmt=gmt)


def from_epoch(epoch, *, force_gmt=0):
    """
    Epoch time should be taken to mean UTC. It is a 10-digit number.
    """
    dt = datetime.datetime.utcfromtimestamp(epoch)
    return from_datetime(dt, gmt=force_gmt)


def now():
    gmt = -time.timezone / 60 / 60
    print(f"Your timezone is GMT {gmt}")
    return from_datetime(datetime.datetime.now(), gmt=gmt)


class datetimerange:
    def __init__(self):
        pass
