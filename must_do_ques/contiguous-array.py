class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={0:-1} #count:index
        #1---->+1
        #0----->-1
        count=0
        ans=0
        for ind,num in enumerate(nums):
            if num==1:
                count+=1   
            else:
                count-=1
            if count in hash:
                ans=max(ans,ind-hash[count])
            else:
                hash[count]=ind
        return ans
