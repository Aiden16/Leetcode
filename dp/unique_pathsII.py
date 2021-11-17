class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m,n=len(g),len(g[0])
        if g[m-1][n-1]==1:return 0
        dp=[]
        for i in range(m):
            tmp=[]
            for j in range(n):
                tmp.append(0)
            dp.append(tmp)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j)==(m-1,n-1):
                    if g[i][j]==1:
                        return 0
                    else:
                        dp[i][j]=1
                elif i==m-1:
                    if g[i][j]!=1 and g[i][j+1]!=1 and dp[i][j+1]!=0:
                        dp[i][j]=1
                elif j==n-1:
                    if g[i][j]!=1 and g[i+1][j]!=1 and dp[i+1][j]!=0:
                        dp[i][j]=1
                else:
                    if g[i][j]!=1:
                        dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        # def dfs(r,c):
        #     if r<0 or r>=m or c<0 or c>=n or g[r][c]==1:
        #         return 0
        #     if (r,c)==(m-1,n-1):
        #         return 1
        #     total=dfs(r+1,c) + dfs(r,c+1)
        #     g[r][c]=0
        #     return total
        # return (dfs(0,0))