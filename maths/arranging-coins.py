class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        while n>count:
            count+=1
            n-=count
        return count
        