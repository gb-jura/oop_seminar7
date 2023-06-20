class Complex:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f'{self.real_part} + {self.imaginary_part}i'

class ComplexAdd:
    def execute(self, complex1, complex2):
        return Complex(complex1.real_part + complex2.real_part,
                       complex1.imaginary_part + complex2.imaginary_part)

class ComplexMultiply:
    def execute(self, complex1, complex2):
        real_part = complex1.real_part * complex2.real_part - complex1.imaginary_part * complex2.imaginary_part
        imaginary_part = complex1.real_part * complex2.imaginary_part + complex1.imaginary_part * complex2.real_part
        return Complex(real_part, imaginary_part)

class ComplexDivide:
    def execute(self, complex1, complex2):
        denominator = complex2.real_part ** 2 + complex2.imaginary_part ** 2
        real_part = (
                                complex1.real_part * complex2.real_part + complex1.imaginary_part * complex2.imaginary_part) / denominator
        imaginary_part = (
                                     complex2.real_part * complex1.imaginary_part - complex1.real_part * complex2.imaginary_part) / denominator
        return Complex(real_part, imaginary_part)

class ComplexCalculatorFactory:
    def create_operator(self, operator):
        if operator == '+':
            return ComplexAdd()
        elif operator == '*':
            return ComplexMultiply()
        elif operator == '/':
            return ComplexDivide()
        else:
            raise ValueError(f"Unknown operator '{operator}'")

class ComplexCalculator:
    def __init__(self, calculator_factory):
        self.calculator_factory = calculator_factory

    def calculate(self, complex1, operator, complex2):
        operator_obj = self.calculator_factory.create_operator(operator)
        result = operator_obj.execute(complex1, complex2)
        return result

class LoggingDecorator:
    def __init__(self, calculator):
        self.calculator = calculator

    def calculate(self, complex1, operator, complex2):
        result = self.calculator.calculate(complex1, operator, complex2)
        print(f"{complex1} {operator} {complex2} = {result}")
        return result

calculator_factory = ComplexCalculatorFactory()
calculator = ComplexCalculator(calculator_factory)
logging_calculator = LoggingDecorator(calculator)

complex1 = Complex(1, 2)
complex2 = Complex(3, 4)

result = logging_calculator.calculate(complex1, '+', complex2)
result = logging_calculator.calculate(complex1, '*', complex2)
result = logging_calculator.calculate(complex1, '/', complex2)