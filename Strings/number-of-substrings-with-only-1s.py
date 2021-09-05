class Solution:
    def numSub(self, s: str) -> int:
        pivot='1'
        count=0
        total=0
        for i in range(len(s)):
            if s[i]==pivot:
                count+=1
            else:
                count=0
            total+=count
        return total % (10**9+7)
        