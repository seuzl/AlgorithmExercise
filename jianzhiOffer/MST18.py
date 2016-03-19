# -*- coding:utf-8 -*-
# 输入两颗二叉树A，B，判断B是不是A的子结构。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result=False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result=self.DoesTreeBHasTreeA(pRoot1,pRoot2)
            if not result:
                result=self.DoesTreeBHasTreeA(pRoot1.left,pRoot2)
            if not result:
                result=self.DoesTreeBHasTreeA(pRoot1.right,pRoot2)
        return result

    def DoesTreeBHasTreeA(self,root1,root2):
        if not root2:
            return True
        if not  root1:
            return False
        if root1.val!=root2.val:
            return False
        return self.DoesTreeBHasTreeA(root1.left,root2.left) and self.DoesTreeBHasTreeA(root1.right,root2.right)