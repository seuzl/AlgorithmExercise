# -*- coding:utf-8 -*-
# 反转链表
# prev引入头结点的前驱
# tmp保存head的后继结点-->防止断裂!!

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        if not pHead:
            return
        prev=None
        while(pHead):
            tmp=pHead.next
            pHead.next=prev
            prev=pHead
            pHead=tmp
        return prev
