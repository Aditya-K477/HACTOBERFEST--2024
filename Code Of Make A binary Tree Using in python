# Definition of a Node in the Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Binary Tree class with common operations
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a new node in the binary tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    # Helper method to insert nodes recursively
    def _insert(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    # In-order traversal: Left, Root, Right
    def inorder_traversal(self):
        return self._inorder_helper(self.root, result=[])
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
        return result

    # Pre-order traversal: Root, Left, Right
    def preorder_traversal(self):
        return self._preorder_helper(self.root, result=[])
    
    def _preorder_helper(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)
        return result

    # Post-order traversal: Left, Right, Root
    def postorder_traversal(self):
        return self._postorder_helper(self.root, result=[])
    
    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)
        return result

# Example usage
if __name__ == "__main__":
    # Creating a binary tree and inserting nodes
    tree = BinaryTree()
    tree.insert(3)  # Root node
    tree.insert(1)
    tree.insert(5)
    tree.insert(2)
    tree.insert(4)

    print("In-order traversal:", tree.inorder_traversal())
    print("Pre-order traversal:", tree.preorder_traversal())
    print("Post-order traversal:", tree.postorder_traversal())
