# -* - coding: UTF-8 -* -

# 非原地快排(list comprehension--列表生成式--以非常简介的代码生成list)
# 递归
# 基准永远取第一个元素

def qsort1(array):
    # 基本条件:只剩一个元素
    if len(array)<=1:return array
    else:
    # 对基准左边快排+基准+对基准右边快排
        pivot=array[0]
        return qsort1([x for x in array[1:] if x<pivot])+[pivot]+qsort1([x for x in array[1:] if x>=pivot])

unsortArray=[6,5,3,1,8,7,2,4]
# print(qsort1(unsortArray))

# 原地快排
# l:待排序数组下界,u:待排序数组上界,m:分界点(一开始m左边(包括m)都比t小,之后m=t)

# def qsort2(array,l,u):
#     # 递归终止:l u 交叉或相等
#     if l>=u:return array
#     m=l   #m是基准分割点
#     for i in xrange(l+1,u+1):
#         if array[i]<array[l]:
#             m+1
#             array[m],array[i]=array[i],array[m]
# #!!!!!循环结束记得交换array[m],array[l],这一步非常重要,非常容易遗漏!通过这步之后基准就到了正确的位置
#     array[m],array[l]=array[l],array[m]
# #     对m左右两旁递归上述过程
#     qsort2(array,l,m-1)
#     qsort2(array,m+1,u)
#     return array

# print(qsort2(unsortArray,0,len(unsortArray)-1))



#两层循环(内循环有两个)
def qsort(array,l,r):
    if l>=r:return array
    # arr[l]作为target,所以lp开始要向后移一位
    lp,rp,key=l+1,r,array[l]
    while lp<=rp:    #第一个while
        while lp<=rp and array[lp]<key:  #左循环,找不小于(<合法)
            lp+=1
        while lp<=rp and array[rp]>=key:  #右循环,找小于(>=合法)
            rp-=1
        # 这个if..break..是必需的,lp>rp,说明二者发生交叉,但之前二者位置已经排好,不能再执行交换
        if lp>rp:
            break
        array[lp],array[rp]=array[rp],array[lp]
    # 此时rp<lp,所以rp指向的值<arr[l](本来应由lp指向,但二者发生交叉)
    array[l],array[rp]=array[rp],array[l]
    qsort(array,l,rp-1)
    qsort(array,rp+1,r)
    return array

print(qsort(unsortArray,0,len(unsortArray)-1))

