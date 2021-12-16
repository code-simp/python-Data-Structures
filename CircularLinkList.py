class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Cir_LinkList:
    def __init__(self):
        self.head = None

    def output(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next
            if cur_node == self.head:
                break

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next =self.head
            return
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.next = self.head

    def prepend(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.next =self.head
            return
        cur_node = self.head
        while cur_node.next != self.head:
            cur_node = cur_node.next
        cur_node.next = new_node
        new_node.next = self.head
        self.head = new_node

    def delete(self,key):
        if self.head == None:
            return 
        cur_node = self.head

        while cur_node.next != self.head:
            cur_node = cur_node.next
        prev = cur_node
        cur_node = self.head

        while cur_node.next != self.head:
            if cur_node.data == key and cur_node == self.head:
                prev.next = cur_node.next
                self.head = cur_node.next
                cur_node.next = None
                return
            if cur_node.data == key:
                prev.next = cur_node.next
                cur_node.next = None
                return
            prev = cur_node
            cur_node = cur_node.next

    def delete_at(self,n):
        cur_node = self.head

        while cur_node.next != self.head:
            cur_node = cur_node.next
        prev = cur_node
        cur_node = self.head

        count = 0
        if n == count:
            prev.next = cur_node.next
            self.head = cur_node.next
            cur_node.next = None
            return
        
        cur_node = self.head.next
        prev = self.head

        while cur_node != self.head:
            count += 1
            if count == n:
                prev.next = cur_node.next
                cur_node.next = None
                return
            prev = cur_node
            cur_node = cur_node.next



    def len(self):
        count = 0
        if self.head == None:
            return 0
        cur_node = self.head
        while cur_node.next != self.head:
            count += 1
            cur_node = cur_node.next
        return count+1

    def cur_in_half(self):
        if self.head == None:
            return 0
        if self.len() == 1:
            return self
        print(self.head.data)
        cur_node = self.head.next
        count = 0
        while cur_node != self.head:
            count +=1
            if count < (self.len()//2):
                print(cur_node.data)
                cur_node = cur_node.next
            else:
                break
        
        print('\n\n\n')
                
        while cur_node != self.head:
            print(cur_node.data)
            cur_node = cur_node.next

    def josephus(self,step):
        cur_node = self.head
        length = self.len()
        while length > 1:
            count = 1
            while count != step:
                cur_node = cur_node.next
                count+=1
            print('execute node : ', cur_node.data)
            self.delete_at(cur_node)
            cur_node = cur_node.next
            length -= 1

    def is_circular_linked_list(self, input_list):
        cur_node = input_list.head
        while cur_node.next != input_list.head:
            cur_node = cur_node.next
            if cur_node == None:
                return False
        return True
            


list1 = Cir_LinkList()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.append(7)
list1.append(8)

list1.josephus(2)

    

