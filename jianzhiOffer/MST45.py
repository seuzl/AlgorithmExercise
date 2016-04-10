# -*- coding:utf-8 -*-
# 圆圈中最后剩下的数

class Solution:

    # 方法一:用环链表模拟圆圈,当遍历到尾的时候,从头再开始遍历
    def LastRemaining_Solution(self, n, m):
        if n is None or m is None or n<1 or m<1:
            return -1
        circleList,p=range(n),0
        while(len(circleList)>1):
            p+=m-1
            if p>len(circleList)-1:
                p%=(len(circleList))
            circleList.pop(p)
        return circleList[0]

    # 方法二:分析每一轮删除后剩余数字与下一轮删除后剩余数字之间的规律,用递归解决
    # 时间\空间复杂度优于方法一
    # 关系:f(n,m)=[f(n-1,m)+m]%n-->推导见P231
    def LastRemaining(self,n,m):
        if n is None or m is None or n<1 or m<1:
            return -1
#         基于循环实现
#         最后一轮:f(2,m)=[f(1,m)+m]%2   f(1,m)==0,所以last==0
        last=0
        for i in xrange(2,n+1):
            last=(last+m)%i
        return last


s=Solution()
print(s.LastRemaining_Solution(5,3))
print(s.LastRemaining(5,3))