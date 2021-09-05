class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([i*i for i in nums])
        ans=[0]*len(nums)
        left=0
        right=(len(nums)-1)
        index=0
        while left<=right:
            if abs(nums[left])<=abs(nums[right]):
                ans[index]=nums[right]**2
                right-=1
            else:
                ans[index]=nums[left]**2
                left+=1
            index+=1
        ans.reverse()
        return ans