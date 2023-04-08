class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
prev_node = TreeNode(-10000000)

def isValidBST( root) -> bool:
    global prev_node
    # prev node method
    if root is None:
        return True
    res_left = isValidBST(root.left)
    if prev_node.val >= root.val:
        return False
    prev_node = root
    res_right = isValidBST(root.right)
    return (res_left and res_right)

if __name__ == '__main__':
    # root_ = TreeNode(2)
    # root_.left = TreeNode(1)
    # root_.right = TreeNode(3)
    print(isValidBST(TreeNode(0)))