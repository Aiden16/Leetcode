#----------------using loop-------------#
class Solution:
    def addDigits(self, num: int) -> int:
        s=str(num)
        x=0
        while True:
            for i in s:
                x+=int(i)
            s=str(x)
            x=0
            if len(s)==1:
                break
        return s

#-------------using formula---------#
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        return 1+(num-1)%9
        