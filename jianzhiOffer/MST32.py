# -*- coding:utf-8 -*-
# 整数中1出现的次数（从1到n整数中1出现的次数）
# 方法一:先统计个位上出现1的个数,再依次除10取余求高位的1个数

class Solution:
    # 方法一
    def NumberOf1Between1AndN_Solution(self, n):
        count=0
        if n is None or n==0:
            return count
        for i in xrange(1,n+1):
            tmp=i
            while(tmp):
                if tmp%10==1:
                    count+=1
                tmp/=10
        return count
#         由于数字n有logn位,该法复杂度为O(nlogn),不理想



s=Solution()
print(s.NumberOf1Between1AndN_Solution(213))