    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        
        dp=[]
        for i in range(n+1):
            tmp=[]
            for j in range(W+1):
                tmp.append(0)
            dp.append(tmp)
        # print(dp)
        for i in range(1,n+1):
            for j in range(1,W+1):
                if j>=wt[i-1]:
                    dp[i][j]=max(dp[i-1][j-wt[i-1]]+val[i-1],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]
        # print(dp)
        return dp[n][W]