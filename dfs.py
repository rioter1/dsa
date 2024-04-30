class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_binary_tree(root):
    if not root:
        return

    stack = [root]

    while stack:
        current = stack.pop()

        print(current.value, end=' ')  # Do whatever you want with the current node

        # Push the right child first, so it gets popped off the stack first (LIFO)
        if current.right:
            stack.append(current.right)

        # Push the left child
        if current.left:
            stack.append(current.left)

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

print("DFS traversal of binary tree:")
dfs_binary_tree(root)
