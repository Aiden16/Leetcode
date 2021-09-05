class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        alexPoint = 0
        leePoint = 0
        piles.sort(reverse=True)
        for i in range(len(piles)):
            if i%2==0:
                alexPoint+=piles[i]
            else:
                leePoint+=piles[i]
        if alexPoint > leePoint:
            return True
        return False