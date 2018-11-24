# coding:utf-8

import os,time
from collections import OrderedDict
from operator import itemgetter

#获取文件的IP，并排序输出。
def ip_counter(file, num, sequence = "Desc"):
    if not os.path.isfile(file):
        print("Not a File.")
        return
    elif not os.path.getsize(file):
        print("File is empty.")
        return
    start_time = time.time()
    ip_dict = {}
    ip_result = OrderedDict()
    with open(file, 'r', encoding='utf-8') as f:
        for ip in f:
            ip = ip.strip()
            ip_dict[ip] = ip_dict.setdefault(ip,0) + 1
    if sequence.lower() == "asc":
        ip_dict = OrderedDict(sorted(ip_dict.items(),key = lambda x: x[1]))
    else:
        ip_dict = OrderedDict(sorted(ip_dict.items(), key = lambda x: x[1], reverse = True))
    for key, value in ip_dict.items():
        if num == 0:
            break
        ip_result[key] = value
        num -= 1
    end_time = time.time()
    print(end_time-start_time)
    return ip_result

file = 'e:\\py3test\\ip.txt'
num = 5
print(ip_counter(file, num))

# 取出给定字符串中的数字，并打印出是偶数的字符，当打印次数大于10时退出
def printStr(istr,num):
    if not isinstance(istr, str):
        print("astr is not a string.")
        return
    if not isinstance(num, int):
        print("num is not int.")
        return
    n = 0
    alist = []
    for i in istr:
        if n >= num:
            break
        if i.isdigit() and int(i) % 2 == 0:
            print(i)
            alist.append(i)
            n += 1
    return alist

s = "asdasj678596knxcn2132930knsdns12398mnfsdh234898ncmdnsdkj"
num = 10
print(printStr(s,num))

#找出连续重复字符次数最多的子字符串
a = '''uuuuuueqwoiej231aaaa8230912jdlskdasks22ddddddsdjasjdmnmxczfddfd56555555zmwqeoiqwoizcmmmmmm'''
b = list(a)
n = 1
max = 0
for i in range(len(b)):
    if i >= 1:
        if b[i] == b[i-1]:
            n += 1
        else:
            if max < n:
                max_str = []
                max_str.append(b[i - 1])
                max, n = n, 1
            if max == n:
                max_str.append(b[i - 1])
                max, n = n, 1
            else:
                n = 1
    if i == len(b) - 1 and max <= n:
        max = n
        max_str.append(b[i])
print(max, max_str)
for i in max_str:
    print(i * max)

#字符串反转
teststr = 'asaaq eqwed'
# 字母顺序反转1
print(teststr[::-1])
# 字母顺序反转2
testlist = list(teststr)
if len(testlist) % 2:
    num = int(( len(testlist) - 1 ) / 2)
else:
    num = int(len(testlist) / 2)
for i in range(num):
    testlist[i], testlist[len(testlist)-1-i] = testlist[len(testlist)-1-i], testlist[i]
teststr = ''.join(testlist)
print(teststr)
teststr = 'asaaq eqwed'
#单词顺序反转1
print(" ".join(teststr.split(' ')[::-1]))
#单词顺序反转2
testlist = teststr.split(' ')
if len(testlist) % 2:
    num = int(( len(testlist) - 1 ) / 2)
else:
    num = int(len(testlist) / 2)
for i in range(num):
    testlist[i], testlist[len(testlist)-1-i] = testlist[len(testlist)-1-i], testlist[i]
teststr = ' '.join(testlist)
print(teststr)