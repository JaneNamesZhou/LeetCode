# Checked Date: 2023/01/30

# Given the root of a binary tree, return the inorder traversal of its nodes' values.
#
#
#
# Example 1:
#
#
# Input: root = [1,null,2,3]
# Output: [1,3,2]


# Example 2:
#
# Input: root = []
# Output: []


# Example 3:
#
# Input: root = [1]
# Output: [1]
#
#
# Constraints:
#
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root) -> List[int]:
    result = []
    if root == None:
        return result
    if root.left == None and root.right == None:
        result.append(root.val)
        return result

    if root.left != None:
        result += inorderTraversal(root.left)
    result.append(root.val)
    if root.right != None:
        result += inorderTraversal(root.right)
    return result


if __name__ == "__main__":
    e3 = TreeNode(3, None, None)
    e2 = TreeNode(2, e3, None)
    e1 = TreeNode(1, None, e2)
    print(inorderTraversal(e1))
