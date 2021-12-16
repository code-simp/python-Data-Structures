# def jump_game(array1):
#     if len(array1) == 0:
#         return False
#     i = 0
#     while True:
#         print( 'index is ' + str(i) ) 
#         diff = (len(array1) - i) - 1
#         count = 0
#         if array1[i] >= diff:
#             return True
#         if array1[i] == 0:
#             return False
#         i += array1[i]
        

# print(jump_game([2,2,3,0,2,4])) 

def sum_two_lists(self, llist):
        result = LinkedList()
        pointer1 = self.head
        pointer2 = llist.head

        if self.len_iterative() > llist.len_iterative():
            while llist.len_iterative != self.len_iterative():
                llist.append(0)

        if self.len_iterative() < llist.len_iterative():
            while self.len_iterative() != llist.len_iterative():
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