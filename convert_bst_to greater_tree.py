# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        summ=[0]
        def greater_tree(root,sum_arr):
            if not root:
                return
            else:
                greater_tree(root.right,sum_arr)
                sum_arr[0]=sum_arr[0] + root.val
                root.val = sum_arr[0]
                greater_tree(root.left,sum_arr)
            return root
        greater_tree(root,summ)
        return root
