class Solution:
    def printBoundaryView(self, root):
        # Code here
        if not root:
            return 
        boundary = [root.data] 
        
        #function to store left boundary
        def leftBoundary(root):
            if not root:
                return
            if not root.left and not root.right:
                return 
            if not root.left and root.right:
                boundary.append(root.data)
                right = leftBoundary(root.right)
            else:
                boundary.append(root.data)
                left = leftBoundary(root.left)
        #call to left boundary
        if root.left:
            leftBoundary(root.left)
        #function to store leaves
        def leavesBoundary(root):
            if not root:
                return
            if not root.left and not root.right:
                boundary.append(root.data)
            left = leavesBoundary(root.left)
            right = leavesBoundary(root.right)
        
        #call to leavesBoundary
        leavesBoundary(root)
        
        #function sto store right boundary
        def rightBoundary(root):
            if not root:
                return
            if not root.right and not root.left:
                return
            if not root.right and root.left:
                left = rightBoundary(root.left)
                boundary.append(root.data)
            else:
                right = rightBoundary(root.right)
                boundary.append(root.data)
        #call to rightBoundary
        if root.right:
            rightBoundary(root.right)
        return boundary