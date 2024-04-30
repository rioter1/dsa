class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

print("DFS traversal of binary tree (recursive):")
dfs_binary_tree_recursive(root)


#################### DFS without print statement

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_binary_tree_recursive(node):
    result = []  # List to store DFS traversal results

    def dfs_helper(current_node):
        if current_node is not None:
            result.append(current_node.value)  # Store the value of the current node
            dfs_helper(current_node.left)
            dfs_helper(current_node.right)

    dfs_helper(node)
    return result