class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        nums1=list(set(nums1))
        nums2=list(set(nums2))
        for i in nums1:
            if i not in dic:
                dic[i]=1
        ans=[]
        for i in nums2:
            if i in dic:
                ans.append(i)
            else:
                dic[i]=1
        print(ans)
        return ans
        