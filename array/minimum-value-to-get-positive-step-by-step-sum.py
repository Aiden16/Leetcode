class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s=0
        m=float('Infinity')
        for i in nums:
            s+=i
            m=min(m,s)
        if m>0:
            return 1
        return (1-(m))
