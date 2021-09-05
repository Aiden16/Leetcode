# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        pass
        #use postorder
        s=[]
        hash={}#sum:fre
        def post(root):
            if not root:
                return 0
            sub_sum = post(root.left)+post(root.right)+root.val
            hash[sub_sum]=hash.get(sub_sum,0)+1
            s.append(sub_sum)
            return sub_sum
        post(root)
        high_freq=max(list(hash.values()))
        ans=[]
        for key,val in hash.items():
            if val==high_freq:
                ans.append(key)
        return ans
