# -* - coding: UTF-8 -* -
import collections
class Soluciton():
    def anagram(self,s,t):
        s,t=list(s),list(t)
        if len(s)!=len(t):return False
        for i in xrange(len(s)):
            for j in xrange(len(t)):
                if s[i]==t[j]:
                    t.pop(j)
                    break
            else:
                return False
        return True


# 统计词频
class Solution2():
    def anagram(self,s,t):
        return collections.Counter(s)==collections.Counter(t)

so=Soluciton()
s='abcede'
t='beecda'
print(so.anagram(s,t))

so2=Solution2()
s2="abcd"
t2="bcda"
print(so2.anagram(s2,t2))

# Counter(list)用来统计词频,用法:
c=collections.Counter("abbc")
print(c['b'])

#  先排序再比较
class Solution3():
    def anagram(self,s,t):
        return sorted(s)==sorted(t)
