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
        while cur != None :
            result = result + " " +str(cur.item)
            cur = cur.next
        return result.strip(" ")
    
    def append(self,item):
        new_node = Node(item)
        if self.head == None:
            self.head = self.tail = new_node
        else :
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

            

newlist = linklist()
inp = input("Enter input : ").split(",")
length = len(inp)
dict = {}
for i in range(length) :
    dict[inp[i][:1]] = inp[i][2:]
cur = inp[0][:1]
count = 0
for i in range(length):
    newlist.append(cur)
    dict.pop(cur)


    cur = dict(cur)
print(dict["10"] == None)
