# coding:utf-8

import os,time
from collections import OrderedDict
from operator import itemgetter
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