class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        #Just simply check the frequency for nums[i]+k in the hashmap since ==>nums[i]+k-nums[i]=k
        dic=Counter(nums)
        ans=0
        for ind,val in enumerate(nums):
            if val+k in dic:
                ans+=dic[val+k]
        return ans
        