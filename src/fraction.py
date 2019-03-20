class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
            self.value = numerator / denominator
        else:
            raise ZeroDivisionError

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)
