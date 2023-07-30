class LinkedList :
    def __init__(self,head = None):
        if head ==None :
            self.head = self.tail = None
            self.size = 0
    def append(self,data):
        temp = Node(data)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else :
            self.tail.next = temp
            self.tail = temp
        self.size+=1
        return temp
    
    def insert(self,pos,data):
        newnode = Node(data)
        temp = self.head
        count = 1
        while count != pos:
            count +=1
            if count == pos :
                newnode.next = temp.next
                temp.next = newnode
            temp = temp.next


    def __str__(self):
        temp = ''
        cur = self.head
        while cur != None:
            temp = temp+","+str(cur.data)
            cur = cur.next
        return temp[1:]

class Node : 
    def __init__ (self,data ,next = None):
        self.data = data
        if next != None:
            self.next = next
        else : self.next = None
    
    def __str__(self):
        return str(self.data)

newLinkedList = LinkedList()
for i in range(10):
    newLinkedList.append(i)
newLinkedList.insert(3,40)
print(newLinkedList)
