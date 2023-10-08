class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def father(r,data):
    if r.data == data:
        return r
    elif not r.left and  not r.right:
        return None
    elif data < r.data:
        check  = father(r.left,data)
    else:
        check = father(r.right,data)
    if check and check.data == data:
        return r
    else:
        return check


tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
find_father = father(tree.root,data[1])
if tree.root.data == data[1]:
    print("None Because {} is Root".format(data[1]))
elif find_father == None:
    print("Not Found Data")
else:
    print(find_father)