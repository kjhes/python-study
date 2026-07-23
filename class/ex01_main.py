# 여기는 ex01_main.py

import ex01_fun
ex01_fun.hello() #함수호출

from ex01_fun import *
hello()

import ex01_fun as f1
f1.hello()