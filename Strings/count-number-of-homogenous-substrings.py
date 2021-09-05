class Solution:
    def countHomogenous(self, s: str) -> int:
        total=0
        pivot=s[0]
        count=1
        for i in range(1,len(s)):
            total+=count
            if s[i]==pivot:
                count+=1
            else:
                pivot=s[i]
                count=1
        total+=count
        return total % (10**9 + 7)