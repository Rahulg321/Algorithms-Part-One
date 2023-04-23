# implementing a basic tree structure in python


class TreeNode:
    def __init__(self, data, children=None):
        self.data = data
        if children is None:
            self.children = []

    def __str__(self, level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)

        return ret

    def add_child(self, TreeNode):
        self.children.append(TreeNode)


tree = TreeNode("drinks")

hot = TreeNode("Hot")
cold = TreeNode("Cold")

coffee = TreeNode("Coffee")
tea = TreeNode("Tea")

fanta = TreeNode("Fanta")
milk = TreeNode("Milk")

tree.add_child(hot)
tree.add_child(cold)


hot.add_child(coffee)
hot.add_child(tea)

cold.add_child(fanta)
cold.add_child(milk)


print(tree)
