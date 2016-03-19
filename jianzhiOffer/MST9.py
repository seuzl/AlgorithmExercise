# -* - coding: UTF-8 -* -
# 斐波那契数列
# 递归效率低
# 用循环解决

class Solution:
    # case1:递归解法
    def FibonacciStack(self, n):
        if n<=0:return 0
        if n==1:return 1
        return self.FibonacciStack(n-1)+self.FibonacciStack(n-2)
    # case2:非递归
    def Fibonacci(self, n):
        alist=[0,1]
        if n<2:return alist[n]
        for i in xrange(2,n+1):
            alist.append(alist[i-1]+alist[i-2])
        return alist[n]

s=Solution()
print(s.Fibonacci(5))