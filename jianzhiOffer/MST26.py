# -*- coding:utf-8 -*-
# 复杂链表的复制
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点）。
# 方法1:在原链表每个结点后插入新的复制结点,然后复制random,最后把原/复制链表分开
# 方法2:复制原链表,借助hash表保存原结点与复制结点的对应关系<originNode,copyNode>,然后复制next和random指针

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        ppHead=pHead
        # 第一步:为每个结点复制结点
        while(ppHead):
            tmp=ppHead.next
            copyNode=RandomListNode(ppHead.label)
            ppHead.next=copyNode
            copyNode.next=tmp
            ppHead=tmp
        ppHead=pHead
        # 第二步:为每个复制结点复制random
        while(ppHead):
            # 注意此处必须有if
            # 要保证ppHead.random存在,不然.next会报错
            if ppHead.random:
                ppHead.next.random=ppHead.random.next
            ppHead=ppHead.next.next
        # 第三步:隔离原链表与复制链表
        # 注意:OJ不允许修改原始链表,所以原链表也要分离出来
        head,ppHead,result=pHead,pHead.next,pHead.next
        while(head):
            head.next=ppHead.next
            # 注意if判断
            # 要保证head.next存在,head.next.next才存在
            if head.next:
                ppHead.next=head.next.next
            head=head.next
            ppHead=ppHead.next
        return result

    def CloneWithHash(self,pHead):
        if not pHead:
            return
        ppHead,nodeDict=pHead,dict()
        while(ppHead):
            copyNode=RandomListNode(ppHead.label)
            nodeDict[ppHead]=copyNode
            ppHead=ppHead.next
        ppHead=pHead
        while(ppHead):
            # 注意if判断
            if ppHead.next:
                nodeDict[ppHead].next=nodeDict[ppHead.next]
            # 注意if判断,因为不是所有原结点都有random指针,所以nodeDict[ppHead.random]不一定存在
            if ppHead.random:
                nodeDict[ppHead].random=nodeDict[ppHead.random]
            ppHead=ppHead.next
        return nodeDict[pHead]