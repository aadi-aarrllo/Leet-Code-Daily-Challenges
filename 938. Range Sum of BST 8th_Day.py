'''Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.

Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique.'''

# Solution ----------------------------------------------------------------------------------------------------------------------------------

# DFS

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.sum = 0
        self.dfs(root, low, high)
        return self.sum
    
    def dfs(self, root, low, high):
        if root:
            if low <= root.val <= high:
                self.sum += root.val
            if low < root.val:
                self.dfs(root.left, low, high)
            if root.val < high:
                self.dfs(root.right, low, high)

# Runtime: 212 ms, faster than 99.05% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.3 MB, less than 99.97% of Python3 online submissions for Range Sum of BST.

# BFS

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        queue = [root]
        while queue:
            node = queue.pop()
            if node:
                if low <= node.val <= high:
                    sum += node.val
                if low < node.val:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)
        return sum
    
# Runtime: 232 ms, faster than 95.88% of Python3 online submissions for Range Sum of BST.
# Memory Usage: 22.2 MB, less than 99.97% of Python3 online submission for Range Sum of BST