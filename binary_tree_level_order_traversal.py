# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        def depth_search(root,level,result):
            if not root:
                return
            if len(result) <=level :
                result += [[]]
            depth_search(root.left,level+1,result)
            depth_search(root.right,level+1,result)
            result[level].append(root.val)
        depth_search(root,0,result)
        return result
