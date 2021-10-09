class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        sink non common islands
        count subisland
        '''
        row,col=len(grid1),len(grid1[0])
        def dfs(r,c):
            if r<0 or r>=row or c>=col or c<0 or grid2[r][c]==0:
                return
            grid2[r][c]=0
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(row):
            for c in range(col):
                if grid1[r][c]==0 and grid2[r][c]==1:
                    dfs(r,c)
        sub=0
        for r in range(row):
            for c in range(col):
                if grid2[r][c]==1:
                    dfs(r,c)
                    sub+=1
        return sub