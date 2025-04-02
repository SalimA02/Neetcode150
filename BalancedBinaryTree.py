# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
        
#         left = self.height(root.left)
#         right = self.height(root.right)
#         if abs(left - right) > 1:
#             return False
#         return self.isBalanced(root.left) and self.isBalanced(root.right)

#     def height(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0

#         return 1 + max(self.height(root.left), self.height(root.right))

################### DFS ####################

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
