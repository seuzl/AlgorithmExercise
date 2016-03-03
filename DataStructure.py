# -* - coding: UTF-8 -* -
import heapq
import collections

# string
a='hello'
print('---------------- 获取index --------------')
print a.index('e')
print a.find('l')

# linked list
class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    #单链表反转
    def reverse(self,head):
        prev = None
        while head:
            head.next = prev
            prev = head
            head = head.next
        return prev

# ?????? 如何测试
# LN0 = ListNode(0)
# LN1 = ListNode(1)
# LN2 = ListNode(2)
# LN0.next = LN1
# LN1.next = LN2
# New = .reverse(LN0)
# print(New.val)

# 双向 linked list
class DListNode:
    def __init__(self,val):
        self.val = val
        self.prev = self.next = None

# Binary Tree
class TreeNode:
    def __index__(self,val):
        self.val = val
        self.left,self.right = None, None

# priority queue(优先队列--用最小/最大堆实现)
# python 中用 heapq 实现最小堆
heap=[]
heapq.heapify(heap)   #初始化

heapq.heappush(heap,7)     #插入,复杂度 O(logn)
heapq.heappush(heap,70)
heapq.heappush(heap,40)
heapq.heappush(heap,30)
heapq.heappush(heap,9)

heapq.heappop(heap)    #删除,复杂度 O(logn),永远删除heap[0],

print('----------------- 优先队列 ----------------')
print(heap)

# deque 双端队列(可在任一端插入/删除(注意不能在中间插入),同时具有栈和队列的性质)
# python 中用 collection.deque() 实现
# 插入/查询复杂度 O(1)
dq=collections.deque()
dq.appendleft(0)
dq.appendleft(1)
print('----------------- 双端队列 ------------------')
print(dq)
dq.append(2)
dq.append(3)
print(dq)

dq.popleft()
print(dq)
dq.pop()
print(dq)

print dq[0]
print dq[-1]

# stack 栈(list实现即可)
stack = []
stack.append(0)
stack.append(1)
print('-------------------- 栈 ----------------------')
print(stack)
print(stack[-1])   #取栈顶元素
stack.pop()
print(stack)
print(len(stack)==0)

# set 不可重复
s=set()
s={1,2,3}     #可看作只有key的dict
print('-------------------- set ---------------------')
print(s)
s.add(1)
s.add('zhaolei')
print(s)
s.remove(1)
print(s)

# map (哈希表,就是dict)
hash_map = {}
hash_map['zhao']='lei'
hash_map['hello']='world'
print('-------------------- map ---------------------')
print(hash_map)
print 'zhao' in hash_map   #只能查 key
print(hash_map['zhao'])
hash_map.pop('zhao')
print(hash_map.keys())
for key,value in hash_map.items():
    print(key,'-',value)
print(len(hash_map))

# 图
f = [0 for _ in range(4)]
print(f)
# 初始化一个邻接矩阵(二维数组)
g = [[0 for _ in range(4)] for _ in range(4)]
print(g)

# 有向图
class DirectedGraphNode:
    def __int__(self,label):
        self.label = label
        self.neighbors = []   #邻接边

# 无向图定义相同,只是建图时双向加
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

c=collections.Counter("aaddbc")
print('-------------------- 统计词频 ---------------------')
print(c['a'])








