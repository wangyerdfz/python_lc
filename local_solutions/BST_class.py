


class BST_node:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None

    def __del__(self):
        print(f'BST_node destructor called, {self.val} is destoryed.')


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def _insert(self, node : BST_node, val):
        if node.val == val:
            return
        if val < node.val:
            if node.left is not None:
                self._insert(node.left, val)
                return
            node.left = BST_node(val)
            self.size += 1
            return
        
        if node.right is not None:
            self._insert(node.right, val)
            return
        node.right = BST_node(val)
        self.size += 1

    def insert(self, val):
        if self.root is None:
            self.root = BST_node(val)
            self.size += 1
        else:
            self._insert(self.root, val)

    def get_min(self):
        return self._get_min(self.root)

    def get_max(self):
        return self._get_max(self.root)

    def get_min_node(self):
        return self._get_min_node(self.root)

    def get_max_node(self):
        return self._get_max_node(self.root)

    def _get_min_node(self, node : BST_node):
        if node is None:
            return None
        cur_node = node
        while(cur_node.left is not None):
            cur_node = cur_node.left
        return cur_node

    def _get_max_node(self, node : BST_node):
        if node is None:
            return None
        cur_node = node
        while(cur_node.right is not None):
            cur_node = cur_node.right
        return cur_node

    def _get_min(self, node : BST_node):
        if node is None:
            return None
        cur_node = node
        while(cur_node.left is not None):
            cur_node = cur_node.left
        return cur_node.val

    def _get_max(self, node : BST_node):
        if node is None:
            return None
        cur_node = self.root
        while(cur_node.right is not None):
            cur_node = cur_node.right
        return cur_node.val


    def _delete(self, node: BST_node, val):
        if node is None:
            return node
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if node.left is None:
                tmp = node.right
                node = None
                self.size -= 1
                return tmp

            if node.right is None:
                tmp = node.left
                node = None
                self.size -= 1
                return tmp

            tmp = self._get_min_node(node.right)
            node.val = tmp.val
            node.right = self._delete(node.right, tmp.val)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)


    def if_exists(self, val):
        cur_node = self.root
        while(cur_node is not None):
            if cur_node.val == val:
                return True
            if cur_node.val > val:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return False


    def print(self):
        print(f'size : {self.size}')
        def _print(list_in):
            if len(list_in)  == 0:
                return
            new_list = []
            print_list = []
            for node in list_in:
                if node is None:
                    print_list += [None]
                else:
                    print_list += [node.val]
                    new_list += [node.left, node.right]
            print(print_list)
            _print(new_list)
        # if self.root is None:
        #     return
        _print([self.root])


    



if __name__ == '__main__':
    bst = BST()
    for i in range(10):
        bst.insert(3*i + 1)
        bst.print()
        bst.insert(3*i - 1)
        bst.print()
        bst.insert(3*i)
        bst.print()
    for i in range(-1, 29):
        bst.delete(i)
        bst.print()

