# calculate simple interest
class Calculator:
    p = 10
    t = 10
    r = 10
    # p = int(input("Enter principle: "))
    # t = int(input("Enter time: "))
    # r = int(input("Enter rate: "))

    def take_value(self):
        x = self.p
        y = self.t
        z = self.r
        return [x, y, z]

    def calculate(self):
        smp = self.take_value()
        a = smp[0]
        b = smp[1]
        c = smp[2]
        return a * b * c / 100

    def display(self):
        return self.calculate()


obj = Calculator()
print(obj.display())

