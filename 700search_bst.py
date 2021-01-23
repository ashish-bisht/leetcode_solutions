# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return

        if root.val == val:
            return root

        left = right = None

        if root.val > val:
            left = self.searchBST(root.left, val)

        else:
            right = self.searchBST(root.right, val)

        return left if not right else right
