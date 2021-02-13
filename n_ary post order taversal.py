class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        else:
            nodes=[]
            for c in root.children:
                nodes+=self.postorder(c)
            return nodes+[root.val]
