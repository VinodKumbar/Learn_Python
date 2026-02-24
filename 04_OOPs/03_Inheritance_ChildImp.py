from Constructor import calculator

class ChildImplementation(calculator):
    num = 300

    def child_method(self):
        return "This is a method in the child class."

    def add(self):
        return self.a + self.b + self.num

obj = ChildImplementation(10, 20)
print(obj.add()) # Output: 330
print(obj.child_method()) # Output: "This is a method in the child class."



