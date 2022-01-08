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



if __name__ == "__main__":
    grandFather = TreeNode('Abdus Samad')

    father = TreeNode('Enus Ali')
    uncle = TreeNode('Ayub Ali')
    me = TreeNode('Md. Rakib')
    cousineOne = TreeNode('Al amin')
    cousineTwo = TreeNode('Shoshi')

    grandFather.add_left_child(father)
    grandFather.add_right_child(uncle)
    father.add_left_child(me)
    uncle.add_left_child(cousineOne)
    uncle.add_right_child(cousineTwo)

    inorder_traversal(father)