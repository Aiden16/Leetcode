class Solution:
    def minReorder(self, n: int, c: List[List[int]]) -> int:
        visit=set()
        edges={(a,b) for a,b in c}
        neighbours=defaultdict(list)
        for u,v in c:
            neighbours[u].append(v)
            neighbours[v].append(u)
        count=0
        def dfs(city):
            nonlocal visit,edges,neighbours,count
            for nei in neighbours[city]:
                if nei in visit:
                    continue
                if (nei,city) not in edges:
                    count+=1
                visit.add(nei)
                dfs(nei)
        visit.add(0)
        dfs(0)
        return count