# -*- coding:utf-8 -*-
# 求1+2+3+...+n
# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字
# 及条件判断语句（A?B:C）。

# 利用构造函数:
# class Temp{
#     public:
#   	Temp(){
#         N++;
#         sum+=N;
#     }
#
#     static void Reset(){
#         N=0;
#         sum=0;
#     }
#
#     static unsigned int getSum(){
#         return sum;
#     }
#
# 	private:
#     static unsigned int N;
#     static unsigned int sum;
#
# };
#
# unsigned int Temp::N=0;
# unsigned int Temp::sum=0;
#
# class Solution {
#
# public:
#     static unsigned int Sum_Solution(int n) {
#         Temp::Reset();
# 		Temp* temps = new Temp[n];
#         delete[] temps;
#         temps=NULL;
#         return Temp::getSum();
#     }
# };
