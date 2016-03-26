# -*- coding:utf-8 -*-
# 字符串的排列(全排列)
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
# 结果请按字母顺序输出。
# 递归,每次取一个为标准,对剩下的元素进行全排,ss[0]+allRange(ss[1:])就是结果

class Solution:
    # 全排列
    def Permutation(self, ss):
        if ss is None:
            return []
        sss=list(ss)
        if len(sss)<=1:
            return sss
        result=[]
        for i,item in enumerate(sss):
            for p in self.Permutation("".join(sss[:i]+sss[i+1:])):
                result.append(p+item)
        # 去重用set,排序用sorted
        return sorted(set(result))

    # 全组合
    def AllCombine(self,ss):
        if ss is None:
            return []
        sss=list(ss)
        if len(sss)<=1:
            return sss
        result=self.AllCombine("".join(sss[1:]))
        # 注意此处不能用for p in result来遍历,因为for内result会发生变化
        # result发生变化后返回来再判断,死循环
        for i in xrange(len(result)):
            result.append(sss[0]+result[i])
        result.append(sss[0])
        return sorted(set(result))

s=Solution()
print(s.Permutation("aac"))
print(s.AllCombine("abc"))