from oops.inheritence.Parent_Class import Parent


class Child(Parent):

    def sound(self):
        print("This is child class sound")
        super().sound()

obj = Child()
obj.sound()
obj.walk()