class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(arr,start,end):
            while start<=end:
                tmp=arr[start]
                arr[start]=arr[end]
                arr[end]=tmp
                start+=1
                end-=1
            return arr
        k=k%len(nums)
        nums.reverse()
        reverse(nums,0,k-1)
        reverse(nums,k,len(nums)-1)

                
