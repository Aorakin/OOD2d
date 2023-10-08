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

    def findparent(self,root,son):
        if root and (root.left == son or root.right ==son):
            return root
        elif not root :
            return 
        temp = self.findparent(root.left,son)
        if temp:
            return temp
        temp2 = self.findparent(root.right,son)
        if temp2 :
            return temp2
        
    def getbarance(self,root):
        if root:
            return self.get_height(root.left) - self.get_height(root.right)
        return 0
    
    def get_height(self,root):
        if root :
            return root.height
        return 0 
        
    def findroot(self,num):
        return self._findroot(self.root,num)
    
    def _findroot(self,root,num):
        if root :
            if root.data == num :
                return root
            temp1 = self._findroot(root.left,num)
            temp2 = self._findroot(root.right,num)
            if temp1 : 
                return temp1
            elif temp2 :
                return temp2
            else:
                return None
    
    def family(self,root,list):
        if root == None:
            return []
        list=self.family(root.left,list)
        list.append(root)
        list+=self.family(root.right,list)
        return list

    def fire(self,root):
        queue = [root]
        used = [root]
        while  queue:
            for i in range(len(queue)):
                if not queue:
                    break
                temp = queue.pop(0)
                Papa = self.findparent(self.root,temp)
                if  temp.left and temp.left not in used:
                    queue.append(temp.left)
                    used.append(temp.left)
                if  temp.right and temp.right not in used:
                    queue.append(temp.right)
                    used.append(temp.right)
                if  Papa and Papa not in used:
                    queue.append(Papa)
                    used.append(Papa)
                print(temp.data,end = " ")
            print("")

newAVL = AVL()
inp = input("Enter node and burn node : ").split("/")
datalist = inp[0].split(" ")
for i in datalist:
    newAVL.insert(int(i))
findroot = newAVL.findroot(int(inp[1]))
if findroot == None:
    print("There is no {0} in the tree.".format(inp[1]))
else:
    newAVL.fire(newAVL.findroot(int(inp[1])))

