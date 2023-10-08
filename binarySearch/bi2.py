class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
class BST():
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self._insert(self.root,data)
    
    def _insert(self,root,data):
        if root == None :
            return Node(data)
        if data < root.data :
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        return root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def height(self,root):
        if not root.left and not root.right:
            return 0
        count1 = count2 = 0
        if root.left :
            count1 = self.height(root.left)
        if root.right :
            count2 = self.height(root.right)
        return max(count1, count2) + 1

inp  = input("Enter Input : ").split()
new_tree = BST()
for i in inp:
    new_tree.insert(int(i))
# new_tree.printTree(new_tree.root)
print("Height of this tree is : {}".format(new_tree.height(new_tree.root)))
