class Solution:
    def findCircleNum(self, a: List[List[int]]) -> int:
        row,col=len(a),len(a[0])
        
        visited=set()
        def dfs(i):
            visited.add(i)
            for ind,con in enumerate(a[i]):
                if ind not in visited and con:
                    dfs(ind)
                    
                    
#================ iterative====================================#
        def bfs(ind):
            qu=deque([ind])
            while qu:
                n=qu.popleft()
                visited.add(n)
                for ind,con in enumerate(a[n]):
                    if con and ind not in visited:
                        qu.append(ind)
        bfs(0)
        ans=0
        for i in range(row):
            if i not in visited:
                ans+=1
                dfs(i)
        return ans
                    
                
        