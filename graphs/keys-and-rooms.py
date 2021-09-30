class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #recursion
        visited=set()
        def dfs(key):
            if key not in visited:
                visited.add(key)
                for keys in rooms[key]:
                    if keys not in visited:dfs(keys)
        dfs(0)
        return len(visited)==len(rooms)
        #ietartive dfs
        # visited=set()
        # stack=[0]
        # while stack:
        #     key=stack.pop()
        #     if key not in visited:
        #         visited.add(key)
        #         for keys in rooms[key]:
        #             if keys not in visited:
        #                 stack.append(keys)
        # return len(rooms)==len(visited)
        