# -*- coding:utf-8 -*-
# 二叉搜索树的后序遍历序列
# 借鉴partition,每次以最后一个元素为基准,前半部分是<,后半部分是>
# 然后再判断这两个子数组是否也符合二叉搜索树(递归)
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        if len(sequence)==1:
            return True
        l,r,end=0,len(sequence)-2,sequence[len(sequence)-1]
        while l<=r and sequence[l]<end:
            l+=1
        while l<=r and sequence[r]>end:
            r-=1
        if r<l:
            leftArr,rightArr=sequence[:r+1],sequence[l:len(sequence)-1]
            if leftArr and rightArr:
                return self.VerifySquenceOfBST(leftArr) and self.VerifySquenceOfBST(rightArr)
            if leftArr and not rightArr:
                return self.VerifySquenceOfBST(leftArr)
            if rightArr and not leftArr:
                return self.VerifySquenceOfBST(rightArr)
        else:
            return False

s=Solution()
# print(s.VerifySquenceOfBST([5,7,6,9,10,11,8]))

print(s.Verify([5]))