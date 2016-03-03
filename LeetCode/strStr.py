# -* - coding: UTF-8 -* -

class Solution():
    def strStr(self,haystack,needle):
        if haystack is None or needle is None:
            return -1
        if not len(needle):
            return 0
        for i in xrange(len(haystack)-len(needle)+1):
            for j in xrange(len(needle)):
                if haystack[i+j]!=needle[j]:
                    break
            else:  #注意python中的else接的是for不是if,表示no break
                    return i
        return -1

s=Solution()
source="mississipp"
target="issip"
print(s.strStr(source,target))