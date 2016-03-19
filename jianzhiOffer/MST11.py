# -* - coding: UTF-8 -* -
# 数值的整数次方
# 实现c++中的power()
# case1:指数>=0-->easy(但要注意高效解法)
# case2:指数为负数-->先求指数绝对值,然后case1,然后取倒数
# case3:底数为0(case3.1:指数>=0:0;case3.2:指数<0--->error)

# 所谓高效解法:PowerWithUnsignedExp

# a^n=a^(n/2)*a^(n/2)当n为偶
# a^n=a^((n-1)/2)*a^((n-1)/2)*a当n为奇

import math
class Solution:
    result=1.0
    # 计算机表示小数(float/double)有误差,不能直接用==判断两个小数是否相等,
    # 如果两个小数差的绝对值很小(比如0.0000001),即可认为相等
    def equal(self,num1,num2):
        if num1-num2>-0.0000001 and num1-num2<0.0000001:
            return True
        else:
            return False

    def Power(self, base, exponent):
        # case3:
        if self.equal(base,0.0):
            if exponent>=0:
                return 0.0
            else:
                return -1.0
        # 这种计算方法效率低,计算时间超过oj限制
        for i in xrange(1,int(math.fabs(exponent))+1):
            self.result*=base
        # case1:
        if exponent>=0:
            return self.result
        # case2:
        else:
            return 1.0/self.result

    def Power2(self,base,exponent):
        if base==0.0:
            if exponent>=0:
                return 0.0
            else:
                return -1.0
        if exponent>=0:
            return self.PowerWithUnsignedExp(base,exponent)
        else:
            return 1.0/self.PowerWithUnsignedExp(base,-exponent)

    def PowerWithUnsignedExp(self,base,exponent):
        # 利用上次计算的结果平方
        if exponent==0:
            return 1.0
        if exponent==1:
            return base
        # 注意这里提高效率的做法:用位操作代替除法,以及判断是否为奇数
        self.result=self.PowerWithUnsignedExp(base,exponent>>1)
        self.result*=self.result
        # 判断是否为奇数,奇数的话还要再乘一次base
        if exponent&1==1:
            self.result*=base
        return self.result

s=Solution()
# print(s.Power(2,-2))
print(s.Power2(2,-2))