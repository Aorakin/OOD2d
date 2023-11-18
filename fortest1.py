class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
    
    def __str__(self):
        return str(self.data)
    
class AVL():
    def __init__(self):
        self.root = None
    
    def getheight(self,node):
        if node == None :
            return 0
        return 1+max(self.getheight(node.left),self.getheight(node.right))
    
    def getbarance(self,node):
        return self.getheight(node.left)-self.getheight(node.right)

    def rotateright(self,node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp
    
    def rotateleft(self,node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp

    def rebarance(self,node):
        barance  = self.getbarance(node)
        print(barance)
        if barance >1 :
            if self.getbarance(node.left) ==-1:
                node.left = self.rotateleft(node.left)
            node = self.rotateright(node)
        elif barance <-1:
            if self.getbarance(node.right) == 1 :
                node.right = self.rotateright(node.right)
            node = self.rotateleft(node)
        return node

    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if root == None:
            return Node(data)
        if root.data > data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        root = self.rebarance(root)
        return root
    
    def delete(self,data):
        self.root = self._delete(self.root,data)
        return self.root

    def _delete(self,root,data):
        if root.data > data:
            root.left = self._delete(root.left,data)
        elif root.data < data:
            root.right = self._delete(root.right,data)
        else:
            if root.left == None:
                return root.right
            elif root.right ==None:
                return root.left 
            cur = root.left
            while cur.right != None:
                cur = cur.right
            root.data = cur.data
            root.left = self._delete(root.left,root.data)
        root = self.rebarance(root)
        return root
    
    def printFormat(self,node,level):
        if node != None:
            self.printFormat(node.right,level+1)
            print("    "*level,node)
            self.printFormat(node.left,level+1)
    
newAVL = AVL()
list = [6,3,1,2,4,5,8,9]
for i in list :
    newAVL.insert(i)
newAVL.printFormat(newAVL.root,0)
newAVL.delete(8)
newAVL.printFormat(newAVL.root,0)
