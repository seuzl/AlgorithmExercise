# -*- coding:utf-8 -*-
# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
# 例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
# 方法一:全排列出所有拼接情况,求最小值
# 方法二:重新定义比较比较规则.两个数字分别为m,n
# mn<nm:m<n
# nm<mn:n<m
# mn=nm:m=n
# 将list中的数字按新规则排序,最后将排序后的list拼接.

class Solution:
    def PrintMinNumber(self, numbers):
        if numbers is None:
            return
        if len(numbers)==0:
            return ""
        # 把数字转成字符串,否则拼接的时候相当于两个int数值相加.
        # 由于最后拼接的位数都是相同的,所以直接按字符串的比较规则比较就可以.
        # 没必要再将str转为int
        for i in xrange(len(numbers)):
            numbers[i]=str(numbers[i])
        return min(self.AllRange(numbers))


    def AllRange(self,numbers):
        if numbers is None:
            return
        if len(numbers)<=1:
            return numbers
        result=[]
        for i,item in enumerate(numbers):
            for p in self.AllRange(numbers[:i]+numbers[i+1:]):
                result.append(p+item)
        return result


    # 方法2

    def customCompare(self,m,n):
        if str(m)+str(n)<str(n)+str(m):
            return -1
        elif str(n)+str(m)<str(m)+str(n):
            return 1
        else:
            return 0

    def printminnumber(self,numbers):
        if numbers is None:
            return
        if len(numbers)==0:
            return ""
        resultList=sorted(numbers,self.customCompare)
        resultStr=""
        for p in resultList:
            resultStr+=str(p)
        return int(resultStr)


s=Solution()
# print(s.PrintMinNumber([3,32,321]))
print(s.printminnumber([]))