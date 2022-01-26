def convertToDLL(root):
    #return the head of the DLL and remove those node from the tree as well.
    leaves = []
    def recur(root):
        if not root.left and not root.right:
            leaves.append(root)
            return None
        if root.left:
            root.left = recur(root.left)
        if root.right:
            root.right = recur(root.right)
        return root
    recur(root)
    for i in range(len(leaves)-1):
        leaves[i].right = leaves[i+1]
    for i in range(len(leaves)-1,0,-1):
        leaves[i].left = leaves[i-1]
    return leaves[0]