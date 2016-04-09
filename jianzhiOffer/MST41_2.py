# -*- coding:utf-8 -*-
# 和为S的连续正数序列(至少包含两个数)
# 输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

# 指针法:初始lp指向1,rp指向2
# 计算sum(range(lp,rp+1)),结果>tsum,则lp往右移,<tsum,则rp往右移(都是向右)

class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum is None or tsum<3:
            return []
        lp,rp,results=1,2,[]
        while(lp<=tsum/2):
            tmpSum=sum(range(lp,rp+1))
            if tmpSum<tsum:
                rp+=1
            elif tmpSum>tsum:
                lp+=1
            else:
                results.append(range(lp,rp+1))
                rp+=1
        return results

s=Solution()
print(s.FindContinuousSequence(15))
