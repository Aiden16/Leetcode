class Solution:
    def distanceBetweenBusStops(self, distance: List[int], s: int, d: int) -> int:
        a,b=min(s,d),max(s,d)
        return min(sum(distance[a:b]),sum(distance)-sum(distance[a:b]))
#         ans=float('inf')
#         for i in range(len(distance)):
#             if i==s and (i+1)%len(distance)==d:
#                 ans=min(ans,distance[i])
                