class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c1=edges[0][0]
        c2=edges[0][1]
        e1=0
        e2=0
        for i in range(1,len(edges)):
            if c1==edges[i][0] or c1==edges[i][1]:
                e1+=1
            if c2==edges[i][0] or c2==edges[i][1]:
                e2+=1
        return c1 if e1==len(edges)-1 else c2