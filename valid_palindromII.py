class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strlis=[]
        strlis[:0]=s
        
        lis=[]
        p1=0
        p2=len(s)-1
        if s==s[::-1]:
            return True
        while p1<=p2:
            if s[p1]!=s[p2]:
                s1=s[p1]
                s2=s[p2]
                break
            p1+=1
            p2-=1
        strlis.pop(p1)
        if strlis==strlis[::-1]:
            return True
        strlis.insert(p1,s1)
        strlis.pop(p2)
        if strlis==strlis[::-1]:
            return True
        return False
        