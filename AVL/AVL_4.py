def nameValue(val):
    # Code Here
    pass

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class AVL_Tree(object):
    def __init__(self):
        self.root = None

    def insert(self,data):
        self.root = self._insert(self.root,data)
        return self.root

    def _insert(self, root, data):
        if not root : 
            return TreeNode(data)
        elif self.getASCII(data) < self.getASCII(root.val):
            root.left = self._insert(root.left,data)
        else : 
            root.right = self._insert(root.right,data)
        asciiLval = asciiRval = None 
        if root.right :
            asciiRval = self.getASCII(root.right.val)
        if root.left :
            asciiLval = self.getASCII(root.left.val)
        asciidata = self.getASCII(data)
        barance = self.getBalance(root)
        if asciiRval and barance < -1 and asciidata > asciiRval:
            root = self.leftRotate(root)
        elif asciiLval and barance >1 and asciidata < asciiLval :
            root = self.rightRotate(root)
        elif asciiRval and barance < -1 and asciidata < asciiRval :
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        elif asciiLval and barance > 1 and asciidata > asciiLval:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        return root
    
    def findroot(self,data):
        return self._findroot(self.root,self.getASCII(data))

    def _findroot(self,root,data):
        if not root:
            return
        elif self.getASCII(root.val) > data:
            return self._findroot(root.left,data)
        elif self.getASCII(root.val) < data :
            return self._findroot(root.right,data)
        else:
            return root

    def delete(self,data):
        self.root = self._delete(self.root,data)
        return self.root

    def _delete(self, root, data):
        if not root :
            return root
        elif self.getASCII(root.val) > self.getASCII(data) :
            root.left = self._delete(root.left,data)
        elif self.getASCII(root.val) < self.getASCII(data):
            root.right = self._delete(root.right,data)
        else:
            if root.right == None :
                return root.left
            if root.left == None:
                return root.right
            temp = self.getMinValueNode(root.right)
            temp.right = self._delete(root.right,temp.val)
            temp.left = root.left
            root = temp

        if root == None:
            return root

        barance = self.getBalance(root)
        if   barance < -1 and self.getBalance(root.right) <=0 :
            root = self.leftRotate(root)
        elif  barance >1 and self.getBalance(root.left) >=0 :
            root = self.rightRotate(root)
        elif  barance < -1 and self.getBalance(root.right) >0 :
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        elif barance > 1 and self.getBalance(root.left) <0 :
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        return root
    
    def leftRotate(self, root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        return temp

    def rightRotate(self, root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        return temp

    def getHeight(self, root):
        if not root:
            return 0
        return 1+max(self.getHeight(root.right) , self.getHeight(root.left))

    def getBalance(self, root):
        return self.getHeight(root.left) - self.getHeight(root.right)


    def getMinValueNode(self, root):
        if root == None:
            return 
        if  root.left == None and root.right == None:
            return root
        elif root.left == None:
            return root
        return self.getMinValueNode(root.left)

    def getASCII(self,string):
        val = 0
        for i in string : 
            val += ord(i)
        return val

    def printTree(self, root,printdok = 0, level=0):
        if root != None :
            print(f'    '* level+f'{root.val} ({self.getASCII(root.val)})')
            if root.right == None and root.left == None  :
                self.printTree(root.left,0, level + 1)
                self.printTree(root.right,0, level + 1)
            else:
                self.printTree(root.left,1, level + 1)
                self.printTree(root.right,1, level + 1)
        elif printdok :
            print('    ' * level+"*")
            
            


avl_tree = AVL_Tree()
root = None
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(data)
    elif op == "D":
        root = avl_tree.delete(data)
    elif op == "P":
        avl_tree.printTree(root)
        print("------------------------------")