# -*- coding:utf-8 -*-
# 二叉树的深度
# 输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，
# 最长路径的长度为树的深度。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        leftDepth=self.TreeDepth(pRoot.left)
        rightDepth=self.TreeDepth(pRoot.right)
        if leftDepth>rightDepth:
            return leftDepth+1
        else:
            return rightDepth+1