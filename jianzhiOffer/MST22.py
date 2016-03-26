# -*- coding:utf-8 -*-
# 栈的压入、弹出序列
# 设置辅助栈buffer
# 遍历popV,如果待pop值不在buffer,则遍历pushV,将其之前的值都push进buffer
# 反正对于pushV内每次pop的值,要么从buffer顶部pop,要么从pushV pop(之前的值都push进buffer)
# 如果buffer[0]!=popV待pop值,并且pushV里也找不到,return False

class Solution:
    bufferList=list()
    def IsPopOrder(self, pushV, popV):
        if not (len(pushV) and len(popV) and len(pushV)==len(popV)):
            return False
        for i in xrange(len(popV)):
            if not len(self.bufferList) or (len(self.bufferList)>0 and self.bufferList[len(self.bufferList)-1]!=popV[i]):
                if not len(pushV):
                    return False
                else:
                    while len(pushV):
                        if pushV[0]!=popV[i]:
                            self.bufferList.append(pushV.pop(0))
                        else:
                            pushV.pop(0)
                            break
                    else:
                        return False
            else:
                self.bufferList.pop()
        return True

s=Solution()
print(s.IsPopOrder([1],[2]))