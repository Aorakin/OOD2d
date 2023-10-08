class Queue:
    def __init__(self) -> None:
        self.items = []
    def deQueue(self):
        return self.items.pop(0)
    def enQueue(self,i):
        self.items.append(i)
    def peek(self):
        return self.items[0]
    def isEmpty(self):
        return len(self.items)==0

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

def find_parent(root,node):
    if root!= None:
        if (root.right != None and root.right == node) or (root.left != None and root.left == node):
            return root
        elif int(root.data) >= int(node.data):
            return find_parent(root.left,node)
        elif int(root.data) < int(node.data):
            return find_parent(root.right,node)
        
def find_index(root,data):
    if root!= None:
        if int(root.data) == data:
            return root
        elif int(root.data) > data:
            return find_index(root.left,data)
        elif int(root.data) < data:
            return find_index(root.right,data)
        
def burn(root,data):
    Q = Queue()
    check_lst = []
    burn_node = find_index(root,data)
    print(burn_node)
    Q.enQueue(burn_node)
    while not Q.isEmpty():
        for i in range(len(Q.items)):
            burn_node = Q.deQueue()
            check_lst.append(burn_node)
            parent_node = find_parent(root,burn_node)
            if burn_node.left != None and burn_node.left not in check_lst:
                Q.enQueue(burn_node.left)
                check_lst.append(burn_node.left)
            if burn_node.right != None and burn_node.right not in check_lst:
                Q.enQueue(burn_node.right)
                check_lst.append(burn_node.right)
            if parent_node != None and parent_node not in check_lst:   
                Q.enQueue(parent_node)
                check_lst.append(parent_node)
            print(burn_node.data,end=' ')
        print()

T = AVL()
inp = input("Enter node and burn node : ").split('/')
n = inp[0].split()
root = None
if inp[1] not in n:
    print(f'There is no {inp[1]} in the tree.')
else:
    for i in n:
        T.insert(int(i))

    T.printTree(T.root)
    burn(T.root,int(inp[1]))