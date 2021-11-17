class Solution:
    def numTrees(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            left=0
            right=i-1
            while left<=i-1:
                # print(left,right,i)
                dp[i]+=dp[left]*dp[right]
                left+=1
                right-=1
        return dp[n]
        