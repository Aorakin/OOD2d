class Node():
    def __init__(self,data):
        self.val = data
        self.next = None
    def __str__(self):
        return str(self.val)
    
inp = [1,2,3,4,2,3,2]
head = last = None
for i in inp:
    new_node = Node(i)
    if head :
        last.next = new_node
        last = last.next
    else :
        last = new_node
        head  = new_node
def partition(head,x):
    if head == None:
        return 
    cur = head
    newcur= temp = newhead = None
    while cur.next != None:
        if cur.val <x  : 
            if temp == None:
                temp = cur
            else:
                temp.next = cur
                temp = temp.next
        else: 
            if newhead == None:
                newhead = cur
                newcur = cur
            else :
                newcur.next = cur
                newcur = newcur.next
        cur = cur.next
    
    if cur.val <x:
        temp.next = cur
        newcur.next =None
    elif cur.val >= x and newcur :
        newcur.next = cur
    elif newcur == None:
        newcur = cur
    # print(head)
    return head
        
link= partition(head,3)
while link != None:
    print(link)
    link = link.next