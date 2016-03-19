# -* - coding: UTF-8 -* -
# 旋转数组的最小数字
# 有序数组-->二分查找
# case1:[3,4,5,1,2]
# case2:[1,2,3,4,5]
# case3:[1,0,1,1,1]

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # corner case:
        if not rotateArray or len(rotateArray)==0:
            return rotateArray
        l,r,mid=0,len(rotateArray)-1,0
        # case2:返回首个元素
        if rotateArray[l]<rotateArray[r]:
            return rotateArray[l]
        while l+1<r:
            mid=(l+r)/2
        # case 3:
            if rotateArray[l]==rotateArray[r]==rotateArray[mid]:
                # 只能遍历
                return self.findMin(rotateArray[l:r+1])
        # case 1:
            if rotateArray[mid]>=rotateArray[l]:
                l=mid
            else:
                r=mid
        return rotateArray[r]


    def findMin(self,array):
        result=array[0]
        for i in xrange(1,len(array)-1):
            if array[i]<result:
                result=array[i]
        return  result

s=Solution()
print s.minNumberInRotateArray([3,4,5,1,2])