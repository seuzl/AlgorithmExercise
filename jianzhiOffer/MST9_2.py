# -* - coding: UTF-8 -* -
# 跳台阶
# 看作斐波那契的应用
# 基本条件:第一次跳有两种方法:
# 跳一阶:剩下的有f(n-1)种
# 跳两阶:剩下的有f(n-2)种

class Solution:
    def jumpFloor(self, number):
        if number<=0:
            return 0
        if number<3:
            return number
        return self.jumpFloor(number-1)+self.jumpFloor(number-2)

    # 迭代
    def jump(self,number):
        if number<=0:
            return 0
        if number<3:
            return number
        fib,fib1,fib2=0,2,1
        for i in xrange(3,number+1):
            fib=fib1+fib2
            fib2=fib1
            fib1=fib
        return fib

s=Solution()
print(s.jumpFloor(5))