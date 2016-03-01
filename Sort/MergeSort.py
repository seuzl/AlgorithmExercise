# -* - coding: UTF-8 -* -
def mergeSort(array):
    # 先递归分解,最基本情况为每个数组一个元素
    if len(array)<=1:
        return array
    mid=int(len(array)/2)
    leftArr=mergeSort(array[:mid])
    rightArr=mergeSort(array[mid:])
    #再合并数组
    return merge(leftArr,rightArr)

def merge(left,right):
    l=r=0  #初始下标指针
    result=[]
    while l<len(left) and r<len(right):
        if(left[l]<right[r]):
            result.append(left[l])
            l+=1
        else:
            result.append(right[r])
            r+=1
    #把left或right剩余的都加进来
    result+=(left[l:])
    result+=(right[r:])
    return result

unsortArr=[6,5,3,2,8,4]
print(mergeSort(unsortArr))


