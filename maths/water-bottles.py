class Solution:
    def numWaterBottles(self, nb: int, ne: int) -> int:
        total=0
        while nb>=ne:
            nb-=ne
            nb+=1
            total+=ne
        total+=nb
        return total