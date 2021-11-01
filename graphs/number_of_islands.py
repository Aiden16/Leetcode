class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row,col=len(board),len(board[0])
        #let use bfs
        seen=set()
        def bfs(r,c):
            seen.add((r,c))
            qu=deque([[r,c]])
            board[r][c]='1'
            while qu:
                i,j=qu.popleft()
                dirn=[[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in dirn:
                    rows,cols=i+dr,j+dc
                    if(rows in range(row) and
                      cols in range(col) and
                      board[rows][cols]=='O'):
                        seen.add((rows,cols))
                        board[rows][cols]='1'
                        qu.append([rows,cols])
        #let us use dfs

        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or board[r][c]!='O':
                return
            board[r][c]='1'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        for i in range(row):
            for j in range(col):
                if (i*j==0 or i==row-1 or j==col-1) and board[i][j]=='O' and (i,j) not in seen:
                    # dfs(i,j)
                    bfs(i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='1':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
