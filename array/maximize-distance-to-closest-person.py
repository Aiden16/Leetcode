class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev = None
        count = 0
        ans = float('-inf')
        mid = float('-inf')
        start = float('-inf')
        for ind,val in enumerate(seats):
            if val == 0:
                count+=1
                if prev!=None:
                    ans = max(ans,ind-prev)
            elif val == 1 and prev==None:
                start = count
                count = 0
                prev = ind
            else:
                mid = max(mid,(ind-prev)//2)
                ans = mid
                prev = ind
        return max(start,ans)
                
        