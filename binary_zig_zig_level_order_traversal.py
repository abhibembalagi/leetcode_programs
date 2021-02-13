# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        def depth_search(root,level,results):
            if not root:
                return
            if len(results) <= level:
                results += [[]]
            depth_search(root.left,level+1,results)
            depth_search(root.right,level+1,results)
            if level % 2 == 0 :
                results [level].append(root.val)
            else:
                results [level].insert(0,root.val)
        depth_search(root,0,results)
        return results
