class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        while k:
            nums[0]=-nums[0]
            nums.sort()
            k-=1
        return sum(nums)
            
        