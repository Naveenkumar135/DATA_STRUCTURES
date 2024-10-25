class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_item(self,data):
        if not self.data:
            return BST(data)
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_item(data)
            else:
                self.left = BST(data)
        elif data > self.data:
            if self.right:
                self.right.add_item(data)
            else:
                self.right = BST(data)
                

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def search(self,data):
        if data ==self.data:
            print(True)
            return
        if data < self.data:
            if self.left:
                self.left.search(data)
            else:
                print(False)
                return
        elif data > self.data:
            if self.right:
                self.right.search(data)
            else:
                print(False)
                return



if __name__ == "__main__":

    binary_tree = BST(6)
    binary_tree.print_tree()
    binary_tree.add_item(1)
    binary_tree.add_item(3)
    binary_tree.add_item(9)
    binary_tree.add_item(7)
    binary_tree.print_tree()
    binary_tree.search(1)
