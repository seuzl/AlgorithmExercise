# -*- coding:utf-8 -*-
# 翻转单词顺序列
# I am a student. --> student. a am I

class Solution:
    # s为字符串
    def ReverseSentence(self, s):
        if s is None:
            return s
        ss,lp,rp=list(s),0,0

        # 先将每个单词反转
        while(rp<len(ss)):
            while(rp<len(ss) and ss[rp]!=' '):
                rp+=1
            self.ReverseWord(ss,lp,rp-1)
            rp+=1
            lp=rp
        # 整个单词再反转一次
        self.ReverseWord(ss,0,len(ss)-1)
        return "".join(ss)

    # s为list,这里lp,rp,而不用切片操作是因为要修改原list的值.
    # 直接传切片相当于传值,原值不会被修改
    def ReverseWord(self,s,lp,rp):
        if len(s)<2:
            return s
        while(lp<rp):
            s[lp],s[rp]=s[rp],s[lp]
            lp,rp=lp+1,rp-1

s=Solution()
print(s.ReverseSentence("I am a student."))