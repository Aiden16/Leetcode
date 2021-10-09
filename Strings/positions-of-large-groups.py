class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        ans=[]
        pivot,ind=s[0],0
        c=1
        for i in range(1,len(s)):
            if s[i]==pivot:
                c+=1
            else:
                if c>=3:
                    ans.append([ind,i-1])
                pivot,ind=s[i],i
                c=1
        if c>=3:
            ans.append([ind,i])
        return ans
                