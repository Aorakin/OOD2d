class Node():
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)
    
class BST():
    def __init__(self):
        self.root = None

    def setLeft(self,left):
        self.left  = left

    def setRight(self,right):
        self.right = right
    
    def insert(self,data):
        self.root = self._insert(self.root,data)

    def _insert(self,root,data):
        if root == None :
            root =  Node(data)
        elif not root.left :
            root.left = self._insert(root.left,data)
        else: 
            root.right = self._insert(root.right,data) 
        return root
    
    def printformat(self):
        self.root =  self._printformat(self.root,0)

    def _printformat(self,root,depth):
        if root != None:
            self._printformat(root.right,depth+1)
            print('     ' *depth,root.data)
            self._printformat(root.left,depth+1)
        return root

    def expressionTree(self,list):
        i = 0
        while len(list) > 1:
            if list[i].data in "+-*/":
                cur = list[i]
                cur.left= list.pop(i-2)
                cur.right = list.pop(i-2)
                i -=2
            else :
                pass
            i+=1
        self.root  = list[0]
        return self.root

    def toInfix(self):
        return self._toInfix(self.root,"")
    
    def _toInfix(self,root,string):
        if root != None:
            left_str = self._toInfix(root.left,string)
            right_str = self._toInfix(root.right,string)
            if left_str and right_str:
                string  = '('+left_str+root.data+right_str+")"
            else:
                string  = left_str+root.data+right_str
        return string
    def toPrefix(self):
        return self._toPrefix(self.root,"")

    def _toPrefix(self,root,string):
        if root!= None:
            string += root.data
            string = self._toPrefix(root.left,string)
            string = self._toPrefix(root.right,string)
        return string
        
new_bi_tree = BST()
inp = input("Enter Postfix : ")
list = []
for i in range(len(inp)):
    list.append(Node(inp[i]))
root  = new_bi_tree.expressionTree(list)
print("Tree : ")
new_bi_tree.printformat()
print("--------------------------------------------------")
print("Infix :",new_bi_tree.toInfix())
print("Prefix :",new_bi_tree.toPrefix())