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
        self.tail = None
        self.size = 0
    def __str__(self):
        cur = self.head
        result = ""
        if cur != None:
            while cur != None:
                result = result + " -> " + str(cur.item)
                cur = cur.next
        return result.strip(" -> ")
    
    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = self.tail = new_node
        else:   
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size+=1
    
    def backward(self):
        pre = self.tail.prev
        pre.next = None
        self.tail = pre
        self.size -=1
        return pre
    
    def reverse(self):
        if self.size == 0:
            return "welcome"
        cur = lasttail = self.tail
        while cur.prev != None:
            cur.next = cur.prev
            cur = cur.prev
        self.head = lasttail
        self.tail = cur
        cur.next = None
        cur = self.head
        while cur.next !=None:
            temp = cur
            cur = cur.next
            cur.prev = temp
        

inp = input("Enter Input : ").split(",")
mainlist=  linklist()
history = linklist()
countB = 0
for i in range(len(inp)):
    if inp[i][0] == 'E':
        mainlist.append(inp[i][2:])
        history.append(inp[i][2:])
    elif inp[i][0] == "B":
        if mainlist.size > 1:
            countB+=1
            history.append(mainlist.backward())
    elif inp[i][0] == "F" and countB != 0:
        cur = history.tail
        if countB == 1:
            cur = cur.prev
        while countB > 1 and cur.prev != None:
            cur = cur.prev
            countB-=1
        countB = 0
        mainlist.append(cur)
        history.append(cur)
mainlist.reverse()
print("History : {0}".format(history))
print("BackPath : {0}".format(mainlist))



