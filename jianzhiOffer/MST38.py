# -*- coding:utf-8 -*-
# 数字在排序数组中出现的次数
# 排序数组-->二分查找.
# 先找出第一个出现的位置first
# 再找出最后一个出现的位置last
# last-first+1即是出现次数
# 找first和end的方法都是二分查找法

class Solution:
    def GetNumberOfK(self, data, k):
        if not data or len(data)<1:
            return 0
        first=self.getFirstK(data,k,0,len(data)-1)
        last=self.getLastK(data,k,0,len(data)-1)
        if first>=0 and last>=0:
            return last-first+1
        else:
            return 0

    def getFirstK(self,data,k,start,end):
        if not data or start>end:
            return -1
        mid=(start+end)/2
        if data[mid]>k:
            end=mid-1
        elif data[mid]<k:
            start=mid+1
        else:
            # 判断是不是第一个出现
            if mid-1>=start and data[mid-1]==k:
                end=mid-1
            else:
                return mid
        return self.getFirstK(data,k,start,end)

    def getLastK(self,data,k,start,end):
        if not data or start>end:
            return -1
        mid=(start+end)/2
        if data[mid]>k:
            end=mid-1
        elif data[mid]<k:
            start=mid+1
        else:
            # 判断是不是最后一个出现
            if mid+1<=end and data[mid+1]==k:
                start=mid+1
            else:
                return mid
        return self.getLastK(data,k,start,end)

s=Solution()
print(s.GetNumberOfK([1,3,3,3,3,4,5],2))