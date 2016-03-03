# -* - coding: UTF-8 -* -

def binarySearch(array,target):
    if not array:return -1
    start,end=0,len(array)-1
    while start+1<end:
        mid=(start+end)/2
        if array[mid]<=target:
            start = mid
        else:
            end=mid
    # 最后退出的条件是start+1=end,target一定在二者之间
    if array[start]==target:
        return start
    if array[end]==target:
        return end
    return -1

num=[1,2,3,4,5]
print(binarySearch(num,3))