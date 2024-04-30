from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bfs_binary_tree(root):
    if root is None:
        return

    queue = deque([root])

    while queue:
        current = queue.popleft()

        print(current.value, end=' ')  # Do whatever you want with the current node

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

def dfs_binary_tree_recursive(node):
    if node is not None:
        print(node.value, end=' ')  # Do whatever you want with the current node
        dfs_binary_tree_recursive(node.left)
        dfs_binary_tree_recursive(node.right)

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

print("BFS traversal of binary tree:")
bfs_binary_tree(root)

print("\nDFS traversal of binary tree (recursive):")
dfs_binary_tree_recursive(root)
