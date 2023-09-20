class Roman:
    def init(self, value):
        self.value = value

    def add(self, other):
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        else:
            raise TypeError("Unsupported operand type for +")

    def sub(self, other):
        if isinstance(other, Roman):
            return Roman(self.value - other.value)
        else:
            raise TypeError("Unsupported operand type for -")

    def mul(self, other):
        if isinstance(other, Roman):
            return Roman(self.value * other.value)
        else:
            raise TypeError("Unsupported operand type for *")

    def truediv(self, other):
        if isinstance(other, Roman):
            return Roman(self.value / other.value)
        else:
            raise TypeError("Unsupported operand type for /")

    @staticmethod
    def to_roman(decimal):
        # Реализуйте преобразование десятичного числа в римское число
        pass

    @staticmethod
    def from_roman(roman):
        # Реализуйте преобразование римского числа в десятичное число
        pass
