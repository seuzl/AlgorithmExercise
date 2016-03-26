# -*- coding:utf-8 -*-
# 顺时针打印矩阵
# 问题1:什么时候需要打印下一圈?
# 问题2:打印某一圈时如何判断哪一步是否需要打印?(➡️⬇️⬅️⬆️)

class Solution:
    # matrix类型为二维列表，需要返回列表
    result=list()
    def printMatrix(self,matrix):
        if not matrix:
            return self.result
        # 每一圈开始打印的start总是左上角的元素,即满足startX==startY.[0,0]-->[1,1]-->[2,2]
        rows,columns,start=len(matrix),len(matrix[0]),0
        # 继续打印下一圈的条件
        while(rows>2*start and columns>2*start):
            # 打印一圈
            self.printCircle(matrix,columns,rows,start)
            start+=1
        return self.result

    # 打印一圈
    def printCircle(self,matrix,columns,rows,start):
        endX=columns-1-start
        endY=rows-1-start
        # 第一行肯定要打印:右-->左
        for i in xrange(start,endX+1):
            self.result.append(matrix[start][i])
        # 上-->下:当endY>start
        if endY>start:
            for i in xrange(start+1,endY+1):
                self.result.append(matrix[i][endX])
        # 右-->左
        if endY>start and endX>start:
            for i in xrange(endX-1,start-1,-1):
                self.result.append(matrix[endY][i])
        # 下-->上
        if endX>start and endY-1>start:
            for i in xrange(endY-1,start,-1):
                self.result.append(matrix[i][start])
        # return

s=Solution()
# s.printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# print s.printMatrix([[1,2,3],[4,5,6],[7,8,9]])
# print(s.printMatrix([[2,3]]))
print(s.printMatrix([[1,2],[3,4]]))