#_*_coding:utf-8_*_

#位置参数、默认参数、可变参数、关键字参数
def a(*args, **kwargs):
    print(args)
    print(kwargs)
def aa(x,*args,y=1, **kwargs):
    print(x,y)
    print(args)
    print(kwargs)
def aaa(x,y=1,*args, **kwargs):
    print(x,y)
    print(args)
    print(kwargs)
b = (1,2,3)
c = {'a':'b', 'c':'d', 'e':'f'}
name = '111'
age = 222
sex = '333'
d = (name,age,sex)
a(name,age,sex)
a(*b,**c)
aa(1,2,3,4,5,6,**c,y=7)
aa(1,2,3,4,5,6,**c)
aaa(1,*(2,3,4,5,6),**c)
aaa(1,2,3,4,5,6,**c)

#类
class A():

    age = 111

    def __init__(self, name, age=2):
        self.name = name
        self.__class__.age = age

    def a(self, b = 'aaa'):
        print(self.name, self.age, b)

    @staticmethod
    def b(name, age = '3', b = 'bbb'):
        A.age = age
        print(name, b, age)

    @classmethod
    def c(cls, name, b = 'ccc'):
        print(name, b, cls.age)
        cls.age = 333
        print(cls.age)

a = A(1)
a.a()
print(a.age, A.age)
b = A(1, 22)
b.a()
print(b.age, A.age)
A.b(1, 4)
print(A.age)
A.c(1)
print(A.age)

class A():

    a = 'a'

    @classmethod
    def aa(cls, bb):
        print('say {1} in {0}, a is {2}'.format(cls.__name__, bb, cls.a))

A.aa('haha')
print(A.a)

