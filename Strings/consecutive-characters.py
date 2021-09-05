class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        pivot=s[0]
        ans=1
        for i in range(1,len(s)):
            if pivot == s[i]:
                count+=1
            else:
                ans=max(ans,count)
                pivot=s[i]
                count=1
        ans=max(ans,count)
        return ans
        