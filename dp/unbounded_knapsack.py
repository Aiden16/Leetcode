class Solution:
    def knapSack(self, N, W, val, wt):
        #twickin 
        #comination
        '''
        we checking each wt once for entire dp array
        
        '''
        dp=[0 for i in range(W+1)]
        dp[0]=0
        for w in range(len(wt)):
            for j in range(len(dp)):
                if wt[w]<=j:
                    dp[j]=max(dp[j-wt[w]]+val[w],dp[j])
        # print(dp)
        return dp[W]
        # code here
        #permutation
        '''
        we checking each wt for each entery of entire dp
        
        '''
        dp=[0 for i in range(W+1)]
        dp[0]=0
        for i in range(1,W+1):
            m=0
            for j in range(0,len(wt)):
                if wt[j]<=i:
                    m=max(m,dp[i-wt[j]]+val[j])
            dp[i]=m
        # print(dp)
        return dp[W]