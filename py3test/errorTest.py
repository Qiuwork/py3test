#_*_coding:utf-8_*_
#异常语法块
#语法块形式

# try:
#     code
# except[Exception as e]:
#     processing
# [else:
#     do else
# finally:
#     clean up]
#异常捕获
try:
    5 / 0
except:
    pass
print('well')
#异常查看
import sys
import traceback
try:
    5 / 0
    pass
except Exception as e:
    print(e)
    print(sys.exc_info())
    traceback.print_exc()
#异常类型：
import builtins
dir(builtins)

import traceback
try:
    5 / 0
    pass
except ZeroDivisionError as e:
    traceback.print_exc()
#捕获多个异常
import traceback
try:
    5 / 0
except (ZeroDivisionError,KeyError,IOError) as e:
    traceback.print_exc()
#异常优先级
import traceback
try:
    5 / 0
    pass
except ZeroDivisionError as e:
    traceback.print_exc()
except IOError as e:
    pass
except IOError as e:
    pass
#抛出异常
# raise ValueError("test raise error")
#自定义异常
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

# raise MyError("my error test")
#异常顺序流
try:
    print('start')
    5 / 0
    #return
except Exception as e:
    print('catch except')
    raise Exception()
else:
    print('no except')
    raise Exception()
finally:
    print('in finally')