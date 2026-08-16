class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class DLinkedList:

    def __init__(self):
        self.head = None

    # Insert at beginning
    def InsertAtBeg(self, data_in):
        NewNode = Node(data_in)

        NewNode.next = self.head

        if self.head is not None:
            self.head.prev = NewNode

        self.head = NewNode

        self.DisplayList()

    # Insert at end
    def InsertAtEnd(self, data_in):
        NewNode = Node(data_in)

        if self.head is None:
            self.head = NewNode
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = NewNode
            NewNode.prev = temp

        self.DisplayList()

    # Delete from beginning
    def RemoveNodeAtBeg(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        print(temp.data, "is Deleted from List")

        self.head = temp.next

        if self.head is not None:
            self.head.prev = None

        temp = None

        self.DisplayList()

    # Delete from end
    def RemoveNodeAtEnd(self):
        if self.head is None:
            print("List is Empty")
            return

        temp = self.head

        if temp.next is None:
            print(temp.data, "is Deleted from List")
            self.head = None
        else:
            while temp.next is not None:
                temp = temp.next

            print(temp.data, "is Deleted from List")

            temp.prev.next = None
            temp = None

        self.DisplayList()

    # Display list
    def DisplayList(self):
        temp = self.head

        if temp is None:
            print("Doubly Linked List is Empty")
        else:
            while temp is not None:
                print("<==>", temp.data, end="")
                temp = temp.next

            print()

    # Count nodes
    def NodeCount(self):
        count = 0
        temp = self.head

        while temp is not None:
            count = count + 1
            temp = temp.next

        return count

    # Insert at position
    def InsertAtPos(self, data_in, pos):
        NewNode = Node(data_in)
        Nc = self.NodeCount()

        if pos < 1 or pos > Nc + 1:
            print("Invalid Position\nTry Again")
            return

        # Insert at beginning
        if pos == 1:
            NewNode.next = self.head

            if self.head is not None:
                self.head.prev = NewNode

            self.head = NewNode

        else:
            cur = self.head
            count = 1

            while count < pos - 1:
                cur = cur.next
                count = count + 1

            NewNode.next = cur.next
            NewNode.prev = cur

            if cur.next is not None:
                cur.next.prev = NewNode

            cur.next = NewNode

        self.DisplayList()

    # Delete at position
    def DelAtPos(self, pos):
        Nc = self.NodeCount()

        if Nc == 0:
            print("List is empty")
            return

        if pos < 1 or pos > Nc:
            print("Invalid Position\nTry Again")
            return

        # Delete first node
        if pos == 1:
            temp = self.head

            print(temp.data, "is Deleted from List")

            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

            temp = None

        else:
            cur = self.head
            count = 1

            while count < pos:
                cur = cur.next
                count = count + 1

            print(cur.data, "is Deleted from List")

            cur.prev.next = cur.next

            if cur.next is not None:
                cur.next.prev = cur.prev

            cur = None

        self.DisplayList()

    # Search
    def search(self, key):
        count = 1
        Loc = -1
        temp = self.head

        if temp is None:
            print("List is Empty")
            return

        while temp is not None:
            if key == int(temp.data):
                Loc = count
                break

            count = count + 1
            temp = temp.next

        if Loc != -1:
            print(key, "Found at Location", Loc)
        else:
            print(key, "Not Found in the List")


# Creating Object
dll = DLinkedList()

while True:

    print("\n**** Operations On Doubly Linked List ****")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete at Beginning")
    print("4. Delete at End")
    print("5. Display")
    print("6. Node Count")
    print("7. Insert at a Position")
    print("8. Delete at a Position")
    print("9. Search for a Node")
    print("10. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        data = input("Enter a Value: ")
        dll.InsertAtBeg(data)

    elif choice == 2:
        data = input("Enter a Value: ")
        dll.InsertAtEnd(data)

    elif choice == 3:
        dll.RemoveNodeAtBeg()

    elif choice == 4:
        dll.RemoveNodeAtEnd()

    elif choice == 5:
        dll.DisplayList()

    elif choice == 6:
        print("Total nodes in the List:", dll.NodeCount())

    elif choice == 7:
        data = input("Enter a Value: ")

        nCount = dll.NodeCount()

        print("Available maximum position is", nCount + 1)

        pos = int(input("Enter position of insertion: "))

        dll.InsertAtPos(data, pos)

    elif choice == 8:
        pos = int(input("Enter position for Deletion: "))

        dll.DelAtPos(pos)

    elif choice == 9:
        keyVal = int(input("Enter key for searching: "))

        dll.search(keyVal)

    elif choice == 10:
        exit(0)

    else:
        print("Invalid Choice! Try Again")
