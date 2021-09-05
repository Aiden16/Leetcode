class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # print(p)
        if p == root or q==root:
            return root
        dic={root:None}
        lis=[]
        qu=[root]
        level=1
        while qu:
            for i in range(len(qu)):
                node=qu.pop(0)
                if node.left:
                    qu.append(node.left)
                    dic[node.left]=node
                if node.right:
                    qu.append(node.right)
                    dic[node.right] = node
        while p:
            lis.append(p)
            p=dic[p]
        while q not in lis:
            q=dic[q]
        # print(q)
        return q
            
        # print(dic)
        
#         if dic[p.val]==dic[q.val]:
#             print('if')
#             return dic[p.val][0]
#         else:
#             print('else')
#             if dic[p.val][1]<dic[q.val][1]:
#                 while True:
#                     if dic[q.val][0]==p:
#                         return p
#                     if dic[q.val][0]==dic[p.val][0]:
#                         return dic[p.val][0]
                    
#                 print('else p')
#                 return p
#             else:
#                 print('else q')
#                 return q
#         # cur=root
#         # while cur:
#         #     if p>cur.val and q>cur.val:
#         #         cur
        