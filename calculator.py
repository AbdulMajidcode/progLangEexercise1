class Calculator:
    def __init__(self,a,b) -> None:
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    


calculator = Calculator(6,2)

print(calculator.addition())
print(calculator.subtraction())
print(calculator.multiplication())
print(calculator.division())

