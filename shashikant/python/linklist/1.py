class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node("shashikant")
    second = Node(2)
    third = Node(3)
    four = Node(4)

    llist.head.next = second
    second.next = third
    third.next = four
    llist.printList()
