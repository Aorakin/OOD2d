class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)
    
class BinarySearch():
    def __init__(self,root = None):
        self.root = root
    
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

    def inorder(self,root):
        if root == None:
            return 
        self.inorder(root.left)
        print(root,end=" ")
        self.inorder(root.right)
    
    def preorder(self,root):
        if root != None:
            print(root,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
        
    def postorder(self,root):
        if root!= None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root,end=" ")

    def breadth(self,root):
        list = [root]
        result = ""
        while list != []:
            cur = list.pop(0)
            if cur.left :
                list.append(cur.left)
            if cur.right :
                list.append(cur.right)
            result += " " + str(cur.data)
        return result.strip()

        

inp = input("Enter Input : ").split()
newBi =  BinarySearch()   
for i in inp:
    newBi.insert(int(i))
print("Preorder : ",end="")
newBi.preorder(newBi.root)
print("\nInorder : ",end="")
newBi.inorder(newBi.root)
print("\nPostorder : ",end="")
newBi.postorder(newBi.root)
print("\nBreadth : {0}".format(newBi.breadth(newBi.root)))

        