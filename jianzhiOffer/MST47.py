# -*- coding:utf-8 -*-
# 不用加减乘除做加法
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
# 不能用+-*/,则考虑用位运算
# 位运算是针对二进制的.
# 两数相加过程:
# 1:先不考虑进位,相加(该步运算结果同异或结果)
# 2:考虑进位,计算进位是多少(该步等同于先与,再左移一位)
# 3:将1\2结果相加(步骤同上)


class Solution:
    def Add(self, num1, num2):
        sum=0
        while(num2!=0):
            sum=num1^num2
            num2=(num1&num2)<<1
            num1=sum
        return num1

s=Solution()
print(s.Add(100,200))