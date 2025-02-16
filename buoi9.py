# class TreeNode:
#     def __init__(self, root):
#         self.root = root
#         self.children = []
#     def add_child(self, child):
#         self.children.append(child)
    
#     def print_tree(self, level=0):
#         print("  " * level + self.root)  
#         for child in self.children:
#             child.print_tree(level + 1)


# root = TreeNode("Menu")
# nd = TreeNode("pho")
# com = TreeNode("com")
# bun = TreeNode("bun")
# root.add_child(nd)
# root.add_child(com)
# root.add_child(bun)
# nd.add_child("pho ga")
# nd.add_child("pho bo")
# com.add_child("com chien")
# com.add_child("com suon")
# bun.add_child("bun bo")
# bun.add_child("bun rieu")
# root.print_tree()


class Node:
    def __init__(self, key):
        self.left = None  
        self.right = None 
        self.value = key  

class BinaryTree:
    def __init__(self):
        self.root = Node(1)
        self.root.left = Node(2)
        self.root.right = Node(3)
        self.root.left.left = Node(4)
        self.root.left.right = Node(5)
        self.root.right.left = Node(6)
        self.root.right.right = Node(7)

    def count_nodes(self, node):
        if node is None:
            return 0  
        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)  
    def count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1  
        return self.count_leaves(node.left) + self.count_leaves(node.right) 
tree = BinaryTree()
total_nodes = tree.count_nodes(tree.root)
total_leaves = tree.count_leaves(tree.root)
print("Tổng số nút trong cây:", total_nodes)
print("Tổng số lá trong cây:", total_leaves)



