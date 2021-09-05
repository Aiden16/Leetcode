class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #optimal soln
        dic={0:1}
        s=0
        c=0
        for i in range(len(nums)):
            s+=nums[i]
            if s-k in dic:
                c+=dic[s-k]
            if s in dic:
                dic[s]+=1
            else:
                dic[s]=1
        return c
       