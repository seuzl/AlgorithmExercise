# -* - coding: UTF-8 -* -

def insertSort(array):
    for i in xrange(1,len(array)):
        if array[i]<array[i-1]:
            tmp=array[i]
            index=i        #记录插入位置,这里是初始位置
            for j in xrange(i-1,-1,-1):   #从i-1循环到0(包括0),注意倒着循环方式
                if array[j]>tmp:
                    array[j+1]=array[j]  #比tmp大的都后移
                    index=j
                else:
                    break     #找到最终插入位置,退出循环
            array[index]=tmp
    return  array

unsortArray=[6,4,3,8,5,2]
print insertSort(unsortArray)

# 时间O(n^2) 空间O(1)--tmp  稳定

