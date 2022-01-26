class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        
        if len(a)>len(b):
            a,b=b,a
        left,right = 0,len(a)
        total = len(a)+len(b)
        
        while left<=right:
            aleft = left+(right-left)//2
            bleft = (total+1)//2-aleft
            am1 = a[aleft-1] if aleft>0 else float('-inf')
            bm1 = b[bleft-1] if bleft>0 else float('-inf')
            a1 = a[aleft] if aleft<len(a) else float('inf')
            b1 = b[bleft] if bleft<len(b) else float('inf')
            
           
            #proper segregation
            if(am1<=b1 and bm1<=a1):
                if total%2:
                    median = max(am1,bm1)
                else:
                    lmax,rmin = max(am1,bm1),min(a1,b1)
                    median = (lmax+rmin)/2
                return median
            elif bm1>a1:
                left = aleft+1
            elif am1>b1:
                right = aleft-1
        
        #O(m+n)
        # new = []
        # p1,p2=0,0
        # while p1<len(nums1) and p2<len(nums2):
        #     if nums1[p1]>=nums2[p2]:
        #         new.append(nums2[p2])
        #         p2+=1
        #     else:
        #         new.append(nums1[p1])
        #         p1+=1
        # if p1<len(nums1):
        #     for i in range(p1,len(nums1)):
        #         new.append(nums1[i])
        # if p2<len(nums2):
        #     for i in range(p2,len(nums2)):
        #         new.append(nums2[i])
        # if len(new)%2 == 1:
        #     return new[len(new)//2]
        # else:
        #     x,y = new[len(new)//2],new[len(new)//2-1]
        #     return (x+y)/2
