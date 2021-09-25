class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        uni=set()
        right=0
        left=0
        ans=0
        s=0
        for right in range(len(nums)):
            while nums[right] in uni:
                uni.remove(nums[left])
                s-=nums[left]
                left+=1
            uni.add(nums[right])
            s+=nums[right]
            ans=max(ans,s)
        return ans