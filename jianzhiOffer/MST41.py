# -*- coding:utf-8 -*-
# 和为S的两个数字
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
# 如果有多对数字的和等于S，输出两个数的乘积最小的。

# 方法一:暴力,选择一个数,然后依次判断其与剩余数字的和是否为tsum-->O(n^2)
# 方法二:数组有序==>二分查找
# 两个指针一首一尾,判断和,和>tsum,rp往前,<sum,lp往后

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array is None or len(array)<2:
            return []
        results,multiplyResults=[],[]
        lp,rp=0,len(array)-1
        while(lp<rp):
            sum=array[lp]+array[rp]
            if sum<tsum:
                lp+=1
            elif sum>tsum:
                rp-=1
            else:
                results.append([array[lp],array[rp]])
                lp+=1
                rp-=1
        if len(results)<1:
            return []
        else:
            for p in results:
                multiplyResults.append(p[0]*p[1])
        return  sorted(results[multiplyResults.index(min(multiplyResults))])


s=Solution()
print(s.FindNumbersWithSum([1,2,4,7,11,15],15))