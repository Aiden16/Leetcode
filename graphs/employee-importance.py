"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp={empl.id : empl for empl in employees}
        # print(emp[id].importance)
        self.s=0
        def dfs(_id):
            self.s+=emp[_id].importance
            for ids in emp[_id].subordinates:
                dfs(ids)
            return self.s
        dfs(id)
        return self.s
            
        # ans=0
        # qu=deque([])
        # for i in range(len(employees)):
        #     if employees[i].id==id:
        #         ans+=employees[i].importance
        #         for ids in employees[i].subordinates:
        #             qu.append(ids)
        #         break
        # while qu:
        #     _id=qu.popleft()
        #     for i in range(len(employees)):
        #         if employees[i].id==_id:
        #             ans+=employees[i].importance
        #             for ids in employees[i].subordinates:
        #                 qu.append(ids)
        #             break
        # return ans
 
        