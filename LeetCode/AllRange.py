# -* - coding: UTF-8 -* -
class Solution():
    def allRange(self,nums):
        if nums is None:
            return []
        if len(nums)==1:
            return [nums]
        result=[]
        for i in xrange(len(nums)):
            nums[i],nums[0]=nums[0],nums[i]
            # 注意这里还要有个for循环,因为allRange函数返回[[2,3][3,2]]
            # 如果直接[nums[0]]+allRange()-->[[1,[[2,3],[3,2]]],...]
            # 所以还要把allRange()返回的list每个元素取出来与nums[0]组合
            for p in self.allRange(nums[1:]):
                result.append([nums[0]]+p)
            nums[i],nums[0]=nums[0],nums[i]
        return result

s=Solution()
print(s.allRange([1,2,3]))