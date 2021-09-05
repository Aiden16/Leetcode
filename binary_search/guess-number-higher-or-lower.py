# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(n)==0:return n
        l=1
        r=n
        while l<=r:
            mid=l+(r-l)//2
            if guess(mid)==0:
                return mid
            elif guess(mid)==1:
                l=mid+1
            else:
                r=mid-1
        