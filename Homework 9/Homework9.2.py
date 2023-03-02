class Math:

    def __init__(self, a=None, b=None):
        self.a, self.b = a, b

    def addition(self, a: float, b: float) -> float:
        self.a, self.b = a, b
        print(float(a + b))

    def multiplication(self, a: float, b: float) -> float:
        self.a, self.b = a, b
        print(float(self.a * self.b))

    def division(self, a: float, b: float) -> float:
        self.a, self.b = a, b
        print(float(self.a / self.b))

    def subtraction(self, a: float, b: float) -> float:
        self.a, self.b = a, b
        print(float(self.a - self.b))
