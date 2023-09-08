class Node():
    def __init__(self,item):
        self.data = item
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)

class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        result = ''
        if not self.isEmpty():
            cur = self.head
            while cur != None:
                result = result+" "+str(cur.data)
                cur = cur.next 
        return result.strip(",")

    def isEmpty(self):
        if self.head == None:
            return True
        else : False

    def append(self,item):
        new_node =Node(item)
        if self.head == None :
            self.head = self.tail  = new_node
        else: 
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail =new_node
        self.size +=1
    
    def reverse(self):
        cur = temp =self.tail
        lasttail = self.tail
        while cur.prev != None:
            cur.next = cur.prev
            cur = cur.prev
        self.head = lasttail
        self.tail = cur
        cur.next = None
        cur  = self.head
        while cur.next != None:
            if cur.next != None:
                temp =cur.next
            temp.prev = cur
            cur = cur.next


newlinklist1 = Linklist()
newlinklist2 = Linklist()
newlist = input("Enter Input (L1,L2) : ").split(" ")
L1,L2= newlist[0].split("->"),newlist[1].split("->")
for i in L1:
    newlinklist1.append(i)
for j in L2:
    newlinklist2.append(j)
print("L1    :{0}".format(newlinklist1))
print("L2    :{0}".format(newlinklist2))
newlinklist2.reverse()
print("Merge :{0}{1}".format(newlinklist1,newlinklist2))