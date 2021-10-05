# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        qu=deque([root])
        hv_null=False
        while qu:
            node=qu.popleft()
            if not node:
                hv_null=True
                continue
            if hv_null:return False
            qu.append(node.left)
            qu.append(node.right)
        return True
            
        
        #optimal
        # qu=deque([root])
        # hv_null=False
        # while qu:
        #     node=qu.popleft()
        #     if not node:
        #         hv_null=True
        #         continue
        #     if hv_null:return False
        #     qu.append(node.left)
        #     qu.append(node.right)
        # return True
        
        #daheck
#         level=0
#         qu=deque([root])
#         temp=[]
#         while qu:
#             for i in range(len(qu)):
#                 node=qu.popleft()
#                 if node.left:
#                     qu.append(node.left)
#                 if node.right:
#                     qu.append(node.right)
#             level+=1
#         last_level=level-1
#         qu=deque([root])
#         level=0
#         tmp=[]
#         couldbe=0
#         while qu:
#             for i in range(len(qu)):
#                 node=qu.popleft()
#                 tmp.append(node.val)
#                 if node.left:
#                     qu.append(node.left)
#                 if node.right:
#                     qu.append(node.right)
#                 if level==last_level-1:
#                     if node.right and not node.left:
#                         return False
#                     if (node.left and not node.right) or (not node.left and not node.right):
#                         couldbe=1
#                     if couldbe and qu:
#                         if (qu[0].left and qu[0].right) or (qu[0].left and not qu[0].right):
#                             return False
#             couldbe=0
#             level+=1
#             if level!=last_level+1 and len(tmp)!=2**(level-1):
#                 return False
#             tmp=[]
#         return True
                
        