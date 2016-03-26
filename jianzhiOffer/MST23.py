# -*- coding:utf-8 -*-
# 从上往下打印二叉树
# 按层次遍历二叉树
# 数据结构:队列
# A队列存储所有结点
# B队列存储结点的值
# A队列pop的时候将其左右子女(有的话)push到A后面,并将其值push进B队列

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    result,nodeList=list(),list()
    def PrintFromTopToBottom(self, root):
        if not root:
            return
        self.nodeList.append(root)
        while(len(self.nodeList)>0):
            if self.nodeList[0].left:
                self.nodeList.append(self.nodeList[0].left)
            if self.nodeList[0].right:
                self.nodeList.append(self.nodeList[0].right)
            self.result.append(self.nodeList.pop(0).val)
        return self.result

