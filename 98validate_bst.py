# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.helper(float("-inf"), root, float("inf"))

    def helper(self, left_bound, root, right_bound):
        if not root:
            return True

        if not left_bound < root.val < right_bound:
            return False

        left = self.helper(left_bound, root.left, root.val)
        right = self.helper(root.val, root.right, right_bound)

        return left and right
