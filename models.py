import math

class Calculator:
    """Simple calculator model with basic arithmetic operations."""

    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Деление на нула не е позволено.")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def percent(self, value, percent_value):
        result = (value * percent_value) / 100
        self.history.append(f"{percent_value}% от {value} = {result}")
        return result

    def power(self, base, exponent):
        result = base ** exponent
        self.history.append(f"{base} ^ {exponent} = {result}")
        return result

    def root(self, value, degree: int):
        if degree == 0:
            raise ValueError("Степента на корена не може да бъде 0.")
        if value < 0 and degree % 2 == 0:
            raise ValueError("Четен корен от отрицателно число не е реално число.")

        if value < 0:
            result = -((-value) ** (1 / degree))
        else:
            result = math.pow(value, 1 / degree)

        self.history.append(f"{degree}-ти корен от {value} = {result}")
        return result

    def get_history(self):
        return self.history