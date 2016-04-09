# -* - coding: UTF-8 -* -

def heapSort(array):
    n=len(array)
    # 1\构造最大堆
    first=int(n/2-1)
    for start in xrange(first,-1,-1):  #构造最大堆的顺序是自底向上构造,所以倒着遍历,从最后一个非叶子节点开始往上走
        max_heapify(array,start,n-1)
    # 2\排序,end代表最后一个叶结点(也就是原来的root(最大值)),这个相当于去掉,不用再最大堆调整中考虑
    for end in xrange(n-1,0,-1):
        array[end],array[0] = array[0],array[end]
        max_heapify(array,0,end-1)
    return array



#     最大堆调整
def max_heapify(array,start,end):
    root=start
    while True:
        child=root*2+1
        # 要保证 child 不超过end
        if child>end:break
        # 选出较大的child作为要与root比较的child
        if child+1<end and array[child]<array[child+1]:
            child=child+1
        # 大child与root比
        if array[root]<array[child]:
            array[root],array[child]=array[child],array[root]
            # 交换后的child(原root)作为新的root继续与下边的child比,这种比价仅发生在原root被替换后
            root=child
        else:
            break

print heapSort([5,3,6,7,2,6,3,6,8,9,2])