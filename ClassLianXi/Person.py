import math


class Person:
    def __new__(cls, *args, **kwargs):
       obj =super().__new__(cls)
       print("id = {0}".format(id(obj)))
       return obj

    def __init__(self,name):
        self.name=name
        
class Person2(Person):
    def __init__(self,name):
        super().__init__(name)


p2=Person2("aaa")
print(p2.name)