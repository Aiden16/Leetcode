class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [i for i in range(len(edges)+1)]
        parent={}#node:parent
        rank={}#node:rank
        for i in range(1,len(edges)+1):
            parent[i]=-1
            rank[i]=1
        def find(n):
            p=parent[n]
            if p==-1:
                return n
            while parent[p]!=-1:
                p=parent[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
            
            
        #array
            
        parent = [i for i in range(len(edges)+1)]
        rank=[1]*(len(edges)+1)
        
        def find(n):
            p=parent[n]
            while p!=parent[p]:
                p=parent[p]
            return p
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            else:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            return True
        for n1,n2 in edges:
            if not union(n1,n2):
                return [n1,n2]