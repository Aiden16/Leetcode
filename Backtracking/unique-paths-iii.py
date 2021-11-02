class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx,sy=0,0
        emp=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    emp+=1
                elif grid[i][j]==1:
                    sx,sy=i,j
        def dfs(r,c,emp):
            # print(r,c,emp)
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==-1:
                return 0
            if grid[r][c]==2:
                # print('yes',emp)
                return 1 if emp==-1 else 0
            grid[r][c]=-1
            emp-=1
            total=dfs(r+1,c,emp)+dfs(r-1,c,emp)+dfs(r,c+1,emp)+dfs(r,c-1,emp)
            grid[r][c]=0 #this part here is backtracking
            emp+=1
            return total
        return (dfs(sx,sy,emp))
        