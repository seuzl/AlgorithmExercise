# -*- coding:utf-8 -*-
# 数组中只出现一次的数字
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

class Solution:
    def FindNumsAppearOnce(self, array):
        if not array or len(array)<3:
            return [0,0]
        tmp,index,list1,list2=0,0,[],[]
        for p in array:
            tmp^=p
        index=self.findFirst1(tmp)
        for q in array:
            if self.isIndex1(q,index):
                list1.append(q)
            else:
                list2.append(q)
        firstNum,secondNum=0,0
        for i in list1:
            firstNum^=i
        for j in list2:
            secondNum^=j
        return [firstNum,secondNum]

    def findFirst1(self,num):
        # 右数第index为1(第一个)
        index=0
        while(num&1!=1):
            num>>=1
            index+=1
        return index

    # 判断右数第index位是否为1
    def isIndex1(self,num,index):
        num>>=index
        if num&1==1:
            return True
        return False




s=Solution()
# print(s.findFirst1(4))
# print(s.isIndex1(4,2))
print(s.FindNumsAppearOnce([1,2,3,3,4,5,6,6,7]))