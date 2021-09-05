class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        #not a binary search approach but an optimum one
        '''
            handles edge case,
            incase if the nums has only one element
        '''
        if len(nums)==1: 
            return nums[0]
        p1=0
        p2=p1+1
        while True:
            if p2>=len(nums): #handles if unique element is at end
                return nums[p2-1]
            if nums[p1]!=nums[p2]:
                return nums[p1]
            p1+=2
            p2=p1+1