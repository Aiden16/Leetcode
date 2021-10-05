    class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        #no extra array
        s=sum(nums)
        leftSum=0
        for ind,val in enumerate(nums):
            if leftSum==(s-leftSum-val):
                return ind
            leftSum+=val
        return -1
        # prefix=[]
        # s=0
        # if len(nums)==1:
        #     return 0
        # for i in range(len(nums)):
        #     s+=nums[i]
        #     prefix.append(s)
        # for i in range(len(nums)):
        #     print(i)
        #     if i==0:
        #         if s-prefix[i]==0:
        #             return i
        #     elif i==len(nums)-1:
        #         if prefix[i-1]==0:
        #             return i
        #     else:
        #         if prefix[i-1]==s-prefix[i]:
        #             return i
        # return -1
        