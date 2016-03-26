# -*- coding:utf-8 -*-
# 二叉树中和为某一值的路径

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root or not expectNumber:
            return
        nodeList,tmpList,result=list(),list(),list
        # 先一直向左找
        nodeList.append(root)
        while(root.left):
            nodeList.append(root.left)
            root=root.left
        # 如果当前结点(root)是叶结点,计算和
        if not root.right:
            if self.isEqualToExpectedNum(nodeList,expectNumber):
                for node in nodeList:
                    result.append(node.val)
            else:
                



    def isEqualToExpectedNum(self,nodeArray,num):
        result=0
        for node in nodeArray:
            result+=node.val
        if result==num:
            return True
        else:
            return False