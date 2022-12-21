class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def add(x1, x2):
        return x1 + x2

    @staticmethod
    def multiply(x1, x2):
        return x1 * x2

    @staticmethod
    def subtract(x1, x2):
        return x1 - x2

    @staticmethod
    def divide(x1, x2):
        if x2 != 0:
            return x1 / x2
