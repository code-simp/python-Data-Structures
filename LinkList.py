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

    def nth_to_last(self,input):
        cur_node = self.head
        count = 0
        incr=0
        while cur_node:
            count+=1
            if count > input:
                incr+=1
            cur_node = cur_node.next
        return incr

    def move_tail_to_head(self):
        cur_node = self.head
        while cur_node.next:
            if cur_node.next.next == None:
                this = cur_node
            cur_node = cur_node.next
        cur_node.next = self.head
        self.head = cur_node
        this.next = None

    def sum_two_lists(self, llist):
        result = LinkList()
        pointer1 = self.head
        pointer2 = llist.head

        if self.length() > llist.length():
            while llist.length() != self.length():
                llist.append(0)

        if self.length() < llist.length():
            while self.length() != llist.length():
                self.append(0)

        while pointer1!=None and pointer2 != None:
            sum = pointer1.data + pointer2.data
            if sum >= 10:
                remain = sum - 10
                pointer2.next.data += 1
                result.append(remain)
            else:
                result.append(sum)
            pointer1 = pointer1.next
            pointer2 = pointer2.next    
            
        return result

    def pairs_with_sum(self, sum_val):  
        result = []
        cur_node = self.head
        while cur_node:
            pointer1 = cur_node.data
            p2 = cur_node
            while p2:
                if p2.data == sum_val - pointer1:
                    result.append('(' + str(pointer1)+','+ str(p2.data) + ')')
                p2 = p2.next
            cur_node = cur_node.next
        return result



list1 = LinkList()
list1.append(4)
list1.append(9)    


list2 = LinkList()

list3 = LinkList()

list3 = list2.sum_two_lists(list1)
list3.output()



