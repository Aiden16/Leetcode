class Solution:
    def minReorder(self, n: int, c: List[List[int]]) -> int:
        chuck=set()
        routes={}
        nei=defaultdict(list)
        adj=defaultdict(list)
        for i in c:
            adj[i[0]].append(i[1])
            nei[i[0]].append(i[1])
            nei[i[1]].append(i[0])
        seen=set()
        flag=1
        def bfs(root):
            qu=deque([root])
            cost=0
            seen.add(root)
            while qu:
                node=qu.popleft()
                seen.add(node)
                flag=1
                parent=node
                for n in nei[node]:
                    if n not in seen:
                        qu.append(n)
                        if n in adj:
                            for reach in adj[n]:
                                if reach==parent:
                                    flag=0
                                    break
                            if flag:
                                cost+=1
                            flag=1
                        else:
                            cost+=1
            return cost
        # print(bfs(0))
        return bfs(0)
        # return cost
        
        #--passed 27 test cases----------------------#
        # for i in range(len(c)):
        #     if c[i][0] in routes:
        #         routes[c[i][0]].append(c[i][1])
        #     else:
        #         routes[c[i][0]]=[c[i][1]]
        # def check(i):
        #     if i not in routes:
        #         chuck.add(i)
        #         return 1
        #     qu=deque([i])
        #     count=0
        #     while qu:
        #         for i in range(len(qu)):
        #             node=qu.popleft()
        #             # print(node)
        #             if node in routes:
        #                 for nei in routes[node]:
        #                     if nei == 0 or nei in chuck:
        #                         return 0
        #                     qu.append(nei)
        #                     # print(nei)
        #                     chuck.add(nei)
        #                     count+=1
        #             else:
        #                 # print('-------')
        #                 return count
        #     return count
        # ans=0
        # for i in range(1,n):
            # print(i,check(i))
            # ans+=check(i)
            # ans+=check(i)
        # print(ans)
        # return ans
        # check(4)
        # print(routes)
        