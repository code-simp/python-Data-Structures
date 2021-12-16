from Queue import Queue 

class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
class binaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_pre(self,start,traversal):
        if start:
            traversal += (str(start.data) + '-')
            traversal = self.print_pre(start.left,traversal)
            traversal = self.print_pre(start.right,traversal)
        return traversal

    def print_in(self,start,traversal):
        if start:
            traversal = self.print_in(start.left,traversal)
            traversal += (str(start.data) + '-')
            traversal = self.print_in(start.right,traversal)
        return traversal

    def print_post(self,start,traversal):
        if start:
            traversal = self.print_post(start.left,traversal)
            traversal = self.print_post(start.right,traversal)
            traversal += (str(start.data) + '-')
        return traversal

    def output(self,type):
        if type == 'pre':
            print(self.print_pre(self.root,""))
        if type == 'in':
            print(self.print_in(self.root,""))
        if type == 'post':
            print(self.print_post(self.root,""))

    def level_order(self,start):
        if start is None:
            return
        
        queue = Queue()
        queue.enque(start)
        traversal = ''

        while queue.size() > 0:
            traversal += (str(queue.peek()) + '-')
            node = queue.deque()

            if node.left:
                queue.enque(node.left)
            if node.right:
                queue.enque(node.right)

        return traversal


#               1
#           /       \  
#          2          3  
#         /  \      /   \
#        4    5     6   7 


tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.level_order(tree.root))