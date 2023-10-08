class Node():
    def __init__(self,item):
        self.item = item
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.item)

class linklist():
    def __init__(self):
        self.head = None
        self.tail =None
        self.count_size = 0

    def __str__(self):
        result = ''
        if not self.isEmpty():
            cur = self.head
            while cur != None:
                result = result+" "+str(cur.item)
                cur = cur.next 
        return result.strip(" ")

    def isEmpty(self):
        if self.head ==None:
            return True
        else: return False

    def append(self,item):
        new_node = Node(item)
        if self.head  == None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail 
            self.tail.next =  new_node
            self.tail = new_node
        self.count_size+=1

    def deleteR(self,pos):
        cur = self.head
        if pos > self.count_size:
            pos =self.count_size
        for i in range(pos):
            cur = cur.next
        if cur == None:
            self.count_size+=1
            pass
        elif pos == 0 :
            newhead = cur.next
            self.head = newhead
        else:
            precur = cur.prev
            nextcur = cur.next
            precur.next = nextcur
            if nextcur != None :    
                nextcur.prev = precur
            else :
                self.tail = precur
        self.count_size-=1

    def deleteL(self,pos):
        count = 0
        cur = self.head
        check = 0
        for i in range(pos) :
            if cur.next == None:
                check =1
                break
            cur = cur.next
            count +=1
        if check :
            precur = cur.prev
            precur.next = None
        elif cur.prev == None :
            self.count_size+=1
            pass
        elif cur.prev.prev == None:
            self.head = cur
            cur.prev = None
        else:
            precur = cur.prev.prev
            precur.next = cur
            cur.prev = precur
        self.count_size-=1

    def size(self):
        return self.count_size
    
    def insert(self,pos,item):
        new_node= Node(item)
        if pos > self.count_size:
            pos = self.count_size
        elif pos<0 and abs(pos)<=self.count_size :
            pos = self.size()+pos
            pos = abs(pos)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            cur = self.head
            for i in range(pos):
                if cur == None:
                    break
                cur = cur.next
            if pos == 0 or pos < 0  :
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            elif cur == None: 
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            else:
                precur = cur.prev
                precur.next = new_node
                new_node.next = cur
                new_node.prev = precur
                cur.prev = new_node
        self.count_size+=1

newlinklist = linklist()
Inp = input("Enter Input : ").split(",")
check = 0
count_del = 0
left = right = 0
for i in range(len(Inp)):
    if check and Inp[i] !="L" and Inp[i] != "R" :
        if left > newlinklist.size():
            left = newlinklist.size()
        if right > newlinklist.size():
            right = newlinklist.size()
        count_del = count_del-left+right
        left = 0
        right = 0    
        check = 0 
        
    if Inp[i][:1] == "I":
        newlinklist.insert(count_del,Inp[i][2:])
        count_del+=1
    elif Inp[i] == "B":
        newlinklist.deleteL(count_del)
        if count_del <= 0:
            count_del = 0
        else:
            count_del-=1
        check = 1
    elif Inp[i] == "D":
        newlinklist.deleteR(count_del)
        if count_del >= newlinklist.size():
            count_del = newlinklist.size()
        check = 1
    else:
        if Inp[i] == "L":
            left+=1
            check = 1
        elif Inp[i] == "R":
            right +=1
            check=1
if right != 0  or left != 0 :
    count_del = count_del-left+right
    if count_del > newlinklist.size():
        count_del = newlinklist.size()
    elif count_del<0 :
        count_del = 0 
newlinklist.insert(count_del,"|")
print(newlinklist)    
