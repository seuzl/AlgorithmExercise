# -*- coding:utf-8 -*-
# 左旋转字符串
# 对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
# 例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
# 这道题类似于以前看过的 "把123456789"-->"678912345"
# 三次反转,分别反转12345/6789 --> 54321/9876,然后整体再反转:678912345

class Solution:
    # s为字符串
    def LeftRotateString(self, s, n):
    # 将字符串分为两部分,分别反转
        if s is None or n is None:
            return ""
        ss=list(s)
        if n>len(ss):
            return ""
        self.ReverseWord(ss,0,n-1)
        self.ReverseWord(ss,n,len(ss)-1)
        self.ReverseWord(ss,0,len(ss)-1)
        return "".join(ss)

    # s 为list
    def ReverseWord(self,s,lp,rp):
        if len(s)<2:
            return s
        while(lp<rp):
            s[lp],s[rp]=s[rp],s[lp]
            lp,rp=lp+1,rp-1

s=Solution()
print(s.LeftRotateString("abcXYZdef",3))