# -* - coding: UTF-8 -* -

import math

#BOOL
a = 'python'
print a and True

b = True
print b and a

#list--有序,可修改
L = ['zhaolei',0,True]
print(L)

L = ['andy','bob','cathy']
L.append('dog')
print(L)

L.insert(0,'Paul')
print(L)

L.pop(2)
print(L)

#tupple--有序,不可修改
t=('a','b','c')
print(t)
print(t[0])

# set -- 无序,不可重复
s = set(['A','B','C','C'])
print(s)
print(len(s))
print('A' in s)

s.add('D')
print(s)
s.remove('D')
print(s)


# 消除歧义
t=('a',)
print(t)

#if
a=70
if a>60:
    print('pass')
else:
    print('hell')
print('haha')

#while
a=0
sum=0
while a<100:
    a+=1
    sum+=a
print(sum)

s=str(123)
print(s)
i=int(123.5)
print(i)

def sum(L):
    sum=0
    for x in L:
        sum+=x
    return sum
print(sum([1,2,3]))

# 切片(Slice),1--100,不包括101
l=range(1,101)
# 即[1,2,3...100]

# 前10个,注意切片l[begin:end]包含l[begin],不包含l[end]
print(l[:10])
# 3的倍数,第三个参数n表示n个取一个
print(l[2::3])
print l[4:51:5]

def firstCharUpper(s):
    return s[0].upper()+s[1:]
print(firstCharUpper('zhaolei'))

 # enumerate() 函数,把每个元素变成tuple(index,value)
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index,name in enumerate(L):
#enumrate(L)=[(0,'Adam'),(1,'Lisa'),(2,'Bart'),(3,'Paul')]
    print index,'-',name

# zip()函数把两个list变成一个list
L = ['Adam', 'Lisa', 'Bart', 'Paul']
S = range(1,5)
for index,name in zip(S,L):
#zip(S,L)=[(1,'Adam')...]
    print index,'-',name

# 迭代dic,直接for in 迭代的是key,再用dic[key]访问value
# 直接迭代value,用dic.values()或dic.itervalues()
# 同时迭代key,value--items()方法把dic转换为[('Lisa', 85)...]
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
for key in d:
    print key,'-',d[key]

for value in d.values():
    print value

for key,value in d.items():
    print key,'-',value

# 列表生成式--以非常简介的代码生成list
L = range(1,100,2)
# 可生成[1, 3, 5, 7, 9,...]
print [x*(x+1) for x in L]

# range 直接生成 list,支持切片
# xrange 生成的是迭代器  list(xrange_type)才可生成list,不支持切片
# range/xrange 常用于循环(遍历),如果不需要切片操作尽量用 xrange,空间代价小.


L = xrange(1,100,2)
print('----------------- xrange -------------')
print list(L)


# 多层表达式
print [m+n for m in 'abc' for n in '123']

# 高阶函数--函数作为参数
def add(a,b,f):
    return f(a)+f(b)

print add(25,9,math.sqrt)

#map()--对每个元素调用f,返回新的list
def f(x):
    return  x*x
print map(f,[1,2,3])

#reduce()--对每个元素反复调用f,直到返回最终结果
def f(x,y):
    return x+y
print reduce(f,[1,2,3])

#strip(rm)--删除开头\结尾处的rm序列
s='   123   '
print(s.strip())
s='1 23 1'
print(s.strip('1'))

#filter(f,[]) 过滤[]中不符合f的元素
def is_odd(x):
    return x%2==1
print filter(is_odd,[1,2,3,4,5])

# sorted()对list排序
# sorted([],cmp)  自定义cmp比较函数(cmp:如果 x 应该排在 y 的前面，
# 返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。)
def reverse_cmp(x,y):
    if x>y:
        return -1
    elif x<y:
        return 1
    else:
        return 0

print sorted([1,2,3],reverse_cmp)

#匿名函数 lambda,只能有一个表达式
print sorted([1,2,3],lambda x,y:-cmp(x,y))   #reverse_cmp简化
print map(lambda x:x*x,[1,2,3])




