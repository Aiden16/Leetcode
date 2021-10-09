class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        #dfs soln
        row,col=len(board),len(board[0])
        def dfs(r,c):
            if r<0 or r>=row or c<0 or c>=col or board[r][c]=='.':
                return
            board[r][c]= '.'
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        count=0
        for i in range(row):
            for j in range(col):
                if board[i][j]=='X':
                    count+=1
                    dfs(i,j)
        return count
        
        #constant space
        count=0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=='X':
                    #check above
                    if r>0 and board[r-1][c]=='X':
                        pass
                    #check left
                    elif c>0 and board[r][c-1]=='X':
                        pass
                    else:
                        count+=1
        return count