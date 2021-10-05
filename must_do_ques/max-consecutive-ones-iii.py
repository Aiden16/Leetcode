class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #optimized soln
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                k-=1
            if k<0:
                if nums[left]==0:
                    k+=1
                left+=1
        return right-left+1
        
        #tle
#         ans=0
#         left=0
#         for right in range(len(nums)):
#             if nums[right]==0:
#                 k-=1
#             if k<0:
#                 while k<0:
#                     if nums[left]==0:
#                         k+=1
#                         left+=1
#                     else:
#                         left+=1
#             ans=max(ans,len(nums[left:right+1]))

#         return ans
                
        