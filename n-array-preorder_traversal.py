"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        array=[]
        def nodes(root):
            array.append(root.val)
            for child in root.children:
                nodes(child)
        if root:
            nodes(root)
        return array
