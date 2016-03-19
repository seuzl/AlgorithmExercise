# -* - coding: UTF-8 -* -
# 调整数组顺序使奇数位于偶数前面
# 借鉴快排 partition做法
# 注意这类问题可以归结为:将数组按照某种规则分成两部分,一部分在前,另一
# 部分在后,while()条件可以抽象成一个bool函数.解法都可以借鉴快排的partition

class Solution:
    # 借鉴快排思想:不能保证相对位置不变(不稳定)
    def reOrderArray(self, array):
        l,r=0,len(array)-1
        while(l<=r):
            while l<=r and array[l]&1==1:
                l+=1
            while l<=r and array[r]&1==0:
                r-=1
            if l>r:
                break
            array[l],array[r]=array[r],array[l]
        return array

#     借鉴插入排序思想
    def reOrderArray2(self, array):
        for i in xrange(1,len(array)):
            if array[i]&1==1:
                # 注意要有index记录插入位置,tmp记录原数字
                index,tmp=i,array[i]
                for j in xrange(i-1,-1,-1):
                    if array[j]&1==0:
                        array[j+1]=array[j]
                        index=j
                    else:
                        break
                array[index]=tmp
        return array

s=Solution()
print s.reOrderArray2([2,4,6,1,3,5,7])