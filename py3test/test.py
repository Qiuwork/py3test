# coding:utf-8


import os,collections
from collections import OrderedDict
from operator import itemgetter

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]


try:
    print(1)
    # 1/0
    # return
except Exception as e:
    print(2)
else:
    print(3)
finally:
    print(4)