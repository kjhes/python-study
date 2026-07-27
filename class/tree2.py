class TreeNode:
    def __init__(self,data):
        self.left =None
        self.right = None

root = TreeNode(10)
root.left  = TreeNode(20)
root.right = TreeNode(30)

print("루트",root.data)
print("왼쪽 자식",root.left.data)
print("오른쪽 자식",root.right.data)

class TreeNode2:
    def __init__(self,data):
        self.left =None
        self.right = None
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(60)
root.right.right = TreeNode(70)
root.left.left = TreeNode(40)
root.left.right = TreeNode(50)


# 전위 순행
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("전위순회")
preorder(root)

# 중위 순행 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    inorder(node.left)
    print(node.data,end =" ")
    inorder(node.right)

# 후위 순행
def postorder(node):
    if node is not None:
        postorder(node.left)