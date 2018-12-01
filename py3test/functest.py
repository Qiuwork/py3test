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


class Foo(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return '{what}'.format(what=self._name)

    @name.setter
    def name(self, value):
        if isinstance(value, bytes):
            self._name = value
        else:
            self._name = None


f = Foo('hello')
print(f.name)
f.name = 22
print(f.name)
f._name = 2
print(f.name)

class base(object):
    def __init__(self):
        print('in base init')

    def say(self):
        print('in base say')

    def __del__(self):
        print('in base del')

class father(base):
    pass

f = father()
f.say()
del f

class base(object):
    def __init__(self):
        print('in base init')

    def say(self):
        print('in base say')

    def __del__(self):
        print('in base del')

class father(base):
    def __init__(self):
        print('in father init')

    def say(self):
        print('in father say')

    def __del__(self):
        print('in father del')

f = father()
f.say()
del f

#二叉树先序遍历

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def a(root):
    if root == None:
        return
    print(root.value)
    a(root.left)
    a(root.right)

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6
n5.left = n7
a(n1)
