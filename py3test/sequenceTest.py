#_*_coding:utf-8_*_
alist = []
for i in range(10):
    alist.append(i)
atuple = tuple(alist)

#tuple : index , count

print(atuple)
print(atuple[1:3])
print(atuple[13:])
print(atuple.count((1,2)))
print(atuple.index(3))
b  = {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}
print(tuple(b))
print(tuple(b.values()))
print(tuple(b.items()))
c = tuple(b.items())
print(c[0][0])
d = ()
e = 1,2
print(d,type(d))
print(e,type(e))

#list:append,extend,insert,clear,remove,pop,copy,sort,reverse,count,index

alist[1:3] = "111"
print(alist)
alist[1:3] = [3,3,3,3]
print(alist)
alist.reverse()
print(alist)
print(alist.pop(3))
print(alist.pop())
print(alist)
a2 = a1 = [1,2,3,4]
a3 = (1,a2)
print(a3)
a1.clear()
print(a3)
a2 = a1 = [1,2,3,4]
a3 = (1,a2)
print(a3)
a2.clear()
print(a3)

#dict:get, keys, values, items, pop, popitem, update, setdefault, fromkeys, clear, copy
a  = {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003}
print(a)
print(a.get('fname1',1))
print(a.get('fname2'))
print(a.keys())
print(a.values())
print(a.items())
print(a.pop('Brian','not have'))
print(a.pop('fname','not have'))
print(a.popitem())
print(a.update({'1':'2','3':4,'5':'6','7':8}))
print(dict.fromkeys({'1':'2','3':4},'a'))
print(dict.fromkeys(a,'a'))
print(a.setdefault('lname','aaa'))
print(a.setdefault('11','bbb'))
print(a)


# set
# 'add', 'remove', 'update', 'discard', 'pop', 'clear', 'copy'
# 'intersection'(&), 'union'(|), difference(-), symmetric_difference(^)
# 'intersection_update', 'difference_update', 'symmetric_difference_update'
# 'issubset'(<=), 'issuperset'(>=), 'isdisjoint'

t1 = {1, 2, 3, 4}
t2 = {3, 4, 5, 6}
dir(t1)
t1.discard(7)
print(t1)
t1.pop()
t1.clear()
t1.copy()

t1.isdisjoint(t2)   # 是否不存在交集， 不存在则True， 存在则False
t1.intersection_update(t2)  # 相比与intersection，会更新t1只保留交集的内容
t1.difference_update(t2)    # 相比与difference，会更新t1只保留差集的内容
t1.symmetric_difference_update(t2)  # 相比与symmetric_difference，会更新t1只保留对称差集的内容


#collections.OrderedDict() 有序字典
from collections import OrderedDict

