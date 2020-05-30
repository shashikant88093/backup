class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, newNode):

        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node("shashikant")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("chandan")
linkedList.insert(secondNode)
thirdNode = Node("keshav")
linkedList.insertHead(thirdNode)
linkedList.printList()
