# https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.answer = True

        def dfs(root):
            l, r = 0, 0

            if root.left:
                l += dfs(root.left)
            if root.right:
                r += dfs(root.right)
            if abs(r-l) > 1:
                self.answer = False

            return max(r, l) + 1
        dfs(root)
        return self.answer
