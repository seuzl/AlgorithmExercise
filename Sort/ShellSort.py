# -* -coding: UTF-8 -* -
# 分组插入排序,增量递减,更高效--权衡了子数组的规模和有序性。

def shellSort(arr):
    n=len(arr)
    gap=int(round(n/2))
    while gap>0:
         for i in xrange(gap,n):
            tmp=arr[i]
            index=i     #先备份位置和元素,然后再找正确的插入位置
            while(index>=gap and arr[index-gap]>tmp):  #这一while循环是为arr[i]寻找合适的插入位置
                arr[index],index=arr[index-gap],index-gap  #发现前面有大的,往后移,游标往前移
            # 跳出while表明找到插入位置
            arr[index]=tmp
         gap=int(round(gap/2))
    return arr

unsortArr=[4,3,6,5,8,2]
print(shellSort(unsortArr))






