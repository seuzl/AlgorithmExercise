# -* - coding: UTF-8 -* -
# 判断二进制数有几个1

class Solution:
    # p80解法,python貌似不对,因为数据永远不会溢出,死循环
    # 如果是在c++/java int 最多4*8=32位,最后一定会变为0退出循环
    # 把1逐渐左移,和n相与
    def NumberOf1(self, n):
        count,flag=0,1
        while(flag):
            if n&flag:
                count+=1
            flag=flag<<1
        return count

    # 把n逐渐右移,和1相与
    # 这种解法对当有符号数且为负数时会陷入死循环
    def number2(self,n):
        count,flag=0,1
        while(n):
            if n&flag:
                count+=1
            n=n>>1
        return count

    # n&(n-1)-->结果是把n最右边的1变为0
    # 反复进行此操作,直到n==0,就可以得出有多少个1
    def number3(self,n):
        count=0
        while(n):
            count+=1
            n=n&(n-1)
        return count


s=Solution()
# print(s.NumberOf1(9))
# print(s.number2(9))
print(s.number3(9))