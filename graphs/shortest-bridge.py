class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        #island expansion, faster
        to_visit=deque([])
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1:
                return
            grid[r][c]=-1
            to_visit.append((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        flag=0
        step=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    # print(i,j)
                    dfs(i,j)
                    flag=1
                    break
            if flag:
                break
        seen=set()
        while to_visit:
            # print('------------------------------')
            for i in range(len(to_visit)):
                r,c=to_visit.popleft()
                # print(r,c)
                seen.add((r,c))
                dirn=[[-1,0],[1,0],[0,1],[0,-1]]
                for dr,dc in dirn:
                    row,col=r+dr,c+dc
                    # print(row,col)
                    if 0<= row <rows and 0<=col<cols:
                        if grid[row][col]==1:
                            return step
                        elif grid[row][col]==0:
                            to_visit.append((row,col))
                            grid[row][col]=-1
                            # seen.add((row,col))
            step+=1
        
        
        #works but is slow
        
        rows,cols=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!=1:
                return
            grid[r][c]=-1
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        flag=None
        for i in range(rows):
            if flag:
                break
            for j in range(cols):
                if grid[i][j]==1:
                    dfs(i,j)
                    flag=1
                    break
        def bfs(r,c,path):
            seen = set()
            seen.add((r,c))
            qu=deque([[r,c,path]])
            while qu:
                r,c,path=qu.popleft()
                if grid[r][c]==-1:
                    return path
                dirn=[[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in dirn:
                    row,col=r+dr,c+dc
                    if (row in range(rows) and
                        col in range(cols) and (row,col) not in seen and
                        grid[row][col]!=1):
                        if grid[row][col]==-1:
                            return path
                        seen.add((row,col))
                        qu.append((row,col,path+1))
        ans=float('Infinity')
        for i in range(rows):
            for j in range(cols):
                if (i*j==0 or i==rows-1 or j==cols-1) and grid[i][j]==1:
                    c=bfs(i,j,0)
                    if c:
                        ans=min(ans,c)
                    
                elif grid[i][j]==1 and (grid[i-1][j]==0 or grid[i+1][j]==0 or grid[i][j-1]==0 or  grid[i][j+1]==0):
                    c=bfs(i,j,0)
                    if c:
                        ans=min(ans,c)
        return ans
        