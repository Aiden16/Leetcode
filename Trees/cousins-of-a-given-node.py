class Solution:
    def printCousins(self, root, tar):
        #code here
        qu = deque([[root,-1]])
        flag = 0
        ans = []
        while qu:
            if flag:
                # print(qu,p)
                for ele,par in qu:
                    if par!=p:
                        # print('----',ele.data)
                        ans.append(ele.data)
                    flag = 0
            for i in range(len(qu)):
                node,parent = qu.popleft()
                if node.left:
                    if node.left == tar:
                        # print('leftttttt')
                        flag,p = 1,node.data
                    qu.append([node.left,node.data])
                if node.right:
                    if node.right == tar:
                        # print('rightttt')
                        flag,p = 1,node.data
                        
                    qu.append([node.right,node.data])
        return ans if ans else [-1]