# -*- coding:utf-8 -*-
# 数组中出现次数超过一半的数字
# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，
# 超过数组长度的一半，因此输出2。如果不存在则输出0。

#方法1:频率超过一半,排序后一定在最中间,即数组中第n/2大的数-->partition
#方法2:参考选班长唱票

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        