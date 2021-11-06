class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        #we could use land expansion 
        rows,cols=len(grid),len(grid[0])
        qu=deque([])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    qu.append((i,j))
        if len(qu)==rows*cols:
            return -1
        step=0
        while qu:
            for i in range(len(qu)):
                r,c=qu.popleft()
                dirn=[[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in dirn:
                    row,col=r+dr,c+dc
                    if 0<=row<rows and 0<=col<cols:
                        if not grid[row][col]:
                            qu.append((row,col))
                            grid[row][col]=1
            step+=1

            return step-1