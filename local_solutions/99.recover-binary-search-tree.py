#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convert_treenode_to_list_breadth(node):
    result_list = []
    my_queue = []
    my_queue.append(root)
    while(my_queue):
        tmp = my_queue.pop(0)
        if tmp is None:
            result_list.append(None)
        else:
            my_queue.append(tmp.left)
            my_queue.append(tmp.right)
            result_list.append(tmp.val)

    return result_list

# def convert_treenode_to_list_depth(node):
#     result_list = []
#     my_queue = []
#     my_queue.append(root)
#     while(my_queue):
#         tmp = my_queue.pop(0)
#         if tmp is None:
#             result_list.append(None)
#         else:
#             my_queue.append(tmp.left)
#             result_list.append(tmp.val)
#             my_queue.append(tmp.right)
#     return result_list

def convert_treenode_to_list_depth(node):
    if node is None:
        return [None]
    result_list = []
    my_stack = []
    cur = node
    while True:
        if cur is not None:
            my_stack.append(cur)
            cur = cur.left
        elif (my_stack):
            result_list.append(None)
            cur = my_stack.pop()
            ## visit cur
            result_list.append(cur.val)
            cur = cur.right
        else:
            result_list.append(None)
            break
    return result_list

            



def convert_treenode_to_list_depth_recur(node):
    if node is None:
        return [None]
    return convert_treenode_to_list_depth_recur(node.left) + \
           [node.val] + \
           convert_treenode_to_list_depth_recur(node.right)






prev_element = TreeNode(-2**31 -1)
first_element = None
second_element = None
def recoverTree(root) -> None:
    global first_element
    global second_element
    global prev_element

    def recover_tree_helper(root):
        global first_element
        global second_element
        global prev_element
        if root is None:
            return None
        recover_tree_helper(root.left)
        if (first_element is None) and (prev_element.val >= root.val):
            first_element = prev_element
        if (first_element is not None) and (prev_element.val >= root.val):
            second_element = root
        prev_element = root
        recover_tree_helper(root.right)
        return None
    recover_tree_helper(root)
    tmp = first_element.val
    first_element.val = second_element.val
    second_element.val = tmp
    return root


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    four = TreeNode(4)
    four.left = TreeNode(2)
    root.right = four
    print(convert_treenode_to_list_breadth(root))
    print(convert_treenode_to_list_depth(root))
    print(convert_treenode_to_list_depth_recur(root))
    recoverTree(root)
    print(convert_treenode_to_list_breadth(root))
    print(convert_treenode_to_list_depth(root))
    print(convert_treenode_to_list_depth_recur(root))

    # print(1)
