class Node():
    def __init__(self,item = None):
        self.item = item
        self.next = None
    def __str__(self):
        return str(self.item)
    
class linklist():
    def __init__(self):
        self.head = None
        self.size = 0

    def __str__(self):
        cur = self.head
        string = ""
        while cur != None :
            string +=str(cur.item) + " "
            cur = cur.next
        return string.strip(" ")
    
    def append(self,item):
        newNode = Node(item)
        if self.head == None:
            self.head = newNode
        else : 
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = newNode
        self.size +=1
    def pop(self,index = None):
        if self.size ==1:
            temp  = self.head.val
            self.head = None
            return temp
        elif self.size == 0 :
            return "kuay"
        else:
            cur = self.head
        if index == None:
            while index == None and cur.next.next != None:
                cur = cur.next
            num = cur.next
            cur.next = None
            
        else:
            if index == 0 :
                num = self.head
                self.head = self.head.next
                return num
            for i in range(index-1):
                cur = cur.next
            num = cur.next
            cur.next  = cur.next.next
        self.size -= 1
        return num
    
    def insert(self,data,pos):
        newnode = Node(data)
        if self.head == None :
            self.head = newnode
        if abs(pos) >= self.size :
            if pos <0:
                pos = 0
            else:  
                pos = self.size
        if pos == 0:
            newnode.next = self.head
            self.head = newnode
        else :
            cur = self.head
            if pos < 0 : 
                pos = self.size+pos
            for i in range(pos-1):
                cur = cur.next
            newnode.next  = cur.next
            cur.next = newnode


fah = "abse"
def ijiof():
    global fah
    fah = fah[1:]
    return fah
print(ijiof())
newlinklist = linklist()
for i in [1,2,3,5,4,6,8]:
    newlinklist.append(i)
newlinklist.insert(100,-7)
print(newlinklist)