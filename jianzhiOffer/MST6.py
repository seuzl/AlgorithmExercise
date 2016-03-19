# -* - coding: UTF-8 -* -
# 根据前序+中序遍历数组还原二叉树
# 前序确定根,中序确定左右子树范围
# 递归,每次返回根(root.value,root.left,root.right)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 入口函数
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        if len(preorder)==0 or len(inorder)==0:
            return None
        if len(preorder)!=len(inorder):
            return None
        root=self.helper(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1)
        return root

    # 核心,该函数返回树的root结点.由root可遍历树.树类问题最后如果要返回树,实际是让你返回root
    # root有三个成员变量,首先root.val=preOrder[preStart].
    # root.left以及root.right又是构建树,所以各自递归
    # 关键在于根据root在inorder中的index得出构造子树时的preOrder和inOrder范围!!
    def helper(self,preorder,preStart,preEnd,inorder,inStart,inEnd):
        if preStart>preEnd or inStart>inEnd:
            return
        root=TreeNode(preorder[preStart])
        index=self.findIndex(preorder[preStart],inorder,inStart,inEnd)
        root.left=self.helper(preorder,preStart+1,preStart+index-inStart,inorder,inStart,index-1)
        root.right=self.helper(preorder,preStart+index-inStart+1,preEnd,inorder,index+1,inEnd)
        return root

    # 辅助函数:找根结点在inorder中的index
    def findIndex(self,rootVal,inorder,inStart,inEnd):
        for i in xrange(inStart,inEnd+1):
            if inorder[i]==rootVal:
                return i
        return -1