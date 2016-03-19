# -* - coding: UTF-8 -* -
# 变态跳台阶
# f(n)=f(n-1)+f(n-2)+f(n-3)+...+f(1)+f(0)
# f(n-1)=f(n-2)+f(n-3)+...+f(1)+f(0)
# f(n)=2f(n-1),等比数列,首项为1
# f(n)=2^(n-1)
# 所以不必用递归

class Solution:
    def jumpFloorII(self, number):
        if number<=0:
            return 0
        if number<3:
            return number
        result=0
        for i in xrange(0,number):
            result+=self.jumpFloorII(i)
        return  result+1

    def jump2(self,number):
        return 1<<(number-1)

s=Solution()
print s.jumpFloorII(6)
print s.jump2(6)