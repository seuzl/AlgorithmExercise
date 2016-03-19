# -* - coding: UTF-8 -* -
def allRange(array,begin,end):
    if not array:return
    if end==begin:print array
    for i in xrange(begin,end+1):
        array[begin],array[i]=array[i],array[begin]
        allRange(array,begin+1,end)
        array[begin],array[i]=array[i],array[begin]

list=[1,2,3]
allRange(list,0,len(list)-1)