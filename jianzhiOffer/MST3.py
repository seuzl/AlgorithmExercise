# -* - coding: UTF-8 -* -
# 二维数组中的查找()
# P38
# 从右上角开始入手

class Solution():
    def find(self,array,target):
        if not array or not target:return False
        rows,columns=len(array),len(array[0])
        row,column=0,columns-1
        while row<rows and column>=0:
            if array[row][column]==target:return True
            elif array[row][column]>target:
                column-=1
            else:
                row+=1
        return False

s=Solution()
print s.find([[-5]],-2)