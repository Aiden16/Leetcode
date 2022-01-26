class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        #code here
        tmp = curr_node.next.data
        curr_node.next = curr_node.next.next
        curr_node.data = tmp