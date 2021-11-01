class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #let us use bfs
        row,col=len(board),len(board[0])
        
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
                if (i*j==0 or i==row-1 or j==col-1) and board[i][j]=='O':
                    dfs(i,j)
        for i in range(row):
            for j in range(col):
                if board[i][j]=='1':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'
