class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        for n in nums:
            if i<2 or nums[i-2]<n:
                nums[i] = n
                i+=1
        return i
    
        #bit big but honest work
        pivot = nums[0]
        j,flag=None,None
        c = 1
        for i in range(1,len(nums)):
            if nums[i] == pivot and flag and c>=2:
                continue
            if nums[i] == pivot:
                c+=1
            elif nums[i]!=pivot:
                pivot = nums[i]
                c = 1
            if not flag and c == 3:
                flag = True
                j = i
            elif flag:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        return j if j else None