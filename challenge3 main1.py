# A Sample class with init method
class Person:
 
    # init method or constructor
    def __init__(self, name):
        self.name = name
 
    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)
 
 
# Creating different objects
p1 = Person('Gayathri')
p2 = Person('Surya')
p3 = Person('Nithya')
 
p1.say_hi()
p2.say_hi()
p3.say_hi()