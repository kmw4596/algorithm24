class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def calc_height(root):
    if root is None:
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1

# 이진 트리 생성
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# 이진 트리의 높이 계산
height = calc_height(root)
print("Height of the binary tree:", height)
