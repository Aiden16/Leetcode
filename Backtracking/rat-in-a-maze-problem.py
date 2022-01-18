class Solution:
    def findPath(self, m, n):
        # code here
        row,col=len(m),len(m[0])
        ans=[]
        def dfs(r,c,p):
            # print(r,c,p,m[r][c])
            if r<0 or r>=row or c<0 or c>=col or m[r][c]==0:
                return
            # print(p)
            if (r,c)==(row-1,col-1):
                # print(p)
                ans.append(p)
            m[r][c]=0
            dfs(r-1,c,p+'U')
            dfs(r+1,c,p+'D')
            dfs(r,c+1,p+'R')
            dfs(r,c-1,p+'L')
            m[r][c]=1
            
        dfs(0,0,'')
        ans.sort()
        return ans