class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #adjacency list, still slow asf
        adj = {i:[] for i in range(len(points))}
        for i in range(len(points)):
            xi,yi=points[i]
            for j in range(i+1,len(points)):
                xj,yj = points[j]
                dist = abs(xi-xj)+abs(yi-yj)
                adj[i].append([dist,j])
                adj[j].append([dist,i])
        pq = []
        'wt,ver'
        visited = set()
        cost = 0
        heapq.heappush(pq,(0,0))
        while pq:
            wt,vert = heapq.heappop(pq)
            if vert in visited:
                continue
            cost+=wt
            visited.add(vert)
            for w,nei in adj[vert]:
                if nei not in visited:
                    heapq.heappush(pq,(w,nei))
        return cost
    
    
        #my own implementation but bit slow
        cost = 0
        pq = []
        'wt,index'
        heapq.heappush(pq,(0,0))
        visited = set()
        while pq:
            wt,ind = heapq.heappop(pq)
            if ind in visited:
                continue
            visited.add(ind)
            cost+=wt
            xi,yi=points[ind]
            for nei in range(len(points)):
                if nei not in visited:
                    xj,yj = points[nei]
                    wt = abs(xi-xj)+abs(yi-yj)
                    heapq.heappush(pq,(wt,nei))
                    
        return cost
            