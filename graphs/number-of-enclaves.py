class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        #check for adjacent 1 and flip connected 1
        row,col=len(grid),len(grid[0])
        # if col==1:
            # return 0
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
                return
            grid[r][c]=0
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range(row):
            for j in range(col):
                if(i*j==0 or i==row-1 or j==col-1) and grid[i][j]==1:
                    dfs(i,j)
        return sum(map(sum,grid))
        # #first row
        # for i in range(1):
        #     for j in range(col):
        #         if grid[i][j]==1:
        #             dfs(i,j)
        # # #last row
        # for i in range(1):
        #     for j in range(col):
        #         if grid[row-1][j]==1:
        #             dfs(row-1,j)
        # #left col
        # for i in range(1):
        #     for j in range(row):
        #         if grid[j][i]==1:
        #             dfs(j,i)
        # #right col
        # for i in range(1):
        #     for j in range(row):
        #         if grid[j][col-1]==1:
        #             dfs(j,col-1)
        count=0
        for i in range(1,row-1):
            for j in range(1,col-1):
                if grid[i][j]==1:
                    count+=1
        return count
