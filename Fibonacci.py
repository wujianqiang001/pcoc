#!/usr/bin/env python
# coding=utf-8

#第一种实现方法
def fibonacci1():
  a=b=1
  yield a
  yield b
  while True:
    a,b = b,a+b
    yield b

for num in fibonacci1():
  if num > 100:
    break
  print(num),