# -* - coding: UTF-8 -* -
#链表中倒数第k个结点
# 注意代码的鲁棒性
# cornerCase1:head=none
# cornerCase2:k=none
# cornerCase3:k=0

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # cornerCase:链表为空,k==0
        if not head or not k:
            return None
        tmp=head
        for i in xrange(1,k):
            tmp=tmp.next
        # cornerCase:k>链表长度
            if not tmp:
                return
        while(tmp.next):
            tmp=tmp.next
            head=head.next
        return head