class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        
        rows,cols=len(isWater),len(isWater[0])
        seen=set()
        qu=deque([])
        
        def bfs(qu):
            while qu:
                r,c=qu.popleft()
                seen.add((r,c))
                dirn=[[-1,0],[1,0],[0,-1],[0,1]]
                for dr,dc in dirn:
                    row,col=r+dr,c+dc
                    if(0<=row<rows and
                      0<=col<cols and (row,col) not in seen):
                        isWater[row][col]=isWater[r][c]+1
                        seen.add((row,col))
                        qu.append((row,col))
                        
            
        for i in  range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    seen.add((i,j))
                    isWater[i][j]=0
                    qu.append((i,j))
        bfs(qu)
        print(isWater)
        return isWater
        