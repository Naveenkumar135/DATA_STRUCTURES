class TreeNode:

    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,data):
        data.parent = self
        self.children.append(data)

    def get_level(self):
        level = 0
        p=self.parent
        while p:
            p = p.parent
            level+=1
        # print(level)

        return level

        
    
    def print_tree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_tree_format(self):
        spaces = " " * self.get_level() * 2
        print(spaces + "|--->" + self.data)
        if self.children:
            for child in self.children:
                child.print_tree_format()




def tree_node_test():
    root = TreeNode("mobiles")
    vivo = TreeNode("vivo")
    root.add_child(vivo)
    oppo = root.add_child(TreeNode("oppo"))
    samsung = root.add_child(TreeNode("samsung"))

    v1 = vivo.add_child(TreeNode("v1"))

    root.get_level()

    root.print_tree()

    root.print_tree_format()

    return root

if __name__ == '__main__':
    tree_node_test()

