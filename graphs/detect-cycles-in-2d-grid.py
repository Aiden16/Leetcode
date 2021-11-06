class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        rows,cols=len(grid),len(grid[0])
        seen=set()
        def bfs(r,c,l):
            seen.add((r,c))
            visited=set()
            qu=deque([(r,c)])
            while qu:
                for i in range(len(qu)):
                    x,y=qu.popleft()
                    seen.add((x,y))
                    dirn=[[-1,0],[1,0],[0,-1],[0,1]]
                    for dr,dc in dirn:
                        row,col=x+dr,y+dc
                        if(0<=row<rows 
                           and 0<=col<cols 
                          and grid[row][col]==l and (row,col) not in seen ):
                            if (row,col) in visited:
                                return True
                            visited.add((row,col))
                            qu.append((row,col))
                for s in visited:
                    seen.add(s)
                visited=set()
            return False
        for i in range(rows):
            for j in range(cols):
                if (i,j) not in seen:
                    if bfs(i,j,grid[i][j]):
                        return True
