class Solution:
    def maxScoreSightseeingPair(self, g: List[int]) -> int:
        maxi=g[0]+0
        ans=0
        for i in range(1,len(g)):
            ans=max(ans,maxi+g[i]-i)
            maxi=max(maxi,g[i]+i)
        return ans