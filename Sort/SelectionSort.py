# -* - coding: UTF-8 -*-

# 冒泡:每轮循环把最大的排到最后
# 选择:后面的不断跟第一位相比,只要更小就交换,每轮结束后把最小的排到最前

def selectSort(arr):
    for i in xrange(len(arr)):
        min=i
        for j in xrange(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
    return arr

unsortArray=[6,5,3,1,8,4,2]
print(selectSort(unsortArray))

# T:O(N^2),S:O(1),不稳
