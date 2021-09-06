class Solution:
    def slowestKey(self, t: List[int], k: str) -> str:
        dur=t[0]
        ans=k[0]
        for i in range(1,len(t)):
            comp=t[i]-t[i-1]
            if comp>dur:
                dur=comp
                ans=k[i]
            elif comp==dur:
                ans=max(ans,k[i])
        return ans
                
        