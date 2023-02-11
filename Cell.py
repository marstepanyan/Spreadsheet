from Colors import Color
from datetime import datetime


class Cell:
    def __init__(self, value: str, color: Color):
        self._value = value
        self._color = color

    def set_value(self, new_value: str):
        try:
            new_value = str(new_value)
            self._value = new_value
        except ValueError:
            print("Cell's value should be string")

    def set_color(self, new_color: Color):
        if isinstance(new_color, Color):
            self._color = new_color
        else:
            raise ValueError("Cell's value should be Color")

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def to_int(self):
        try:
            return int(self._value)
        except ValueError:
            raise ValueError("Couldn't convert to integer")

    def to_float(self):
        try:
            return float(self._value)
        except ValueError:
            raise ValueError("Couldn't convert to float")

    def to_date(self):
        try:
            self._value = datetime.strptime(self._value, '%d/%m/%y')
        except ValueError:
            raise ValueError("Couldn't convert to date")

    def reset(self):
        self._value = ''
        self._color = ''

    def __repr__(self):
        return str(dict(value=self._value, color=self._color))
