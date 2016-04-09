# -*- coding:utf-8 -*-
# 连续子数组的最大和
# 遍历数组,如果当前值<0,则先tmp保留sum(因为要加负数,tmp就可能是最终的最大值),再sum+=array[i]
# 每一次加的结果要跟当前值比较,如果sum<当前值,说明前面的一堆数拖累了当前值,
# 把前面的都舍弃掉,从当前值开始往后加
# 遇到负数时不直接舍弃,而是用tmp保留当前和,是期望负数后边的正数会弥补它,如果弥补得了就取最后的sum,弥补不了就取tmp

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array is None or len(array)<=0:return 0
        if len(array)==1:return array
        tmp,sum=array[0],array[0]
        for i in xrange(1,len(array)):
            if array[i]<0 and tmp<sum:
                tmp=sum
            sum+=array[i]
            # 前面的拖累了当前值
            if sum<array[i]:
                sum=array[i]
        if tmp>sum:return tmp
        else:return sum


s=Solution()
print(s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))