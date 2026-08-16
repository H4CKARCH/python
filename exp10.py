class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None


class SLinkedList:

    def __init__(self):
        self.head = None

    def InsertAtBeg(self, data_in):
        NewNode = Node(data_in)
        NewNode.link = self.head
        self.head = NewNode
        self.TraverseList()

    def InsertAtEnd(self, data_in):
        temp = self.head
        NewNode = Node(data_in)

        if temp is None:
            self.head = NewNode
        else:
            while temp.link is not None:
                temp = temp.link

            temp.link = NewNode

        self.TraverseList()

    # Delete node at beginning
    def RemoveNodeAtBeg(self):
        temp = self.head

        if temp is not None:
            self.head = temp.link
            print(temp.data, "is Deleted from List")
            temp = None
        else:
            print("List is Empty")

    # Delete node at end
    def RemoveNodeAtEnd(self):
        temp = self.head

        if temp is None:
            print("List Empty")

        elif temp.link is None:
            print(temp.data, "is Deleted from List")
            self.head = None
            temp = None

        else:
            while temp.link is not None:
                prev = temp
                temp = temp.link

            print(temp.data, "is Deleted from List")
            prev.link = None
            temp = None

        self.TraverseList()

    # Traverse the linked list
    def TraverseList(self):
        temp = self.head

        if temp is None:
            print("Linked List is Empty")
        else:
            while temp is not None:
                print("-->", temp.data, end="")
                temp = temp.link

            print()

    # Count number of nodes
    def NodeCount(self):
        count = 0
        temp = self.head

        while temp is not None:
            count = count + 1
            temp = temp.link

        return count

    # Insert node at a given position
    def InsertAtPos(self, data_in, pos):
        NewNode = Node(data_in)
        Nc = self.NodeCount()

        if pos < 1 or pos > Nc + 1:
            print("Invalid Position\nTry Again")
            return

        if pos == 1:
            NewNode.link = self.head
            self.head = NewNode

        else:
            cur = self.head
            count = 1

            while count < pos - 1:
                cur = cur.link
                count = count + 1

            NewNode.link = cur.link
            cur.link = NewNode

        self.TraverseList()

    # Delete node at a given position
    def DelAtPos(self, pos):
        Nc = self.NodeCount()

        if Nc == 0:
            print("List is empty")
            print("Deletion Not Possible")

        elif pos < 1 or pos > Nc:
            print("Invalid Position\nTry Again")

        elif pos == 1:
            temp = self.head
            print(temp.data, "is Deleted from List")
            self.head = temp.link
            temp = None

        else:
            cur = self.head
            count = 1

            while count < pos:
                prev = cur
                cur = cur.link
                count = count + 1

            prev.link = cur.link
            print(cur.data, "is Deleted from List")
            cur = None

    # Search for a node
    def search(self, key):
        count = 1
        Loc = -1
        temp = self.head

        if temp is None:
            print("List is Empty")
        else:
            while temp is not None:
                if key == int(temp.data):
                    Loc = count
                    break

                count = count + 1
                temp = temp.link

            if Loc != -1:
                print(key, "Found at Location", Loc)
            else:
                print(key, "Not Found in the List")


# Creating Object to List ADT
llist = SLinkedList()

while True:
    print("\n**** Operations On Single Linked List ***")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete at Beginning")
    print("4. Delete at End")
    print("5. Traverse the List")
    print("6. Node Count")
    print("7. Insert at a Position")
    print("8. Delete at a Position")
    print("9. Search for a Node")
    print("10. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        data = input("Enter a Value: ")
        llist.InsertAtBeg(data)

    elif choice == 2:
        data = input("Enter a Value: ")
        llist.InsertAtEnd(data)

    elif choice == 3:
        llist.RemoveNodeAtBeg()

    elif choice == 4:
        llist.RemoveNodeAtEnd()

    elif choice == 5:
        llist.TraverseList()

    elif choice == 6:
        print("Total nodes in the List:", llist.NodeCount())

    elif choice == 7:
        data = input("Enter a Value: ")
        nCount = llist.NodeCount()

        print("Available maximum position is", nCount + 1)
        pos = int(input("Enter position of insertion: "))

        llist.InsertAtPos(data, pos)

    elif choice == 8:
        pos = int(input("Enter position for Deletion: "))
        llist.DelAtPos(pos)

    elif choice == 9:
        keyVal = int(input("Enter key for searching: "))
        llist.search(keyVal)

    elif choice == 10:
        exit(0)

    else:
        print("Invalid Choice! Try Again")  
