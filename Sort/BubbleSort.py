# -* - coding: UTF-8 -* -

def bubbleSort(array):
    for i in xrange(len(array)):
        for j in xrange(1,len(array)-i):
            if array[j-1]>array[j]:
                array[j],array[j-1] = array[j-1],array[j]
    return array

unsortArray=[6,5,3,1,8,4,2]
print bubbleSort(unsortArray)

# 优化:

# 优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
# 用一个标记记录这个状态即可。

# 优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
# 如[3,1,4,2,6,7,8]后三个本来就有序,没必要再循环到后面了

# 最优:
def bubbleSort_bettet(array):
    k=len(array)   #优化2
    for i in  xrange(len(array)):
        flag = 1   #优化1
        for j in xrange(1,k):
            if array[j-1]>array[j]:
                array[j],array[j-1]=array[j-1],array[j]
                k=j
                flag=0
        if flag:
            break
    return array

unsortArray=[6,5,3,1,8,4,2]
print bubbleSort(unsortArray)

# 分析:
# 时间O(n^2)
# 稳定