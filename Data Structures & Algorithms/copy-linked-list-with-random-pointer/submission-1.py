"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Create copy nodes and interleave them
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next
        
        # Step 2: Set random pointers for copy nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate original and copy list
        current = head
        copy_head = head.next
        while current:
            copy_node = current.next
            current.next = copy_node.next
            if copy_node.next:
                copy_node.next = copy_node.next.next
            current = current.next
        
        return copy_head