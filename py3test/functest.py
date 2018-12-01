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

