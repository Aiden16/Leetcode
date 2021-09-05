class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dic={}
        for i in range(1,27):
            dic[chr(i+96)]=i
        nums=''
        for i in s:
            nums+=str(dic[i])
        x=0
        while k:
            for i in nums:
                x+=int(i)
            nums=str(x)
            x=0
            k-=1
        return nums
                