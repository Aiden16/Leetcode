class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic={}
        flag=0
        for ind,key in enumerate(nums):
            if key not in dic:
                dic[key]=ind
            else:
                ans=abs((dic[key]+1)-(ind+1))
                if ans<=k:
                    return True
                else:
                    dic[key]=ind
        return False
        