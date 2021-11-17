class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        
        row,col=len(grid),len(grid[0])
        dp=[]
        for i in range(len(grid)):
            tmp=[]
            for j in range(len(grid[0])):
                tmp.append(0)
            dp.append(tmp)
        s=0
        for j in range(len(grid[0])-1,-1,-1):
            s+=grid[row-1][j]
            dp[row-1][j]=s
        for i in range(row-2,-1,-1):
            for j in range(col-1,-1,-1):
                m=float('Infinity')
                if (i+1)<row:
                    m=min(m,dp[i+1][j])
                if(j+1)<col:
                    m=min(m,dp[i][j+1])
                dp[i][j]=m+grid[i][j]
        return dp[0][0]
#         '''
#         brute force
        
#         let us see all the possile paths
        
#         '''
        
#         rows,cols=len(grid),len(grid[0])
        
#         #bfs
#         seen=set()
#         def bfs(r,c):
#             qu=deque([(r,c,0)])
#             while qu:
#                 r,c,s=qu.popleft()
#                 print(r,c)
#                 # if (r,c)==(rows-1,cols-1):
#                     # print(r,c,s)
#                 dirn=[[1,0],[0,1]]
#                 for dr,dc in dirn:
#                     row,col=r+dr,c+dc
#                     if(0<=row<rows and 0<=col<cols and (row,col) not in seen):
#                         seen.add((row,col))
#                         qu.append((row,col,s+grid[row][col]))
#         bfs(0,0)