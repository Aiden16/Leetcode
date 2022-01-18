# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return
        cur=root
        pre=root
        while True and cur:
            if cur.val>key:
                pre=cur
                cur=cur.left
                dirn='left'
            elif cur.val<key:
                pre=cur
                cur=cur.right
                dirn='right'
            else:
                break
        if not cur:
            return root
        if cur.val==key and cur.val==root.val and not cur.right and not cur.left:
            return
        
        #if it's a leaf node
        if not cur.right and not cur.left:
            if dirn=='left':
                pre.left=None
            else:
                pre.right=None
            
            return root
        #if the node has only left child
        if not cur.right and cur.left:
            if cur.val==root.val:
                return root.left
            if dirn=='left':
                pre.left = cur.left
            else:
                pre.right=cur.left
            return root
        #if the node has only right child
        if not cur.left and cur.right:
            if cur.val==root.val:
                return root.right
            if dirn=='left':
                pre.left = cur.right
            else:
                pre.right = cur.right
                
            return root
                
        #if the node has both right and left child
        '''
        get maximum node in left subtree of node to be deleted
        
        '''
        ma=cur
        pre=ma
        ma=cur.left
        while ma.right:
            pre=ma
            ma=ma.right
        if ma.val == cur.left.val: # if to_del node has only one child which is left
            if ma.left: #if left child of to_del node has left subtree
                cur.val=ma.val
                cur.left=ma.left
                return root
            cur.val=ma.val #if left child of to_del node has no sutree
            cur.left=None
            return root
        
        #now comes, where we have to_del node right subtree
        tmp=ma.val    
        cur.val=tmp
        if ma.left:   #if the right subtree node has left subtree
            pre.right=ma.left
            return root
        pre.right=None
        
    
        return root
            