#!/usr/bin/env python
# coding=utf-8

import time
def tail(f):
  f.seek(0,2)#移动到文件EOF
  while True:
    line = f.readline() #读取文件中新的文本行
    if not line:
      time.sleep(0.1)
      continue
    yield line

def grep(lines,searchtext):
  for line in lines:
    if searchtext in line:
      yield line

flog = tail(open('warn.log'))
pylines = grep(flog,'python')
for line in pylines:
  print ( line, )
#当此程序运行时，若warn.log文件中末尾有新增一行，且该一行包含python,该行就会被打印出来
#若打开warn.log时，末尾已经有了一行包含python，该行不会被打印，因为上面是f.seek(0,2)移动到了文件EOF处
#故，上面程序实现了tail -f warn.log | grep 'python'的功能，动态实时检测warn.log中是否新增现了
