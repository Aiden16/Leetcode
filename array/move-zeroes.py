class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #snowball approach
        snow=0
        for i in range(len(nums)):
            if nums[i]==0:
                snow+=1
            else:
                temp=nums[i]
                nums[i]=0
                nums[i-snow]=temp