class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #binary search
        f=0
        l=len(nums)-1
        while f<=l:
            mid=(f+l)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                f=mid+1
            else:
                l=mid-1
        return f

        