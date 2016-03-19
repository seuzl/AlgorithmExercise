# -* - coding: UTF-8 -* -
# n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
# 仍是斐波那契

class Solution:
    def rectCover(self, number):
        if number<0:
            return 0
        if number<2:
            return 1
        fib,fib1,fib2=0,1,1
        for i in xrange(2,number+1):
            fib=fib1+fib2
            fib2=fib1
            fib1=fib
        return fib