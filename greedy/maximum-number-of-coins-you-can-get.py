class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        ans = 0
        turns = len(piles)//3
        while len(piles)>turns:
            a = piles.pop()
            n = piles.pop()
            ans+=n
        return ans
            
            
        
        