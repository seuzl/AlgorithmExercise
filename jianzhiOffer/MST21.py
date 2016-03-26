# -*- coding:utf-8 -*-
# 包含min函数的栈
# 定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
# 引入辅助栈,每push进一个元素都要向辅助栈push截止到现在最小的值(需要把push进栈的值与辅助栈中当前最小的值进行比较)
# 如果新值<辅助栈min,辅助栈 min 换成新值,else:再push一次辅助栈min

class Solution:
    list_data,list_min=list(),list()
    def push(self, node):
        self.list_data.append(node)
        if len(self.list_data)==1:
            self.list_min.append(node)
        elif node<self.list_min[len(self.list_min)-1]:
            self.list_min.append(node)
        else:
            self.list_min.append(self.list_min[len(self.list_min)-1])
        return

    def pop(self):
        if not len(self.list_data):return
        self.list_min.pop()
        return self.list_data.pop()

    def top(self):
        if not len(self.list_data):return
        return self.list_data[len(self.list_data)-1]

    def min(self):
        if not len(self.list_min):return
        return self.list_min[len(self.list_min)-1]