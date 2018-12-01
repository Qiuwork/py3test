#_*_coding:utf-8_*_
# 文件读取
# 默认读取方式
f = open('bar.py')
ctx = f.read()
print(ctx)
f.close()
# 指定读取方式
f = open('bar.py', 'r', encoding='utf8')
ctx = f.read()
print(ctx)
f.close()
# 文件写入
# 单次写入
f = open('write.test', 'w', encoding='utf8')
f.write('hello python\nhello world')
f.close()
# 多次写入
f = open('write.test', 'w+', encoding='utf8')
f.write('hello python\n')
f.write('hello world')
f.close()
# 文件追加
f = open('write.test', 'a', encoding='utf8')
f.write('hello python\nhello world')
f.close()
# 二进制文件读写
f1 = open('test.jpg', 'rb')
f2 = open('test.bak.jpg', 'wb')
f2.write(f1.read())
f2.close()
f1.close()
# with语句块
with open('bar.py', 'r', encoding='utf8') as f:
    print(f.read())
# 文件对象方法
with open('bar.py', 'r', encoding='utf8') as f:
    print(f.tell())
    print(f.read())
    print(f.tell())
    print(f.read())
    f.seek(0)
    print(f.tell())
    print(f.read())


str
class Foo(object):
    def __str__(self):
        return "<Foo>"

f = Foo()
print(f)
repr
class Foo(object):
    def __repr__(self):
        return "<Foo repr>"

f = Foo()
print(repr(f))
len
class Foo(object):
    def __len__(self):
        return 0

f = Foo()
print(len(f))
iter
class Foo(object):
    def __init__(self, name, age, sex):
        self.set = (name, age, sex)
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.set):
            b = self.set[self.i]
            self.i += 1
            return b
        else:
            raise StopIteration()

foo = Foo('python', 18, 'male')
print(next(foo))
for a in foo:
    print(a)
getitem
class Foo(object):
    def __init__(self, name, age, sex):
        self.set = (name, age, sex)

    def __getitem__(self, n):
        if n < len(self.set):
            return self.set[n]
        else:
            raise IndexError('index out of range')

std1 = Foo('python', 18, 'female')
print(std1[0])
getattr
class URL():
    def __init__(self, path='http://api.huice.server'):
        self._path = path
        self.args = '?k=v'

    def __getattr__(self, path):
        return URL('%s/%s' % (self.__path, path))

    def __str__(self):
        return self._path

print(URL().user.login.args)
#练习 属性常见用的魔法属性

#作用域
- globals()
- locals()
- global
- nonlocal