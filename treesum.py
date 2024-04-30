class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    # for search bfs or dfs, do not return anything i.e. just use return. for sum return 0
    
    # Sum of the current node's value plus the sum of its left and right subtrees
    return root.value + tree_sum(root.left) + tree_sum(root.right)

def tree_sum_with_memoization(root, memo={}):
    if root is None:
        return 0

    # Check if the result for the current node is already memoized
    if root in memo:
        return memo[root]

    # Sum of the current node's value plus the sum of its left and right subtrees
    result = root.value + tree_sum_with_memoization(root.left, memo) + tree_sum_with_memoization(root.right, memo)

    # Memoize the result for the current node
    memo[root] = result

    return result

# Example usage:
# Construct a binary tree
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

total_sum = tree_sum(root)
print("Sum of all nodes in the binary tree:", total_sum)
