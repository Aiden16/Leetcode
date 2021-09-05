class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lis=[]
        for i in s:
            if i.isalnum():
                lis.append(i.lower())
        p1=0
        p2=len(lis)-1
        print(lis)
        while p1<=p2:
            if lis[p1]!=lis[p2]:
                return False
            p1+=1
            p2-=1
        return True
        
            