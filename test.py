class Solution:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next
        self.head = None
    
    def append(self,data):
        new_node = Solution(data,None)
        if self.head == None:
            self.head = new_node
            return
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = new_node
        return

    def printf(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.val)

list1 = Solution()
list1.append(20)
list1.append(21)
list1.append(22)
list1.append(23)
list1.printf()
