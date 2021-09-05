class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMax=1
        curMin=1
        for n in nums:
            if n==0:
                curMax=1
                curMin=1
                continue
            tmp=curMax
            curMax=max(curMax*n,n,curMin*n)
            curMin=min(curMin*n,n,tmp*n)
            res=max(res,curMax)
        return res


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 pass soln
        prod=1
        res=max(nums)
        for num in nums:
            prod=prod*num
            res=max(prod,res)
            if prod==0:
                prod=1
        prod=1
        for i in range(len(nums)-1,-1,-1):
            prod=prod*nums[i]
            res=max(prod,res)
            if prod==0:
                prod=1
        return res