# -*- coding:utf-8 -*-
# 数组中的逆序对
# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组，求出这个数组中的逆序对的总数。

# 方法一:暴力,依次遍历,并与后边的比较,只要小于就组成一个逆序对,复杂度O(n^2)
# 方法二(较难):借鉴归并排序思想,先递归分解,再合并
# 递归分解后先求出子数组的逆序对数,然后进行合并时再计算逆序对数


class Solution:
    def InversePairs(self, data):
        count=0
        if data is None or len(data)<2:
            return 0
        for i in xrange(len(data)):
            for j in xrange(i+1,len(data)):
                if data[i]>data[j]:
                    count+=1
        return count

class SimpleSolution:
    def InversePairs(self, data):
        if data is None or len(data)<2:
            return 0
        copy=[]
        for p in data:
            copy.append(p)
        start,end=0,len(data)-1
        return self.InversePairsCore(data,copy,start,end)


    # 为什么要有copy?
    # 每次递归时data是有序的(只有子数组都有序后才能进行归并,无序时不能归并)
    # copy用于存放排序后的数组
    # 所以leftCount=..(copy,data)这里copy与data的位置要换一下

    # 为什么要有start,end?
    # 由于copy存放的是两个data子数组归并后的数组
    # 大小要足够大,所以不对copy/data进行切片操作,而是始终保持数组完整性,利用下标来区分

    def InversePairsCore(self,data,copy,start,end):
        if end==start:
            copy[start]=data[start]
            return 0
        mid=(end-start)/2
        leftCount=self.InversePairsCore(copy,data,start,start+mid)
        rightCount=self.InversePairsCore(copy,data,start+mid+1,end)
        leftp,rightp,count,copyIndex=start+mid,end,0,end
        while(leftp>=start and rightp>=start+mid+1):
            if data[leftp]>data[rightp]:
                count+=rightp-start-mid
                copy[copyIndex]=data[leftp]
                leftp-=1
            else:
                # 注意必须是前者>后者时count+=1
                # 因为逆序对的定义要求是数组前面的>后面的,二者相对位置不能变
                copy[copyIndex]=data[rightp]
                rightp-=1
            copyIndex-=1
        while(leftp>=start):
            copy[copyIndex]=data[leftp]
            copyIndex-=1
            leftp-=1
        while(rightp>=start+mid+1):
            copy[copyIndex]=data[rightp]
            copyIndex-=1
            rightp-=1
        return leftCount+rightCount+count

# s=Solution()
s=SimpleSolution()
print(s.InversePairs([7,5,6,4]))