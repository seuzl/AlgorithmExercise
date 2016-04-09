# -*- coding:utf-8 -*-
#最小的K个数
#输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
#方法一:利用快排partition,O(n)时间得到数组中第k大的数,再把前面的排序就是了
#方法二:引入辅助容器,先装满前k个数,每添加一个新数进来和当前容器中的最大数进行比较
#如果比最大数小就替换,反之不处理.由于涉及删除最大数,可用最大堆实现

import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # 注意 tinput is None 和 len(tinput)是两码事,写 cornerCase 的时候要注意如果参数
        # 有list类型,要两种情况都考虑
        if tinput is None or k is None or k<=0 or k>len(tinput) or len(tinput)<=0:
            return []
        l,r,index=0,len(tinput)-1,0
        while(l<=r):
            index=self.partition(tinput,l,r)
            if index==k-1:
                return self.qsort(tinput[:k])
            elif index>k-1:
                r=index-1
            else:
                l=index+1
        return

    def partition(self,numbers,l,r):
        lp,rp,key=l+1,r,numbers[l]
        while(lp<=rp):
            while lp<=rp and numbers[lp]<key:
                lp+=1
            while lp<=rp and numbers[rp]>=key:
                rp-=1
            if lp>rp:
                break
            numbers[lp],numbers[rp]=numbers[rp],numbers[lp]
        numbers[l],numbers[rp]=numbers[rp],numbers[l]
        return rp

    def qsort(self,numbers):
        if len(numbers)<=1:return numbers
        l,r=0,len(numbers)-1
        rp=self.partition(numbers,l,r)
        self.qsort(numbers[l:rp])
        self.qsort(numbers[rp+1:r])
        return numbers

    def GetLeastKNumbers(self,tinput,k):
        if tinput is None or k is None or k>len(tinput) or k<=0:
            return []
        heapq.heapify(tinput)
        return heapq._nsmallest(k,tinput)




s=Solution()
print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3],5))
# print(s.GetLeastKNumbers([4,5,1,6,2,7,3],5))