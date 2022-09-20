#create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create a class to represent your linked list
class Sll:
    def __init__(self):
        self.head = None

    def traverse(self):
        node = self.head
        if node is None:
            print("Empty linked list")
        else:
            while node is not None:
                print(node.data, " ")
                node = node.next


n1 = Node(1)
sll = Sll()
print('---ssl', sll)
sll.head = n1
n2 = Node(2)
print('---n2', n2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
sll.traverse()
