from django_unixdatetimefield import UnixDateTimeField as BaseUnixDateTimeField
import datetime


class UnixDateTimeField(BaseUnixDateTimeField):
    def to_python(self, val):
        if val is None or isinstance(val, datetime.datetime):
            return val
        if isinstance(val, datetime.date):
            return datetime.datetime(val.year, val.month, val.day)
        else:
            try:
                return datetime.datetime.fromtimestamp(float(val))
            except OSError:
                return None
