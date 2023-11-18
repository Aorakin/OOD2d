import random
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BiTree():
    def __init__(self):
        self.root = None
    
    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if root ==None:
            return Node(data)
        if root.data > data:
            root.left = self._insert(root.left,data)
        else :
            root.right = self._insert(root.right,data)
        return root
    
    def delete(self,data):
        return self._delete(self.root,data)
    
    def _delete(self,root,data):
        if root == None :
            return root
        if root.data > data:
            root.left = self._delete(root.left,data)
        elif root.data < data:
            root.right = self._delete(root.right,data)
        else:
            if root.left == None: 
                return root.right
            elif root.right == None :
                return root.left
            cur = root.right
            print(cur)
            while cur.left != None:
                cur= cur.left
            print(cur)
            root.data = cur.data
            root.right = self._delete(root.right,root.data)
        return root

            

    def printTree(self,root,level):
        if root is not None:
            self.printTree(root.right,level+1)
            print("      "*level,root.data)
            self.printTree(root.left,level+1)


newbi = BiTree()
list = [6,3,5,1,8,2,9,7]
for i in list :
    newbi.insert(i)
print(list)
newbi.printTree(newbi.root,0)
print("-------------------")
newbi.delete(3)
newbi.printTree(newbi.root,0)


