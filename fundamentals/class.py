# instanciar com valores
class Calculator:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def som(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# instanciar sem valores, passando somente quando for chamar algum metodo
class CalculatorTwo:
    def som(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def mul(self, num1, num2):
        return num1 * num2

    def div(self, num1, num2):
        return num1 / num2


class Television:
    def __init__(self):
        self.on = False
        self.canal = 1

    def power(self):
        self.on = not self.on

    def next_channel(self):
        self.canal += 1 if self.on else "Tv desligada"

    def previous_channel(self):
        self.canal -= 1


tv = Television()
print(tv.on)
tv.power()
print(tv.on)
tv.power()
print(tv.on)
