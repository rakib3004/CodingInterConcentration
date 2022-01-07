class TreeNode:
    def __init__(self,x):
        self.value =x
        self.left = None
        self.right = None

def add_left_child(self, node):
    self.left = node

def add_right_child(self, node):
    self.right = node



if __name__ == "__main__":
    root = TreeNode(1)
    two, three, four, five, six = [TreeNode(x) for x in range(2,7)]

    root.add_left_child(two)
    root.add_right_child(three)
    two.add_left_child(four)
    three.add_left_child(five)
    three.add_rigth_child(six)

    inorder_traversal(root)