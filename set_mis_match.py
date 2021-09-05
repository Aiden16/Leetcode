class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        ans=[]
        dic={}
        setLis = list(set(nums))
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                ans.append(i)
                break
        missing = sum(i for i in range(1,len(nums)+1)) - sum(setLis)
        ans.append(missing)
        # print(sum(nums) - sum(set(nums))) to find the duplicate
        return ans

        