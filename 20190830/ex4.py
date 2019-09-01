# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:47:45 2019

@author: carrie
"""
from functools import total_ordering # import裝飾器
@total_ordering # 相當於Box = total_ordering(Box)，能夠通過實現好的__eq__\__lt__推導出其他運算方式
class Box():
    def __init__(self,ival):
        self.value = ival 
    # 這是一個已經被python3.X遺棄的方法
    def __cmp__(self,other):
        if self.value < other.value:
            return -1
        elif self.value > other.value:
            return 1
        else:
            return 0
    # 必須實現equal和其他另一個函數裝飾器才能工作
    # equal
    def __eq__(self, other):
        return self.value == other.value
    # less than
    def __lt__(self, other):
        return self.value < other.value
    
    def __add__(self,other):
        return Box(self.value + other.value)
 

print(Box(3) + Box(4))
   