# -* - coding: UTF-8 -* -
class Solution():
    def sum(self,array):
        if len(array)==0:return 0
        else:return sum(array[:len(array)-1])+array[len(array)-1]

s=Solution()
print s.sum([1,2,3])