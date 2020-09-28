class Node:
    def __init__(self, key):
        self.data = key
        self.left_child = None
        self.right_child = None


class BSTDemo:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not isinstance(key, Node):
            key = Node(key)
        if self.root == None:
            self.root = key
        else: 
            self._insert(self.root, key)

    def _insert(self, curr, key):
        
        if key.data > curr.data:
            if curr.right_child == None:
                curr.right_child = key
            else: 
                self._insert(curr.right_child, key)

        elif key.data < curr.data:
            if curr.left_child == None:
                curr.left_child = key
            else:
                self._insert(curr.left_child, key)

    def in_order(self):
        #left, root, right
        self._in_order(self.root)

    def _in_order(self, curr):
        if curr:
            self._in_order(curr.left_child)
            print(curr.data, end = " ")
            self._in_order(curr.right_child)

    def find_val(self, key):
        return self._find_val(self.root, key)

    def _find_val(self, curr, key):
        
        if curr:
            if key == curr.data:
                return "Value found in tree"
            elif key < curr.data:
                return self._find_val(curr.left_child, key)
            else: 
                return self._find_val(curr.right_child, key)

        return "Value not found in tree"
        
    def pre_order(self):
        pass

    def _pre_order(self, curr):
        pass

    def post_order(self):
        pass

    def _post_order(self, curr):
        pass
    
    def delete_val(self, key):
        self._delete_val(self.root, None, None, key)

    def _delete_val(self, curr, prev, is_left, key):
        if curr:
            
            if key == curr.data:
    
                if is_left:
                    prev.left_child = None
                else:
                    prev.right_child = None

            elif key < curr.data:
                self._delete_val(curr.left_child, curr, True, key)
            elif key > curr.data:
                self._delete_val(curr.right_child, curr, False, key)

        else: 
            print(f"{key} not found in Tree")


tree = BSTDemo()
tree.insert("F")
tree.insert("G")
tree.in_order()
tree.delete_val("G")
tree.in_order()

# tree.insert("F")
#tree.insert("C")
#tree.insert("G")
#tree.insert("A")
#tree.insert("B")
#tree.insert("K")
#tree.insert("H")
#tree.insert("I")
#tree.insert("J")
#tree.insert("L")
#tree.insert("E")
#tree.in_order()
#print(tree.find_val("E"))