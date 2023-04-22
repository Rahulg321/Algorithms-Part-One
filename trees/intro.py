import sys


class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self):
        return [str(x) for x in self.children]

    def addChild(self, TreeNode):
        self.children.append(TreeNode)


drinks = TreeNode("Drink", [])
hot = TreeNode("hot", [])
cold = TreeNode("cold", [])

drinks.addChild(hot)
drinks.addChild(cold)


print(sys.version)
# print(drinks)
