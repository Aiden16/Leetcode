class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ans=[]
        def ss(arr):
            if not arr:
                return ['']
            first=arr[0]
            rs=ss(arr[1:])
            tmp=[]
            for i in range(len(rs)):
                tmp.append(str(rs[i]))
            for i in range(len(rs)):
                if str(rs[i])!='':
                    tmp.append(str(first)+','+str(rs[i]))
                else:
                    tmp.append(str(first)+str(rs[i]))
            return tmp
        tmp=ss(nums)
        ans=[]
        # print(tmp)
        for i in tmp:
            ans.append([i])
        return ans
        # print(ans)
        
        # arr=deque([])
        # for ind,val in enumerate(nums):
        #     arr.append([[val],ind])
        # print(arr)
        # ans=[[]]
        # def bfs(arr):
        #     while arr:
        #         node,ind=arr.popleft()
        #         ans.append(node)
        #         for i in range(ind+1,len(nums)):
        #             arr.append([node+[nums[i]],i])
        # bfs(arr)
        # # print(ans)
        # return ans
        