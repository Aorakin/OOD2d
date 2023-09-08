class Node():
    def __init__(self,item):
        self.item = item
        self.next = None

    def __str__(self):
        return str(self.item)

def createLL(LL):
    head= cur =None
    for i in LL:
        if head == None :
            head = cur = Node(i)
        else:
            cur.next = Node(i)
            cur  = cur.next
    return head

def printLL(head):
    result = ""
    if head !=None:
        cur = head
        while cur != None:
            result = result+" "+str(cur.item)
            cur = cur.next
    return result

def SIZE(head):
    count = 0
    cur = head
    while cur != None :
        cur = cur.next
        count +=1
    return count 
    
def pop(head):
    cur = head
    while cur.next.next != None:
        cur = cur.next
    temp = cur.next
    cur.next = None
    return temp

def Riffle(head,pos,size):
    cur = head
    for i in range(pos-1):
        cur = cur.next
    newhead = cur.next
    cur.next = None
    queue = newhead
    cur = head
    templ1 = templ2 = None
    for i in range(size):
        if cur == None or queue == None :
            break
        templ1 = cur.next
        templ2 = queue.next
        if queue !=None :
            cur.next = queue
        if templ1 != None:
            queue.next = templ1
        queue = templ2
        cur = templ1
    return printLL(head)

def deRiffle(head,pos,size):
    cur= head.next
    temp  = head
    next_list =newhead = head.next
    checkback = 0
    checkfront = 0
    for i in range(1,size+1):
        if (i//2) == (size-pos) and checkfront !=1:
            checkback = 1
        elif (i//2) == pos and checkback!=1:
            checkfront = 1
        if ((i%2 == 1 and i!=1) or checkfront) and checkback ==0:
            next_list.next = cur
            next_list = next_list.next
        elif i%2 ==0 or checkback  : 
            temp.next = cur
            temp = temp.next
        if cur.next == None :
            break
        cur = cur.next
    next_list.next = None
    temp.next = newhead
    return printLL(head)
    
def Bottomup(head,pos,size):
    cur = head           
    for i in range(pos-1):
        cur = cur.next
    temp = cur.next 
    cur.next = None 
    cur = temp
    while cur.next !=None:
        cur = cur.next
    cur.next = head
    head = temp
    return head

def scarmble(head, b, r, size):
    size = SIZE(head)
    formatb = b
    formatr = r
    b = int((b*size)/100)
    r = int((r*size)/100) 
    head = Bottomup(head,b,size)
    print("BottomUp {:.3f} % :{}".format(formatb,printLL(head)))
    print("Riffle {:.3f} % :{}".format(formatr,Riffle(head,r,size)))
    print("Deriffle {:.3f} % :{}".format(formatr,deRiffle(head,r,size)))
    head = Bottomup(head,size-b,size)
    print("Debottomup {:.3f} % :{}".format(formatb,printLL(head)))

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split(" "))
for i in inp2.split('|'):
    print("Start :{0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
