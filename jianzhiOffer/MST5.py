# -* - coding: UTF-8 -* -
# 倒序打印链表
# 递归,先打印list[1:],再打印list[0]

class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution():
    alist=list()
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return
        if listNode.next:
            self.printListFromTailToHead(listNode.next)
        self.alist.append(listNode.val)
        return self.alist

    def print2(self,listNode):
        while(listNode):
            self.alist.append(listNode.val)
            listNode=listNode.next
        return self.alist[::-1]

s=Solution()
head=ListNode(5)
parentNode=head
for i in xrange(1,4):
    node=ListNode(i)
    parentNode.next=node
    parentNode=node
# print s.printListFromTailToHead(head)
print(s.print2(head))