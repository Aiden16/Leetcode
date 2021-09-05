class Solution(object):
     def maximumProduct(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            nums.sort()
            a = nums[-1] * nums[-2] * nums[-3]
            b = nums[0] * nums[1] * nums[-1]
            return max(a,b)