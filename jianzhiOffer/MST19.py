# -*- coding:utf-8 -*-
# 反转二叉树
# 二叉树的镜像定义：源二叉树
#     	    8
#     	   /  \
#     	  6   10
#     	 / \  / \
#     	5  7 9 11
#     	镜像二叉树
#     	    8
#     	   /  \
#     	  10   6
#     	 / \  / \
#     	11 9 7  5
#仿照前序遍历进行递归交换左右子树

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if not root:
            return
        root.left,root.right=root.right,root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return root