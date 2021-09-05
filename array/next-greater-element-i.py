class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash={}
        for i,val in enumerate(nums2):
            hash[val]=i
        ans=[]
        c=0
        for i in nums1:
            for j in range(hash[i],len(nums2)):
                if nums2[j]>i:
                    c=nums2[j]
                    break
            if c!=0:
                ans.append(c)
            else:
                ans.append(-1)
            c=0
        return ans