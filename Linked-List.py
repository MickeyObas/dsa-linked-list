# Just me practicing some DSA basics.
# This is an implementation of Linked Lists


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The previous node has to actually exist.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

            
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None



    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data, end= ", ")
            temp = temp.next

l1 = LinkedList()
l1.head = Node("First node")
N1 = Node("First added node")
N2 = Node("Second added node")
N3 = Node("Third added node")

l1.head.next = N1
N1.next = N2
N2.next = N3

l1.push("Pushed some real quick..")
l1.insertAfter(N2, "I'm after N2.")
l1.append("Last boiiiii")

l1.deleteNode("Second added node")

l1.printlist()








