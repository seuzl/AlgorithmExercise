# -* - coding: UTF-8 -* -
# 用两个栈实现队列
# push:直接stack1.append()
# pop:if stack2 为空,先把stack1元素全部pop->push to stack2
#     else 直接stack2.pop

# 两个队列实现栈:
# push:直接queue1.append
# pop:先把(当前不为空的queue1[注:用两个队列实现栈时每一时刻都必定有一队列为空!])下边的依次pop(0)移到queue2,
# 然后只剩一个元素的queue:queue1.pop(0).如此queue1为空了


class Solution:
    list1,list2=list(),list()
    def push(self, node):
        self.list1.append(node)
    def pop(self):
        if len(self.list2)>0:
            return self.list2.pop()
        elif len(self.list2)==0 and len(self.list1)==0:
            return None
        while len(self.list1)>0:
            self.list2.append(self.list1.pop())
        return self.list2.pop()