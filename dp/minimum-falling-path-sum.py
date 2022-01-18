class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                if j==0:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1])
                elif j==len(matrix[0])-1:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j-1])
                else:
                    matrix[i][j]+=min(matrix[i-1][j],matrix[i-1][j+1],matrix[i-1][j-1])
        return min(matrix[len(matrix)-1])
    
    
        #extra space 
        dp=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        row,col=len(matrix),len(matrix[0])
        for i in range(col):
            dp[row-1][i]=matrix[row-1][i]
        for i in range(row-2,-1,-1):
            for j in range(col-1,-1,-1):
                m=float('Infinity')
                if (j+1<col):
                    m=min(m,dp[i+1][j+1])
                if(0<=j-1<col):
                    m=min(m,dp[i+1][j-1])
                m=min(m,dp[i+1][j])
                dp[i][j]=m+matrix[i][j]
        return min(dp[0])