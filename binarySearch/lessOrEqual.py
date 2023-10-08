class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root,data)
        return self.root
    
    def _insert(self,root,data):
        if not root :
            return Node(data)
        if data < root.data :
            root.left = self._insert(root.left,data)
        else:
            root.right =  self._insert(root.right,data)
        return root
        
    def inOrder(self, val):
        res = self._inOrder(self.root, val)
        print(len(res))

    def _inOrder(self, root, val):
        if not root: 
            return []
        res = []
        res += self._inOrder(root.left, val)
        if root.data <= val:
            res.append(str(root.data))
            res += self._inOrder(root.right, val)
        return res 
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ')
tree, val = inp.split("/")[0], int(inp.split("/")[1])
inp = [int(i) for i in tree.split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print("--------------------------------------------------")
T.inOrder(val)