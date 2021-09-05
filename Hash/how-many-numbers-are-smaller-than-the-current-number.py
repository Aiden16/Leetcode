class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        newLis=sorted(nums)
        dic={}
        for index,val in enumerate(newLis):
            if val not in dic:
                dic[val]=index
        ans=[]
        for i in nums:
            ans.append(dic[i])
        return ans