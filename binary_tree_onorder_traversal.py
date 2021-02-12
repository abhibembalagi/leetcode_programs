# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        arr=[]
        self.inorder_traversal(root,arr)
        return arr
    def inorder_traversal(self,root,array):
        if root:
            self.inorder_traversal(root.left,array)
            array.append(root.val)
            self.inorder_traversal(root.right,array)
        return array
