class Solution(object):
    fixed=[]
    # fixed=nums

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # fixed=[]
        self.array=nums
        self.original = list(nums)
        # self.fixed=nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums=[]
        random.shuffle(self.array)
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()