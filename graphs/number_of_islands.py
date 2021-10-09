class Solution:
    '''
    bfs
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=set()
        def bfs(r,c):
            area=0
            qu=deque([[r,c]])
            visited.add((r,c))
            while qu:
                r,c=qu.popleft()
                #up
                if (r!=0) and ((r-1,c) not in visited) and (grid[r-1][c]=='1'):
                    qu.append([r-1,c])
                    visited.add((r-1,c))
                #down 
                if (r!=row-1) and ((r+1,c) not in visited) and (grid[r+1][c]=='1'):
                    qu.append([r+1,c])
                    visited.add((r+1,c))
                #left
                if (c!=0) and ((r,c-1) not in visited) and (grid[r][c-1]=='1'):
                    qu.append([r,c-1])
                    visited.add((r,c-1))
                #right
                if (c!=col-1) and ((r,c+1) not in visited) and (grid[r][c+1]=='1'):
                    qu.append([r,c+1])
                    visited.add((r,c+1))
                area+=1
            return area
        c=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]=='1' and ((i,j) not in visited):
                    print(bfs(i,j))
                    c+=1
        return c



'''
bfs
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols=len(grid),len(grid[0])
        visited=set()
        def bfs(r,c):
            qu=deque([[r,c]])
            visited.add((r,c))
            while qu:
                r,c=qu.popleft()
                dirn = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dirn:
                    row,col=r+dr,c+dc
                    if (row in range(rows) and 
                    col in range(cols) and 
                    (row,col) not in visited and 
                    grid[row][col]=='1'):
                        visited.add((row,col))
                        qu.append([row,col])
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visited:
                    bfs(r,c)
                    ans+=1
        return ans

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        row,col=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]=='0':
                return
            grid[r][c]='0'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        isLand=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=='1':
                    dfs(r,c)
                    isLand+=1
        return isLand