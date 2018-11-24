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
            if ip_dict.get(ip):
                ip_dict[ip] += 1
            else:
                ip_dict[ip] = 1
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

file = 'D:\\py3test\\ip.txt'
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