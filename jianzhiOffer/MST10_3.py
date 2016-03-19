# -* - coding: UTF-8 -* -
# 计算m变成n需要变化多少位

def changeCount(m,n):
    result,flag=0,m^n
    while(flag):
        result+=1
        flag=flag&(flag-1)
    return result

print(changeCount(10,13))

