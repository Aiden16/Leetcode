class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #dp
        # if m==1 and n==1:
        #     return 1
        dp=[]
        for i in range(m):
            tmp=[]
            for j in range(n):
                tmp.append(1)
            dp.append(tmp)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i,j)==(m-1,n-1):
                    dp[i][j]=1
                elif i==m-1:
                    dp[i][j]=1
                elif j==n-1:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        
        # print(m-1,n-1)
#         def bfs(r,c):
#             qu=deque([(r,c)])
#             count=0
#             while qu:
#                 # print(qu)
#                 row,col=qu.popleft()
#                 # print(row,col)
#                 if (row,col)==(m-1,n-1):
#                     count+=1
#                 dirn=[[1,0],[0,1]]
#                 for dr,dc in dirn:
#                     r,c=row+dr,col+dc
#                     if (0<=r<m and 0<=c<n):
#                         qu.append((r,c))
#             return count
#         return bfs(0,0)
        
        # def dfs(r,c):
        #     if r<0 or r>=m or c<0 or c>=n and (r,c) in seen:
        #         return 0
        #     # print(total)
        #     if (r,c)==(m-1,n-1):
        #         return 1
        #     seen.add((r,c))
        #     # dfs(r+1,c)
        #     # dfs(r,c+1)
        #     ans=dfs(r+1,c)+dfs(r,c+1)
        #     print(ans)
        #     seen.remove((r,c))
        #     return ans
        # total=0
        # seen=set()
        # dfs(0,0)
        # print(total) 