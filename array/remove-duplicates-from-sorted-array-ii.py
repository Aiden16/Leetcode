class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return
        p1=0
        p2=1
        count=1
        counter=len(nums)
        while p2!=counter:
            if nums[p1]==nums[p2]:
                count+=1
                if count>2:
                    del nums[p2]
                    if p2==len(nums):
                        break
                else:
                    p2+=1
                    if p2==len(nums):
                        break

            elif nums[p1]!=nums[p2]:
                p1=p2
                p2+=1
                count=1
                if p2==len(nums):
                    break
                