# -* - coding: UTF-8 -* -
# 用一条语句判断一个整数是不是2的整数次方
# 如果是的话肯定只有一个1
# n&(n-1)==0
def isTwo(n):
    return not n&(n-1)

print(isTwo(8))
print(isTwo(9))