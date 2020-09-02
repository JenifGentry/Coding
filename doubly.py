class Node: # Create the Node class
    def __init__(self, data):
        self.data = data
        self.next=None
        self.prev =None
class doubly_linked_list:   # Create the doubly linked list
    def __init__(self):
        self.head =None
    def push(self,NewVal):  # Adding elements using push
        NewNode=Node(NewVal)
        NewNode.next=self.head
        if self.head is not None:
            self.head.prev =NewNode
            self.head =NewNode
    def listprint(self, node):  # print the linked list 
         print("The doubly linked list is")
         while(node is not None):
            print(node.data)
            last= node
            node = node.next
d_list = doubly_linked_list()
d_list.push(1)
d_list.push(25)
d_list.push(6)
d_list.listprint(d_list.head)


