# -*- coding:utf-8 -*-
# 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，
# 超过数组长度的一半，因此输出2。如果不存在则输出0。

# 方法1:频率超过一半,排序后一定在最中间,即数组中第n/2大的数-->partition
# 方法2:参考选班长唱票

class Solution:
    # 方法一:partition
    def MoreThanHalfNum_Solution(self, numbers):
        if numbers is None or len(numbers)==0:
            return 0
        if len(numbers)==1:
            return numbers[0]
        l,r,index=0,len(numbers)-1,len(numbers)/2
        tmpIndex=self.findCorrectIndex(numbers,l,r)
#       此时number[l]已经到了正确的位置,与index比较
        while(l<r):
            if tmpIndex>index:
                r=tmpIndex-1
                tmpIndex=self.findCorrectIndex(numbers,l,r)
            elif tmpIndex<index:
                l=tmpIndex+1
                tmpIndex=self.findCorrectIndex(numbers,l,r)
            else:
            # rp==index后还要判断频率是不是超过一半
                count=0
                for p in numbers:
                    if p==numbers[tmpIndex]:
                        count+=1
                if count>=len(numbers)/2:
                    return numbers[tmpIndex]
                else:
                    return 0
        return 0

    # 这个类似快排中的partition 操作
    def findCorrectIndex(self,numbers,l,r):
        lp,rp=l+1,r
        while lp<=rp:
            while lp<=rp and numbers[lp]<numbers[l]:
                lp+=1
            while lp<=rp and numbers[rp]>=numbers[l]:
                rp-=1
            if lp>rp:
                break
            numbers[lp],numbers[rp]=numbers[rp],numbers[lp]
        numbers[l],numbers[rp]=numbers[rp],numbers[l]
        return rp


#     选班长唱票
    def MoreThanHalf(self,numbers):
        if numbers is None or not len(numbers):
            return 0
        result,count=0,0
        for p in numbers:
            if count==0:
                result=p
                count+=1
            else:
                if result==p:
                    count+=1
                else:
                    count-=1
                    if count==0:result=0
        if count>0:
            # 判断频率是否真的>一半
            testCount=0
            for q in numbers:
                if q==result:
                    testCount+=1
            if testCount>len(numbers)/2:return result
            else:return 0
        else:return 0

s=Solution()
# print(s.MoreThanHalfNum_Solution([2]))
print(s.MoreThanHalf([1,2,3,4,5]))