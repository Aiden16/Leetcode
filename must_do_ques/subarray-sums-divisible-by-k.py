class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        hash={0:1} #remainder:freq
        prefix=0
        count=0
        for num in nums:
            prefix+=num
            if prefix%k in hash:
                count+=hash[prefix%k]
                hash[prefix%k]+=1
            else:
                hash[prefix%k]=1
        return count
            
        