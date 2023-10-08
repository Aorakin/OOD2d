class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class AVL():
    def __init__(self):
        self.root = None

    def height(self,root):
        if not root:
            return 0
        return 1 + max(self.height(root.right),self.height(root.left))
        
    def insert(self,data):
        self.root = self._insert(self.root,data)
    
    def _insert(self,root,data):
        if not root:
            return Node(data)
        elif data < root.data:
            root.left = self._insert(root.left,data)
        else:
            root.right = self._insert(root.right,data)
        # barance = self.height(root.left) - self.height(root.right)
        # if barance <-1 and data > root.right.data:
        #     root = self.rotateLeft(root)
        # elif barance >1 and data < root.left.data:
        #     root = self.rotateRight(root)
        # elif barance <-1 and data < root.right.data:
        #     root.right = self.rotateRight(root.right)
        #     return self.rotateLeft(root)
        # elif barance >1 and data > root.left.data:
        #     root.left = self.rotateLeft(root.left)
        #     return self.rotateRight(root)
        return root 

    def ranking(self,num):
        if num < self.root.data and not self.root.left:
            return 0
        return self._ranking(self.root,num,0)

    def _ranking(self,root,num,count):
        if not root :
            return 0
        count = self._ranking(root.left,num,count)
        if root.data == num :
            return count+1
        elif num < root.data or (num  < root.data and num > root.left.data) :
            return count
        else :
            count +=1
            count += self._ranking(root.right,num,count)
        return count

    def rotateRight(self,root):
        temp = root.left
        root.left = temp.right
        temp.right = root
        return temp
    
    def rotateLeft(self,root):
        temp = root.right
        root.right = temp.left
        temp.left = root
        return temp
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
newAVL = AVL()
inp = input("Enter Input : ").split("/")
newinp = inp[0].split(" ")
for i in newinp:
    newAVL.insert(int(i))
newAVL.printTree(newAVL.root)
print("--------------------------------------------------")
print("Rank of {0} : {1}".format(inp[1],newAVL.ranking(int(inp[1]))))