class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        c1=0
        row=len(grid)
        col=len(grid[0])
        def check(r,c):
            u,d,l,ri=0,0,0,0
            #check for up
            if r!=0:
                u=1 if grid[r-1][c]==1 else 0
            #check for down:
            if r!=row-1:
                d=1 if grid[r+1][c]==1 else 0
            #check for right
            if c!=col-1:
                ri=1 if grid[r][c+1]==1 else 0
            #check for left
            if c!=0:
                l=1 if grid[r][c-1]==1 else 0
            return 4-(u+d+l+ri)
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    c1+=check(r,c)
        return c1