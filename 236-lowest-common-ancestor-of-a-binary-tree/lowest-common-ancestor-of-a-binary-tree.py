# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None
        def lca(root,p,q):
            if root == None:
                return 0
            left = lca(root.left,p,q)
            right = lca(root.right,p,q)

            current = 0
            if root == p or root == q:
                current = 1
            total = left + right + current
            if total == 2 and self.ans == None:
                self.ans = root
            return total
        
        lca(root,p,q)
        return self.ans