class student(object):
	pass

s = student()
s.name="mike"
print(s.name)


def set_age(self,age):
	self.age=age

from types import MethodType

s.set_age=MethodType(set_age,s)
s.set_age(100)
print(s.age)

class study(object):
		__slots__=('name','age')

m = study()
m.name='ok'
print(m.name)
m.age=100
print(m.age)

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)