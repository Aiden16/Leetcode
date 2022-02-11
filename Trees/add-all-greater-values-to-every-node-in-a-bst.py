def modify(root):
    def recurSum(root):
        if not root:
            return 0
        left = recurSum(root.left)
        right = recurSum(root.right)
        return left+right+root.data
    tree_sum = recurSum(root)
    
    def inorder(root,tree_sum):
        nonlocal sum_so_far
        if not root:
            return 
        left = inorder(root.left,tree_sum)
        tmp = root.data
        root.data = tree_sum-sum_so_far
        sum_so_far+=tmp
        right = inorder(root.right,tree_sum)
    sum_so_far = 0
    inorder(root,tree_sum)
    
    return root