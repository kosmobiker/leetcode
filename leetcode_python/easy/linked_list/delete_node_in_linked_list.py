"""
There is a singly-linked list `head` and we want to delete a node `node` in it.
You are given the node to be deleted `node`. You will **not be given access** to the first node of `head`.
All the values of the linked list are **unique**, and it is guaranteed that the given node `node` is not the last node in the linked list.
Delete the given node. Note that by deleting the node, we do not mean removing it from memory. 

We mean:

    1. The value of the given node should not exist in the linked list.
    2. The number of nodes in the linked list should decrease by one.
    3. All the values before node should be in the same order.
    4. All the values after node should be in the same order.

Custom testing:

    1. For the input, you should provide the entire linked list head and the node to be given node. 
    node should not be the last node of the list and should be an actual node in the list.
    2. We will build the linked list and pass the node to your function.
    3. The output will be the entire list after calling your function.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        nextNode = node.next
        # Step 2
        node.val = nextNode.val
        # Step 3
        node.next = nextNode.next
        nextNode.next = None
        del(nextNode)
    

if __name__ == '__main__':
    
    
    # # Test case 1
    head1 = ListNode([4,5,1,9])

    print(head1.val)
    print(head1.next)
    # assert r1 == expected1, f"Test Case 1 Failed: expected output {expected1}, but got {r1}"
    
    # # Test case 2
    # node2 = 1
    # expected2 = [4,5,9]
    # r2 = s.deleteNode(node2)
    # assert r2 == expected2, f"Test Case 2 Failed: expected output {expected2}, but got {r2}" 
   