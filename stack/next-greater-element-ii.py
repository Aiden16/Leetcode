class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        max_so_far=nums[0]
        ind=0
        stack=[]
        nge=[-1 for i in range(len(nums))]
        for i in range(len(nums)):
            if max_so_far<nums[i]:
                max_so_far=nums[i]
                ind=i
            while stack and nums[stack[-1]]<nums[i]:
                nge[stack.pop()]=nums[i]
            stack.append(i)
        for i in stack:
            if nums[i]!=max_so_far:
                for j in range(0,ind+1):
                    if nums[j]>nums[i]:
                        nge[i]=nums[j]
                        break
        return nge
                
                