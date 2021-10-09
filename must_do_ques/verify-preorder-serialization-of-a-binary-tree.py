class Solution(object):
    def isValidSerialization(self, preorder):
        preorder, stack = preorder.split(","), []
        for node in preorder:
            print(stack)
            while stack and node == stack[-1] == "#":
                stack.pop()
                if not stack: return False
                stack.pop()
            stack.append(node)
        print(stack)
        return stack == ["#"]
        