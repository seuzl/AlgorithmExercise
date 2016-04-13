# -*- coding:utf-8 -*-
# 把字符串转换成整数
# 注意cornerCase:
# 合法输入:只允许s[0]为'+'/'-'表示正负,其它必须是0~9
# 当输入空指针或其它非法输入,返回0,但需要一个全局变量flag标志
# result==0 and flag==0:非法输入
# result==0 and flag==1:表示输入的是'0'
# 注意python不像C++,两个字符可以直接相减,从而通过-'0'获得ascii值
# python只能通过 ord('c')得到ascii值再相减
# ascii->字符:chr

class Solution:
    # flag标记输入是否合法,minus标记是否为负
    flag,result,minus=1,0,0
    def StrToInt(self, s):
        if s is None or s=="":
            self.flag=0
            return 0

        ss,p=list(s),0
#       判断正负
        if ss[0]=='-':
            self.minus=1
            p=1
        elif ss[0]=='+':
            p=1
        for i in ss[p:]:
            # 检查非法输入
            if i<'0' or i>'9':
                self.flag=0
                return 0
            self.result=self.result*10+(ord(i)-ord('0'))
        if self.minus:
            return 0-self.result
        return self.result

s=Solution()
print(s.StrToInt("1daj278"))