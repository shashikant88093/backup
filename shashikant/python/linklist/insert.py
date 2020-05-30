class Node:

    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        data = input("Add an element:")
        node = Node()
        node.data = data
        node.next = self.head
        self.head = node

    def print(self):
        print_list = self.head
        while print_list:
            print(print_list.data)
            print_list = print_list.next

    def size(self):
        i = 0
        head = self.head
        while head:
            i += 1
            head = head.next
        print(i)


MyList = LinkedList()

while True:
    print("1. Add an element")
    print("2. Print the list")
    print("3. Size of the list")
    menu = int(input("Choose an action:"))

    if menu == 1:
        MyList.insert(1)
    elif menu == 2:
        MyList.print()
    elif menu == 3:
        MyList.size()