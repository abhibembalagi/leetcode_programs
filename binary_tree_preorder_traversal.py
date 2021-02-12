# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        node_values=[]
        self.preorder_traversal(root,node_values)
        return node_values
    def preorder_traversal(self,root,node_values):
        if root is not None:
            node_values.append(root.val)
            self.preorder_traversal(root.left,node_values)
            self.preorder_traversal(root.right,node_values)
        return node_values
