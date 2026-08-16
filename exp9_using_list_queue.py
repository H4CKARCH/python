class Queue:

    def __init__(self):
        self.Q = []
        self.front = -1
        self.rear = -1
        self.max = 3

    def Enqueue(self):

        if self.front > self.rear:
            self.front = -1
            self.rear = -1
            self.Q = []

        if self.rear == self.max - 1:
            print("Queue is Full")

        else:
            if self.front == -1:
                self.front = 0

            val = input("Enter an Element into Queue: ")

            self.rear = self.rear + 1
            self.Q.append(val)

            print(val, "Inserted successfully into Queue")

    def Dequeue(self):

        if (self.front == -1 and self.rear == -1) or (self.front > self.rear):
            self.front = -1
            self.rear = -1
            self.Q = []

            print("Queue is Empty")

        else:
            val = self.Q[self.front]
            self.Q[self.front] = ""

            self.front = self.front + 1

            print(val, "is deleted successfully")

    def Display(self):

        if (self.front == -1 and self.rear == -1) or (self.front > self.rear):
            self.front = -1
            self.rear = -1
            self.Q = []

            print("Queue is Empty")

        else:
            for i in range(self.front, self.rear + 1):
                print(self.Q[i], "<--", end="")


Qobj = Queue()

while True:

    print("\n**** Operations On Queue ****")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        Qobj.Enqueue()

    elif choice == 2:
        Qobj.Dequeue()

    elif choice == 3:
        Qobj.Display()

    elif choice == 4:
        exit(0)

    else:
        print("Invalid Choice! Try Again")
