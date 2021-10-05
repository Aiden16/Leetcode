class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        k=1
        for i in range(len(nums)):
            if nums[i]==0:
                k-=1
            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1
        return i-left
        #sliding window
        ans=0
        k=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            if k==-2:
                while k==-2:
                    if nums[left]==0:
                        k+=1
                    left+=1
            ans=max(ans,right-left)
        return ans
        