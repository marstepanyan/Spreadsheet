class Cell:
    def __init__(self, value, color):
        self._value = value
        self._color = color

    def set_value(self, new_value):
        self._value = new_value

    def set_color(self, new_color):
        self._color = new_color

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def to_int(self):
        return int(self._value)

    def to_float(self):
        return float(self._value)

    def to_date(self):
        pass

    def reset(self):
        self._value = ''
        self._color = ''

    def __repr__(self):
        return str(dict(value=self._value, color=self._color))
