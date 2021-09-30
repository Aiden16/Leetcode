class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs=set()
        dic=Counter(nums)
        for ind,val in enumerate(nums):
            if k==0:
                if dic[val]>1:
                    pairs.add((val,val))
            else:
                if val+k in dic:
                    pairs.add((val,val+k))
        return len(pairs)
        