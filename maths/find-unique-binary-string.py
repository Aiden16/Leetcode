class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:      
        setLis = set(int(i,2) for i in nums)
        for i in range((pow(2,len(nums)-1))-1 if len(nums)>1 else 0,pow(2,len(nums))):
            if i not in setLis:
                print(i)
                ans=bin(i)[2:]
                return '0'*(len(nums)-len(ans))+ans