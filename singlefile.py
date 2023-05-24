class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertionAtStart(self, newItem):
        newNode = Node(newItem)
        newNode.next = self.head
        self.head = newNode

    def insertionAtEnd(self, newItem):
        newNode = Node(newItem)
        if self.head is None:
            return newNode
        else:
            lastNode = self.head
            while lastNode.next:
                lastNode = lastNode.next
            lastNode.next = newNode

    def insertionAtMiddle(self, middleNode, newItem):
        if middleNode is None:
            print("Middle node is absent")
            return
        else:
            newNode = Node(newItem)
            newNode.next = middleNode.next
            middleNode.next = newNode

linked_list = LinkedList()
linked_list.head = first = Node("Madhu")
second = Node("RLT")
third = Node("Sravan")
first.next = second
second.next = third

linked_list.insertionAtStart("Venkat")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head = linked_list.head.next

linked_list = LinkedList()
linked_list.head = first = Node("Madhu")
second = Node("RLT")
third = Node("Sravan")
first.next = second
second.next = third

linked_list.insertionAtEnd("Pavan")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head = linked_list.head.next

linked_list = LinkedList()
linked_list.head = first = Node("Madhu")
second = Node("RLT")
third = Node("Sravan")
first.next = second
second.next = third

linked_list.insertionAtMiddle(second, "Venkat")

while linked_list.head:
    print(linked_list.head.item)
    linked_list.head = linked_list.head.next
