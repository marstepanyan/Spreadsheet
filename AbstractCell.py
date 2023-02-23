from Colors import Color
from datetime import datetime
import abc


class AbstractCell(abc.ABC):
    def __init__(self, value, color: Color):
        self._value = value
        self._color = color

    def set_color(self, new_color: Color):
        if isinstance(new_color, Color):
            self._color = new_color
        else:
            raise TypeError("Cell's color should be Color")

    @abc.abstractmethod
    def set_value(self, new_value):
        pass

    def get_value(self):
        return self._value

    @abc.abstractmethod
    def get_string_value(self):
        pass

    def reset(self):
        self._value = None
        self.set_color(Color(1))

    def __repr__(self):
        return str(dict(value=self._value, color=self._color))


class IntCell(AbstractCell):
    def __init__(self, value: int, color: Color):
        if isinstance(value, int):
            super().__init__(value, color)
        else:
            raise TypeError('you are creating IntCell')

    def set_value(self, new_value: int):
        if isinstance(new_value, int):
            self._value = new_value
        else:
            raise TypeError("Cell's value should be integer")

    def get_string_value(self):
        return str(self._value)


class FloatCell(AbstractCell):
    def __init__(self, value: float, color: Color):
        if isinstance(value, float):
            super().__init__(value, color)
        else:
            raise TypeError('you are creating FloatCell')

    def set_value(self, new_value: float):
        if isinstance(new_value, float):
            self._value = new_value
        else:
            raise TypeError("Cell's value should be float")

    def get_string_value(self):
        return str(self._value)


class StringCell(AbstractCell):
    def __init__(self, value: str, color: Color):
        if isinstance(value, str):
            super().__init__(value, color)
        else:
            raise TypeError('you are creating StringCell')

    def set_value(self, new_value: str):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise TypeError("Cell's value should be string")

    def get_string_value(self):
        return str(self._value)


class DateCell(AbstractCell):
    def __init__(self, value, color: Color):
        try:
            value = datetime.strptime(str(value), '%d/%m/%y')
            super().__init__(value, color)
        except ValueError:
            raise TypeError("Couldn't convert to date")

    def set_value(self, new_value):
        try:
            new_value = datetime.strptime(new_value, '%d/%m/%y')
            self._value = new_value
        except ValueError:
            raise TypeError("Couldn't convert to date")

    def get_string_value(self):
        return str(self._value)
