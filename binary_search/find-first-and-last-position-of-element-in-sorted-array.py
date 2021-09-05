class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
       # o(n)
        f=0
        l=len(nums)-1
        while f<=l:
            if nums[f]==target and nums[l]==target:
                return [f,l]
            elif nums[f]==target:
                l-=1
            elif nums[l]==target:
                f+=1
            else:
                f+=1
                l-=1
        return [-1,-1]
        
#o(logn)
        #o(logn)
        def left(arr,t):
            l=0
            r=len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<t:
                    l=mid+1
                else:
                    r=mid-1
            return l
        def right(arr,t):
            l=0
            r=len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=t:
                    l=mid+1
                else:
                    r=mid-1
            return r
        left,right=left(nums,target),right(nums,target)
        return [left,right] if left<=right else [-1,-1]
                