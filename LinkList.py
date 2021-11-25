class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def min_of(item1,item2):
    if item1 == None:
        return item2
    elif item2 == None:
        return item1
    elif item2 == None and item1 == None:
        return None
    elif item1 > item2:
        return item2
    return item1

class LinkList:
    def __init__(self):
        self.head = None

    def output(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next    

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node does not exist.")
            return 

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None 
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return 

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node = None
                return

            prev = None
            count = 1
            while cur_node and count != pos:
                prev = cur_node 
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return 

            prev.next = cur_node.next
            cur_node = None

    def length(self):

        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next
        return count        

    def swap(self,pointer1,pointer2):
        cur_node = self.head
        while cur_node:
            if cur_node.data == pointer1:
                pointer1 = cur_node
            elif cur_node.data == pointer2:
                pointer2 = cur_node
            cur_node = cur_node.next

        temp = pointer1.data
        pointer1.data = pointer2.data
        pointer2.data = temp
        return

    def rev(self):
        prev = None 
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur 
            cur = nxt 
            self.head = prev
    

    def merge(self,link1,link2):
        pointer1 = link1.head
        pointer2 = link2.head
        while pointer1!=None and pointer2!=None:
            temp = min_of(pointer1.data,pointer2.data)
            if temp == pointer1.data:
                pointer1 = pointer1.next
            else:
                pointer2 = pointer2.next
            self.append(temp)

    def remove_duplicate(self):
        dup = []
        cur_node = self.head
        while cur_node:
            if cur_node.data in dup:
                self.delete_node(cur_node.data)
            else:
                dup.append(cur_node.data)
            cur_node = cur_node.next
        print(dup)



list1 = LinkList()
list1.append(20)
list1.append(22)
list1.append(24)    
list1.append(26) 
list1.append(28) 
list1.append(29) 
list1.append(30) 


list2 = LinkList()
list2.append(21)
list2.append(21)
list2.append(23)
list2.append(25)    
list2.append(27) 
list2.append(27) 
list2.append(27) 
list2.append(27) 

list2.output()
print('*     -    *')
list2.remove_duplicate()
list2.output()



