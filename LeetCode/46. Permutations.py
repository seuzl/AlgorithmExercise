# -*- coding:utf-8 -*-
class Solution(object):
    def permute(self, nums):
        if nums is None:return [[]]
        if len(nums)<=1:return [nums]
        result=[]
        for i,item in enumerate(nums):
            for p in self.permute(nums[:i]+nums[i+1:]):
                result.append(p+[item])
        return result

s=Solution()
print(s.permute([1,2,3]))