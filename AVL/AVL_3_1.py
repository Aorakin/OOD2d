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
        cur = [root]
        nextparent = self.findparent(self.root,root)
        if nextparent != None:
            secqueue = [nextparent]
            seccur = [nextparent]
        else:
            secqueue = []
            seccur = []
        while cur != [] or seccur != []:
            if cur:
                temp = cur.pop(0)
                if temp == None:
                    pass
                else:
                    cur +=[temp.left,temp.right]
                    queue += [temp.left,temp.right]
            if seccur:
                newtemp = seccur.pop(0)
                if newtemp !=None:
                    if newtemp not in secqueue and newtemp != root :
                        seccur.append(newtemp)
                        secqueue.append(newtemp)
                    if (newtemp.left != root and newtemp.left not in secqueue) or newtemp.left == None:
                        if newtemp.left != None:
                            seccur += [newtemp.left]
                        secqueue +=[newtemp.left]
                    if (newtemp.right != root and newtemp.right not in secqueue) or newtemp.right == None:
                        if newtemp.right != None:
                            seccur += [newtemp.right]
                        secqueue +=[newtemp.right]
                    parent = self.findparent(self.root,newtemp) 
                if parent :
                    seccur+=[parent]
                    if parent not in secqueue:
                        secqueue+=[parent]
        k =2
        temp = queue.pop(0)
        check = 0
        print(temp)
        count = clear  = 1
        clearNone = 0
        LR = None 
        for i in secqueue:
            if i :
                print(i.data,end=" ")
            else:print(None,end=" ")
        print("------")
        while queue or secqueue:
            if queue:
                for i in range(k):
                    if queue==[]:
                        break
                    front = queue.pop(0)
                    if front != None:
                        print(front,end=" ")
                    else:
                        continue
                    if i == k-1 and secqueue == []:
                        print("")
            if secqueue:
                if check :
                    if clearNone:
                        for i in range(clear):
                            secqueue.pop(0)
                        clearNone = 0
                    for i in range(count):
                        if secqueue == []:
                            break
                        if (secqueue[0] and LR and secqueue[0].data >=self.root.data and LR.data >= self.root.data ):
                            who = secqueue.pop(0)
                            who2 =None 
                            if secqueue[0] and LR and secqueue[0].data>=self.root.data and LR.data >= self.root.data:
                                print(secqueue[0])
                                who2 = secqueue.pop(0)
                            if who:
                                print(who,end=" ")
                            if who2:
                                print(who2,end= " ")
                                clear = 2
                            if who and who.left == None  and who.right == None:
                                clearNone = 1
                            elif who2 and who2.left == None  and who2.right == None:
                                clearNone = 1
                        checkNone = secqueue.pop(0)
                        if checkNone :
                            print(checkNone,end=" ")
                        if (i == count-1 and secqueue!=[] )  :    
                            print("")
                    count*=2
                    clear*=2
                elif secqueue[0] == self.findparent(self.root,root):
                    if secqueue[0] == self.root:
                        check = 1
                    print(secqueue.pop(0))
                else:
                    LR = secqueue.pop(0)
                    if secqueue:
                        Papa = secqueue.pop(0)
                    if LR :
                        print(LR,end=" ")
                    if Papa :
                        print(Papa)
                        if Papa == self.root:
                            check = 1   
                            while secqueue[0] == None :
                                if secqueue[0] == None:
                                    secqueue.pop(0) 
            k*=2
            

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
newAVL.printTree(newAVL.root)

