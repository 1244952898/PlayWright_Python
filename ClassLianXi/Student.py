class Student:
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)

st0=Student("aaaa")
st1=Student("bbbb")
s=st0+st1
print(s)
print(len(st0))