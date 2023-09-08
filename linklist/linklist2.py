class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.checksize =0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        new_node = Node(item)
        if self.tail == None:
            self.head = self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.checksize +=1

    def addHead(self, item):
        new_node = Node(item)
        if self.head == None :
            self.head = self.tail = new_node
        else : 
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.checksize+=1

    def insert(self, pos, item):
        new_node = Node(item)
        cur = self.head
        count = 0
        if pos<0:
            pos = self.size()+pos
            pos = abs(pos)
        pos = pos%(self.checksize+1)
        while count < pos :
            count += 1
            cur = cur.next
        if self.head  == None:
            self.head = self.tail = new_node
        elif self.checksize == count or self.checksize ==1:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail =new_node    
        elif cur.previous!= None :
            temp = cur.previous
            temp.next = new_node
            new_node.next = cur
            new_node.previous = temp
            cur.previous = new_node
        else: 
            cur.previous = new_node
            new_node.next = cur
            self.head =new_node
        self.checksize+=1

    def search(self, item):
        cur = self.head
        while cur.value!=item:
            if cur.next == None:
                return "Not Found"
            cur = cur.next
            
        return "Found"
        
    def index(self, item):
        cur = self.head
        count = 0
        if self.search(item) == "Not Found":
            return -1
        while cur.value!=item:
            count+=1
            cur = cur.next
        return count

    def size(self):
        return self.checksize

    def pop(self, pos):
        if self.checksize == 0  or pos > self.checksize-1 :
            return "Out of Range"
        if pos<0:
            pos = -pos
        count = 0
        cur = self.head
        temp = None
        while count < pos:
            count+=1
            cur = cur.next
        if cur.previous == None:
            if cur.next == None :
                self.head = self.tail =  None
                temp = cur.value
            else:
                temp = cur.next
                cur.next = None
                self.head = temp
        elif cur.next == None:
            temp = cur.previous
            temp.next = None
            self.tail = temp
        else :
            temp = cur.previous
            temp.next = cur.next
            cur.next = cur.previous = None
        self.checksize-=1
        if self.checksize == 1:
            self.tail = self.head = temp
        return "Success"
        

            


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{0}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
