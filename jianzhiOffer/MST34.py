# -*- coding:utf-8 -*-
# 把只包含因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含因子7。
# 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。

# 方法一:一个一个挨个判断--超时!
class Solution:
    def GetUglyNumber_Solution(self, index):
        if not index:
            return
        number,count=0,0
        while(count<index):
            number+=1
            if self.IsUglyNum(number):
                count+=1
        return number

    def IsUglyNum(self,number):
        while(number%2==0):
            number/=2
        while(number%3==0):
            number/=3
        while(number%5==0):
            number/=5
        if number==1:
            return True
        else:
            return False

#方法二:某个位置的丑数一定是由它前面的某个丑数x2/x3/x5得到的,因此只要计算已有丑数x2/x3/x5即可
# 设现有最大丑数为max
# 不必所有丑数都计算,x2/x3/x5都有一个分界点,在此之前x2/x3/x5的结果都<=max,从结点开始x2/x3/x5>max
# 而下一个丑数一定是这三个结点中最小的.
# 所以只要保留三个结点的位置即可,前面的不必再算了
class AnotherSolution:
    def GetUglyNumber_Solution(self, index):
        if not index:
            return 0
        numlist=[1]
        count,p2,p3,p5=0,0,0,0
        while(count<index-1):
            count+=1
            numlist.append(min(numlist[p2]*2,numlist[p3]*3,numlist[p5]*5))
            while(numlist[p2]*2<=numlist[count]):
                p2+=1
            while(numlist[p3]*3<=numlist[count]):
                p3+=1
            while(numlist[p5]*5<=numlist[count]):
                p5+=1
        return numlist[index-1]

# s=Solution()
s=AnotherSolution()
print s.GetUglyNumber_Solution(0)