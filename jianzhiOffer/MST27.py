# -*- coding:utf-8 -*-
# 二叉搜索树与双向链表
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。
# 递归:先处理左子树,然后把左子树最大值(一直往右找)与root相连,
# 再处理右子树,然后把右子树最小值(一直往左找)与root相连.
# 不要在意具体递归细节,先默认左子树和右子树各自调用递归函数后就处理好了.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return pRootOfTree
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        # 处理左子树
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while(left.right):
                left=left.right
            pRootOfTree.left,left.right=left,pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while(right.left):
                right=right.left
            pRootOfTree.right,right.left=right,pRootOfTree

        #  最后返回链表头
        while(pRootOfTree.left):
            pRootOfTree=pRootOfTree.left
        return pRootOfTree
