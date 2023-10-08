class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height =1

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def getbarance(self,root):
        if root:
            return self.get_height(root.left) - self.get_height(root.right)
        return 0
    
    def get_height(self,root):
        if root :
            return root.height
        return 0 

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if not root :
            return Node(data)
        elif data < root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        root.height = max(self.get_height(root.right),self.get_height(root.left))+1
        newbarance = self.getbarance(root)
        if newbarance >1 or newbarance < -1:
            return self.reBarance(root)
        return root

    def reBarance(self,root):
        barance = self.getbarance(root)
        if barance >1  :
            if self.getbarance(root.left) <= -1  :
                root.left = self.rotateRight(root.left)
            root = self.rotateLeft(root)
        elif barance < -1:
            if self.getbarance(root.right) >= 1:
                root.right = self.rotateLeft(root.right)
            root = self.rotateRight(root)
        return root

    def rotateLeft(self,root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        root.height = max(self.get_height(root.right),self.get_height(root.left))+1
        temp.height = max(self.get_height(temp.right),self.get_height(temp.left))+1
        return temp
    
    def rotateRight(self,root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        root.height = max(self.get_height(root.right),self.get_height(root.left))+1
        temp.height = max(self.get_height(temp.right),self.get_height(temp.left))+1
        return temp
    

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

newAVL = AVL()
inp = input("Enter Input : ").split()
for i in inp:
    newAVL.insert(int(i))
newAVL.printTree(newAVL.root)
