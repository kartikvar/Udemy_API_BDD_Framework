class Calculator:
    def __init__(self):
        print("Hi i m constructor")

    num = 10

    def add(self):
        num = 11
        print("Local variable is --> ", num)
        print("Class variable is --> ", self.num)

obj = Calculator()
obj.add()
print(obj.num)
