class Node:
    def __init__(self,item):
        self.left=None
        self.right=None
        self.item=item
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.item)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.item)
        inorder(root.right)
def preorder(root):
    if root:
        print(root.item)
        preorder(root.left)
        preorder(root.right)
n1=Node(1)
n1.left=Node(2)
n1.right=Node(3)
n1.left.left=Node(4)
n1.left.right=Node(5)
preorder(n1)