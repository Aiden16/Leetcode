class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        row,col=len(arr),len(arr[0])
        dp=[[0]*col for i in range(row)]
        # print(dp)
        for i in range(row):
            for j in range(col):
                if i==0:
                    dp[i][j]=arr[i][j]
                else:
                    m=float('Infinity')
                    for k in range(col):
                        if k!=j:
                            m=min(m,dp[i-1][k])
                    dp[i][j]=arr[i][j]+m
        # print(dp)
        return min(dp[row-1])