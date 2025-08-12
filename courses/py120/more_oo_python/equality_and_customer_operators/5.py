class Silly:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Silly({repr(self.value)})'

    @staticmethod
    def _is_numeric(value):
        if isinstance(value, int):
            return True

        return value.isdigit()

    def __add__(self, other):
        if not isinstance(other, int):
            if not isinstance(other, str):
                return NotImplemented

        both_numeric = (self._is_numeric(self.value) and
                        self._is_numeric(other))
        if both_numeric:
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))