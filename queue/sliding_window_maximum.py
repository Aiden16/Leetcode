class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #deque , maintain monotonic decreasing stack
        deq=deque()
        res=[]
        for ind,val in enumerate(nums):
            while deq and nums[deq[-1]]<=val:
                deq.pop()
            deq.append(ind)
            
            #remove ele outside the window
            if deq[0]==ind-k:
                deq.popleft()
            #incase if we cover our window
            if ind>=k-1:
                res.append(nums[deq[0]])
        return res
        #sliding window, gave tle
        # right=k
        # ans=[]
        # for left in range(len(nums)-k+1):
        #     win=nums[left:right]
        #     ans.append(max(win))
        #     right+=1
        # return ans
        