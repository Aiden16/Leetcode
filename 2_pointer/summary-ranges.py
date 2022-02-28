class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        ans = []
        c,p1,p2 =0,0,1
        while p1<=p2 and p2<len(nums):
            if nums[p2]-nums[p1]==1:
                p2+=1
                p1+=1
            else:
                ans.append(str(nums[c])) if nums[c]==nums[p1] else ans.append(str(nums[c])+'->'+str(nums[p1]))
                p1=p2
                c=p1
                p2+=1
        
        ans.append(str(nums[c])) if nums[c]==nums[p1] else ans.append(str(nums[c])+'->'+str(nums[p1]))
        return ans