class Node:

    def __init__(self, value, nextnode=None):
        self.value = str(value)
        self.nextnode = nextnode

class LinkedList:

    def __init__(self):
        self.num_nodes = 0
        self.firstknownnode = None
        self.lastknownnode = None
        self.showlist = ''

    def insert_at_start(self, node):
        if self.num_nodes == 0:
            self.showlist += (node.value)
            self.num_nodes += 1
            self.lastknownnode = node
            self.firstknownnode = node
        else:
            self.num_nodes += 1
            node.nextnode = self.lastknownnode
            itr = node
            while itr:
                self.showlist = (itr.value + '-->') + self.showlist
                itr = None
                self.lastknownnode = node

    def insert_at_end(self, node):
        if self.num_nodes == 0:
            self.showlist += (node.value)
            self.num_nodes += 1
            self.lastknownnode, self.firstknownnode = node
        else:
            self.num_nodes += 1
            self.firstknownnode.nextnode = node
            self.showlist += ('-->' + node.value)
    
    
    def clearlist(self):
        self.num_nodes = 0
        self.lastknownnode = None
        self.showlist = ''


ll = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(50)
n5 = Node(34)
n6 = Node(100)

ll.insert_at_start(n1)
ll.insert_at_start(n2)
ll.insert_at_start(n3)
ll.insert_at_start(n4)
ll.insert_at_end(n5)
ll.insert_at_end(n6)

print(ll.showlist)


