class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.prev = cur_node

    def prepend(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.prev:
            cur_node = cur_node.prev
        cur_node.prev = new_node
        new_node.next = cur_node
        self.head = new_node

    def output(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next  
              
    def add_after(self,key,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                new_node.next = cur_node.next
                if cur_node.next != None:
                    cur_node.next.prev = new_node
                cur_node.next = new_node
                new_node.prev = cur_node
                return
            cur_node = cur_node.next

    def add_before(self,key,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                if cur_node.prev != None:
                    new_node.prev = cur_node.prev
                    cur_node.prev.next = new_node
                cur_node.prev = new_node
                new_node.next = cur_node
                self.head = new_node
            cur_node = cur_node.next       

    def remove(self,key):
        #case 1
        if self.head == None:
            return 0

        #case 2
        if key == self.head.data:
            cur_node = self.head
            if self.head.next == None:
                self.head = None
                return
            self.head = cur_node.next
            self.head.prev = None

        
        #case 3
        cur_node = self.head
        while cur_node:
            if cur_node.data == key:
                if cur_node.next != None:
                    cur_node.next.prev = cur_node.prev
                if cur_node.next != None:    
                    cur_node.prev.next = cur_node.next
                else:
                    cur_node.prev.next = None
                cur_node = None
                return
            cur_node = cur_node.next

    def rev(self):
        temp = None
        cur_node = self.head
        while cur_node:
            temp = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = temp
            cur_node = cur_node.prev
        if temp:
            self.head = temp.prev

    


dlist = DoublyLinkList()

dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)
dlist.prepend(0)
dlist.rev()

dlist.output()
        
        