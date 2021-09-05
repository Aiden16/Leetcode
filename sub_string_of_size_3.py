class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if len(s)<3:
            return 0
        count=0
        lis=s[:3]
        if len(set(lis))==len(lis):
            count+=1
        for i in range(len(s)-3):
            lis=lis[1:]+s[i+3]
            if len(set(lis))==len(lis):
                count+=1
        return count
            
        