class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVL():
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        print("Insert : ( {0} )".format(data))
        self.root = self._insert(self.root,data)
        self.printTree(self.root)
        print("--------------------------------------------------")

    def _insert(self,root,data):
        if not root :
            return Node(data)
        elif root.data <= data :
            root.right = self._insert(root.right,data)
        else:
            root.left = self._insert(root.left,data)
        root.height = max(self.getheight(root.right),self.getheight(root.left))+1
        barance = self.getbarance(root)
        if barance <-1 or barance >1:
            return self.rebarance(barance,root)
        return root

    def rebarance(self,barance,root):
        if barance >1:
            if self.getbarance(root.left) <=-1:
                root.left = self.rotateRight(root.left)
            root = self.rotateLeft(root)
        elif barance<-1:
            if self.getbarance(root.right) >=1:
                root.right = self.rotateLeft(root.right)
            root = self.rotateRight(root)
        return root
                
    def getheight(self,root):
        if root:
            return root.height
        return 0

    def getbarance(self,root):
        if root:
            return self.getheight(root.left)- self.getheight(root.right)
        return 0

    def rotateLeft(self,root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        root.height = max(self.getheight(root.right),self.getheight(root.left)) +1
        temp.height = max(self.getheight(temp.right),self.getheight(temp.right)) +1
        return temp

    def rotateRight(self,root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        root.height = max(self.getheight(root.right),self.getheight(root.left)) +1
        temp.height = max(self.getheight(temp.right),self.getheight(temp.right))+1
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