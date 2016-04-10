# -*- coding:utf-8 -*-
# 扑克牌顺子
# 2个大王,2个小王.随机从中抽出5张牌,看看能不能抽到顺子,
# 大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
# 先排序,统计0和非0个数,再计算顺子需要多少张,减去实际非0个数,则为需要0补全的个数
# 如果需要补全数<=实际0个数,则True,反之False

import collections
class Solution:
    def IsContinuous(self, numbers):
        if numbers is None or len(numbers)!=5:
            return False
        numbers=sorted(numbers)
        print(numbers)
        p,countOf0,end=0,0,len(numbers)-1
        while(numbers[p]==0):
            p+=1
        # 如果有两个非0值相等,则一定不是顺子
        c=collections.Counter(numbers[p:])
        for count in c.values():
            if count>1:
                return False
        countOf0=p
        countExp0=5-countOf0
        countOfContinuous=numbers[end]-numbers[p]+1
        if countOfContinuous-countExp0<=countOf0:
            return True
        return False

s=Solution()
print(s.IsContinuous([1,0,0,1,0]))