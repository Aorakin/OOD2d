class node(): 
    def __init__ (self,data ,next = None):
        self.data = data
        self.next = next
    
    def __str__(self) -> str:
        return str(self.data)

class linklist():
    def __init__(self,head = None) :
        if head == None :
            self.head = None
        else :
            self.head= head
    
    def __str__(self):
        result = ''
        t = self.head
        while t.next != None:
            result = result+str(t.data)+' <- '
            t = t.next
        result += str(t.data)
        return result.strip(' <- ')
    def append(self,data): 
        newnode = node(data)
        if self.head == None: 
            self.head = newnode
        else : 
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
    def pop(self):
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = None
        return temp.data
    def newTrain(self):
        cur = self.head
        temp = None
        check = 0
        while cur.next != None:
            if cur.next.data == "0":
                if cur.next.next == None :
                    cur.next.next = self.head
                    self.head = cur.next
                    cur.next = None
                    check = 1
                    break
                temp = cur.next
                before_zero = cur.next
                cur.next = None 
                cur = before_zero
            elif temp==None and cur.data == "0":
                check =1 
                break
            else:cur = cur.next
        if not check :
            cur.next = self.head
            self.head  = temp
        
newlist = linklist()
print(" *** Locomotive ***")
train = input("Enter Input : ").split(' ')
for i in train:
    newlist.append(i)
print("Before : {0}".format(newlist))
newlist.newTrain()
print("After : {0}".format(newlist))

            

        