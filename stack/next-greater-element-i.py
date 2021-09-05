class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        stack=[]
        nge=[0]*len(nums2)
        for i in range(len(nums2)):
            #maintain monotonic decreasing stack
            while stack and nums2[stack[-1]]<nums2[i]:
                dic[nums2[stack.pop()]]=nums2[i]
            stack.append(i)
        ans=[]
        for i in nums1:
            if i in dic:
                ans.append(dic[i])
            else:
                ans.append(-1)
        return ans