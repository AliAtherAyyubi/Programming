

class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.data=item


class BinaryTree:
    def __init__(self):
        self.root=None

    def preOrder(self,root):
        if root:
            print(root.data," ",end="")
            self.preOrder(root.left)
            self.preOrder(root.right)


tree= BinaryTree()

tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.right=Node(3)

tree.preOrder(tree.root)
    
        
