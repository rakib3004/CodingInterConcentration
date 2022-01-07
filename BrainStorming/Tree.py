class TreeNode:
    def __init__(self,x):
        self.value =x
        self.left = None
        self.right = None

    def add_left_child(self, node):
        self.left = node

    def add_right_child(self, node):
        self.right = node









def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value, end=" -> ")
    if node.right:
        inorder_traversal(node.right)

def postorder_traversal(node):
    if node.left:
        preorder_traversal(node.left)
    if node.right:
        preorder_traversal(node.right)
    print(node.value, end=" -> ")

def preorder_traversal(node):
    print(node.value, end=" -> ")
    if node.left:
        postorder_traversal(node.left)
    if node.right:
        postorder_traversal(node.right)


if __name__ == "__main__":
    root = TreeNode(1)
    two, three, four, five, six = [TreeNode(x) for x in range(2,7)]

    root.add_left_child(two)
    root.add_right_child(three)
    two.add_left_child(four)
    three.add_left_child(five)
    three.add_right_child(six)

    print("----------Inorder Traversal----------")
    inorder_traversal(root)
    print()

    print("----------Preorder Traversal----------")
    preorder_traversal(root)
    print()

    print("----------Postorder Traversal----------")
    postorder_traversal(root)
    print()