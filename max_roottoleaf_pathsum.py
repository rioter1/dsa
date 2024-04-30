class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def max_path_sum(root):
    def helper(node):
        nonlocal max_sum
        if not node:
            return 0

        # Calculate the maximum path sum for the left and right subtrees
        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        # Update the maximum path sum considering the current node as the root
        current_path_sum = node.value + left_sum + right_sum
        max_sum = max(max_sum, current_path_sum)

        # Return the maximum path sum for the current subtree (including the current node)
        return node.value + max(left_sum, right_sum)

    max_sum = float('-inf')  # Initialize with negative infinity
    helper(root)
    return max_sum

def max_path_sum_with_memoization(root, memo={}):
    def helper(node, max_sum):
        if not node:
            return 0

        # Check if the result for the current node is already memoized
        if node in memo:
            return memo[node]

        # Calculate the maximum path sum for the left and right subtrees
        left_sum = max(helper(node.left, max_sum), 0)
        right_sum = max(helper(node.right, max_sum), 0)

        # Update the maximum path sum considering the current node as the root
        current_path_sum = node.value + left_sum + right_sum
        max_sum[0] = max(max_sum[0], current_path_sum)

        # Memoize the result for the current node
        memo[node] = node.value + max(left_sum, right_sum)

        # Return the maximum path sum for the current subtree (including the current node)
        return memo[node]

    max_sum = [float('-inf')]  # Use a list to emulate a mutable value
    helper(root, max_sum)
    return max_sum[0]



# Example usage:
# Construct a binary tree
#        10
#       / \
#      2   10
#     / \    \
#    20  1   -25
#             / \
#            3   4

root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

result = max_path_sum(root)
print("Maximum root-to-leaf path sum:", result)
