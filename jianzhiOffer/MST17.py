# -*- coding:utf-8 -*-
# 合并两个排序的链表,要求合并后依旧有序
# 方法一:归并排序
# 方法二:递归

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    head=ListNode(0)
    # 借鉴归并排序
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val<pHead2.val:
            self.head,tmp=pHead1,pHead1
            pHead1=pHead1.next
        else:
            self.head,tmp=pHead2,pHead2
            pHead2=pHead2.next
        while pHead1 and pHead2:
            if pHead1.val<pHead2.val:
                tmp.next=pHead1
                pHead1=pHead1.next
            else:
                tmp.next=pHead2
                pHead2=pHead2.next
            tmp=tmp.next
        if pHead1:
            tmp.next=pHead1
        elif pHead2:
            tmp.next=pHead2
        return self.head

    # 递归-->效率比方法1低
    def Merge2(self,phead1,phead2):
        if not phead1:
            return phead2
        if not phead2:
            return phead1
        if phead1.val<phead2.val:
            self.head=phead1
            self.head.next=self.Merge2(phead1.next,phead2)
        else:
            self.head=phead2
            self.head.next=self.Merge2(phead1,phead2.next)
        return self.head