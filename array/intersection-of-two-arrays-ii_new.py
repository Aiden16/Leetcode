class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #using hashmap
        hash={}
        for i in nums1:
            hash[i]=hash.get(i,0)+1
        check=[]
        for i in nums2:
            if i in nums1 and hash[i]>0:
                check.append(i)
                hash[i]-=1
        return check
        #2 pointer approach
        # p1=0
        # p2=0
        # nums1.sort()
        # nums2.sort()
        # check=[]
        # while p1!=len(nums1) and p2!=len(nums2):
        #     if nums1[p1]<nums2[p2]:
        #         p1+=1
        #     elif nums2[p2]<nums1[p1]:
        #         p2+=1
        #     else:
        #         check.append(nums1[p1])
        #         p2+=1
        #         p1+=1
        # return check

        