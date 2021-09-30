class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #recursion
        res=[]
        def dfs(node,path):
            if node == len(graph)-1:res.append(path)
            for nodes in graph[node]:dfs(nodes,path+[nodes])
        dfs(0,[0])
        print(res)
        return res
        #using stack
        # stack=[[0,[0]]]
        # res=[]
        # while stack:
        #     node,path=stack.pop()
        #     if node == len(graph)-1:
        #         res.append(path)
        #     for nodes in graph[node]:
        #         stack.append([nodes,path+[nodes]])
        # return res