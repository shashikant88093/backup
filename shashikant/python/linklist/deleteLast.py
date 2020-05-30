class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return  length

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def middleInsert(self, newNode, position):
        if position < 0 or position > self.listLength():
            print("invalind position")
            return
        if position is 0:
            self.insertHead(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1

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

    def delete(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None


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
linkedList.insert(thirdNode)
linkedList.delete()
linkedList.printList()
