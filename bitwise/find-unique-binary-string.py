class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:      
        setLis = set(int(i,2) for i in nums)
        print(setLis)
        for i in range(pow(2,len(nums))):
            if i not in setLis:
                ans=bin(i)[2:]
                return '0'*(len(nums)-len(ans))+ans