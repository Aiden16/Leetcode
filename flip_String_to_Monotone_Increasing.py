class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cost=s.count('0')
        best=cost
        for i in s:
            if i=='0':
                cost-=1
            else:
                cost+=1
            best=min(best,cost)
        return best