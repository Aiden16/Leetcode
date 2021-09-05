class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 pass solution
        prefix=[0]
        s=0
        for i in nums:
            s+=i
            prefix.append(s)
        for i in range(1,len(prefix)):
            if prefix[i-1] == prefix[-1]-prefix[i]:
                return i-1
        return -1
        #not so optimal
        # for i in range(len(nums)):
        #     arr1=nums[:i]
        #     arr2=nums[i+1:]
        #     if sum(arr1)==sum(arr2):
        #         return i
        # return -1
        