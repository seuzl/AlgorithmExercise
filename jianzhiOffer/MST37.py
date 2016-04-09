# -*- coding:utf-8 -*-
# 两个链表的第一个公共结点
# 输入两个链表，找出它们的第一个公共结点。
# 这里只考虑两个无环单链表相交的情况

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return
        len1,len2=0,0
        tmp1,tmp2=pHead1,pHead2
        while(pHead1):
            len1+=1
            pHead1=pHead1.next
        while(pHead2):
            len2+=1
            pHead2=pHead2.next
        if len1>len2:
            forwardSteps=len1-len2
            for i in xrange(forwardSteps):
                tmp1=tmp1.next
        else:
            forwardSteps=len2-len1
            for i in xrange(forwardSteps):
                tmp2=tmp2.next
        while(tmp1 and tmp2):
            if tmp1==tmp2:
                return tmp1
            else:
                tmp1=tmp1.next
                tmp2=tmp2.next
        return None