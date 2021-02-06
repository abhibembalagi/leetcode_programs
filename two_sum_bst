# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        bst=[]
        result=self.inorder(root,bst)
        return self.twoSum(result,k)
    def inorder(self,root,bst):
        if root is None:
            return bst
        bst.append(root.val)
        self.inorder(root.left,bst)
        self.inorder(root.right,bst)
        return bst
    def twoSum(self, result, k):
        d = {}
        for i in range(len(result)):
            target = k - result[i]
            if target in d:
                return True
            d[result[i]] = i
                
