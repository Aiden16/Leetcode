class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # pass
        
        lis = []
        for ind,val in enumerate(nums):
            lis.append([val,ind])
        count = [0]*len(nums)
        
        def merge(a,b):
            #merge
            ap,bp=0,0
            new = []
            x = 0
            while ap<len(a) and bp<len(b):
                if a[ap][0]>b[bp][0]:
                    new.append(b[bp])
                    x+=1
                    bp+=1
                else:
                    new.append(a[ap])
                    count[a[ap][1]]+=x
                    ap+=1
            if ap<len(a):
                for i in range(ap,len(a)):
                    new.append(a[i])
                    count[a[i][1]]+=x
            if bp<len(b):
                for i in range(bp,len(b)):
                    new.append(b[i])
            return new
        
        def merge_sort(arr,l,r):
            if l==r:
                return [arr[l]]
            mid = l+(r-l)//2
            left = merge_sort(arr,l,mid)
            right = merge_sort(arr,mid+1,r)
            ans = merge(left,right)
            return ans
        (merge_sort(lis,0,len(lis)-1))
        return count