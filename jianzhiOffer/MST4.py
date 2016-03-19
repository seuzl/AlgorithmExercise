# -* - coding: UTF-8 -* -

# 替换空格为20%
# 设置两个指针,从后往前遍历,遇到空格插入

import collections
class Solution():
    def replaceSpace(self,s):
        if not s:
            return s
        blankNum=collections.Counter(s)[' ']
        if blankNum==0:
            return s
        new=range(len(s)+blankNum*2)
        l,r=len(s)-1,len(s)+blankNum*2-1
        while(l>=0):
            if s[l]!=' ':
                new[r]=s[l]
                l,r=l-1,r-1
            else:
                new[r],new[r-1],new[r-2]='0','2','%'
                l,r=l-1,r-3
        return "".join(new)

    def replace(self,ss):
        if not ss:return ss
        slist=list(ss)
        index=0
        while index<len(slist):
            if slist[index]==' ':
                # slist.replace(index,'%20')
                slist[index]='%20'
                index+=3
            else:
                index+=1
        return "".join(slist)

tmp="hello world."
s=Solution()
# print s.replaceSpace(tmp)
print(s.replace(tmp))

