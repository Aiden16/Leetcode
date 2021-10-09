class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        res=0
        if x<0:
            sym=-1
        elif x>0:
            sym=1
        x=abs(x)
        while x:
            res=(res*10)+(x%10)
            x//=10
        return 0 if (sym*res>=(2**31-1) or sym*res<=(-2**31) ) else sym*res
        