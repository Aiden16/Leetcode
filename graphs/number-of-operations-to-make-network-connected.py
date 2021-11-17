class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:
        
        '''
        union find
        
        '''
        if n-1>len(c):
            return -1
        parent={i:i for i in range(n)}
        
        def find(s):
            # print(s)
            if parent[s]==s:
                return s
            return find(parent[s])
        def union(x,y):
            parent[find(x)]=find(y)
        for x,y in c:
            union(x,y)
        return len({find(i) for i in range(n)})-1
    
    '''
    dfs
    
    '''
class Solution:
    def makeConnected(self, n: int, c: List[List[int]]) -> int:
        #if connections are less, not possible to connect
        #all computers
        if n-1>len(c):
            return -1
        seen=set()
        connection=defaultdict(list)
        for u,v in c:
            connection[u].append(v)
            connection[v].append(u)
        def dfs(root):
            seen.add(root)
            for node in connection[root]:
                if node not in seen:
                    dfs(node)
        count=0
        for i in range(n):
            if i not in seen:
                count+=1
                dfs(i)
        return count-1
        # return arr.count(-1)