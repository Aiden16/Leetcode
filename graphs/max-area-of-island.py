class Solution:
    '''
    bfs
    '''
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        def bfs(r,c):
            area=0
            qu=deque([[r,c]])
            visited.add((r,c))
            while qu:
                r,c=qu.popleft()
                dirn=[[-1,0],[1,0],[0,-1],[0,1]]
                for i,j in dirn:
                    row,col=r+i,c+j
                    if (row in range(rows) and 
                    col in range(cols) and 
                    (row,col) not in visited and 
                    grid[row][col])==1:
                        qu.append([row,col])
                        visited.add((row,col))
                area+=1
            return area
        max_area=float('-inf')
        ans=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    area=bfs(r,c)
                    max_area=max(max_area,area)
                    ans+=1
        return max_area if max_area!=float('-inf') else 0



'''
dfs
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row,col=len(grid),len(grid[0])
        visited=set()
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or grid[r][c]==0:
                return 0
            grid[r][c]=0
            return (1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1))
        ans=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1 and (r,c) not in visited:
                    ans=max(ans,(dfs(r,c)))
        return ans                     
                            
        