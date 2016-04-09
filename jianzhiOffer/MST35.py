# -*- coding:utf-8 -*-
# 第一个只出现一次的字符位置
# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符的位置。
# 若为空串，返回-1。位置索引从0开始
# 两次遍历字符串
# 第一次遍历:将字符和对应出现频次纪录在 hash 表
# 第二次遍历:依据 hash 表中纪录的次数找出第一个次数=1的

class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None:
            return -1
        ss,dic=list(s),{}
        for p in ss:
            if not dic.has_key(p):
                dic[p]=1
            else:
                dic[p]+=1
        for i in xrange(len(ss)):
            if dic[ss[i]]==1:
                return i
        return -1

s=Solution()
print(s.FirstNotRepeatingChar("abaccdeff"))