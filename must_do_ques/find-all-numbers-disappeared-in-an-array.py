class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for num in nums:
            if nums[abs(num)-1]>0:
                nums[abs(num)-1]*=-1
        print(nums)
        for ind,num in enumerate(nums):
            if num>0:
                res.append(ind+1)
        return res