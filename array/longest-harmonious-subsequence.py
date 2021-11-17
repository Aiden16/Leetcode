class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #rute force
#         ans=0
#         for i in range(len(nums)):
#             c=1
#             # print('i=====>',nums[i])
#             for j in range(i+1,len(nums)):
#                 if abs(nums[j]-nums[i])<=1:
#                     # print('j---',nums[j])
#                     c+=1
#             ans=max(ans,c)
#         return ans

#counter solutipn
        
        dic=Counter(nums)
        ans=0
        for i in dic.keys():
            if i+1 in dic:
                ans=max(dic[i]+dic[i+1],ans)
        return ans
        nums.sort()
        h1={}
        for ind,val in enumerate(nums):
            h1[val]=ind
        ans=0
        # print(nums)
        for ind,val in enumerate(nums):
            if val+1 in h1:
                ans=max(ans,h1[val+1]-ind+1)
        return ans
        # for i in n