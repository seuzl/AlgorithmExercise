# -*- coding:utf-8 -*-
# 平衡二叉树
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。
# 方法一(前序遍历):
#       计算左右子树深度,二者差绝对值<2,判断完根结点,在判断根结点的两个孩子
#       也就是要求本树/左/右子树也都是平衡二叉树
#       这种方法会重复遍历许多结点,复杂度高
# 方法二(后序遍历):
#       每次遍历结点的时候,该结点的左右子树均已被遍历过
#       如果左右子树都满足平衡二叉树的话,根据左右孩子深度更新该结点深度值
#       这里在参数列表以传应用的方式传递&depth参数,以达到在函数体内计算并修改&depth的目的

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 方法一
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        leftDepth=self.TreeDepth(pRoot.left)
        rightDepth=self.TreeDepth(pRoot.right)
        diff=leftDepth-rightDepth
        if diff>1 or diff<-1:
            return False
        # 要求左子树和右子树也都是平衡二叉树
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        if not pRoot:
            return 0
        leftDepth=self.TreeDepth(pRoot.left)
        rightDepth=self.TreeDepth(pRoot.right)
        if leftDepth>rightDepth:
            return leftDepth+1
        else:
            return rightDepth+1

#   方法二(由于不了解python中如何传引用,此处用C++):
#
# class Solution {
# public:
#     bool isBalanced(TreeNode* root) {
#         int depth=0;
#         return isBalanced(root,&depth);
#     }
#     bool isBalanced(TreeNode* root,int *depth){
#         if(root==NULL){
#             *depth=0;
#             return true;
#         }
#         int leftDepth,rightDepth;
#         if(isBalanced(root->left,&leftDepth)&&isBalanced(root->right,&rightDepth)){
#             int diff=leftDepth-rightDepth;
#             if(diff<=1 && diff>=-1){
#                 *depth=1+(leftDepth>rightDepth?leftDepth:rightDepth);
#                 return true;
#             }
#         }
#         return false;
#     }
# };





