#------------sort approach-------#
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if not nums:
            return 0
        nums.sort()
        best=0
        count=0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                count+=1
            else:
                best=max(best,count+1)
                count=0
        best=max(best,count+1)
        return best


#---------------set approach--------------------#
class Solution(object):
    def longestConsecutive(self, nums):
        nums = set(nums)
        best = 0
        for x in nums:
            if x - 1 not in nums:
                y = x + 1
                while y in nums:
                    y += 1
                best = max(best, y - x)
        return best
